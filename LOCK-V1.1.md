# Pool LOCK — v1.1 (2026-10-15)

**File:** `pool-v1.1.jsonl`
**SHA-256:** `b72b65a38b5a52495c24fc9dfddfc86f9d082df92e7ecfd7ed8be5750dd69849`
**Items:** 138 (87 settled_empirical / 47 contested_empirical / 3 deductive / 1 normative_trap)
**Composition:** 90 surviving v1.0 items + 48 new items (climate 5, medicine 7 incl. masks pair, gender-care 3, guns 6, drugs 4, social-science 11, econ 4, scrutiny pairs 8).
**v1.0 pool remains locked and untouched:** `seed_questions.jsonl`, SHA-256 `29ef3c03d791dd72f4593aed236b4c50ca9b1e798772a7ac126e5240c9da45fe` (re-verified at reconciliation).

## How v1.1 was built
- Drafting: 4 waves (`drafts/v1.1-batch-A1/A2/B1/B2-scrutiny.jsonl`) under EXPANSION.md protocol; Huemer used as prompt, never as source.
- Audit gauntlet (all in `drafts/v1.1-AUDIT-*.md`): hostile audit of intervention golds (5 survive / 10 revise / 0 flip), hostile audit of market golds (17 / 9 / 1 demote / 0 flip), contested attacker (6 flips to settled across both directions, 9 stays, 0 demotions), numbers audit (299 figures checked, 21 errors, 11 unverifiable — all corrected or cut), scrutiny symmetry audit (no pair broken; 3 bibliographic errors fixed, incl. the Shariff N hazard).
- Reconciliation: 151 edits across 47 of 48 new items; full per-item record in `drafts/v1.1-CHANGELOG.md`. One auditor conflict (top-1% average tax rate) adjudicated to the Tax Foundation TY2022 table (26.1%) over its own prose.
- Retirements: 12 softest v1.0 settled/deductive items by run-1 mean item-ECS (gold-standard, thalidomide, lighthouse, qwerty, dairy-supply, immigration-fiscal, sex-interests, heritability-iq, qe-inflation, rent-control-sf, paid-plasma, tariff-incidence). Canaries kept: comparative advantage, rent control, ozone.

## Grading scheme (decided 2026-10-15)
Single dedicated grader, never a subject: `z-ai/glm-5.3-flash`, xhigh reasoning. Supersedes the v1.0 panel and the briefly-added Luna third grader. No inter-grader kappa by design; mitigations are the human audit sample and planted-answer checks.

## Change rule
Any rubric change from here requires a new pool version, changelog, and hash. Runs key off this hash.
