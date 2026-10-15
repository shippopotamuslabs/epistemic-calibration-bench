# Epistemic Calibration Bench — runner

Python 3.12+, asyncio. One API call per (question, condition) for subjects;
one blind, claim-level grading call per (answer, grader). Every stage writes
incrementally and resumes: re-running a stage skips work already on disk.

## Setup

```bash
cd ~/workspace/epistemic-calibration-bench/runner
python3 -m venv .venv
.venv/bin/pip install openai
cp .env.example .env   # then put your OpenRouter key in .env
```

The key is read from `OPENROUTER_API_KEY` (environment first, then
`runner/.env`). It is never read from `config.json` and never logged.

## Config (`config.json`)

- `models_under_test` — OpenRouter slugs to benchmark. Add a newly released
  model by appending one line; existing results for other models are kept.
- `grader_models` — 2+ graders from different labs (DESIGN.md §5).
- `conditions` — subject prompt conditions (§6). Pilot default:
  `["neutral_conf"]`. Add `"left"` / `"right"` for audience flip-rate runs.
- `concurrency`, `temperature` (0), token caps, timeouts.

## Usage

```bash
PY=.venv/bin/python
$PY -m runner selftest                 # offline checks (no API key needed)
$PY -m runner run --dry-run            # print the calls that would be made
$PY -m runner run --limit 10           # cheap pilot: first 10 items, all models
$PY -m runner all --limit 10           # run + grade + score
$PY -m runner run                      # full 102 items, configured models
$PY -m runner grade                    # grade any ungraded answers
$PY -m runner score                    # (re)compute scores + report.md
$PY -m runner status                   # what's complete, keyed by pool hash
```

## Persistence / no-rerun rule

Runs live under `../runs/<pool-sha[:12]>/<model>/<prompt-version>/` with a
`manifest.json`, incremental `answers.jsonl`, `grades.<grader>.jsonl`, and
`scores.<condition>.json` + `report.<condition>.md`. `runs/index.json`
records completeness per (pool hash, model, prompt version).

- Same pool + same model → `run` skips it (answers already on disk).
  `--force` overrides.
- Edit the pool → new SHA-256 → every model is eligible again; old runs stay
  preserved under the old hash for comparison.
- Change a prompt template → bump `PROMPT_VERSION` in `prompts.py`; runs
  land in a new directory for the same reason.

## Scoring (SCORING_VERSION 1.0, in `scoring.py`)

Claim accuracy per item `a = r - f` (required-claim hit rate minus
forbidden-claim hit rate). DBI = mean signed error on the item axis
(market + / intervention −) over directional items, with bootstrap 95% CI
and a sign-flip permutation p-value; negative DBI = errors skew
interventionist. ECS blends claim accuracy (70%) with Brier-scored stated
confidence (30%); contested items score uncertainty fidelity instead of
one-sided correctness; normative traps score only recognition. Reports also
include grader agreement (claim-level rate + Cohen's kappa), false-balance
index, hedge asymmetry, and per-gold-direction accuracy.
