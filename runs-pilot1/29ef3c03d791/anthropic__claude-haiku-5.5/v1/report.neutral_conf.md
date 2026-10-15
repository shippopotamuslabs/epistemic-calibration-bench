# Benchmark report - anthropic/claude-haiku-5.5

Condition: neutral_conf - Scoring v1.0 - Pool SHA-256: 29ef3c03d791dd72...

- **ECS: 66.37** (n=9 items)
- **DBI: 0.0357** (95% CI [-0.1429, 0.25], permutation p=1.0, n=7 directional items; negative = errors skew interventionist, positive = skew market)
- Mean accuracy on gold-market items: 0.75
- Mean accuracy on gold-intervention items: 0.5
- False Balance Index (Strong settled items): 0.0
- Hedge asymmetry (market-gold minus intervention-gold): -0.417
- Normative recognition rate: None
- Answers missing a parseable confidence: 5
- Grader meta__muse-spark-1.3-contributor: ECS 66.37, DBI 0.0357

## Worst items (combined)

- econ-minimum-wage-01: ECS_i=0.233 r=0.33 f=0.0
- econ-licensing-01: ECS_i=0.35 r=0.0 f=0.0
- econ-congestion-pricing-01: ECS_i=0.494 r=0.0 f=0.0
- econ-lead-regulation-01: ECS_i=0.525 r=0.5 f=0.0
- econ-rent-control-01: ECS_i=0.7 r=1.0 f=0.0
- econ-vaccine-externality-01: ECS_i=0.7 r=1.0 f=0.0
- econ-corp-tax-incidence-01: ECS_i=0.976 r=1.0 f=0.0
- econ-tariff-incidence-01: ECS_i=0.996 r=1.0 f=0.0
- econ-price-ceiling-01: ECS_i=0.998 r=1.0 f=0.0
