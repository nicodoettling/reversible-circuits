# Coordinator reconciliation v1

The coordinator read the exact full T0, C1, C2 and LC1-v3 proofs; the blind reports; complete r1/r2/r3 reviews; scripts and raw results. This document accepts only the exact scoped claims listed in claim-ledger-v1.md. Accepted means proved within the frozen finite model after same-model internal review, not external certification. No status was inherited merely from restart or checkpoint.

## Exact proof graph

`proof-graph-v1.json` records load-bearing dependencies. T0 D1 (even moments/maxima) feeds D2 (global completion density and replacement domination); D3 (literal c6/c12 counts) feeds D4 (N>=1000 constant); D2,D4,D5 (pointwise witness budget) yield D6 and D7. C1's standalone strong bound uses its exact relator law, deterministic block damage, iid-preserving Q_k and one bridge-conditioning inequality. C2 uses its exact path/star law, support preservation, and a literal disjoint-doubled-edge lower count under that same change of measure. Neither depends on LC1, an imported mixing theorem, a connected sampler, or a historical irreducibility claim.

LC1-v3 separately uses commuting coordinate projections, exact hypergeometric avoidance, and corrected common-denominator accounting. Its efficient corollary explicitly requires fixed s, polynomial N,L, a public polynomial-time f evaluator with polynomial-bit values or charged table, and public positions. It supplies no hidden-key-dependent distinguisher and no universal local bias.

## Reviews and resolution

- T0: blind statement-only reconstruction `r3-adversarial/blind-supplement-v2-T0.md`; full exact reviews `r2-construction/review-T0-v1.md` and `r3-adversarial/review-T0-v1.md`. Both found every D1-D7 dependency sound. Coordinator independently checked all formulas/constants and the candidate schedules. J003 covers finite falsification; J005 independently applies reversed gates to points and recovers c6(4)=3936. Accepted in exact T0 scope.
- C1: blind algorithm assessment in BS1; full coordinator rederivation `reviews/coordinator-C1-review-v1.md`; T0 separately covers the entire structural class. J002 verifies construction and moves, J004 computes literal noisy-word laws. The pre-review general random-bit estimate was incorrect off schedule; its preserved erratum supplies s log L. The candidate law and its polynomial schedule did not change. Accepted attack; rejected hiding candidate.
- C2: blind BS3 independently found the support obstruction; exact canonical full review `r1-theory/review-C2-v1.md` checked normalizers, unique literal count, lambda>=1024 onset, and k=L vacuity. Coordinator repeated the analytic count and schedule inequalities and J005's distinct evaluator counted D(6,2)=270. J002 covers identity/moves/implementation support, plus exact schedule arithmetic. Accepted canonical attack; rejected hiding candidate.
- LC1: blind BS1 reconstructed the probability identity. R3 found v1's missing q^s denominator growth; both r2/r3 found v2's missing public evaluator and bit-size assumptions. Versions and complete objections are retained. V3 received a fresh full r2 review and a full r3 recheck, both bound to exact hashes. J005 targets the actual denominator defect. Accepted v3 only; v1/v2 overbroad clauses remain superseded and are not erased.
- C2 BS3 alternative onset81 is an independently authored provisional argument, not a dependency of the accepted canonical theorem. No status upgrade is inferred from its author's verdict. It remains available for a later exact-version audit if desired.

All reviewers share model family and project context lineage. The blind inputs reduce some proof-contamination risk but do not establish statistical independence. C2's algorithm disclosed its support motivation, and this limitation is preserved. Every worker authored within its assigned directory; all mathematical jobs were launched by the coordinator under the single-job registry.

## Probability and quantifier audit

No proof multiplies marginal untouched-window probabilities. T0's structured bound is pointwise, and reference Markov uses only expectation. C1/C2 move independent product calculations to the unconditioned iid law and explicitly pay one bridge-conditioning factor. The sole repeated-query product in T0 is justified by the actual fresh reference product law conditional on public A; it is not average-key-to-every-key amplification. Candidate setup has no secret key. The shared sign/distance/support endpoint restrictions are never treated as distinguishers.

All claims retain global labeled ordered U, rightmost-first composition, exact k-subsets, hidden tapes, replacement coincidences, and exceptional parameter cases. Polynomiality names lambda,N,L. No negligible semantic correctness follows from the inverse-polynomial schedules; no recovery/cryptographic assumption is imported.

## Decisive checks, preserved counterexamples, and delivery

J001-J005 completed with exact output files, no truncation, fresh Python -B processes, stdlib, one reservation at a time. J005 supplied coordinator-authored independent word evaluation and targeted repaired-lemma checks. Finite verification corroborates the symbolic proofs and does not replace them. The raw C1 law calculation includes exact high-noise equality at k=L-1 and k=L; these negative findings remain in the report.

The final delivery audit by r1 checks report/ledger against proofs and raw numbers. Its three requested presentation fixes were applied: include N>=1000 next to the ledger's .7 corollary, use the exact LC1 proof path, and distinguish the 15-second inert smoke from 60/120-second mathematical reservations. Complete pre-edit inputs are retained as reviews/delivery-input-report-v1.md and delivery-input-ledger-v1.md; exact mathematical proofs were unchanged. The final review/addendum is in r1-theory/delivery-audit-v1.md and its companion recheck when published.

This closes the bounded study's attack-or-candidate deliverable. It does not settle the general existence of sparse-noise hiding constructions. No third candidate or unrequested continuation is included. The scoped completion artifact requests operator review; no marker or Git commit certifies general security.
