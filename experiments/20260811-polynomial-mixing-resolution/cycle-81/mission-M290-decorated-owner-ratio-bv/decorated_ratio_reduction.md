# M290 exact decorated owner-ratio reduction

Date: 2026-08-14 UTC.

Status: Propositions 1--4 below are proved exact.  The boundary owner-defect
transport lemma `(BODT)` and the optional sign route `(DSR)/(DTR)` are
unresolved.  No PBV, FD, or downstream claim is made.

## 1. Setting and literal decorated endpoint law

Use `(pq)(x)=p(q(x))`, with displayed factors multiplied left-to-right.  Put
`n=3k`, with odd `k>=3`.  For a supported rank-two product `s`, let
`q_s=s^-1h` have residual owners `C_i` of sizes `d_i`, and extend the generic
edge-owner map by a null owner at every support head.  Write

```text
kappa_ii=tau(d_i-2)/tau(d_i),
kappa_ij=tau(d_i-1)tau(d_j-1)/[tau(d_i)tau(d_j)]  (i!=j),
rho_ij=e^2 kappa_ij-1,
rho(i,empty)=rho(empty,j)=0.
```

Invalid shifted sizes are zero.  Define

```text
C_ij^s(ell)=sum_x 1[o_s(x)=i]1[o_s(x+ell)=j],
Q_ell(s)=sum_(i,j)rho_ij C_ij^s(ell).
```

### Proposition 1 (literal decorated endpoint coefficient)

For every `2<=ell<=n-3`, exactly

```text
Delta Q_ell(s):=Q_(ell+1)(s)-Q_ell(s)

 =sum_(x mod n) [
    rho(o_s(x-ell),o_s(x+1))
   -rho(o_s(x-ell),o_s(x))].                       (1.1)
```

Only a literal owner jump at `x` contributes.  Formula `(1.1)` retains every
positive and negative endpoint of each one-run or two-run owner, the cyclic
lag, the owner sizes, and the same-owner/cross-owner distinction.

#### Proof

Subtract adjacent circular correlations and put `x=r+ell`.  At fixed `x`,
the owner sums select the three displayed owner positions; the null extension
covers support heads.  This is the same exact index operation as M267's
accepted endpoint law, with `kappa` replaced by `rho`.  QED.

## 2. Defect-field decomposition and diagonal second order

Put

```text
a_d=tau(d-1)/tau(d),
b_d=tau(d-2)/tau(d),
delta_d=b_d-a_d^2,
u_d=e a_d-1.
```

Let `chi_i(x)=1[o_s(x)=i]`, let

```text
G_s=sum_i chi_i,                  B_s=1-G_s,
U_s(x)=sum_i u_(d_i) chi_i(x),
Corr(f,g;ell)=sum_x f(x)g(x+ell).
```

Thus `B_s` is the indicator of the three or four support-head positions.

### Proposition 2 (exact defect-field identity)

At every circular lag,

```text
Q_ell(s)
 =2 sum_x U_s(x)
  -Corr(U_s,B_s;ell)-Corr(B_s,U_s;ell)
  +Corr(U_s,U_s;ell)
  +e^2 sum_i delta_(d_i) Corr(chi_i,chi_i;ell).      (2.1)
```

Consequently the constant first term disappears from `Delta Q_ell`.

#### Proof

M285/M287's accepted owner decomposition is

```text
F_ell=Corr(A_s,A_s;ell)+sum_i delta_(d_i)C_ii(ell),
A_s(x)=sum_i a_(d_i)chi_i(x).
```

Since `eA_s=G_s+U_s` and
`Q_ell=e^2F_ell-Corr(G_s,G_s;ell)`, expansion gives

```text
Q_ell=Corr(U,G)+Corr(G,U)+Corr(U,U)
       +e^2 sum_i delta_i C_ii.
```

Insert `G=1-B`.  Each mixed correlation contributes the constant
`sum_xU_s(x)` minus its support-head correlation, proving `(2.1)`.  No
owner-pair, `IS/IN/X` phase, or seam has been discarded; `(2.1)` is an
algebraic regrouping of their complete sum.  QED.

For `d>=2`, the accepted logarithmic ratio bounds give

```text
0<=u_d<=4/d.                                        (2.2)
```

For `d>=3`, log-convexity gives

```text
0<=delta_d<=C/d^2.                                  (2.3)
```

At `d=2`, `delta_2=-1`, but that owner has at most one generic phase, so its
autocorrelation vanishes at every nonzero lag.  Thus it contributes nothing
to any target derivative in `(1.1)`.

## 3. A sharp statewise inverse-owner variation theorem

For a circular sequence `f`, write
`TV_circ(f)=sum_ell|f(ell+1)-f(ell)|`.

### Proposition 3 (proved inverse-owner envelope)

There is an absolute constant `C` such that every supported triangle or
double satisfies

```text
sum_(ell=2)^(n-3)|Delta Q_ell(s)|
 <=C sum_(i:d_i>=2) 1/d_i.                          (3.1)
```

In particular, if all three residual owners have size at least `(k+1)/2`,
the left side is `O(1/k)` uniformly in `s`.

#### Proof

Each `chi_i` is a union of at most two circular intervals, so
`TV_circ(chi_i)<=4` and `||chi_i||_1<=d_i`.  From `(2.2)`,

```text
||U_s||_1<=12,
TV_circ(U_s)
 <=sum_i u_(d_i)TV_circ(chi_i)
 <=16 sum_(i:d_i>=2)1/d_i.                          (3.2)
```

Also `||B_s||_1<=4`.  Circular correlation satisfies

```text
TV_circ(Corr(f,g))
 <=min(||f||_1 TV_circ(g),TV_circ(f)||g||_1).        (3.3)
```

Use the second form, after reflection if necessary, on each of the two
`U/B` terms in `(2.1)`, and use either form on `Corr(U,U)`.  Equations
`(3.2)--(3.3)` bound their total variation by an absolute multiple of
`sum_i1/d_i`.

For the diagonal remainder, owners of size one have no generic phase and the
size-two derivative vanishes on the target range.  For `d_i>=3`,
`(2.3)` and

```text
TV_circ(Corr(chi_i,chi_i))
 <=||chi_i||_1 TV_circ(chi_i)<=4d_i
```

give an `O(1/d_i)` contribution.  Restricting the circular variation to
`2,...,n-3` can only decrease it.  This proves `(3.1)`.  QED.

This is strictly sharper than the accepted uniform statewise `O(1)` bound:
it supplies the full target factor whenever every owner is macroscopic.

## 4. Literal positive-composition coefficient law

Let the complete centered first-pair product coefficient from M261/M264 be

```text
omega_k(s)=a(s)[C_B(s)/A_B-C_A(s)/A_A],             (4.1)
```

so `eta(G)=sum_s omega_k(s)G(s)` and
`sum_s|omega_k(s)|<=2`.  This coefficient already combines the two live
source channels; `a(s)=3,2` retains every raw triangle/double lift.

For a positive cyclic composition `g`, anchor `r`, and the supported
products `s_T,s_S,s_N` of M285/M287, use the exact owner intervals

```text
T: I_1,I_2,I_3                       / g_1,g_2,g_3,
S: I_1,I_3,I_2 union I_4             / g_1,g_3,g_2+g_4,
N: I_2,I_4,I_1 union I_3             / g_2,g_4,g_1+g_3.
```

Let `mathcal D_K(g,ell)` be `(1.1)`, or equivalently the adjacent difference
of `(2.1)`, evaluated on these literal intervals and sizes.  Translation by
the support anchor cancels in every circular correlation, so the response
depends on `g,K,ell` but not on `r`.

### Proposition 4 (exact combined coefficient law)

For every target lag,

```text
eta(Delta Q_ell)
 =1/3 sum_(r mod n) sum_(g_1+g_2+g_3=n)
       omega_k(s_T(r,g)) mathcal D_T(g,ell)

  +1/4 sum_(r mod n) sum_(g_1+...+g_4=n) [
       omega_k(s_S(r,g)) mathcal D_S(g,ell)
      +omega_k(s_N(r,g)) mathcal D_N(g,ell)].        (4.2)
```

All compositions are positive.  Each supported forward triangle occurs
three times and each supported double occurs four times across `S/N`; there
is no additional factor `n`.  In `(4.2)`, channels are already recombined in
`omega_k`, the two outer kinds are added before the lag absolute value, and
every same-owner `IS/IN` and cross-owner `X` incidence remains in
`mathcal D_K`.

#### Proof

Apply the accepted three/four-to-one positive-composition parameterization
to `eta(Delta Q_ell)=sum_s omega_k(s)Delta Q_ell(s)`, then use Propositions
1--2 for the response.  QED.

## 5. Strict removal of the macroscopic-owner sector

Call a supported state **interior** if every residual owner has size at least
`(k+1)/2`, and **boundary** otherwise.  Decompose the right side of `(4.2)`
as `V_int(ell)+V_bd(ell)`, without separating channels or kinds.

Proposition 3 and `sum_s|omega_k(s)|<=2` prove

```text
sum_(ell=2)^(n-3)|V_int(ell)|=O(1/k).               (5.1)
```

Therefore DOR is equivalent to the strictly smaller positive-composition
obligation

> **Boundary owner-defect transport `(BODT)` (unresolved).**
>
> In `(4.2)`, restrict each `T/S/N` sum to states having a residual owner of
> size at most `(k-1)/2`, retain the complete combined signed coefficient,
> and prove
>
> ```text
> sum_(ell=2)^(n-3)|V_bd(ell)|=O(1/k).              (BODT)
> ```

Indeed `(BODT)` plus `(5.1)` proves DOR; conversely DOR and `(5.1)` imply
`(BODT)` by subtraction.  This removes the entire all-macroscopic-owner
sector at target scale.  The remaining boundary is explicit and falsifiable:
in the triangle row it means some `g_i<k/2`; in the two double rows it means
the corresponding one-run or two-run owner size is `<k/2`.

No absolute value has been inserted between channels, between `T/D`, or
between `IS/IN/X`; the only separately bounded block is the proven
target-scale interior vector.

## 6. Optional one-threshold route

Put `q_ell=eta(Q_ell)` and `d_ell=q_(ell+1)-q_ell`.  Symmetry of `rho` gives

```text
q_ell=q_(n-ell),
d_ell=-d_(n-ell-1),
d_((n-1)/2)=0.                                      (6.1)
```

The already-frozen exact rows at `k=5,7` motivate, but do not prove,

> **Decorated sign regularity `(DSR)` (unresolved).**  For odd `k>=5`,
>
> ```text
> d_ell<=0,  2<=ell<=k-2;
> d_ell>=0,  k-1<=ell<=(n-3)/2.                    (DSR)
> ```

(`k=3` is a finite exceptional rank and does not satisfy this formulation.)
Conditional on `(DSR)`, lower-half telescoping and `(6.1)` give exactly

```text
sum_(ell=2)^(n-3)|d_ell|
 =2[q_2+q_((n-1)/2)-2q_(k-1)].                     (6.2)
```

Thus, conditional on `(DSR)`, DOR is equivalent to the three-point estimate

```text
q_2+q_((n-1)/2)-2q_(k-1)=O(1/k).                  (DTR)
```

Both `(DSR)` and `(DTR)` are unresolved.  The sole predeclared finite
falsifier was an independent exact-symbolic `k=9` evaluation, including all
combined channels and kinds.  It certified

```text
d_ell<0 for ell=2,...,7,
d_ell>0 for ell=8,...,12,
d_13=0,
```

as well as exact reflection and equality of the full absolute sum with the
right side of `(6.2)`.  It found

```text
sum_(ell=2)^24 |d_ell| = 0.2784019538957808...,
9 sum_(ell=2)^24 |d_ell| = 2.5056175850620277....
```

Thus `(DSR)` survives `k=9`, but this remains exact finite-only and proves
neither `(DSR)`, `(DTR)`, nor `(BODT)` at general rank.

## 7. Exact stop

The proved advance is the defect-field identity, the inverse-owner
statewise theorem, the literal combined positive-composition coefficient
law, and target-scale removal of the all-macroscopic-owner sector.  The first
open lemma is `(BODT)`.  DOR, `(DSR)`, `(DTR)`, CIBV, SET, PBV, FD, FCL1,
every gap/mixing claim, and both Terminals remain unresolved.
