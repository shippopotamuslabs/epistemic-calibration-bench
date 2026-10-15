# Runner spec — DRAFT (prepared 2026-10-15, for Sean's review)

Status: draft answering Sean's 2026-10-15 design questions. Pool is LOCKED v1.0
(102 items, SHA-256 29ef3c03…); this spec does not touch the pool. Any run must
cite the pool hash it was produced against (LOCK.md terms).

## Language: Python

- Sean's instinct is right. The workload is I/O-bound API calls plus
  statistics (bootstrap CIs, permutation tests, kappa — DESIGN §2/§5);
  Python's data stack wins and there is no performance case for Go here.
- Async via `asyncio` + `httpx.AsyncClient`. The C# `Parallel.ForEachAsync`
  equivalent is an `asyncio.Semaphore(N)` bounding in-flight requests —
  spawn one task per (item × condition), the semaphore caps concurrency.
  Start N=8–16; OpenRouter rate limits, not local CPU, are the ceiling.

## Run matrix (from DESIGN §6 — easy to forget, drives all the numbers)

Per model: 102 items × 4 prompt conditions (neutral; neutral+confidence;
left-coded user; right-coded user) = **408 answer calls per sample**.
v0.1 design says 1 sample and notes the limitation; n≥3 is the upgrade path.
This is why resume/caching (below) is not optional — a crashed or
half-finished run at 400+ calls per model must not restart from zero.

## Config vs secrets — two separate files

- `config.json` (committed, no secrets): models to test as a JSON array of
  OpenRouter model ids; grader model id(s); concurrency; temperature;
  samples per condition; grading chunk size. Adding a newly released model
  = one line in this array.
- Secret: the OpenRouter API key lives ONLY in an environment variable
  (`OPENROUTER_API_KEY`), optionally via a local `.env` that is gitignored.
  Never in config.json, never in run output, never logged.

## Storage & resume (the "don't re-run a model" requirement)

Append-only JSONL under `runs/<run-id>/`:

- `manifest.json` — pool SHA-256, config snapshot, grader model, timestamps,
  target model list. Written first; a run is defined by (pool hash, config).
- `answers.jsonl` — one line per result, keyed by
  `(model, item_id, condition, sample_idx)`, with status + raw response.
- `grades.jsonl` — keyed the same way plus `grader_model`.

Resume rule: before dispatching any call, load existing keys with
status=ok and skip them. Re-running the same model against the same pool
hash is therefore free/no-op unless `--force` is passed. If the pool ever
changes, the hash changes, the manifest differs, and old answers can never
be silently mixed into a new-version run — re-benchmarking after a question
tweak is automatic and safe, exactly the two cases Sean described.

## Answering

- One API call per (item, condition). Never batch questions into one call:
  answers would contaminate each other and per-item confidence parsing
  (condition 2 asks for a 0–100% confidence on the central claim) breaks.
- Persist each answer to `answers.jsonl` the moment it returns
  (crash-safe), not at the end of the run.

## Grading — chunk, don't aggregate all 102

Sean's chunking instinct (10–20) is the right compromise; grading all 102
answers in one call risks output truncation, claims bleeding across items,
and unparseable partial JSON with no clean retry unit.

- Recommended default: **chunks of 10**, grader call receives ONLY
  (question, answer, rubric, direction codebook) per item — DESIGN §5:
  the grader never sees the target model's name and never free-styles a
  holistic bias judgement; it scores claim-by-claim entailment.
- Grader returns structured JSON per item (required claims hit/missed,
  forbidden claims present, direction code per error). A failed chunk
  retries as a unit; grades already written are skipped on resume.
- DESIGN §5 also calls for 2–3 graders from different labs/families +
  inter-grader agreement (kappa/alpha) and a ~20% human audit in the
  pilot. Config should hold a grader *list*, not a single grader, even if
  the pilot starts with one.

## Suggested CLI shape

```
python -m bench run     --config config.json            # answers only
python -m bench grade   --run runs/<run-id>             # grades answers
python -m bench report  --run runs/<run-id>             # ECS + DBI + CIs
python -m bench run --model <new-model-id>              # add one model later
```

## Open decisions for Sean

1. Grading chunk size: 10 (recommended) vs 20 (cheaper, riskier parses).
2. Pilot scope: 3–4 models × 1 sample (DESIGN build order step 4) before
   any n≥3 sampling.
3. One grader for the pilot with the multi-grader list wired but unused,
   or pay for 2 graders from day one for the agreement stats?
