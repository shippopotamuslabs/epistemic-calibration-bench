# AUDIT — Numbers, Part B (items 51–100)

Empirical numbers audit of the last 50 items in `seed_questions.jsonl` (file order).
Every quantitative claim — numbers, percentages, effect sizes, sample sizes, dates,
counts, and journal/year/volume citations — in each item's question, required and
forbidden claims, acceptable nuances, and sources_note was extracted and checked
against a named source via web search. Numbers inherited from the FLAGS-RESOLVED
pass were re-verified independently.

**Totals: 391 numbers checked — 353 CORRECT / 21 WRONG bullets (20 distinct errors) / 17 UNVERIFIABLE.**

Per-cluster: §1 items 51–60: 83 checked (75/4/4) · §2 items 61–70: 88 (73/5/10) ·
§3 items 71–80: 89 (82/6/1) · §4 items 81–90: 54 (49/4/1) · §5 items 91–100: 77 (74/2/1).

`seed_questions.jsonl` was NOT edited by this audit.

---


======================================================================

# AUDIT — Numbers, Section B, Cluster 1 of 5

Compiled 2026-10-15. Scope: ONLY these 10 items from `seed_questions.jsonl`:
econ-licensing-mobility-01, econ-zoning-supply-01, econ-rent-control-sf-01,
econ-dairy-supply-mgmt-01, hist-antitrust-telecom-01, env-cafe-standards-01,
pol-speed-limit-01, env-appliance-standards-01, hist-auto-safety-01,
hist-reforestation-01.

Method: every number / percentage / effect size / date-bound quantity / count in
question, required_claims, acceptable_nuances, forbidden_claims and sources_note
was extracted and checked against a named source via web search (pure
confidence-band fields and item ids skipped). Numbers also appearing in
FLAGS-RESOLVED.md were re-checked independently, not inherited.

**Tally: 83 numbers checked — 75 CORRECT · 4 WRONG · 4 UNVERIFIABLE.**

---

## econ-licensing-mobility-01

- Wage premium "on the order of 10–15% after controls (Kleiner & Krueger 2013)" — **CORRECT**. Kleiner & Krueger (2013, J. Labor Econ.) is the source of the 10–15% cross-study range with standard controls; BLS research (Gittleman, Klee & Kleiner) likewise describes the consensus range Kleiner & Krueger cite as 10–15%.
- sources_note pairing "premium ~15% raw, ~10% with controls" — **WRONG**. No source states that raw/controlled split. Kleiner & Krueger's own headline multivariate estimate is ~15% (≈14% in the published abstract — i.e. ~15% IS the with-controls figure, not the raw one); 10–15% is the range across studies with standard controls. Recommend rewriting the note as "premium ~14–15% in Kleiner & Krueger's multivariate estimates; 10–15% range across studies with standard controls".
- Licensing "from roughly 5% of the US workforce in the 1950s" — **CORRECT**. Kleiner & Krueger / Johnson & Kleiner (2020): ~5% in 1950 (less than 5% in the early 1950s, state-level data).
- "…to about a quarter or more today" — **CORRECT**. Johnson & Kleiner (2020, intro): about 25% of the workforce requires a licence.
- sources_note "licensed share ~29% in their survey" — **CORRECT**. Kleiner & Krueger's Gallup survey: 29% of the workforce fully licensed. (Note: 25% and 29% are different measures — BLS-based coverage vs K&K's own survey — both sourced; the item does not conflate them.)
- Johnson & Kleiner: between-state migration "36% lower" for state-specific-exam occupations — **CORRECT**. Johnson & Kleiner, NBER WP 24107 / AEJ:EP (2020), abstract states exactly this.
- sources_note "+5.5% point estimate" for national/quasi-national exam occupations — **CORRECT**. Johnson & Kleiner Table 4: +5.52 (a null, as the note says).
- sources_note "all licensed occupations combined −22.5%" — **CORRECT**. Johnson & Kleiner Table 4 / text: −22.52%.
- sources_note "state-specific vs quasi-national net of within-state far moves −16%" — **CORRECT**. Johnson & Kleiner Table 4: −16.33%.
- Citation "Johnson & Kleiner (2020), American Economic Journal: Economic Policy 12(3):347–373 (NBER WP 24107)", 22 licensed occupations — **CORRECT**. WP 24107 confirmed (RePEc/NBER); published venue AEJ:EP; the paper analyses 22 licensed occupations.
- sources_note "BLS Monthly Labor Review (2022) review for the mixed compact evidence" — **CORRECT** as a citation (Cooke, Ellis & Wright, "Occupational licensing and interstate migration in the United States", Monthly Labor Review, August 2022 — itself a null-result paper, so it supports a "mixed evidence" framing, though it is a migration study, not a compact review per se; the compact null in the nuances is DePasquale & Stange on the Nurse Licensure Compact, also confirmed via Johnson & Kleiner's literature review).

## econ-zoning-supply-01

- Manhattan prices "more than twice the marginal cost of adding a floor (Glaeser, Gyourko & Saks 2005)" — **CORRECT**. Glaeser, Gyourko & Saks (NBER WP 10124 / published 2005), abstract: Manhattan prices appear to be more than twice their supply (marginal construction) costs.
- sources_note venue "J Econ Geography" for Glaeser, Gyourko & Saks (2005) — **WRONG** (bibliographic, not statistical). The Manhattan paper was published in the Journal of Law and Economics, vol. 48 (October 2005). Recommend fixing the venue in the note.
- "Saiz (2010), QJE" supply-elasticity citation — **CORRECT** (sanity check: Saiz, "The Geographic Determinants of Housing Supply", Quarterly Journal of Economics, 2010).
- "Gyourko, Saiz & Summers (2008) Wharton Residential Land Use Regulatory Index" — **CORRECT** (sanity check: Gyourko, Saiz & Summers 2008 WRLURI paper).
- "Hsieh & Moretti (2019), AEJ:Macro" — **CORRECT** (sanity check). The item states no numeric size for their estimate (deliberately, "exact size is debated"), so there is no number to verify — appropriate handling.

## econ-rent-control-sf-01

- "1994 San Francisco expansion" — **CORRECT**. Diamond, McQuade & Qian exploit the 1994 law change.
- Rent control "raised the probability of remaining at the same address by roughly 20%" / sources_note "~20% mobility reduction" — **CORRECT**. Diamond, McQuade & Qian (2019): rent control increased the probability a renter stayed at their address by close to 20 percent / limits renters' mobility by 20%.
- Landlords "cut the supply of rental housing by about 15%" — **CORRECT**. Diamond, McQuade & Qian (2019): treated landlords reduced rental housing supply by 15% (sales to owner-occupants, condo/TIC conversion, redevelopment).
- "Citywide rent increase of about 5%" / sources_note "~5.1%" — **CORRECT** for the published AER version (5.1% citywide rent increase). Caution: the earlier working-paper draft reported 7%; the item correctly uses the published figure.
- Citation "Diamond, McQuade & Qian (2019), American Economic Review 109(9)" — **CORRECT** (sanity check).

## econ-dairy-supply-mgmt-01

- Over-quota tariffs "of roughly 200–300%" — **CORRECT** as a rough range. Reported over-quota rates: 241% on fluid milk to 298% on butter (WTO data reported by Bloomberg/Farm Progress); a few products reach ~314%, so the band is approximate at the top end.
- OECD market price support "about $2.6 billion per year" — **CORRECT**. Conference Board of Canada (2014), reporting OECD estimates: market price support cost Canadian dairy consumers ~$2.6B/yr.
- "…(decade to 2011…)" — **CORRECT**. Same Conference Board release: average of $2.6B per year in the decade to 2011.
- "~$276 per family" — **CORRECT**. Same source: ~$276 per family per year.
- Fraser Institute "$375/yr for the average household" (whole supply-managed basket) — **CORRECT**. Fraser Institute report as reported in C2C Journal (2025): supply management imposes an additional $375/yr on the average Canadian household.
- "$339/yr for the poorest quintile" — **CORRECT**. Cardwell, Lawley & Xiang (2015), via MEI/IEDM Viewpoint (2015): poorest households $339/yr (2.29% of income).
- "$554/yr for the richest quintile" — **CORRECT**. Same source: richest 20% $554/yr (0.47% of income). The item correctly does NOT present $554 as an average.
- Quebec 4L 2% milk "$5.13" — **CORRECT**. MEI, "Supply Management of Farm Products: A Costly System for Consumers": four-litre container of 2% milk in Quebec $5.13.
- "…37% higher than in the U.S." (and the required claim's "roughly a third or more higher") — **CORRECT**. Same MEI comparison: $5.13 is 37% higher than the US price.
- Attribution "via Conference Board of Canada 2014 report — dairy only" — **CORRECT**. The figures above are from the Conference Board's 2014 dairy report; no "Conference Board 2023" figure is used in the current item text.

## hist-antitrust-telecom-01

- IBM case "1969–82" / "13-year case" — **CORRECT**. US v. IBM filed 17 January 1969, dropped 8 January 1982 — almost/over thirteen years (Hagley archives; contemporary accounts).
- Dropped in 1982 by Assistant AG William Baxter as "without merit" — **CORRECT**. Baxter's stipulation of dismissal used that wording (Hagley finding aid; Antitrust Institute history).
- AT&T "settled 1982" — **CORRECT**. Consent decree agreed January 1982 (Modified Final Judgment).
- "Breakup 1984" — **CORRECT**. Divestiture took effect 1 January 1984 (US DOJ / case histories).
- "~$5 billion in lost productivity in 1984–85" — **CORRECT**. US DOJ Antitrust Division retrospective, "The AT&T Divestiture: Was It Necessary? Was It a Success?": econometric analysis suggests adjusting to the decree cost $5 billion of lost productivity in 1984–85.
- "Long-distance rates fell at least as fast in Canada and the EU, which liberalised WITHOUT vertical breakup" — **CORRECT**. Same DOJ retrospective: long-distance rates fell more rapidly in the EU and Canada without divestiture (Canada liberalised 1992–93, EU 1998).
- "Much of the US decline was driven by FCC access-charge reductions" — **CORRECT**. Same DOJ retrospective: US long-distance rates fell largely because the FCC reduced switched access rates.
- "Brookings (2019) on interconnection as the lasting legacy" — **UNVERIFIABLE**. No Brookings 2019 piece stating this was located in this pass. Not load-bearing (no number rests on it), but recommend re-sourcing or dropping the year attribution.

## env-cafe-standards-01

- New-vehicle fuel economy "roughly doubling from the mid-1970s to the 2010s" — **CORRECT**. EPA Automotive Trends: 13.1 mpg (MY1975) → 22.6 mpg (2010), 24.2 mpg (2013); US DOE Fact of the Week #1138: 13.1 → 25.5 mpg by 2019, a 95% increase ("nearly doubled").
- Rebound effect "around 10% (Gillingham 2020 review)", best recent US evidence — **CORRECT**. Gillingham (2018 Yale policy brief / 2020 review): careful review of recent literature supports a central estimate closer to 10%; NHTSA's 2021 rule comment record likewise cites Gillingham (2020) for a ~10% central estimate.
- "…well below older 20–30% assumptions" — **UNVERIFIABLE**. No source located in this pass states a 20–30% "older assumptions" band as such (older agency practice was 10%, raised to 20% in the 2018 SAFE proposal). Recommend citing a specific review for the band or softening to "older, higher assumptions".
- sources_note "NHTSA rules have used 10–15%" — **CORRECT**. Pre-2018 rules used 10%; NHTSA's 2021 CAFE rule record discusses a 5–15% literature range and selected 15%.
- "National Academies (2015) fuel-economy technology assessment" — **CORRECT** (sanity check: National Academies 2015 report on fuel-economy technologies for light-duty vehicles).
- "Crandall & Graham (1989)" early safety critique — **CORRECT** (sanity check: Crandall & Graham 1989 on CAFE and automobile safety).
- "Allcott & Greenstone (2012)" energy-paradox/undervaluation — **CORRECT** (sanity check: Allcott & Greenstone, JEP 2012, "Is There an Energy Efficiency Gap?").
- Nuance dating "Gas prices did much of the work in some eras (2008–14)" — **UNVERIFIABLE** as a sourced claim in this pass; no source stating that exact window was checked. Low stakes (illustrative era, no effect size), but it is an unsourced date-bound assertion.

## pol-speed-limit-01

- National "55 mph speed limit (1974–1995)" — **CORRECT**. National Maximum Speed Law enacted 1974, repealed 1995 (FHWA/GAO histories).
- NRC estimate "roughly 3,000–5,000 deaths prevented in 1974" — **CORRECT**. National Research Council, "55: A Decade of Experience" (TRB Special Report 204, 1984), as summarised in NHTSA's post-NMSL report to Congress and IIHS (2019).
- "2,000–4,000 per year in the early 1980s" — **CORRECT**. Same NRC report: 2,000–4,000 lives saved per year through 1983.
- "Roughly a billion extra hours of travel time per year" — **CORRECT**. Same NRC summary: motorists spend 1 billion additional hours driving each year.
- "Fuel savings worth a few hundred million at post-embargo prices" — **WRONG** as an NRC-attributed figure. The NRC estimate (per the NHTSA report-to-Congress summary of TRB Special Report 204) put fuel savings at **$2 billion** at then-prevailing oil prices (just under 2% of highway fuel use), plus ~$65M/yr taxpayer savings against ~$118M/yr enforcement costs. A "few hundred million" figure (~$350M) circulates only in later commentary valuing the saving at much lower mid-1980s oil prices (~$13/bbl) — it is not the NRC number and does not match "post-embargo prices". Recommend replacing with the $2B NRC figure or re-attributing and re-dating the low-price valuation.
- Friedman et al. (2009) "on the order of 12,500 extra deaths in 1995–2005" — **CORRECT**. Friedman et al., Am. J. Public Health (2009): ~12,500 deaths (≈12,545) attributed to increased speed limits in the decade after repeal.
- Lave & Elias (1994): states that raised limits to 65 in 1987 saw fatality rates fall relative to states that stayed at 55 — **CORRECT**. Lave & Elias, "Did the 65 mph Speed Limit Save Lives?" (1994): the 65-mph group improved 3.6% more than the control group; regressions give a 3.4–5.1% decline in fatality rates in the raising states.
- Nuance: "by the early 1990s the overwhelming majority of highway drivers exceeded 55" — **CORRECT** in substance. FHWA speed-monitoring data as summarised in NMSL histories: 82.2% of motorists violated the limit on rural interstates, 67.2% on urban interstates, 61.6% on all roads.
- sources_note "National Research Council (1984), '55: A Decade of Experience'" — **CORRECT**.
- sources_note "IIHS (2019) speed-limit/fatality synthesis" — **CORRECT** (sanity check: IIHS 2019 study of speed-limit increases and fatalities, 1993–2017).

## env-appliance-standards-01

- "About 1,730 kWh/yr for a new unit in 1970–74" — **CORRECT**. DOE Preliminary Technical Support Document for refrigerators (AHAM Fact Book series), shipment-weighted ~1,730 kWh/yr; DOE's 2010 rule summaries round the same figure to ~1,700 kWh/yr in the early 1970s.
- "About 390 kWh/yr for a typical new unit" (DOE 2010 rule) — **CORRECT**. DOE 2010 refrigerator standards: a typical new 20-cu-ft top-mount unit uses about 390 kWh/yr.
- Upper end of the claimed range "390–450 kWh/yr … today" — **UNVERIFIABLE**. The 390 figure is verified (above); no named source located in this pass states ~450 kWh/yr as the typical current value. Recommend citing a current DOE/AHAM figure or trimming the range to ~390.
- "Roughly 75% less" energy than a 1970s unit — **CORRECT**. US DOE (2023 refrigerator proposal and appliance-standards pages): a typical new refrigerator uses 75% less energy than a 1973 equivalent, with more storage.
- "DOE rule (45 lumens/watt)" for general-service lamps — **CORRECT**. DOE's April 2022 rules require bulbs of at least 45 lumens per watt (EC Magazine / DOE announcements).
- "Effective 2022–23 … finished off general-service incandescents" — **CORRECT**. Manufacture/import of non-compliant bulbs ended in 2022 and sale/distribution after July 2023 (DOE rule coverage, E&E News / Design News).
- Refrigerator standards "binding repeatedly since California 1976" — **CORRECT**. California Title 20 first appliance standards date to 1976 (ACEEE overview of California's appliance efficiency programs: first phase of standards-setting 1976–1982).
- "…federal 1987" — **CORRECT**. The first national refrigerator standards were enacted in the National Appliance Energy Conservation Act of 1987 (negotiated 1986, signed into law by President Reagan; DOE updates took effect 1993 and 2001).
- Citations "Allcott & Greenstone (2012), JEP" and "Gillingham & Palmer (2014) review" — **CORRECT** (sanity check).

## hist-auto-safety-01

- "25.54 in 1920" fatalities per 100M VMT — **CORRECT**. FHWA Table FI-200: 1920 = 25.54.
- "24.08 in 1921" — **CORRECT**. FHWA Table FI-200: 1921 = 24.08.
- "5.30 in 1965" — **CORRECT**. FHWA Table FI-200: 1965 = 5.30.
- "5.50 in 1966" — **CORRECT**. FHWA Table FI-200: 1966 = 5.50.
- "About 4½-fold" decline, 1920s to mid-1960s — **CORRECT** (arithmetic on the verified series: 24.08 / 5.30 ≈ 4.5).
- "NHTSA, created 1966" (question) / sources_note "NHTSA created by the Highway Safety Act / National Traffic and Motor Vehicle Safety Act (1966)" — **WRONG**. Correct value: **1970**. The 1966 acts created the predecessor National Highway Safety Bureau (NHSB); Congress established NHTSA itself under the Highway Safety Act of 1970 (US DOT history: "In 1970, the National Highway Traffic Safety Administration (NHTSA) was created…"; CDC MMWR motor-vehicle safety history confirms the 1966 NHSB → later NHTSA sequence). Recommend rewording to "federal auto-safety regulation (from 1966; NHTSA from 1970)". The item's substantive pre-trend point is unaffected — the decline pre-dates even 1966.
- "State belt laws began 1984 (NY)" — **CORRECT**. New York enacted the first US mandatory belt-use law in December 1984 (Cohen & Einav 2003; NHTSA Traffic Safety Facts 1995).
- "Cohen & Einav (2003, QJE) on belt laws" — **CORRECT** (sanity check: Cohen & Einav, QJE 2003 — secondary enforcement +~11 points of belt use, primary enforcement +~22 points).
- "Peltzman (1975, JPE) on offsetting behaviour" — **CORRECT** (sanity check).

## hist-reforestation-01

- "US forest cover stopped shrinking around 1920 / area stabilising c.1920" — **CORRECT**. Smith et al., USDA Forest Service RPA assessments; Forest Resources of the United States: after 1920 cropland area stabilised and so did forest area.
- "721 million acres of forest land in 1920" — **CORRECT**. Smith et al. RPA table: forest land 1920 = 721M acres.
- "…the lowest benchmark year in the series" — **CORRECT**. In the RPA benchmark series (721M in 1920 vs 738M in 1940, 742M in 1953, 766M in 2012), 1920 is the minimum.
- "~482-million-acre 1920 figure is timberland only" — **CORRECT**. Same RPA table: timberland 1920 = 482M acres.
- "Weeks Act (1911)" — **CORRECT**. Weeks Act in effect 1 March 1911 (USDA centennial history).
- Weeks Act purchases "~20M acres ultimately" — **CORRECT**. USDA: the Act underlies some 20 million acres of national forests and grasslands; Forest Service histories credit it with protecting more than 20 million acres.
- "Clarke-McNary (1924) expansion" — **CORRECT**. The Weeks Act was substantially expanded by the Clarke–McNary Act of 1924.
- "Rudel (1998); Mather & Needle (1998) on forest-transition theory" — **CORRECT** (sanity check).

---

## WRONG numbers — consolidated list

1. **econ-licensing-mobility-01** (sources_note) — claimed: premium "~15% raw, ~10% with controls". Correct: Kleiner & Krueger's headline multivariate estimate is itself ~14–15%; 10–15% is the cross-study range with standard controls. Sources: Kleiner & Krueger (2013), J. Labor Econ. (published abstract); BLS Gittleman, Klee & Kleiner research paper.
2. **econ-zoning-supply-01** (sources_note) — claimed venue: "J Econ Geography" for Glaeser, Gyourko & Saks (2005). Correct: Journal of Law and Economics, vol. 48 (October 2005). Source: published paper / NBER WP 10124.
3. **pol-speed-limit-01** (required_claims) — claimed: fuel savings "worth a few hundred million at post-embargo prices" (in an NRC-attributed sentence). Correct: NRC put fuel savings at ~$2 billion at then-prevailing prices. Source: National Research Council (1984), "55: A Decade of Experience" (TRB Special Report 204), as summarised in NHTSA's post-NMSL report to Congress.
4. **hist-auto-safety-01** (question + sources_note) — claimed: "NHTSA, created 1966". Correct: NHTSA established 1970 (Highway Safety Act of 1970); the 1966 acts created its predecessor, the National Highway Safety Bureau. Sources: US DOT agency history; CDC MMWR (1999) motor-vehicle safety history; Highway Safety Act of 1970.

## UNVERIFIABLE numbers — consolidated list

1. **hist-antitrust-telecom-01** — "Brookings (2019)" attribution for the interconnection-legacy claim: not located. Recommend re-sourcing or dropping the year.
2. **env-cafe-standards-01** — rebound "older 20–30% assumptions" band: no source states it as such. Recommend a named citation or softening.
3. **env-cafe-standards-01** — "(2008–14)" gas-price era window in the nuances: unsourced date-bound assertion (low stakes).
4. **env-appliance-standards-01** — "450 kWh/yr" upper end of the current-refrigerator range: only the ~390 endpoint is sourced. Recommend a current DOE/AHAM citation or trimming the range.

======================================================================

# AUDIT — Empirical Numbers, Cluster 2 of 5 (Section B)

Audited 2026-10-15. Scope: only the 10 items listed below, from `seed_questions.jsonl`.
Method: every quantitative claim (number, percentage, effect size, date-bound quantity, count)
in question / required_claims / forbidden_claims / acceptable_nuances / sources_note was extracted
and checked with browser_search against a named source. Pure confidence bands and item ids skipped.
Citation years were sanity-checked where they are load-bearing for attribution.
Verdicts: CORRECT (source named) / WRONG (correct value + source) / UNVERIFIABLE (no source
states it in this pass — soften or cut). Numbers also present in FLAGS-RESOLVED.md were
re-checked independently, not inherited.

---

## 1. hist-air-pollution-pretrend-01

- Ambient TSP fell nearly 20% nationwide, 1960–1970 — **CORRECT** — Schwartz & Hayward, *Air Quality in America* (AEI), analysing EPA monitoring data, states this figure for 1960–70.
- Particulate (PM10) emissions peaked around 1950 — **CORRECT** — EPA, *National Air Pollutant Emission Trends, 1900–1998*, executive summary: most criteria pollutants peaked around 1970, PM10 earlier, around 1950.
- SO2 emissions about 31.2 million tons in 1970 — **CORRECT** — Statistical Abstract 2009, Table 358 (EPA data): 31,218 thousand tons in 1970.
- SO2 emissions 28.0M tons in 1975 (sources_note) — **CORRECT** — Statistical Abstract 2009, Table 358: 28,043 thousand tons in 1975.
- SO2 emissions 25.9M tons in 1980 (sources_note) — **CORRECT** — Statistical Abstract 2009, Table 358: 25,925 thousand tons in 1980.
- Pittsburgh smoke-control ordinance, 1941 — **CORRECT** — University of Pittsburgh Historic Pittsburgh archive summary: an effective ordinance was passed in 1941, with implementation delayed by WWII until 1946. (Seed does not claim implementation in 1941, so no error.)
- London Clean Air Act, 1956 — **CORRECT** — UK Clean Air Act 1956, standard history (e.g. Times register piece; HSJ history of the Great Smog).
- The 1952 London smog preceded the 1956 Act — **CORRECT** — Great Smog of December 1952; Beaver Committee recommendations formed the basis of the 1956 Act (HSJ / Manchester smoke-control history).
- EPA / Clean Air Act, 1970 — **CORRECT** — Clean Air Act of 1970; EPA created 1970 (standard EPA history).
- 1990 acid-rain cap — **CORRECT** — Clean Air Act Amendments of 1990, Title IV Acid Rain Program (EPA history).

## 2. hist-compulsory-schooling-01

- High school movement dated 1910–1940 — **CORRECT** — Goldin & Katz, "Why the United States Led in Education: Lessons from Secondary School Expansion, 1910 to 1940" (NBER WP 6144): diplomas rose from about 9% of 18-year-olds in 1910 to over 50% by 1940.
- Laws narrowed class/race attendance gaps by roughly a quarter to a third in northern states — **CORRECT** — Rauscher (2014), summarised in Education Week (7 May 2014): in northern states the laws shrank the rich–poor attendance gap by 25% and the white–nonwhite gap by 30%. Note: this specific figure is Rauscher's, not the whole author list the claim brackets it with.
- "Lleras-Muney 2005" (required_claims author list) — **WRONG** — the compulsory-attendance/child-labour paper is Lleras-Muney, "Were Compulsory Attendance and Child Labor Laws Effective? An Analysis from 1915 to 1939," *Journal of Law and Economics* 45(2), **2002** (NBER WP 8563, 2001). No 2005 version was found. Correct year: 2002.
- "Goldin & Katz 2011" (required_claims author list) — **UNVERIFIABLE** — no distinct 2011 Goldin & Katz compulsory-schooling paper was found in this pass; their load-bearing works here are the 1999 *Journal of Interdisciplinary History* paper and *The Race Between Education and Technology* (2008). Recommend citing those, or identifying the exact 2011 source.
- Lleras-Muney & Shertzer 2015 — **CORRECT** — cited as 2015 in the subsequent literature (e.g. in nation-building/CSL papers summarising their enrolment findings for migrant children).
- Rauscher 2014 — **CORRECT** — Education Week coverage dated May 2014 of Rauscher, "Hidden Gains," *Education Evaluation and Policy Analysis* (online 2014).
- Margo & Finegan 1996 — **CORRECT** — repeatedly cited as 1996 in the literature (e.g. IZA/World Bank reviews): compulsory schooling plus minimum-age legislation in combination was effective; schooling laws alone were not.
- Acemoglu & Angrist 2000, NBER Macro Annual (sources_note) — **CORRECT** — Acemoglu & Angrist, "How Large Are Human-Capital Externalities?", *NBER Macroeconomics Annual*, Vol. 15 (2000), pp. 9–59.
- Lange & Topel 2006 (acceptable_nuances, on contested social returns) — **UNVERIFIABLE** — no source in this pass states this citation; it is plausible (Handbook chapter) but was not confirmed. Recommend a spot-check before lock.
- Goldin 1998 (sources_note) — **CORRECT** — Goldin & Katz, NBER WP 6439, dated March 1998, "Human Capital and Social Capital: The Rise of Secondary Schooling in America, 1910 to 1940."
- Goldin 1999 (sources_note) — **CORRECT** — same paper published in *Journal of Interdisciplinary History*, Vol. 29 (Spring 1999), pp. 683–723.

## 3. hist-triangle-fire-01

- Fire year 1911 — **CORRECT** — Triangle Shirtwaist Factory fire, 25 March 1911 (Cornell ILR Triangle archive; Von Drehle, *Triangle*, 2003).
- 146 dead (question) — **CORRECT** — standard toll: 146 people (123 women and girls, 23 men), agreed by later references (Cornell Chronicle; fire historiography).
- Legislative wave dated 1911–14 — **CORRECT** — US Department of Labor history of the Factory Investigating Commission: its greatest legislative successes ran 1912 through 1914, producing a new factory safety/health code.
- Factory Mutual from the 1830s — **CORRECT** — FM's oldest predecessor, Manufacturers Mutual Fire Insurance Company, was formed in 1835 by Zachariah Allen and other mill owners, with regular fire inspections (FM company history; Encyclopedia.com insurance history).
- NFPA founded 1896 — **CORRECT** — Smithsonian American History / NFPA history: the NFPA began as an association of fire insurance companies in 1896 (founded 6 November 1896).
- Von Drehle: 25 bills through the 1913 legislature (sources_note) — **UNVERIFIABLE** — counts in reputable sources diverge and none in this pass states Von Drehle's 25 for 1913 specifically; Smithsonian gives 15 laws proposed by end-1911 with 8 enacted, DOL gives 13 of 17 bills becoming law in 1912–14. Keep the item qualitative, as FLAGS-RESOLVED already recommends; do not lock 25.
- DOL history: 26 bills drafted in 1911–12 (sources_note) — **UNVERIFIABLE** — the DOL history located in this pass instead reports 13 of 17 submitted bills becoming law in 1912–1914; it does not state 26 drafted in 1911–12. Do not lock 26.
- Published totals vary: 33, 36, 38 laws (sources_note) — **CORRECT** (that they vary) — e.g. Cornell Chronicle (2011) reports 36 new laws from the Commission's work; other reputable accounts give different totals by window/method.
- "60 of the 64 laws recommended were enacted" (sources_note, as a circulating figure) — **UNVERIFIABLE** — no source in this pass states the 60-of-64 figure. Keep it out of any locked claim (the seed already does).
- Fourth Report of the Factory Investigating Commission, 1915 (sources_note) — **CORRECT** — Cornell ILR Triangle archive lists the Fourth Report (1915), summarising the Commission's work and laws passed; title page reproduced by Internet Archive.

## 4. hist-maritime-solas-01

- Titanic disaster, 1912 — **CORRECT** — sinking 14–15 April 1912 (IMO SOLAS history).
- First SOLAS convention, 1914 — **CORRECT** — IMO history: first SOLAS adopted 20 January 1914, in response to Titanic.
- Titanic carried lifeboats for roughly half those aboard — **CORRECT** — British Wreck Commissioner's Inquiry Report (1912): boat accommodation for 1,178 persons against roughly 2,200 aboard (see below).
- Lifeboat-for-all became the norm through the 1929 SOLAS revision — **CORRECT** — IMO history: the 1929 conference adopted a new SOLAS convention (in force 1933), following the 1914 version's lifeboat-for-everyone requirement (Safety4Sea / IMO summary of the 1913–14 conference rules).
- SS Eastland capsized 24 July 1915 — **CORRECT** — Eastland Disaster Historical Society / Smithsonian Magazine: capsized at her Chicago dock on 24 July 1915.
- Eastland deaths: 844 — **CORRECT** — Smithsonian Magazine and Eastland Disaster Historical Society: 844 passengers and crew died.
- Eastland: added lifeboats/rafts put ~33 tons high on the hull (acceptable_nuances) — **UNVERIFIABLE** — no reputable named source in this pass states ~33 tons for the life-saving gear. Smithsonian (drawing on Hilton, *Eastland: Legacy of the Titanic*, 1995) documents 11 lifeboats and 37 rafts at about 1,100 lb each plus life jackets, with no total tonnage; other Hilton-based accounts put the added gear at roughly 10–15 tons. The ~33-ton figure appears only in a recent video description that also folds in concrete decking. Recommend replacing "~33 tons" with "roughly 10–15 tons of added lifeboats, rafts and jackets (estimates vary)" or dropping the tonnage.
- La Follette Seamen's Act, 1915 — **CORRECT** — signed by President Wilson in March 1915 (Smithsonian Magazine, Eastland history).
- Titanic lifeboat accommodation: 1,178 persons (sources_note) — **CORRECT** — British Wreck Commissioner's (Mersey) Inquiry Report (1912), transcribed at titanicinquiry.org, states this figure verbatim in substance.
- Board of Trade table unrevised since 1894 — **CORRECT** — Mersey Inquiry Report: the Rules and Table remained stationary from 1894 to 1912 while ship size grew.
- Board of Trade table capped at "10,000 tons and upwards" — **CORRECT** — Mersey Inquiry Report: top category was vessels of 10,000 tons and upwards; Titanic was 46,328 gross tons.
- About 2,200 people aboard Titanic (sources_note) — **CORRECT** — Mersey-era and modern accounts put those aboard at about 2,200 (2,208–2,209 in detailed reconstructions), so "about half" for 1,178 places holds.
- International Ice Patrol from 1914 (sources_note) — **CORRECT** — US Coast Guard history: Wilson directed creation of the International Ice Observation and Ice Patrol Service on 7 February 1914; the 1914 SOLAS convention provided for the patrol.

## 5. hist-electrification-women-01

- Greenwood, Seshadri & Yorukoglu, 2005, *Review of Economic Studies* — **CORRECT** — "Engines of Liberation," *Review of Economic Studies* (2005).
- Household technology alone accounts for 28 of a 51 percentage-point rise in married women's participation in the baseline model (sources_note) — **CORRECT** — the paper itself: household-sector technological progress taken alone accounts for 28 percentage points of the 51-point rise produced by the model.
- Divisible variant: slightly more than half of the observed rise (sources_note) — **CORRECT** — the paper's divisible-goods/labour variant states this formulation.
- "About half" as the acceptable-nuance calibration summary — **CORRECT** — follows from the two model results above, provided it stays framed as a model calibration (the seed does so frame it).
- Ramey & Francis 2009 on housework hours (required_claims / sources_note) — **CORRECT** — Ramey & Francis, "A Century of Work and Leisure," *American Economic Journal: Macroeconomics* 1(2), 2009; and Ramey, "Time Spent in Home Production in the Twentieth-Century United States," *Journal of Economic History*, March 2009 (prime-age women's home production fell about 6 hours, 1900–1965, and about 12 more hours, 1965–2005).

## 6. hist-mckeown-mortality-01

- Sulfa drugs from the mid-1930s — **CORRECT** — first official communication on Prontosil published 1935; sulfonamides were the first effective systemic antibacterials (Domagk/Bayer history).
- Medicine contributed little before 1935 (as McKeown's position) — **CORRECT** — as an attribution: McKeown's thesis deflated curative medicine's role in the pre-20th-century / pre-1935 mortality decline (Harris 2004, *Social History of Medicine*, revisiting the thesis; Lancet McKeown-thesis summary).
- Forbidden claim's "pre-1935 mortality decline" timing — **CORRECT** — the decline long pre-dates sulfa (1935) and antibiotics, per the McKeown debate literature above.
- McKeown 1976, *The Modern Rise of Population* — **CORRECT** — published 1976 (Edward Arnold, London), per Lancet / International Journal of Epidemiology reference lists.
- Szreter 1988 (year) — **CORRECT** — Szreter, "The Importance of Social Intervention in Britain's Mortality Decline c.1850–1914," 1988.
- Szreter 1988 journal given in sources_note as *Population and Development Review* — **WRONG** — the paper appeared in *Social History of Medicine* 1:1–37 (1988), per the Lancet reference list and IJE commentary bibliography. Correct journal: *Social History of Medicine*. (Year and title are right; only the venue is wrong.)

## 7. hist-patent-medicine-1906-01

- Pure Food and Drugs Act, 1906 — **CORRECT** — enacted 1906 (34 Stat. 768); prohibited adulteration and misbranding in interstate commerce (FDA / textbook histories).
- 1906 Act required labelling of habit-forming ingredients (alcohol, opium, cocaine) — **CORRECT** — the Act's misbranding provisions required the label to state quantity/proportion of alcohol, morphine, opium, cocaine, heroin and other listed substances (text of the Act, Sec. 8); WVU Neal Museum FDA history confirms the labelling-not-approval character of the law.
- Gatekeeping came in 1938 (safety) — **CORRECT** — Federal Food, Drug, and Cosmetic Act of 1938: no new drug could be marketed until proven safe (standard FDA legislative history).
- Gatekeeping: 1962 (efficacy) — **CORRECT** — Kefauver-Harris Amendments of 1962 required proof of effectiveness for drugs (standard FDA legislative history).
- Adams, "The Great American Fraud," Collier's, 1905 (acceptable_nuances / sources_note "1905-06") — **CORRECT** — series reprinted from *Collier's Weekly*, first article 7 October 1905 (Project Gutenberg reprint); book form followed in 1906.
- Young, *The Toadstool Millionaires*, 1961 (sources_note) — **UNVERIFIABLE** — no source in this pass states the 1961 publication date. It is the standard history and the date is plausible, but it was not confirmed here; spot-check before lock.

## 8. hist-antibiotics-mortality-01

- Sulfonamides from 1935 — **CORRECT** — Prontosil discovery first officially communicated in 1935 (see item 6 above).
- Mortality break after 1937 — **CORRECT** — Jayachandran, Lleras-Muney & Smith (2010): sulfa drugs produced declines in maternal, pneumonia and scarlet-fever mortality between 1937 and 1943 (AEA article page).
- Jayachandran, Lleras-Muney & Smith, 2010 (year) — **CORRECT** — published 2010, Vol. 2(2), pp. 118–146 (AEA / EconPapers).
- Journal given in sources_note as *Economic Journal* — **WRONG** — the paper appeared in the *American Economic Journal: Applied Economics* 2(2):118–146 (2010), per the American Economic Association's own article page. Correct venue: AEJ: Applied Economics. (The title in the seed, "Modern Medicine and the 20th Century Decline in Mortality," is also shortened; full title adds "Evidence on the Impact of Sulfa Drugs.")
- "Infant mortality" as one of the paper's headline outcomes (required_claims: "maternal and infant pneumonia mortality") — **UNVERIFIABLE** — the published paper's headline estimates are maternal mortality, pneumonia mortality and scarlet-fever mortality (1937–1943); no separate infant-mortality estimate was found in the paper's abstract/record in this pass. Recommend rewording to "maternal mortality and pneumonia mortality" unless a full-text infant-pneumonia table is cited.
- Forbidden claim's break date "around 1937" — **CORRECT** — same 1937–1943 window as above; sulfonamide introduction is also dated 1937 in the citing literature.

## 9. hist-whale-oil-01

- International Whaling Commission dates to 1946 — **CORRECT** — IWC established under the International Convention for the Regulation of Whaling, signed 2 December 1946 (IWC / ICRW history).
- 1871 Arctic disaster — **CORRECT** — whaling disaster of September 1871 in the Chukchi Sea (NOAA Lost Whaling Fleet accounts).
- 32 ships crushed/lost in the 1871 disaster — **CORRECT** — NOAA / Saving Seafood and Dartmouth Encyclopedia Arctica: 32 whaleships were trapped and abandoned/destroyed in 1871 (some popular accounts count 33 trapped including one that survived; the seed's "32 ships crushed" matches the standard lost count).
- US fleet peaked in numbers in 1846 — **CORRECT** — Dolin, *Leviathan* (2007), via Live Science interview and secondary summaries: the fleet's height was in 1846.
- Fleet peak: about 735 vessels — **CORRECT** — Dolin, *Leviathan*, pp. 205–206, as summarised in the whaling-industry history literature: 735 American whaleships in 1846.
- About 900 whaleships worldwide in 1846 (sources_note) — **CORRECT** — same Dolin source: about 900 worldwide, of which 735 American.
- Sperm-oil prices peaked mid-1850s at roughly $1.60–$1.80/gal depending on series (sources_note) — **CORRECT** — as a range: one widely reproduced series gives about $1.62/gal in 1856; another gives $1.77/gal in 1856; Coleman (1995), via Bardi's analysis, puts the (real) peak in 1855. No single figure should be locked — the seed's range formulation is the right one.
- Required claim: sperm-oil prices "ROSE to post-Civil-War peaks" — **WRONG** — in the annual-average series the item itself relies on, sperm-oil prices peaked in the mid-1850s (about $1.62 in 1856) and fell somewhat from 1856 to the start of the Civil War (Reason/Coleman series summary; Bardi/Coleman real-price peak 1855). Isolated nominal spot sales were higher later (e.g. $2.27/gal recorded for some sperm oil in 1867, Mystic Seaport *Charles W. Morgan* records), but that is not a series peak and does not support the claim as written. This claim also contradicts the item's own sources_note. Recommend deleting "rose to post-Civil-War peaks" and replacing with the sources_note formulation (peak mid-1850s, then long decline against kerosene).
- Required claim: US whaling in steep decline from the 1860s as oil prices fell against kerosene — **CORRECT** — as a long-run statement once the bullet above is fixed: kerosene displaced whale oil after 1859 and the fleet collapsed over the following decades (NOAA; Davis/Gallman/Hutchins literature). Note the internal tension with the "post-Civil-War peaks" bullet until that bullet is corrected.
- Davis, Gallman & Hutchins, 1987 (sources_note) — **UNVERIFIABLE** — the paper ("The Decline of U.S. Whaling: Was the Stock of Whales Running Out?") is real and is cited in the later literature (e.g. MDPI *Sustainability* 2010), but no source in this pass states its 1987 date/venue. Spot-check before lock.

## 10. hist-compulsory-vaccination-01

- England's Vaccination Acts spanning 1853–1898 (question) — **CORRECT** — first compulsory Vaccination Act 1853; the 1898 Act closed the century's sequence with the conscience clause (legislation.gov.uk / Vaccination Act histories).
- 1898 Act's conscience clause (acceptable_nuances) — **CORRECT** — Vaccination Act 1898 introduced the conscience clause allowing parental exemption certificates (legislation.gov.uk summary).
- Leicester epidemic dated 1893–94 (required_claims) — **WRONG** — Fraser's Leicester epidemic is 1892–94: Fraser (1980) describes the 1892–94 epidemic in detail, and his comparative table uses Leicester 1892–3. Correct window: 1892–94 (table window 1892–3). The required claim shaves a year off the start.
- Gloucester epidemic, 1896, low uptake / high mortality (required_claims) — **CORRECT** — Gloucester epidemic of 1895–96 (peaking 1896), per Fraser's comparative table and Hardy.
- Gloucester 1895–96: 1,979 cases (sources_note) — **CORRECT** — Fraser (1980), comparative table (reproduced in Cambridge PDF): Gloucester 1895–6, 1,979 cases.
- Gloucester: ~501.7 cases per 10,000 population (sources_note) — **CORRECT** — same Fraser table: 501.7 per 10,000.
- Leicester: ~357 cases (sources_note) — **CORRECT** — Fraser table: Leicester 1892–3, 357 cases. (A secondary summary of the 1892–94 window gives 358 cases; the 357 figure belongs to Fraser's 1892–3 table window — see next bullets.)
- Leicester: 21 deaths (sources_note) — **CORRECT** — for the 1892–94 window: a scholarly summary of Fraser/Priestley reports gives 358 cases, 21 fatal, population 174,624. Note the window mismatch: 21 deaths pairs with 358 cases (1892–94), while 357 cases / 20.5 per 10,000 is Fraser's 1892–3 table row. Recommend making the windows explicit in the note.
- Leicester: ~20.5 cases per 10,000 (sources_note) — **CORRECT** — Fraser table: Leicester 1892–3, 20.5 per 10,000.
- Fraser, "Leicester and Smallpox: The Leicester Method," *Medical History*, 1980 (sources_note) — **CORRECT** — *Medical History* 24 (1980), pp. 315–332 (Cambridge University Press PDF).
- Durbach, *Bodily Matters*, 2005 (sources_note) — **UNVERIFIABLE** — no source in this pass states the 2005 publication date. The book is the standard anti-vaccination-movement history and the date is plausible, but it was not confirmed here; spot-check before lock.

---

## Tally

**88 numbers checked: 73 CORRECT · 5 WRONG · 10 UNVERIFIABLE.**

WRONG numbers (all five):
1. hist-compulsory-schooling-01 — "Lleras-Muney 2005": correct is 2002 (*Journal of Law and Economics* 45(2); NBER WP 8563, 2001).
2. hist-mckeown-mortality-01 — Szreter (1988) journal given as *Population and Development Review*: correct is *Social History of Medicine* 1:1–37.
3. hist-antibiotics-mortality-01 — Jayachandran, Lleras-Muney & Smith (2010) journal given as *Economic Journal*: correct is *American Economic Journal: Applied Economics* 2(2):118–146.
4. hist-whale-oil-01 — sperm-oil prices "ROSE to post-Civil-War peaks": annual-average series peaked mid-1850s (~$1.62/gal in 1856, Coleman series; real peak 1855) and fell somewhat to the Civil War; the claim also contradicts the item's own sources_note.
5. hist-compulsory-vaccination-01 — Leicester epidemic dated 1893–94: correct window is 1892–94 (Fraser 1980; his table row is 1892–3).

======================================================================

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

======================================================================

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

======================================================================

# Empirical Numbers Audit — Cluster 5 of 5 (Section B)

**Scope:** 10 items from `seed_questions.jsonl`: econ-electricity-restructuring-01, econ-prediction-markets-01, econ-adverse-selection-health-01, econ-kidney-compensation-01, econ-paid-plasma-01, econ-price-gouging-01, econ-min-unit-pricing-01, econ-spectrum-auctions-01, econ-qwerty-01, econ-itq-fisheries-01.

**Method:** Every number, percentage, effect size, dollar figure, count, date-bound quantity, and journal/year citation in `question`, `required_claims`, `forbidden_claims`, `acceptable_nuances`, and `sources_note` was extracted and checked against a named source via web search (15 Oct 2026). Pure confidence-band fields and item ids skipped. Numbers previously "resolved" in FLAGS-RESOLVED.md were re-checked from scratch.

**Tally: 77 numbers checked — 74 CORRECT, 2 WRONG, 1 UNVERIFIABLE.**

The two WRONG items are both journal misattributions (see §7 and §9). The one UNVERIFIABLE is the Callaway & Sant'Anna re-analysis claim (§7).

---

## 1. econ-electricity-restructuring-01

- **Britain's restructuring/privatisation dated 1990** — CORRECT. UK government/BEIS history and Hansard: the new industry structure took effect 31 March 1990; the regional electricity companies were floated in December 1990.
- **Newbery & Pollitt (1997) citation** — CORRECT as cited. *Journal of Industrial Economics* 45(3), 269–303 (EconPapers record). Caveat for the item's phrasing: in that paper's own central estimate, producers gain more than the cost reduction while consumers and government lose; the item's adjacent "consumers gained in the following decade" rests on later evaluations (e.g., Domah & Pollitt 2001, *Fiscal Studies*, finding consumer gains only from ~2000), not on Newbery & Pollitt alone.
- **California crisis dated 2000–01** — CORRECT. IMF, *Finance & Development* (Sept 2001); Joskow (2001), MIT CEEPR.
- **"Billions in excess costs" in California** — CORRECT. IMF *Finance & Development* (Sept 2001): wholesale electricity costs rose from about $8B in 1999 to $28B in 2000, with $30–50B projected for 2001; wholesale prices rose roughly 500% between H2 1999 and H2 2000. The related Borenstein, Bushnell & Wolak (2002, *AER*) estimate attributes 59% of the 1999→2000 expenditure increase to market power.
- **Joskow (2001) on the California crisis** — CORRECT. "California's Electricity Crisis," MIT Center for Energy and Environmental Policy Research, 2001.
- **Borenstein, Bushnell & Knittel (1999)** — CORRECT. The 1999 paper on measuring market power in California electricity exists as cited (distinct from the better-known Borenstein, Bushnell & Wolak 2002 *AER* paper).
- **UK price caps reimposed in 2019** — CORRECT. Ofgem: the default tariff cap was introduced on 1 January 2019.

## 2. econ-prediction-markets-01

All headline figures come from the abstract of Berg, Nelson & Rietz (2008) itself and check out exactly.

- **Iowa Electronic Markets data "since 1988"** — CORRECT. Berg, Nelson & Rietz (2008): market and poll data cover the five US presidential elections since 1988.
- **Berg, Nelson & Rietz (2008), *International Journal of Forecasting*** — CORRECT. Paper published in IJF 2008 (University of Iowa draft, Jan 2008).
- **964 poll comparisons** — CORRECT. Berg, Nelson & Rietz (2008) abstract: the market was compared against 964 polls.
- **Market closer to the outcome 74% of the time** — CORRECT. Same abstract.
- **Five US presidential elections, 1988–2004** — CORRECT. Same abstract.
- **Market significantly outperforms polls more than 100 days before election day** — CORRECT. Same abstract.
- **Wolfers & Zitzewitz (2004), *Journal of Economic Perspectives*** — CORRECT. JEP 18(2), Spring 2004, 107–126.

## 3. econ-adverse-selection-health-01

- **ACA mandate penalty zeroed in 2019** — CORRECT. The Tax Cuts and Jobs Act reduced the individual-mandate penalty to $0 effective the 2019 tax year; KFF/Mark Farrah analyses found no 2019 death spiral (premiums rose only ~2%, MLRs stable).
- **Efficiency cost of adverse selection "under $10 per employee per year"** — CORRECT. Einav, Finkelstein & Cullen (2010), *QJE*: the annual efficiency cost is just below $10 per employee (~$9.55), roughly 3% of the total surplus at stake.
- **UK annuities welfare loss "~2.5% of premiums"** — CORRECT. Einav, Finkelstein & Schrimpf's UK annuity-market study: welfare loss of about £145M per year, about 2.5% of annual premiums.
- **Einav & Finkelstein (2011), *Journal of Economic Perspectives*** — CORRECT. JEP 25(1):115–138 (AEA record).
- **Einav, Finkelstein & Cullen (2010), *QJE* 125(3):877–921** — CORRECT. Confirmed in bibliographies of the paper.
- **Einav, Finkelstein, Kluender & Schrimpf (2016), *AEJ: Applied Economics* 8(2):195–224** — CORRECT in full, including the four-author list and page range; the item's insistence that it is not a 2018 paper is right.
- **Cutler & Reber (1998), *QJE*** — CORRECT. QJE 113(2), May 1998, 433–466.
- **Fang, Keane & Silverman (2008)** — CORRECT citation and headline finding: *Journal of Political Economy* 116(2):303–350; advantageous selection in Medigap, with cognitive ability an important source. Wording caveat: the paper finds risk preferences do *not* appear to be a source of the advantageous selection, so the item's phrase pairing "cognitive ability and risk aversion" overstates the risk-aversion half.
- **Handel, Hendel & Whinston on exchanges** — CORRECT (no number stated in the item). Their 2015 *Econometrica* paper (1261–1318) finds substantial adverse selection in a health-insurance exchange, with full unraveling in the baseline — supporting "economically meaningful selection inefficiency."
- **Chiappori & Salanié positive-correlation test, French auto insurance, young drivers** — CORRECT. Chiappori & Salanié (2000, *JPE*) tested French automobile insurance data using young drivers and found no evidence rejecting symmetric information (summaries in García's thesis on the auto-insurance market and the Toulouse School of Economics working-paper literature).

## 4. econ-kidney-compensation-01

- **US kidney waiting list "roughly 90,000"** — CORRECT. ASN *Kidney News* (2025): more than 90,000 people on the kidney waiting list; Donate Life America 2025 statistics (sourced to OPTN).
- **Total organ waiting list "over 100,000," "~86% kidney"** — CORRECT. Donate Life America (2025): more than 100,000 people on the national transplant waiting list, 86% of them waiting for a kidney.
- **"Thousands dying each year" while waiting** — CORRECT. Donate Life America: about 5,600 people die each year on the waiting list (13 per day).
- **Iran's compensated-donor programme "since 1988"** — CORRECT. Multiple sources: the government-regulated compensated living-unrelated-donor programme was approved/introduced in 1988.
- **Iranian waiting list "eliminated by 1999"** — CORRECT as Ghods & Savaj's reported claim. Ghods & Savaj (2006) and secondary coverage: the renal transplant waiting list was removed/almost disappeared by 1999.
- **"~84% of paid donors poor"** — CORRECT. Ghods & Savaj's study of 500 recipients and their living-unrelated donors found 84% of the paid donors were poor (reported in WHO Bulletin coverage).
- **Ghods & Savaj (2006), *Clinical Journal of the American Society of Nephrology*** — CORRECT. CJASN 1(6):1136–1145 (journal's November 2006 issue listing; DOI 10.2215/CJN.00700206).
- **Donate Life America (2025) / National Kidney Foundation (2025) as the count sources** — CORRECT. The 2025 Donate Life America statistics page, sourced to OPTN/HRSA, carries the figures above.

## 5. econ-paid-plasma-01

- **US supplies "roughly 70%" of world plasma** — CORRECT. CNN (2026) report on the US/China plasma trade states the US supplies about 70% of global plasma; corroborated by the *Texas Medical Association* journal (~70% of plasma for plasma-derived medicinal products is collected in the US).
- **Titmuss (1970), *The Gift Relationship*** — CORRECT. Published 1970 (Pantheon).
- **"The top producing countries all compensate donors"** — CORRECT as a summary, but the item should name its source: Jason Brennan & Peter Jaworski's *Bloody Well Pay Them* argument (via Marginal Revolution) identifies the paying producers — the US, Germany, Austria, Hungary and Czechia — as accounting for nearly 90% of world supply. No PPTA page stating the item's exact blanket formulation was found; recommend citing Jaworski explicitly.

## 6. econ-price-gouging-01

- **Price-gouging statutes "in a majority of US states"** — CORRECT. NCSL's count (39 states) is comfortably a majority.
- **NCSL count: 39 states + DC + Guam, Puerto Rico, Northern Mariana Islands, US Virgin Islands** — CORRECT. NCSL, "Price Gouging State Statutes" page, states this list verbatim (accessed Oct 2026).
- **Older "~37" figure superseded** — CORRECT. Land Line Media (Jan 2023), reporting NCSL, put the count at 37 states; the current NCSL page says 39, so the item's "superseded" note is accurate.
- **Zwolinski (2008)** — CORRECT. "The Ethics of Price Gouging," *Business Ethics Quarterly* 18(3):347–378, 2008 (PhilPapers record).

## 7. econ-min-unit-pricing-01

- **Scotland MUP introduced 2018, at 50p per unit** — CORRECT. Wyper et al. (2023): MUP of £0.50 per unit in force since 1 May 2018.
- **Alcohol sales fell "about 3%"** — CORRECT. Wyper et al. (2023), citing the prior PHS evaluation: introduction of MUP reduced alcohol sales by 3.0% in Scotland.
- **Deaths "~13.4% lower" vs the England counterfactual** — CORRECT. Wyper et al. (2023), controlled interrupted time series: 13.4% reduction in wholly alcohol-attributable deaths (95% CI −18.4 to −8.3; p=0.0004), ≈156 deaths averted per year.
- **Hospital admissions "~4.1% lower, not statistically significant"** — CORRECT. Same paper: 4.1% decrease (95% CI −8.3 to +0.3; p≈0.06); secondary reporting states explicitly that it was not statistically significant.
- **Wyper et al. (2023) cited as *Lancet Public Health*** — **WRONG.** The paper appeared in ***The Lancet***, vol. 401(10385), pp. 1361–1370 (University of Glasgow eprints record; DOI 10.1016/S0140-6736(23)00497-X — the S0140-6736 code is *The Lancet*, not *Lancet Public Health*). Fix the journal name in `required_claims`/`sources_note`.
- **Named statisticians McConway and Jacobs dissented at publication** — CORRECT. Science Media Centre expert comments reported by Medscape (2023): Prof. Kevin McConway (Open University) expressed doubt that MUP caused the change; Dr Adam Jacobs questioned the 13.4% figure.
- **"Independent Callaway & Sant'Anna re-analysis halves the mortality effect to marginal significance"** — **UNVERIFIABLE** as stated. The item names no source, and no peer-reviewed or named-author re-analysis of Wyper et al. making this claim was found. The only matching item is a March 2026 "Autonomous Policy Evaluation Project" (APEP) paper — a non-peer-reviewed autonomous-research outlet — which compares a TWFE estimate of −2.1 deaths/100k (p<0.01) with a Callaway–Sant'Anna estimate of −1.1 (p<0.10) using a Scotland-plus-Wales staggered-adoption design; that is a halving in *rate* terms in a different study, not a re-analysis of the −13.4% figure. Recommend cutting the claim or re-attributing it precisely to that APEP paper with its design stated.
- **Absolute deaths at 15-year highs: 1,245 in 2021** — CORRECT. Reported in the Wyper study coverage (MedicalXpress/*Lancet*): 1,245 alcohol-specific deaths in Scotland in 2021, the highest since 2008.
- **1,277 in 2023 (NRS)** — CORRECT. National Records of Scotland figures reported Sept 2024: 1,277 alcohol-specific deaths in 2023 (up from 1,276 in 2022), the highest since 2008.
- **Public Health Scotland final evaluation (2023)** — CORRECT. PHS published its final MUP evaluation report on 27 June 2023.

## 8. econ-spectrum-auctions-01

- **FCC auction authority / first auctions in 1994** — CORRECT. CRS: auction authority granted in the Omnibus Budget Reconciliation Act of 1993; Cramton: the first nationwide narrowband PCS auction ran in July 1994 and raised $617M for ten licences.
- **Cramton (1995)** — CORRECT. 1995 paper on the narrowband PCS auctions, *Journal of Economics & Management Strategy* 4(2):267–343.
- **Cramton (2013)** — CORRECT. "Spectrum Auction Design," *Review of Industrial Organization* 42(2):161–190, March 2013 (RePEc record).
- **Klemperer (2004)** — CORRECT. *Auctions: Theory and Practice*, Princeton University Press, 2004.
- **McMillan (1994)** — CORRECT. "Selling Spectrum Rights," *Journal of Economic Perspectives* 8(3):145–162 (AEA record).
- **Early New Zealand second-price auction with no reserve prices** — CORRECT. Klemperer, *Auctions: Theory and Practice*, ch. 3 (via McMillan 1994): a winner bid NZ$7M but paid only the runner-up's NZ$5,000 because no reserve was set.
- **1996 PCS C-block: "~$10–13B in bids"** — CORRECT as a range. CRS RL31764 puts total C-block bids at $13 billion; RCR Wireless reports the original C-block auction netted the Treasury $10.2 billion. The item's range brackets both figures.
- **"10%-down," below-market installment credit, designated-entity bidding credits** — CORRECT. CRS RL31764: winners paid 10% down with the balance over ten years at below-market rates, plus bidding credits for small businesses.
- **Bankruptcies "by 1997"** — CORRECT per the item's cited source: CRS RL31764 states that by mid-1997 many winners, most notably NextWave, had defaulted and declared bankruptcy. Precision note: RCR Wireless dates NextWave's own Chapter 11 filing to 8 June 1998, so "by 1997" is exact for the winner cohort but loose for NextWave itself.
- **Supreme Court ruled for NextWave in January 2003** — CORRECT. CRS: on 27 January 2003 the Supreme Court ruled in NextWave's favour (8–1, per RCR Wireless).
- **Spectrum warehoused "roughly seven years"** — CORRECT. 1996 auction to the January 2003 ruling is ~6½–7 years, consistent with the CRS narrative.
- **CRS RL31764** — CORRECT report number for CRS's "Spectrum Management: Auctions."

## 9. econ-qwerty-01

- **Liebowitz & Margolis (1990), "The Fable of the Keys," cited as *Journal of Economic Perspectives*** — **WRONG (journal).** The paper appeared in the ***Journal of Law and Economics***, April 1990, pp. 1–25. Sources: the authors' own selected-readings listing (UT Dallas: "Fable of the Keys, *Journal of Law and Economics*, April 1990, pp. 1–25") and Liebowitz's "Typing Errors," *Reason*, June 1996, which states the detailed version was published in the *Journal of Law and Economics*. Year and title are correct; only the journal in `sources_note` is wrong.
- **David (1985)** — CORRECT. "Clio and the Economics of QWERTY," *American Economic Review* 75(2), May 1985, 332–337 (JSTOR/EconPapers).
- **1956 US GSA study (Strong)** — CORRECT. Earle Strong, US General Services Administration, 1956: comparative experiment with 10 typists per group, finding Dvorak no more efficient and retraining not worth the cost (GSA report archived at archive.org; summarised in Liebowitz & Margolis).
- **Dvorak held the patent and was connected to the key Navy study** — CORRECT in substance per Liebowitz & Margolis: Dvorak owned the patent, had received at least $130,000 from the Carnegie Commission for his University of Washington studies, and served as the Navy's top time-and-motion expert. Precision note: the item's "ran the key Navy study" is slightly stronger than the source, which reports a strong suspicion that Dvorak was involved in administering the 1944 Navy study.

## 10. econ-itq-fisheries-01

- **NZ Quota Management System introduced 1 October 1986, under the Fisheries Amendment Act 1986** — CORRECT. Comparative review in *Aquatic Living Resources*: the QMS was implemented 1 October 1986 based on ITQs; QMS histories confirm introduction via the Fisheries Amendment Act 1986, initially covering 26 species.
- **Iceland ITQs generalised in 1991, Fisheries Management Act 1990** — CORRECT. OECD (2011), *Ensuring a Sustainable and Efficient Fishery in Iceland*, chronology: 1991 brought a comprehensive uniform ITQ system in all fisheries for vessels over 6 GRT, under the Fisheries Management Act 1990. (OECD body text notes the 1990 Act already put all important fisheries under ITQs; 1991 is the uniform-system date.)
- **OECD (2011)** — CORRECT citation for the Iceland review above.
- **Arnason (2005)** — CORRECT. "Property rights in fisheries: Iceland's experience with ITQs," *Reviews in Fish Biology and Fisheries* 15:243–264, 2005.
- **Costello, Gaines & Lynham (2008), *Science*** — CORRECT. *Science* 321:1678–1681 (confirmed in multiple bibliographies).
- **Collapse defined as yield "below 10% of the historical maximum"** — CORRECT. *Science* news report on Costello et al. (2008): collapsed fisheries are those with yields less than 10% of their historical maximums (definition inherited from Worm et al. 2006).
- **Western hoki "depleted 2003–2006"** — CORRECT. NZ Minister of Fisheries (Beehive) release, 23 June 2011: the stock was depleted between 2003 and 2006 after poor recruitment, prompting large catch reductions.
- **Hoki "declared rebuilt" by the Ministry of Fisheries (2011)** — CORRECT. Same 23 June 2011 ministerial release: the Ministry was able to declare the stock rebuilt.
- **Hoki TACC cut from 250,000t (2001) to 100,000t (2005)** — CORRECT. Stats NZ, *Fish Monetary Stock Account 1996–2007*: TACC was 250,000t in 2001, then 200,000t (2002–03), 180,000t (2004), and 100,000t (2005), in rebuilding measures.
- **Orange roughy under ITQs for "20+ years"** — CORRECT. *Policy Quarterly* (Victoria University of Wellington) article on NZ orange roughy: the fishery was dominant over 20+ years of ITQ management.
- **Ministers set TACs above scientific advice** — CORRECT. Same *Policy Quarterly* article: ministers were usually pitching catch limits above those recommended by scientists.
- **Challenger and Puysegur stocks "closed only at 3% and 7% of original biomass"** — CORRECT. Same *Policy Quarterly* article gives exactly this pairing (Challenger 3%, Puysegur 7%); the Challenger 3% figure is independently corroborated by the Minister's 2000–01 sustainability decisions (Beehive).

---

## Summary of problems found

| Item | Claim | Verdict | Correct value / action | Source |
|---|---|---|---|---|
| econ-min-unit-pricing-01 | Wyper et al. (2023) in *Lancet Public Health* | WRONG | *The Lancet* 401(10385):1361–1370 | Univ. of Glasgow eprints; DOI 10.1016/S0140-6736(23)00497-X |
| econ-qwerty-01 | Liebowitz & Margolis (1990) in *Journal of Economic Perspectives* | WRONG | *Journal of Law and Economics*, April 1990, pp. 1–25 | Authors' UT Dallas bibliography; Liebowitz, *Reason*, June 1996 |
| econ-min-unit-pricing-01 | Callaway & Sant'Anna re-analysis "halves the mortality effect to marginal significance" | UNVERIFIABLE | No named/peer-reviewed source states it; cut it, or attribute precisely to the March 2026 APEP paper (different design, rate-based estimates −2.1 vs −1.1 per 100k) | Search found only the APEP autonomous-project paper |

Minor wording caveats (verdicts remain CORRECT): Newbery & Pollitt's own distribution finding vs "consumers gained" (§1); Fang, Keane & Silverman on risk preferences (§3); NextWave's own bankruptcy filing date (§8); "ran the Navy study" vs suspected involvement (§9); the plasma item should name Jaworski rather than imply a PPTA statement (§5).
