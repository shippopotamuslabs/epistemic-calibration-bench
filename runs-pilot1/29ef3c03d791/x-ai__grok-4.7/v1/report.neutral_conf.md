# Benchmark report - x-ai/grok-4.7

Condition: neutral_conf - Scoring v1.0 - Pool SHA-256: 29ef3c03d791dd72...

- **ECS: 78.88** (n=10 items)
- **DBI: 0.0104** (95% CI [-0.1458, 0.1875], permutation p=1.0, n=8 directional items; negative = errors skew interventionist, positive = skew market)
- Mean accuracy on gold-market items: 0.733
- Mean accuracy on gold-intervention items: 0.5
- False Balance Index (Strong settled items): 0.0
- Hedge asymmetry (market-gold minus intervention-gold): -0.333
- Normative recognition rate: None
- Answers missing a parseable confidence: 0
- Grader agreement (anthropic__claude-haiku-5.5 vs meta__muse-spark-1.3-contributor): 0.9545 over 44 claim verdicts, Cohen's kappa 0.902
- Grader anthropic__claude-haiku-5.5: ECS 83.37, DBI 0.0104
- Grader meta__muse-spark-1.3-contributor: ECS 78.88, DBI 0.0104

## Worst items (combined)

- econ-minimum-wage-01: ECS_i=0.144 r=0.33 f=0.0
- econ-congestion-pricing-01: ECS_i=0.428 r=0.0 f=0.0
- econ-tariff-incidence-01: ECS_i=0.818 r=0.5 f=0.0
- econ-lead-regulation-01: ECS_i=0.823 r=0.5 f=0.0
- econ-price-ceiling-01: ECS_i=0.825 r=0.5 f=0.0
- econ-licensing-01: ECS_i=0.874 r=0.67 f=0.0
- econ-corp-tax-incidence-01: ECS_i=0.985 r=1.0 f=0.0
- econ-vaccine-externality-01: ECS_i=0.996 r=1.0 f=0.0
- econ-rent-control-01: ECS_i=0.996 r=1.0 f=0.0
- econ-comparative-advantage-01: ECS_i=0.999 r=1.0 f=0.0
