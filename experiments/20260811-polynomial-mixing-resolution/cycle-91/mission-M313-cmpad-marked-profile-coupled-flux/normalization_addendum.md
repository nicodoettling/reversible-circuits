# M313 controlling normalization addendum

The displayed flux `(2)` in `plan.md` omitted the fixed slot mass

```text
c_X=r_X(alpha_1+alpha_2),   r_H=r_A=3, r_C=6,
```

after defining `kappa_(s,t)` as a coupling of **normalized** extended laws.
The controlling exact definition, fixed analytically before the finite guard,
is equation `(3.3)` of `analytic_flux.md`:

```text
J^X(P,Q)=c_X sum_(s,t)pi_(s,t)
          [kappa^X_(s,t)(P,Q)-kappa^X_(s,t)(Q,P)].
```

This factor is essential for the literal divergence equality.  It is bounded
by six and therefore does not alter the asymptotic MPCF statement or its
Borel scales.  The sole guard uses the corrected exact definition.

