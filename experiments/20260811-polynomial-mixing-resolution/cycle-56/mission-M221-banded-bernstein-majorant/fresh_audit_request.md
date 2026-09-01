# M221 fresh immutable audit request

Please audit frozen M221 without editing it.

1. Verify the complete inventory and every `SHA256SUMS` entry before reading
   conclusions.
2. Independently reconstruct the exact `(B,L,kappa,D)=(1,6,2,1)` actual
   coefficient matrix `A` and first-Jacobi charge matrix `G`, including reset,
   exterior `eta`, the single `1/pi_a`, and omission of killed `a=d`.
3. Derive the banded primal/dual pair and check its on-band/off-band indexing
   under the symmetric Frobenius pairing.
4. Recheck the rational width-zero dual feasibility and positive objective
   excess.
5. Recheck every entry of the displayed tridiagonal `C_1`, all exact signed
   diagonal-dominance margins for both `C_1` and `C_1-A`, its charge, and its
   positive budget slack.
6. Verify that these two certificates prove least bandwidth one only for this
   exact row, not an optimum value or recursive theorem.
7. Independently check saturated bandwidth preservation and the unsaturated
   width-five counterexample/general `w+(L-n)` bound.
8. State `ACCEPT` or `REJECT` with numbered objections.

Strict scope: do not infer a cost-controlled width-one envelope, all-state
fresh contraction, total AMV, a gap, mixing, or Terminal A/B.

