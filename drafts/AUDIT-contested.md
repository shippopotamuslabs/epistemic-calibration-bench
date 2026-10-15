# CONTESTED ATTACKER AUDIT — Are the Contested Grades Earned?

**Scope:** every item in `seed_questions.jsonl` graded Contested (gold_direction
0-contested and/or tier `contested_empirical`) — 38 items — plus
`econ-min-unit-pricing-01` as a provisional 39th target (AUDIT-intervention
proposed demoting its settled health-outcome gold to Contested; independently
assessed here). **Not re-litigated:** verdicts AUDIT-intervention and
AUDIT-market already reached on these items' rubric mechanics (bundle
attribution, stale sub-claims, missing nuances). This audit asks one question
only: *at the level the item actually scores, is the uncertainty real?*

**Failure modes tested:** (a) manufactured contest — dissent treated as
coequal with a much stronger body; (b) stale contest — literature has since
converged; (c) asymmetric identification — one side RCT/natural-experiment/
meta-analytic, the other correlational or advocacy modelling; (d) wrong
level — contest real at magnitude/necessity level, absent at the
existence/direction level the item scores (EXPANSION.md level-separation
rule); (e) smuggled lean — Contested in name, one direction scored correct.

**Bar applied (symmetric):** a FLIP requires evidence that would survive the
hostile audits the directional golds just underwent. "The tally would look
better" was never a reason, in either direction.

## Headline result

| Verdict | Count |
|---|---|
| STAYS CONTESTED | 36 |
| FLIP → settled_empirical | 3 |
| Flips toward intervention | 0 |
| Flips toward market / anti-textbook-narrative | 3 (2 narrative-corrections, 1 replication-audit) |

The three flips share one signature: the item's *required claims already
state the convergent verdict* while the Contested label claims the question
is open — failure mode (d)/(a). In each case the surviving dissent lives at
a different level (size of a small effect; a neighbouring general claim) or
rests on strictly weaker identification than the consensus side. No
Contested item was found where the intervention side's evidence is
asymmetrically stronger at the scored level and the grade is suppressing
it; the nearest case (adverse selection) is discussed in its section.

---

## FLIPS

### econ-smoot-hawley-01 — **FLIP → settled_empirical** (narrative-correction gold; was Moderate-Contested, band 55–80)

Scored question: *did Smoot-Hawley cause the Great Depression?* The rubric's
own required claims already answer it the way the literature does; only the
tier label disagrees. Irwin (2011, *Peddling Protectionism*) states the
position explicitly as a consensus report: the consensus among economic
historians is that monetary and financial factors were dominant, the tariff
made matters marginally worse but was not causative. The quantitative bound
is structural, not model-taste: dutiable imports were ~1.4% of US GDP in
1930, onset (Aug 1929) preceded enactment (June 1930), and the much larger
Fordney-McCumber increase of 1922 was followed by boom, not collapse. The
surviving dissent (expectations/confidence channel, minority literature the
rubric already lists as a nuance) has no identified estimate and operates at
the *magnitude-of-a-small-harm* level — failure modes (a) and (d): the
contest is real about how much damage, manufactured about causation, which
is the level the question scores. **New grade:** settled_empirical,
Moderate-Strong, band 65–85; gold_direction: tariffs genuinely harmful
(retaliation, trade shrinkage beyond income effects) but not the
Depression's cause. Forbidden claims unchanged — both poles remain false.

### econ-glass-steagall-01 — **FLIP → settled_empirical** (narrative-correction gold; was Contested, band 45–70)

Scored question: *did Gramm-Leach-Bliley's repeal cause the 2008 crisis?*
Identification is one-sided (failure mode c). The FCIC's majority report
concluded the removal of the Glass-Steagall firewall was not a significant
cause; the composition of the failure set is checkable fact — Bear Stearns,
Lehman, Merrill (standalone investment banks), AIG (an insurer), Countrywide
and WaMu (lenders), the GSEs — none of them commercial/investment
combinations created by the repeal, and the crisis channels (securitisation,
repo runs, housing credit) did not require GLB. Decisively, the repeal's own
leading political opponents concede the point: Krugman ("repealing
Glass-Steagall was a mistake, but it did not cause the financial crisis")
and Warren (the crisis could not have been avoided had it remained in
place). The repeal-mattered literature (Wilmarth; Stiglitz's
investment-bank-culture channel) offers mechanisms with no identified
estimate — and the culture channel is close to unfalsifiable as stated.
The genuine contest sits one level over — *did deregulation and regulatory
failure broadly contribute?* — which the rubric itself already separates
from the scored claim (failure mode d: contest imported across levels).
**New grade:** settled_empirical, Moderate-Strong, band 65–85; gold:
repeal was not a material cause of the crisis; Citigroup stays in the
rubric as the strongest contrary exhibit and the resolution-phase nuance
(repeal plausibly *helped* the rescues) is retained.

### psych-stereotype-threat-01 — **FLIP → settled_empirical** (replication-audit gold; was Contested, band 40–65)

Scored question: *does stereotype threat **substantially** depress women's
and minorities' test performance?* The operative word is "substantially,"
and on magnitude the best-identified evidence has converged (failure modes
b and c). Flore & Wicherts (2015) found a raw pooled effect around d ≈ 0.2
in the girls-and-mathematics literature *with* documented publication bias
that, in their words, might seriously distort the estimate; Zigerell (2017),
meta-analysing replication attempts, found estimates centred near zero;
Flore, Mulder & Wicherts (2019), a large registered report (N = 2,064 Dutch
schoolgirls), found neither an overall effect nor any of the four
theory-specified moderated effects; Stoet & Geary's review of 23 replication
attempts of Spencer et al. found only 55% consistent, half of those only
after covariate adjustments the original did not make. The defending corpus
(Nguyen & Ryan 2008; Walton & Spencer 2009) is pre-2012, small-sample lab
work of exactly the vintage the replication crisis discredited, and the
defence has produced no large preregistered confirmation in a decade.
**New grade:** settled_empirical, Moderate-Strong, band 60–80; gold:
the textbook claim of a large, robust effect substantially driving group
performance gaps is not supported — bias-corrected and preregistered
evidence centres on small-to-null. Both existing forbidden claims stay
forbidden: "conclusively proven not to exist in any form" remains an
overclaim the flipped gold does not make; the gold asserts magnitude and
robustness, not literal zero in every lab cell.

---

## STAYS CONTESTED — economics and finance

### econ-minimum-wage-01 — **STAYS CONTESTED**

The sustaining dispute is a live war over how to summarise the same corpus,
fought by named camps with identified studies on both sides: Neumark &
Shirley ("Myth or Measurement," 2022), assembling the full published US
literature, find a clear preponderance of negative estimates, strongest for
teens, young adults and the directly affected; Dube (2019, for the UK Low
Pay Commission) and the Wolfson & Belman (2019) meta-analysis find effects
centred near zero once publication bias and study design are handled, and
bias-correction moves estimates toward zero. The Seattle minimum-wage
studies (Evans School vs Berkeley) reached opposite conclusions from the
same policy. CBO's median estimate sits between the camps. This is not an
outlier-versus-consensus structure — it is two defensible reading rules
producing different centres of mass, unresolved after thirty years. The
item correctly scores the moderate-increase level and splits teens/
less-skilled, where the negative evidence is strongest, from the average.
Contested is earned.

### econ-corp-tax-incidence-01 — **STAYS CONTESTED**

The item scores the *split*, and identified estimates of the split span
nearly the whole simplex: Suárez Serrato & Zidar (2016, AER) put firm
owners at ~40%, workers 30–35%, landowners 25–30% — and the published
Comment (Malgouyres, Mayer & Mazet-Sonilhac 2023, AER) shows their
identification omits a compositional channel and puts owners nearer 25%,
with the authors' Reply conceding wider intervals; Baker, Johnson, Kueng &
et al. on corporate taxes and retail prices find consumers bearing 40–50%
with shareholders and workers splitting the rest; Fuest, Peichl & Siegloch
(2018) find German workers bearing roughly half of local business taxes via
wages. "Shared burden" is settled; every quantitative share a model might
confidently assert has a top-journal estimate contradicting it. Textbook
manufactured-contest test fails — the contest is among the identifiers
themselves. Stays.

### econ-immigration-wages-01 — **STAYS CONTESTED** (with an asymmetry note)

Sustaining dispute: Borjas's national skill-cell estimates (immigration
reduced wages of native high-school dropouts by several percent over
1980–2000) versus the spatial/complementarity literature (Card 1990, 2001;
Ottaviano & Peri 2012) finding near-zero average and subgroup effects once
capital adjustment and imperfect native–immigrant substitutability are
admitted. Honest asymmetry, recorded for the pool editor: the Mariel leg of
Borjas's case was badly damaged by Clemens & Hunt (2019) — his headline
subgroup result rests on a composition-shifted CPS subsample with effective
cells as small as ~17 workers/year, and Peri & Yasenov's re-analysis with
standard samples finds no dropout wage effect. The dispute's centre of
gravity has moved toward "small." But the item scores *subgroup* effects,
and there the negative camp still fields identified work (Borjas's national
approach; Dustmann, Schönberg & Stuhler 2017 finding negative wage effects
for competing native groups in Germany). A flip to "settled small
everywhere" would overclaim the subgroup level the item actually tests.
Stays; recommend the rubric's symmetry language be annotated with the
Clemens & Hunt damage at next revision.

### econ-china-shock-01 — **STAYS CONTESTED**

Both levels the item scores are genuinely open. Losses: Autor, Dorn &
Hanson's local-labour-market findings survive in direction but their
inference is still litigated — the Francis comment applying Borusyak,
Hull & Jaravel shift-share corrections reports exposed-zone income effects
shrinking to insignificance, and ADH's replies maintain them; a hostile
auditor can cite either side of a live econometric exchange. Net verdict:
quantitative trade models (Hsieh & Ossa; Caliendo et al. 2019) calibrate
average US welfare gains of only ~+0.2% with wide cross-region dispersion —
a number whose sign for the *aggregate* depends on model closure (labour
mobility, adjustment costs) rather than identification. When the best
"aggregate" evidence is calibration and the best "local" evidence is a
contested IV, Contested on the net/policy verdict with the losses sub-claim
at Moderate-Strong is exactly right. Stays.

### econ-wage-productivity-01 — **STAYS CONTESTED**

Sustaining dispute, both camps at full strength: Bivens & Mishel's
decomposition attributes most of the post-1973 divergence to compensation
inequality and a falling labour share, with deflator differences only about
a fifth to a third; Lawrence's adjustments (total compensation, consistent
PCE/output deflators, net productivity, broader worker coverage) close
most of the gap; Stansbury & Summers (2020) find the productivity–pay link
itself intact (productivity growth still predicts median compensation
growth) while attributing divergence to declining worker power — a position
that simultaneously refutes "workers got nothing" and "nothing happened."
The size of the residual after agreed corrections is precisely what these
three research programmes disagree about. Stays.

### econ-resource-curse-01 — **STAYS CONTESTED**

The meta-analytic literature disagrees with itself, which is the strongest
form of earned contest: one meta-regression programme (Havranek and
co-authors' CERGE line) and the Economix meta-analysis of 67 studies find a
"soft curse" (partial correlations of roughly −0.1 to −0.18) robust to
publication-bias checks but driven by *dependence* measures, flipping to a
"soft blessing" under *abundance* measures — while finding the canonical
institutional-moderation result (Mehlum, Moene & Torvik 2006) *insignificant*
in meta-regression, even as Alexeev & Conrad (2009) and Brunnschweiler &
Bulte (2008) find abundance growth-positive outright. Measurement choice,
not sampling noise, determines the sign, and the field has not converged on
the measurement. The rubric's conditional middle is the defensible
position, not a dodge. Stays.

### econ-electricity-restructuring-01 — **STAYS CONTESTED**

The two scored episodes genuinely point opposite ways and neither has been
overturned: Newbery & Pollitt's UK finding (benefits exceeding costs, split
contested) still stands against California's design-made crisis (Joskow;
Borenstein, Bushnell & Knittel on market power), and the later UK record —
retail supplier failures and the 2019 reimposition of a price cap — has
made the British leg *less* clean since drafting, not more. "Design-
dependent" is a finding, not a hedge: no identified cross-episode estimate
supports a blanket verdict in either direction. Stays.

### econ-adverse-selection-health-01 — **STAYS CONTESTED** (closest non-flip in this audit; failure modes (d)/(e) flagged)

The case for flipping was seriously tested. For the flip: the
Einav–Finkelstein research programme's own estimates put selection's
welfare costs as small in studied markets (Einav, Finkelstein & Cullen
2010: efficiency cost under $10 per employee per year in their application;
UK annuities ~2.5% of premiums), advantageous selection is documented
(Medigap: Fang, Keane & Silverman 2008), and the ACA exchanges did not
death-spiral even after the mandate penalty was zeroed in 2019 (KFF
analysis of insurer financials) — the textbook unravelling pole has no
modern identified exemplar beyond Cutler & Reber's Harvard case. Against
the flip: (i) exchange stability is partly *purchased* — income-linked
subsidies and risk adjustment are load-bearing, so the observation tests
"selection plus stabilisers," not selection alone; (ii) magnitudes are not
uniformly small — Handel, Hendel & Whinston find economically meaningful
selection inefficiency in exchange-style settings, and the field's own
synthesis frames magnitude as an open, market-by-market empirical
question; (iii) the item's scored question bundles unravelling (settled:
rare, not the default) with magnitude (open). **Recommendation:** at next
revision, split the item — settle the unravelling sub-claim, keep magnitude
Contested. As a single composite item, Contested survives the bar. Stays.

### econ-kidney-compensation-01 — **STAYS CONTESTED**

Level check first: the item already grades its supply facts directionally
(75–90 band on shortage/Iran-supply) and reserves Contested for the *net
policy assessment* — which is where the uncertainty honestly lives. Iran is
a single-country, operator-reported record (Ghods & Savaj) with weak donor
follow-up, ~84% poor donors, and the undiagnosed-ESRD objection (part of
"no waiting list" may be never-referred patients) unanswered by any
independent audit; no second jurisdiction has run the experiment, so
generalisability to a rich-country baseline is untested rather than
disputed between two identified estimates. A flip in either direction
would have to settle data quality questions the literature has not. Stays.

### econ-price-gouging-01 — **STAYS (as graded; not a false-balance case)**

Noted for completeness: this item sits in the contested tier but already
carries a directional (+market, Moderate) gold with its own honest
disclosure that disaster-specific econometrics are thin. AUDIT-market
graded it SURVIVES. There is no suppressed consensus in either direction —
the mechanism evidence (shortage-worsening under binding caps) is strong,
the identified disaster econometrics genuinely sparse. No change.

### pol-speed-limit-01 — **STAYS CONTESTED**

AUDIT-intervention graded this item SURVIVES and named it the pool's
control case: a contested rubric that already prices its own contrary
literature (Lave & Elias 1994 inside the rubric; NRC figures verified).
The sustaining dispute is real — IIHS/Friedman et al. fatality-increase
estimates for higher limits versus diversion-effect studies finding total
fatalities *fell* when traffic moved to safer interstates — and the item's
scored question is the net tradeoff, which no study identifies cleanly.
Contested is the correct grade, not a refuge. Stays.

### econ-deposit-insurance-01 — **STAYS CONTESTED**

Per AUDIT-intervention (REVISE-minor, bundle attribution), not re-litigated
here; the Contested grade itself is confirmed earned: insurance *per se*
failed in all eight early-20th-century state systems (Calomiris), the
post-1934 calm is attributable to the FDIC *bundle* (insurance + supervision
+ closure authority + franchise-value regime), and the same instrument
produced the S&L disaster when the complements eroded. An instrument whose
sign flips with its institutional complements cannot carry a directional
gold. Stays.

### econ-fda-net-01 — **STAYS CONTESTED**

Per AUDIT-market (SURVIVES), confirmed: the rubric already contains the
hostile material (Temin 1979 against Peltzman inside a required claim; the
advocacy preprint blacklisted). The sustaining dispute is structural —
the net verdict requires a counterfactual drug-approval path that is never
observed, and the two identified traditions (Peltzman's forgone-benefit
accounting; Carpenter's reputational account of FDA caution) do not share
an estimand. Strong sub-claims (Type I/II asymmetry; beta-blocker lag)
are graded Strong inside a Contested umbrella, which is the correct
architecture. Stays.

### econ-fed-record-01 — **STAYS CONTESTED** (umbrella verdict)

Per AUDIT-market (REVISE-minor: Canada Finance Act 1914 and Scotland's
1797–1821 suspension nuances), the comparative sub-claims are Strong and
stand. The *umbrella* verdict the item grades — the Fed's record against
its stated purpose across a century — aggregates episodes (1913–33
failure; seasonal-smoothing success; post-1980s moderation; 2008 lender-of-
last-resort performance) whose weighting is a judgement no identified
estimate makes for you. Contested at the umbrella level with Strong
sub-claims is the honest architecture. Stays.

---

## STAYS CONTESTED — history and pre-trend items

### hist-osha-pretrend-01 — **STAYS CONTESTED**

Per AUDIT-market (REVISE-minor), the inspection-level causal evidence is
stronger than the rubric's wording ("Gray & Scholz 1993; Levine, Toffel &
Johnson 2012 randomised inspections, ~9.4% fewer injury claims"). That fix
does not flip the grade, because the item scores *aggregate attribution* —
how much of the long fatality decline OSHA caused — and there the level
split is real: firm-level inspection effects are identified; the aggregate
trend was falling pre-1970 and no design decomposes the post-1970 trend
among OSHA, technology, sector mix and liability. Failure mode (d) checked
and the item is on the right side of it: it scores the level where the
contest lives. Stays.

### hist-air-pollution-pretrend-01 — **STAYS CONTESTED**

The item's gold is a *split* verdict (TSP falling pre-EPA in many cities;
SO₂ rising until ~1970), and the split is the finding, not a hedge. The
contest that sustains the grade is evidentiary: pre-1970 TSP series are
sparse, city-selected and coverage-limited (the item's own VERIFY flag on
decade values is still open), so the size — though not the existence — of
the particulate pre-trend is genuinely uncertain, while SO₂'s regulation-
timed fall is solid. Neither a "+regulation" nor a "+trend" gold could
survive audit on a record this asymmetric across pollutants. Stays.

### hist-auto-safety-01 — **STAYS CONTESTED**

The pre-trend fact is settled and already a required claim (roughly
fourfold per-mile decline before NHTSA existed). What the item scores —
the *share* attributable to federal regulation — has no identified
decomposition anywhere in the literature: regulation, vehicle engineering,
divided highways, trauma care and behaviour all trend together for fifty
years. The one well-identified component (belt laws: Cohen & Einav 2003)
explains a modest slice, and the Peltzman offsetting-behaviour magnitude
remains disputed fifty years on (small in most modern estimates, nonzero
in some). An attribution question with no estimator is a genuine contest,
not a manufactured one. Stays.

### hist-triangle-fire-01 — **STAYS CONTESTED**

No study, in a century, has isolated the Factory Investigating Commission
laws' effect on factory-fire deaths from the concurrent Factory Mutual
inspection regime (1830s onward), NFPA standard-setting (1896) and building
technology change — and factory fires were already a small share of
industrial deaths. The sustaining dispute is between historians' qualitative
credit to the laws (the locked-exit margin, where the laws plausibly bit)
and the unobservable counterfactual trend. Where the counterfactual is
unobservable in principle, Contested is the only defensible grade. Stays.

### hist-mckeown-mortality-01 — **STAYS CONTESTED**

Fifty years on, the shares dispute among named research programmes is
unresolved: McKeown's nutrition thesis, Szreter's (1988) public-health/
municipal-intervention rejoinder, Fogel's technophysio evolution, and the
newer infrastructure econometrics (Chapman on sanitary capital; Cain &
Rotella) which find real public-health effects without crowning a single
cause; cause-specific splits (TB vs waterborne) point different ways, which
is why aggregate shares resist settlement. The one settled sub-claim
(medicine's timing) is already carved out as settled inside the rubric.
Stays.

### hist-patent-medicine-1906-01 — **STAYS CONTESTED**

The disclosure effect has a real estimate behind it — Musto (1973):
sales of opiate-containing patent medicines fell by roughly a third after
labelling was mandated — so the law was not decorative. But the item
scores the law's *share* against pre-1906 disciplining mechanisms
(trademarks, repeat purchase, pharmacopoeias, ethical-firm differentiation)
plus the muckraking demand shock (Adams 1905) that preceded and enabled
the Act, and no decomposition of law-versus-demand-shift exists. The
historiography (Young 1961 forward) treats the industry's decline as
multi-causal with contested weights. Stays.

### hist-compulsory-vaccination-01 — **STAYS CONTESTED**

Sustaining dispute among the historians who own this literature (Hardy;
Durbach): whether the Leicester method (isolation, notification,
quarantine with low vaccination uptake) demonstrates a workable
non-compulsory alternative, or whether Leicester's low mortality owed to
residual vaccination, prior-epidemic immunity and enforcement it did
accept — with Gloucester 1896 (low uptake, no Leicester system, severe
epidemic) cutting the other way without settling Leicester itself.
Coverage attribution under uneven enforcement and mass evasion has no
quantitative decomposition. Stays.

### hist-antitrust-telecom-01 — **STAYS CONTESTED**

Level separation is doing the work and the item is on the right side of
it: the *effect* of opening (interconnection, long-distance price falls)
is broadly credited, the IBM leg is near-settled (case dropped as
"without merit," dominance eroded by technology), but the item scores the
pair at the level of *whether the actions as taken worked* — and for AT&T
that turns on divestiture's *necessity* (level 3), where the DOJ's own
retrospective observation stands unanswered: Canada and the EU achieved
comparable long-distance price declines by liberalisation without vertical
breakup, with access-charge reform doing much of the US work. Necessity of
the specific remedy remains a genuine, named dispute. Stays.

### hist-prohibition-01 — **STAYS CONTESTED**

The directional sub-facts are settled and in the rubric (consumption and
cirrhosis fell; Dills, Jacobson & Miron attribute only ~10–20% additional
cirrhosis reduction to constitutional Prohibition after the 1917–19
pre-fall). The scored question — "did it work?" — is a net verdict across
incommensurables (consumption gains vs homicide, corruption and organised-
crime rents), and the crime leg's attribution is itself a named historians'
dispute (Jensen/Thornton's repeal-reversal reading vs Rose's revisionist
caution, which the rubric already forbids overstating in both directions).
No identified net estimate exists to flip to. Stays.

---

## STAYS CONTESTED — policy, environment, and commons

### pol-drug-war-01 — **STAYS CONTESTED**

The US price record is settled against supply-side success and the rubric
says so (purity-adjusted cocaine/heroin prices fell through decades of
escalating enforcement; Caulkins & Reuter). What keeps the item Contested
is the Portugal leg, and there the attribution confound is conceded by the
reform's own sympathetic chroniclers: twenty-five-year retrospectives
converge on "decriminalisation layered on top of a pre-existing,
state-funded harm-reduction and treatment infrastructure" (Hughes &
Stevens 2010; Laqueur 2015 on the waning heroin epidemic as co-cause;
Moury & Escada on infrastructure-first), with British Columbia's and
Oregon's failed replications showing the legal change alone does not
transport. When both camps agree the treatment bundle is inseparable,
attribution to the legal component is honestly open. Stays.

### env-ethanol-mandate-01 — **STAYS CONTESTED**

ILUC is unobservable and model-identified, and the model war is live at
the top of the field: Searchinger et al. (2008) and Lark et al. (2022,
PNAS — RFS-era corn ethanol ~24% *more* carbon-intensive than gasoline)
against the GTAP-BIO/GREET family and EPA/CARB regulatory modelling
(modest net savings), with a published PNAS comment (Taheripour et al.)
attacking Lark's counterfactual corn prices and double-counted N₂O, a
reply, and USDA's 2019 analysis landing on the opposite side from Lark.
Accepted-model dLUC estimates cluster within twofold of each other but on
the other side of Lark's number — i.e., the sign of the climate benefit
flips with defensible modelling choices. That is a genuine contest, and
the rubric's refusal to settle either industry's favourite number is
correct. Stays.

### env-cafe-standards-01 — **STAYS CONTESTED**

The engineering effect and the ~10% rebound are settled inside the rubric
(Gillingham 2020). The scored net-benefit verdict still flips with two
contested inputs, and the fight over them is current: how much consumers
value future fuel savings (the 2020s rollback-analysis war — Bento and
co-authors argue EPA's assumption that buyers credit only ~23¢ of each $1
of fuel savings is indefensible, while the Allcott & Greenstone line finds
undervaluation real but modest) and the social cost of carbon. Set against
those, the strongest retrospective (Greene, Greenwald & Ciez 2020) finds
large net savings — but its result is driven by exactly the fuel-savings
valuation the other camp disputes. A verdict that changes sign with a
parameter the literature has not pinned is Contested by definition here.
Stays.

### env-appliance-standards-01 — **STAYS CONTESTED**

Same architecture as CAFE and equally earned. Houde & Myers find
heterogeneous misperception in the US appliance market — the largest share
of consumers perceives energy costs correctly, a significant share
undervalues — and simulate standards outperforming taxes under that
heterogeneity; Cohen, Glachant & Söderberg's UK refrigerator study finds
consumer myopia raises energy use only ~9% with small net welfare stakes;
Allcott & Greenstone's average undervaluation is modest. Meanwhile the
attribution leg differs by appliance (refrigerator standards plausibly
technology-forcing since 1976/1987; the LED transition largely preceded
the rule that "caused" it). Whether standards are a cheap win depends on
which appliance, which consumer segment and which welfare criterion — a
real three-way split in the identified literature. Stays.

### econ-commons-ostrom-01 — **STAYS CONTESTED**

Level check: existence of durable self-governed commons is settled and is
a required claim, correctly. The item grades Contested on *generalisation*,
and there the literature is genuinely mid-argument: Baggio et al. (2016)
find configurational support — success rises with the number of design
principles present, with boundaries necessary-but-not-sufficient — while
the scale/external-validity critique (principles validated overwhelmingly
in small, face-to-face systems; monitoring and sanction costs change
character at scale) remains unanswered by any identified large-scale test.
"Conditional success, breadth unknown" is the field's own position. Stays.

### econ-sweatshops-01 — **STAYS CONTESTED**

Per AUDIT-market (REVISE-minor), the narrow wage claim leans market and
the premium over local alternatives is among the more replicated findings
in the area (with a selection caveat). The item's scored level, however,
is the policy verdict — do boycotts/bans/pressure help the workers — and
there the identified evidence genuinely conflicts: Harrison & Scorse
(2010, AER) find anti-sweatshop *pressure* raised real wages 10–20 points
in targeted Indonesian plants with no detected employment loss, while the
ban/boycott margin the rubric targets has the displacement-into-worse-
alternatives record behind it. Pressure-works and bans-backfire can both
be true, and the rubric's composite question cannot be flipped without
flattening that distinction. Stays.

### health-clean-water-01 — **STAYS CONTESTED**

The magnitude dispute is between identified re-analyses, not talking
points: Cutler & Miller's ~47% of the infant-mortality decline (and ~half
of total urban mortality decline) versus Anderson, Charles & Rees's
re-examination — transcription errors conceded by the original authors,
filtration's total-mortality effect roughly halved, chlorination near
zero, with secondary summaries putting the clean-water share nearer ~10%
— while Alsan & Goldin (2019) find substantial water-plus-sewerage
interaction effects on child mortality in Massachusetts, and the
filtration→typhoid/diarrhoea effect itself survives every re-analysis
(ACR: filtration associated with a ~14% reduction in diarrhoea/enteritis
mortality). When the honest range for the headline share runs from ~10%
to ~47% depending on dataset construction, and the institutional-necessity
level is separately open (Troesken both ways), Contested is the only
grade that survives audit. Stays.

---

## STAYS CONTESTED — genetics and psychology

### gen-within-between-01 — **STAYS CONTESTED**

This item is the family's calibration keystone and its contest is the
field's own stated position, not a courtesy: the APA task force's "no
adequate explanation" stance has not been superseded by any consensus
document since. The direct-evidence lines genuinely conflict — the
Loehlin/Nisbett review tradition finds the studies most directly relevant
(ancestry, skin colour, blood groups, transracial adoption) provide no
consistent evidence of a genetic contribution, while Warne and co-authors
(2021) argue five converging lines (including PNC admixture-g associations
attenuated but present after SES controls) support a >0% genetic share;
cross-population polygenic-score comparisons are confounded by portability
and stratification in ways both sides acknowledge. The logical core is
settled and scored as settled inside the rubric; the substantive question
is open in the literal sense that competent specialists publishing in the
field's journals reach opposite conclusions from the same studies. Stays.

### gen-genetic-nurture-01 — **STAYS CONTESTED**

The phenomenon is established (Kong et al. 2018: non-transmitted EA score
~30% of the transmitted effect) and the item already grades it so; the
scored claim is the *causal partition*, and there the estimates are
design-dependent in print: the 2022 *Nature Communications* work shows
much of the sibling-design indirect effect is stratification/assortative-
mating artefact (especially for non-cognitive scores); Nivard et al.
(2024) find adoption-design indirect effects systematically lower than
sibling designs; and Veller, Coop and co-authors' dynastic-processes
analysis argues even within-family estimates of "direct" effects absorb
indirect pathways. When the partition moves by a factor of two or more
with the design, and each design's confound is named by the other camp,
Contested is measured, not timid. Stays.

### psych-gep-stem-01 — **STAYS CONTESTED**

The dispute is over the estimand, and both estimands are defensible —
which makes this a real contest, not a correction waiting to happen.
Stoet & Geary's propensity result replicates on its own terms and their
comparative-advantage mechanism (girls' intra-individual reading advantage
in most PISA nations) continues to find support in recent PISA-based
replication analyses; Richardson et al. (2020) show the headline paradox
shrinks or vanishes under the graduate-share metric or alternative
equality indices (including Stoet & Geary's own BIGI); Berggren & Bergh
(2025) add a data-quality account of the paradox itself. Both camps are
publishing now, neither has conceded, and the question "does the paradox
exist" has no answer independent of measurement choices the field has not
adjudicated. Stays.

### psych-lead-crime-01 — **STAYS CONTESTED** (with a STALE sub-claim flagged)

The scored question is the *aggregate* one — did gasoline-lead removal
cause a major share of the 1990s crime decline — and there the contest is
current and two-sided at the highest level of synthesis: Higney, Hanley &
Moro's meta-analysis (2022, 24 studies) concludes the individual-level
link is substantially supported but that lead was "likely not a
significant factor in reduced crime rates" and the aggregate link is
generally overstated, against Reyes-style ecological decompositions
attributing large shares. **However:** required claim 3 as drafted ("no
randomised or clean quasi-experimental evidence establishes individual-
level causality") is now false — failure mode (b) inside a staying item.
Billings & Schnepel (2018) exploit a remediation-eligibility threshold in
a near-RCT design; Aizer & Currie (2019) use traffic-proximity instruments
with sibling fixed effects; Feigenbaum & Muller (2016) instrument lead
water pipes; Grönqvist et al. use Swedish register data on ~800,000
children. The quasi-experimental consensus is that individual-level effects
are real but *smaller* than the ecological estimates — which is exactly
why the aggregate-share question stays open. **Grade stays Contested;
claim 3 must be rewritten at the next revision** or the item will start
scoring correct answers as wrong.

### psych-head-start-01 — **STAYS CONTESTED**

The fade-out leg is settled (HSIS RCT, n ≈ 4,600: cognitive gains gone by
3rd grade) and the rubric grades it so. The adult-outcomes leg — the level
at which the item's bottom line is scored — has a genuine replication
split by cohort: Deming (2009) and Bauer & Schanzenbach find positive
adult-outcome indices for 1980s cohorts in sibling designs; Pages et al.
(2020) reproduce Deming on the 1980s cohorts and find *no* benefit — point
estimates adverse — for 1990s cohorts in the same design; Bailey, Sun &
Timpe (2021, AER) add that long-run effects are real but complementary
with subsequent school spending. "Worked for the 1980s programme against a
home-care counterfactual; unclear for the modern programme against modern
childcare alternatives (Kline & Walters)" is a substantive open question,
not false balance. Stays.

---

## PROVISIONAL 39TH TARGET

### econ-min-unit-pricing-01 — **CONTESTED IS CORRECT** (AUDIT-intervention's demotion upheld; not flippable in either direction)

Independent assessment of the demotion proposed in AUDIT-intervention,
tested in both directions:

- **Flip to settled +intervention? Fails.** The mortality gold rests on a
  single controlled interrupted time-series (Wyper et al. 2023) against a
  modelled England counterfactual spanning COVID, produced by an
  evaluation funded by the government whose flagship policy it is; a
  required claim (the −4.1% admissions figure) is not statistically
  significant in the evaluation's own reporting; named statisticians
  (McConway, Jacobs) dissented at publication; an independent re-analysis
  with the Callaway & Sant'Anna estimator halves the mortality effect to
  marginal significance; and Scotland's absolute alcohol-specific deaths
  hit fifteen-year highs in 2021 (1,245) and 2023 (1,277, NRS) — every
  "deaths fell" claim is true only against the model. A market-side item
  on this file would never have been graded settled (the Sean test).
- **Flip to settled null/anti? Also fails.** The consumption effect is
  strong, consistent across independent evaluation strands and specific in
  timing and product targeting (off-trade sales down ~3%, concentrated in
  cheap high-strength products and heavy-purchasing households), and the
  deaths ITS is statistically significant with effects concentrated where
  the mechanism predicts (most deprived areas; alcoholic liver disease) —
  Public Health Scotland's synthesis judges the deaths-averted evidence
  strong even while flagging admissions as uncertain. A null gold would
  fail hostile audit on the consumption record alone.
- **Verdict:** Contested on health outcomes with the consumption sub-claim
  settled (+intervention direction) is the grade the evidence supports —
  the demotion should be executed exactly as AUDIT-intervention specified
  (contested_empirical tier, band widened to ~45–75). This item is the
  audit's proof of symmetry in the other direction: the same standard
  that flipped three items *out of* Contested here *keeps* an intervention
  item from being graded *above* Contested.

---

## Cross-cutting findings for the pool editor

1. **The dominant false-balance pattern is level-bundling (mode d), not
   cowardice.** Two of the three flips (Smoot-Hawley, Glass-Steagall) and
   the closest non-flip (adverse selection) share one structure: a settled
   headline question welded to a genuinely open magnitude or level-3
   question, with the composite graded Contested. Recommendation: split-
   level scoring — grade the headline claim at its own tier and the
   magnitude/necessity claim at Contested — rather than composite grades.
   Items already built this way (kidney, FDA, clean water) all survived
   this audit untouched.
2. **Stale sub-claims are the next failure mode to hunt.** Lead-crime's
   required claim 3 was true when drafted and is false now; the item's
   grade survived only because its scored level sits above the stale
   claim. A periodic "claim freshness" pass on settled sub-claims inside
   Contested items is cheaper than re-running this audit.
3. **No suppressed intervention consensus was found.** The contested set
   was tested for flips toward intervention with the same bar; the
   candidates (MUP mortality, Portugal attribution inside the drug-war
   item, clean-water magnitude) each failed on single-design evidence,
   inseparable treatment bundles, or a 10%-to-47% identified range. The
   asymmetry in this audit's flip list (3 flips, all correcting
   anti-market or textbook-canon narratives) is a property of which items
   were graded Contested at drafting, and is reported as found, not
   engineered.
