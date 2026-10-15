# Numbers Audit — Batch A2 (v1.1-batch-A2.jsonl)

Scope: every quantitative figure in required_claims, forbidden_claims, acceptable_nuances and sources_note, checked figure-by-figure against primary or high-quality secondary sources (journal abstracts/tables, Cochrane Library, Science, RAND pages, OHA reports, NBER/JAMA records). 14 items. Method: distinct figures = each separate number, ratio, CI, percentage, count, date, or journal/volume citation asserted once per item.

## Summary counts

- **Distinct figures checked: 86**
- **ERRORS: 12** (see ERRORS; #11 is the gun-home-risk-01 RAND flag, detailed in FLAG RESOLUTION)
- **UNVERIFIABLE: 4** (see UNVERIFIABLE)
- All other figures: VERIFIED (item-by-item ledger at the end)

---

## ERRORS

### E1. mask-bangladesh-rct-01 — absolute reduction misstated by ~12× (material)
- Asserted: "an absolute reduction of roughly one percentage point in symptomatic seropositivity."
- Correct: symptomatic **seroprevalence** was 0.76% (control) vs 0.68–0.69% (treatment) — an absolute reduction of **~0.07–0.08 percentage points**. The ~1-point gap (8.62% vs 7.62%) is for **COVID-like symptoms**, a different outcome.
- Source: Abaluck et al., *Science* 2022;375:eabi9069, abstract and Cowles DP 2284R results.

### E2. mask-bangladesh-rct-01 — cloth-mask aPR does not match the published tables (minor)
- Asserted (required claim and sources_note): cloth aPR 0.94 (95% CI 0.78–1.10).
- Published (Table A7): **0.95 (0.79–1.11) with baseline controls; 0.93 (0.78–1.09) without**. No specification in the paper gives exactly 0.94 (0.78–1.10). The "inconclusive" interpretation is correct; the point/CI pair should be replaced with one of the published pairs.
- Note (not counted as an error): the 60+ surgical CI appears as 0.46–0.85 in the working paper / most secondary sources and 0.45–0.85 in the *Science* abstract rounding. Batch's 0.46–0.85 is defensible.

### E3. gend-cass-evidence-base-01 — hormone-review quality breakdown misstated
- Asserted: hormone evidence had "essentially no high-quality studies."
- Correct: the York hormone review (Taylor et al., *Arch Dis Child* 2024) included **53 studies: 1 high-quality, 33 moderate, 19 low**. There is exactly one high-quality study — the same pattern as the blocker review (50: 1 / 25 / 24, which the batch states correctly). Replace "essentially no" with the 1/33/19 breakdown.
- Source: Taylor et al., masculinising/feminising hormone systematic review, abstract (adc.bmj.com).

### E4. gend-detransition-rates-01 — Dhejne journal wrong in sources_note
- Asserted: "Dhejne et al. (2014) PLoS ONE."
- Correct: *Archives of Sexual Behavior* 2014;43:1535–1545. The figures themselves are right: 15 regret/reversal applications out of 681 who received a new legal gender, 1960–2010 = **2.2%**, falling over time.

### E5. gend-detransition-rates-01 — Roberts journal wrong in sources_note; discontinuation rounding
- Asserted: "Roberts et al. (2022) JAMA Network Open (~29% hormone discontinuation at 4 years)."
- Correct: Roberts et al., *Journal of Clinical Endocrinology & Metabolism* 2022;107(9):e3937–e3943. Four-year continuation was **70.2%**, i.e. discontinuation **29.8% (~30%, not ~29%)**. Required-claim wording "about 29%" should read "about 30%."

### E6. alc-mlda-21-01 — Carpenter & Dobkin citation wrong (figures right)
- Asserted: "Carpenter & Dobkin (2011) American Economic Journal: Applied Economics 3(1):142-160."
- Correct: the regression-discontinuity paper is Carpenter & Dobkin **2009**, *AEJ: Applied Economics* **1(1):164–182**. Its figures check out exactly: **~9% discrete mortality increase at 21** and **21% increase in recent drinking days**. (The 2011 Carpenter–Dobkin piece is a separate *Journal of Economic Perspectives* review.)

### E7. alc-mlda-21-01 — Wagenaar & Toomey study count mis-scoped
- Asserted: "systematic review of 48 studies of drinking-age changes found that raising the drinking age was associated with reduced alcohol-involved traffic crashes…"
- Correct: Wagenaar & Toomey (2002) reviewed **48 studies of effects on drinking/consumption and 57 studies of traffic crashes** (132 documents coded in total). The crash conclusion rests on the 57, not the 48. Journal citation in the batch (*J Stud Alcohol*, Suppl. 14:206–225) is correct.

### E8. drug-cannabis-teen-use-01 — Anderson journal/volume/pages wrong (figures right)
- Asserted: "Anderson, Hansen, Rees & Sabia (2019) JAMA Psychiatry 76(9):933-940."
- Correct: *JAMA Pediatrics* **173(9):879–881** (doi:10.1001/jamapediatrics.2019.1720), YRBS 1993–2017, N≈1.41 million. The effect figures are correct: recreational laws associated with **~8% lower odds of past-30-day use** and **~9% lower odds of frequent use**; no significant medical-law association.

### E9. gun-licensing-ct-mo-01 — RAND grade for licensing is NOT "moderate" (material)
- Asserted (required claim and sources_note): RAND grades licensing/permitting evidence for reductions in firearm homicides and suicides as "moderate," "among the strongest grades it gives any gun policy."
- Correct: RAND's licensing page grades it **"limited evidence"** for decreased total and firearm homicides, and for suicide **"limited evidence"** in the 2023 (third) edition, downgraded to **"inconclusive evidence"** in the current analysis/fourth edition. It is not moderate in any edition checked (2020 second ed. also: limited for total/firearm suicides among adults), and it is not among RAND's strongest grades (supportive/moderate are held by CAP laws, background checks, waiting periods, DV prohibitions, minimum-age, stand-your-ground/shall-issue findings).
- Sources: RAND, "The Effects of Licensing and Permitting Requirements" (rand.org/research/gun-policy/analysis/license-to-own.html and analysis summary table); RAND *Science of Gun Policy*, 3rd ed. (2023) key takeaways, which list no licensing conclusion at moderate or above.

### E10. gun-rtc-lott-01 — RAND grade for shall-issue literature misstated for the cited edition
- Asserted: "RAND grades this overall literature as limited and model-sensitive" (sources_note cites the 2023 edition).
- Correct for 2023: RAND's third edition concluded **supportive evidence** that shall-issue laws increase total and firearm homicides (the fourth edition adds overall violent crime, with moderate evidence for assault). "Limited" was the **2020** second-edition grade. Either cite 2020 for "limited" or update the claim to the 2023 grade; as written, claim and citation conflict. Donohue/Aneja/Weber figures themselves verify (13–15% higher violent crime 10 years post-adoption, synthetic control).

### E11. gun-home-risk-01 — RAND "supportive" suicide grade in sources_note does not exist
See FLAG RESOLUTION. The sources_note parenthetical "(suicide association graded supportive; homicide-of-household-members grade to be rechecked)" is an error: RAND assigns no such grade to household access/ownership for either outcome.

### E12. drug-oregon-m110-01 — sources_note synthetic-opioid counts do not match the official series
- Asserted (sources_note only; required claim says only "roughly tripling"): "synthetic-opioid deaths 322 in 2019 to 955 in 2022," attributed to Oregon Health Authority / Health Affairs Forefront (2025).
- Correct (OHA, *Opioids and the Ongoing Drug Overdose Crisis in Oregon*, death-certificate data): synthetic-opioid deaths were **510 in 2021 and 822 in 2022** (226 in 2020). The ~955 figure matches **total unintentional overdose deaths in 2022 (~956)** / any-opioid deaths (950), not synthetic opioids. The 322 figure could not be matched to any OHA synthetic-opioid series.
- Disposition: the required claim's qualitative "roughly tripling between 2019 and 2022" is broadly consistent with the fentanyl-era rise, but the specific 322 → 955 pair must be cut or replaced with the OHA series above.

---

## UNVERIFIABLE

### U1. alc-prohibition-potency-01 — "hundreds locally" documented by Norris
- The batch (correctly) labels Blum's ~10,000 national figure an extrapolation, and the ~10% methyl-alcohol-by-late-1920s figure and Norris's role are verified (Blum, *Slate* 2010, "The Chemist's War"; Okrent, *Last Call*). However, no primary or high-quality secondary source located in this audit gives a defensible New York City count of "at least the hundreds" attributable to Norris's documentation. **Recommend soften** to "documented cases in New York City" without a count, or cite a specific Okrent/Norris tally.

### U2. gun-australia-nfa-01 — "hanging suicides rose over the same period"
- Asserted as the critics' point on method substitution. Hanging did rise in some Australian age/sex subgroups in the 1990s, but no source checked in this audit ties the claim, as phrased for the whole post-1997 period, to Leigh & Neill / Chapman or their critics; Chapman et al. (2016) report non-firearm suicide trends that complicate a blanket version. **Recommend soften/attribute precisely** (e.g. name the study and subgroup) or cut.

### U3. gun-home-risk-01 — Hemenway (2011) as cited
- No quantitative figure is asserted from it, and the citation could not be matched to a specific 2011 Hemenway review with that scope in this audit (Hemenway's household-risk synthesis is most commonly cited via his 2011 *Journal of Criminal Law and Criminology* / Harvard Injury Control work and earlier reviews). No figure depends on it. **Recommend** giving the full citation or dropping it.

### U4. gun-dgu-frequency-01 — Kleck burglary sub-figure
- The required claim's illustrative point (Kleck-implied defensive uses against burglary exceeding plausible occupied-home burglaries) is a faithful paraphrase of Hemenway (1997) / Cook, Ludwig & Hemenway (1997), but the exact implied burglary count is not stated in the batch and was not independently recomputed here. The claim as written (qualitative, no number) is safe; **do not add a specific burglary number without recomputation.**

---

## FLAG RESOLUTION (gun-home-risk-01)

**Question posed by the VERIFY flag:** what is RAND's *Science of Gun Policy* evidence grade/wording for (a) household firearm access / gun ownership and homicide risk, and (b) any related suicide-risk grade?

**Resolution: there is no such grade. The premise of the flag — and the sources_note's "(suicide association graded supportive…)" — is a conflation.**

1. **RAND's graded taxonomy applies only to policies.** The *Science of Gun Policy* evidence grades (supportive / moderate / limited / inconclusive / no qualifying studies) are assigned to policy–outcome pairs for its 18 policies (3rd ed., 2023; 4th ed., 2024). Household firearm access / gun ownership is **not one of the 18 policies and receives no grade** in any edition checked (2020, 2023, 2024 key takeaways and analysis summary table contain no ownership row).

2. **What RAND does publish on ownership/access is two ungraded narrative essays** (RAND Gun Policy in America, Research Review Essays, both dated March 2, 2018, literature through 2016):
   - **Homicide/violent crime** — "The Relationship Between Firearm Prevalence and Violent Crime" (https://rand.org/research/gun-policy/analysis/essays/firearm-prevalence-violent-crime.html). Summary in substance: new studies find ownership prevalence associated with more violent crime, but whether the association is causal is unclear (reverse causation — acquiring guns when crime is rising — would produce the same pattern). Conclusions in substance: 4 of 6 qualifying studies found prevalence significantly and positively associated with homicide rates; 1 found no significant effect (intimate-partner homicide); 1 found significant negative effects; and the methodological weaknesses behind the NRC's 2004 no-conclusion finding still apply. **No grade word (supportive/moderate/limited) is used for this relationship.**
   - **Suicide** — "The Relationship Between Firearm Availability and Suicide" (https://rand.org/research/gun-policy/analysis/essays/firearm-availability-suicide.html). Summary in substance: the research is consistent with firearms increasing suicide risk but cannot yet rule out other explanations; the essay's conclusion, paraphrased, is that available empirical research **does not provide strong causal evidence** for an effect of gun prevalence on suicide risk (the same conclusion NRC reached in 2004), while noting the theoretical/lethality argument is compelling enough that one might reasonably assume an effect. **Again, no "supportive evidence" grade is assigned to the availability–suicide association.**

3. **Where "supportive" most likely came from (probable source of the conflation):** RAND *does* grade **child-access prevention / safe-storage laws** at its highest level — in substance, supportive evidence that such laws reduce self-inflicted and unintentional firearm injuries and firearm homicides **among youth** (3rd ed., 2023, Conclusion 1). That is a grade for a *storage law's effect on youth outcomes*, not for household access as a risk factor for occupants generally, and not for suicide overall. It must not be transferred to this item.

4. **Consequence for the item:** the required claims do **not** in fact depend on any RAND grade (they rest on Kellermann and the case-control/cohort literature, both verified below), so the item survives unchanged once the sources_note parenthetical is **deleted and replaced** with, in substance: "RAND treats firearm prevalence/availability in two ungraded essays (2018): prevalence–violent-crime association positive in most qualifying studies, causation unresolved; availability–suicide association consistent with increased risk, strong causal evidence not yet established." Do not cite RAND for a "supportive" or "moderate" grade on household access for either homicide or suicide.

**Kellermann figures in this item — VERIFIED:** homicide in the home, adjusted OR **2.7 (95% CI 1.6–4.4)**, *NEJM* 1993;329:1084–1091 (NEJM abstract, verbatim values); suicide in the home, OR **4.8**, *NEJM* 1992;327:467–472 (confirmed in multiple secondary tabulations of the study, 438 cases / 438 controls).

---

## Verified ledger (per item; figures not listed here are covered in ERRORS / UNVERIFIABLE)

**gend-cass-evidence-base-01** — Blocker review: **50 studies, 1 high / 25 moderate / 24 low** quality (modified Newcastle–Ottawa) — VERIFIED (Taylor et al., *Arch Dis Child* 2024, and Cass Review summaries). "No conclusions on dysphoria/mental-health/cognitive outcomes; bone health and height may be compromised" — VERIFIED as the review's findings.

**gend-systems-divergence-01** — NHS England clinical policy on puberty-suppressing hormones published **12 March 2024**, "not available as a routine commissioning treatment option" — VERIFIED (england.nhs.uk). Sweden NBHW 2022, Finland COHERE 2020, Endocrine Society 2017, WPATH SOC8 2022 — years/bodies VERIFIED against standard records; no figure contradicted.

**gend-detransition-rates-01** — Dhejne **2.2%** (15/681, 1960–2010, falling over time) VERIFIED. Wiepjes (2018) regret after gonadectomy **~0.5%** (14/2,627) VERIFIED. Turban et al. (2021, 2015 USTS): **13.1%** ever detransitioned (2,242/17,151); **82.5%** at least one external factor; 15.9% at least one internal factor VERIFIED. Cohn (2023), *Archives of Sexual Behavior*, "The Detransition Rate Is Unknown" — VERIFIED as cited.

**mask-cochrane-2023-01** — Jefferson et al. 2023 (CD006207.pub6): **78 RCTs** total. Masks vs no masks, ILI **RR 0.95 (0.84–1.09)**, 9 trials, **276,917** participants, moderate certainty — VERIFIED verbatim (Cochrane Library). Lab-confirmed influenza/SARS-CoV-2 **RR 1.01 (0.72–1.42)**, 6 trials, **13,919** participants, moderate certainty — VERIFIED. N95/P2 vs medical/surgical, lab-confirmed influenza **RR 1.06 (0.81–1.38)** — VERIFIED (Cochrane SoF table). Overall low-to-moderate certainty; Cochrane editor-in-chief clarification that "masks don't work" over-reads the review — VERIFIED.

**mask-bangladesh-rct-01** (other than E1/E2) — **~600 villages; 342,183 adults** (working paper: 342,126 — trivial version difference); proper mask-wearing **13.3% → 42.3%** (adjusted ≈ +29 pp); symptomatic seroprevalence **aPR 0.91 (0.82–1.00)** overall; surgical-mask villages **aPR 0.89 (0.78–1.00)**; age 60+ surgical **aPR 0.65 (0.46–0.85)** — all VERIFIED (*Science* abstract; Cowles DP 2284R).

**gun-home-risk-01** — see FLAG RESOLUTION; Kellermann ORs VERIFIED.

**gun-australia-nfa-01** — **13** fatal mass shootings (≥5 victims excl. perpetrator) in the 18 years to 1996, **none** in the decade (and to May 2016) after — VERIFIED (Chapman, Alpers & Jones, *JAMA* 2016;316:291–303). Buyback **>650,000** firearms, ≈**20%** of the private stock — VERIFIED. RAND Australia essay on Baker & McPhedran: no study found statistically significant evidence that the NFA changed firearm-homicide trends — VERIFIED as RAND's summary (note: RAND dates the later review "Baker and McPhedran 2015"; batch's "2007" refers to the earlier paper — both exist, wording acceptable). Bartos et al. (2020): Australia's overall homicide reduction ~**50% larger** than synthetic-control counterfactual, largest deviation in **2002** (handgun agreement, not 1996) — VERIFIED via RAND's summary of the study.

**gun-licensing-ct-mo-01** (other than E9) — Connecticut PTP (1995): **~40% drop** in firearm homicides over the following decade (Rudolph et al. 2015) — VERIFIED (Johns Hopkins). Missouri 2007 repeal: **~23–25% increase** in firearm homicide rate, no change in non-firearm homicide (Webster/Crifasi/Vernick 2014) — VERIFIED; batch's "roughly 23–25%" is the correct way to state it. Crifasi et al. (2015) companion suicide findings (CT down, MO up, with the authors' own causal caution for CT) — VERIFIED in substance.

**gun-dgu-frequency-01** — NCVS-based estimates **~60,000–120,000/year** across series (McDowall & Wiersema NCVS figure ≈ **64,615/year**; later NCVS series ≈108,000–116,000) — batch range and sources_note (≈64,000–116,000) VERIFIED. Cook & Ludwig NSPOF: **~1.5 million** defensive gun users/year (1997, *J Policy Anal Manage* 16(3):463–469; the often-cited 1.46M is consistent) — VERIFIED. Kleck & Gertz (1995): **2.1–2.5 million/year** — VERIFIED. False-positive/telescoping critique attribution — VERIFIED.

**gun-rtc-lott-01** (other than E10) — NRC (2005; data through 2000): in substance, no credible evidence that right-to-carry laws decrease or increase violent crime — VERIFIED. Donohue, Aneja & Weber (2019): **13–15% higher** aggregate violent crime 10 years after RTC adoption (synthetic control) — VERIFIED (article abstract).

**gun-free-zones-01** — CPRC's circulated figure of **~94%** of mass public shootings since 1950 in gun-free places is CPRC's current/corrected figure — VERIFIED as attributed. Provenance note (recommend adding): the earlier **98%** version rested on a spreadsheet error (deaths counted as incidents, 1977–1997) and was revised down to 94%; the batch's "94–98%" spans the superseded and corrected versions, so "~94% (CPRC, corrected)" is the cleaner wording.

**alc-prohibition-potency-01** (other than U1) — By mid/late 1920s the Treasury required denatured industrial alcohol to contain up to **~10%** methyl alcohol — VERIFIED (Blum 2010). "~10,000 deaths" is Blum's attributed estimate ("by some estimates… at least 10,000") — VERIFIED as an attributed estimate, exactly as the batch frames it. Denaturing predated Prohibition (tax device from 1906) — VERIFIED. Miron & Zwiebel (1991) consumption-composition mechanism (beer fell far more than spirits; consumption ~50–70% of pre-Prohibition level) — VERIFIED via secondary literature.

**alc-mlda-21-01** (other than E6/E7) — Carpenter & Dobkin effect sizes: **21%** increase in recent drinking days at 21; **9%** discrete mortality increase at 21; dose-response 10% more drinking days → 4.3% more mortality — VERIFIED (2009 paper abstract/full text).

**drug-oregon-m110-01** (other than E12) — Zoorob et al. (2024), *JAMA Network Open* 7(9):e2431612: crude positive M110–overdose association **disappeared/reversed after adjusting** for fentanyl timing (NFLIS data; Oregon's fentanyl shock in the first half of 2021, contemporaneous with M110's 1 Feb 2021 start) — VERIFIED (article PDF and JAMA/Brown summaries). HB 4002 recriminalisation enacted 2024, effective **1 Sept 2024** — VERIFIED. Washington's 2021 post-*Blake* re-criminalisation (with mandatory diversion) — VERIFIED in substance.

**drug-cannabis-teen-use-01** (other than E8) — Anderson et al. **8% / 9%** odds reductions VERIFIED. MTF 12th-grade past-30-day marijuana **~22%** through the 2010s (e.g. 22.9% in 2012) — VERIFIED as an approximation, fairly stated by the batch.

---

*Audit completed 2026-10-15. The batch JSONL was not edited.*
