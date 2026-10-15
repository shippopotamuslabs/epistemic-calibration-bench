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
