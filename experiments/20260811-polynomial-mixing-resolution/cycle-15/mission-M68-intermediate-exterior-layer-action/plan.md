# M68 plan: intermediate exterior-layer action

## Objective

For `N>=5`, `m=2N-2`, and the literal lazy exact `{3,4,5}` same-product
heat-bath chain, analyze the M64 breadth-first cuts

```text
C_k=A union E_k,   0<=k<2R_ext,
R_ext=50N^2m^3+N+1.
```

The primary target is either:

1. a universal inverse-polynomial lower bound on the two-sided conductance of
   every growing intermediate-radius `C_k`; or
2. an explicit infinite family of literal-chain cuts with superpolynomially
   small two-sided conductance, with exact stationary mass and complete
   H3/H4/H5 boundary flow.

The multiplication convention is `(pq)(x)=p(q(x))`, words are written and
evaluated left to right as `t_1...t_m`, and every probability includes the
outer laziness, block-size choice, window choice, and exact conditional-fiber
normalization.

## Exact inherited identity

With `L_0=E_0`, `L_k=E_k minus E_(k-1)`, `W=|Omega(N,m)|`, and
`s_k=min(|C_k|,W-|C_k|)`, M64 proves

```text
Q_K(C_k,C_k^c)
=W^-1 [sum_(x in C_k) K(x,F_N minus A)
       +sum_(x in L_k)K(x,L_(k+1))],

Phi_pm(C_k)=W Q_K(C_k,C_k^c)/s_k.
```

It also proves the lower numerator

```text
alpha_N |A| + p_min |L_(k+1)|,
```

fixed-radius polynomial leakage, exterior saturation by radius `2R_ext`, and
polynomial leakage after saturation.  Polynomial exterior diameter alone is
not an expansion theorem and will not be used as one.

## Work lanes

1. **Coarea/layer growth.** Seek an exact inequality relating cumulative
   exterior volume to the next-layer flow or to flow back into `F_N minus A`,
   retaining global smaller-side orientation.
2. **Recoverable exterior escape flow.** Try to replace the fixed paired-word
   exterior hub by a distributed surplus-handle deletion/merge map whose
   boundary edge and bounded metadata recover the source with polynomial
   multiplicity.
3. **Barbell search.** Test whether a family of weighted-component or Hurwitz
   subregions can carry nonnegligible global stationary mass while every
   H3/H4/H5 exit is superpolynomially suppressed.  Any proposed cut must use
   the exact full boundary, not a sparse subchain.
4. **Reduction audit.** If the literal target remains open, isolate the first
   standalone missing proposition and prove why diameter, minimum edge
   probability, or finite layer thickness does not supply it.

## Computational scope

Exact calculations, if used, will have fixed commands and machine-readable
output and will test named finite identities or candidate lemmas only.  They
will not be used to infer asymptotic expansion.  Existing exact `N=5` closure
already serves as the smallest full H3/H4/H5 calibration.

## Expected failure modes

- canonical normalization paths collide at exponentially small hubs;
- minimum positive transition probability loses an `N^11` factor per layer;
- within-macro Hurwitz diameter supplies reachability but no congestion;
- a cut defined only in a sparse H3/Hurwitz subchain is bypassed by H4/H5;
- an exterior mass estimate is useless unless paired with the globally
  oriented smaller-side denominator;
- a barbell in an auxiliary projection need not lift to the literal word
  chain.

## Required final schema

The final report will contain: exact claim/convention; full argument;
probability/runtime/path/congestion accounting; labeled dependencies; first
unproved standalone proposition; self-attack; calibrations; artifacts and
reproduction; and exactly one scoped verdict `PROVED`, `REFUTED`, or
`OPEN AT A NAMED STEP`.
