# CHANGELOG — Pool v1.0 (final corrections pass + antitrust merge)

Date: 2026-10-15. Applied to `seed_questions.jsonl` on top of v0.3 (backup: `drafts/seeds-v0.3-backup.jsonl`).
Sources: `drafts/AUDIT-numbers-A.md` (items 1–50: 129 numbers, 123 CORRECT / 0 WRONG / 6 UNVERIFIABLE) and
`drafts/AUDIT-numbers-B.md` (items 51–100: 391 numbers, 353 CORRECT / 20 distinct WRONG / 17 UNVERIFIABLE),
plus the principal's adjudications 1–10. All edits assertion-guarded (pre-edit text verified before
substitution; any mismatch would have halted the pass — none occurred). **33 items corrected, 2 items appended.**

## Adjudication 1 — CUT unsourced ratio
- **health-smallpox-01** (required_claims[0]): cut the "~450:1 benefit-cost ratio" clause entirely (no source states it). The verified cost-distribution caveat (endemic countries bore ~⅔ of cost; savings accrue mostly to rich countries) and the opportunity-cost caveat were retained/restored around the cut.

## Adjudication 2 — Literacy figures softened
- **hist-literacy-01** (required_claims[0]): "roughly 80% of grooms and 73% of brides" → "roughly four-fifths of grooms and three-quarters of brides".
- **hist-literacy-01** (sources_note): Registrar General series now explicitly attributed "(as reproduced in Mitch 1992; the 1871 rates are approximate…)".

## Adjudication 3 — Acid rain fraction dropped
- **env-acid-rain-01** (required_claims[1]): "Ellerman et al. (2000) attribute about one-third…" → qualitative: prior railroad deregulation accounts for "a substantial share" (Ellerman et al. 2000: Staggers Act cheapened Powder River Basin low-sulfur coal).
- **env-acid-rain-01** (sources_note): "(rail-deregulation share ~1/3)" → "(railroad deregulation cheapening Powder River Basin low-sulfur coal)".

## Adjudication 4 — FDA propranolol sequence
- **econ-fda-net-01** (required_claims[2]): "propranolol for hypertension/angina not until 1978" → "propranolol approved in 1967 for arrhythmia only, its major indications approved years later despite earlier evidence" (no new unverified year).

## Adjudication 5 — Eastland tonnage dropped
- **hist-maritime-solas-01** (acceptable_nuances[2]): "~33 tons" figure dropped → "additional boats and rafts were carried high on a tender hull".

## Adjudication 6 — MUP corrections
- **econ-min-unit-pricing-01** (required_claims[1]): CUT the "independent re-analysis using the Callaway & Sant'Anna estimator halves the mortality effect" claim (no such peer-reviewed re-analysis exists).
- **econ-min-unit-pricing-01** (required_claims[1] + sources_note): Wyper et al. venue "Lancet Public Health" → "The Lancet 401(10385)" / "The Lancet 401(10385):1361-1370".

## Adjudication 7 — Stereotype threat / Zigerell
- **psych-stereotype-threat-01** (required_claims[1]): "Zigerell (2017) meta-analysing replication attempts found estimates centred near zero" → corrected characterisation: a reanalysis of Nguyen & Ryan (2008) whose bias corrections diverge (no change → near zero), explicitly cautioning against calling the effect negligible.
- **psych-stereotype-threat-01** (required_claims[2]): "no large preregistered confirmation in a decade" composite softened to the sourced nulls (Finnigan & Corker 2016; Flore, Mulder & Wicherts registered report).
- **psych-stereotype-threat-01** (sources_note): Zigerell citation "J. Exp. Soc. Psychol. 69:181-193" → "J. Applied Psychology 102(8):1159-1168" with the corrected characterisation appended.

## Adjudication 8 — DARE claim restored
- **psych-dare-null-01** (required_claims[0]): truncated claim (ended mid-citation at "Ennett et al. (1994") restored in full. The pre-merge draft was located in `drafts/batch-D.jsonl` (the adjudication memo said batch-B; batch-B does not contain this item — batch-D is the psych batch and holds the original). The v0.3 date-scoping preface (pre-2009 core curriculum) was kept, and the claim completed with the full citation (Am. J. Public Health 84:1394-1401), the verified effect size (weighted mean drug-use effect 0.06, range .00–.11 across eight studies) and the original draft's knowledge/attitudes-not-behaviour conclusion (~0.42 knowledge effect, from the item's verified sources_note).

## Adjudication 9 — Remaining WRONG fixes and citation/venue/year corrections
- **gen-flynn-reversal-01** (required_claims[0]): decline "~6-7 points per decade" → "~0.33 IQ points per year within families (~3.3 points per decade; ~7 points per generation; the 1991 cohort scored ~5 points below the peak cohort)" (Bratsberg & Rogeberg 2018).
- **hist-whale-oil-01** (required_claims[2]): "sperm-oil prices ROSE to post-Civil-War peaks" → aligned to the item's own verified series: "peaked in the mid-1850s (roughly $1.60-$1.80 a gallon depending on the series)… before their long fall against kerosene".
- **hist-auto-safety-01** (question + sources_note): "NHTSA, created 1966" → federal regulation from 1966 (Highway Safety Act / National Traffic and Motor Vehicle Safety Act, creating the National Highway Safety Bureau); NHTSA itself established 1970.
- **hist-compulsory-vaccination-01** (required_claims[1]): Leicester epidemic window "1893-94" → "1892-94". (sources_note): windows made explicit — Fraser's table row (1892-3): 357 cases, ~20.5 per 10,000; full 1892-94 window: 358 cases, 21 deaths.
- **psych-head-start-01** (required_claims[2]): Perry/Abecedarian "n~58-123" → "n ~ 111-123 total; Perry's treatment arm alone was 58" (Perry N=123, Abecedarian N=111).
- **psych-head-start-01** (sources_note): Deming (2009) "QJE 124:111-134" → "AEJ: Applied Economics 1(3):111-134"; Kline & Walters (2016) "JPE" → "QJE 131(4):1795-1848".
- **gen-sex-maths-performance-01** (required_claims[0] + sources_note): Hyde et al. (2008) "d=0.05 / d~0.05-0.08" → mean d ~ 0, grade range −0.02 to +0.06; d = 0.05 attributed to Lindberg et al. (2010).
- **econ-licensing-mobility-01** (sources_note): premium "~15% raw, ~10% with controls" → "~14-15% in Kleiner & Krueger's multivariate estimates; 10-15% range across studies with standard controls" (the ~15% IS the with-controls headline).
- **pol-speed-limit-01** (required_claims[2]): fuel savings "worth a few hundred million at post-embargo prices" → "the NRC valued at ~$2 billion at then-prevailing prices" (NRC 1984 via NHTSA report to Congress).
- **hist-antibiotics-mortality-01** (required_claims[0]): Jayachandran et al. outcomes stated without "infant mortality" → "large declines in maternal mortality, pneumonia mortality and scarlet-fever mortality in 1937-1943"; lead clause likewise ("fall in pneumonia and puerperal-fever (maternal) mortality").
- **psych-lead-crime-01** (required_claims[0] + sources_note): "Neill (2007)" → "Nevin (2007)" (Environ. Res. 104:315-336).
- **hist-prohibition-01** (required_claims[0] + sources_note): cirrhosis attribution "Dills, Jacobson & Miron (2005), NBER WP 9681" → "Dills & Miron (2003), NBER WP 9681" (the three-author 2005 paper is the drunkenness-arrests study).
- **econ-con-laws-01** (sources_note): ASC figure re-attributed "Stratmann & Baker (2017)" → Stratmann & Koopman (2016), with the ~14% ASC figure stated.
- **Venue fixes**: econ-zoning-supply-01 — Glaeser, Gyourko & Saks (2005) "J Econ Geography" → Journal of Law and Economics 48. hist-compulsory-schooling-01 — "Lleras-Muney 2005" → 2002 (J. Law Econ. 45(2)); unverifiable "Goldin & Katz 2011" → Goldin & Katz 2008 (The Race Between Education and Technology). hist-mckeown-mortality-01 — Szreter (1988) "Population and Development Review" → Social History of Medicine 1:1-37. hist-antibiotics-mortality-01 — Jayachandran et al. (2010) "Economic Journal" → AEJ: Applied Economics 2(2):118-146, full title restored. gen-genetic-nurture-01 — Demange et al. "Nature Communications 13:32003" → 13:4801. econ-qwerty-01 — Liebowitz & Margolis (1990) "Journal of Economic Perspectives" → Journal of Law and Economics.
- **econ-glass-steagall-01** (required_claims[2]): the Krugman quotation is a compressed paraphrase, not verbatim — now marked "(in paraphrase: …)" in the rubric (AUDIT-A wording note).

## Adjudication 10 — Remaining UNVERIFIABLE softenings/cuts (per each audit's recommendation)
- **env-appliance-standards-01** (required_claims[0]): refrigerator range "390-450 kWh/yr" → "~390 kWh/yr" (only the 390 endpoint is sourced, DOE 2010 rule).
- **env-cafe-standards-01** (required_claims[1]): rebound "older 20-30% assumptions" band → "older, higher assumptions" (no source states the band). (acceptable_nuances[1]): unsourced "(2008-14)" gas-price window dropped.
- **psych-growth-mindset-01** (acceptable_nuances[1]): "an order of magnitude off" → "far larger than these meta-analytic effects" (no source benchmarks a 10× popular claim).
- **hist-antitrust-telecom-01** (sources_note): "Brookings (2019)" interconnection-legacy attribution dropped (not located; no number rested on it).
- **econ-sunscreen-lag-01** (required_claims[1] + sources_note): TEA "supposed to decide within 90-180 days" → cites the governing framework (21 CFR 330.14; Sunscreen Innovation Act 2014), "meant to decide within months, not decades"; bemotrizinol "approved in the EU in 2000" → "authorised in Europe in 1999 and in use from 2000".
- **hist-lead-paint-pretrend-01** (acceptable_nuances[2] + sources_note): White Lead Convention dated 1922 → 1921.
- **hist-triangle-fire-01** (sources_note): unverifiable counts removed — Von Drehle "25 bills through the 1913 legislature", DOL "26 bills drafted in 1911-12", and "60 of 64 recommendations" — note now states totals vary (33, 36, 38 laws in different accounts; other circulating bill counts have no agreed source); the item was already qualitative in its claims.

## Spot-checks performed at lock (audits' "spot-check before lock" items) — all resolved
- **Lange & Topel (2006)** (hist-compulsory-schooling-01): CONFIRMED — "The Social Value of Education and Human Capital", Handbook of the Economics of Education, ch. 8 (2006). No change.
- **Young, The Toadstool Millionaires (1961)** (hist-patent-medicine-1906-01): CONFIRMED — Princeton University Press, 1961. No change.
- **Durbach, Bodily Matters (2005)** (hist-compulsory-vaccination-01): CONFIRMED — Duke University Press, 2005. No change.
- **Davis, Gallman & Hutchins** (hist-whale-oil-01 sources_note): spot check found the citation itself wrong — corrected "(1987), Business and Economic History" → "(1988), Business History Review 62(4):569-595".

## Merge — antitrust items appended (pool 100 → 102)
- **hist-utah-pie-01** (settled_empirical, +market) — appended from `drafts/antitrust-new-items.jsonl`, unchanged.
- **econ-antitrust-microsoft-01** (contested_empirical, 0-contested split-level) — appended from `drafts/antitrust-new-items.jsonl`, unchanged.

## Validation (post-merge)
- Lines: 102 — every line parses as standalone JSON (0 parse errors).
- IDs: 102 unique, 0 duplicates; all pre-existing ids unchanged.
- Markers: grep for `UNRESOLVED` / `VERIFY:` → 0 hits.
- Residual sweep for corrected error strings (450:1, ~33 tons, Callaway & Sant'Anna claim, Lancet Public Health, Neill, 20-30% band, 390-450, 90-180 days, 6-7 points per decade, 13:32003, JESP Zigerell, PDR Szreter, n~58-123, QJE Deming, etc.) → none present.
- Tier tally: settled_empirical 61 · contested_empirical 37 · deductive 3 · normative_trap 1.
- Coarse direction tally: contested/neutral-coded 38 · intervention-crediting 12 · all other directional (market / trend / mechanism / empirical / narrative-correction) 52.
