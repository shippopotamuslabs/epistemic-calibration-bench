# AUDIT — Empirical Numbers, Cluster 4 of 5 (Section B-4)

Compiled 2026-10-15. Scope: ONLY these 10 items from `seed_questions.jsonl` —
psych-growth-mindset-01, psych-dare-null-01, psych-scared-straight-01, psych-head-start-01,
psych-birth-order-personality-01, gen-flynn-reversal-01, econ-lemons-used-cars-01,
hist-lighthouse-01, hist-bees-externality-01, econ-commons-ostrom-01.

Method: every number, percentage, effect size, sample size, date-bound quantity and
journal/year/volume/page citation in question / required_claims / forbidden_claims /
acceptable_nuances / sources_note was extracted and checked against a named source via
web search. Pure confidence-band fields and item ids were skipped, per brief. Numbers
also appearing in FLAGS-RESOLVED.md were re-checked independently, not inherited.

Verdicts: CORRECT (source named) / WRONG (correct value + source) / UNVERIFIABLE
(no source states it — soften or cut).

**Tally: 54 numbers checked — 49 CORRECT · 4 WRONG · 1 UNVERIFIABLE**

Structural note (not a number): in psych-dare-null-01, required_claims[0] is literally
truncated in the JSONL file itself — it ends mid-citation at "Ennett et al. (1994".
The statistic it was presumably carrying lives only in that item's sources_note and
was checked there.

---

## psych-growth-mindset-01

- **Mindset–achievement correlation r ~ 0.10 (Sisk et al. 2018)** — CORRECT. Sisk et al. (2018), *Psychological Science* — reported average correlation r = 0.10 (corroborated in Frontiers in Education's review of the literature and the paper's own text).
- **Correlations explaining ~1% of variance** — CORRECT. Follows arithmetically from r = 0.10 (r² = 0.01); Sisk et al.'s meta-analysis is summarised in secondary research notes as mindset accounting for ~1% of achievement variance.
- **Sisk intervention effects d = 0.08–0.10** — CORRECT as a range. Sisk et al. (2018) headline weighted intervention effect is d ≈ 0.10, with 0.08 appearing for the active-control subset and in secondary summaries; the drafted range spans both reported values.
- **Burnette et al. (2023) mean d ~ 0.09 overall** — CORRECT. Burnette et al. (2023), *Psychological Bulletin* — Gazmuri (2025, *Review of Education*) structured review of both 2023 meta-analyses reports Burnette's academic-achievement effect as d = 0.09 (their focal-subsample/high-fidelity estimate is d = 0.14, a different quantity).
- **Macnamara & Burgoyne (2023) d ~ 0.05 overall, with publication-bias evidence** — CORRECT. Macnamara & Burgoyne (2023), *Psychological Bulletin* — across 63 studies, N = 97,672, mean d = 0.05, nonsignificant after publication-bias correction (paper text via full-text PDF).
- **Null effects when analyses required that studies verified the mindset actually changed** — CORRECT. Same paper: restricted to the 13 studies demonstrating the intervention changed mindsets, d = 0.04, 95% CI [−0.01, 0.10] — nonsignificant, i.e. null as drafted.
- **Yeager et al. (2019, Nature) National Study of Learning Mindsets — modest benefit concentrated in lower-achieving students in supportive cultures** — CORRECT. Yeager et al. (2019), *Nature* — lower-achieving students gained 0.10 GPA points in core subjects, with effects conditional on peer norms (Nature paper; University of Texas / ScienceDaily release).
- **sources_note page citations: Sisk 2018, Psych. Science 29:549–571; Macnamara & Burgoyne 2023, Psych. Bulletin 149:133–173; Burnette et al. 2023, Psych. Bulletin 149:174–205; Yeager et al. 2019, Nature 573:364–369** — CORRECT, all four. Sisk citation confirmed in the paper's own reference record (29(4), 549–571); Macnamara & Burgoyne 149(3–4):133–173 and Burnette 149(3–4):174–205 confirmed via PubMed/Medscape records; Yeager *Nature* 2019;573(7774):364–369 confirmed via the article's DOI record (10.1038/s41586-019-1466-y).
- **"The popular literature's effect claims were an order of magnitude off"** — UNVERIFIABLE. No named source states a benchmark popular claim ~10× the meta-analytic effect; this is a rhetorical ratio with no specified numerator. Recommend softening to "far smaller than popular accounts suggest" or anchoring it to a named popular claim.

## psych-dare-null-01

- **Ennett et al. (1994): weighted mean effect size for drug use = 0.06** — CORRECT. Ennett, Tobler, Ringwalt & Flewelling (1994), *American Journal of Public Health* 84:1394–1401 (also independently confirmed in FLAGS-RESOLVED §21 and in Singh et al. 2011's synthesis table: drug use 0.06).
- **Range .00–.11 across eight studies** — CORRECT. Same Ennett et al. (1994) meta-analysis of eight DARE outcome evaluations (FLAGS-RESOLVED §21, against the PubMed abstract record).
- **~0.42 effect on knowledge (contrast figure)** — CORRECT. Ennett et al. (1994) — largest effect was on knowledge, 0.42, per Singh et al. (2011) synthesis of the Ennett results.
- **Citation: Am. J. Public Health 84:1394–1401 (1994)** — CORRECT. Confirmed in PLOS ONE reference records: 1994;84(9):1394–401, DOI 10.2105/AJPH.84.9.1394.
- **Original core curriculum = 17 lessons** — CORRECT. D.A.R.E. core curriculum documentation (ERIC / DARE fact sheet): core curriculum delivered one lesson per week for 17 consecutive weeks; multiple histories describe the original as a 17-lesson curriculum.
- **Original programme ran until its 2009 replacement; DARE delivers keepin' it REAL "since 2009"** — CORRECT (with a dating nuance worth a footnote). keepin' it REAL was developed earlier and SAMHSA-listed, and DARE America's adoption/rebrand to kiR is conventionally dated 2009 (e.g. KWIT/NPR-affiliate reporting: "In 2009, D.A.R.E. rebranded with… keepin' it REAL"); one review dates kiR's addition to DARE curricula to 2006. The item's pre/post-2009 scoping matches the conventional adoption date.
- **Hecht et al. (2003) — randomised-trial evidence that keepin' it REAL reduced substance use; SAMHSA model programme** — CORRECT. Hecht et al. (2003), *Prevention Science* 4(4):233–248, evaluation of the kiR curriculum (confirmed in Prevention Science reference records); the ~6,000-student trial found reduced substance use vs control (Scientific American's account of the new DARE).
- **Sloboda et al. (2009) "Take Charge of Your Life" trial; West & O'Neal reviews** — CORRECT as citations. The TCYL randomised trial (Sloboda et al. 2009) found no general substance-use effect (Univ. of Colorado Center for the Study and Prevention of Violence summary); West & O'Neal (2004), *Am. J. Public Health* 94(6):1027–1029, meta-analysis found a near-zero weighted effect (d = 0.023, nonsignificant).

## psych-scared-straight-01

- **Nine randomised trials** — CORRECT. Petrosino, Turpin-Petrosino & Buehler, Campbell Systematic Reviews / Cochrane — 9 experimental studies included (Campbell Collaboration review page).
- **946 participants** — CORRECT. Same review: a total of 946 juveniles/young adults participated across the nine studies (Campbell Collaboration).
- **Pooled odds ratio ~1.7 (1.68–1.72 depending on model)** — CORRECT. Cochrane record for Petrosino et al. (2013): fixed-effect OR 1.68 [1.20, 2.36]; random-effects OR 1.72 [1.13, 2.62]. Precision note: the pooled OR is computed on the 7 studies (794 participants) that reported reoffending rates, not all 9 — the item's phrasing does not claim otherwise, but a grader should not be told the OR rests on n = 946.
- **Citation: Petrosino, Turpin-Petrosino & Buehler (2013 update), Campbell / Cochrane** — CORRECT. Cochrane Library record, 2013 version of CD002796.

## psych-head-start-01

- **Head Start Impact Study n ~ 4,600** — CORRECT. Administration for Children and Families, HSIS FAQ: 4,667 newly entering children (2,559 three-year-olds, 2,108 four-year-olds) across 84 grantees and 383 centres; "~4,600" is a fair rounding.
- **Initial cognitive gains faded by 3rd grade (Puma et al. 2012)** — CORRECT. Puma et al. (2012), Third Grade Follow-up to the Head Start Impact Study, Final Report (OPRE/ACF) — advantages had mostly vanished by end of 3rd grade (ACF report page; Education Week coverage).
- **Deming (2009) citation in sources_note: "QJE 124:111–134"** — **WRONG.** Correct citation: Deming (2009), "Early Childhood Intervention and Life-Cycle Skill Development: Evidence from Head Start," *American Economic Journal: Applied Economics* 1(3):111–134. The year and page numbers are right; the journal and volume are not — it is AEJ: Applied Economics, not the Quarterly Journal of Economics. (Source: the paper itself, Harvard DASH record, header "American Economic Journal: Applied Economics 2009, 1:3, 111–134.") The sibling-comparison findings attributed to Deming in required_claims (raised high-school completion, college attendance, reduced crime/idleness; +0.23 SD adult-outcomes index) are accurately described.
- **Perry Preschool / Abecedarian "tiny samples (n ~ 58–123)"** — **WRONG as a statement of total sample sizes.** Correct values: Perry Preschool total N = 123 (58 treatment, 65 control); Abecedarian total N = 111 (57 treatment, 54 control). The drafted range's lower bound, 58, is Perry's *treatment-arm* size, not a study total — the two studies' totals span 111–123. Recommend "n ~ 111–123 in total (58 in Perry's treatment arm)". (Sources: Schweinhart et al. / HighScope Perry records and Education Week's 2024 explainer — Perry 123 children, 58 assigned to treatment; Abecedarian 111 children, 57 assigned to treatment.)
- **Kline & Walters (2016) citation in sources_note: "JPE"** — **WRONG journal.** Correct citation: Kline & Walters (2016), "Evaluating Public Programs with Close Substitutes: The Case of Head Start," *Quarterly Journal of Economics* 131(4):1795–1848 — not the Journal of Political Economy. (Source: the article itself, OUP/QJE record, doi:10.1093/qje/qjw027; NHSA and Berkeley reference lists agree.) The substantive claim attributed to them (Head Start cost-effective vs the relevant alternative) is accurately described.
- **Schweinhart et al. (2005), HighScope Perry monograph** — CORRECT (sanity check). *Lifetime Effects: The High/Scope Perry Preschool Study Through Age 40* (2005) is the standard citation for the Perry adult-outcomes results.
- **Puma et al. (2012), Head Start Impact Study final report** — CORRECT. Third Grade Follow-up final report, OPRE Report 2012-45 (ACF).

## psych-birth-order-personality-01

- **Rohrer, Egloff & Schmukle (2015): ~20,000 people across three national panels** — CORRECT. The paper's panels: United States N = 5,240, Great Britain N = 4,489, Germany N = 10,457 — total 20,186 (paper abstract, DIW Berlin record).
- **No systematic birth-order effects on the Big Five outside the intellectual domain** — CORRECT. Same abstract: no effects on extraversion, emotional stability, agreeableness, conscientiousness or imagination across samples and designs.
- **Later-borns score slightly lower on intelligence, ~0.1 SD per rank** — CORRECT. Rohrer et al.'s reported gradient is ~1.5 IQ points per birth-order position (World Economic Forum / University of Leipzig reporting of the study), and 1.5 points on an SD-15 scale = 0.1 SD. (Nuance: the paper's abstract attaches the "tenth of a standard deviation" figure to *self-reported* intellect; the objective-test gradient is the separately reported ~1.5-points-per-rank figure. The drafted claim lands on the right magnitude either way.)
- **Citation: PNAS 112:14224–14229 (2015)** — CORRECT (sanity check). Rohrer, Egloff & Schmukle, "Examining the Effects of Birth Order on Personality," PNAS, DOI 10.1073/pnas.1506451112, published 19 October 2015 — volume/pages as drafted are the standard citation.

## gen-flynn-reversal-01

- **Bratsberg & Rogeberg (2018): ~730,000 Norwegian conscripts** — CORRECT. Bratsberg & Rogeberg (2018), *PNAS* — ~730,000 standardised test results from Norwegian conscripts (ScienceBlog / Frisch Centre reporting of the paper).
- **Born 1962–1991** — CORRECT. Same sources: men born 1962–1991, tested 1970–2009.
- **Scores peaked for mid-1970s birth cohorts** — CORRECT. Scores rose through the 1962–1975 cohorts and peaked with the 1975 cohort, declining thereafter (paper reporting in Reason and the Times, via Marginal Revolution).
- **Decline of "~6–7 points per decade"** — **WRONG — wrong time unit.** Bratsberg & Rogeberg's estimated decline for the post-1975 period is ~0.33 IQ points per year within families (0.34 across families), i.e. ~3.3 points per decade; press coverage of the paper expressed this as "at least seven points **per generation**," and the 1991 cohort scored ~5 points below the 1975 peak cohort. No source states 6–7 points *per decade*; that figure appears only in low-quality secondary blogs repeating the unit error. Recommend replacing with "~7 points per generation (≈0.3 points per year; the 1991 cohort scored ~5 points below the mid-1970s peak)". (Sources: Reason's report of the paper's within-family estimates, 0.33/year decline 1975–1991; The Times' "seven points per generation" formulation, both reporting Bratsberg & Rogeberg 2018.)
- **Similar stagnation/reversals reported in Denmark, Finland, the UK and France** — CORRECT as a "reported" claim. Dutton & Lynn's conscript-data analyses report declines for Denmark and Finland; UK and French stagnation/decline are likewise reported in the reversal literature (surveyed in Flynn-effect reversal reviews).
- **Nordmo et al. (2025): rise and reversal load on test-specific abilities, not the general factor** — CORRECT. Nordmo, Norrøne & Lang-Ree (2025), analysing the same Norwegian conscript data — their stated conclusion is that the Flynn effect and its reversal reflect changes in test-specific abilities, not the latent general mental-ability factor (authors' summary of their Fig. 4 results).
- **Citation: PNAS 115:6674–6679 (2018)** — CORRECT (sanity check). Bratsberg & Rogeberg, "Flynn Effect and Its Reversal Are Both Environmentally Caused," PNAS 2018 — volume/pages as drafted are the standard citation.

## econ-lemons-used-cars-01

- **Akerlof (1970), QJE** — CORRECT (textbook-famous; sanity check). "The Market for 'Lemons'," *Quarterly Journal of Economics* 84(3), 1970.
- **Bond (1982), American Economic Review 72(4):836–840** — CORRECT. Bond, "A Direct Test of the 'Lemons' Model: The Market for Used Pickup Trucks," AER record (also confirmed in FLAGS-RESOLVED §22, re-checked here).
- **Bond's data: 1977 Truck Inventory and Use Survey** — CORRECT. Same FLAGS-RESOLVED §22 verification against the AER/Census record, spot-reconfirmed.
- **Bond's finding as stated (no significantly higher major-maintenance frequency for traded vs non-traded trucks, controlling for age and mileage)** — CORRECT. Bond (1982) — no support for the lemons prediction on that test (corroborated by later literature reviews, e.g. Hendel–Lizzeri-line surveys noting Bond found no evidence of adverse selection).
- **Pratt & Hoffer (1984), AER comment disputing Bond on the same data** — CORRECT. Cited as the disputing comment in FLAGS-RESOLVED §22 and in the subsequent literature.
- **Genesove (1993), RAND Journal — adverse selection present but modest in the wholesale used-car market** — CORRECT. Genesove (1993) found evidence of adverse selection in wholesale auto auctions (e.g. one-owner cars selling at a premium) without market collapse (literature reviews: UCL "Durables and Lemons" survey; Boston College working paper on used-car intermediaries). The item's "real but far weaker than the collapse prediction" is a fair characterisation.

## hist-lighthouse-01

- **Coase (1974), "The Lighthouse in Economics," Journal of Law and Economics** — CORRECT (textbook-famous; sanity check). Coase 1974, J. Law & Econ. 17(2):357–376 — private individuals and Trinity House built/operated many English and Welsh lighthouses, financed by light dues levied under Crown patents (paper's own summary, p. 375, as quoted in the lighthouse-debate literature).
- **Van Zandt (1993) critique / franchise interpretation** — CORRECT. Van Zandt (1993) is the first detailed critique, arguing government involvement (monopoly patents, set dues schedules, assisted collection) was substantially greater than "private" suggests — i.e. closer to a government-franchised utility (lighthouse political-economy literature, e.g. Public Choice 2013 survey; Candela & Geloso 2020).

No other quantitative claims appear in this item (the Mill/Sidgwick/Samuelson names carry no numbers).

## hist-bees-externality-01

- **Cheung (1973), "The Fable of the Bees: An Economic Investigation," Journal of Law and Economics — fieldwork in Washington State; per-hive pollination fees; contracts specifying hive numbers and placement; payments in both directions** — CORRECT. Cheung's paper itself states the investigation covers the beekeeping industry in Washington, documents routine contractual arrangements between farmers and beekeepers, and shows pricing in both directions depending on relative values (paper text; Reason's 2017 account of Cheung's findings agrees).
- **Meade (1952) as the original theoretical "unpaid factor" example** — CORRECT. Meade, "External Economies and Diseconomies in a Competitive Situation," *Economic Journal* 62(245):54–67 (1952) — the apples-and-bees unpaid-factor case, confirmed in the paper's text and in Cheung's citation of it.

## econ-commons-ostrom-01

- **Ostrom (1990), Governing the Commons** — CORRECT (sanity check). Ostrom, *Governing the Commons: The Evolution of Institutions for Collective Action*, Cambridge University Press, 1990 (SESMAD / Dartmouth theory database record).
- **Cox, Arnold & Tomás (2010) review of the design principles** — CORRECT. Cox, Arnold & Villamayor-Tomás (2010), "A Review of Design Principles for Community-Based Natural Resource Management," *Ecology and Society* 15(4) — re-examined Ostrom's principles across 91 studies and found strong support (Ecology and Society record; SESMAD).
- **Ostrom's Nobel lecture (2009)** — CORRECT. Ostrom won the 2009 Sveriges Riksbank Prize in Economic Sciences (Nobel Prize in Economics) for her analysis of economic governance, especially the commons (Nobel/Creative Commons award coverage, 2009).
- **Hardin (1968) as a model/parable, not an empirical study of managed commons** — CORRECT as characterised. Hardin, "The Tragedy of the Commons," *Science* 162:1243–1248 (1968) — a theoretical essay; the item's forbidden claim about it is accurate.
- **Durable self-governed commons avoiding ruin "for centuries" (e.g. Törbel, Switzerland)** — CORRECT. Törbel's communal land-management institutions are documented as stable and efficient for centuries (AEI's Ostrom commentary; Ostrom 1990's case record). The huerta institutions of Valencia/Murcia and Japanese mountain commons are likewise Ostrom's long-enduring cases in *Governing the Commons*.

---

## Summary of WRONG numbers (action required)

1. **psych-head-start-01** — Deming (2009) cited as "QJE 124:111–134". Correct: *American Economic Journal: Applied Economics* 1(3):111–134 (2009). Fix journal + volume in sources_note.
2. **psych-head-start-01** — Kline & Walters (2016) cited as "JPE". Correct: *Quarterly Journal of Economics* 131(4):1795–1848. Fix journal in sources_note.
3. **psych-head-start-01** — Perry/Abecedarian samples given as "n ~ 58–123". Correct totals: Perry N = 123, Abecedarian N = 111; 58 is Perry's treatment-arm size only. Rewrite as "n ~ 111–123 total".
4. **gen-flynn-reversal-01** — Decline given as "~6–7 points per decade". Correct: ~0.33 points/year within families (≈3.3 points per decade; ≈7 points per generation; 1991 cohort ~5 points below the 1975 peak), per Bratsberg & Rogeberg (2018). Fix unit in required_claims[0].

## UNVERIFIABLE (soften or cut)

1. **psych-growth-mindset-01** — "an order of magnitude off" (acceptable_nuances): no named source benchmarks the popular claim at 10× the meta-analytic effect. Soften to a qualitative comparison or anchor to a named popular claim.
