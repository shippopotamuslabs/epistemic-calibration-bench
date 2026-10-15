"""CLI: python -m runner {run|grade|score|all|status|selftest}

Stage flags:
  --model SLUG        subject model (default: every model in config)
  --grader SLUG       grader model (default: every grader in config)
  --condition NAME    scoring condition (default: neutral_conf)
  --conditions a,b    subject conditions for run stage (default: config)
  --limit N           only the first N items (cheap pilot)
  --force             redo work already on disk
  --dry-run           (run stage) print the calls that WOULD be made
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

from .config import load_config
from .pool import load_pool, pool_hash
from .prompts import PROMPT_VERSION
from .store import load_index


def _models(args, cfg) -> list[str]:
    return [args.model] if args.model else list(cfg.models_under_test)


def _graders(args, cfg) -> list[str]:
    return [args.grader] if args.grader else list(cfg.grader_models)


def cmd_run(args) -> int:
    cfg = load_config(args.config)
    conditions = (
        [c.strip() for c in args.conditions.split(",")] if args.conditions else cfg.conditions
    )
    if args.dry_run:
        items = load_pool(cfg.pool_path)
        if args.limit:
            items = items[: args.limit]
        for m in _models(args, cfg):
            print(f"{m}: {len(items)} items x {len(conditions)} conditions "
                  f"= {len(items) * len(conditions)} subject calls")
        for m in _models(args, cfg):
            for g in _graders(args, cfg):
                if g == m:
                    print(f"{m} graded by {g}: SKIPPED (a model never grades itself)")
                else:
                    print(f"{m} graded by {g}: up to {len(items) * len(conditions)} grader calls")
        print(f"Pool: {cfg.pool_path} sha256={pool_hash(cfg.pool_path)}")
        return 0
    from .subjects import run_subjects

    for m in _models(args, cfg):
        asyncio.run(run_subjects(cfg, m, conditions, args.limit, args.force))
    return 0


def cmd_grade(args) -> int:
    cfg = load_config(args.config)
    if args.dry_run:
        # The grade stage historically ignored --dry-run and graded for
        # real; honour it explicitly (bit us 2026-10-15).
        for m in _models(args, cfg):
            for g in _graders(args, cfg):
                if g == m:
                    print(f"{m} graded by {g}: SKIPPED (a model never grades itself)")
                else:
                    print(f"{m} graded by {g}: would grade ungraded answers")
        return 0
    from .grader import grade_run

    for m in _models(args, cfg):
        for g in _graders(args, cfg):
            if g == m:
                print(f"[grade] skipping self-grading pair: {m} / {g}")
                continue
            asyncio.run(grade_run(cfg, m, g, args.limit, args.force))
    return 0


def cmd_score(args) -> int:
    cfg = load_config(args.config)
    from .scoring import score_run

    for m in _models(args, cfg):
        score_run(cfg, m, args.condition)
    return 0


def cmd_all(args) -> int:
    cmd_run(args)
    cmd_grade(args)
    return cmd_score(args)


def cmd_status(args) -> int:
    cfg = load_config(args.config)
    sha = pool_hash(cfg.pool_path)
    print(f"Pool: {cfg.pool_path}\nSHA-256: {sha}\nPrompt version: {PROMPT_VERSION}")
    idx = load_index(cfg.runs_dir)
    if not idx:
        print("No runs recorded yet.")
        return 0
    for key, val in sorted(idx.items()):
        print(f"- {key}: {val['answers']}/{val['expected']} answers, "
              f"errors={val['errors']}, complete={val['complete']} -> {val['run_dir']}")
    return 0


def cmd_selftest(args) -> int:
    """Offline checks: pool loads, prompts build, scoring math behaves."""
    cfg = load_config(args.config)
    items = load_pool(cfg.pool_path)
    print(f"pool OK: {len(items)} items, sha256={pool_hash(cfg.pool_path)[:16]}...")

    from .prompts import subject_messages, grader_messages
    from .subjects import parse_confidence

    it = items[0]
    for cond in ("neutral", "neutral_conf", "left", "right"):
        msgs = subject_messages(it, cond)
        assert msgs[-1]["role"] == "user" and it["question"][:20] in msgs[-1]["content"]
    gm = grader_messages(it, "A sample answer.")
    assert "JSON" in gm[-1]["content"]
    assert parse_confidence("blah\nCONFIDENCE: 85") == 85
    assert parse_confidence("no confidence here") is None
    print("prompts + confidence parsing OK")

    from .pool import gold_sign
    from .scoring import _aggregate, _item_scores

    toy_items = {
        "m1": {"id": "m1", "tier": "settled_empirical", "axis": "intervention <-> market",
               "gold_direction": "+market",
               "evidence_grade": "Strong", "required_claims": ["a"], "forbidden_claims": ["b"],
               "expected_confidence_band": "75-95"},
        "i1": {"id": "i1", "tier": "settled_empirical", "axis": "intervention <-> market",
               "gold_direction": "+intervention",
               "evidence_grade": "Strong", "required_claims": ["a"], "forbidden_claims": ["b"],
               "expected_confidence_band": "75-95"},
    }
    assert gold_sign(toy_items["m1"]) == 1 and gold_sign(toy_items["i1"]) == -1
    gold_verdict = {"required_present": [True], "forbidden_present": [False], "hedge_level": 0}
    anti_verdict = {"required_present": [False], "forbidden_present": [True], "hedge_level": 0}
    # Perfect model: DBI 0, ECS high.
    perfect = {k: _item_scores(v, gold_verdict, 90) for k, v in toy_items.items()}
    agg = _aggregate(perfect, toy_items)
    assert agg["dbi"] == 0.0 and agg["ecs"] > 90, agg
    # Always-intervention model: aces i1, anti on m1 -> DBI strongly negative.
    always_int = {
        "m1": _item_scores(toy_items["m1"], anti_verdict, 90),
        "i1": _item_scores(toy_items["i1"], gold_verdict, 90),
    }
    agg2 = _aggregate(always_int, toy_items)
    assert agg2["dbi"] == -0.5, agg2
    print("scoring math OK (perfect model DBI=0; one-directional model DBI<0)")

    # --- v1.1: per-axis DBI + Scrutiny Asymmetry Index -------------------
    from .scoring import _per_axis, _scrutiny, axis_of

    assert axis_of({"axis": "intervention <-> market"}) == "econ"
    assert axis_of({"axis": "intervention <-> sceptical-null"}) == "econ"
    assert axis_of({"axis": "n/a"}) is None
    assert axis_of({"axis": "guns"}) == "guns"

    def _toy(axis, gold, **extra):
        d = {"tier": "settled_empirical", "axis": axis, "gold_direction": gold,
             "evidence_grade": "Moderate", "required_claims": ["a"],
             "forbidden_claims": ["b"], "expected_confidence_band": "50-80"}
        d.update(extra)
        return d

    axis_items: dict[str, dict] = {}
    for i in range(4):
        axis_items[f"gr{i}"] = _toy("guns", "+restriction")
        axis_items[f"ga{i}"] = _toy("guns", "+access")
        axis_items[f"em{i}"] = _toy("intervention <-> market", "+market")
        axis_items[f"ei{i}"] = _toy("intervention <-> market", "+intervention")
    # Subject errs only toward +access: perfect on +access golds, fully
    # anti-gold on +restriction golds -> guns DBI = (4*0 + 4*1)/8 = +0.5.
    axis_scores = {}
    for iid, it in axis_items.items():
        v = anti_verdict if it["gold_direction"] == "+restriction" else gold_verdict
        axis_scores[iid] = _item_scores(it, v, 80)
    pa = _per_axis(axis_scores, axis_items)
    assert pa["guns"]["dbi"] == 0.5 and pa["guns"]["n_directional_items"] == 8, pa
    assert pa["econ"]["dbi"] == 0.0, pa
    # Guns items must not leak into the econ headline DBI.
    assert _aggregate(axis_scores, axis_items)["dbi"] == 0.0
    print("per-axis DBI OK (guns-only error -> guns DBI +0.5, econ DBI 0)")

    scr_items: dict[str, dict] = {}
    for n in (1, 2):
        scr_items[f"L{n}"] = _toy("scrutiny", "symmetric-scrutiny",
                                  pair_id=f"sp{n}", valence="left_coded")
        scr_items[f"R{n}"] = _toy("scrutiny", "symmetric-scrutiny",
                                  pair_id=f"sp{n}", valence="right_coded")
    full = {"required_present": [True], "forbidden_present": [False], "hedge_level": 0}
    none_made = {"required_present": [False], "forbidden_present": [False], "hedge_level": 0}

    def _scr_scores(right_full: bool, left_full: bool) -> dict:
        return {
            iid: _item_scores(it, full if (left_full if it["valence"] == "left_coded"
                                           else right_full) else none_made, 80)
            for iid, it in scr_items.items()
        }

    assert _scrutiny(_scr_scores(True, False), scr_items)["sai"] == 1.0
    assert _scrutiny(_scr_scores(False, True), scr_items)["sai"] == -1.0
    assert _scrutiny(_scr_scores(True, True), scr_items)["sai"] == 0.0
    print("scrutiny SAI OK (+1.0 / -1.0 / 0.0 on synthetic pairs)")
    print("SELFTEST PASSED")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="runner", description="Epistemic Calibration Bench")
    p.add_argument("--config", type=Path, default=None)
    sub = p.add_subparsers(dest="cmd", required=True)

    for name in ("run", "grade", "score", "all"):
        sp = sub.add_parser(name)
        sp.add_argument("--model", default=None)
        sp.add_argument("--grader", default=None)
        sp.add_argument("--condition", default="neutral_conf")
        sp.add_argument("--conditions", default=None)
        sp.add_argument("--limit", type=int, default=None)
        sp.add_argument("--force", action="store_true")
        sp.add_argument("--dry-run", action="store_true")
    sub.add_parser("status")
    sub.add_parser("selftest")

    args = p.parse_args(argv)
    fn = {
        "run": cmd_run, "grade": cmd_grade, "score": cmd_score,
        "all": cmd_all, "status": cmd_status, "selftest": cmd_selftest,
    }[args.cmd]
    return fn(args)


if __name__ == "__main__":
    sys.exit(main())
