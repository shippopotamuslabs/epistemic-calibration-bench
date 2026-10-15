# AUDIT — Empirical Numbers, Cluster 3 of 5 (Section B3)

Scope: ONLY these 10 items from `seed_questions.jsonl`:
gen-adoption-iq-01, gen-eea-tests-01, gen-pgs-attenuation-01, gen-genetic-nurture-01,
gen-sex-maths-performance-01, psych-marshmallow-01, psych-gep-stem-01, psych-lead-crime-01,
psych-stereotype-threat-01, psych-iat-validity-01.

Method: every number, percentage, effect size, sample size, date-bound quantity and
journal/year/volume/page citation in question / required_claims / forbidden_claims /
acceptable_nuances / sources_note was extracted (pure confidence bands and item ids skipped)
and checked against a named source found via web search. Numbers also appearing in
`drafts/FLAGS-RESOLVED.md` were re-checked from scratch — and in one case (Zigerell, below)
the FLAGS-RESOLVED resolution itself propagates an error.
Verdicts: CORRECT (source named) / WRONG (correct value + source) / UNVERIFIABLE (no source states it).

**Tally: 89 numbers checked — 82 CORRECT, 6 WRONG, 1 UNVERIFIABLE.**
The 6 WRONG bullets represent 5 distinct errors (the Hyde d error appears in two fields).

---

## gen-adoption-iq-01

- Adoption age 4–6 years — CORRECT. Duyme, Dumaret & Tomkiewicz (1999), PNAS: selection criterion was adoption between ages 4 and 6.
- Mean pre-adoption IQ 77 — CORRECT. Duyme et al. (1999), PNAS abstract: pre-adoption IQ <86, mean 77 (SD 6.3).
- Gain ~7.7 IQ points, lower-SES adoptive homes — CORRECT. Duyme et al. (1999), PNAS abstract: mean gain 7.7 in low-SES families.
- Gain ~19.5 IQ points, higher-SES adoptive homes — CORRECT. Duyme et al. (1999), PNAS abstract: mean gain 19.5 in high-SES families (post-adoption means 85 vs 98).
- Adoptive-environment shift "roughly 12 points" — CORRECT. Arithmetic of the two verified gains: 19.5 − 7.7 = 11.8 ≈ 12 (Duyme et al. 1999).
- Duyme et al. (1999), PNAS — CORRECT citation. PNAS, 20 July 1999.
- n = 65 late-adopted children — CORRECT. Duyme et al. (1999), PNAS: 65 children selected from 5,003 adoption files.
- PNAS 96:8790–8794 — CORRECT. PNAS 96(15):8790–8794.
- Capron & Duyme (1989), Nature, four-group cross-fostering, independent biological- and adoptive-SES effects — CORRECT. Nature record / contemporary reporting: 38 cross-fostered children; both biological-parent status (~12 points) and rearing status (~15+ points) independently associated with IQ.
- Nature 340:552–554 — CORRECT. Capron & Duyme, Nature 340, 552–554 (1989), DOI 10.1038/340552a0.

## gen-eea-tests-01

- Kendler et al. (1993), five psychiatric disorders — CORRECT. Kendler, Neale, Kessler, Heath & Eaves (1993): major depression, generalized anxiety disorder, phobia, bulimia, alcoholism.
- Behavior Genetics 23:21–27 — CORRECT. Kendler et al. (1993), Behavior Genetics 23:21–27 (this is the corrected journal; the earlier drafting flag about Archives of General Psychiatry was rightly rejected in FLAGS-RESOLVED).
- 1,030 female–female Virginia Twin Registry pairs — CORRECT. Kendler et al. (1993) abstract: 1,030 female–female pairs.
- 15.3% of pairs misperceived their zygosity — CORRECT. Kendler et al. (1993): 158 of 1,030 pairs (15.3%) disagreed with assigned zygosity; perceived zygosity had no significant effect on resemblance.
- Kendler et al. (1994), Psychological Medicine, parental perceived zygosity / differential treatment, same null — CORRECT. Kendler et al. (1994), Psychological Medicine 24(3):579–590: parental beliefs disagreed with assigned zygosity in ~20% of cases; no effect of parental perceived zygosity or similarity-emphasis on twin resemblance (tested for four disorders — the seed quotes no disorder count for 1994, so no conflict).

## gen-pgs-attenuation-01

- Howe et al. (2022), Nature Genetics — CORRECT. Howe et al., "Within-sibship GWAS of 25 phenotypes", Nature Genetics (2022).
- Nature Genetics 54:581–592 — CORRECT. Howe et al. (2022), Nat Genet 54:581–592.
- Lee et al. within-sibship shrinkage for EA "around 40% lower" — CORRECT. As cited in Howe et al. (2022) / FLAGS-RESOLVED verification: within-sibship EA estimates ~40% below population estimates.
- Selzam et al. (2019), Am J Hum Genet 105:351–363 — CORRECT. Selzam et al. (2019), AJHG 105:351–363.
- EA polygenic-score prediction attenuates by 48.9% within vs between families — CORRECT. Selzam et al. (2019): attenuation D = 48.9% for educational achievement (GCSE).
- Attenuation "roughly two-fifths to one-half" / "roughly half" — CORRECT. Supported range across the two verified sources: ~40% (Lee/Howe) to 48.9% (Selzam). No precise single R² pair is stated in the item, correctly.

## gen-genetic-nurture-01

- Kong et al. (2018), Science — CORRECT. Kong et al., "The nature of nurture", Science (2018).
- Science 359:424–428 — CORRECT. Kong et al., Science 359, 424–428 (2018).
- Non-transmitted polygenic score effect ~30% of the transmitted effect on offspring schooling — CORRECT. Kong et al. (2018): estimated effect 29.9% of the transmitted score's effect.
- "Nature Communications 2022 (13:32003)" — **WRONG.** No such article number exists. The paper described (Demange et al., "Estimating effects of parents' cognitive and non-cognitive skills on offspring education using polygenic scores") is Nature Communications **13:4801** (2022), DOI 10.1038/s41467-022-32003-x — "32003" is the DOI suffix, not the article number. Fix the citation to 13:4801.
- Substance of the 2022 claim (sibling-design indirect effects partly stratification/mating artefact, especially for non-cognitive scores) — CORRECT. Demange et al. (2022): 33% (cognitive) and 83% (non-cognitive) of sibling-design indirect effects attributable at least in part to stratification, assortative mating and prenatal effects; adoption design gives systematically lower estimates (also supporting the item's adoption-design nuance).
- Nivard et al. (2024), Nature Human Behaviour — CORRECT. Nivard et al. (2024), Nat Hum Behav 8:771–778, on indirect effects as dynastic social processes.

## gen-sex-maths-performance-01

- Hyde et al. (2008), Science — CORRECT citation (authors/year/journal). Hyde, Lindberg, Linn, Ellis & Williams (2008), Science.
- Science 321:494–495 — CORRECT. Hyde et al. (2008), Science 321:494–495.
- ">7 million US students" — CORRECT. Hyde et al. (2008): state-assessment data on over 7 million students in 10 states.
- "effect sizes around d = 0.05" as Hyde et al. (2008)'s finding (required_claims) — **WRONG.** Hyde et al. (2008)'s grade-by-grade effect sizes for grades 2–11 ranged roughly −0.02 to +0.06 and averaged essentially zero (contemporary summary: effect sizes "ranging from 0.01 and 0.06… basically zero"). d = 0.05 is the headline of Lindberg et al. (2010), Psychological Bulletin meta-analysis, and of Hyde et al.'s hard-item subsets — not the 2008 state-assessment mean. Correct value: d ≈ 0.00–0.01 overall (range −0.02 to +0.06 by grade), Hyde et al. (2008, Science).
- "d ~ 0.05–0.08" (sources_note) — **WRONG** (same error, second field). No Hyde (2008) overall estimate of 0.08 exists; the paper's averages are ~0 for general items, 0.05 (grade 8) and 0.07 (grade 12) only for depth-of-knowledge level-3 items. Replace with d ≈ 0 (range −0.02 to +0.06), Hyde et al. (2008); d = 0.05, Lindberg et al. (2010).
- Variance ratios ~1.1–1.2 — CORRECT (as an approximation). Hyde et al. (2008): all variance ratios >1.0, range 1.11 to 1.21 by grade — the seed's upper bound rounds the top value (1.21) down by 0.01; immaterial.
- Interest difference "d ~ 0.9" (cross-reference to the sibling interests item) — CORRECT. Su, Rounds & Armstrong (2009), Psychological Bulletin: Things–People d = 0.93.
- Hyde (2005) gender-similarities hypothesis — CORRECT citation. Hyde (2005), American Psychologist.
- Feingold (1992) on male variability — CORRECT citation. Feingold (1992) is the standard greater-male-variability reference for these data.

## psych-marshmallow-01

- Watts, Duncan & Quan (2018), Psychological Science — CORRECT. Watts, Duncan & Quan (2018), Psychological Science 29(7):1159–1177.
- Psychological Science 29:1159–1177 — CORRECT. As above.
- 918 children, NICHD study — CORRECT. Watts et al. (2018): analysis sample n = 918 from the NICHD Study of Early Child Care and Youth Development.
- "Roughly 10× the original n" — CORRECT (approximation, as stated in secondary coverage of Watts et al. 2018). Note the original Shoda et al. analytic n varied by outcome, so 10× is a loose ratio, not an exact one — the item's "roughly" covers this.
- Bivariate correlation about HALF the original — CORRECT. Watts et al. (2018) abstract: the bivariate correlation was only half the size of those in the original studies.
- Association shrank by a further two-thirds after controls — CORRECT. Watts et al. (2018) abstract: reduced by two thirds with controls for family background, early cognitive ability and home environment.
- Behavioural outcomes at age 15, small / mostly non-significant — CORRECT. Watts et al. (2018) abstract: associations with behavioural outcomes at age 15 were much smaller and rarely statistically significant.
- Most predictive variation from being able to wait ~20 seconds — CORRECT. Watts et al. (2018) abstract: most of the variation came from being able to wait at least 20 s.
- Shoda, Mischel & Peake (1990) as the original — CORRECT citation. Shoda, Mischel & Peake (1990), Developmental Psychology 26:978–986.
- Kidd et al. (2013), Cognition, waiting moderated by beliefs about reliability — CORRECT. Kidd, Palmeri & Aslin (2013), Cognition 126:109–114 (n = 28; reliable-condition children waited significantly longer).

## psych-gep-stem-01

- Stoet & Geary (2018), Psychological Science — CORRECT. Stoet & Geary (2018), Psychological Science 29(4):581–593.
- Psychological Science 29:581–593 — CORRECT. As above.
- 2019 corrigendum — CORRECT. Corrigendum to Stoet & Geary (2018), Psychological Science (2019), DOI 10.1177/0956797619892892.
- Headline metric was a propensity ratio a/(a+b), not the percentage of women among STEM graduates — CORRECT. The 2019 corrigendum's own clarification, as summarised in Richardson et al. (2020) and subsequent coverage.
- Richardson et al. (2020), Psychological Science, conclusions "likely spurious" — CORRECT. Richardson et al. (2020), Psychological Science 31(3):338–341, commentary on Stoet & Geary (2018).
- Richardson et al. pages 31:338–341 — CORRECT. Psychological Science 31:338–341 (2020).
- Paradox shrinks/disappears using BIGI — CORRECT. Richardson et al. (2020): with the Basic Index of Gender Inequality (Stoet & Geary's own BIGI) the paradox disappears; summarised in subsequent literature.
- "Most of 67 PISA nations" for the relative-strength pattern — CORRECT. Stoet & Geary (2018) PISA analysis as reported contemporaneously: across 67 countries/regions, girls' relative strength was reading and boys' was science in most countries.
- Charles & Bradley (2009) related cross-national pattern — CORRECT citation. Charles & Bradley (2009), American Journal of Sociology 114(4):924–976 (44 countries).

## psych-lead-crime-01

- "Neill (2007), Environmental Research" — **WRONG (author name).** The author is Rick **Nevin**, not Neill. Correct: Nevin (2007), Environmental Research 104(3):315–336, "Understanding international crime trends: The legacy of preschool lead exposure."
- Environmental Research 104:315–336 — CORRECT (for Nevin 2007, above). Environ Res 104(3):315–336.
- Reyes (2007), B.E. Journal of Economic Analysis & Policy — CORRECT. Reyes (2007): phase-out of leaded gasoline and violent crime, with ~20-year lags.
- Violent crime fell ~20 years after leaded-gasoline use peaked — CORRECT. Reyes (2007) and contemporary reporting: lead-exposure arc matches the violent-crime arc with a ~20-year lag (Nevin's crime-specific lags run 18–24 years, so ~20 is a fair central value).
- Billings & Schnepel (2018), remediation-eligibility / intervention design — CORRECT citation and design description. Billings & Schnepel (2018), American Economic Journal: Applied Economics 10(3):315–344, on CDC-recommended intervention for lead-exposed children.
- Aizer & Currie (2019), traffic-proximity / linked records with sibling comparisons — CORRECT citation. Aizer & Currie (2019), Review of Economics and Statistics 101(4):575–587.
- Feigenbaum & Muller (2016), lead water pipes instrumented — CORRECT citation and description. Feigenbaum & Muller (2016), Explorations in Economic History 62:51–86: lead pipes × water acidity / distance to refinery, higher later homicide.
- Grönqvist et al., Swedish register data on ~800,000 children — CORRECT. Grönqvist, Nilsson & Robling (2020), Journal of Political Economy 128(9): the study follows 800,000 children differentially exposed to the Swedish leaded-gasoline phase-out. (Seed gives no year for Grönqvist — the published version is 2020, not a working-paper year.)
- Higney, Hanley & Moro meta-analysis (2022) — CORRECT citation. Higney, Hanley & Moro, "The Lead-Crime Hypothesis: A Meta-Analysis" (2022).
- Meta-analysis of 24 studies — CORRECT. Higney et al. (2022): 24 studies pooled (529–542 estimates depending on version).
- Higney et al.'s conclusion as stated (supports individual-level link; lead likely not a significant factor in the aggregate decline; aggregate link generally overstated) — CORRECT paraphrase of Higney et al. (2022) and its published summaries.

## psych-stereotype-threat-01

- Spencer, Steele & Quinn (1999) — CORRECT citation. Spencer, Steele & Quinn (1999), Journal of Experimental Social Psychology 35:4–28.
- JESP 35:4–28 — CORRECT. As above.
- Flore & Wicherts (2015), Journal of School Psychology — CORRECT (journal as now stated in the seed; the Psychological Bulletin attribution in earlier drafts was wrong and FLAGS-RESOLVED correctly fixed it).
- Journal of School Psychology 53:25–44 — CORRECT. Flore & Wicherts (2015), J Sch Psychol 53:25–44.
- Pooled effect g = −0.22 — CORRECT. Flore & Wicherts (2015): pooled Hedges g = −0.22 across 47 samples of girls under 18.
- 47 samples — CORRECT. Flore & Wicherts (2015): 47 comparisons/samples (also reported as 47 in independent meta-analytic tables).
- Bias-adjusted g = −0.07, non-significant — CORRECT. Flore & Wicherts (2015): trim-and-fill adjusted g = −0.07, non-significant.
- "Zigerell (2017), J. Exp. Soc. Psychol. 69:181–193" — **WRONG.** No Zigerell stereotype-threat paper exists at that journal/volume/pages. The actual Zigerell (2017) stereotype-threat paper is "Potential publication bias in the stereotype threat literature: Comment on Nguyen & Ryan (2008)", **Journal of Applied Psychology 102(8):1159–1168**. FLAGS-RESOLVED §20 repeats the wrong JESP citation — do not inherit it.
- "Zigerell (2017) meta-analysing replication attempts found estimates centred near zero" — **WRONG (description).** Zigerell (2017) reanalysed the Nguyen & Ryan (2008) meta-analysis (it is not a meta-analysis of replication attempts) and found the bias adjustments **divergent** — from essentially no change, to a ~50% decrease, to near zero — and explicitly cautioned against claiming the effect is negligible on that basis. The seed's one-directional summary ("centred near zero") misstates his conclusion; soften to "bias adjustments produced divergent estimates, some near zero."
- Flore, Mulder & Wicherts (2019), large registered report — CORRECT citation and venue (Comprehensive Results in Social Psychology, published online 30 Jan 2019).
- N = 2,064 Dutch schoolgirls/students — CORRECT. Flore, Mulder & Wicherts (2019): N = 2,064 Dutch high-school students (age 13–14); among girls, no overall effect.
- Four theory-specified moderated effects, none found — CORRECT. Flore et al. (2019): four moderators tested (domain identification, gender identification, math anxiety, test difficulty); no moderated effects.
- Stoet & Geary review of 23 replication attempts of Spencer et al. — CORRECT. Stoet & Geary (2012), Review of General Psychology, as summarised in PLOS ONE (2022) conceptual-replication literature: 23 replication attempts reviewed.
- Only 55% consistent — CORRECT. Stoet & Geary (2012): only 55% of replicable-design articles had results consistent with Spencer et al.
- Half of those only after covariate adjustments the original did not make — CORRECT. Stoet & Geary (2012): half of the consistent results required statistical adjustment for pre-existing maths scores (of the unconfounded experiments, only 30% replicated).
- "Defending corpus is pre-2012 small-sample lab work with no large preregistered confirmation in a decade" — UNVERIFIABLE as stated. No named source states this composite claim in this form; its components are individually plausible (Stoet & Geary's review is 2012; Finnigan & Corker 2016 is a preregistered failure), but "no large preregistered confirmation in a decade" is a negative existential with no cited source. Recommend softening to a sourced formulation (e.g. cite Finnigan & Corker 2016 and Flore et al. 2019 as the large/preregistered attempts, both null) or cutting the decade clause.
- Ganley et al. (2013), no threat effect in schoolchildren — CORRECT citation and finding. Ganley et al. (2013), Developmental Psychology: 3 studies, total n = 931 students, no evidence of stereotype-threat effects on girls' maths performance. (Seed calls the sample "large" — 931 across three studies is defensible relative to the lab literature, but it is not a single large sample.)

## psych-iat-validity-01

- Oswald et al. (2013), J. Pers. Soc. Psychol. — CORRECT. Oswald, Mitchell, Blanton, Jaccard & Tetlock (2013), JPSP 105(2):171–192.
- JPSP 105:171–192 — CORRECT. As above.
- Mean correlation around r = 0.14 for race/ethnicity criteria — CORRECT. Oswald et al. (2013): aggregate r = .140 for the race/ethnicity criterion samples (86 samples, per Greenwald et al.'s 2020 summary of the three meta-analyses); Oswald's broader aggregate is cited as r = .148 by Greenwald, Banaji & Nosek (2015) — the seed's 0.14 matches the race/ethnicity figure it claims.
- IAT added no predictive power beyond explicit self-report — CORRECT. Oswald et al. (2013): IAT measures provided no more insight than explicit measures / no incremental validity over explicit measures.
- Greenwald et al. (2009) higher estimate r ~ 0.24 — CORRECT. Greenwald, Poehlman, Uhlmann & Banaji (2009): average predictive-validity r = .236.
- Greenwald et al. (2009) r = 0.236 (sources_note) — CORRECT. As above, confirmed in Greenwald, Banaji & Nosek (2015), JPSP 108(4):553–561, which contrasts GPUB r = .236 with Oswald et al. r = .148.
- Greenwald, Banaji & Nosek (2015) — CORRECT citation. JPSP 108(4):553–561, "Statistically small effects of the Implicit Association Test can have societally large effects."
- Oswald et al. (2015) reply, JPSP 108:562–571, "small effect sizes of unknown societal significance" — CORRECT. Oswald et al. (2015), JPSP 108(4):562–571, immediately following Greenwald et al. (2015) at 553–561 in the same issue.
