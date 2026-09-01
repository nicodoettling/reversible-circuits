# M118 plan: fresh audit of M113 handle projection

Date: 2026-08-12 UTC.

## Objective and scope

Audit the frozen M113 handle-cell projection reduction without editing any
predecessor or shared durable file.  The target is the auxiliary uniform law
on connected-support length-`2d` identity transposition words and the
half-lazy signed adjacent-Hurwitz kernel, with composition
`(pq)(x)=p(q(x))` and factors multiplied left-to-right.

The audit is deliberately nonterminal.  It tests the exact reduction to the
local connected-unicycle incidence chain; it does not attempt to prove the
open polynomial incidence gap or a full `{3,4,5}` heat-bath mixing theorem.

## Claims to test

1. Re-derive the exact cut-refresh projected mass and stationary flow, and
   the factor `beta >= gap(G)/2`.
2. Verify that `A_d` is a valid reversible chain and independently derive
   `gap(G) >= 2 D^{-3} gap(A)` and `beta >= D^{-3} gap(A)`.
3. Audit realizable-key sufficiency/necessity, adjacent overlap and its two
   coagulation/fragmentation cases, and the exact cell count.
4. Audit the qualitative key-graph connectivity proof, including `d=2`.
5. Verify the first-Higgs-lift basis identification.
6. Reconstruct exactly the `d=4` weighted Hessian obstruction and its
   untilted analogue.
7. Re-derive the balanced split-family pointwise and aggregate arithmetic.
8. Write independent code (no predecessor imports) to enumerate `d=2,3,4`,
   compare observed keys with the combinatorial characterization, check cell
   and overlap counts, form `A`, `G`, and the full projected chain, and
   numerically diagonalize their exact rational flows.

## Expected failure modes

- a missing factor two in extracting the holding subkernel;
- using the density comparison in the wrong direction;
- an invalid row normalization for `A_d`;
- a zero-size combinatorially declared key;
- a join/cut convention reversal;
- a cell-count mismatch caused by a Hurwitz convention error;
- an incorrect coefficient normalization in the Hessian test;
- treating finite spectra or qualitative connectivity as a polynomial gap.

## Reproducibility

The computation is deterministic (`seed=null`) and uses Python plus NumPy
only.  Raw output will be written to `independent_results.json`.  The final
report will give an `ACCEPT` or `REJECT` verdict with numbered material
objections, followed by a freeze manifest and checksums.
