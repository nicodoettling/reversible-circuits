# M297 strict small-owner localization for BODT

Date: 2026-08-14 UTC.

Status: Propositions 1--3 below are proved exact/all-rank.  The rowwise
small-owner coefficient lemma `(SOCL)` is unresolved.  Consequently BODT and
DOR remain unresolved.

## 1. Scope, convention, and immutable inputs

Use `(pq)(x)=p(q(x))`, with displayed factors multiplied left-to-right.  Put

```text
n=3k,                 k>=3 odd,
h_0=(k-1)/2.
```

The target is the complete centered first-pair law in the auxiliary uniform
minimal-factorization model used by M261--M293.  This is not the global
identity-word target and not the lazy exact same-product `{3,4,5}` heat-bath
chain.

All payloads in the required accepted author/referee pairs pass their frozen
`SHA256SUMS` inventories:

```text
M261 b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b
M264 b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f
M267 001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6
M270 6c0c6e13c62885a0c56e8c232c0f2ddc48922be56b3edce97a4f9c9b9ca5491e
M276 882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db
M279 3910c66a134083117e8defce4bf6a3d57fdce3a48b519e7c8271c1864bf52f66
M282 cac6e77151401e708acb5a812097ccce44ed1dce45acefada9a3c13ebcfe5ed7
M286 3778a3884212e4b5403df1d37a1145a2810b77f94b55e84dd84aac1dec6c0f0a
M289 327176968d69eb447ff862354eb566ed00cfd2c56b2e77079231bcc077f93680
M292 8fefffab69cca864c9260429e9eef34671aab23a497e36fb05cb6b89c378740f
M290 85373b13ab4799f59d98dd20bf5b0496fa61d119b45b0ffe34900094564df687
M293 b7020fb3ee6cfc9b2536b500928320ff4ce0bc8fc0983c65989ff092d9ac3f1f
```

The imported statuses are literal.  In particular, CIBV is separate from
the decorated vector studied here; M290/M293 prove only `DOR <=> BODT`.

For a supported product `s`, let the three residual owners have indicators
`chi_i`, sizes `d_i`, and null owner at each support head.  Put

```text
G_s=sum_i chi_i,              B_s=1-G_s,
a_d=tau(d-1)/tau(d),          delta_d=tau(d-2)/tau(d)-a_d^2,
u_d=e a_d-1,                  U_s=sum_i u_(d_i) chi_i.
```

Owners of size one have no generic phase.  The accepted M290/M293 bounds are

```text
0<=u_d<=4/d                         (d>=2),
0<=delta_d<=C/d^2                  (d>=3).          (1.1)
```

At `d=2`, `delta_2=-1`, but the owner has at most one generic phase, so its
nonzero-lag self-correlation vanishes.

The complete already-combined product coefficient is

```text
omega(s)=P_B(s)-P_A(s)
        =a(s)[C_B(s)/A_B-C_A(s)/A_A]
        =alpha_1 beta_1(s)+alpha_2 beta_2(s),       (1.2)
```

including both live channels and every triangle/double lift.  Therefore

```text
sum_s omega(s)=0,             sum_s |omega(s)|<=2. (1.3)
```

No source law, channel, kind, topology, or seam is separated below.

## 2. Exact phase collapse with the 1/3--1/4 factors intact

For the positive compositions and owner rows accepted by M290/M293, define

```text
Omega_T(g)=(1/3)sum_(r mod n)omega(s_T(r,g)),
Omega_S(g)=(1/4)sum_(r mod n)omega(s_S(r,g)),
Omega_N(g)=(1/4)sum_(r mod n)omega(s_N(r,g)).       (2.1)
```

The literal owner response depends on `K,g,ell` but not on the support
anchor `r`.  Let `mathcal D_K(g,ell)=Delta Q_ell(s_K(r,g))`.

### Proposition 1 (proved: anchor-collapsed BODT)

If `mathcal G_bd` contains exactly the `T/S/N` compositions with an owner of
size at most `h_0`, then the BODT vector is exactly

```text
V_bd(ell)=sum_((K,g) in mathcal G_bd)
             Omega_K(g) mathcal D_K(g,ell).         (2.2)
```

#### Proof

In M290/M293's exact positive-composition formula, translation by `r`
changes neither owner sizes nor any circular correlation in the response.
Thus the boundary indicator and `mathcal D_K` may be pulled through the
`r`-sum.  A triangle still has three representations and a double still has
four representations across the combined `S/N` rows, yielding exactly
`(2.1)--(2.2)`.  No extra factor `n` is introduced.  QED.

This collapse is coefficientwise: it occurs before every lag absolute value.

## 3. All large-owner fields can be removed even inside boundary states

For a boundary state, split its owner set into

```text
S(s)={i:d_i<=h_0},              L(s)={i:d_i>=h_0+1},
U_S=sum_(i in S)u_(d_i)chi_i,   U_L=sum_(i in L)u_(d_i)chi_i. (3.1)
```

The set `S(s)` is nonempty.  Define the small-owner-local profile, omitting
the irrelevant lag-constant term, by

```text
Q^S_ell(s)
 =-Corr(U_S,B_s;ell)-Corr(B_s,U_S;ell)
  +Corr(U_S,U_S;ell)
  +e^2 sum_(i in S)delta_(d_i)Corr(chi_i,chi_i;ell). (3.2)
```

### Proposition 2 (proved: uniform large-field remainder)

There is an absolute constant `C` such that every boundary state satisfies

```text
sum_(ell=2)^(n-3)
 |Delta Q_ell(s)-Delta Q^S_ell(s)| <= C/k.          (3.3)
```

Consequently BODT is equivalent to

```text
sum_(ell=2)^(n-3)
 |sum_(s boundary)omega(s)Delta Q^S_ell(s)|=O(1/k). (SODT)
```

#### Proof

Each owner indicator is a union of at most two circular intervals, so

```text
TV_circ(chi_i)<=4,       ||chi_i||_1<=d_i,
||B_s||_1<=4.
```

For `i in L(s)`, `(1.1)` and `d_i>=(k+1)/2` give

```text
TV_circ(U_L)<=sum_(i in L)4u_(d_i)=O(1/k),
||U_L||_1<=sum_(i in L)u_(d_i)d_i<=12.             (3.4)
```

The same norm bound `||U_S||_1<=12` holds for the small field.  Circular
correlation obeys

```text
TV_circ Corr(f,g)
 <=min(||f||_1 TV_circ(g),TV_circ(f)||g||_1).      (3.5)
```

Expand M290's accepted defect identity after `U_s=U_S+U_L`.  Equations
`(3.4)--(3.5)` bound each of

```text
Corr(U_L,B_s), Corr(B_s,U_L), Corr(U_L,U_L),
Corr(U_S,U_L), Corr(U_L,U_S)
```

by `O(1/k)` in circular variation.  For a large owner with `d_i>=3`,

```text
e^2 delta_(d_i) TV_circ Corr(chi_i,chi_i)
 <=C d_i^(-2) (4d_i)=O(1/k).                       (3.6)
```

The possible `d_i=2` exception has zero target-lag derivative, and size one
has no generic phase.  The remaining term `2 sum_x U_L(x)` is lag-constant.
This proves `(3.3)`.

Finally apply `(3.3)` only after the complete coefficient `(1.2)` is formed:

```text
||sum_(s boundary)omega(s)Delta(Q-Q^S)(s)||_1
 <=(C/k)sum_s|omega(s)|<=2C/k.
```

Adding or subtracting this proved vector gives the stated equivalence.  No
triangle inequality was taken between `P_B/P_A`, `T/S/N`, or `IS/IN/X`.
QED.

This is strictly stronger than M290's all-macroscopic-state removal: it also
removes every large-owner field and every small/large cross term from the
remaining boundary states.

## 4. Exact scalar coefficient form

For `1<=d,e<=h_0`, define the following scalar lag profiles by summing all
`T/S/N` positive-composition rows with their already-collapsed coefficients
`Omega_K(g)`:

```text
H_d(ell)
 =sum_(K,g)Omega_K(g) sum_(i:d_i=d)
   [Corr(chi_i,B;ell)+Corr(B,chi_i;ell)],

C^off_(d,e)(ell)
 =sum_(K,g)Omega_K(g) sum_(i!=j:d_i=d,d_j=e)
    Corr(chi_i,chi_j;ell),

A_d(ell)
 =sum_(K,g)Omega_K(g) sum_(i:d_i=d)
    Corr(chi_i,chi_i;ell).                          (4.1)
```

The sums in `(4.1)` need no explicit boundary indicator: the displayed
small owner already puts the state in `mathcal G_bd`.  The `1/3` triangle and
`1/4` `S/N` factors, both source channels, all owner seams, and all phases
remain in `Omega_K` before any row norm.

### Proposition 3 (proved: strict scalar reduction)

The exact SODT vector is

```text
W_ell=
 -sum_(d<=h_0)u_d Delta H_d(ell)
 +sum_(d,e<=h_0)u_d u_e Delta C^off_(d,e)(ell)
 +sum_(d<=h_0)[u_d^2+e^2 delta_d]Delta A_d(ell).   (4.2)
```

Hence BODT, DOR, and the scalar statement

```text
sum_(ell=2)^(n-3)|W_ell|=O(1/k)                   (SOCT)
```

are equivalent, using the accepted `DOR <=> BODT` reduction.

#### Proof

Expand `(3.2)` owner by owner.  The two `U_S/B` correlations give the first
sum in `(4.2)`.  Split `Corr(U_S,U_S)` into `i!=j` and `i=j`; the former
gives the second sum and the latter contributes `u_d^2 A_d`.  The diagonal
defect contributes `e^2 delta_d A_d`.  Phase collapse is Proposition 1, and
Proposition 2 supplies the `O(1/k)` equivalence.  QED.

For every rank, `Delta A_d` vanishes throughout the target lags for
`d=1,2,3`: a size-one owner has no generic phase, a size-two owner has at
most one, and a one-run size-three owner has only two consecutive generic
phases (the two-run case has at most one).  Their self-overlap is supported
only at lags `0,1,n-1`, outside both endpoints of every target difference.

## 5. First unresolved scalar coefficient lemma

Put

```text
mathfrak b_d=e^(-d)d^(d-1)/d!=e^(-d)tau(d).
```

The fixed analytic candidate is the following rowwise estimate.

> **Small-owner coefficient lemma `(SOCL)` (unresolved).**  There is an
> absolute constant `C` such that, for every odd `k>=3`,
>
> ```text
> ||Delta H_d||_1
>    <=C d mathfrak b_d/k,                         1<=d<=h_0,
>
> ||Delta C^off_(d,e)||_1
>    <=C d e mathfrak b_d mathfrak b_e/k,          1<=d,e<=h_0,
>
> ||Delta A_d||_1
>    <=C d^2 mathfrak b_d/k,                       4<=d<=h_0,  (SOCL)
> ```
>
> where each norm is over `ell=2,...,n-3` and each row is the complete
> already-combined row `(4.1)`.

This lemma is strictly coefficient-level: the rooted-tree defect amplitudes
`u_d,delta_d` no longer occur in it.

### SOCL implies BODT

For `d>=3`, `(1.1)` gives

```text
|u_d|<=4/d,        |u_d^2+e^2delta_d|<=C/d^2.      (5.1)
```

The `d=2` self row is zero as above.  Since the critical Borel masses are
summable,

```text
sum_d mathfrak b_d<infinity,
sum_(d,e)mathfrak b_d mathfrak b_e<infinity,
```

substitution of `(SOCL)` into `(4.2)`, with a triangle inequality only over
the already-combined owner-size rows, yields `||W||_1=O(1/k)`.  Propositions
2--3 then give BODT and DOR.  No row in `(SOCL)` separates source laws,
`T/S/N`, or same/cross topology incidences.

The missing all-rank step is now exact: prove `(SOCL)`, or prove the weaker
combined `(SOCT)` directly.  The expected Borel mechanism is the accepted
low-component ratio cancellation

```text
signed density =mathfrak b_d H_k(d),
|H_k(d)|<=C d/k,        |H_k(d+1)-H_k(d)|<=C/k,
```

but a complete derivation must retain every complementary gap and both
one-run/two-run geometries.  It is not licensed by M276's collision-tail
calculation.

## 6. Sole fixed-rank calibration

After `(SOCL)` was fixed, the clean-room scripts evaluated only `k=9`.
They reconstruct both source laws from minimal-completion counts, import no
predecessor data, and keep the complete coefficient `(1.2)` before norms.

Exact checks include:

- source masses one from `10,044/22,108` raw A/B ordered pairs;
- `11,388` supported products and `9,673` boundary products;
- all `44,760` positive-composition representations;
- exact 3/4 multiplicities and representationwise owner rows;
- exact equality of direct and anchor-collapsed boundary vectors; and
- exact symbolic lag signs, with no undecided coordinate.

The finite values are

```text
||BODT boundary vector||_1 =0.21916460987626177...,
||full DOR vector||_1      =0.27840195389578080....
```

For the `(SOCL)` normalizations at `d,e<=4`, the observed maxima are

```text
max_d k||Delta H_d||_1/(d mathfrak b_d)             =4.1182...,
max_(d,e) k||Delta C^off_(d,e)||_1/(de b_d b_e)     =3.6385...,
max_d k||Delta A_d||_1/(d^2 mathfrak b_d)           =0.3562....
```

These are exact-rational rows with floating Borel normalizations.  They are
finite calibration only and prove no uniform constant.

## 7. Exact stop

```text
phase-collapsed 1/3--1/4 BODT formula             proved exact
large-owner removal inside every boundary state  proved all-rank
BODT <=> SODT <=> SOCT                            proved reduction
A_d target derivative zero for d<=3              proved all-rank
SOCL                                               unresolved
BODT, DOR, SET/PBV/FD, FCL1                       unresolved
every gap, mixing claim, and Terminal             no inference
```

The correct next mission is an all-rank proof or counterexample for `(SOCL)`
using the full complementary-gap coefficient table.  DSR/DTR and the `k=9`
row are not used as a theorem.

