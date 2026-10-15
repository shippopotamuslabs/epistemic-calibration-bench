# ADVERSARIAL AUDIT — Market / Trend / Mechanism-Crediting Items

**Auditor role:** hostile expert. Job: attack every gold that credits markets, pre-existing
trends, income growth, private mechanisms, or audits a pro-intervention fable, using the
strongest published counterexample or critique available — evidence the intervention
worked, pre-trends that are themselves policy-caused, cherry-picked windows, replication
disputes, under-weighted benefits, cases cutting the other way.

**Scope:** 37 items (the 36 named in the commission plus `econ-comparative-advantage-01`,
a deductive item in the same direction). Method: rubric text read in full from
`seed_questions.jsonl`; one or more targeted literature searches per item family,
2026-10-15. `seed_questions.jsonl` was NOT edited.

**Verdict key:** SURVIVES = hostile case does not move any required/forbidden claim.
REVISE = named claim must be fixed, scoped, or downgraded. DEMOTE = gold should become
Contested or flip.

## Headline result

| Verdict | Count |
|---|---|
| SURVIVES | 23 |
| REVISE | 14 |
| DEMOTE | 0 |

No gold flips outright — but that is partly because the soft items were already graded
Contested at drafting. Fourteen items need surgery, three of them major, and one
embarrassment is structural: **the pool contradicts itself** — `hist-child-labour-01`
lists state compulsory schooling as a *main driver* of the child-labour decline while
`hist-compulsory-schooling-01` says those same laws "bound only for a small margin."
A hostile expert will find that pair within ten minutes. Both items lean on the same
literature (Margo & Finegan 1996; Moehling 1999; Lleras-Muney 2005; Goldin & Katz 2011)
and read it in opposite directions. This is the audit's most damaging finding because
it is not a matter of interpretation — it is an internal inconsistency in the locked pool.

---

## The three most damaging findings (summary; details in item sections)

1. **Child labour + compulsory schooling (REVISE, major, both).** The "laws largely
   codified a trend" gold rests on the older Landes & Solmon (1972) / Moehling (1999)
   reading. The modern literature cuts the other way at the margin that matters:
   Margo & Finegan (1996) found compulsory-schooling laws were ineffective *alone* but
   binding *in combination with* child-labour laws; Bugni (2009) shows Moehling-style
   difference-in-differences estimates are biased toward zero under Basu & Van
   general-equilibrium effects and finds child-labour legislation *was* effective at
   reducing general child employment (ineffective only in manufacturing — Moehling's
   sector, in a window ending 1910). Lleras-Muney (2005) and Goldin & Katz (2011) —
   the very authorities the schooling item cites — assign the laws a real, significant
   role. Both items' Moderate-Strong grades overstate how settled "codification" is.

2. **Lead paint pre-trend (REVISE, major).** The required claim that interior paint was
   "effectively de-leaded by a 1955 voluntary industry standard" is the pool's most
   vulnerable sentence. The appellate record in the NL Industries litigation notes the
   1955 ASA Z66.1 standard imposed **no labelling requirement**, and whether it drove
   actual compliance is contestable; the 1% limit it set is ~10,000 ppm — hardly
   "de-leaded" against the 1978 limit of 0.06%. Markowitz & Rosner's *Deceit and Denial*
   documents the Lead Industries Association suppressing hazard knowledge for decades,
   and the US declined the 1922 League of Nations interior white-lead ban that 20+
   countries adopted — under industry pressure. The pre-trend *fact* (decline before
   1978) is solid; the *attribution* to voluntary action is level-smuggling of exactly
   the kind this benchmark exists to catch: the shift occurred under public-health
   pressure, local bans (Baltimore 1951 — in the rubric), pigment economics, and
   liability shadow. The rubric credits the trend and quietly assigns it to voluntarism.

3. **English literacy (REVISE).** Required claim 2 calls pre-1870 provision "pre-state."
   It was not. Parliament's first education grant (£20,000 to the church school
   societies) dates to **1833**; by 1862 the grant had risen to ~£775,000, with a state
   inspectorate from 1839 and payment-by-results from the early 1860s. The 1850s–60s
   cohorts whose 1871 marriage signatures the item relies on were educated inside a
   *state-subsidised* voluntary system. The gold's numbers survive; its mechanism
   label ("dense mix of private, church, charity…" provision *before the state*) is
   historically wrong for the cohorts in question, and Sweden's church-examination
   system was itself a state-church compulsion apparatus, not a market outcome.

---

## Item-by-item findings

### econ-rent-control-01 — REVISE (scope)
Rubric (Strong) requires supply-reduction, incumbent-benefit, and lock-in claims with no
generation qualifier. Hostile case: the required claims are well-supported for *strict /
first-generation* control, but the second-generation rent-stabilisation literature is
genuinely mixed — Gilderbloom & Ye (2007) found little new-construction effect across
New Jersey municipalities; Turner (1990, DC) similarly weak; Arnott's "Time for
Revisionism on Rent Control?" (*Journal of Economic Perspectives*, 1995) is the canonical
statement that the textbook verdict over-generalises from hard controls. Autor, Palmer &
Pathak (2014) on Cambridge decontrol also complicate the simple supply story.
**Fix:** scope required claims to strict/binding controls and long horizons; add a
nuance that evidence for vacancy-decontrolled stabilisation regimes is weaker and
contested. As written, a model that recites the strong verdict about *all* rent
regulation scores full marks for an overclaim.

### econ-price-ceiling-01 — SURVIVES
Deductive item. The only hostile lever is the textbook monopoly exception (a ceiling
between monopoly and competitive price can raise output), which qualifies the model's
domain, not its claims — the rubric's required claims are stated for the standard
competitive setup, and the WWII OPA record (shortages, quality degradation, rationing)
confirms rather than refutes them. No change.

### econ-tariff-incidence-01 — SURVIVES
Near-complete pass-through of the 2018–19 tariffs is confirmed by Amiti, Redding &
Weinstein (2019) and Fajgelbaum et al. (2020), including retaliation. Hostile wrinkles
are sector-level: ARW's follow-up found foreign *steel* exporters absorbed some of the
tariff via lower pre-tariff prices, and Cavallo et al. (2019) found incomplete
pass-through for some Chinese agricultural goods. The rubric already requires the
terms-of-trade nuance. The optimal-tariff theorem (a large country can gain from a
small tariff absent retaliation) is a welfare point, not an incidence refutation, and
the rubric does not forbid it. No change.

### econ-comparative-advantage-01 — SURVIVES
Deductive. Samuelson's (2004) caveat — a partner's productivity growth in *your* export
sector can worsen your terms of trade — qualifies the gains' distribution over time,
not the existence of mutual gains from comparative advantage, which is all the rubric
requires. No change.

### econ-licensing-01 — REVISE (minor; health-sector carve-out)
Required claim: quality/safety evidence is "weak or inconsistent for most licensed
occupations studied." Hostile case: in health professions there is a real literature
linking nursing licensure/scope regulation to patient outcomes (work by Needleman,
Aiken and co-authors; surveyed in Benton et al. 2018's bibliometric review), which a
hostile expert will deploy against the blanket phrasing. Kleiner's own reviews and the
2015 White House report (stricter licensing associated with quality improvement in only
2 of 12 studies) support the rubric's centre of mass — but "most occupations" needs
the carve-out made explicit.
**Fix:** scope the quality claim to non-health occupations, or add a required nuance
that health-professions evidence is the contested exception.

### hist-lead-paint-pretrend-01 — REVISE (major; downgrade to Moderate)
See damaging finding #2. Required claim 1 must be rewritten: replace "effectively
de-leaded by a 1955 voluntary industry standard" with a mixed-causes claim — industry
moved away from interior white lead by the 1950s under pigment economics (TiO₂),
public-health pressure, local bans, and an industry standard whose compliance and
labelling force are contested in the litigation record; the Lead Industries
Association simultaneously resisted bans elsewhere (US non-adoption of the 1922
international interior white-lead ban). The 1978-ban-mattered claim and both forbidden
claims survive intact.

### hist-child-labour-01 — REVISE (major; downgrade to Moderate)
See damaging finding #1. The pre-1938 decline and the FLSA's ~6% coverage are
undisputed and keep the item's core. What fails is "laws largely codified" at
Moderate-Strong: Margo & Finegan (1996) show schooling + child-labour laws bound
jointly; Bugni (2009) shows the modest-effects estimate may be a GE artefact and
finds legislation effective outside manufacturing; Moehling's window ends in 1910,
before the state-law regime matured.
**Fix:** required claim 3 becomes "income growth was the largest driver; state
law *combinations* (compulsory schooling plus child-labour law) bound at the margin
increasingly after 1900 — how much is contested." Also resolve the contradiction with
`hist-compulsory-schooling-01` (below) in one direction or the other.

### hist-osha-pretrend-01 — REVISE (minor)
Already Contested, and the aggregate-trend claims are fair. But required claim 3's
"mixed and effect sizes are debated" understates the best-identified micro evidence:
Gray & Scholz (1993) found penalty inspections cut lost-workday injuries ~22% in
inspected plants; Mendeloff & Gray's programme of work finds persistent
inspection-with-penalty effects; Levine, Toffel & Johnson (*Science*, 2012), using
randomised California inspections, found ~9.4% fewer injury claims with no detectable
employment or survival harm. A hostile expert will say the rubric grades the
intervention by its weakest evidence (aggregate trend) while the strongest evidence
(firm-level causal) is waved at as "plausible."
**Fix:** claim 3 should state that inspection-level causal effects are consistently
positive in the identified literature, while *aggregate* attribution of the fatality
trend remains unsettled.

### hist-literacy-01 — REVISE
See damaging finding #3. Numbers (≈80% of grooms, 73% of brides signing by 1871)
survive. **Fix:** strike "pre-state provision"; describe the system accurately as a
voluntary sector subsidised and inspected by the state from 1833. Also note the
standing measurement caveat (signature ≠ reading fluency; Schofield/Mitch) — the
rubric's Sweden example should be labelled a church-state examination system, not
private provision.

### hist-standard-oil-01 — REVISE (minor)
The price and share series in the required claims are accurate, and McGee (1958)
remains standing on predatory pricing. Hostile case: Granitz & Klein ("Monopolization
by Raising Rivals' Costs: The Standard Oil Case," *Journal of Law and Economics*,
1996) argue Standard's power ran through enforcing the railroad transport cartel —
when the cartel held, Standard sold refined product at monopoly prices and bought
crude at monopsony prices; McGee does not address this mechanism. Falling kerosene
prices also do not establish prices at the competitive level — costs were falling
industry-wide. The rubric's forbidden claims only block "raised prices" and "share
still rising," leaving a model free to imply benign dominance.
**Fix:** add a required nuance: falling prices are consistent with prices above the
competitive counterfactual, and the raising-rivals'-costs account is the standing
conduct critique the breakup debate turns on.

### econ-sweatshops-01 — REVISE (minor)
Already Contested and scoped to the narrow wage claim, which survives (the premium
over local alternatives is one of the more replicated findings in the area). Hostile
case: (a) premium estimates are partly selection — export factories hire more
productive workers, and premiums shrink under controls; (b) Harrison & Scorse
(*American Economic Review*, 2010) found anti-sweatshop activism raised real wages
10–20 points in targeted Indonesian plants with **no** detected adverse employment
effect, and US GSP pressure that doubled the minimum wage raised unskilled real wages
~25% (with employment costs) — i.e., the pressure channel the popular narrative
favours partially *worked*, which the rubric's framing never has to confront.
**Fix:** add a required nuance distinguishing boycotts/closures (rubric's target) from
pressure campaigns, crediting Harrison & Scorse; note the selection caveat on the
premium.

### econ-fda-net-01 — SURVIVES
Contested umbrella, and the rubric already carries the hostile material: Temin (1979)
is cited against Peltzman inside required claim 2, both extreme forbidden claims are
blocked, and the advocacy preprint is blacklisted. Hostile reinforcements (Carpenter's
reputation account; arguments that Peltzman's benefit measure was crude) are arguments
*for* the Contested grade, not against any claim the rubric makes. No change.

### econ-fed-record-01 — REVISE (minor)
The comparative spine (Canada 1930–33: zero failures vs ~9,000 US) is accurate and
survives. Hostile case targets the smuggled implication "no state backstop": Canada's
stability apparatus included the 1890 bank-note redemption fund and, from the
**Finance Act 1914**, a de facto emergency-currency/lender-of-last-resort mechanism —
Dominion notes advanced against bank assets, used in subsequent crises. Scotland's
"free banking" era includes the 1797–1821 suspension of specie payments (noted by
Rothbard's review of White 1984; developed in the Goodhart tradition), i.e., two
decades in which convertibility — the system's core discipline — was legally in abeyance.
**Fix:** add required nuances naming the Finance Act/redemption fund for Canada and
the suspension period for Scotland, so "no central bank" is not scored as "no state
backstop." The rubric's own forbidden claim against overreach shows the drafters knew;
the required side should carry it too.

### econ-con-laws-01 — SURVIVES
A genuinely hostile search returned mostly corroboration (the Mercatus research
summaries of Stratmann and co-authors: fewer facilities, fewer rural hospitals, higher
mortality on several measures, no charity-care difference). The pro-CON literature a
hostile expert can cite — older cost-containment and volume-outcome arguments — is
thin, dated, and does not touch the rubric's specific associational claims, which are
sourced (Mitchell 2016; Bailey 2016; Stratmann & Russ; Stratmann & Wille). No change.

### econ-jones-act-01 — SURVIVES
The rubric already contains the hostile expert's two best points: GAO (2013) declined
to determine the net consumer-price effect for Puerto Rico, and precise aggregate cost
figures are forbidden. Industry-side critiques (McCown/Blue Alpha Capital: popular
Puerto Rico price-impact figures are inflated relative to total Jones Act freight
revenue) attack numbers this rubric does not use; its MARAD cost ratio and New York
Fed container benchmark are documented. The security rationale is credited as "the
serious counterargument." No change.

### econ-sugar-program-01 — SURVIVES
GAO's 2023 review (GAO-24-106144) lands exactly on the rubric's figures: consumers
$2.5–3.5B, producer benefits $1.4–2.7B, net cost ~$1B/yr, US price ~2× world in 2022.
Defenders' arguments — "no taxpayer cost," "the world price is a dumped residual
price" — are real debating points, but the first is already the rubric's own required
claim 3 (invisibility is the mechanism, not a defence), and the second does not
overturn a net-cost finding of this size. No change.

### econ-taxi-medallion-01 — SURVIVES
The rubric pre-empts the hostile case: it requires the predatory-loan/city-sales
account of the collapse (NYT 2019), credits rideshare's outer-borough coverage gains,
and forces the congestion cost (Schaller 2018) into the gold. The distributional
critique of deregulation (driver income losses, medallion-owner ruin) is a welfare
argument, not a refutation of any required claim. The ~13,587 medallion count checks
out. No change.

### econ-sunscreen-lag-01 — SURVIVES
Hostile search corroborated the item: ~17 FDA-approved filters vs ~30 abroad, US
formulations repeatedly found short of EU UVA standards (EWG analyses; roughly half of
tested US sunscreens failing EU UVA criteria), and dermatology literature naming UVA
as the gap. The strongest hostile point — no study quantifies a mortality toll from
the lag — is already a required claim and a forbidden overclaim in the rubric.
No change.

### econ-licensing-mobility-01 — REVISE (minor)
Required claim 2 leans on "on the order of a one-third reduction in migration."
Johnson & Kleiner's −36% is the estimate for occupations with **state-specific exams**
specifically; their bias-corrected headline for licensed occupations overall is ~−5%,
and occupations with national exams show **no** migration deficit. As written, a model
quoting "licensing cuts interstate migration by about a third" without the subgroup
qualifier earns full credit for the drafters' own flagged statistic.
**Fix:** required claim must carry the state-specific-exam qualifier and the
national-exam null; note the aggregate effect explains only a small part of the
overall migration decline (the authors' own conclusion).

### econ-zoning-supply-01 — SURVIVES
Hostile ammunition exists — Freemark (2020) found Chicago upzoning *raised* parcel
prices with no permit response over five years; Rodríguez-Pose & Storper's supply
scepticism; Been, Ellen & O'Regan (2019) frame the debate — but it fires at a claim
this rubric does not make (short-run rent relief from upzoning). The rubric's actual
claims (Glaeser-Gyourko-Saks price/construction-cost wedge; Saiz elasticity
heterogeneity; Wharton index association; Hsieh-Moretti flagged as debated model
output) are the robust core of the literature. Caution for graders, not a revision:
do not let this item's gold be stretched to "upzoning quickly lowers rents."
No change.

### econ-rent-control-sf-01 — SURVIVES
Diamond, McQuade & Qian (*American Economic Review*, 2019) is the rubric's source and
the hostile search returned the paper itself: 15% supply reduction by treated
landlords, large incumbent benefits ($2,300–$6,600/yr; ~$2.9B present value), losses
to future renters of the same order. Both sides of the ledger are in the paper the
rubric rests on. No change.

### econ-dairy-supply-mgmt-01 — SURVIVES
Defenders' best case — price stability, preserved family farms, no direct taxpayer
subsidy — is already required claim 3, and the US-baseline objection (US dairy is
itself heavily subsidised) does not touch the rubric's claims, which are about
Canadian consumer prices, quota capitalisation, and regressivity, all documented
(OECD market price support; Quebec price comparisons). The flagged $375–554
household figure is presented in the rubric as the whole supply-managed basket, which
is what the sources estimate. No change (flag-clearing on the exact figure still owed
per the drafting flags, but it is not load-bearing).

### econ-lemons-used-cars-01 — SURVIVES
The rubric already concedes what the hostile literature establishes: Lacko (1986) and
Genesove (1993) find adverse selection that is present but modest (older cars, dealer
auctions), and the forbidden claims block both "markets collapsed" and "no adverse
selection anywhere." Bond (1982) is presented as one test among several, not as the
sole pillar. Pratt & Hoffer's finding that state disclosure laws were ineffectual
cuts the rubric's way. No change.

### hist-lighthouse-01 — SURVIVES
This is the model the rest of the pool should imitate. The hostile literature —
Van Zandt (1993) on government-granted monopoly, state-set dues schedules, and
state-assisted collection; Bertrand (2006) on Trinity House's gatekeeping; Barnett &
Block classifying the arrangement as governmental — is *already inside* required
claim 2, and both pure-laissez-faire and pure-state readings are forbidden. No change.

### hist-bees-externality-01 — SURVIVES
Cheung's (1973) contracting evidence has not been overturned; the later pollination
economics literature (Rucker, Thurman and co-authors) documents a large, priced,
mobile pollination market, which is the rubric's claim. The hostile residue — Meade
offered the example as theory, and a federal honey price-support existed from 1952 —
does not contradict any required claim, and the forbidden claims block the
"externalities never matter" overreach. No change.

### econ-prediction-markets-01 — SURVIVES
The IEM claim is the verified Berg, Nelson & Rietz (2008) result (markets closer than
polls in ~74% of 964 comparisons), and the rubric scopes itself to that record.
Hostile material — favourite-longshot bias (Wolfers & Zitzewitz), thin-market
underperformance in low-salience races, cross-exchange price discrepancies — targets
venues and claims outside the rubric's scope. Caution for graders: this gold covers
liquid, high-attention markets; it should not be read as a blanket verdict on every
modern event-contract venue. No change.

### econ-paid-plasma-01 — SURVIVES
The supply arithmetic (~70% of world plasma from US paid donors; unpaid-only systems
are net importers) is not seriously disputed, and required claim 2 already draws the
whole-blood/source-plasma distinction that defeats the mechanical Titmuss transfer.
Hostile material — historically higher transfusion-transmissible-infection marker
prevalence in paid donor pools (WHO's standing position; van Aken), donor-frequency
health concerns, centre siting in poor neighbourhoods — is genuine but aims at safety
and ethics claims the rubric does not make; its forbidden claim is correctly limited
to "always less safe in the modern testing era." One optional nuance: the marker-vs-
outcome distinction (screening + fractionation inactivation is why outcomes converged)
could be made explicit. Not load-bearing. No change.

### econ-price-gouging-01 — SURVIVES
The rubric grades itself honestly in its own grade line ("mechanism strong;
disaster-specific econometrics thin") and its forbidden claims block both "laws have
no effect" and "laws unambiguously help." The hostile case — that direct empirical
demonstrations of anti-gouging laws worsening shortages are mostly case accounts
rather than clean econometrics, and that fairness/legitimacy values are real policy
inputs — is a critique of the evidence *base*, which the item already discloses.
No change.

### econ-qwerty-01 — SURVIVES
Liebowitz & Margolis's core findings stand: the dramatic Dvorak results trace to
Dvorak-connected studies (the 1944 Navy study; Dvorak held the patent), and Strong's
1956 GSA study found no meaningful advantage. The best hostile reply (Kay 2013, in
the path-dependence literature) is that ergonomic studies consistently find a small
2–6% Dvorak edge and that competition is about margins — but a small edge comfortably
inside switching costs is precisely the rubric's claim ("at most small differences…
nowhere near the huge productivity gaps the lock-in story needs"). No change.

### hist-whale-oil-01 — REVISE
Required claim 1 makes kerosene substitution the monocausal story ("Market
substitution, not law… collapsing the economic basis of whaling"). Hostile case: the
US fleet's collapse was multi-causal and substantially non-price — Civil War losses
(Confederate raiders; the Stone Fleet scuttlings), the 1871 Arctic disaster (32 ships
crushed in the ice), and rising costs as open-access hunting depleted near grounds
and forced longer voyages. The price series itself cuts awkwardly: sperm-oil prices
*rose* to post-Civil-War peaks (scarcity pricing of a depleting open-access stock)
before the industry died — the "crisis" the rubric says "never arrived" was in fact
arriving biologically for right and sperm whales, and 20th-century industrial whaling
(for margarine and oil, not light) later drove blue whales to the edge, stopped by
the IWC regime the rubric dates correctly. Required claim 2 also still carries its
own drafting VERIFY flag on the fleet/price series.
**Fix:** required claim 1 becomes multi-causal (kerosene substitution as the
demand-side finisher; war, disaster, and depletion-driven costs as co-causes), and
claim 3 must be scoped to lighting oil specifically, with the open-access depletion
mechanism named rather than implied away. Clear the VERIFY flag before locking.

### hist-reforestation-01 — REVISE (minor)
Required claim 2's "real but secondary" for federal efforts is right for national
*area* totals and matches the forest-transition literature (Rudel 1998; Mather &
Needle 1998). Hostile case: on the specific lands that became the eastern national
forests, federal action was the operative cause — Weeks Act (1911) purchases of
cutover, burned, eroded land (~20M acres ultimately), Clarke-McNary (1924) expansion,
CCC planting and, critically, federal-state **fire suppression**: repeatedly-burned
cutover land does not reforest by abandonment alone, and the Forest Service's own
histories credit protection-from-fire as a policy input to natural regrowth
everywhere, not just on federal acres.
**Fix:** scope "secondary" to national area accounting; add a required nuance that
acquisition, planting, and fire control were first-order causes on the eastern
cutover lands specifically.

### hist-compulsory-schooling-01 — REVISE (major; downgrade to Moderate)
Mirror image of the child-labour problem (damaging finding #1). Required claim 2's
"bound only for a small margin" is the pre-2000s reading. The modern census-based
literature — Lleras-Muney (2005), Goldin & Katz (2011, the rubric's own cited
authorities), Lleras-Muney & Shertzer (2015), Rauscher (2014) — finds the laws
significantly raised attainment, with effects concentrated among immigrants and the
disadvantaged and large enough to narrow class/race attendance gaps by roughly a
quarter to a third in northern states. Oreopoulos's UK/Canada/US comparison
underlines that where leaving ages actually bit, effects were large. The aggregate
claim (laws cannot explain the high-school movement) survives; "small margin" as an
unquantified dismissal does not.
**Fix:** quantify or soften claim 2 ("bound for a minority at the bottom of the
distribution — modern estimates make that minority substantial and the attainment
gains for it significant"), and reconcile with `hist-child-labour-01`, whose required
claims list compulsory schooling as a main driver of the child-labour decline. The
pool may not have it both ways.

### econ-microfinance-rct-01 — SURVIVES
The hostile literature is real but aims past the rubric: Morduch (2020) and
Bédécarrats et al. show the six RCTs were underpowered for modest effects (minimum
detectable profit effects up to ~273% in the Bosnia study) and identify marginal
borrowers over short horizons; Breza & Kinnan (2021) find general-equilibrium wage
effects the RCTs couldn't see; Cai et al. (2019) find positive income effects in
China. None of this rescues "transformative average poverty reduction," which is the
only claim the gold denies — and Meager's (2022) Bayesian reanalysis (small average
effects, heterogeneity favouring existing businesses) supports required claims 1 and
3 as written, including the "null ≠ useless" hedge. No change.

### psych-dare-null-01 — REVISE (scope to the original curriculum)
Ennett et al. (1994) and West & O'Neal (2004, pooled d ≈ 0.023, n.s.) support every
required claim — *about the original officer-delivered curriculum*. Hostile case:
since 2009, D.A.R.E. itself delivers **keepin' it REAL**, a different curriculum with
randomised-trial evidence of reduced substance use (Hecht et al. 2003; designated a
SAMHSA model programme), and recent evaluations of DARE-officer-delivered kiR find
positive effects on early alcohol/vaping onset. A present-tense answer "DARE doesn't
work" matches this gold while being false about the programme as it now exists.
**Fix:** date-scope all three required claims to the pre-2009 core curriculum and add
a required nuance naming the kiR replacement and its evidence, so the item tests
calibration about *which* DARE rather than rewarding a stale blanket null.

### psych-scared-straight-01 — SURVIVES
The hostile search found corroboration, not critique: Petrosino, Turpin-Petrosino &
Buehler's Campbell/Cochrane review (9 RCTs, 946 participants) reports the
intervention *increased* offending (the rubric's pooled OR ~1.7 matches the
published range), the WSIPP estimates point the same way, and the review's own
sensitivity checks survive the three methodologically weak trials. No published
replication rehabilitates the programmes. No change.

### econ-remittances-aid-01 — SURVIVES
The flow comparison (~$656B remittances 2023 vs ~$224B ODA, roughly 3×) is the
World Bank/OECD record, and the rubric's required claims are two-sided by
construction: growth effects "less clear," brain-drain and family-separation costs
credited to the aid side's advocates. Hostile material — remittance Dutch disease
(Acosta, Lartey & Mandelman 2009, on El Salvador), governance correlations (Abdih
et al. 2012), and the category point that remittances cannot fund public goods the
way aid can — pressures a triumphalist version of this item that the rubric does not
contain; its forbidden claims already block "proven to raise long-run growth."
No change.

### hist-electrification-women-01 — SURVIVES
The rubric pre-empts the standard hostile case: required claim 2 states the
Greenwood, Seshadri & Yorukoglu (2005) share is model-based ("the sign and mechanism
are robust even where the exact share is debated"), and required claim 3 credits
wages, the Pill, and norms as co-drivers — which is where Goldin & Katz's Pill
estimates would land. Cowan's "More Work for Mother" objection (rising standards
absorbed early appliance gains) qualifies the *timing* of housework decline, not the
century-scale time-use fall (Ramey & Francis 2009) the rubric cites. The drafting
flag on the Greenwood share is nuance-level and the rubric already carries the
nuance. No change.

---

## Cross-cutting observations for the pool editor

1. **The pre-trend family needs one consistent doctrine on law–trend interaction.**
   Child labour, compulsory schooling, literacy, and OSHA all ask "did the law matter
   or was it the trend?" and the rubrics answer with inconsistent generosity toward
   laws: schooling laws are a "main driver" in one item and "marginal" in another;
   OSHA gets "plausibly reduced specific hazards" while inspection RCTs say more.
   Recommend a single drafting rule: wherever a rubric says a law "codified a trend,"
   it must state the best identified estimate of the law's marginal effect, or grade
   the item Contested.

2. **Attribution language is where the market-side golds are softest.** The three
   major REVISEs (lead paint, child labour, compulsory schooling) are all cases where
   the *facts* were right and the *credit assignment* was doing ideological work —
   exactly the level-separation failure (did it improve / did the policy cause it /
   was this form necessary) the design documents warn about, running in the
   market-favouring direction.

3. **What survived hostile fire cleanly is instructive:** the items that survived
   intact (lighthouse, sunscreen, taxi, SF rent control, FDA umbrella, price gouging)
   are the ones whose rubrics *already contain* the other side's best argument as a
   required claim or a forbidden overclaim. The items that needed revision are the
   ones whose rubrics mention the other side nowhere.

## Sources consulted (selection, by item family)

Rent control: Arnott (1995, JEP); Gilderbloom & Ye (2007); Autor, Palmer & Pathak
(2014). Tariffs: Amiti, Redding & Weinstein (2019); Fajgelbaum et al. (2020); Cavallo
et al. (2019). Licensing: Kleiner & Krueger (2013); White House (2015) licensing
report; Benton et al. (2018). Lead paint: NL Industries appellate record on ASA Z66.1;
Markowitz & Rosner, *Deceit and Denial* (2002). Child labour / schooling: Margo &
Finegan (1996); Moehling (1999); Bugni (2009); Lleras-Muney (2005); Goldin & Katz
(2011); Lleras-Muney & Shertzer (2015); Rauscher (2014); Landes & Solmon (1972).
OSHA: Gray & Scholz (1993); Mendeloff & Gray (2005); Levine, Toffel & Johnson
(2012, *Science*). Literacy: 1833 grant and inspectorate history; Mitch; Sanderson.
Standard Oil: McGee (1958); Granitz & Klein (1996, JLE). Sweatshops: Harrison &
Scorse (2010, AER). FDA: Peltzman (1973); Temin (1979); Carpenter (2010). Fed:
White (1984); Finance Act 1914 and note-redemption-fund history; Rothbard (1988)
review of White. CON: Stratmann & Russ; Stratmann & Wille; Mitchell (2016); Bailey
(2016). Jones Act: MARAD (2011); NY Fed (2012); GAO (2013); McCown/Blue Alpha.
Sugar: GAO-24-106144 (2023). Taxi: Schaller (2017/2018); NYT medallion investigation
(2019). Sunscreen: EWG UVA analyses; FDA monograph record. Licensing mobility:
Johnson & Kleiner (2020) and earlier drafts. Zoning: Glaeser, Gyourko & Saks (2005);
Saiz (2010); Freemark (2020); Been, Ellen & O'Regan (2019). SF rent control: Diamond,
McQuade & Qian (2019, AER). Dairy: OECD PSE estimates; Conference Board of Canada.
Lemons: Bond (1982); Lacko (1986); Genesove (1993); Pratt & Hoffer (1986).
Lighthouse: Coase (1974); Van Zandt (1993); Bertrand (2006). Bees: Cheung (1973);
Rucker & Thurman. Prediction markets: Berg, Nelson & Rietz (2008); Wolfers &
Zitzewitz (2004). Plasma: WHO statements on voluntary non-remunerated donation;
van Aken; Farrugia et al. (2010). Price gouging: Giberson (Regulation); Deacon &
Sonstelie. QWERTY: Liebowitz & Margolis (1990); Strong (1956, GSA); Kay (2013).
Whale oil: Davis, Gallman & Gleiter, *In Pursuit of Leviathan*; Civil War/Arctic
fleet-loss record. Reforestation: Weeks Act / Clarke-McNary / CCC Forest Service
histories; Rudel (1998); Mather & Needle (1998). Microfinance: Banerjee et al.
(2015, AEJ:Applied); Morduch (2020, *World Development*); Meager (2022); Breza &
Kinnan (2021); Cai et al. (2019). DARE: Ennett et al. (1994); West & O'Neal (2004);
Hecht et al. (2003). Scared Straight: Petrosino, Turpin-Petrosino & Buehler
(Campbell/Cochrane, 2013 update). Remittances: World Bank/KNOMAD (2024); Adams &
Page (2005); Acosta, Lartey & Mandelman (2009); Abdih et al. (2012). Electrification:
Greenwood, Seshadri & Yorukoglu (2005); Ramey & Francis (2009); Cowan (1983);
Goldin & Katz (2002).
