"""Stage 1 - subject runs: one API call per (item, condition), all in parallel
under a semaphore. Answers are appended to answers.jsonl as they land, so an
interrupted run resumes by skipping keys already present.
"""
from __future__ import annotations

import asyncio
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from .client import Client
from .config import Config
from .pool import load_pool, pool_hash
from .prompts import PROMPT_VERSION, subject_messages
from .store import JsonlStore, index_key, load_index, run_dir, save_index

_CONF_RE = re.compile(r"CONFIDENCE[:\s]*([0-9]{1,3})", re.IGNORECASE)


def parse_confidence(text: str) -> int | None:
    matches = _CONF_RE.findall(text)
    if not matches:
        return None
    val = int(matches[-1])
    return val if 0 <= val <= 100 else None


async def run_subjects(
    cfg: Config,
    model: str,
    conditions: list[str],
    limit: int | None = None,
    force: bool = False,
) -> Path:
    items = load_pool(cfg.pool_path)
    if limit:
        items = items[:limit]
    sha = pool_hash(cfg.pool_path)
    rd = run_dir(cfg.runs_dir, sha, model, PROMPT_VERSION)
    rd.mkdir(parents=True, exist_ok=True)

    store = JsonlStore(rd / "answers.jsonl", ("item_id", "condition"))
    todo = [
        (it, cond)
        for cond in conditions
        for it in items
        if force
        or not store.has(it["id"], cond)
        or store.get(it["id"], cond).get("error")  # errored answers are retried
    ]
    print(f"[{model}] {len(store)} answers on disk; {len(todo)} calls to make "
          f"({len(items)} items x {len(conditions)} conditions)")

    manifest_path = rd / "manifest.json"
    manifest = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update({
        "model_requested": model,
        "pool_path": str(cfg.pool_path),
        "pool_sha256": sha,
        "prompt_version": PROMPT_VERSION,
        "temperature": cfg.temperature,
        "subject_max_tokens": cfg.subject_max_tokens,
        "conditions": sorted(set(manifest.get("conditions", [])) | set(conditions)),
        "started_at": manifest.get("started_at") or datetime.now(timezone.utc).isoformat(),
    })
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    if todo:
        client = Client(cfg)
        sem = asyncio.Semaphore(cfg.concurrency)
        done = 0

        async def one(item: dict, cond: str) -> None:
            nonlocal done
            async with sem:
                try:
                    comp = await client.complete(
                        model, subject_messages(item, cond), cfg.subject_max_tokens
                    )
                    if not comp.text:
                        raise RuntimeError("empty completion after retries")
                    store.append({
                        "item_id": item["id"],
                        "condition": cond,
                        "model_requested": model,
                        "model_returned": comp.model_returned,
                        "text": comp.text,
                        "confidence": parse_confidence(comp.text),
                        "prompt_tokens": comp.prompt_tokens,
                        "completion_tokens": comp.completion_tokens,
                        "latency_s": comp.latency_s,
                        "attempts": comp.attempts,
                        "error": None,
                    })
                    if "model_returned" not in manifest:
                        manifest["model_returned"] = comp.model_returned
                except Exception as e:  # noqa: BLE001 - record and continue
                    store.append({
                        "item_id": item["id"],
                        "condition": cond,
                        "model_requested": model,
                        "model_returned": None,
                        "text": "",
                        "confidence": None,
                        "prompt_tokens": None,
                        "completion_tokens": None,
                        "latency_s": None,
                        "attempts": cfg.max_attempts,
                        "error": f"{type(e).__name__}: {e}",
                    })
                    print(f"  !! {item['id']} ({cond}) failed: {e}")
                done += 1
                if done % 20 == 0:
                    print(f"  ... {done}/{len(todo)}")

        await asyncio.gather(*(one(it, c) for it, c in todo))

    manifest["updated_at"] = datetime.now(timezone.utc).isoformat()
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    expected = len(items) * len(conditions)
    errors = sum(1 for r in store.rows.values() if r.get("error"))
    complete = len(store) >= expected and errors == 0
    index = load_index(cfg.runs_dir)
    index[index_key(sha, model, PROMPT_VERSION)] = {
        "run_dir": str(rd),
        "answers": len(store),
        "expected": expected,
        "errors": errors,
        "complete": complete,
        "updated_at": manifest["updated_at"],
    }
    save_index(cfg.runs_dir, index)
    print(f"[{model}] done: {len(store)}/{expected} answers, {errors} errors -> {rd}")
    return rd
