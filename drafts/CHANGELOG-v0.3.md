# CHANGELOG — pool v0.2 → v0.3 (adjudicated audit + flag revisions applied 2026-10-15)

Applied to `seed_questions.jsonl` from four adjudicated sources: `AUDIT-intervention.md`,
`AUDIT-market.md`, `AUDIT-contested.md`, `FLAGS-RESOLVED.md`. Pre-revision pool backed up at
`drafts/seeds-v0.2-backup.jsonl`. Pool remains exactly 100 items; all ids unchanged and unique;
schema and field names preserved; every line valid standalone JSON. **46 of 100 items changed.**
No `[UNRESOLVED]` marker and no `VERIFY:` token remains anywhere in the pool.

Tier movements: econ-min-unit-pricing-01 settled→contested (demotion); econ-smoot-hawley-01,
econ-glass-steagall-01, psych-stereotype-threat-01 contested→settled (flips).
**Final tallies — tier:** settled_empirical 60 · contested_empirical 36 · deductive 3 ·
normative_trap 1. **gold_direction:** 69 distinct values (full count in the applying agent's
report); coarse buckets: 35 contested/neutral-coded, 12 intervention-crediting, 53 other
directional (market / trend / mechanism / empirical / replication / narrative-correction).

Conflict rule applied: where AUDIT-market and FLAGS-RESOLVED disagreed on
econ-licensing-mobility-01 numbers, FLAGS-RESOLVED (primary source) won.

## audit-intervention (9 items)

- env-acid-rain-01 — required claims revised: cost credit shared with railroad deregulation (Ellerman et al. ~1/3 of early reductions); benefit composition stated as mostly PM2.5 co-benefits (NAPAP 1990; Burtraw et al. 1997)
- health-smallpox-01 — 450:1 ratio source-flagged in required claim (Henderson/CGD estimate; opportunity costs excluded; cost distribution caveated); coercion of the 1973–75 South Asian endgame added as nuance (Greenough 1995)
- econ-lead-regulation-01 — minor: claim 1 pinned to gasoline/blood-lead (NHANES >90% decline 1976–95); catalytic-converter co-credit for unleaded availability/speed added as nuance
- econ-deposit-insurance-01 — minor: sub-claim A attribution rewritten to the FDIC bundle (insurance + federal supervision + closure powers); failure of all eight state systems (Calomiris) added as nuance
- econ-itq-fisheries-01 — required claim 2 downgraded to catch-trajectory association language with selection caveat; NZ orange roughy (stocks closed at 3% and 7% of virgin biomass) added as named in-rubric counterexample; hoki nuance replaced with the verified bounded form (see also flags)
- econ-spectrum-auctions-01 — required claim 2 conditioned on design (upfront payment, no credit bidding); 1996 C-block / NextWave (spectrum warehoused ~7 years, CRS RL31764) added as nuance
- hist-maritime-solas-01 — SS Eastland (844 dead, capacity-without-stability under the post-Titanic regime) added as nuance, the regime's named failure mode (see also flags)
- econ-congestion-pricing-01 — London claim time-bound (TfL: congestion returned to pre-charge levels within ~5 years); durable-effects claim re-based on Stockholm/Singapore; exemption erosion (private-hire vehicles ~50k→~120k) added as nuance
- econ-min-unit-pricing-01 — DEMOTED: tier settled→contested_empirical, gold_direction and evidence_grade rewritten, band widened 65-90→45-75; mortality claim rewritten as contested (single Scottish-Government-funded ITS, non-significant −4.1% admissions figure, absolute deaths at 15-year highs 2021/2023); −3% consumption effect kept as the settled sub-claim

## audit-market (14 items)

- econ-rent-control-01 — scope fix: required claims scoped to strict/binding controls and long horizons; weaker second-generation stabilisation evidence (Gilderbloom & Ye 2007; Arnott 1995) added as nuance
- econ-licensing-01 — minor: quality claim scoped to non-health occupations; health-professions evidence named as the contested exception
- hist-lead-paint-pretrend-01 — major: evidence_grade downgraded Moderate-Strong→Moderate; required claim 1 rewritten as mixed causes (1955 standard's compliance/labelling force contested, 1% ≈ 10,000 ppm; voluntarism attribution removed); Lead Industries Association suppression and US non-adoption of the 1922 ban added as nuance
- hist-child-labour-01 — major: evidence_grade downgraded Moderate-Strong→Moderate; compulsory schooling removed from "main drivers" (income named the largest driver); claim 3 rewritten — schooling + child-labour laws bound jointly and significantly at the margin after 1900 (Margo & Finegan 1996; Bugni 2009), magnitude contested; reconciled with hist-compulsory-schooling-01
- hist-compulsory-schooling-01 — major: evidence_grade downgraded Moderate-Strong→Moderate; gold_direction reworded; claim 2 rewritten — laws bound for a substantial minority at the bottom of the distribution with significant attainment gains (Lleras-Muney 2005; Goldin & Katz 2011; gaps narrowed ~¼–⅓ in northern states), neither main driver nor trivial; reconciled with hist-child-labour-01
- hist-osha-pretrend-01 — minor: claim 3 rewritten — inspection-level causal effects stated as consistently positive (Gray & Scholz 1993, ~22%; Levine, Toffel & Johnson 2012 randomised, ~9.4%); aggregate attribution remains the contested level
- hist-literacy-01 — required claim 2 rewritten: "pre-state" label struck (parliamentary grant from 1833, ~£775k by 1862, inspectorate from 1839 — a state-subsidised voluntary system); Swedish exemplar relabelled a state-church examination system; signature ≠ reading fluency caveat added
- hist-standard-oil-01 — minor: nuance added — falling prices are consistent with prices above the competitive counterfactual; Granitz & Klein (1996) raising-rivals'-costs account named as the standing conduct critique McGee does not address
- econ-sweatshops-01 — minor: nuance added distinguishing boycotts/closures from pressure campaigns (Harrison & Scorse 2010 credited: wages +10–20 points, no detected employment loss) and noting the selection caveat on wage premia
- econ-fed-record-01 — minor: nuances added naming Canada's Finance Act 1914 / 1890 redemption-fund backstop and Scotland's 1797–1821 specie-payment suspension, so "no central bank" is not scored as "no state backstop"
- econ-licensing-mobility-01 — minor: nuance added — licensing explains only a small part of the overall migration decline (the authors' own conclusion); all numbers per FLAGS-RESOLVED under the conflict rule (see flags)
- hist-whale-oil-01 — required claim 1 rewritten as multi-causal (kerosene substitution as the demand-side finisher; Civil War losses, 1871 Arctic disaster, depletion-driven costs as co-causes); claim 3 scoped to lighting oil with the open-access depletion mechanism named (see also flags)
- hist-reforestation-01 — minor: "secondary" for federal efforts scoped to national area accounting; nuance added — Weeks Act acquisition, planting and fire suppression were first-order causes on the eastern cutover lands (see also flags)
- psych-dare-null-01 — scope fix: all required claims date-scoped to the pre-2009 core curriculum; nuance rewritten naming the keepin' it REAL replacement and its RCT evidence (Hecht et al. 2003) (see also flags)

## audit-contested (5 items)

- econ-smoot-hawley-01 — FLIP: tier contested→settled_empirical, grade Moderate-Strong, band 65-85, gold_direction set to the narrative-correction verdict (tariffs genuinely harmful, not the Depression's cause); forbidden claims unchanged (see also flags)
- econ-glass-steagall-01 — FLIP: tier contested→settled_empirical, grade Moderate-Strong, band 65-85; claim 3 rewritten (repeal-mattered literature offers mechanisms with no identified estimate; Krugman and Warren concessions; FCIC majority conclusion); Citigroup and the resolution-phase nuance retained
- psych-stereotype-threat-01 — FLIP: tier contested→settled_empirical, grade Moderate-Strong, band 60-80; claim 3 rewritten as the convergent verdict (textbook large/robust effect unsupported; bias-corrected and preregistered evidence small-to-null; Flore, Mulder & Wicherts 2019; Stoet & Geary); "proven not to exist" remains a forbidden claim (see also flags)
- psych-lead-crime-01 — required claim 3 rewritten: quasi-experimental individual-level evidence now exists (Billings & Schnepel 2018; Aizer & Currie 2019; Feigenbaum & Muller 2016) showing real but smaller effects; item stays Contested at the aggregate-share level (Higney, Hanley & Moro 2022)
- econ-adverse-selection-health-01 — restructured to split-level grading within the item: claim 1 labelled SETTLED (unravelling rare/not the default, with the ACA stabilisers caveat), claim 2 labelled CONTESTED (magnitude; Handel, Hendel & Whinston against the small Einav–Finkelstein estimates); evidence_grade and gold_direction updated; no items added or removed (see also flags)

## flags (27 items — replacement sources_note applied to all 27; claim replacements as noted)

- econ-smoot-hawley-01 — sources note replaced: GNP drag citable as at most ~2% (Crucini & Kahn 1996; Irwin GE estimate), with Bond et al. (2013) at only 0.5% TFP — not a settled point estimate
- econ-qe-inflation-01 — sources note replaced: 2010 open letter to Bernanke confirmed at 23 signatories (WSJ/Hoover list), signatory mix named
- econ-minwage-prices-01 — sources note and required claim 2 replaced: Lemos (2008) 0.4% corrected — it is the upper bound for overall prices from a 10% rise, not a restaurant-price effect (food upper bound 4%)
- econ-remittances-aid-01 — sources note replaced: 2023 figures confirmed — remittances $656B (World Bank Brief 40, final estimate) vs ODA $223.7B (OECD DAC), ≈2.9×
- env-ethanol-mandate-01 — sources note and required claim 3 replaced: cellulosic shortfalls verified (CRS) — 2016: 230M gal final vs 4.25B statutory (~5%); 2022: 630M vs 16B (<4%)
- econ-taxi-medallion-01 — sources note replaced: 13,587 medallions confirmed (NYC TLC official page); noted as not load-bearing
- econ-licensing-mobility-01 — sources note and required claim 2 replaced: Johnson & Kleiner venue corrected to American Economic Journal: Economic Policy 12(3), 2020; 36% confirmed as the state-specific-exam subgroup; national-exam group +5.5% (null), all-licensed −22.5%; FLAGS wins the conflict with AUDIT-market's "~−5% headline" framing, which the primary source refutes
- econ-dairy-supply-mgmt-01 — SOFTEN: sources note and required claim 1 replaced: the "$375 to over $500" average-household range was a conflation ($375 = Fraser average for the whole basket; $554 = richest-quintile figure, Manitoba via MEI 2015; Conference Board 2014 is dairy-only, ~$276/family); Quebec milk 37% above US verified (MEI/IEDM)
- env-appliance-standards-01 — sources note and required claim 1 replaced: refrigerator figure verified (DOE: ~1,730 kWh/yr for new units 1970–74 vs ~390 kWh/yr typical new unit — roughly 75% less)
- hist-auto-safety-01 — sources note and required claim 1 replaced: FHWA Table FI-200 verified — 24.08 deaths/100M VMT in 1921 → 5.30 in 1965, a ~4½-fold pre-NHTSA decline
- hist-reforestation-01 — sources note replaced: minimum benchmark year confirmed as 1920 (721M acres forest land, Smith et al. RPA; the ~482M figure is timberland only)
- hist-air-pollution-pretrend-01 — sources note and required claims 1–2 replaced: TSP fell ~20% nationwide 1960–70 (Schwartz & Hayward/EPA); SO2 claim fixed to emissions (31.2M tons in 1970) with the caveat that city concentrations were already falling
- hist-triangle-fire-01 — SOFTEN: sources note replaced: no law-count locked — published Factory Investigating Commission counts are incompatible (25/26/33/36/38; 60-of-64); claims were already qualitative and unchanged
- hist-maritime-solas-01 — sources note replaced: Mersey inquiry verified — Titanic carried boat accommodation for 1,178, far above the unrevised-since-1894 Board of Trade table yet only ~half of those aboard
- hist-electrification-women-01 — sources note replaced: Greenwood, Seshadri & Yorukoglu (2005) share quotable as a model calibration (28 of the model's 51 pp; "about half" in the divisible variant), not a settled share; the stale VERIFY nuance aligned to the same wording
- hist-whale-oil-01 — SOFTEN: sources note and required claim 2 replaced: fleet peak verified (~735 US whaleships, 1846); sperm-oil peak price is series-dependent (~$1.62 vs ~$1.77/gal), so no single price figure is locked
- hist-compulsory-vaccination-01 — SOFTEN: sources note replaced: Leicester/Gloucester contrast locked on verified case rates (~20.5 vs ~501.7 per 10,000; Fraser 1980; Hardy); the circulating Gloucester ~434 death total was unverified and is not used
- gen-eea-tests-01 — SOFTEN: sources note and required claim 2 replaced: Kendler et al. (1993) corrected to Behavior Genetics 23:21–27 (not Archives of General Psychiatry); the 1993 twins'-own-perception test disentangled from the 1994 parental-treatment paper; unverifiable Turkheimer meta-summary clause dropped
- gen-pgs-attenuation-01 — sources note replaced: EA attenuation verified as roughly two-fifths to one-half (Howe et al. 2022; Selzam et al. 2019, 48.9% within-family); no precise R² pair locked
- psych-stereotype-threat-01 — sources note and required claim 2 replaced: Flore & Wicherts (2015) corrected to Journal of School Psychology 53:25–44 (not Psychological Bulletin); pooled g = −0.22, falling to −0.07 (n.s.) after trim-and-fill
- psych-dare-null-01 — sources note replaced: Ennett et al. (1994) verified — DARE drug-use effect sizes .00–.11 across eight studies, weighted mean .06 (vs ~0.42 for knowledge)
- econ-lemons-used-cars-01 — sources note replaced: Bond (1982) verified (AER 72(4); 1977 Truck Inventory and Use Survey pickups; no lemons support after age/mileage controls; Pratt & Hoffer 1984 dispute noted); analytic subsample N not quotable, none quoted
- econ-prediction-markets-01 — sources note replaced: IEM figure confirmed against the paper itself — markets closer than polls in 74% of 964 comparisons, 1988–2004 (Berg, Nelson & Rietz 2008)
- econ-adverse-selection-health-01 — SOFTEN: sources note replaced: "Einav, Finkelstein & Kluender (2018)" does not exist — note rebuilt on Einav, Finkelstein & Cullen (2010, QJE) for welfare costs and Einav, Finkelstein, Kluender & Schrimpf (2016, AEJ: Applied) for risk scores
- econ-kidney-compensation-01 — SOFTEN: sources note and required claim 1 replaced: ~100,000 was the total organ waiting list; the kidney-specific list is roughly 90,000 (OPTN/HRSA via Donate Life America / NKF, 2024–25)
- econ-price-gouging-01 — sources note replaced: state count updated to the current NCSL figure — 39 states plus DC, Guam, Puerto Rico, NMI and USVI (the ~37 figure is superseded)
- econ-itq-fisheries-01 — sources note replaced: Iceland's generalisation to a comprehensive ITQ system in 1991 verified (OECD 2011 chronology; Fisheries Management Act 1990) and NZ QMS 1986 confirmed; western hoki "declared rebuilt" (2011, after TACC cuts) verified in that bounded form only

## Method note

Edits were applied by assertion-guarded scripts (`drafts/apply_flags.py`,
`drafts/apply_audits.py`): every replaced claim was matched against its pre-edit text before
substitution, and FLAGS replacement notes/claims were parsed verbatim out of
`FLAGS-RESOLVED.md` rather than retyped. Items graded SURVIVES or STAYS CONTESTED were left
untouched except where a flag fix applied to them.
