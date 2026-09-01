# Plan: independent referee of the M10 two-block bridge recursion

## Frozen target

Audit the exact constant-loss recursion for microfactorized
`Q=P_transposition^2` fixed-endpoint bridges, including its pointwise
smoothing threshold, tilted two-tail angle, Hamiltonian comparison, affine
iteration, and final conversions to the aligned scan `B` and the original
lazy `{3,4,5}` chain `K`.

## Audit lanes

1. Re-derive the Diaconis--Shahshahani parity conversion from the primary
   Plancherel inequality, including the exponent `2s` and finite-`N` closure.
2. Check the endpoint-tilt Radon--Nikodym formula and optimize/test the stated
   `22/75` maximal-correlation bound with sparse endpoint weights.
3. Verify that the two conditional expectations include all microfactor
   labels and that their principal angle is exactly the boundary maximal
   correlation.
4. Audit every interval-site coefficient and ensure the continuous-time
   comparison avoids a repeated random-scan loss.
5. Check the parity choice of overlap, affine halving, stopping range, and
   `3^{-ceil(log_2 x)}` algebra.
6. Re-derive `gap(B)=Lambda/(n-1)` and the exact
   `(m-2)/[12(m-3)]` comparison coefficient for `K`.
7. Run a deterministic finite-dimensional counterexample search for the
   density/correlation and projection-angle inequalities, and exhaustive
   integer checks of the recursion indices.  Survival is an audit only, not
   proof.

## Decision rule

Return `ACCEPT` only if every dependency is proved or cited with matching
normalization and no endpoint/boundary case changes the frozen theorem.
Otherwise return `REJECT` with numbered objections.
