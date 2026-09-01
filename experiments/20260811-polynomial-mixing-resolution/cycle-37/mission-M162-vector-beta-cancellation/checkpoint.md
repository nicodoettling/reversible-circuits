# M162 halfway checkpoint

Date: 2026-08-13 UTC.

## Status

The frozen M123/M128, M147/M151, M152/M156, and M157/M160 artifacts have
been read.  The exact M157 kernel is PSD because its recursion expands into
actual history-current outer products.  I will make that implicit expansion
explicit as a finite vector feature map.

The first genuinely off-diagonal inequality is now fixed.  For
`U~Beta(D,kappa-D)`, decompose the vector polynomial `Phi_x(U)` into its
constant and centered Jacobi modes.  Bessel/Pythagoras in the *actual
history-feature Hilbert space* gives

```text
||E Phi_x||^2
 <= E||Phi_x||^2
    - ||E[(U-EU)Phi_x]||^2/Var(U).
```

This keeps an exact signed two-copy covariance term and is strictly sharper
than M157's diagonal trace whenever the degree-one vector coefficient is
nonzero.  It does not use the refuted generic canonical-basin frame.  The
inequality itself is universal; whether its right-heavy value stays below
`1-q` is the current falsifiable question.

No gap or terminal claim is presently available.

## Completed halfway test

The exact capped run has now finished.  It verified the shared-observation
transfer, the feature-kernel equality, finite Jacobi Parseval, and the exact
first-mode vector recursion in every one of 588 states with
`B<=3,L<=6,kappa<=8`.  On all 147 right-heavy rows `D=1`, the degree-one
bound is within budget.  Diagonal trace already passes 143 rows; subtracting
the first centered Jacobi energy repairs exactly four:

```text
(s,kappa,D,B)=(8,2,1,2),(7,2,1,3),(8,2,1,3),(9,2,1,3).
```

This is exact finite evidence only.  The universal theorem is the feature
map, Jacobi decomposition, truncated upper bounds, and first-mode recursion.
The all-suffix degree-one boundary is still open.
