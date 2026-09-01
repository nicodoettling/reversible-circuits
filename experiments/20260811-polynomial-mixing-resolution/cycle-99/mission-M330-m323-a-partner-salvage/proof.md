# M330 exact fixed-cell salvage proof

Date: 2026-08-14 UTC

## Statement

In the frozen `k=7,H_2` quantile cell `(s,t)=(1,1)`, with
`Sigma={0,1,6,14,20}` and M323's fixed bad B atom
`e=(6,14), f=(3,5)`, the missing A-side non-Touch residual mass satisfies

```text
N_A=2037915313150409615825963
    /288085426550809623412604928 > 0.              (1)
```

Consequently the append-only package M323+M330 contains a positive-mass token
outside `Exc_pf` on which M323's frozen `S_pf` is undefined.

Status: **proved as an exact finite statement**.

## Exact A-fiber reconstruction

The script SHA-gates M323/M326/M329 and the M297 completion primitive. It
reconstructs only split 1 in the fixed row/cell, retaining the A raw marked
slots. The fixed-cell B side is aggregated only to define the already-frozen
profile residual `a(P)=[g_A(P)-f_B(P)]_+`; no B candidate search is performed.

For every retained A atom `xi` of profile `P`, its contribution is

```text
a(P) Pr[xi | s=1,P] 1[not Touch_Sigma(xi)].       (2)
```

Summing (2) over all 3,276 raw marked A slots gives (1). The positive residual
mass on all A profiles also sums to the frozen

```text
rho_11=49168032837363259/1633552709319917568,
```

providing an internal normalization check.

## First explicit non-Touch A atom

The first lexicographic positive-residual, non-Touch A atom is

```text
channel       2
split         1
first edge    (3,4)
second edge   (4,5)
marked slot   1
owner size    1
profile       (0,...,0)  [17 zeros]
owner support empty
support heads {2,3,4}.
```

Both owner and head intersections with `Sigma` are empty. Its exact weights
are

```text
completion numerator/denominator
  =59379122092290000/81435568248417631248,
raw unconditional prefix mass
  =625/857157,
q_1=1296/2401,
raw conditional marked mass
  =625/462672,
A profile marked mass
  =176355146/69429717,
a(P)=1703889405470479/77788224253329408,
Pr[xi|s=1,P]=1500625/2821682336,
a(P)Pr[xi|s=1,P]
  =1064930878419049375/91417600301718608805888 >0.  (3)
```

The owner-size-one slot is part of the frozen three-slot zero-profile extension;
its marked profile is therefore exactly the zero profile, not an omitted slot.

## Pairing with M323's fixed B atom

For the fixed B atom, the frozen and rechecked facts are

```text
b(Q)=21484375/54238159872,
Pr[eta|t=1,Q]=1/2,
marked-owner support={3},
support heads={2,4,5,13}.
```

Those B owner/head sets are also disjoint from `Sigma`. Hence both endpoints
of the explicit token lie outside `Exc_pf`.

Using `c_H=46/17`,
`pi_11=61917364224/137858491849`, the displayed `rho_11`, (3), and the B
weights, the residual product-coupling mass of the explicit pair is

```text
(c_H pi_11/rho_11)
 [a(P)Pr[xi|s,P]] [b(Q)Pr[eta|t,Q]]
=65802548799959422226562500000
 /706358481579483924710894769596909369 >0.         (4)
```

Summing over every non-Touch A atom while keeping this B atom fixed gives

```text
(c_H pi_11/rho_11) N_A b(Q)Pr[eta|t,Q]
=119877371361788800930939000000000
 /2119075444738451774132684308790728107 >0.        (5)
```

## `S_pf` conclusion and strict boundary

M323's fixed B prefix has opposite-source A ranks

```text
18 -> 19 -> 18,
```

instead of the required `18 -> 17 -> 16`. Thus its opposite A raw prefix does
not exist. Equations (4)--(5), together with the two non-Touch checks, supply
the endpoint certificate missing from M323: `S_pf` is undefined on an actual
positive-mass token outside `Exc_pf`.

This salvages exactly M323's off-`Exc_pf` obstruction. It does not prove the
enlarged-exception compatible coboundary, supported reverse-token landing,
any H/A/C exceptional Borel-scale estimate, MPCF, or a downstream theorem.

