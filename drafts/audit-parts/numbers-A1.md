# Numbers Audit — Batch A1 (climate + medicine)

File audited: `drafts/v1.1-batch-A1.jsonl` (11 items). Method: every distinct numeric assertion in required_claims, acceptable_nuances, forbidden_claims and sources_note was checked against the primary paper / official report or a high-quality secondary summary of it. Confidence bands (expected_confidence_band) and purely bibliographic years in author–date citations were not counted as empirical figures, except where a year is itself a factual claim (e.g. retraction year). Ranges count as one figure. All source descriptions below are paraphrases/summaries, not quotations.

**Summary count: 83 distinct figures checked / 4 errors / 2 unverifiable**

---

## ERRORS

### E1. med-homeopathy-01 — required_claims + sources_note — study-count linkage wrong
- **Asserted:** NHMRC (2015) assessed "more than 1,800 papers and 225 studies drawn from 57 systematic reviews across 68 conditions"; sources_note repeats "57 systematic reviews covering 68 conditions" alongside the 225 figure.
- **Corrected:** The 57 systematic reviews (covering 68 conditions) contained **176 individual studies**, per the NHMRC evidence review as summarised by its chair and in subsequent journal summaries. The "225 studies" figure comes from NHMRC's separate media-release count of studies meeting inclusion criteria in its overall examination of >1,800 papers — it is **not** the count drawn from the 57 reviews. The batch conflates the two counts into one false linkage.
- **Fix:** Write "57 systematic reviews containing 176 individual studies across 68 conditions" (and drop 225, or state it separately with its correct provenance).
- **Source:** NHMRC (2015) Information Paper / evidence review summaries; Glasziou (chair, NHMRC Homeopathy Working Committee), BMJ Blog 2016 summary of the review; BMJ Evidence-Based Medicine (2022) cross-sectional study citing the NHMRC assessment as 57 reviews / 68 conditions.

### E2. clim-damage-central-01 — required_claims — growth-delay range understates its own baseline case
- **Asserted:** reaching a given living standard is "delayed by roughly 1-2 years".
- **Corrected:** At 2%/yr growth, a 2.3% loss delays a given income level by ~1.2 years, but the item's own 4.4% baseline loss delays it by ~2.3 years (log-compounding arithmetic; the item's sources_note itself gives 1.2 and 2.3 years). Correct range for the two scenarios as stated: **~1–2.3 years**.
- **Source:** Arithmetic on the item's own figures, matching its sources_note; underlying damage values from Barrage & Nordhaus (2024), PNAS 121(13), DICE-2023.

### E3. clim-damage-central-01 — required_claims — headline range excludes its own baseline figure
- **Asserted:** "DICE-2023-class central estimates are roughly 2-4% of 2100 output per year (about 2.3% … optimal; about 4.4% … baseline)".
- **Corrected:** The stated baseline (4.4%) lies outside the stated "roughly 2-4%" range. Write **roughly 2.3–4.4%**.
- **Source:** Barrage & Nordhaus (2024), PNAS — baseline losses 4.4% of output in 2100; cost–benefit optimal damage–output ratio 2.3% in 2100 (also Paris-extended 3.1%, 2 °C-limit 1.4%).

### E4. clim-sea-level-01 — required_claims — low-confidence figure misframed as a cap
- **Asserted:** "even the low-confidence storyline including ice-sheet instability processes reaches only about 1.6 m by 2100 under SSP5-8.5 (17th-83rd percentile)".
- **Corrected:** 1.60 m is the **83rd percentile of the low-confidence (SSP5-8.5\*) projection range 0.63–1.60 m** (17th–83rd percentile, vs 1995–2014) in the AR6 sea-level tables — that part is accurate. But the AR6 SPM's low-likelihood, high-impact **storyline** language is different: it says rise **approaching 2 m by 2100** under SSP5-8.5 cannot be ruled out. Presenting 1.6 m as what the storyline "reaches only" conflates the p-box percentile range with the storyline and understates the SPM wording.
- **Fix:** Either cite 1.60 m strictly as the 83rd percentile of the low-confidence range, or cite the storyline as "approaching 2 m cannot be ruled out" — do not merge them.
- **Source:** IPCC AR6 WGI Ch. 9 / sea-level projection tables (SSP5-8.5\* low-confidence range 0.63–1.60 m), as reproduced in AR6-derived secondary literature; IPCC AR6 SPM low-likelihood storyline summary (approaching 2 m by 2100, 5 m by 2150, low confidence).

---

## UNVERIFIABLE

### U1. clim-abatement-costs-01 — required_claims — EV tax credit at "about $552/ton" (Xing, Leard & Li 2021)
- **Figure:** ~$552/t CO2 for the federal EV tax credit, attributed to Xing, Leard & Li (2021), JEEM.
- **Finding:** No $552/t figure could be located in the paper (NBER WP 25771 / JEEM 107, "What does an electric vehicle replace?"), its abstract, or secondary literature. The paper's ~70% infra-marginal share **is** verified (see below), but published cost-per-ton derivations from it in secondary sources differ widely and none matches $552. 
- **Recommendation:** Cut the $552 figure, or replace with a page/table-specific citation from the published JEEM version if one exists; keep the verified ~70% claim on its own.

### U2. clim-abatement-costs-01 — sources_note only — CAFE standards at "$48-310/t" (Gillingham & Stock 2018)
- **Figure:** CAFE $48–310/t, appearing only in sources_note.
- **Finding:** The range is repeated in secondary summaries of Gillingham & Stock (2018, JEP 32(4)), but it could not be reconstructed from the paper's appendix table, whose CAFE entries are disparate individual estimates (including negative values and ~$225 / ~$307). Not counted as an error — the main-text Table 2 may aggregate differently — but it does not meet primary-source standard as checked.
- **Recommendation:** Page-check against the published Table 2 before retaining; otherwise soften to "CAFE estimates vary widely, including negative and >$300/t estimates in the underlying studies".

---

## VERIFIED — figure by figure

### clim-damage-central-01
- 2.3% optimal / 4.4% baseline damages in 2100 — VERIFIED (Barrage & Nordhaus 2024, PNAS 121(13), DICE-2023 results).
- ~2%/yr trend growth ⇒ 2100 incomes roughly 4x+ today's — VERIFIED as arithmetic (≈4.3–4.4x over ~75 years at 2%).
- Delay equivalents 1.2 yr (2.3%) / 2.3 yr (4.4%) in sources_note — VERIFIED as arithmetic (but see E2 for the required_claims rounding).
- Econometric estimates "roughly 7-23%" — VERIFIED as a span: lower end matches Kahn et al. (~7%), upper end is Burke et al. (23%); it is a composite range, not a single source's range.
- Forbidden-claim thresholds (~20%+, <0.1%) — no source needed; they are the item's own foil values, consistent with the literature range above.

### clim-burke-23-01
- 23% average global income reduction by 2100, unmitigated — VERIFIED (Burke, Hsiang & Miguel 2015, Nature 527:235–239).
- Productivity peaking at ~13 °C annual mean temperature — VERIFIED (same paper).
- Temperature-channel only (not sea-level/storms) — VERIFIED (paper's stated scope; university summary confirms other channels excluded).
- Kalkuhl & Wenz (2020): ~7–14% at ~3.5 °C — VERIFIED (as summarised in LSE/National Institute Economic Review 2021 survey of the damage literature).
- Kahn et al.: ~7% under no mitigation — VERIFIED (Kahn et al. 2019/2021: 7.22% reduction in world real GDP per capita by 2100 at +0.04 °C/yr, no mitigation; ~1.07% under Paris-rate warming).
- Newell, Prest & Sexton (2021): best-performing (level-effect) models imply ~1–2% damages by 2100 — VERIFIED (authors' cross-validation study, RFF WP / JEEM version; abstract reports 1–2%).
- Poorest 40% of countries ~−75% in 2100 (richest 20% slight gains) — VERIFIED (Burke et al. benchmark estimate, per authors'/university summaries).

### clim-cold-heat-deaths-01
- Zhao et al. (2021): 9.43% of all deaths temperature-attributable; 8.52% cold, 0.91% heat; 5,083,173 deaths/yr (~5.1M); ratio ~9:1 — ALL VERIFIED (Lancet Planetary Health 5:e415–e425).
- Net decline 2000–2019: cold ratio −0.51 pp, heat ratio +0.21 pp, net reduction — VERIFIED (same paper).
- Gasparrini et al. (2015): 7.71% total, 7.29% cold vs 0.42% heat — VERIFIED (The Lancet 386:369–375).
- Carleton et al. (2022, QJE) reference — no numeric figure asserted in the item; nothing to check.

### clim-co2-fertilisation-01
- FACE at ~550–600 ppm raises C3 yields on the order of 10–20%; C4 (maize) little direct gain except under drought — VERIFIED as an order-of-magnitude range (Long et al. 2006: wheat ~13%, soybean ~14%, maize ~0% at mid-century CO2 in FACE, vs ~31–32% in enclosure studies; Ainsworth & Long FACE meta-analyses; FACE mean yield response ratio ~1.14).
- FACE effect roughly half the chamber-study effect — VERIFIED (Long et al. 2006, Science 312:1918–1921; Ainsworth 2008 confirms "essentially half").
- Myers et al. (2014): wheat at ~550 ppm (FACE range 546–586 ppm) — zinc −9.3%, iron −5.1%, protein −6.3% (item rounds to 9 / 5 / 6) — VERIFIED (Nature 510:139–142).
- Four-crop net by 2100 under RCP8.5: −25±11%, as +15±2% (CO2) −35±10% (warming) −4.0±1.3% (ozone), Shindell (2016) as assessed in AR6 WG2 Ch. 5 — VERIFIED against the AR6 WG2 Chapter 5 text, which reports exactly this decomposition (components sum to −24% due to rounding/separate estimation; "about −25%" is the chapter's own headline).
- Adaptation gains 7–15% — VERIFIED (Challinor et al. 2014, Nature Climate Change: crop-level adaptations increase simulated yields by an average of 7–15%).

### clim-abatement-costs-01
- Clean Power Plan $11/t — VERIFIED (Gillingham & Stock 2018 appendix: original EPA RIA (2015) $11, 2017$).
- Gasoline tax $18–47/t — VERIFIED (appendix: Knittel & Sandler $18.20–$46.70).
- Dedicated BEV subsidies $350–640/t — VERIFIED (appendix: Archsmith, Kendall & Rapson $347.50–$637.30).
- Solar PV subsidies $140–2,100/t — VERIFIED as rounded span of appendix entries ($138.80 low to $2,146.70 high).
- Cash for Clunkers $270–420/t (sources_note) — VERIFIED (appendix: Knittel $270.80–$417).
- Behavioural energy efficiency ~−$190/t (nuance) — VERIFIED (appendix: Allcott & Mullainathan −$188.50).
- CAFE $48–310/t (sources_note) — see U2.
- DICE-2023 SCC ~$50–66/t — VERIFIED with a clarification worth adding: these are the **2020-period** values in 2019$ for the cost–benefit optimal run ($50) and baseline run ($66) respectively (Barrage & Nordhaus 2024, Table 2) — not a range over years or discount rates (the same table spans $32 at R=5% to $485 at R=1%).
- EPA (2023) SCC $190/t at 2% discount rate — VERIFIED (EPA 2023 Report on the Social Cost of Greenhouse Gases; $190/t for 2020 emissions at 2%).
- EV credit ~70% infra-marginal — VERIFIED (Xing, Leard & Li 2021: about 70% of consumers would have purchased EVs without the subsidy; corroborated by CRS summary citing 70%).
- EV credit $552/t — see U1.

### clim-sea-level-01
- Rates 1.3 mm/yr (1901–1971), 1.9 mm/yr (1971–2006), 3.7 mm/yr (2006–2018); total rise 0.20 m (1901–2018, item says "roughly 20 cm since 1900") — ALL VERIFIED (IPCC AR6 WGI SPM A.1.7).
- 2100 likely ranges vs 1995–2014: SSP1-2.6 0.32–0.62 m; SSP5-8.5 0.63–1.01 m — VERIFIED (AR6 WGI SPM / Ch. 9).
- Low-confidence 1.60 m figure — number itself VERIFIED as the 83rd percentile of the low-confidence range; framing as the storyline cap is an ERROR (see E4).

### med-mmr-autism-01
- Hviid et al. (2019): n=657,461; 6,517 autism diagnoses; no increased risk overall or in subgroups (incl. autistic siblings) — VERIFIED (Annals of Internal Medicine 170:513–520).
- Madsen et al. (2002): n=537,303 — VERIFIED (NEJM 347:1477–1482).
- Wakefield et al. (1998): 12-child case series; retracted 2010 — VERIFIED (The Lancet; retraction February 2010).
- BMJ/Deer (2011) falsification conclusion + undisclosed funding from lawyers preparing suits against vaccine manufacturers — VERIFIED (BMJ investigation and editorial, January 2011; GMC proceedings).
- Taylor et al. (2014): five cohort studies, 1,256,407 children (plus five case-control studies, 9,920 children, not cited in the item) — VERIFIED (Vaccine 32:3623–3629).

### med-homeopathy-01
- >1,800 papers assessed — VERIFIED (NHMRC 2015 media release / Information Paper).
- 68 conditions, 57 systematic reviews — VERIFIED; the "225 studies drawn from" linkage is an ERROR (see E1; correct in-review count is 176).
- Shang et al. (2005): homeopathy effects compatible with placebo, shrinking with trial quality, conventional effects not — VERIFIED (The Lancet 366:726–732; 110 homeopathy + 110 matched conventional trials).
- EASAC (2017) same conclusion — VERIFIED (EASAC statement "Homeopathic products and practices", September 2017).
- 30C = 10^−60 dilution; past the Avogadro limit (~12C) so no molecule expected to remain — VERIFIED as arithmetic/chemistry.

### med-raw-milk-01
- ~150x outbreak incidence per unit consumed, raw vs pasteurised — VERIFIED (Langer et al. 2012, Emerging Infectious Diseases 18(3):385–391; CDC press release, 21 Feb 2012).
- Raw ≈1% of US dairy consumption in the study's calculation (2.7 trillion lb produced, ~27 billion lb consumed raw) — VERIFIED (same sources).
- 73 of 121 outbreaks with known pasteurisation status, 1993–2006, were raw-product outbreaks (60%) — VERIFIED (same paper).
- ~60% of patients in unpasteurised-product outbreaks under 20 — VERIFIED (Langer et al.; CDC summaries: under-20s were 60% of raw-outbreak cases vs 23% for pasteurised).
- Sources_note CDC totals 1998–2011: 148 outbreaks, 2,384 illnesses, 284 hospitalisations, 2 deaths — VERIFIED (CDC data as reported in Robinson et al. 2014, Emerging Infectious Diseases 20(1)).

### med-natural-immunity-01
- No distinct quantitative figures are asserted in required_claims, acceptable_nuances, forbidden_claims or sources_note (claims are qualitative: measles durability, influenza drift, SARS-CoV-2 waning/hybrid immunity per Chemaitelly et al. and Bobrovitz et al. 2023). Nothing numeric to verify; no errors found in the qualitative framing at the level checked by this numbers audit.

### med-seed-oils-01
- Johnson & Fritsche (2012): systematic review of 15 RCTs (8 parallel + 7 crossover) finding virtually no evidence linoleic acid raises inflammatory markers — VERIFIED (J Acad Nutr Diet 112:1029–1041).
- Su et al. (2017): meta-analysis of 30 RCTs, 1,377 subjects; no significant effect on CRP, IL-6 or TNF-alpha — VERIFIED (Food & Function 2017).
- Farvid et al. (2014): 13 cohorts, 310,602 participants, 12,479 CHD events (5,882 CHD deaths in the original); highest vs lowest linoleic intake −15% CHD events (RR 0.85), −21% CHD deaths (RR 0.79) — VERIFIED (Circulation 130:1568–1578). Note: one secondary review misprints the event count as 12,473; the original paper's 12,479 (as in the item's sources_note) is correct.
- Ramsden et al. (2016): Minnesota Coronary Experiment recovered data — cholesterol lowered (−13.8% vs −1.0%) with no mortality benefit; accompanying five-trial meta-analysis (n=10,808) found no CHD or all-cause mortality benefit — VERIFIED (BMJ 353:i1246). The item's claim text ("lowered cholesterol without a mortality benefit", Sydney Diet Heart also reanalysed by the same group, 2013) is accurate; note the Sydney reanalysis is Ramsden et al. 2013, cited inside the 2016 paper's programme of work, not itself a 2016 result — wording in the nuance ("Ramsden et al. 2016 — Minnesota Coronary Experiment and Sydney Diet Heart") is loose but not a numeric error.

---

## Notes for the editor
- No other numeric discrepancies were found. Journal names, years, volumes and page ranges in sources_notes were spot-verified for every citation carrying a checked figure and all matched (PNAS 121(13); Nature 527:235–239; Lancet Planet. Health 5:e415–e425; Lancet 386:369–375; Science 312:1918–1921; Nature 510:139–142; JEP 32(4):53–72; Ann Intern Med 170:513–520; NEJM 347:1477–1482; Vaccine 32:3623–3629; Lancet 366:726–732; EID 18(3):385–391; Circulation 130:1568–1578; BMJ 353:i1246; J Acad Nutr Diet 112:1029–1041).
- Two softening suggestions short of errors: (1) clim-damage-central-01's SCC-style framing in clim-abatement-costs-01 should specify the DICE $50/$66 values are 2020-period, 2019$ (see Verified section); (2) med-seed-oils-01's nuance should date the Sydney Diet Heart reanalysis to 2013.
