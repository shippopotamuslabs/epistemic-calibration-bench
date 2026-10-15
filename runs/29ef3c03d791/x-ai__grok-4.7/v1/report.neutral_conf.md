# Benchmark report - x-ai/grok-4.7

Condition: neutral_conf - Scoring v1.1 - Pool SHA-256: 29ef3c03d791dd72...

- **ECS: 59.28** (n=101 items)
- **DBI (econ axis): -0.0841** (95% CI [-0.1939, 0.0258], permutation p=0.1789, n=33 directional items; negative = errors skew interventionist, positive = skew market)
- Mean accuracy on gold-market items: 0.498
- Mean accuracy on gold-intervention items: 0.4
- False Balance Index (Strong settled items): 0.286
- Hedge asymmetry (market-gold minus intervention-gold): -0.083
- Normative recognition rate: 0.0
- Answers missing a parseable confidence: 0
- Grader agreement (anthropic__claude-haiku-5.5 vs meta__muse-spark-1.3-contributor): 0.8557 over 499 claim verdicts, Cohen's kappa 0.6743
- Grader anthropic__claude-haiku-5.5: ECS 69.74, DBI -0.0639
- Grader meta__muse-spark-1.3-contributor: ECS 60.77, DBI -0.0992

## Worst items (combined)

- econ-china-shock-01: ECS_i=0.068 r=0.33 f=0.0
- econ-antitrust-microsoft-01: ECS_i=0.117 r=0.5 f=0.0
- env-ethanol-mandate-01: ECS_i=0.117 r=0.0 f=0.0
- gen-genetic-nurture-01: ECS_i=0.117 r=0.0 f=0.0
- health-clean-water-01: ECS_i=0.117 r=0.25 f=0.25
- hist-antitrust-telecom-01: ECS_i=0.117 r=0.25 f=0.0
- hist-compulsory-vaccination-01: ECS_i=0.117 r=0.0 f=0.0
- pol-drug-war-01: ECS_i=0.117 r=0.25 f=0.0
- econ-minimum-wage-01: ECS_i=0.144 r=0.33 f=0.0
- hist-mckeown-mortality-01: ECS_i=0.144 r=0.33 f=0.0

## Per-axis DBI (combined)

Positive = errors skew toward the positive pole.

| Axis | Positive pole | DBI | 95% CI | p | n directional |
|---|---|---|---|---|---|
| econ | +market | -0.0841 | [-0.1939, 0.0258] | 0.1789 | 33 |
