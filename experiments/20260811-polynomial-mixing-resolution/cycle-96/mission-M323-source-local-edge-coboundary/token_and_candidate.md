# M323 fully combined token and frozen source surgery

Date: 2026-08-14 UTC.

Status: **reconstructed and frozen before computation.**

## 1. Exact normalization and token label

Put `m=k-1`.  The two live-channel masses are

```text
alpha_1=4m^2/[3m(3m-1)],
alpha_2=2m(2m-1)/[3m(3m-1)],
alpha_1+alpha_2=2(4m-1)/[3(3m-1)].                 (1.1)
```

For H/A there are three literal owner slots and for C there are six ordered
distinct-owner slots.  Hence the controlling M313 normalization is

```text
c_X=r_X(alpha_1+alpha_2),
r_H=r_A=3,        r_C=6.                            (1.2)
```

In particular

```text
c_H=c_A=2(4m-1)/(3m-1),
c_C=4(4m-1)/(3m-1).
```

The source-A normalized endpoint law is `g_s=Gtilde_s/c_X`; the source-B
law is `f_t=Ftilde_t/c_X`.  Both live channels are summed before this
normalization.

A complete weighted raw marked atom is written

```text
xi=(R,j,v,e,f,g,K,r,gaps,iota,P).                   (1.3)
```

Here `R` is source A or B, `j` is the live channel, `v` is the conditioned
exterior split, `(e,f)` is the literal ordered first-factor pair,
`g=ef` is its product, `(K,r,gaps)` is one of the exact positive-composition
representations with its triangle `1/3` or combined-double `1/4` weight,
`iota` is one of the fixed literal slots (including a zero slot), and `P` is
the derived H/A/C response profile.  The atom weight includes the exact
minimal-completion count after `(e,f)`.  Thus all raw lifts, channels,
`T/S/N` kinds, anchors, phases, seams, incidences, representation factors,
and zero slots are fields of `(1.3)`; none is normed separately.

For a supported quantile cell `(s,t)`, put

```text
a_(s,t)(P)=[g_s(P)-f_t(P)]_+,
b_(s,t)(Q)=[f_t(Q)-g_s(Q)]_+,
rho_(s,t)=sum_P a_(s,t)(P)=sum_Q b_(s,t)(Q).        (1.4)
```

Disintegrate `g_s` and `f_t` over their complete raw fibers at each profile.
A literal off-diagonal residual token is

```text
omega=(s,t; xi_A at P, eta_B at Q),                 (1.5)
```

with exact weight

```text
w(omega)=c_X*pi_(s,t)*a_(s,t)(P)*b_(s,t)(Q)/rho_(s,t)
         *Pr[xi_A | s,P]*Pr[eta_B | t,Q].           (1.6)
```

It is oriented `P -> Q`.  Summing `(1.6)` gives M319/M321's literal token
expansion and `J_e=L_e^+-L_e^-`, including edges incident to profile zero.

## 2. Frozen natural surgery `S_pf`

The exterior residual cycles are

```text
source A: C_-=(0,...,k-1), M=(k,...,2k-1),
          C_+=(2k,...,3k-1),
source B: {0}, L=(1,...,k-1,2k,...,3k-1), M.        (2.1)
```

Their cut/join seam vertices are

```text
Sigma={0,1,k-1,2k,3k-1}.                            (2.2)
```

For a raw atom `xi`, define the attempted product-fixed source switch
`sigma(xi)` as follows:

1. change source A to B or B to A;
2. retain the literal ordered prefix `(e,f)`, hence the product `g=ef`, its
   positive-composition representation, marked slot, and response profile;
3. recompute only the channel and exterior-split labels relative to the new
   source, and use the new source's exact minimal-completion weight.

This is a valid opposite-source raw atom exactly when the retained prefix is
rank-decreasing for that source.  It is the literal weighted-atom version of
cutting source A at `0`, joining its two exterior arcs into `L`, or applying
the inverse seam cut, without moving the observed first-pair product.

For a token `(1.5)`, the predeclared surgery is

```text
S_pf(s,t;xi_A,eta_B)
  =(s',t'; sigma(eta_B)_A, sigma(xi_A)_B),           (2.3)
```

where `(s',t')` are the derived new split labels.  Because the two products
and marked slots are retained, `(2.3)`, whenever valid, preserves the
unordered profile edge and reverses its orientation.

## 3. Frozen exceptional predicate and target assertion

For a marked atom, let `chi_iota` be the marked owner indicator (the union
of both indicators for a C slot) and let `B_g` be its literal support-head
set.  Freeze

```text
Touch_Sigma(xi)
 :=[(supp chi_iota) intersect Sigma != empty]
   or [B_g intersect Sigma != empty],

Exc_pf(omega)
 :=Touch_Sigma(xi_A) or Touch_Sigma(eta_B).          (3.1)
```

This predicate uses only marked-owner/head/seam geometry.  It does not use a
profile-edge sign, a final surplus, an atom order, or arbitrary mass matching.

The frozen `SLPF` assertion to be tested analytically is: off `Exc_pf`, both
source switches in `(2.3)` exist, `S_pf` is an involution on literal tokens,
the new quantile cell is supported, and

```text
w(S_pf omega)=w(omega).                              (3.2)
```

Thus `(3.2)` is the zero-coboundary special case of the required exact weight
coboundary and would cancel every nonexceptional edge contribution before a
norm.  The remaining task would be the three required Borel bounds on
`mass(Exc_pf)`.  No part of `SLPF` is claimed here; it is now frozen before
the sole optional guard.
