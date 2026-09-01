# M180 boundary-charge reduction for the fixed-cell response

Date: 2026-08-13 UTC.

Status: Propositions 1--4 are **proved**.  The final one-dimensional
small-component coefficient estimate `(SCBR)` is **unresolved**.  Hence
M174's `(BR)` and PCS-bound remain unresolved.

## 1. Exact setting

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  Put `n=3k`, odd `k>=3`,

```text
h=(0 1 ... n-1),
A=(0,k,2k),                       B=(0,1)(k,2k).
```

The target is the uniform law on minimal length-`n-1` transposition
factorizations of `h`, and the kernel is M73's nonlazy cyclic rank-two
coordinate kernel.  This is not the global identity-word law or the lazy
`{3,4,5}` heat-bath chain.

Let

```text
eta=P_B-P_A
```

be M91's complete signed first-row law.  It already combines the normalized
`J=1,2` channels; its `J=0` measure cancels.  For an intermediate `s`, let
the three cycles of `q=s^-1h` have sizes `d_i` and ambient run types one or
two.  M174/M178 proved

```text
e^2 R_n f(s)=n^2+L_kind n+B_k(s),
R_n=(n-3)(n-4),                  L_T=0, L_D=-2,       (1.1)
```

and reduced PCS-bound to

```text
(BR)       eta(B_k)=O(1).                            (1.2)
```

All statements below retain the triangle/double kind, the unique two-run
component of every double, and every unit-run collision indicator.

## 2. Sharper Cayley-ratio centers

For a one-run component, M174's exact decorations are

```text
U_1(d)=(d-1)tau(d-1)/tau(d),
V_1(d)=(d-2)(d-3)tau(d-2)/tau(d),

u_1(d)=eU_1(d)-d-1/2,
v_1(d)=e^2V_1(d)-d^2+2d.                             (2.1)
```

For a positive two-run component with run lengths `a,b`, `d=a+b`, put

```text
I(a,b)=1[a=1]+1[b=1]
```

and retain

```text
U_2(a,b)=(d-2)tau(d-1)/tau(d),
V_2(a,b)=(d^2-7d+14-2I(a,b))tau(d-2)/tau(d),

u_2(d)=eU_2(a,b)-d+1/2,
v_2(a,b)=e^2V_2(a,b)-d^2+4d.                         (2.2)
```

The `U_2` residual depends only on `d`; only `V_2` sees the unit-run
indicator.

### Proposition 1 (proved: uniform sharp centers)

Uniformly over valid positive sizes,

```text
u_1(d)=  7/(24d)+O(d^-2),
u_2(d)=-29/(24d)+O(d^-2),                            (2.3)

v_1(d)=-5/3+O(d^-1),
v_2(a,b)=1/3-2I(a,b)+O(d^-1).                        (2.4)
```

The constants hidden in `O(.)` are absolute and the last estimate is
uniform over all positive splits `a+b=d`.

#### Proof

Factorial cancellation gives, for `d>=2`,

```text
A_d:=tau(d-1)/tau(d)=(1-1/d)^(d-2).
```

Taylor expansion of `log(1-x)`, with the geometric bound on its remainder,
gives uniformly

```text
log(e A_d)=3/(2d)+2/(3d^2)+O(d^-3),
e A_d=1+3/(2d)+43/(24d^2)+O(d^-3).                  (2.5)
```

Multiplication by `d-1` and `d-2` proves (2.3).  Similarly, for `d>=4`,

```text
B_d:=tau(d-2)/tau(d)
    =(1-1/d)(1-2/d)^(d-3).
```

Here the cubic logarithm term must be retained because it is multiplied by
`d-3`.  The correct expansion is

```text
log(e^2 B_d)=3/d+17/(6d^2)+O(d^-3),
e^2B_d=1+3/d+22/(3d^2)+O(d^-3).                     (2.6)
```

Thus

```text
(d^2-5d+6)e^2B_d=d^2-2d-5/3+O(d^-1),

(d^2-7d+14-2I)e^2B_d
   =d^2-4d+1/3-2I+O(d^-1),                          (2.7)
```

uniformly because `0<=I<=2`.  This proves (2.4).  The finitely many invalid
shifted-subscript cases use M174's zero convention and are absorbed into the
same absolute constants.  QED.

The coefficient `22/3` in (2.6) is material.  Truncating the logarithm one
term too early gives a wrong constant response.  Equations (2.3)--(2.4), not
that transient calculation, control the rest of this note.

## 3. Exact boundary-charge decomposition

For component `i`, put

```text
(epsilon_i,c_i)=(1/2,2)     for one run,
(epsilon_i,c_i)=(-1/2,4)    for two runs,
```

and write `u_i,v_i` for (2.1)--(2.2).  Define the additive centered charge

```text
Q(s)=sum_(i=1)^3 u_i.                                (3.1)
```

If `s` is a double, let `I_D(s)` be the `I(a,b)` of its unique two-run
component; put `I_D(s)=0` for a triangle.

### Proposition 2 (proved: all unbounded response lies in one charge)

There is an explicit remainder `R(s)` such that, exactly,

```text
B_k(s)=2nQ(s)-7/2-2I_D(s)+R(s),                      (3.2)
```

and

```text
sup_(n,s)|R(s)|<infinity.                            (3.3)
```

Consequently

```text
(BR)  eta(B_k)=O(1)
       iff n eta(Q)=O(1).                            (3.4)
```

#### Proof

M174's exact response can be regrouped as

```text
B_k(s)=sum_i v_i+2sum_(i<j)epsilon_i epsilon_j
 +2sum_j(n-d_j)u_j
 +2sum_(i<j)(epsilon_i u_j+epsilon_j u_i+u_i u_j).   (3.5)
```

Indeed, the omitted deterministic linear expression is exactly zero by the
already-audited affine identities `L_T=0,L_D=-2`.

For a triangle, the constant part of the first line is

```text
3(-5/3)+2*3*(1/2)^2=-7/2.
```

For a double, two one-run constants, the two-run constant, and the epsilon
pair sum give

```text
2(-5/3)+(1/3-2I)
 +2[(1/2)(1/2)+2(1/2)(-1/2)]
=-7/2-2I.                                            (3.6)
```

Define

```text
w_i=v_i+5/3                         (one run),
w_i=v_i-1/3+2I_D(s)                 (two runs),

R(s)=sum_i w_i-2sum_i d_i u_i
 +2sum_(i<j)(epsilon_i u_j+epsilon_j u_i+u_i u_j).   (3.7)
```

Substitution in (3.5) proves (3.2).  Proposition 1 gives
`|u_i|<=C/d_i`, `|w_i|<=C/d_i`; hence every `d_i u_i`, epsilon term, and
product in (3.7) is bounded.  There are only three components, proving
(3.3).

The signed measure `eta` has total mass zero and total variation norm at
most two.  Also `0<=I_D<=2`.  Applying `eta` to (3.2) therefore differs
from `2n eta(Q)` by an absolute bounded amount, proving both directions of
(3.4).  No channelwise absolute value is used.  QED.

This proves that collision indicators and the full second-order
Cayley-ratio response are already harmless for `(BR)`.  The only possible
growth is the signed expectation of the additive first-boundary charge.

## 4. One-dimensional signed component coefficient

Retain M94's exact critical-Borel notation

```text
beta_3(s)=product_(C cycle of s^-1h)b_|C|,
beta_5(g,s)=1[ell_T((gs)^-1h)=n-5]
              product_(C cycle of (gs)^-1h)b_|C|,

delta_k(s)=beta_5(B,s)/beta_3(B)-beta_5(A,s)/beta_3(A),
R_n=(n-3)(n-4).                                      (4.1)
```

For a supported intermediate `s`, let `N_r(d;s)` be the number of residual
components of size `d` and ambient run type `r in {1,2}`.  Define the exact
channel- and kind-combined signed coefficients

```text
M_(r,k)(d)=1/R_n sum_(s in X_n)
                 a(s) delta_k(s) N_r(d;s).            (4.2)
```

Here `a(s)=3` for a triangle and `2` for a double.  Equation (4.2) sums the
complete source contrast before projection; it is equivalently the
`alpha_1,alpha_2` channel sum from M91.  No absolute value occurs in it.

### Proposition 3 (proved: exact one-dimensional reduction and tail)

One has

```text
eta(Q)=sum_(d=1)^(n-2)
 [M_(1,k)(d)u_1(d)+M_(2,k)(d)u_2(d)].                (4.3)
```

Writing

```text
t_k=eta(T)=12(k-1)/[3k(3k-4)(2k-1)],                (4.4)
```

the coefficients satisfy the exact moment cancellations

```text
sum_d M_(1,k)(d)= t_k,
sum_d M_(2,k)(d)=-t_k,
sum_d d[M_(1,k)(d)+M_(2,k)(d)]=0.                   (4.5)
```

Moreover,

```text
sum_(d>n/2)
 |M_(1,k)(d)u_1(d)+M_(2,k)(d)u_2(d)|=O(1/n).         (4.6)
```

Therefore `(BR)` is equivalent to the strictly one-dimensional statement

> **SMALL-COMPONENT BOUNDARY RESPONSE `(SCBR)` (unresolved).** Uniformly
> over odd `k>=3`,
>
> ```text
> |sum_(1<=d<=n/2)
>   [M_(1,k)(d)u_1(d)+M_(2,k)(d)u_2(d)]|=O(1/n).     (SCBR)
> ```

A stronger sufficient, directly falsifiable form is obtained by putting an
absolute value around each already type- and channel-combined size
coefficient before summing.

#### Proof

Equation (4.3) is Fubini's theorem applied to (3.1) and the exact raw signed
row (4.2).  Every triangle has three one-run components; every double has
two one-run and one two-run component.  Since `eta(D)=-eta(T)`, this gives
the first two identities in (4.5).  Every residual has total size `n`, and
`eta(1)=0`, proving the size moment.

For either source probability law, the residual has exactly three
components.  Hence

```text
sum_(r,d)|M_(r,k)(d)|<=6.                            (4.7)
```

Proposition 1 gives `|u_r(d)|<=C/d`.  On `d>n/2`, equations (4.7) and this
bound prove (4.6).  Combine (3.4), (4.3), and (4.6) to obtain the equivalence
with `(SCBR)`.  QED.

The first asymptotic part of the coefficient is explicitly

```text
M_1(d)u_1(d)+M_2(d)u_2(d)
 =[7M_1(d)-29M_2(d)]/(24d)
  +O((|M_1(d)|+|M_2(d)|)/d^2).                      (4.8)
```

Thus `(SCBR)` is a signed small-component transfer estimate, not a generic
covariance inequality.  It retains all collision and kind information in
the coefficients `M_r` before estimating.

## 5. Equivalent single boundary-incidence observable

Let `E_n={(r,r+1):r mod n}` be the polygon boundary transpositions.  For a
rank-two state `t`, let

```text
L(t)={(a,b): a,b transpositions, ab=t},

W(t)=1/a(t) sum_((a,b) in L(t))
                 [1[a in E_n]+1[b in E_n]].          (5.1)
```

Thus `0<=W<=2`, and `W` is invariant under cyclic conjugation.  For a
double, it is simply the number of its two edges lying in `E_n`; for a
triangle it is the ordered-lift average of the same count.

Put

```text
H(s)=sum_i U_i.                                      (5.2)
```

### Proposition 4 (proved: bounded-observable form)

For every supported `s`,

```text
(bar K W)(s)=2H(s)/(n-3).                            (5.3)
```

Furthermore,

```text
eta(Q)=e eta(H)-t_k,                                 (5.4)
```

and `(BR)` is equivalent to the single scalar predictive estimate

> **BOUNDARY-INCIDENCE RESPONSE `(BIR)` (unresolved).**
>
> ```text
> |(bar K^2W)(B)-(bar K^2W)(A)|=O(n^-2).             (BIR)
> ```

#### Proof

Conditional on a rank-two product `t`, all `a(t)` ordered lifts have the
same remaining completion count.  Hence `(bar K W)(s)` is the expected
number of boundary transpositions among the next two ordered factors in a
uniform minimal factorization of `s^-1h`.

A boundary edge can be the next minimal factor exactly when it is generic
for `s`.  In a component of size `d`, each such edge isolates a singleton,
so its completion ratio is

```text
1/(n-3) * tau(d-1)/tau(d).
```

Summing its `g_i` generic edges gives `H(s)/(n-3)` for one factor.  The two
factor positions have the same marginal (equivalently, the transposition
class sum is central), proving (5.3).

By definition, `Q=eH-n-sum_i epsilon_i`.  The signed mass of the constant
`n` vanishes.  The epsilon sum is `3/2` on a triangle and `1/2` on a double,
so its signed expectation is exactly `t_k`.  This proves (5.4).

Finally `eta=(delta_B-delta_A)bar K`.  Therefore

```text
eta(H)=(n-3)/2 [(bar K^2W)(B)-(bar K^2W)(A)].         (5.5)
```

Since `t_k=O(n^-2)`, equations (3.4), (5.4), and (5.5) prove the claimed
equivalence.  QED.

The bounded observable in `(BIR)` is much narrower than a two-step total-
variation theorem.  It is nevertheless unproved; boundedness of `W` alone
only gives a constant, not the required `n^-2` predictive difference.

## 6. Exact finite calibration and scope

`boundary_charge_check.py` reconstructs both source laws from literal
ordered transpositions and checks every identity above as a polynomial in a
formal variable `E`, later evaluated at `E=e`.  It is capped at exact
`k=3,5`.  The channel-combined finite values are

```text
k       n eta(H)       n eta(Q)       n sum_d |combined size charge|
3       2.0725360      4.6737370      7.4808092
5       1.4820926      3.5438970      5.2546970
```

The same run reproduces M174's `eta(B_k)` values
`5.3716368,5.5840961`.  These are exact-formula calibrations only.  They do
not prove `(SCBR)`, `(BIR)`, a limit, a sign, or a uniform bound.

This mission does not address FD-bound, FCL1 beyond the inherited PCS
implication, direct L1, H0, a spectral gap, the original identity heat-bath
chain, mixing, or either Terminal.
