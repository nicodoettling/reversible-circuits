# M297 report: small-owner localization of BODT

Date: 2026-08-14 UTC.

## Verdict

```text
PROVE AN ALL-RANK STRICT REDUCTION OF BODT TO SMALL-OWNER-LOCAL FIELDS.
PROVE THE EXACT PHASE-COLLAPSED SCALAR COEFFICIENT FORM.
ISOLATE THE FIRST ROWWISE BOREL COEFFICIENT LEMMA (SOCL).
SOCL, BODT, AND DOR REMAIN UNRESOLVED.
```

The scope is odd `k>=3`, `n=3k`, the complete centered first-pair law in the
auxiliary uniform minimal-factorization model, with `(pq)(x)=p(q(x))`.
It is not the global bridge law or the lazy `{3,4,5}` heat-bath chain.

## Proved advance

Let `h_0=(k-1)/2`.  In every BODT state decompose M290's exact defect field
as `U=U_S+U_L`, where `U_S` contains owners of size at most `h_0` and `U_L`
contains the rest.  The accepted ratio bound gives

```text
TV(U_L)=O(1/k),       ||U_S||_1,||U_L||_1=O(1).
```

The correlation-TV inequality then makes every `U_L/B`, `U_L/U_L`, and
`U_S/U_L` term `O(1/k)` in lag variation.  Large-owner diagonal defects are
also `O(1/k)`.  Applying this only after the complete signed product
coefficient is formed, using `sum|omega|<=2`, proves that BODT is equivalent
to the small-owner-local vector `(SODT)`.

This goes beyond M290/M293's removal of states with three large owners: it
removes large-owner fields even inside every remaining boundary state.

## Exact coefficient reduction

The support-anchor phase is collapsed before norms by

```text
Omega_T(g)=(1/3)sum_r omega(s_T(r,g)),
Omega_S(g)=(1/4)sum_r omega(s_S(r,g)),
Omega_N(g)=(1/4)sum_r omega(s_N(r,g)).
```

Define complete signed scalar lag profiles `H_d` for small-owner/support-head
correlations, `C^off_(d,e)` for distinct small-owner correlations, and `A_d`
for self-owner correlations.  The remaining vector is exactly

```text
-sum_d u_d Delta H_d
+sum_(d,e)u_d u_e Delta C^off_(d,e)
+sum_d(u_d^2+e^2 delta_d)Delta A_d.
```

Thus BODT is equivalent to the lag `l1` estimate `(SOCT)` for this one
already-combined vector.  The self rows for `d<=3` vanish identically on the
target lag range.

## First open lemma

With `b_d=e^-d d^(d-1)/d!`, the rowwise sufficient target is

```text
||Delta H_d||_1                 <=C d b_d/k,
||Delta C^off_(d,e)||_1         <=C d e b_d b_e/k,
||Delta A_d||_1                 <=C d^2 b_d/k,  d>=4.   (SOCL)
```

Every row already combines both source laws, both live channels, all
`T/S/N` compositions, every phase and seam, and all incidences appropriate
to that row.  Summability of the critical Borel masses and
`u_d=O(1/d)`, `u_d^2+e^2 delta_d=O(1/d^2)` show that SOCL implies BODT.

SOCL is not proved.  The missing work is a full complementary-gap Borel
coefficient table; M276's collision-tail calculation cannot be imported as
that theorem.

## Fixed-rank falsification/calibration

The only rank used was the already-authorized `k=9`.  The clean-room probe
reconstructed both source laws, `11,388` supported products, all `44,760`
positive-composition representations, exact 3/4 multiplicities, and the
owner rows.  The direct and phase-collapsed boundary vectors agree exactly.

```text
||BODT boundary||_1 =0.21916460987626177...,
||full DOR||_1      =0.27840195389578080....
```

At small sizes `d,e<=4`, the largest observed normalized SOCL rows are
`4.1182`, `3.6385`, and `0.3562` for `H`, distinct-owner `C`, and self-owner
`A`, respectively.  These data are finite only.

## Exact stop

```text
anchor-collapsed BODT formula                         proved exact
large-owner removal within boundary states           proved all-rank
BODT <=> SODT <=> SOCT                               proved reduction
SOCL                                                  unresolved
BODT, DOR, SET/PBV/FD, FCL1                          unresolved
gap, mixing, Terminal                                 no inference
```

Verdict: **freeze the strict reduction and send it to a fresh referee; assign
the all-rank SOCL coefficient table next.**

