# Cycle 06 M16-CGL plan: leave-one-out recursion and correlations

## Exact model and target

Use `(pq)(x)=p(q(x))` and left-to-right tuple products. Let

```text
E=T_N^2,             p(a,b)=ab,
Omega_l(h)={x in E^l:product_i p(x_i)=h},
```

with the uniform law on every nonempty bridge. For raw coordinates `i<j`,
`P_ij` is conditional expectation given all coordinates outside `{i,j}` and

```text
C_(l,h)=binom(l,2)^(-1) sum_(i<j) P_ij.
```

For `A_k=sigma(x_k)`, put `R_k=E[.|A_k]` and
`A_(l,h)=l^(-1)sum_k R_k`.

The first target is the exact endpoint-uniform recursion

```text
gap(C_(l,h))
 >= gap_worst(C_(l-1)) [1-mu_l(h)],
```

including every crossing pair and singleton conditional slice. The second
target is the coordinate-correlation spectrum and either an accumulated
polynomial bound through `l=O(N log N)` or the sharpest surviving named
replacement.

## Proof programme

1. Define the micro Hurwitz bijection
   `(x,y)->(y,x^(p(y)))`, with coordinatewise conjugation, and move a fixed
   coordinate to the left or right boundary without changing that
   microstate.
2. On each fixed-coordinate slice, prove that the braid is a product of
   one-coordinate bijections. This must explicitly include raw pairs with
   one index on either side of the deleted coordinate.
3. Average the leave-one-out chains and derive the CGL quadratic-form
   inequality with exact normalizations.
4. Write `A=T T*` and identify its nonzero spectrum with the block Gram
   operator `T*T`, whose blocks are coordinate conditional-correlation
   kernels.
5. Exploit the central group-algebra element
   `W=(sum_(t in T_N)t)^2` to compute exact one- and two-coordinate laws.
   Separate micro-lift noise from product-coordinate modes.
6. Audit the literal accumulated product at `l=2`, formulate the corrected
   product from `l=3`, and prove the finite-dimensional CGL Lemma-4.1
   dichotomy for high-correlation modes.
7. Use exact small cases only to falsify named candidate correlation bounds;
   do not infer an asymptotic lower bound from finite spectra.

## Known obstructions retained

- Crossing raw pair projections need not commute and may have a negative
  Caputo cross term. The proof will not use either assertion.
- The complete three-site gap is not uniformly greater than `1/3`.
- A pointwise inverse-polynomial bound on `1-mu_l` is insufficient if its
  product over `O(N log N)` lengths is superpolynomial.
- Canonical or linear buffer recovery has superpolynomial congestion.

## Finite falsifiers and calibration

If a small exact correlation harness is needed, it will test explicit claims
such as `mu_l<=1/(l-1)` or a proposed endpoint-independent block kernel. It
will cover `N=3,4`, `l=2,3`, identity and nonidentity endpoints, and will
retain microfactor multiplicities exactly. Passing data will be labeled
finite only.
