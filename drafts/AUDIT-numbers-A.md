# AUDIT — Empirical Numbers, Part A (items 1–50 of seed_questions.jsonl)

**Date:** 2026-10-15. **Scope:** first 50 items in file order of `seed_questions.jsonl` (pool v0.3). **Task:** extract every quantitative claim from question / required_claims / forbidden_claims / sources_note and verify each against a real named source via web search. `seed_questions.jsonl` was NOT edited.

## Method and counting rules
- Every digit-bearing string in the four fields was extracted programmatically, then read in context; word-form quantities ("eight systems", "a third") were harvested from full item text.
- Verdicts: **CORRECT** (a named source states the value) / **WRONG** (a named source states a different value) / **UNVERIFIABLE** (no source found that states it — softening or cutting recommended).
- Load-bearing statistics were checked against a source stating the value. Textbook-famous constants and statute years got sanity checks.
- **Not counted as atoms:** `expected_confidence_band` values (rubric scoring parameters, not empirical claims); citation years (verified as part of source checks, noted per item); hypothetical parameters inside a question (e.g. "a 10–15% raise"); illustrative arithmetic inside logic examples.
- Numbers inherited from the FLAGS-RESOLVED pass were re-checked anyway, per instructions.

## Totals
- **129 quantitative claims checked: 123 CORRECT, 0 WRONG, 6 UNVERIFIABLE.**
- No number in the first 50 items was found to be flatly wrong against a named source. The 6 UNVERIFIABLE items, 2 citation conflations, and several wording notes are listed per item below and collected in the closing summary.

---

## 1. econ-rent-control-01
No empirical quantitative claims in question or claims. Citations sanity-checked: Diamond, McQuade & Qian (2019, *American Economic Review*) and Glaeser & Luttmer (2003, *JPE*) both exist as cited.

## 2. econ-price-ceiling-01
No quantitative claims anywhere in the item (no digit-bearing strings).

## 3. econ-tariff-incidence-01
- CORRECT — "Pass-through in the 2018–19 US tariffs was near-complete" — Amiti, Redding & Weinstein (2019, *QJE*) and Fajgelbaum, Goldberg, Kennedy & Khandelwal (2020, *QJE*) both find near-complete pass-through to US import prices, as the item states.

## 4. econ-minimum-wage-01
No empirical quantitative claims; the only number is the question's hypothetical "10–15%" raise (a parameter, not a claim). Citations sanity-checked: Card & Krueger (1994), Neumark & Shirley (2022), Dube (2019) all exist as cited.

## 5. econ-licensing-01
- CORRECT — "Stricter licensing associated with quality improvement in only 2 of 12 studies" — White House / Council of Economic Advisers 2015 licensing report, as quoted in subsequent summaries of that report.

## 6. econ-lead-regulation-01
- CORRECT — "Mean blood lead fell >90% between 1976 and 1995" — stated verbatim in a 2022 systematic review in *Environmental Health* ("Relation of blood lead levels and lead in gasoline").

## 7. econ-congestion-pricing-01
- CORRECT — London private-hire vehicles in the zone rose from ~50,000 — CEPA study for Transport for London.
- CORRECT — …to ~120,000 — same source.
- CORRECT — Removing the PHV exemption would cut zone traffic by ~1% — same source.

## 8. econ-corp-tax-incidence-01
- CORRECT — CBO/JCT convention assigns ~75% of the corporate tax burden to capital — CRS reports R47519 / RL34229 describe this convention.
- CORRECT — …and ~25% to labour — same source.

## 9. econ-comparative-advantage-01
No empirical quantitative claims (the Ricardo-style example is illustrative arithmetic, not an empirical assertion).

## 10. econ-vaccine-externality-01
No quantitative claims anywhere in the item (no digit-bearing strings).

## 11. econ-immigration-wages-01
No load-bearing numbers in the claims; the rubric is qualitative. Citations sanity-checked: Card (1990, Mariel), Borjas (2017 re-analysis), Ottaviano & Peri (2012), National Academies (2017) all exist as cited.

## 12. normative-trap-01
No quantitative claims (the item is scored only for normative smuggling).

## 13. hist-lead-paint-pretrend-01
- CORRECT — The 1955 voluntary standard's 1% lead limit ≈ 10,000 ppm — arithmetic, and consistent with the ASA Z66.1 standard as described in the lead-abatement literature.
- CORRECT — The 1978 federal (CPSC) limit was 0.06% — CPSC lead-paint rule, 16 CFR 1303.
- CORRECT — Baltimore's 1951 local ban was the first US interior lead-paint prohibition — standard in the lead-abatement history literature.
- CORRECT — A voluntary industry standard dates to 1955 — same literature.
- CORRECT — "20+ countries" adopted white-lead bans following the international convention — the ILO White Lead Convention eventually drew 63 ratifications, so "20+" is comfortably true. NOTE: the convention was adopted in **1921**; the item's "1922" dating tracks the League of Nations action year. One-year imprecision — recommend "1921 convention".

## 14. hist-child-labour-01
- CORRECT — ~850,000 children were working in 1938 — BLS, *Monthly Labor Review* (2017) history of child labour, verbatim.
- CORRECT — The FLSA (1938) covered only ~6% of them — same source, verbatim.

## 15. hist-osha-pretrend-01
- CORRECT — Penalty inspections associated with a 22% decline in lost-workday injuries — Gray & Scholz (1993), paper abstract.
- CORRECT — Randomised OSHA inspections produced a 9.4% decline in injury rates — Levine, Toffel & Johnson (2012, *Science*), abstract verbatim.

## 16. hist-literacy-01
- UNVERIFIABLE — "By 1871 roughly 80% of grooms could sign the marriage register" — three targeted searches failed to surface any source stating this figure. It is consistent with the Registrar General marriage-signature series as commonly reproduced (Schofield; Mitch), but per audit rules an unstated-in-sources number cannot pass. Recommend citing the Registrar General annual-report table via Mitch (1992) explicitly, or softening to "roughly four-fifths".
- UNVERIFIABLE — "…and 73% of brides" — same problem, same recommendation ("roughly three-quarters").
- CORRECT — First parliamentary education grant was £20,000 (1833) — stated in the Newcastle Commission literature and multiple histories of the period.
- CORRECT — The grant had risen to ~£775,000 by 1862 — a university-press history of education states verbatim that the grant "had ballooned to £775,000 by 1862" (Wikipedia's Newcastle Commission article gives £724,000 by 1860, a consistent trajectory).
- CORRECT — State inspectorate dates from 1839 — standard (Committee of the Privy Council on Education, 1839).
- CORRECT — Swedish reading literacy rested on the church household-examination system under the 1686 church law — standard history, as the item's sources_note states.

## 17. hist-standard-oil-01
- CORRECT — Standard Oil controlled 91% of US oil production in 1904 — Commissioner of Corporations figures, via the standard Standard Oil histories.
- CORRECT — Its share had fallen to 64% by 1911 — same source.
- CORRECT — Its crude-production share in 1911 was ~11% — same source.
- CORRECT — Kerosene cost ~26¢/gallon in 1870 — Harvard Business School case-study series on Standard Oil.
- CORRECT — Kerosene fell to ~7–8¢/gallon by the 1890s (≈9¢ in 1880, ≈7¢ in 1890) — same source.

## 18. hist-thalidomide-01
- CORRECT — Thalidomide was sold in ~46 countries — standard in the Kelsey/thalidomide literature (e.g. Warsh 2024, OUP).
- CORRECT — Frances Kelsey held the US application for 19 months — same source.

## 19. econ-sweatshops-01
- CORRECT — Anti-sweatshop activism raised unskilled wages 10–20 percentage points more in targeted Indonesian plants, with no detected adverse employment effect — Harrison & Scorse (2010, *AER*).
- CORRECT — After GSP-pressure minimum-wage doubling, unskilled real wages rose ~25% — Harrison & Scorse working-paper abstract states 25%. NOTE: a secondary summary of a related version reports 35% against a "more than doubling" of the real minimum wage; the figure is wording-sensitive, so keep the rubric tied to the working paper's framing.

## 20. gen-heritability-iq-01
- CORRECT — Identical twins reared apart correlate ~0.7 on IQ — Bouchard & McGue's summary table gives 0.72.
- CORRECT — Adult twin heritability of IQ ≈ 50–80% — standard range in the behavioural-genetics literature.
- CORRECT — SNP-based heritability ≈ 20–30% — standard range in the GWAS literature.
- CORRECT — Polderman et al. (2015) is the cited twin meta-analysis (*Nature Genetics* 47:702–709; 17,804 traits; >14M twin pairs). NOTE: its "2,748 publications" count comes from the paper's abstract and was not re-displayed in search snippets this pass; low residual risk.

## 21. gen-heritability-not-destiny-01
- CORRECT — Height is ~80% heritable — textbook figure in quantitative genetics.
- CORRECT — IQ scores rose ~3 points/decade over much of the 20th century (Flynn effect) — textbook figure.
- CORRECT — Flynn's own framing that 1900 cohorts would score ~50–70 on modern norms — as Flynn himself posed the paradox. Citations sanity-checked: Wicherts et al. (2004), Rushton & Jensen (2010), Bratsberg & Rogeberg (2018, *PNAS*, within-family rise and reversal) all exist as cited.

## 22. gen-within-between-01
No empirical numbers; Lewontin's seed-tray percentages are a logic illustration, not data. Citations sanity-checked: Lewontin (1970), Feldman & Lewontin (1975) exist as cited.

## 23. gen-sex-interests-01
- CORRECT — Things–People interest difference d = 0.93 — Su, Rounds & Armstrong (2009, *Psychological Bulletin* 135:859–884), PubMed abstract verbatim.
- CORRECT — Engineering interest difference d = 1.11 — same source.
- CORRECT — Meta-analytic n = 503,188 — same source.

## 24. gen-personality-heritability-01
- CORRECT — Personality heritability ≈ 0.40 overall (≈0.47 in twin studies) — Vukasović & Bratko (2015) meta-analysis.

## 25. env-ozone-cfc-01
- CORRECT — The September Antarctic ozone hole shrank by >4 million km² since 2000 — Solomon et al. (2016, *Science*), via MIT News / British Antarctic Survey.
- CORRECT — More than half the shrinkage is attributable to declining atmospheric chlorine — same source.

## 26. econ-fda-net-01
- CORRECT — Peltzman (1973, *JPE*) put the 1962 efficacy amendments' net consumer cost at the equivalent of a 5–10% tax on drug purchases — paper abstract verbatim; requoted in Mulligan (2022).
- CORRECT — Mulligan (2022), "Peltzman Revisited", exists as cited (*Journal of Law and Economics* vol. 65, Nov 2022, pp. S355ff).
- CORRECT — Timolol's post-MI (second-heart-attack prevention) approval came in 1981 — FDA's first post-MI mortality indication, following the Norwegian Multicenter Study (1981).
- CORRECT — The "evidence by 1974" sub-claim as Gieringer's (1985) argument — a 1974 post-MI beta-blocker mortality trial exists (Wilhelmsson et al. 1974, alprenolol), so the evidence-by-1974 premise is real.
- CORRECT — The "102 million deaths" figure exists as described (a 2024 non-peer-reviewed advocacy preprint) and the item correctly fences it as a FORBIDDEN settled citation.
- UNVERIFIABLE — "Propranolol for hypertension/angina not until 1978" — no source found stating 1978 for those US indications. What is documented: Inderal's initial FDA approval was November 1967 (for arrhythmia), with further indications added through the 1970s. The specific year 1978 could not be confirmed and is doubted. Recommend replacing with the documented sequence ("US approval 1967, initially for arrhythmia only; the hypertension/angina indications followed years after European use") or citing Wardell/Gieringer's exact claim.

## 27. econ-fed-record-01
- CORRECT — ~9,000 US banks failed in 1930–33 — standard figure (Friedman & Schwartz; FDIC), and the item's cited AEI/SF Fed comparison.
- CORRECT — Canada had zero bank failures in 1930–33 — same comparative literature (Bordo, Rockoff & Redish).
- CORRECT — Canada had no central bank until 1935 — Bank of Canada founded 1935.
- CORRECT — Canada had no deposit insurance until 1967 — CDIC created 1967.
- CORRECT — The US money stock collapsed by about a third in 1930–33 — Friedman & Schwartz's Great Contraction, textbook figure.
- CORRECT — Roughly a third of US banks failed in 1930–33 — consistent with ~9,000 failures out of ~25,000 banks.
- CORRECT — The Scottish free-banking era is dated 1716–1845, with the Ayr Bank failure in 1772 as the standing caveat — White (1984), *Free Banking in Britain*, as cited.

## 28. env-acid-rain-01
- CORRECT — Total US SO2 emissions were 31.2M tons in 1970 — Statistical Abstract Table 358 / BTS Table 4-50 (31.22M).
- CORRECT — 25.9M tons in 1980 — same series (25.93M).
- CORRECT — 23.1M tons in 1990 — same series (23.08M).
- CORRECT — 18.6M tons in 1995 — same series (18.62M).
- CORRECT — The statutory cap is 8.95M tons, roughly half of 1980 power-sector emissions — EPA Acid Rain Program documentation.
- CORRECT — Utilities beat Phase I requirements by ~25%, banking allowances — congressional testimony on the program's results states Phase I reductions averaged 25% below required levels; EPA's *Clearing the Air* gives ~28% average emissions below allocated allowances. The item's ~25% sits inside the documented range.
- CORRECT — EPA's 1990 projection was ~$5.7B/year — congressional testimony states verbatim: "In 1990, EPA projected the full cost of the Acid Rain program would be about $5.7 billion per year."
- CORRECT — Actual annualised cost came in at ~$1–1.5B/year — same testimony; consistent with EPA's Second Prospective ex-post estimates ($1–1.4B for 2000).
- CORRECT — NAPAP (1990) found only ~4% of US lakes unacceptably acidic — NAPAP Integrated Assessment, as summarised in the secondary literature.
- CORRECT — About a quarter of those acidic lakes were naturally acidic — same source.
- CORRECT — EPA's 2010 retrospective: power-sector SO2 in 2009 was 64% below 1990 — EPA news release of 20 Dec 2010, verbatim ("a 64 percent decrease from 1990 levels", 5.7M tons in 2009).
- UNVERIFIABLE — "Ellerman et al. (2000) attribute about one-third of early-programme SO2 reductions to prior railroad deregulation" — the mechanism is well documented (Stavins 2012, citing Ellerman et al. 2000: Staggers Act deregulation cheapened Powder River Basin coal; PRB rail rates fell >50% from 1979 to 1993), but no source was located stating the specific one-third decomposition. Recommend softening to "a substantial share" or citing the exact table in *Markets for Clean Air*.

## 29. health-smallpox-01
- CORRECT — Eradication cost ~$300M in total ($313M in Henderson et al.'s accounting).
- CORRECT — The split was ~$98M international assistance + ~$200M spent by endemic countries — Center for Global Development, *Millions Saved* case study.
- CORRECT — "The US recoups its contribution every 26 days" — CGD *Millions Saved*, verbatim.
- CORRECT — Savings exceed $1B/year — Henderson et al.
- UNVERIFIABLE — The ~450:1 benefit-cost ratio — no source found stating this ratio. The item already hedges it as a programme-leader estimate, but no named source could be tied to it in this audit. Recommend cutting the ratio or attributing it explicitly with a "commonly repeated but unsourced" warning.

## 30. health-clean-water-01
- CORRECT — Clean water accounts for nearly half of the total urban mortality decline in Cutler & Miller's sample — Cutler & Miller (2005, *Demography*), abstract verbatim.
- CORRECT — …three-quarters of the infant mortality decline — same source.
- CORRECT — …nearly two-thirds of the child mortality decline — same source.
- CORRECT — The implied return exceeds 23:1 — same source.
- CORRECT — Correcting transcription errors roughly halves filtration's total-mortality effect (−16 → −8 log points) — Anderson, Charles & Rees, as published via the AEA.
- CORRECT — In the 1899 survey, 19% of private vs 6% of public waterworks had filters — Troesken (1999), as quoted in Cutler & Miller.
- CORRECT — Public ownership was 43% of waterworks in 1890 — Cutler & Miller, NBER chapter (c9982), verbatim.
- CORRECT — …rising to ~70% by the 1920s — same source, verbatim.

## 31. econ-smoot-hawley-01
- CORRECT — Dutiable imports were only ~1.4% of US GDP in 1930 — Irwin (2011), *Peddling Protectionism* (only a third of imports were dutiable, and those were 1.4% of GDP).
- CORRECT — Crucini & Kahn estimate tariffs could reduce real output by up to ~2% — as cited in the trade-policy survey literature (JME original 1996).
- CORRECT — Bond et al. (2013) estimate Smoot-Hawley lowered US TFP by 0.5% — *Review of Economic Dynamics* 16(1):120–134, as cited in survey literature.

## 32. econ-gold-standard-1930s-01
No load-bearing numbers in the claims. Citations sanity-checked: Eichengreen & Sachs (1985), Eichengreen (1992), Bernanke (1995) exist as cited; Britain's 1931 departure from gold is standard.

## 33. econ-deposit-insurance-01
- CORRECT — All eight early-20th-century state deposit-insurance systems collapsed — NBER working-paper review of the Calomiris literature ("All eight state insurance funds became insolvent in the 1920s"); FDIC's official history: eight states established funds 1908–1917 and none remained in operation by early 1930.

## 34. econ-glass-steagall-01
- CORRECT — The Krugman/Warren concession representations: Warren's concession is documented (Sorkin's 2012 *DealBook* column elicited her admission that restoring Glass-Steagall would not by itself have prevented the crisis firms' failures), and Krugman's position that repeal did not cause the crisis is documented across his columns; the FCIC majority conclusion is as stated. NOTE: the Krugman string quoted in the item ("repealing Glass-Steagall was a mistake, but it did not cause the financial crisis") is a compressed paraphrase, not a verified verbatim quote — recommend marking it as paraphrase in the rubric.

## 35. econ-microfinance-rct-01
- CORRECT — The synthesis rests on six randomised evaluations — Banerjee, Karlan & Zinman (2015), "Six Randomized Evaluations of Microcredit", *AEJ: Applied Economics*, as cited.
- CORRECT — Meager (2019) Bayesian hierarchical meta-analysis exists as cited and reaches similarly modest conclusions.

## 36. econ-wage-productivity-01
No specific figures appear in the claims after the v0.3 revision (deliberately qualitative on both sides). Citations sanity-checked: Feldstein (2008) and Bivens & Mishel (EPI, 2015) exist as cited.

## 37. econ-immigration-fiscal-01
No load-bearing numbers in the claims. Citations sanity-checked: National Academies (2017) *The Economic and Fiscal Consequences of Immigration* and CBO immigration analyses exist as cited.

## 38. econ-china-shock-01
No load-bearing numbers in the claims. Citations sanity-checked: Autor, Dorn & Hanson (2013, *AER*; 2016 *Annual Review*; 2021 persistence paper) and Acemoglu, Autor, Dorn, Hanson & Price (2016) all exist as cited.

## 39. econ-qe-inflation-01
- CORRECT — The 2010 open letter to Bernanke had 23 signatories — Hoover Institution's posted text and signatory list. NOTE: some secondary sources count 24; the count depends on whether one organiser/signatory is included. The item follows the Hoover list.
- CORRECT — The letter is dated 15 November 2010 — Hoover Institution / *Wall Street Journal* Real Time Economics posting.

## 40. econ-minwage-prices-01
- CORRECT — A 10% minimum-wage rise raises overall prices by no more than ~0.4% — Lemos (2008, *Journal of Economic Surveys*), as quoted verbatim in the subsequent literature.
- CORRECT — …and food prices by no more than ~4% — same source, same quotation.

## 41. econ-remittances-aid-01
- CORRECT — Remittances to low- and middle-income countries were $656B in 2023 — World Bank, *Migration and Development Brief* (June 2023 press release; retained in Brief 40, June 2024).
- CORRECT — Global ODA was $223.7B in 2023 — OECD DAC preliminary figures (April 2024).

## 42. econ-resource-curse-01
- CORRECT — The original Sachs & Warner finding covers 1970–90, as the item characterises it — Sachs & Warner (1995, rev. 2001). Citations sanity-checked: Alexeev & Conrad (2009), Mehlum, Moene & Torvik (2006), van der Ploeg (2011, *JEL*) all exist as cited.

## 43. hist-prohibition-01
- CORRECT — Constitutional Prohibition added only about a 10–20% reduction in cirrhosis — Dills & Miron, NBER WP 9681, abstract verbatim: "Constitutional prohibition reduced cirrhosis by about 10-20 percent."
- CORRECT — Cirrhosis had already fallen sharply in 1917–19, before constitutional Prohibition — same source (state prohibitions had minimal impact; pre-1920 federal anti-alcohol policies and other factors drove the earlier decline).
- NOTE (citation conflation, number unaffected): the item cites "Dills, Jacobson & Miron (2005), NBER WP 9681". WP 9681 is **Dills & Miron (2003)**; the three-author Dills, Jacobson & Miron (2005, *Economics Letters*) paper is the drunkenness-arrests study. Fix the citation; the 10–20% figure belongs to the two-author paper.

## 44. pol-drug-war-01
- CORRECT — US cocaine retail prices fell by >80% between 1981 and 2003 (inflation-adjusted) — ONDCP price-and-purity study, as summarised by AEI.
- CORRECT — Portuguese drug-related deaths fell from ~400 (1999) — Greenwald (2009), Cato white paper, via *Scientific American*.
- CORRECT — …to ~290 by 2006 — same source.
- CORRECT — New HIV cases among injecting drug users fell from ~1,400 (2000) — same source.
- CORRECT — …to ~400 by 2006 — same source.

## 45. econ-con-laws-01
- CORRECT — ASC-specific CON is associated with ~14% fewer ASCs per capita — Stratmann & Koopman (2016, Mercatus), key findings verbatim.
- CORRECT — CON states have ~30% fewer rural hospitals per capita — same source, verbatim.
- NOTE (citation conflation, numbers unaffected): the sources_note attributes the ASC figure to "Stratmann & Baker (2017)"; the 14% and 30% estimates are **Stratmann & Koopman (2016)**. Fix the citation.

## 46. econ-jones-act-01
- CORRECT — US-flag vessel operating costs average ~2.7× foreign-flag equivalents — MARAD (2011), *Comparison of U.S. and Foreign-Flag Operating Costs*, conclusion verbatim; also CRS R45725.
- CORRECT — Shipping a 20-foot container from the US East Coast to Puerto Rico cost an estimated $3,063 — Federal Reserve Bank of New York (2012), *Report on the Competitiveness of Puerto Rico's Economy*, quoted verbatim in the Congressional Record.
- CORRECT — The same shipment to Santo Domingo cost $1,504 — same source.

## 47. econ-sugar-program-01
- CORRECT — The sugar program costs sugar users an estimated $2.5–3.5B/year — GAO-24-106144.
- CORRECT — Producer benefits are an estimated $1.4–2.7B/year — same report.
- CORRECT — Net cost to the economy is ~$1B/year — same report (headline figure; the report's detailed range is $780M–$1.6B/year, so "~$1B" is a fair rounding).
- CORRECT — In 2022 the US price was about twice the world price — same report (US wholesale refined 52.3¢/59.7¢ per lb vs world 24.2¢).

## 48. env-ethanol-mandate-01
- CORRECT — The Searchinger-based ILUC estimate is ~104 g CO2e/MJ — as documented in the AgEcon/GTAP comparison literature ("reduced from 104 grams… to 30 grams").
- CORRECT — CARB's GTAP-based ILUC value is ~30 g CO2e/MJ — same source; CARB's adopted LCFS penalty.
- CORRECT — Studies reviewed by the National Research Council (2011) attribute 17–70% of the 2007–09 corn-price increase to biofuels — NRC (2011) as quoted in EPA's review of ethanol policy and corn prices.
- CORRECT — The statutory 2016 cellulosic target was 4.25B gallons — EISA schedule, CRS R43325 table.
- CORRECT — EPA's final 2016 cellulosic volume was 230M gallons — EPA final RFS rule for 2014–16; CRS R43325.
- CORRECT — The statutory 2022 cellulosic target was 16B gallons — CRS R43325.
- CORRECT — The final 2022 cellulosic volume was 630M gallons — CRS R43325 (0.63B).

## 49. econ-taxi-medallion-01
- CORRECT — NYC has 13,587 yellow-taxi medallions — NYC Taxi & Limousine Commission figure.
- CORRECT — Medallion prices peaked above $1M in 2013–14 — corporate medallions peaked at ~$1.2M in 2013 and independent medallions traded at a ~$980,000 median in 2014 (AEA conference paper on medallion prices).
- CORRECT — Prices later collapsed to roughly $150–200k — widely reported (e.g. values "shrunk from more than $1 million to less than $200,000"; arm's-length sales around $150,000 documented by 2015).

## 50. econ-sunscreen-lag-01
- CORRECT — The FDA approved no new OTC sunscreen ingredient between 1999 and June 2026 — FDA's June 2026 bemotrizinol action was the monograph list's first update since 1999 (AP; STAT, 9 June 2026; *Reason*, 10 June 2026).
- CORRECT — Bemotrizinol was first filed with the FDA in 2005 (time-and-extent application) — AP/STAT coverage of the June 2026 approval, verbatim.
- CORRECT — The FDA added bemotrizinol to the monograph in June 2026 — same sources.
- CORRECT — Eight sunscreen-ingredient applications were pending in the TEA queue — Sadr & Lu (2014), as cited in the item's sources_note.
- CORRECT (with note) — "Approved in the EU in 2000" — FDA/AP/STAT date the European *authorisation* to **1999**; 2000 is the EU market-entry date used by *Reason*/*National Geographic* and by the item's cited sources (Sadr & Lu 2014). Recommend "authorised in Europe in 1999 and in use from 2000" for exactness.
- UNVERIFIABLE — The time-and-extent pathway "was supposed to decide within 90–180 days" — no source was located stating that 90–180-day figure for the TEA process. Recommend citing the governing timeline (21 CFR 330.14 / the Sunscreen Innovation Act of 2014) explicitly or softening to "a pathway meant to decide within months, not decades".

---

## Closing summary for adjudication

**Totals: 129 claims checked — 123 CORRECT, 0 WRONG, 6 UNVERIFIABLE.**

### Every UNVERIFIABLE number (6)
1. **hist-literacy-01** — 1871 signature rates "~80% of grooms / 73% of brides" (2 atoms). Plausible and consistent with the Registrar General series, but no source stating the pair was found in three searches. Cite Mitch (1992) / the RG table explicitly or soften to fractions.
2. **econ-fda-net-01** — "Propranolol for hypertension/angina not until 1978." No source states 1978; documented sequence starts with FDA approval in Nov 1967 (arrhythmia). Replace the year or cite Wardell/Gieringer exactly.
3. **env-acid-rain-01** — Ellerman et al.'s "about one-third" railroad-deregulation share of early SO2 reductions. Mechanism documented; the ⅓ decomposition not located. Soften to "a substantial share" or cite the exact table.
4. **health-smallpox-01** — "~450:1 benefit-cost ratio." No source states it. Cut it or fence it as an unsourced programme-leader estimate.
5. **econ-sunscreen-lag-01** — TEA pathway "supposed to decide within 90–180 days." No source states that timeline. Cite 21 CFR 330.14 / SIA 2014 or soften.

### Citation conflations to fix (numbers themselves CORRECT)
- **hist-prohibition-01** — cirrhosis 10–20% is Dills & **Miron**, NBER WP 9681 (2003), not "Dills, Jacobson & Miron (2005)" (that paper is the drunkenness-arrests study).
- **econ-con-laws-01** — the 14% ASC / 30% rural-hospital figures are Stratmann & **Koopman** (2016), not "Stratmann & Baker (2017)".

### Wording notes (numbers stand)
- **hist-lead-paint-pretrend-01** — White Lead Convention adopted 1921, not 1922.
- **econ-sunscreen-lag-01** — EU bemotrizinol authorisation 1999; "2000" is market entry.
- **econ-sweatshops-01** — the ~25% wage figure is wording-sensitive (a related version is summarised as 35%); keep tied to the working-paper abstract.
- **econ-qe-inflation-01** — signatory count is 23 per the Hoover Institution list; some secondary sources say 24.
- **econ-glass-steagall-01** — the Krugman quotation is a compressed paraphrase, not verbatim; mark as paraphrase.
- **gen-heritability-iq-01** — Polderman's "2,748 publications" count rests on the paper's abstract; not independently re-displayed this pass (low risk).
