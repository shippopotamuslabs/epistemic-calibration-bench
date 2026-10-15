# Bench v1.1 human-audit starting index

Prepared 2026-10-15 (evening) as groundwork only — no audit has been performed yet.
Run: pool b72b65a38b5a (v1.1, 138 items), single grader z-ai/glm-5.3-flash.
Per the design's mitigation for a single grader (~20% human audit), start with the
highest-leverage grades rather than a random sample: the Scrutiny Asymmetry Index
rests on only 4 matched pairs, and Haiku's SAI (+0.183, CI [0.042, 0.342]) is the
run's only statistically detectable signal — it stands or falls on these grades.

## Scrutiny pairs (8 items x 3 subjects = 24 grades)

- Pair 1: scrutiny-minimum-wage-dube-01 / scrutiny-right-to-carry-lott-01
- Pair 2: scrutiny-bias-training-devine-01 / scrutiny-god-priming-shariff-01
- Pair 3: scrutiny-mariel-card-01 / scrutiny-mariel-borjas-01
- Pair 4: scrutiny-climate-burke-01 / scrutiny-climate-dice-01

## Hardest items (accuracy 0.0-0.5 at 0.85-0.96 stated confidence, all subjects)

- gend-cass-evidence-base-01 (Cass Review evidence base)
- soc-pay-gap-01 (gender pay gap)

## Where the material lives (per subject, under runs/b72b65a38b5a/<subject>/v1/)

- anthropic__claude-haiku-5.5/v1/
- meta__muse-spark-1.3-contributor/v1/
- x-ai__grok-4.7/v1/

Each dir: answers.jsonl (subject answers), grades.z-ai__glm-5.3-flash.jsonl
(claim-level verdicts: required_present / forbidden_present / hedge_level /
evidence_quotes), scores.neutral_conf.json, report.neutral_conf.md.
Verified 2026-10-15: 138 answers and 138 grades per subject, zero errors.
