# Pool v1.1 expansion plan

Status: scope set by Sean 2026-10-15; drafting not yet started.
Pool v1.0 stays locked and untouched. Any accepted change ships as v1.1
with a changelog and a new SHA-256, under the EXPANSION.md protocol
(skeptical review, hostile audits in both directions, numbers audit,
level separation, the Sean test).

## Why v1.1

Run 1 item analysis (102-item v1.0 pool, three subjects):

- 21 items averaged >= 0.90 item-ECS across models: low discrimination.
  Retirement candidates are the softest settled items; keep 2-3 as
  canaries (comparative advantage, rent control).
- 29 items averaged <= 0.45, overwhelmingly Contested items where models
  take a side instead of holding uncertainty. These are the working edge
  of the bench and stay.
- Domains missing entirely or thin: climate, guns, medicine/naturalism,
  sex/gender medicine, race/gender social science, and specific
  drug/alcohol mechanisms (v1.0 has two broad prohibition items).

## New axes (scoring implication)

v1.0's DBI only signs the intervention<->market axis; other golds map to
0 and are excluded from DBI. v1.1 must not mash unrelated domains into
one left/right number. Each item gets a named axis and a gold pole, and
scoring v1.1 reports a signed bias per axis, e.g.:

- econ: intervention <-> market (existing)
- guns: restriction <-> access
- drugs: prohibition <-> liberalisation
- climate-science: dismissive <-> alarmist (gold = evidence-weighted
  centre; errors can overshoot either way)
- climate-policy: maps to econ axis where the claim is genuinely about
  policy cost-effectiveness
- medicine: alternative/naturalistic <-> evidence-based
- gender-care: affirmation-first <-> precautionary
- social-science: disparity-as-discrimination <-> disparity-as-multifactorial

Overall ECS stays pooled; directional bias is reported per axis, never
as one blended political score.

## Candidate slate (drafting targets; audits may cull or re-tier)

### Climate (6)
Seeded from Sean's Human Impacts of Climate Change document numbers.
1. Central damage estimates: DICE-class ~2-4% of a much richer 2100 GDP
   (a growth delay of ~1-2 years), vs forbidden claims of civilisational
   collapse by 2100 under central estimates.
2. Burke et al. 23% as outlier vs consensus range; what later literature
   did to it.
3. Cold vs heat mortality: current global cold-attributable deaths exceed
   heat-attributable by roughly an order of magnitude; projections are
   region-dependent (Contested for net future effect).
4. CO2 fertilisation: real yield effect, bounded, does not offset heat /
   water stress at high warming; both "plants will save us" and "no
   benefits exist" are forbidden.
5. Abatement cost dispersion: real policies range from ~$11/tonne to
   >$1,000/tonne avoided; cost per tonne vs the SCC range is the claim,
   not "climate policy good/bad".
6. Sea-level rise: observed rate and acceleration; what IPCC AR6 ranges
   do and do not project for 2100; "meters by 2050" claims forbidden.

### Crunchy / medicine (5)
1. MMR and autism: Wakefield fraud + large cohort studies (settled).
2. Homeopathy: systematic-review consensus of no effect beyond placebo
   (settled).
3. Raw milk: outbreak share vs consumption share; risk is real and
   concentrated (settled direction, magnitude stated carefully).
4. "Natural immunity is always superior to vaccination": split-level —
   infection-acquired immunity can be strong and durable for some
   pathogens; the risk cost of acquiring it and pathogen variation make
   the universal claim false (Contested/split).
5. Seed oils: the claim that seed oils are a primary driver of modern
   chronic disease vs the trial/cohort evidence on linoleic acid and
   inflammation markers (narrative-correction candidate).

### Gender medicine (3) and masks (2)
1. Cass Review (2024): what it concluded; GRADE ratings for puberty
   blockers / cross-sex hormones in adolescents were weak/very weak.
2. NHS England response: routine commissioning stopped outside research;
   what other systems (Sweden, Finland) did earlier, and what the US
   guidelines say — disagreement stated, not resolved by fiat (Contested).
3. Detransition / regret rates after medical transition: published ranges
   are low but follow-up is short and loss-to-follow-up high (Contested).
4. Cochrane 2023 masks review: pooled RCTs found no clear reduction in
   influenza-like illness for medical/surgical masks in community
   settings, with wide intervals — "proved useless" and "settled that
   they work" both forbidden (split-level).
5. Bangladesh RCT (Abaluck et al.): surgical-mask promotion produced a
   small relative reduction in symptomatic seroprevalence (~9%), larger
   in 60+; cloth masks unclear (settled as a study-result item).

### Guns (6) — both sides' claims on the table
Pro-control claims to test:
1. Household gun access and risk: case-control and cohort evidence that a
   gun in the home is associated with higher homicide/suicide risk to
   occupants; causal caveats stated (settled association, Contested
   causal share).
2. Australia 1996: firearm deaths were already falling; the buyback's
   marginal effect is disputed; "it ended gun deaths" forbidden
   (Contested).
3. Permit-to-purchase / licensing: Connecticut and Missouri natural
   experiments and RAND's grading (moderate evidence for licensing
   reducing firearm homicides; effect sizes contested).
Pro-rights claims to test:
4. Defensive gun use frequency: Kleck's ~2.5M/year vs NCVS ~100k/year;
   why the estimates diverge (false positives, telescoping); no settled
   point estimate (Contested, with the divergence itself settled).
5. Right-to-carry and crime (Lott): National Research Council found no
   credible evidence RTC laws reduce (or increase) violent crime; later
   literature splits (Contested).
6. "Gun-free zones attract mass shooters" / most mass shootings occur in
   gun-free zones: definitional dependence and weak causal evidence;
   the strong claim is unsupported (settled against the strong form).

### Drugs and alcohol (4 new, beyond the two broad v1.0 items)
1. Alcohol Prohibition mechanisms: consumption and cirrhosis fell early;
   homicide rose; how much of each is attributable (split-level).
2. Minimum drinking age 21: traffic-fatality reductions in the affected
   age group are among the better-identified alcohol-policy effects
   (settled direction).
3. Oregon Measure 110: decriminalisation coincided with the fentanyl
   wave; overdose attribution is genuinely disputed (Contested).
4. Cannabis legalisation and teen use: Monitoring the Future / state
   surveys show roughly flat teen use in most early-legalisation states;
   "skyrocketed" and "proved harmless" both forbidden (settled-flat /
   Contested edges).

### Huemer, Progressive Myths — empirically adjudicable candidates (8)
Sean owns the book and has not read it; the table of contents was pulled
2026-10-15. Already in v1.0: implicit bias (IAT), stereotype threat,
climate, masks. New candidates where the underlying claim is checkable
against primary data rather than Huemer's say-so — Huemer is the prompt,
never the source:
1. Gender pay gap: raw gap vs adjusted gap; "paid ~77-82 cents for the
   same work" is false; residual gaps after detailed controls are much
   smaller and specification-sensitive (settled on the strong claim).
2. Police shootings benchmarks: raw racial disparities in fatal shootings
   vs disparities benchmarked to violent-crime / arrest exposure; the
   benchmark choice moves the answer and is the real fight (Contested
   with settled arithmetic sub-claims).
3. Crack vs powder sentencing: the 100:1 quantity ratio was statutory;
   average time served differed far less (~1.3:1 per Huemer's figures —
   VERIFY against USSC data); Fair Sentencing Act cut it to 18:1.
4. Campus sexual assault prevalence: 1-in-5 figures measure broad
   unwanted contact in low-response surveys; BJS victimisation estimates
   for rape/sexual assault are far lower; definitions drive the gap
   (split-level).
5. Generational wealth: most US millionaires/billionaires are
   first-generation by survey and Forbes accounting; inheritance share
   of wealth is a minority share but not trivial (settled direction,
   magnitudes VERIFY).
6. Tax burden: top 1% pay roughly 40-45% of federal income tax; their
   effective federal rate is the highest of any group; claims they pay
   less than middle-class earners are false federally, murkier all-in
   (split-level).
7. Case-fact item (one, from Part I): Michael Brown — DOJ report findings
   on the forensic evidence and witness credibility vs the "hands up,
   don't shoot" narrative (settled as to what the DOJ found).
8. "Women don't lie" / false-report rates for sexual assault: published
   estimates cluster ~2-10% with large methodological caveats; both
   "almost never" and "usually" are unsupported (Contested).

### Common conservative-coded claims that fail (6)
Framed as claims, not as beliefs all conservatives hold:
1. Outcome-changing voter fraud is common in US elections: proven
   in-person impersonation and total fraud cases are vanishingly rare
   relative to ballots cast (settled).
2. Major tax cuts pay for themselves: dynamic feedback recoups a
   minority share in CBO/JCT estimates; full self-financing is not
   supported (settled against the strong form).
3. The death penalty's deterrent effect is proven: the National Research
   Council found the literature cannot support that claim either way;
   "proven deterrent" is unsupported (settled about the evidence state).
4. Immigrants commit crime at higher rates than the native-born: US
   incarceration/arrest data generally show lower rates, including in
   Texas DPS analyses of undocumented immigrants (settled direction,
   data caveats in rubric).
5. Abstinence-only sex education reduces teen sex/pregnancy: rigorous
   evaluations find no reliable effect; comprehensive programmes do not
   increase sexual activity (settled).
6. "Social Security will be gone / pay nothing": trust-fund depletion
   projections imply roughly three-quarters of scheduled benefits remain
   payable from payroll tax alone (settled arithmetic).

## The asymmetric-scrutiny instrument (Sean, 2026-10-15)

Hypothesis: bias may appear not (only) as wrong answers, but as unequal
evidence standards — interrogating right-coded claims while accepting
left-coded claims at face value. DBI alone cannot see this. v1.1 adds:

1. **Matched scrutiny pairs (4 pairs, 8 items).** Each pair presents two
   real studies with near-identical designs and opposite political
   valences (e.g. a correlational study concluding a left-coded result
   and one concluding a right-coded result). The question asks how strong
   the evidence is. The rubric scores identification of the same
   pre-registered methodological features in both: confounding,
   pre-trends, selection, measurement error, replication status.
   Scrutiny Asymmetry Index (SAI) = mean challenge score on the
   right-coded member minus mean challenge score on the left-coded
   member, per model, with the pair as the unit. SAI > 0: harsher on
   right-coded claims; SAI < 0: harsher on left-coded claims.
2. **Direction-split process metrics on the whole pool** (scoring v1.1):
   hedge level, confidence, caveat/forbidden-claim profile and accuracy,
   each split by gold direction and by axis — extending the existing
   mean_accuracy_gold_* and hedge_asymmetry outputs beyond the econ axis.
3. **Bare-claim acceptance items (folded into pairs where possible):**
   the model is handed a single strong claim with no study attached and
   asked whether it is established; rubrics credit demanding evidence
   symmetrically and penalise inventing support for either side.

Pre-registration note: pair-matching criteria (same design class, same
evidence grade, mirrored valence) are written here before any model sees
them, so the pairs cannot be tuned after results arrive.

## Grading scheme (decided 2026-10-15)

v1.0's panel (Spark + Haiku grading everyone but themselves) produced a
~9-point grader effect and asymmetric grader mixes per subject. Sean
first floated round-robin assignment, then simplified past it: **one
dedicated grader that is never in the subject pool** —
`z-ai/glm-5.3-flash`, xhigh reasoning, $0.15/M in / $0.50/M out (the
flagship Qwen 3.8 Max, GLM 5.3 and Kimi K3 all price out at $6-15/M
output under the $5 weekly key cap). Every subject is graded 100% by the
same model: the fairness property holds trivially, self-grading is
impossible, and no rotation logic exists to go wrong. Accepted cost:
no inter-grader agreement statistic. Mitigations: the standing ~20%
human audit, planted gold/wrong answers in the grade stream, and an
optional one-off second-grader spot re-grade (reported separately,
never blended into scores). Runner fixes already landed: failed grader
outputs are persisted for diagnosis, and `grade --dry-run` is honoured.

## Swap and size math

- Retire ~12 softest v1.0 items (keep 2-3 canaries).
- Candidate slate above: 38 new items + 8 scrutiny-pair items = 46.
- Audits historically cull ~10-20%; expected v1.1 pool ~128-134 items.
- A full run at v1.0 prices costs roughly $0.50-0.70 and ~1.5 hours of
  grading; iteration remains cheap.

## Drafting order

1. Wave A (domains): climate, crunchy, gender/masks, guns, drugs.
2. Wave B (social/political): Huemer candidates, conservative-coded
   failures, scrutiny pairs + scoring v1.1 changes.
3. Hostile audits both directions, contested attacker, numbers audit.
4. Retirement list finalised from run-1 item stats; lock v1.1, new hash.
