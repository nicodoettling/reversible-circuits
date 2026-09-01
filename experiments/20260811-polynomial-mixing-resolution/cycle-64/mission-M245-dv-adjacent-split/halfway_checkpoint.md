# M245 halfway checkpoint: exact DV source lock

Date: 2026-08-14 UTC.

## Reconstructed statement

Accepted M192/M195 define `(DV)` exactly as

```text
sup over odd k>=3, 2<=l<=(3k-1)/2, Z in {X_l,Y_l}
  [1/sqrt(l)] sum_(s=1)^(k-2) sqrt(s)
    |Phi_(s+1)^D(Z)-Phi_s^D(Z)| < infinity.
```

Here `Phi_s^D` is the normalized B-side law conditional jointly on smaller
first split `s` and a disjoint second edge.  M199/M207 give its literal tuple
support

```text
(i,r,d,a): 0<=i<D, r in {s,D-s}, 1<=d<r,
            1<=a<=r-d-1,
```

with mass `K_R(r,d)/[D(1-gamma_L(s))]`.  The observable counts the three
post-double component faces with multiplicity: two directed one-run gaps and,
for `X_l`, their complementary two-run gap.  Hence same/cross kinds, both
colors, unit gaps, seams, and repeated component-size collisions are all
inside the single conditional expectation before the absolute adjacent
difference is taken.

## Normalization and weights

`D=2k-1`, `R=2k-3`, and

```text
K_R(r,d)=b_d b_(r-d)/(R b_r),
1-gamma_L(s)=h(s)+h(D-s),
h(r)=(r-1)(r-2)/(rR).
```

There is no split-law weight `q_s` or `q_hat_s` in DV.  The sole outer weight
is `sqrt(s)`.  The hatted A-side weight belongs only to DE and is out of this
mission's theorem target.

## Current proof route

The active route is to express the cyclic face averages as explicit seam
incidences, pair the triangular tuple domains for `s` and `s+1`, and estimate
the combined added/deleted boundary plus common-kernel edit.  Bounded exact
diagnostics have not yet been used for any inference.

