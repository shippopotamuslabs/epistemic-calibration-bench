# Expansion protocol: seeds (30) -> 100 items

Commissioned by Sean 2026-10-15, with his explicit worry attached: the pool
must not become "biased to my opinion." His conversion story matters here —
he arrived at these positions by reading, against his upbringing, and he
wants the benchmark to be the kind of instrument that could have changed
*his* mind with data, not a monument to conclusions already reached.

## Why the popular narrative skews interventionist (structural, not conspiratorial)
1. **Credit-claiming asymmetry.** A law has a date, a sponsor and a signing
   photo; the pre-existing trend it rode has none of those. Textbooks are
   written from the law's press release.
2. **Seen vs unseen (Bastiat).** Intervention successes have visible,
   named beneficiaries; intervention costs are statistical, delayed and
   dispersed (invisible graveyard); market successes are invisible in the
   opposite way — nobody holds a ceremony for a disaster that competition
   prevented or a price that quietly halved (kerosene).
3. **Institutional position of the narrators.** Public schools teach the
   civics-textbook version; academic economics is substantially publicly
   funded. This does not make claims false — it makes *unexamined*
   credit-claims cheap to repeat and expensive to check.
4. **The mirror warning (applies to us):** libertarian literature curates
   its cases too. Every rubric below gets the same audit regardless of
   which direction its gold points. A case that only survives friendly
   reading does not enter the pool.

## The skeptical-review checklist (every drafted item, no exceptions)
- [ ] **Pre-trend?** Was the outcome already moving before the policy?
      (child labour, lead paint, OSHA)
- [ ] **Counterfactual named?** Compared to *what* — nothing, the prior
      regime, a different policy, a foreign twin? (Canada for the Fed)
- [ ] **Credit assignment?** Who else was on the field (income growth,
      technology, a different institution — FDIC vs the Fed)?
- [ ] **Replication status?** Has the headline number survived re-audit?
      (clean water shrank; Peltzman disputed; Flynn hollowed)
- [ ] **Visible/invisible symmetry?** Are both sides' victims counted the
      same way?
- [ ] **Favourable-conditions audit** for successes: what made this case
      easy (ozone: few producers + substitutes; smallpox: no animal
      reservoir)? The caveat goes IN the rubric.
- [ ] **Level separation?** (Sean, 2026-10-15) Three different questions are
      routinely smuggled into one another: (1) did the outcome improve?
      (2) did the policy cause the improvement? (3) was *this institutional
      form* necessary — or would a market / a different policy have done it
      as well, slightly worse, or better? A rubric must state which level it
      scores and forbid importing an answer from one level into another.
      (Clean water: filtration→typhoid is level 2 and solid; "therefore
      government provision was necessary" is level 3 and unsettled.
      Acid rain: emissions fell is level 1; the cap's causal share is level
      2 *after* the pre-1990 decline is subtracted; the trading mechanism's
      credit is cost, not existence of the decline.)
- [ ] **Mirror exists?** Within each family, is there an item whose gold
      points the other way? If a family cannot produce one honestly, the
      family lead writes down why, in the design doc.
- [ ] **Source quality:** peer-reviewed / official data > journalism >
      advocacy. Advocacy-preprint numbers (e.g. "102M FDA deaths") may be
      *mentioned* only as forbidden settled citations.
- [ ] **The Sean test:** if this item's gold were reversed, would we apply
      the same evidence bar? If not, rewrite or grade Contested.

## Workflow
1. Subagents draft batches of ~16 items into `drafts/batch-<X>.jsonl` in
   the exact seed schema, each batch internally mirrored (at least 3 items
   whose gold credits intervention/collective action or is honestly
   Contested), with real named sources in `sources_note` — any statistic
   the drafter cannot source gets flagged `VERIFY:` rather than asserted.
2. Tensor skeptical-reviews every item against the checklist, spot-checks
   sources with web search, cuts or re-grades failures, and only then
   merges into `seed_questions.jsonl`.
3. Target composition at 100: no direction (pro-market / pro-intervention /
   contested / trap) above ~45% of the pool, and every domain family
   carrying at least one item that embarrasses its "home team."

## Slam-dunk hunt (Sean's challenge: find intervention wins besides ozone)
Found and added: **smallpox eradication** (Strong; favourable-biology
caveat in rubric), **acid-rain SO2 cap-and-trade** (Strong; government cap,
market execution — credit to the combination). Already in pool: **leaded
gasoline phaseout**, **thalidomide gatekeeping**, **vaccination
externalities**, **congestion pricing**. Audited and *downgraded*:
**municipal clean water** — the Cutler & Miller headline halved under
re-examination; graded Contested with the typhoid sub-claim Strong.
Verdict so far: clean slam dunks are rare not because interventions never
work but because "worked flawlessly" needs a clean counterfactual, and
history usually supplies a mess — which is itself a finding the benchmark
should report, not hide.
