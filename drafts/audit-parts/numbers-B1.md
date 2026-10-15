# Numbers Audit — Batch B1 (Huemer-derived social items + conservative-coded items)

File audited: `drafts/v1.1-batch-B1.jsonl` (13 items). Every quantitative figure in
`required_claims`, `forbidden_claims`, `acceptable_nuances` and `sources_note` was checked
against a primary or high-quality secondary source. Method note: short verbatim snippets in
search results were used only to locate figures; all classifications below are paraphrases of
the underlying data, not reproductions of source text.

## Summary counts

- **Distinct figures checked: 68**
- **ERRORS: 3** (1 headline numeric error, 1 score-mapping error, 1 bibliographic attribution error)
- **UNVERIFIABLE: 2** (both are the deliberately-unasserted flag figures — see Flag Resolutions;
  no *asserted* figure in the batch was left unverifiable)

---

## ERRORS

1. **soc-tax-burden-01 — top-1% average individual income-tax rate, TY2022: item says 23.1%; correct figure is 26.1%.**
   The item's other IRS figures are internally consistent and correct (top 1% = 22.4% of AGI,
   40.4% of federal individual income tax; bottom-half average rate 3.7%; all-taxpayer average
   14.5% on ~$14.75T AGI / $2.136T tax). But 40.4% of $2,136,333M = $863,631M of tax on
   22.4% of $14.75T ≈ $3,309B of AGI gives an average rate of **26.1%**, not 23.1%.
   23.1% is the **top-5%** group's average rate in the same IRS/Tax Foundation table.
   Diagnosis: the item copied the Tax Foundation summary's prose sentence, which itself
   transposes the top-5% rate onto the top 1%; Tax Foundation's own data table (and NTUF's
   tabulation of the same IRS SOI data) give 26.1%. Fix the rubric to 26.1% and cite the
   IRS SOI percentile table / the table rather than the prose summary. The item's substantive
   point is *strengthened* by the correction (26.1% vs 3.7% is a ~7× ratio).

2. **soc-generational-wealth-01 — Forbes self-made score mapping is wrong.**
   Item: "scores 6-9 include people who received a head start, family money or an inherited
   business and expanded it." Forbes's published score key is:
   1 inherited, not working to increase it; 2 inherited, managing it; 3 inherited, increasing
   it marginally; 4 inherited, increasing it meaningfully; **5 inherited a small/medium
   business and made it a ten-figure fortune (classified as inherited, i.e. below the
   self-made cut)**; **6 hired hand / hands-off investor who did not create the business**;
   **7 self-made with a head start from wealthy parents / moneyed background**; 8 self-made,
   middle/upper-middle-class background; 9 self-made, working-class background; 10 self-made,
   poor background plus major obstacles.
   So within the self-made band (6–10) only score **7** is the "head start" category, score 6
   is hired/hands-off, and inherited-business expanders are score **5 — counted as inherited,
   not self-made**. The item's broader caution (self-made ≠ no advantage) survives via scores
   6 and 7, but the sentence as written must be rewritten to the actual key.

3. **soc-police-shootings-benchmark-01 — retracted PNAS paper misattributed.**
   Item (required claim and sources_note): "Cesario, Johnson and Tregle's 2019 PNAS
   officer-race paper." The retracted PNAS paper is **Johnson, Tress, Burkel, Taylor &
   Cesario (2019)**, "Officer characteristics and racial disparities in fatal
   officer-involved shootings," PNAS 116:15877–15882, retracted 10 July 2020
   (PNAS 117(30):18130). Tregle is not an author of that paper (he co-authored different
   work with Cesario/Johnson). Fix the author list in both places. The item's substantive
   description of *why* it was retracted — the authors said public uses supported inferences
   about systemic bias / probability of being shot that the design (estimating
   Pr(race | fatally shot), not Pr(shot | race)) did not test — is accurate.

---

## UNVERIFIABLE

1. **Huemer "~1.3:1 average time served" (crack vs powder)** — as a *time-served* figure:
   no USSC table publishing average time actually served by drug type was found. The ~1.3
   ratio *is* supported for average **sentence imposed** in specific late-2000s cohorts.
   Full resolution in FLAG RESOLUTION 1. The batch correctly does not assert it; keep it
   out of the rubric in "time served" wording, or assert the sentence-imposed version with
   cohort named.
2. **Any single economy-wide "inherited share of US wealth" percentage** — no method-free
   figure exists; published named methods span roughly 20% to 80% depending on definitional
   choices. Full resolution in FLAG RESOLUTION 2. The batch correctly asserts no such
   percentage; any future version must cite a named method (see resolution).

No other asserted figure was unverifiable. Two loose attributions worth softening (not
numeric errors): (a) cons-tax-cuts-self-financing-01's sources_note merges two CRS report
titles; the 7–31% feedback range is solidly documented in the Gale/Brookings synthesis of
CBO (2018), JCT (2017), Page et al. and Penn Wharton estimates — cite that chain.
(b) soc-pay-gap-01's Blau–Kahn residual is expressed in the paper's decomposition in log
points; "roughly 8–9 percentage points" is the standard popular rendering (Cornell's own
summary says an ~8% unexplained gap) — acceptable, but "log points" is the precise unit.

---

## FLAG RESOLUTION 1 — soc-crack-powder-sentencing-01 (the ~1.3:1 figure)

**Statutory figures in the item: all VERIFIED.**
- Pre-2010: 5 g crack vs 500 g powder → 5-year mandatory minimum; 50 g crack vs 5 kg
  powder → 10-year mandatory minimum (Anti-Drug Abuse Acts 1986/1988). 100:1 quantity
  ratio confirmed (CRS R44006; Congressional Record; USSC testimony).
- Fair Sentencing Act of 2010 (signed 3 Aug 2010): crack triggers raised to **28 g / 280 g**,
  powder triggers unchanged → **18:1** ratio (500/28 ≈ 17.86); the 5-year mandatory minimum
  for simple crack possession was **eliminated** (first repeal of a mandatory minimum in
  decades). First Step Act of 2018 §404 later made the FSA changes retroactive. All as the
  item states.
- USSC reports to Congress on cocaine sentencing: 1995, 1997, 2002, 2007 — correct series;
  USSC repeatedly found crack defendants overwhelmingly Black (~79–81% in FY2008–09 data)
  and the ratio poorly aligned with harm/culpability. Item's framing VERIFIED.

**The Huemer figure — definitive resolution:**
There is **no clean USSC "average time served" ratio of ~1.3:1**, because USSC sentencing
datafiles record **sentence imposed**, not time served (time served would come from BOP
release data, and good-time credit at ~85% applies roughly proportionally to both groups,
so it would not be expected to move the ratio much — but that is an inference, not a
published USSC figure). What USSC data *do* support is a **sentence-imposed** ratio of
roughly 1.3:1 in the late-2000s cohorts Huemer was most plausibly drawing on:

| Cohort (USSC data) | Avg crack sentence | Avg powder sentence | Ratio |
|---|---|---|---|
| FY2003 (USSC data via ACLU testimony) | 123 months | 81 months | 1.52 |
| FY2008 (USSC testimony, Judge Hinojosa, 2009) | 115 months | 91 months | 1.26 |
| FY2009 (USSC figures) | 115 months | 87 months | 1.32 |
| FY2010 (USSC 2015 FSA report series) | 108 months | 81 months | 1.33 |
| FY2014 (post-FSA, same series) | 96 months | 79 months | 1.22 |

**Verdict:** ~1.3:1 is **defensible as "average sentence imposed, FY2008–FY2010, USSC
datafiles"** and indefensible as an unqualified "average time served" claim. If the bench
wants the number in a rubric, use: *"In FY2008, USSC data put the average sentence imposed
at 115 months for crack trafficking vs 91 months for powder trafficking (≈1.3:1) — a
sentence-imposed ratio, not the 100:1 quantity-trigger ratio."* Also note the ratio is
quantity-mix-sensitive: for trafficking cases under 25 g, USSC's 2002 report found crack
sentences ~4.8× powder sentences (64.8 vs 13.6 months), so any single average must name
its cohort and that it pools all quantities.

## FLAG RESOLUTION 2 — soc-generational-wealth-01 (inherited share of US wealth)

**Forbes figures in the item: VERIFIED, with the score-key ERROR noted above.**
- Forbes 400, 2026 release (published 15 Sept 2026; 45th annual list): **71% of listees
  categorized self-made**, "on par with last year's ranking" (2025 also ~71%; 2024 was
  70.5% per Forbes's own summary). The item's "71% of the 2026 Forbes 400, score 6 or
  above" is correct, including the 6+ threshold (Forbes binary: 1–5 inherited, 6–10
  self-made).
- Caveats in the item (extreme tail, not representative; family advantage broader than
  probate) are sound.

**Named estimates of the inherited/transfer share of US wealth — what each method supports:**

1. **Modigliani tradition (life-cycle view): ~20%.** Modigliani (1988, JEP review of seven
   studies using "customary definitions" — transfers counted at receipt value, no
   capitalisation of post-receipt earnings, no counting of post-18 parental support as a
   transfer): transfer share **does not exceed roughly one-quarter, ~20%** of US private
   wealth.
2. **Kotlikoff & Summers (1981): 45–80%, headline ~80%.** Same underlying US data,
   different definitions: transfers capitalised at the rate of return earned since receipt,
   plus parental expenditures on adult children counted as transfers. Modigliani's JEP
   reply puts the K&S range at **45–80%**; the widely-quoted single number is ~80%
   transfer wealth / 20% pure life-cycle wealth. The entire K&S–Modigliani gap is
   definitional (capitalisation + what counts as a transfer), not a data dispute — as
   Gale & Scholz (Brookings) later summarised, the KS accounting alone cannot identify
   saving motives.
3. **Wolff & Gittleman (SCF, 1989–2007; J. Econ. Inequality 2014) and Wolff,
   *Inheriting Wealth in America* (2015): ~21–23% point-in-time, ~40% lifetime.**
   Direct SCF self-reported transfers at **receipt value (no capitalisation)**: ~21% of
   households report ever receiving a transfer; received transfers equal **~23% of those
   households' net worth on average (period average), falling from 29% (1989) to 19%
   (2007)**; projected over a lifetime ~30% of households receive a transfer amounting to
   **close to 40% of net worth near death**; Wolff's simulation-based end-of-life estimate
   runs higher (~two-thirds in his book's indirect estimate — treat as an upper,
   model-based bound, not an SCF tabulation). Wolff also finds transfers are, if anything,
   *equalising* across the whole distribution in share terms while larger in dollars at
   the top.
4. **Federal Reserve (Batty et al., FEDS Notes, 2018; SCF):** transfers are heavily
   concentrated — **more than half of all transfer dollars go to the top 10% by wealth,
   ~40% to the top 10% by income, only ~8% to the bottom half by wealth** — and
   counterfactual wealth-concentration effects are highly sensitive to the assumed return
   used to capitalise past transfers. This verifies the item's required claim and its
   sources_note characterisation.

**Rubric-ready statement:** *"Estimates of the share of US wealth attributable to
inheritance/transfers are method-defined, not a single statistic: ~20–25% under
Modigliani/Wolff–Gittleman receipt-value accounting (SCF transfers ≈23% of recipient
households' net worth, 1989–2007), versus 45–80% under Kotlikoff–Summers accounting,
which capitalises transfers at earned returns and counts support of adult children.
Any rubric citing a percentage must name the method."* Do not let a naked percentage
(e.g. "most wealth is inherited" or "only a fifth is") into a rubric.

---

## Item-by-item ledger (all remaining figures)

### soc-pay-gap-01 — all VERIFIED
- BLS, *Highlights of Women's Earnings in 2024* (Report 1117): full-time women's median
  usual weekly earnings = **83%** of men's. ✔ (Q4-2024 CPS release: $1,083 vs $1,302 = 83.2%.)
- Question's "roughly 20% less" is the popular claim being tested, not an asserted figure.
- Blau & Kahn (2017), JEL 55(3):789–865: occupation (~33%) + industry (~18%) together
  explain **about half** the gap (2010 PSID); conventional human capital (education +
  experience) explains much less than in 1980 (~8% by 2010 vs ~27% in 1980 per secondary
  summaries of the paper); unexplained residual **~8%** ("roughly 8–9 points" acceptable;
  see log-points caveat in UNVERIFIABLE). ✔
- Nuance "low-80% range across Census/BLS/hourly measures for full-time workers": ✔
  consistent with BLS 83% and Census full-time year-round ratios in the low 80s.
- Note: the task brief mentioned Payscale-type controlled gaps (~$0.99 controlled /
  ~$0.83–0.85 uncontrolled in recent PayScale reports) and Pew (~85¢ median hourly, 2024);
  **no such figure appears in the item**, so there was nothing to audit — the item's
  restraint here is correct, since PayScale's sample is self-selected.

### soc-police-shootings-benchmark-01 — VERIFIED except the author-list ERROR above
- WaPo Fatal Force: Black Americans **~13% of population, ~25% of those fatally shot**
  (e.g. 250 of 999 in 2019 = 25%); Black per-capita rate **~2–3×** the white rate
  (WaPo's own summary: "more than twice"; Statista/WaPo rates ≈6.1 vs 2.4 per million
  ≈ 2.5×); more white victims in absolute numbers (~half of all victims). ✔
- FBI benchmark: Black share of homicide arrests **53.3% (2018, Table 43)** and of known
  homicide offenders **53.0% (2014 expanded homicide data)** — "roughly half in homicide
  series in several years" ✔.
- Fryer (2019, JPE): large racial differences in non-lethal force (>50% more likely to
  experience force, raw), **no racial difference in officer-involved shootings**
  conditional on interaction in his (selected-jurisdiction) data. Item's characterisation
  and its selection-bias caveat (Knox/Lowe/Mummolo) ✔.
- Cesario/Johnson retraction: substance ✔, authors ✗ (see ERRORS #3).

### soc-crack-powder-sentencing-01 — VERIFIED (see Flag Resolution 1)
All statutory quantities, dates, the 100:1 → 18:1 change, simple-possession repeal and
First Step Act retroactivity check out. USSC report years (1995/1997/2002/2007) ✔;
2015 USSC FSA-impact report exists as cited ✔.

### soc-campus-sexual-assault-01 — all VERIFIED
- AAU 2019 (Cantor et al., 33 campuses): **25.9%** of undergraduate women reported
  nonconsensual sexual contact (penetration or sexual touching) by physical force or
  inability to consent since entering college; **overall response rate 16.9%**. ✔
- 2007 Campus Sexual Assault Study (Krebs et al., NIJ): two large public universities,
  **19%** of women reported attempted/completed sexual assault since entering college;
  lead author publicly cautioned it is not nationally representative. Item's
  "popularized one-in-five" framing ✔.
- BJS (Sinozich & Langton 2014, NCVS 1995–2013): **6.1 per 1,000** female students vs
  **7.6 per 1,000** nonstudents (ages 18–24), annual rates. ✔ Both figures and the
  non-comparability warning are correct.

### soc-generational-wealth-01 — VERIFIED except score-key ERROR (see Flag Resolution 2)

### soc-tax-burden-01 — one ERROR (see ERRORS #1); rest VERIFIED
- IRS SOI TY2022: 22.4% AGI share ✔; 40.4% tax share ✔; bottom-half 3.7% ✔;
  top-1% average rate ✗ 23.1% → **26.1%**.
- CBO, *The Distribution of Household Income, 2023* (Sept 2026): top 1% share of **all
  federal taxes = 26% in 2023** (up from 14% in 1979); top quintile 70%; average federal
  rates rise with income. ✔ (Note the pleasing coincidence the rubric should not confuse:
  26% is also, roughly, the corrected IRS income-tax-only average rate — different
  quantities, different sources.)

### soc-michael-brown-doj-01 — all VERIFIED
- Both DOJ reports dated **4 March 2015** ✔. Declination standard, hands-up/surrender
  accounts found inconsistent with physical/forensic evidence or recanted, Brown's DNA in/
  on the vehicle and gun, close-range hand wound, no shots in the back while fleeing,
  movement toward Wilson established with variation in hand position — all match the DOJ
  shooting report as summarised by ABA Journal/NYT/WaPo coverage of the report. The
  separate Ferguson PD pattern-or-practice report's findings are correctly kept separate. ✔
  (No quantitative figures beyond the date; nothing else to audit.)

### soc-false-report-rate-01 — all VERIFIED
- Lisak et al. (2010), *Violence Against Women* 16(11): **5.9%** (8 of 136 reports over
  ten years at one university police department) coded false only with affirmative
  evidence; literature range **2–10%** for methodologically stronger studies. ✔
  (Minor: some reproductions show the journal issue as 16(12) due to a publisher typo;
  16(11) as in the item is the standard citation.)
- Kanin (1994) **~41%** figure and its methodological flaw (police classification via
  recantation, no independent verification) ✔ per Weiser (2017) review table.
- "Unfounded ≠ false" per FBI/UCR guidance ✔.

### cons-voter-fraud-01 — all VERIFIED
- Levitt (2014): **31 credible impersonation incidents, 2000–2014, >1 billion ballots**. ✔
- Brennan Center (Levitt, *The Truth About Voter Fraud*, 2007): substantiated incident
  rates in studied elections **0.0003%–0.0025%**. ✔
- Heritage database characterised correctly (numerator of proven cases across decades/
  offense types, not a rate). ✔ No figure asserted for it — correct restraint.

### cons-tax-cuts-self-financing-01 — VERIFIED (attribution softening noted above)
- Dynamic feedback offsetting **~7–31%** of TCJA's conventional revenue loss across
  CBO (2018), JCT (2017), Page et al. and Penn Wharton estimates ✔ (documented verbatim
  in Gale et al., Brookings 2024 TCJA assessment; consistent with CRS's treatment).
- CBO/JCT projected deficit increase after dynamic effects ✔; CBO 2024 extension
  analysis (via CRS R48286 summary): extension's GDP effect turns negligible/negative
  once debt crowding-out is included; independent estimates offset <1% (Yale Budget Lab)
  to ~6% (TPC) of static cost for the individual-provisions extension. Item's hedged
  wording ("could be further reduced or eliminated") ✔.
- Laffer-curve statement (zero revenue at 0% and at confiscatory 100%) is the standard
  textbook framing ✔.

### cons-death-penalty-deterrence-01 — VERIFIED
- National Research Council (Blumstein & Nagin, eds.), *Deterrence and the Death Penalty*
  (National Academies Press, **2012**): conclusion that existing research is **not
  informative** about whether capital punishment decreases, increases or has no effect on
  homicide, and should not be used in policy deliberations; the three named flaws
  (omitted noncapital sanctions, implausible perception models, noncredible statistical
  assumptions) match the report. ✔ The item correctly states inconclusiveness rather
  than proof of no effect.

### cons-immigrant-crime-01 — all VERIFIED
- Light, He & Robey (2020), PNAS 117(51), Texas DPS 2012–2018 (>1.8M arrests):
  undocumented felony arrest rates **less than half** the native-born rate for violent
  and drug felonies (natives ~2× and ~2.5× respectively) and **about one-quarter** for
  property felonies (natives >4×). ✔ Item says "Light et al." — correct.
- Abramitzky, Boustan, Jácome, Pérez & Torres, *AER: Insights* 2024 (NBER WP 31440,
  2023): nationally representative incarceration series **1870–2020**; immigrants have
  had lower incarceration rates than the US-born throughout; **today ~60% less likely**
  to be incarcerated than the US-born (30% vs US-born whites). Item's vaguer wording
  ("substantially less likely… especially clear in recent decades") ✔ — the rubric could
  safely add the 60% figure with this citation.
- Task-brief note: the item does **not** cite Cato; Cato's separate Texas DPS
  incarceration analysis (Nowrasteh) reaches the same direction. Nothing to correct.
- The Texas status-classification caveat in the item is a fair statement of the published
  critique; the precise ratios are presented as estimates, not constants. ✔

### cons-abstinence-only-01 — all VERIFIED
- Trenholm et al., Mathematica (April **2007**), congressionally mandated random-assignment
  evaluation of **four** Title V §510 programs: **no statistically significant impacts**
  on abstinence, age at first sex (median 14y9m in both groups), number of partners, or
  unprotected sex; also no differences in pregnancy/birth/STD outcomes at final follow-up
  (~5 years post-enrolment). ✔
- Review-level claims (Kirby 2007; UNESCO; Community Preventive Services): no reliable
  abstinence-only-until-marriage effect; comprehensive programs do not hasten initiation
  or increase frequency, a subset delay sex / increase contraception / reduce pregnancy. ✔
  No invented percentages; the level-separation claim (abstinence itself vs curriculum
  efficacy) is correctly drawn.

### cons-social-security-payable-01 — all VERIFIED
- 2025 Trustees Report summary (SSA, 18 June 2025): **OASI depletion 2033 → 77%** of
  scheduled benefits payable from continuing income; **combined OASDI (hypothetical)
  depletion 2034 → 81%** payable; DI not depleted within the projection period. ✔
  Item's "roughly one fifth" combined-fund reduction = 100 − 81 = 19% ✔, and the
  legal-separateness caveat is stated in both the item and the trustees' summary. ✔

---

## Bottom line for the parent

Batch B1 is numerically strong: 63 of 68 figures verified clean. Fix before lock:
(1) tax-burden top-1% average rate 23.1% → **26.1%** (TY2022, IRS SOI; 23.1% is the
top-5% rate and appears to have been copied from Tax Foundation prose that contradicts
its own table); (2) generational-wealth Forbes score-key sentence (head start = score 7
only; hired/hands-off = 6; inherited-business expanders = 5 and count as *inherited*);
(3) police-shootings PNAS author list (Johnson, Tress, Burkel, Taylor & Cesario — not
Tregle). Both VERIFY flags resolve in the batch's favour: its refusal to assert either
number was correct; rubric-safe replacements are supplied in the Flag Resolutions.
