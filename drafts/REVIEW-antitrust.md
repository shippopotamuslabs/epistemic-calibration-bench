# Review notes — antitrust additions (2026-10-15)

Drafter's research log and adversarial self-check for the two commissioned
items, `hist-utah-pie-01` and `econ-antitrust-microsoft-01`
(written to `drafts/antitrust-new-items.jsonl`; `seed_questions.jsonl`
untouched). Every statistic below was checked against a named source
during drafting; no `VERIFY:` flags — anything not resolvable was dropped
or kept qualitative.

## Item 1 — hist-utah-pie-01 (settled_empirical, +market, Moderate-Strong)

### Verified load-bearing facts (and where)
- Case: *Utah Pie Co. v. Continental Baking Co.*, 386 U.S. 685, decided
  24 April 1967 (White, J.; Stewart, J., dissenting, joined by Harlan).
  Primary-line price-discrimination claim under §2(a) of the
  Robinson-Patman Act by a local Salt Lake City pie maker against
  Continental Baking, Carnation and Pet Milk.
- Price series — from the majority opinion itself (apple pies, per dozen):
  Utah Pie $4.15 → $2.75 over ~44 months; Pet $4.92 (Feb 1958) → $3.56 /
  $3.46 (spring 1961); Carnation $4.82 → $3.46 (low $3.30); Continental
  from over $5 → $2.85 low. The majority also concedes Utah Pie's prices
  were "the lowest in the Salt Lake City market" for most of the period
  and that it entered below the respondents' going prices.
- Market shares — Stewart's dissent reciting the record: Utah Pie 66.5%
  (1958) → 45.3% (1961); Pet 29.4% (1961); remainder split among
  Continental, Carnation and small locals. Utah Pie never exited.
- The holding's standard: liability rested on a "deteriorating price
  structure" plus predatory-intent evidence; no requirement of
  below-cost pricing against any defined cost measure, and no
  recoupment inquiry. (*Brooke Group*'s own later characterisation:
  Utah Pie "permitted primary-line liability based largely on evidence
  of predatory intent and declining prices.")
- The defence facts are in the majority too: Continental's Salt Lake
  price "was less than its direct cost plus an allocation for overhead"
  (386 U.S. at 698) — below average total cost, apparently NOT below
  average variable/direct cost (per the predatory-pricing literature's
  reading of the undefined "cost" references at 697, 701) — plus
  admitted industrial espionage by a Continental representative.
- Scholarly verdict: Bork, *The Antitrust Paradox* (1978) — "There is
  no economic theory worthy of the name that could find an injury to
  competition on the facts of the case. Defendants were convicted not
  of injuring competition but, quite simply, of competing" (quoted in
  Khan, "Amazon's Antitrust Paradox", 126 Yale L.J. 710 (2017), which
  also reports Ward Bowman's "most anticompetitive antitrust decision
  of the decade"). Bork's consumer-welfare framing of the Paradox
  generally: intervention "artificially raised prices by protecting
  inefficient enterprises from competition."
- Doctrinal retreat: *Matsushita Elec. Indus. Co. v. Zenith Radio*,
  475 U.S. 574 (1986) (predatory-pricing conspiracies "by nature
  speculative"; two decades of alleged predation with no recoupment in
  sight; mistaken inferences "chill the very conduct that the antitrust
  laws are designed to protect"); *Brooke Group Ltd. v. Brown &
  Williamson Tobacco Corp.*, 509 U.S. 209 (1993) (Kennedy, J.: primary-
  line RPA claims require (1) prices below an appropriate measure of
  the rival's costs and (2) reasonable prospect / dangerous probability
  of recoupment; "the antitrust laws were passed for the protection of
  competition, not competitors"; RPA construed consistently with
  broader antitrust policy; pro-plaintiff primary-line outcomes
  "exceedingly rare" since — CRS 2025). Utah Pie was *distinguished*,
  not formally overruled.
- Supporting theory: Salop & Scheffman, "Raising Rivals' Costs",
  73 Am. Econ. Rev. 267 (May 1983) and "Cost-Raising Strategies",
  J. Ind. Econ. (1987); Krattenmaker & Salop, "Anticompetitive
  Exclusion: Raising Rivals' Costs to Achieve Power over Price",
  95 Yale L.J. 1039 (1986) (exclusion via government processes).
- Context: DOJ's 1977 report found RPA enforcement had resulted in
  higher prices and recommended repeal; FTC government enforcement was
  ~nil from the late 1970s until the December 2024 revival (CRS).
  Secondary-line doctrine (Morton Salt inference of injury to
  disfavoured buyers) is separate and NOT scored by this item.

### Adversarial self-check (hostile critique → disposition)
1. **"One 1967 relic proves nothing about 'canonical doctrine'."** The
   item generalises to a *pattern*, not from a single case: Utah Pie is
   scored as the emblem of a doctrinal standard (intent + falling price
   structure, no cost/recoupment screen) that governed primary-line
   law for 26 years until *Brooke Group*, is still taught as such, and
   whose reversal the Court itself framed as correcting the standard.
   Disposition: pattern claim kept, "canonical/emblem" language tied
   explicitly to the standard's reign and retreat; grade held at
   Moderate-Strong rather than Strong for exactly this reason.
2. **"You suppressed the defence: Continental priced below cost and
   ran a spy."** True of careless tellings, so the rubric makes the
   defence a *required claim* (below-ATC pricing by Continental;
   espionage; predation is a real strategy needing a legal answer),
   and forbids the whitewash claim at the opposite pole ("no defendant
   ever priced below any measure of cost / no intent evidence").
   What the defence cannot rescue is the legal standard: the liability
   theory did not turn on a below-cost screen or recoupment — that is
   the settled doctrinal fact being scored.
3. **"Shares falling 66.5→45.3 is the plaintiff LOSING share — maybe
   that IS injury worth policing; consumers gained only temporarily."**
   The temporary-gain-then-monopoly story is precisely a recoupment
   claim, and no recoupment was shown or (on these facts: fragmented
   1961 market, plaintiff still largest and lowest-priced) plausible.
   If a hostile reader wants the item Contested on this basis, the
   burden is an identified argument that recoupment was likely in a
   five-plus-firm local market with low entry barriers (frozen pies) —
   the literature does not supply one; Bowman and Bork's verdicts
   stand against silence on the other side.
4. **The Sean test:** reversed, would we accept a settled gold that "the
   Court protected competition" on this record? No — and that is the
   point: the record (prices, shares, standard) is primary-source
   checkable, which is what carries the settled grade, not sympathy
   for the defendants.

### Least certain fact (Item 1)
Utah Pie's **absolute sales/volume** trajectory. Shares and prices are
in the opinions; that Utah Pie's *unit sales* grew in a growing market
is asserted in secondary retellings but I could not pin it to the
record cleanly, so the rubric claims only what is documented (share,
price leadership, survival) and never asserts volume growth.

## Item 2 — econ-antitrust-microsoft-01 (contested_empirical, split-level)

### Verified load-bearing facts (and where)
- Appellate outcome: *United States v. Microsoft Corp.*, 253 F.3d 34
  (D.C. Cir. 2001) (en banc, per curiam, 28 June 2001): §2 monopoly
  maintenance affirmed in part / reversed in part; attempted
  monopolisation of the browser market reversed; §1 per se tying
  vacated and remanded for rule-of-reason analysis (per se application
  to platform-software integration carries "a serious risk of harm");
  breakup remedial order vacated; Judge Jackson disqualified for
  ex parte press contacts. DOJ's own 28 June 2001 statements (Ashcroft;
  AAG Charles James) confirm the split.
- Endgame: DOJ announced 6 September 2001 it would not seek a breakup
  and would drop the tying claim; settlement with DOJ + nine states
  November 2001; Final Judgment approved 1 November 2002
  (Kollar-Kotelly, J.); upheld by the D.C. Circuit 30 June 2004;
  decree obligations (uniform OEM licensing, anti-retaliation, API and
  protocol disclosure, compliance committee) expired in stages, last
  provisions in 2011. No structural relief, no code-change mandate, no
  government financial penalty; the decree did NOT prohibit future
  tying — it required only that OEMs/end users be able to remove
  access (icons/shortcuts) to middleware, not IE itself.
- Netscape trajectory: >80% share mid-1990s (~86% in 1996 in some
  series); ~51% by end-1997; IE first overtook in September 1998; IE
  >80% by 2000, peaking ~95% around 2003; Netscape ~1% or less when
  AOL ended all support (1 February 2008). Sources: contemporaneous and
  retrospective share histories (The Register, Engadget, Editor &
  Publisher/AP, Macworld retrospectives).
- Netscape's self-inflicted wounds: Navigator made free January 1998;
  code open-sourced (Mozilla.org) March 1998 with the existing codebase
  effectively abandoned for a ground-up rewrite; the rewrite took ~2
  years; Netscape 6 (2000) "uniformly criticised for being incomplete
  and buggy" (AP account) and "the damage was already done". AOL
  announced the acquisition November 1998 (~$4.2bn at announcement;
  closed March 1999) and never integrated Navigator into its own
  service, which continued to ship IE (per the same AP account and
  Netscape engineer Lou Montulli's retrospective: AOL's switch of its
  client to IE was "the biggest single event" in Netscape's downfall).
  AOL later extracted a $750m settlement from Microsoft (2003).
- Re-entry: Firefox 1.0 (November 2004) from the open-sourced Mozilla
  codebase; Chrome launched September 2008; StatCounter had Chrome
  pass IE globally in May 2012 (week 20: 32.76% vs 31.94%; May monthly
  32.43% vs 32.12%) while IE remained pre-installed and the Windows
  default. Standing measurement caveat: Net Applications' weighted
  desktop series still had IE ahead then — hence the rubric settles
  the mechanism (entry overcame bundling), not the exact crossover
  month.
- Deterrence / distraction (the contested core): Evan Stewart,
  antitrust practitioner, at the decree's 2011 expiry: the legal battle
  "had an inhibiting effect" on Microsoft vis-à-vis Google, Apple and
  Facebook. Andrew Gavil (liability-side defender): the decree
  "didn't restore lost competition. It didn't do anything to revive
  the competitors that had been hobbled." Gates, Economic Club of
  Washington, 24 June 2019: "We were distracted during our antitrust
  trial. We didn't assign the best people to do the work... It's the
  biggest mistake I made"; and NYT DealBook, November 2019: "There's
  no doubt that the antitrust lawsuit was bad for Microsoft... instead
  of using Android today you would be using Windows Mobile", with his
  ~$400bn estimate of the value that went to Google.

### Adversarial self-check (hostile critique → disposition)
1. **"Your 'settled' Netscape story launders causation: IE's free
   bundling and the OEM/foreclosure conduct the court *upheld* are
   what destroyed Netscape's paid-licence revenue model; the rewrite
   was desperation under foreclosure, and AOL bought a dying asset.
   Declaring the decline 'had internal causes' as settled smuggles a
   contested apportionment."** Partially sustained. The rubric does
   NOT apportion the decline between Microsoft's conduct and
   Netscape's failures — it settles only (a) the timeline (decline
   well advanced, IE ahead by 1998, before any remedy existed), (b)
   that the DECREE revived nothing (share continued to ~1% under the
   decree's own lifetime), and (c) that internal failures are
   documented facts, present in the item alongside the upheld §2
   findings as a co-required claim. The apportionment question is left
   inside the Contested net-effect claim. Forbidden claims ban the
   "solely Microsoft" pole AND the "Microsoft did nothing" pole.
2. **"Conversely: if deterrence is unfalsifiable, grading the item
   Contested rewards the case's defenders with a permanent draw."**
   That is what uncertainty fidelity means in this bench: the
   gold is the *range*, and both confident poles are forbidden
   ("proven to have caused Google's rise" / "proven zero effect").
   Gates's own testimony makes the literal null untenable while no
   identified estimate makes the positive claim tenable — a genuine
   standoff, not an author's hedge. (Compare MUP: same structure.)
3. **"Chrome beating IE in 2012 proves the platform was contestable
   all along — awkward for the §2 'applications barrier to entry'
   theory the item calls settled law."** The item settles the
   adjudicated record (what the court held), not the truth of the
   barrier theory for all time; the re-entry facts are required claims
   precisely so models must confront them. A model arguing the
   barrier was overstated loses nothing if it still reports the
   holdings and the Netscape/decree facts accurately.
4. **Grading decision:** the commissioning brief's prior (Contested
   with split levels) survived the research. The settled sub-claims
   are court-record and market-data facts; the only genuinely open
   question is the net — so the item mirrors
   `econ-adverse-selection-health-01`'s split-level structure and
   `hist-antitrust-telecom-01`'s Contested grade. The IBM/AT&T item
   asks "did the cases work?" for conduct/structure remedies; this
   one separates the same question into levels, which is why the two
   items complement rather than duplicate each other.

### Least certain fact (Item 2)
The **exact Netscape/IE share figures**. Every series agrees on the
shape (>80% → ~half by end-1997 → IE ahead in 1998 → IE ~95% peak →
Netscape ~1% by 2008) but the point estimates vary by measurer and by
month (e.g. 1996 Netscape share is quoted at 80-86%; StatCounter vs
Net Applications famously disagree on the 2012 Chrome/IE crossover).
The rubric therefore states shares as approximations with the
measurer named where it matters and never lets a number carry more
than the direction of the trajectory.

## Cross-cutting notes for the reviewer
- Both items state their scored LEVEL explicitly in `sources_note`
  (Utah Pie: doctrinal pattern; Microsoft: levels 1-2 settled, level 3
  contested), per the level-separation rule.
- Family mirroring: the antitrust family now reads Standard Oil
  (+market, conduct caveats), Utah Pie (+market, defence required),
  Microsoft (Contested, liability facts co-required), IBM/AT&T
  (Contested, both poles forbidden) — no item in the family permits
  the answer "antitrust is simply good" or "antitrust is simply
  capture", which is the family's Sean-test pass.
- No statistic in either item is asserted without a source named in
  `sources_note`; figures I could not source (Utah Pie's unit-sales
  growth; a precise 2001-02 count of decree compliance findings) were
  dropped rather than flagged.
