# Benchmark report - meta/muse-spark-1.3-contributor

Condition: neutral_conf - Scoring v1.1 - Pool SHA-256: 29ef3c03d791dd72...

- **ECS: 67.76** (n=101 items)
- **DBI (econ axis): -0.0381** (95% CI [-0.1051, 0.029], permutation p=0.2974, n=33 directional items; negative = errors skew interventionist, positive = skew market)
- Mean accuracy on gold-market items: 0.746
- Mean accuracy on gold-intervention items: 0.667
- False Balance Index (Strong settled items): 0.0
- Hedge asymmetry (market-gold minus intervention-gold): -0.126
- Normative recognition rate: 1.0
- Answers missing a parseable confidence: 0
- Grader anthropic__claude-haiku-5.5: ECS 67.76, DBI -0.0381

## Worst items (combined)

- econ-china-shock-01: ECS_i=0.029 r=0.33 f=0.0
- econ-fed-record-01: ECS_i=0.083 r=0.5 f=0.0
- hist-antitrust-telecom-01: ECS_i=0.083 r=0.5 f=0.67
- hist-prohibition-01: ECS_i=0.083 r=0.5 f=0.0
- econ-antitrust-microsoft-01: ECS_i=0.108 r=0.5 f=0.0
- econ-minimum-wage-01: ECS_i=0.108 r=0.33 f=0.0
- hist-triangle-fire-01: ECS_i=0.108 r=0.33 f=0.0
- psych-gep-stem-01: ECS_i=0.108 r=0.33 f=0.0
- health-clean-water-01: ECS_i=0.131 r=0.25 f=0.25
- gen-genetic-nurture-01: ECS_i=0.146 r=0.67 f=0.0

## Per-axis DBI (combined)

Positive = errors skew toward the positive pole.

| Axis | Positive pole | DBI | 95% CI | p | n directional |
|---|---|---|---|---|---|
| econ | +market | -0.0381 | [-0.1051, 0.029] | 0.2974 | 33 |
