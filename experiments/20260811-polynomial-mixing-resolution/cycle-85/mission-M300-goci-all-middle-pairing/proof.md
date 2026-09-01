# M300 all-middle channel-one coefficient reduction

Date: 2026-08-14 UTC.

Status: the identities and exterior Hahn/Abel reduction below are **proved**.
The universal middle cut-length phase inequality `(MCLP_1)` and hence
`(GOCI_1)` remain **unresolved**. The sole `k=7` calculation is **exact
finite evidence only**.

## 1. Scope, convention, and accepted response

Use `(pq)(x)=p(q(x))`, with displayed factors multiplied left-to-right.
Fix odd `k>=3`, put `n=3k`, and take `2<=ell<=n-2`. Write

```text
h=(0,1,...,n-1),
L=(1,...,k-1,2k,...,3k-1),       M=(k,...,2k-1),
C_-=(0,...,k-1),                 C_+=(2k,...,3k-1).
```

This is only the first separated fixed cell of the auxiliary uniform
minimal-factorization law of the long cycle under the nonlazy cyclic
rank-two quotient kernel. It is not the global identity-word law and not the
lazy exact same-product `{3,4,5}` heat-bath chain.

For a directed `d`-cycle `C`, a chord with directed cut size `c` has law

```text
nu_C(e)=v_d(c),
v_d(c)=tau(c)tau(d-c)/[(d-1)tau(d)],
tau(d)=d^(d-2)/(d-1)!,       tau(1)=1.              (1.1)
```

For a supported double `s`, the accepted literal owner response is

```text
F_ell(s)=sum_(a,b) kappa_ab(s) C_ab^s(ell).          (1.2)
```

At admissible lags it also equals the repaired nonnegative
owner-autocorrelation formula

```text
F_ell(s)=sum_x A_s(x)A_s(x+ell)
 +sum_(i:d_i>=3) delta_(d_i)C_ii^s(ell).             (1.3)
```

No statewise positivity in `(1.3)` is pushed through a signed source law.

## 2. Designated channel-one disintegration

Define, with absent chord-law terms equal to zero,

```text
gamma_k(e)=nu_L(e)
 -1/2 1[e in T(C_-)]nu_(C_-)(e)
 -1/2 1[e in T(C_+)]nu_(C_+)(e).                    (2.1)
```

The normalized merged channel-one law draws one chord from `L` and one
independent chord from `M`. The normalized split law first chooses `C_-` or
`C_+` fairly, then draws its chord and an independent `M` chord. Therefore,
for every test function `G`, direct expansion gives

```text
eta_1(G)
 =sum_(f in T(M))nu_M(f) sum_e gamma_k(e)G(ef),
sum_e gamma_k(e)=1-1/2-1/2=0.                       (2.2)
```

Taking `G=F_ell` proves the required disintegration.

Every displayed `e` is exterior and every `f` is middle, so their vertex
supports are disjoint. The double `ef` recovers its unique exterior and
middle cycles. In this designated decomposition one may write

```text
beta_1(ef)=gamma_k(e)nu_M(f).                        (2.3)
```

Equation `(2.3)` is not an unrestricted ordered-lift formula. A double has
two raw ordered transposition lifts, and channel one has already
conditioned/summed its two commuting color orders. The atom-summed identity
`(2.2)` remains valid even without shorthand `(2.3)`.

## 3. Exact middle cut-length partition

Write `m_a=k+a` for `a in Z/kZ`. Since `k` is odd, each unordered middle
chord occurs exactly once as

```text
f_(a,u)={m_a,m_(a+u)},        1<=u<k/2.              (3.1)
```

All `k` phases in one class have the same positive mass

```text
w_(k,u)=v_k(u)=tau(u)tau(k-u)/[(k-1)tau(k)],
sum_(1<=u<k/2) k w_(k,u)=1.                          (3.2)
```

Define the fixed-middle signed cell and its complete phase orbit by

```text
S_(k,ell)(a,u)=sum_e gamma_k(e)F_ell(e f_(a,u)),
P_(k,ell)(u)=sum_(a in Z/kZ)S_(k,ell)(a,u).           (3.3)
```

Substituting the unique partition `(3.1)` into `(2.2)` gives exactly

```text
eta_1(F_ell)
 =sum_(1<=u<k/2) w_(k,u)P_(k,ell)(u).                (3.4)
```

The frozen candidate is

```text
(MCLP_1)  P_(k,ell)(u)>=0                            (3.5)
```

for every allowed `(k,u,ell)`. Every weight in `(3.4)` is positive, so
`(MCLP_1)` would prove `(GOCI_1)`. It is weaker than the refuted
fixed-middle candidate because it retains cancellation across all `k`
middle phases. Symmetry of the owner matrix gives statewise
`F_ell=F_(n-ell)`, hence

```text
P_(k,ell)(u)=P_(k,n-ell)(u).                         (3.6)
```

Both lag endpoints remain present.

## 4. Complete exterior Hahn support

Put `D=2k-1`, `A={1,...,k-1}`, and
`P={2k,...,3k-1}`. The cycle `L` consists of the two contiguous blocks
`A,P`. Its chords split into those internal to one block and those crossing
from `A` to `P`. The split side additionally has the seam chords `{0,i}`
with `i in A`.

The signs of every nonzero `gamma_k(e)` are exact:

```text
e in A x P:               gamma_k(e)=v_D(c)>0,
e={0,c}, 1<=c<=k-1:       gamma_k(e)=-v_k(c)/2<0,
e internal to A or P:     gamma_k(e)=v_D(c)-v_k(c)/2<0.      (4.1)
```

Here `c` is the canonical `L`-cycle separation for the first and third
rows, and the `C_-` separation for the seam row. To prove the last strict
sign, put `r_d=tau(d-1)/tau(d)`. Accepted log-convexity of `tau` says
`r_d` strictly decreases with `d`. For `1<=c<=k-1`,

```text
2v_D(c)/v_k(c)
 =[tau(D-c)/tau(D)]/[tau(k-c)/tau(k)]
 =product_(j=0)^(c-1) r_(D-j)/r_(k-j) < 1.           (4.2)
```

Thus `(4.1)` is the complete Hahn decomposition, not merely two witness
atoms. There are

```text
|A x P|=k(k-1)
```

positive chords and

```text
binom(k-1,2)+binom(k,2)+(k-1)=k(k-1)
```

negative chords. Their cardinalities agree, but their individual masses do
not. Their total positive and negative masses agree because `sum gamma=0`.

## 5. All-middle exterior Hahn--Abel identity

Fix `(k,u,ell)` and abbreviate the fully middle-phase response as

```text
G(e)=sum_(a in Z/kZ)F_ell(e f_(a,u)).                (5.1)
```

For each canonical `L` cut size `1<=c<=k-1`, let `X_c` be the cross chords
of cut `c` and `J_c` the internal `L` chords of cut `c`. Because the two
blocks have lengths `k-1,k`,

```text
|X_c|=2c,             |J_c|=D-2c.                  (5.2)
```

Let `z_c={0,c}` be the seam chord and put

```text
q_c=v_k(c)/2-v_D(c)>0,
x_c=2c v_D(c),
y_c=(D-2c)q_c+v_k(c)/2
   =(k-c)v_k(c)-(D-2c)v_D(c)>0,                     (5.3)

Xbar_c=(1/(2c)) sum_(e in X_c)G(e),
Ybar_c=[q_c sum_(e in J_c)G(e)+(v_k(c)/2)G(z_c)]/y_c.
```

The complete Hahn support `(4.1)` gives

```text
P_(k,ell)(u)=sum_(c=1)^(k-1)[x_c Xbar_c-y_c Ybar_c].         (5.4)
```

This already compresses all `k(k-1)` positive and `k(k-1)` negative edge
responses to `2(k-1)` scalar cut means, after retaining every middle phase.

For the exact Abel form, set

```text
r_c=x_c-y_c=Dv_D(c)-(k-c)v_k(c),
R_c=sum_(d=1)^c r_d.                                      (5.5)
```

There are `D` chords of each canonical cut in the odd `D`-cycle, so
`sum_c Dv_D(c)=1`. Pairing `c` with `k-c` in the `k`-cycle gives
`sum_c(k-c)v_k(c)=1`. Hence `R_(k-1)=0`, and summation by parts in `(5.4)`
proves the exact all-middle exterior Hahn--Abel identity

```text
P_(k,ell)(u)
 =sum_(c=1)^(k-1)y_c(Xbar_c-Ybar_c)
  +sum_(c=1)^(k-2)R_c(Xbar_c-Xbar_(c+1)).            (EHA_1)
```

No term on the right is assigned a sign. In particular, `(EHA_1)` is not
the refuted conditioned MON/FOSD route: every `Xbar,Ybar` already contains
the complete middle phase orbit, and the identity asks for one combined
scalar inequality rather than pathwise or distributional order.

## 6. Why the all-rank proof does not yet close

The Hahn classification aligns the desired sign with cross-exterior chords,
which give nested doubles, versus internal/seam chords, which give separated
doubles. But the rooted owner sizes and interval overlaps change with the
exterior phase. Neither `(1.3)` nor `sum_e gamma(e)=0` compares the two
normalized Hahn laws.

Moreover, the Abel coefficients `R_c` are not one-signed even at the sole
tested rank. At `k=7`, all `r_c,R_c` have common denominator
`2316987672506143`, and their numerators are

| `c` | `r_c` numerator | `R_c` numerator |
|---:|---:|---:|
| 1 | -31342492105056 | -31342492105056 |
| 2 | 5122508240882 | -26219983864174 |
| 3 | 12627195649920 | -13592788214254 |
| 4 | 13706402092560 | 113613878306 |
| 5 | 9418371268750 | 9531985147056 |
| 6 | -9531985147056 | 0 |

Thus a proof cannot simply attach one common direction to every successive
cut response in the second block. This mixed coefficient fact does not
refute `(MCLP_1)`; it identifies the first remaining inequality as the
literal combined right side of `(EHA_1)`.

## 7. Sole exact rank `k=7`

The predeclared checker uses standard-library `Fraction` arithmetic and
imports no predecessor code or data. It evaluates all

```text
3 cut classes x 18 admissible lags = 54 class cells,
3 cut classes x 7 phases x 18 lags = 378 fixed-middle cells.
```

Every class cell is strictly positive. The minimum occurs at `u=2` and the
reflected lags `ell=6,15`:

```text
18391884160007872512505581390057340062886183764340384475832641580678550316483694546164031922299480179423171
/181211325370827177616731812976270118138716435331141156018616780003928170444373248989640785920000000000000000
approximately 0.1014941208689418.                         (7.1)
```

Nevertheless, 44 of 378 fixed-middle cells are negative. Their minimum is
at `u=2`, phase `6`, `f=(8,13)`, and reflected lags `ell=8,13`:

```text
-47887190399462218030782332438763438434346238035631961416543569973932853169
/920408972596550617862664784704103676980180079269295528017920000000000000000
approximately -0.05202816554946053.                        (7.2)
```

Thus the new grouping retains essential middle-phase cancellation. Every
fully weighted `eta_1(F_ell)` is positive at `k=7`; the smallest is at
`ell=8,13`, approximately `0.02016735366799382`. This is not an all-rank
GOCI proof.

The checker verifies exact chord-law and gamma normalization; unique middle
class partition; literal equals repaired response at all admissible lags;
statewise, classwise, and full reflection; and direct full average equals
the cut-class reconstruction.

## 8. Exact stop and first unresolved lemma

The first standalone unproved statement is:

> **All-middle exterior Hahn--Abel inequality.** For every odd `k>=3`,
> `1<=u<k/2`, and `2<=ell<=3k-2`, the combined right side of `(EHA_1)` is
> nonnegative, with `G`, `Xbar`, and `Ybar` defined by `(5.1)--(5.3)`.

This statement is exactly `(MCLP_1)` under the proved identity, and it would
imply `(GOCI_1)` by `(3.4)`. It remains unresolved. Channel two does not have
the independent exterior/middle product factorization `(2.2)`; its
triangle/double and full two-factor completion law require a different
argument, so no `GOCI_2` statement is made here.

No CP, OS+, MS, FCL1, later-cell, direct-L1/H0, spectral-gap, mixing, or
Terminal conclusion follows. Main-chain exceptional cases `m` odd, `m=0`,
`m=2`, and `N=2` are not implicated by this auxiliary-cell calculation.
