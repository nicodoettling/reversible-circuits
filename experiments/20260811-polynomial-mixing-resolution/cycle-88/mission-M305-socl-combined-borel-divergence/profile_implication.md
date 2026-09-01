# M305 deterministic profile implication

Date: 2026-08-14 UTC.

Status: **proved exact conditional implication `CBPV => SOCL`**.  CBPV is
not yet proved.

## 1. Exact conventions

Use M297/M302's already-combined `Omega_K(g)` and target lag range
`2<=ell<=n-3`.  An owner indicator `chi_i` is a union of at most two
circular intervals and the support-head indicator `B` has at most four
points.  Hence

```text
TV_circ(chi_i)<=4,       ||chi_i||_1<=d_i,
||B||_1<=4.                                      (1.1)
```

For circular correlation,

```text
TV_circ Corr(f,g)
 <=min(||f||_1 TV_circ(g),TV_circ(f)||g||_1).    (1.2)
```

Restricting circular variation to the target lag differences can only
decrease it.

## 2. Literal response bounds

For every actual owner occurrence of size `d`, equations `(1.1)--(1.2)`
give

```text
||Delta[Corr(chi_i,B)+Corr(B,chi_i)]||_1<=32,
||Delta Corr(chi_i,chi_i)||_1<=4d.                 (2.1)
```

For two distinct owner occurrences of sizes `d,e`,

```text
||Delta Corr(chi_i,chi_j)||_1<=4 min(d,e).         (2.2)
```

These are deterministic profile bounds.  They do not take an absolute value
between source laws, channels, `T/S/N`, phase anchors, seams, or incidences.

## 3. CBPV implies the three SOCL rows

By the definition fixed in `plan.md`, the exact complete rows can be grouped
by their literal response profiles:

```text
Delta H_d=sum_P mu^H_(k,d)(P) P,
Delta A_d=sum_P mu^A_(k,d)(P) P,
Delta C^off_(d,e)=sum_P mu^C_(k,d,e)(P) P.          (3.1)
```

This is an equality after the full combined coefficient has been formed.
Taking the triangle inequality only over the already-combined profile
classes and using CBPV and `(2.1)--(2.2)` gives

```text
||Delta H_d||_1
 <=32 ||mu^H_(k,d)||_TV
 <=C d b_d/k,

||Delta A_d||_1
 <=4d ||mu^A_(k,d)||_TV
 <=C d^2 b_d/k,

||Delta C^off_(d,e)||_1
 <=4min(d,e)||mu^C_(k,d,e)||_TV
 <=C d e b_d b_e/k.                                (3.2)
```

Thus CBPV proves exactly SOCL, with no signed source/type row split.

## 4. Sizes one, two, and three

Set the formal amplitude `u_1:=0`.  A size-one residual owner has no generic
phase, so `chi_i=0`; therefore every `H_1`, `A_1`,
`C^off_(1,e)`, and `C^off_(d,1)` response row is identically zero.  Under
the literal pushforward definition, the signed coefficient measure may retain
an atom at the zero profile `P=0`; that atom multiplies the zero response and
needs no estimate.  Equivalently, delete the zero profile from every reduced
response measure.

At size two an owner has at most one generic phase.  At size three it has
either two consecutive generic phases (one-run) or at most one (two-run).
Their self-correlations are supported only at circular lags `0,1,n-1`, so

```text
Delta A_2=Delta A_3=0
```

throughout the target range.  The `H_2,H_3` and off-diagonal rows with sizes
two or three do not vanish and still require the first and third CBPV bounds.
This includes the minimal odd rank `k=3`.

No SOCL, SOCT, BODT, DOR, or downstream theorem is asserted until CBPV or a
weaker direct row estimate is proved.
