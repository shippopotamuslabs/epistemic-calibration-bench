# Epistemic Calibration Bench

A benchmark measuring whether LLMs answer politically charged but empirically
verifiable questions in line with the evidence — and whether their *errors*
are directionally systematic. It explicitly rejects midpoint/"both sides"
scoring: calibration to evidence can legitimately land 100/0.

## Headline metrics

- **ECS (Epistemic Calibration Score, /100)** — 70% claim-level accuracy
  against a blind rubric + 30% confidence calibration (Brier).
- **DBI (Directional Bias Index, −1..+1)** — mean signed error per axis
  (econ, guns, drugs, medicine, gender-care, social-science, climate),
  with bootstrap CI and permutation p.
- **SAI (Scrutiny Asymmetry Index)** — matched pairs of studies (same
  design, opposite political valence); positive = the model interrogates
  right-coded studies harder than left-coded ones.
- False Balance Index, hedge asymmetry, normative-trap recognition.

Grading is claim-level and blind: the grader never sees the subject's
identity, the gold direction, or the axis. One dedicated grader model that
is never a subject (currently `z-ai/glm-5.3-flash`).

## Pools

- **v1.0** — `seed_questions.jsonl`, 102 items, locked in `LOCK.md`
  (SHA-256 29ef3c03…). Run 1 (2026-10-15): Spark ECS 67.8, Haiku 66.6,
  Grok 59.3; all econ DBIs statistically indistinguishable from zero.
- **v1.1** — `pool-v1.1.jsonl`, 138 items, locked in `LOCK-V1.1.md`
  (SHA-256 b72b65a3…). Run (2026-10-15, GLM-graded): Haiku ECS 77.2,
  Spark 71.4, Grok 70.6; first significant signal was scrutiny asymmetry
  (Haiku SAI +0.18, CI excludes zero).
- **Open-form twins** — `pool-twins-block.jsonl`: 20 marquee items asked
  the way a person would ask them (no designated authority), run against
  their delegated-form originals. Every model scored worse open (−5 to
  −12 ECS): the form gap is the steering effect, measured.

Every pool survived a hostile audit gauntlet before locking — skeptical
reviews in both political directions, a contested-tier attacker, and a
full numbers audit. The audit trail lives in `drafts/`.

## Layout

- `DESIGN.md`, `EXPANSION.md`, `EXPANSION-V1.1-PLAN.md` — methodology
- `LOCK.md`, `LOCK-V1.1.md`, `POOL-REPORT.md` — pool locks and tallies
- `drafts/` — drafting waves, audit reports, changelogs
- `runner/` — the harness (Python 3.12 asyncio, OpenRouter): one call per
  (item, condition), crash-resume, append-only JSONL run store keyed by
  pool hash
- `runs/` — completed run data (answers, grades, scores, reports)

## Running

```bash
cd runner && python3 -m venv .venv && .venv/bin/pip install openai httpx
# put OPENROUTER_API_KEY in runner/.env (never commit it)
.venv/bin/python -m runner selftest
.venv/bin/python -m runner all          # answers -> grades -> scores
```
