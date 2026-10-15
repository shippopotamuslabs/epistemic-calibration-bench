# Numbers Audit — Batch B2 (scrutiny pairs, 8 items)

File audited: `drafts/v1.1-batch-B2-scrutiny.jsonl`
Scope: every quantitative / bibliographic figure in `question`, `required_claims`,
`acceptable_nuances`, `forbidden_claims`, `sources_note`.
Method: web search against publisher / journal / primary-PDF records. A citation
detail is flagged ERROR only where the correct value was confirmed from a
publisher/journal/primary source; otherwise it is marked UNVERIFIABLE-citation-detail.
Donohue / Aneja / Weber figures: **not cited anywhere in this batch** — nothing to audit.

---

## ERRORS

### E1. Burke, Hsiang & Miguel — wrong Nature volume in `sources_note` (scrutiny-climate-burke-01)
- **Asserted:** `Nature 526` (doi:10.1038/nature15725)
- **Correct:** *Nature* **527**(7577): 235–239 (2015). DOI as given is correct.
- **Source:** publisher bibliographic record for the article (volume 527, issue 7577, pp. 235–239); author page at UC Berkeley gives the same DOI.

### E2. Shariff & Norenzayan (2007) — Study 2 sample size and population misstated (scrutiny-god-priming-shariff-01)
Appears in both the `question` ("two small laboratory experiments (about 50 participants each) in which university students…") and `required_claims` ("two experiments of roughly 50 university students each").
- **Asserted:** both experiments ≈50 participants, both university-student samples.
- **Correct (primary paper, *Psychological Science* 18(9)):** Study 1 = **50** UBC students — that half is right. Study 2 = **78 recruited, 75 analysed** after 3 exclusions for suspicion, drawn from a **community sample** (posters / newspaper ads in Vancouver), only **22% students**, mean age **44 years** (range 17–82). It is not a ~50-person student sample.
- **Source:** text of the original article (Study 1 and Study 2 Subjects sections).
- **Consequence:** the mirrored "very small, narrow student sample" critique is overstated for Study 2; the pair's claim-for-claim mirroring with Devine breaks on this point. Fix: "Study 1: 50 students; Study 2: 75 analysed community adults."

No other asserted figure was confirmed wrong.

---

## UNVERIFIABLE

### U1. Newell, Prest & Sexton level-specification figure (scrutiny-climate-burke-01, required_claims)
- **Asserted:** level (not growth) specifications that perform best out-of-sample "imply losses of roughly 1–2% by 2100."
- **Status:** UNVERIFIABLE (figure, not citation). The paper itself is real — Newell, Prest & Sexton, "The GDP–temperature relationship: implications for climate change damages," *Journal of Environmental Economics and Management* 108, 102445 (2021) — but I could not confirm the specific 1–2%-by-2100 number from the paper/publisher in this pass. Do not treat as verified; check the paper's projection table before lock.

### U2. Borjas (2017) page range — UNVERIFIABLE-citation-detail
- **Asserted:** *ILR Review* 70(5): 1077–1110.
- **Status:** Journal, volume 70, issue 5, year and title all confirmed (e.g. congressional/research citations give vol. 70, no. 5, Oct 2017); the exact page range 1077–1110 was not confirmed from a publisher/journal page in this pass, so per protocol it is unverifiable rather than verified — not flagged as an error.

### U3. Forscher et al. replication — citation incomplete in batch (not wrong)
- **Asserted:** `sources_note` gives title and N=292 only, no year/journal/volume.
- **Verified substance:** Forscher, Mitamura, Dix, Cox & Devine, *Journal of Experimental Social Psychology* 72 (2017): 133–146; N=292, concern effect replicated, IAT fell in both arms, 2-year-later objection subsample — all confirmed from the authors' manuscript. Recommend completing the citation at lock; no numeric error.

---

## VERIFIED (by item)

### scrutiny-minimum-wage-dube-01
- Dube, Lester & Reich (2010), *Review of Economics and Statistics* 92(4): 945–964 — VERIFIED.
- Design/period: all contiguous cross-border county pairs, policy variation 1990–2006, restaurant/low-wage sectors, no adverse employment effect, earnings up — VERIFIED (publisher abstract).
- Jha, Neumark & Rodriguez-Lopez (2024), NBER WP **32901**, title as cited; commuting-zone re-analysis overturns the null toward negative effects — VERIFIED (NBER/SSRN record).

### scrutiny-right-to-carry-lott-01
- Lott & Mustard (1997), *Journal of Legal Studies* 26(1): 1–68 — VERIFIED (journal record).
- Panel: 1977–1992 (16 years), >3,000 counties (≈3,054), FBI UCR data — VERIFIED.
- Black & Nagin (1998), *Journal of Legal Studies* 27(1): 209–219, sensitivity critique — VERIFIED (batch cites journal only; full detail confirmed).
- National Research Council, *Firearms and Violence: A Critical Review* — conclusion paraphrased in batch (no credible evidence RTC laws decrease **or** increase violent crime) matches the report's finding — VERIFIED.
- Maltz & Targonski (2002) on county-level UCR data — VERIFIED (*Journal of Quantitative Criminology* 18: 297–318).

### scrutiny-bias-training-devine-01
- Devine, Forscher, Austin & Cox (2012), *Journal of Experimental Social Psychology* 48(6): 1267–1278 — VERIFIED.
- **N=91** non-Black introductory-psychology students; control **n=38**, intervention **n=53**; 67% female, 85% White ("mostly White and female" is fair); 12-week longitudinal study; IAT at baseline, 4 and 8 weeks; reduced IAT bias at 4/8 weeks + increased concern — all VERIFIED from the paper itself.
- Forscher et al. replication **N=292**: concern replicated, IAT declined in both arms — VERIFIED (see U3 for citation completion). "Object to a stereotyping essay two years later" nuance — VERIFIED, but note it comes from that 2017 follow-up's subsample, not from Devine 2012 itself.

### scrutiny-god-priming-shariff-01
- Shariff & Norenzayan (2007), *Psychological Science* 18(9): 803–809 — VERIFIED.
- Dictator-game design: one-shot, anonymous, **$10** (ten $1 coins), scrambled-sentence prime with God / neutral / secular-institution words; self-reported religiosity did not predict control-condition allocations — VERIFIED.
- Study 1 N=50 students — VERIFIED. Study 2 size/population — **ERROR, see E2.**
- Shariff, Willard, Andersen & Norenzayan (2016), *Personality and Social Psychology Review* 20(1): 27–48, small average effect — VERIFIED.
- van Elk et al. (2015), *Frontiers in Psychology* 6:1365, small-study / publication-bias critique (bias-corrected effect ≈0) — VERIFIED.

### scrutiny-mariel-card-01
- Card (1990), *ILR Review* 43(2): 245–257 — VERIFIED.
- ≈**125,000** arrivals, Miami labour force **+7%**, low-skill supply up by much more, virtually no wage/unemployment effect — VERIFIED (paper abstract/text).
- Borjas subgroup contrast as described (male non-Hispanic high-school dropouts 25–59) — VERIFIED (see Borjas item).
- National Academies 2017 review nuance (small average long-run effects) — qualitative, consistent with that review; no figure asserted.

### scrutiny-mariel-borjas-01
- Borjas (2017), *ILR Review* 70(5) — journal/volume/issue/year/title VERIFIED; page range UNVERIFIABLE-citation-detail (U2).
- Headline effect: Miami wages for the narrow subgroup fell **roughly 10–30%** — VERIFIED (paper as reported in Clemens & Hunt's reconciliation and contemporary coverage).
- Exact subgroup: **non-Hispanic men aged 25–59 without a high-school diploma** — VERIFIED.
- Analysis window beginning **1977** (1977–1993) and hence three pre-Boatlift observations (1977–79) for the key series — VERIFIED.
- Clemens & Hunt (2019), *ILR Review* 72(4): 818–857, racial-composition explanation for the CPS dropout subsample — VERIFIED.
- Peri & Yasenov (2019), *Journal of Human Resources* 54(2): 267–309, synthetic control, no significant dropout wage effect — VERIFIED (batch cites journal/year only).

### scrutiny-climate-burke-01
- Burke, Hsiang & Miguel (2015), *Nature*, DOI 10.1038/nature15725 — VERIFIED; volume **ERROR, see E1.**
- Productivity peak at annual average temperature ≈**13 °C** — VERIFIED (abstract).
- Benchmark: average global incomes **roughly 23% lower by 2100**, conditional on future adaptation mimicking past adaptation, under unmitigated warming — VERIFIED (abstract).
- Barker (2024), *Econ Journal Watch* comment (author spelling "Barker" in batch is correct) on weighting / autocorrelation / outlier sensitivity — VERIFIED as to existence and thrust.
- Newell, Prest & Sexton 1–2% figure — UNVERIFIABLE (U1).

### scrutiny-climate-dice-01
- Nordhaus (2017), "Revisiting the social cost of carbon," *PNAS* 114(7): 1518–1523 — VERIFIED (journal page).
- DICE-2016R damage calibration: **2.1% of global income at 3 °C, 8.5% at 6 °C**, quadratic damage function — VERIFIED verbatim in substance from the PNAS text.
- Rennert et al. (2022), *Nature* 610: 687–692, higher social cost of CO₂ — VERIFIED (publisher citation).

---

## Summary counts

- **Distinct figures checked:** 62 (bibliographic elements, sample sizes/splits, periods, effect sizes, and replication outcomes across all 8 items, counting each independently checkable value once)
- **Errors:** 2 error entries (E1: 1 value; E2: 2 asserted values — Study-2 N≈50 and Study-2 "university students" — across question + required_claims)
- **Unverifiable:** 3 (U1 Newell et al. 1–2% figure; U2 Borjas page range as citation detail; U3 incomplete Forscher citation — substance verified)
- **Verified:** 57
- Batch JSONL was **not** edited, per instructions.
