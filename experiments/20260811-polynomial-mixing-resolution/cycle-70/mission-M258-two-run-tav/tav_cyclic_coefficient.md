# M258 exact cyclic-start two-run coefficient

Date: 2026-08-14 UTC.

Status: the identities in Sections 1--3 are **proved algebraically** from
the frozen M235/M238 two-seam geometry and the frozen M199/M207 literal
ordered-double profile. No estimate labelled TAV is claimed here.

## 1. Literal tuple and seam overlap

Fix odd `k>=3`, and put

```text
n=3k,        D=2k-1,        R=2k-3,
b_u=e^-u u^(u-1)/u!,        K(r,d)=b_d b_(r-d)/(R b_r),
h(r)=(r-1)(r-2)/(rR),       H_s=h(s)+h(D-s).
```

The B exterior source-edge word is

```text
V=(1,...,k-1,2k,...,3k-1).
```

Its large seam `beta` and small seam `sigma` have excess increments `k`
and `1`, respectively, and their source-edge positions differ by `k` modulo
`D`.

The exact tuple domain is

```text
2<=r<=D-1,   1<=d<=r-2,   t=r-d (so 2<=t<=r-1),
1<=a<=t-1.                                             (1.0)
```

For such a parent `r`, middle child `d`, retained length `t`, and placement
`a`, define the untranslated retained source-edge set

```text
E_(r,t,a)=[0,a) union [a+r-t,r)  subset Z/DZ.       (1.1)
```

It has `t` edges. Define its exact simultaneous-seam overlap count

```text
j_(r,t,a)
 = #{x in E_(r,t,a): x+k in E_(r,t,a) mod D},       (1.2)
J_(r,t)=sum_(a=1)^(t-1) j_(r,t,a).                  (1.3)
```

As the cyclic first start `i` ranges over `Z/DZ`, each individual seam lies
in the translated retained set exactly `t` times, while both seams lie in it
exactly `j_(r,t,a)` times. Therefore the four literal seam patterns have
counts

```text
neither:       D-2t+j_(r,t,a),
small only:    t-j_(r,t,a),
large only:    t-j_(r,t,a),
both:          j_(r,t,a).                           (1.4)
```

This includes simultaneous hits. It is an identity of translated sets, so
it does not discard either parent orientation, any placement or kind, or a
repeated-size collision.

## 2. Exact averaged cutoff coefficient

Frozen M235/M238 gives the two-run face size

```text
y_B=t+k 1{beta retained}+1{sigma retained}.         (2.1)
```

Since `t>=2`, the lower cutoff is automatic. For integer `ell`, let
`I_u(t)=1{t<=u}` (zero when `u<0`). From (1.4), the exact cyclic-start
average for one placement is

```text
p_ell(r,t,a)
 = 1/D * {
   (D-2t+j_(r,t,a)) I_ell(t)
  +(t-j_(r,t,a)) I_(ell-1)(t)
  +(t-j_(r,t,a)) I_(ell-k)(t)
  +j_(r,t,a) I_(ell-k-1)(t)
 }.                                                  (2.2)
```

Equivalently, define the head/cutoff coefficient

```text
Q_ell(t)=1/D * {
 (D-2t) I_ell(t)+t I_(ell-1)(t)+t I_(ell-k)(t)
}.                                                   (2.3)
```

The simultaneous-overlap multiplier collapses to two exact boundary spikes:

```text
I_ell(t)-I_(ell-1)(t)-I_(ell-k)(t)+I_(ell-k-1)(t)
 = 1{t=ell}-1{t=ell-k}.                             (2.4)
```

Thus, after summing every placement before taking an absolute value,

```text
sum_(a=1)^(t-1) p_ell(r,t,a)
 =(t-1)Q_ell(t)
  +[J_(r,t)/D]{1{t=ell}-1{t=ell-k}}.                (2.5)
```

Equation (2.5) is the requested exact cyclic-start averaged coefficient
formula. The first term is a scalar cutoff/head response. All dependence on
the relative placement of the two seams is confined to the signed pair of
overlap spikes in the second term.

## 3. Exact unweighted TAV profile

Put

```text
T_r(ell)
 =sum_(t=2)^(r-1) K(r,t) {
    (t-1)Q_ell(t)
   +[J_(r,t)/D](1{t=ell}-1{t=ell-k})
  }.                                                 (3.1)
```

Here kernel symmetry was used: `K(r,r-t)=K(r,t)`. The frozen literal
profile now becomes exactly

```text
Theta_s(ell)
 =Phi_s^D(X_ell)-Phi_s^D(Y_ell)
 =[T_s(ell)+T_(D-s)(ell)]/H_s,       1<=s<=k-1.     (3.2)
```

Consequently the still-unresolved TAV estimate is exactly the weighted
adjacent variation of (3.2), with the short increment and shrinking long
increment paired before absolute values. No `q` or `qhat` average occurs.

## 4. Proof

For fixed `(r,t,a)`, translating the first start translates the retained set
through every element of `Z/DZ`. Hence a fixed seam is retained `|E|=t`
times. Writing the seam separation as `k`, starts retaining both seams are
in bijection with the elements counted in (1.2). Inclusion--exclusion gives
(1.4). Substituting the four sizes from (2.1) gives (2.2). Collect the
coefficient of `j`, use the elementary integer-head identity (2.4), and sum
the `t-1` placements to obtain (2.5). Summing with the literal per-placement
kernel and both parent sizes gives (3.1)--(3.2).

All sums are finite, empty sums are zero, and the derivation is valid at
`k=3`, `s=1`, and every cutoff endpoint.
