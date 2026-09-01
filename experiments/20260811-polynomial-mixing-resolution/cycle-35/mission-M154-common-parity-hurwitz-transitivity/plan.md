# M154 Plan: Common-parity signed-Hurwitz transitivity

## Objective

Attack the remaining diagonal-product-system (DPS) action-orbit obligation after the accepted M135/M137, M141/M143, and M146/M148 reductions.  Let

```text
P_{d,s} = { (g_1,...,g_s) in S_d^s : sgn(g_1)=...=sgn(g_s) }
```

and let `C_{d,s}` be the conjugacy class in `P_{d,s}` consisting of tuples whose every coordinate is a transposition.  The strong candidate is that the signed-Hurwitz action is transitive on length `2d-2`, product-one, generating `C_{d,s}`-factorizations, at least for the aligned matching source/target families constructed in M135, for `d >= 5`.

## Scope and labels

- Target: an action-orbit theorem/reduction inside a fixed Hurwitz fiber, not a global sampler or a mixing bound.
- Product convention and exact signed-Hurwitz action will be copied from the accepted/frozen predecessor artifacts and stated before any theorem claim.
- M150 is evidence only until its independent M153 review is accepted.
- Literature classification theorems are dependencies unless their exact hypotheses, central extension, conjugacy-class data, product convention, and conclusion are checked.
- Exact `d=3,4` and tightly capped `d=5` calculations are falsifiers only.

## Work packages

1. Read the source-of-truth files and frozen/accepted M135/M137, M141/M143, M146/M148, plus frozen M150.
2. Reconstruct the precise aligned matching factorization family and signed-Hurwitz generators.
3. Search for elementary invariants of the braid/group action: coordinate projections, subgroup-generation data, tuple conjugacy, lifting/spin data, ordered intersection/Nielsen data, and stabilizer-coset obstructions.
4. Build a small exact checker for the smallest meaningful cases, with deterministic parameters and machine-readable output.  Use it only to refute overstrong universal statements or expose a missing invariant.
5. Attempt an elementary reduction.  If a Conway--Parker-style completeness statement is indispensable, isolate the exact missing theorem as an unresolved dependency rather than invoke it.
6. Freeze the strongest exact result, all negative findings, checker/results, report, hashes, and manifest for fresh review.

## Candidate outcomes

- `promote`: a self-contained strictly scoped transitivity theorem or a rigorous reduction with a genuinely narrower, falsifiable final action/coset lemma.
- `reject`: an exact counterexample/additional invariant separating aligned source and target orbits.
- `inconclusive`: only if neither survives exact checks; state the first unresolved lemma exactly.

## Exceptional cases

Audit `s=1`, `d=3`, `d=4`, `d=5`, minimal length `2d-2`, and the distinction between arbitrary generating factorizations and the aligned M135 source/target family.  No claim may silently extend from aligned families to all of `C_{d,s}`.

