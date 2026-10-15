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
