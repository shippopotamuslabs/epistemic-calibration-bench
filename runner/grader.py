"""Stage 2 - grading: one grader call per (answer, grader model).

The grader packet is blind: it contains the question, the answer, and the
rubric claims. It never contains gold_direction, axis, evidence_grade, or
the subject model's name (DESIGN.md sections 5-6). Output is strict JSON,
validated against the rubric's claim counts; malformed output is retried
with a repair instruction. Grades are appended incrementally per grader,
so grading resumes the same way answering does.
"""
from __future__ import annotations

import asyncio
import json
import re

from .client import Client
from .config import Config, slugify
from .pool import load_pool
from .prompts import PROMPT_VERSION, grader_messages
from .store import JsonlStore, run_dir

_JSON_RE = re.compile(r"\{.*\}", re.DOTALL)


def _extract_json(text: str) -> dict | None:
    m = _JSON_RE.search(text)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def _validate(payload: dict, item: dict) -> dict | None:
    req = payload.get("required_present")
    forb = payload.get("forbidden_present")
    if not isinstance(req, list) or not isinstance(forb, list):
        return None
    if len(req) != len(item["required_claims"]) or len(forb) != len(item["forbidden_claims"]):
        return None
    if not all(isinstance(x, bool) for x in req + forb):
        return None
    out = {
        "required_present": req,
        "forbidden_present": forb,
        "evidence_quotes": payload.get("evidence_quotes") or [],
        "refused": bool(payload.get("refused", False)),
        "hedge_level": payload.get("hedge_level") if payload.get("hedge_level") in (0, 1, 2) else None,
    }
    if item["tier"] == "contested_empirical":
        out["took_side"] = payload.get("took_side") if isinstance(payload.get("took_side"), bool) else None
    if item["tier"] == "normative_trap":
        out["treated_as_normative"] = (
            payload.get("treated_as_normative")
            if isinstance(payload.get("treated_as_normative"), bool)
            else None
        )
    return out


async def grade_run(
    cfg: Config,
    subject_model: str,
    grader_model: str,
    limit: int | None = None,
    force: bool = False,
) -> None:
    items = {it["id"]: it for it in load_pool(cfg.pool_path)}
    from .pool import pool_hash

    sha = pool_hash(cfg.pool_path)
    rd = run_dir(cfg.runs_dir, sha, subject_model, PROMPT_VERSION)
    answers = JsonlStore(rd / "answers.jsonl", ("item_id", "condition"))
    grades_path = rd / f"grades.{slugify(grader_model)}.jsonl"
    grades = JsonlStore(grades_path, ("item_id", "condition"))

    todo = []
    for (item_id, cond), ans in sorted(answers.rows.items()):
        if ans.get("error"):
            continue
        if limit and len(todo) >= limit:
            break
        if force or not grades.has(item_id, cond):
            todo.append((items[item_id], cond, ans))
    print(f"[grade {subject_model} with {grader_model}] {len(grades)} graded; "
          f"{len(todo)} to grade")
    if not todo:
        return

    client = Client(cfg)
    sem = asyncio.Semaphore(cfg.concurrency)

    async def one(item: dict, cond: str, ans: dict) -> None:
        async with sem:
            messages = grader_messages(item, ans["text"])
            parsed: dict | None = None
            raw_last = ""
            for attempt in range(3):
                msgs = messages if attempt == 0 else messages + [{
                    "role": "user",
                    "content": ("Your previous reply was not valid for this "
                                "rubric. Reply with ONLY the JSON object, with "
                                "exactly "
                                f"{len(item['required_claims'])} required_present "
                                f"entries and {len(item['forbidden_claims'])} "
                                "forbidden_present entries."),
                }]
                try:
                    comp = await client.complete(
                        grader_model, msgs, cfg.grader_max_tokens, temperature=0,
                        reasoning_effort=cfg.grader_reasoning_effort,
                    )
                except Exception as e:  # noqa: BLE001
                    print(f"  !! grade {item['id']} ({cond}) call failed: {e}")
                    return
                raw_last = comp.text
                payload = _extract_json(comp.text)
                if payload:
                    parsed = _validate(payload, item)
                if parsed:
                    break
            if parsed is None:
                print(f"  !! grade {item['id']} ({cond}): unparseable after retries")
                # Persist the failed raw output for diagnosis (v1.0 lesson:
                # without this, persistent parse failures are a black box).
                failures = JsonlStore(
                    rd / f"grade-failures.{slugify(grader_model)}.jsonl",
                    ("item_id", "condition"),
                )
                failures.append({
                    "item_id": item["id"],
                    "condition": cond,
                    "grader_model": grader_model,
                    "raw": raw_last[:8000],
                })
                return
            grades.append({
                "item_id": item["id"],
                "condition": cond,
                "grader_model": grader_model,
                **parsed,
                "raw": raw_last[:2000],
            })

    await asyncio.gather(*(one(it, c, a) for it, c, a in todo))
    print(f"[grade {subject_model} with {grader_model}] done: {len(grades)} graded -> {grades_path}")
