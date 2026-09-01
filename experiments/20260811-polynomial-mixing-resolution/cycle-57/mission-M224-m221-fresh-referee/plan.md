# M224 plan: fresh immutable referee of frozen M221

Date: 2026-08-13 UTC.

## Objective

Independently audit M221's exact one-row minimal-bandwidth theorem and its
negative retained-lift closure statement. Issue `ACCEPT` or `REJECT` with
numbered objections.

## Immutable source gate

- Source mission:
  `cycle-56/mission-M221-banded-bernstein-majorant/`.
- Expected source `SHA256SUMS` digest:
  `ff5315e5930f3d8dc3c959acbb4413e32df4cf1f9870338e94ec892c18ec1983`.
- Verify the complete source inventory and every payload hash before reading
  conclusions.
- Treat M221 as immutable.

## Independent checks

1. Reconstruct the `(B,L,kappa,D)=(1,6,2,1)` actual kernel and degree-six
   Bernstein matrix with exact arithmetic, literal ordered compositions, and
   exact Gaussian basis inversion; import and read no M221 code or data.
2. Construct the uniform first-Jacobi cost matrix independently.
3. Re-derive the banded primal/dual indexing under the symmetric Frobenius
   pairing.
4. Verify the accepted rational width-zero dual's PSD decomposition, on-band
   equality, objective, and positive budget excess.
5. Verify every rational entry of the width-one tridiagonal primal, all exact
   strict signed-diagonal-dominance margins for `C` and `C-A`, its exact
   charge and positive budget slack.
6. Check that these certificates prove least bandwidth exactly one only for
   this row.
7. Independently prove saturated bandwidth preservation and the unsaturated
   upper bound `min(L,w+(L-n))`; reproduce the `d=1,a=0` width-five example.
8. Freeze proof audit, checker/results, report, manifest, and checksums.

## Strict exclusions

No recursive width-one envelope, all-state majorant, fresh contraction, total
AMV, spectral gap, mixing, or Terminal A/B inference.

