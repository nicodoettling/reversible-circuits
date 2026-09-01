# M282 exact CSBV support-pair coefficient reduction

Date: 2026-08-14 UTC.

Status: the identities in Sections 1--4 are **proved exact** by direct
disintegration of the frozen M272 law. Sections 6--9 prove `ACBV` and hence
`CSBV` with an absolute (not optimized) constant. This new proof requires a
fresh immutable audit. No CEBV or downstream claim is made.

## 1. Frozen interface

Use `(pq)(x)=p(q(x))`, `k>=3` odd,

```text
D=2k-1,       R=D-2=2k-3,       n=3k.
```

The B exterior cycle, in abstract cyclic coordinates, is `Z/DZ`; its
literal ambient embedding is

```text
lambda(t)=t+1       for 0<=t<=k-2,
lambda(t)=t+k+1     for k-1<=t<=D-1.
```

Let `p_s,q_s`, `gamma_L(s),gamma_F(s)` and `Phi_s^D` be exactly the frozen
M272/M276/M279 objects. Put

```text
h(r)=(r-1)(r-2)/(rR),
a_L(s)=1-gamma_L(s)=h(s)+h(D-s),
a_F(s)=1-gamma_F(s),
p_hat_s=p_s a_L(s),
q_hat_s=q_s a_F(s),
A_s=p_hat_s-q_hat_s,
W_s=A_s/a_L(s)=p_s-q_s a_F(s)/a_L(s),              (1.1)
```

where `q_s=0` outside `1<=s<k/2`. The exact endpoint is

```text
sum_(s=1)^(k-1) A_s
 =-6(k-1)/[k(2k-1)(2k-3)].                         (1.2)
```

Finite summation by parts, including `(1.2)`, gives the first key collapse:

```text
E_(k-1)Phi_(k-1)^D
 +sum_(u=1)^(k-2)E_u(Phi_u^D-Phi_(u+1)^D)
 =sum_(s=1)^(k-1) A_s Phi_s^D.                     (1.3)
```

Thus CSBV is one common-profile signed mixture, not an adjacent-profile
triangle estimate.

## 2. Literal disjoint-pair kernel

Write

```text
b_r=e^(-r)r^(r-1)/r!,
K_R(r,x)=b_x b_(r-x)/(R b_r),      1<=x<r.         (2.1)
```

Fix a first chord of smaller split `s` and rotate it to `{0,s}`. It cuts
the abstract D-cycle into consecutive cycles of sizes `s,D-s`, each with
one marked endpoint of the first chord. If the ordered second factor is in
the size-`r` component, its total disjoint mass is `h(r)`.

For `1<=x<=r-1`, define the following *unnormalized* coefficient at ordinary
linear separation `x`:

```text
F_r(x)=1[x<=r-2](r-x-1)K_R(r,x),
C_r(x)=4(r-1)/(rR)-2K_R(r,x),
U_r(x)=F_r(x)+C_r(x),                               (2.2)
```

and set these functions to zero outside their displayed domains.

Here `F_r` is the ordered second-edge endpoint pair. There are `r-1-x`
allowed chords at linear separation `x`, and the component-choice factor
turns their completion mass into `(r-x-1)K_R(r,x)`. The term `C_r` is the
four first/second cross pairs. For a nonmarked vertex at cyclic distance
`x` from its component mark, its raw endpoint intensity is

```text
(r-1)/R [2/r-nu_r(x)],
```

and the two first-chord marks give twice this amount. This is exactly the
second formula in `(2.2)`. Thus ordered factors, the two component choices,
both directions, phase, and every support collision are retained before
aggregation. Since the factors are disjoint, the product kind is literally
`D` throughout.

## 3. Abstract signed support-pair profile

For any disjoint product let `I_d` count ordered pairs of its four support
vertices at abstract circular displacement `d`. Rotational invariance makes
the starting phase uniform. Let `c_d` be the expectation of `I_d` under the
signed measure on the right of `(1.3)`. Directly separating the first-edge
pair, second-edge pair, and four cross pairs gives, for `1<=d<=D-1`,

```text
c_d=A_min(d,D-d)
 +sum_(r=1)^(D-1) W_min(r,D-r)[U_r(d)+U_r(D-d)].    (3.1)
```

In particular `c_d=c_(D-d)`. Formula `(3.1)` is a coefficient identity,
not an estimate and not a quotient by component-size or collision type.

## 4. Exact literal phase embedding

An oriented interval of `d` abstract edges crosses the long seam and the
wrap seam. For `1<=d<=k-1`, the four `(neither,wrap only,long only,both)`
counts are

```text
(D-2d,d,d,0),
```

whereas for `k<=d<=D-1` they are

```text
(0,D-d,D-d,2d-D).
```

The corresponding ambient displacement is respectively
`d,d+1,d+k,d+k+1`. Averaging over the `D` literal phases and using
`c_d=c_(D-d)` therefore gives the ambient signed collision profile `J_l`:

```text
c_0=c_k=0,

J_l=[(D-2l)c_l+(l-1)c_(l-1)]/D,       1<=l<=k,

J_l=[(l-k)c_(l-k)+(2k-l)c_(2k-l)]/D,
                                           k+1<=l<=2k-1,

J_(n-l)=J_l.                                           (4.1)
```

The CSBV vector is exactly

```text
(J_(ell+1)-J_ell)_(ell=2,...,n-3).                  (4.2)
```

No boundary term is hidden: `c_0=c_k=0` is only notation for the two absent
half-profile indices, while the nonzero Abel endpoint remains in every
`A_s` through `(1.1)--(1.3)`.

## 5. Reduction to one coefficient estimate

The formulas in `(4.1)` imply by direct adjacent subtraction that

```text
TV(J)<=C TV(c_0,c_1,...,c_(k-1),c_k)
       +(C/D)sum_(s=1)^(k-1)|c_s|.                 (5.1)
```

Moreover every `Phi_s^D` collision profile has total mass `12`, so

```text
sum_d |c_d|
 <=12 sum_s |A_s| <=24.                            (5.2)
```

Consequently CSBV follows from the single explicit coefficient lemma

> **ABSTRACT COEFFICIENT BOUNDED VARIATION (ACBV).**
>
> ```text
> sum_(s=0)^(k-1)|c_(s+1)-c_s|=O(1/k),
> ```
>
> where `c_0=c_k=0` and `c_s` is the literal coefficient `(3.1)`.

This is strictly narrower than CSBV: the literal phase embedding and its
`O(D^-1)` seam cost have already been discharged exactly. The next sections
prove ACBV.

## 6. Borel ratio facts

Put

```text
r_j=b_(j-1)/b_j=e(1-1/j)^(j-2),       j>=2.        (6.1)
```

The logarithmic series for `(6.1)` and Stirling's inequalities give
absolute constants throughout such that

```text
b_j asymp j^(-3/2),
|b_(j+1)-b_j|<=C b_j/j,
|r_j-1|<=C/j,
|r_(j+1)-r_j|<=C/j^2.                 (6.2)
```

For

```text
Q_r(d)=b_(r-d)/b_r=product_(i=0)^(d-1)r_(r-i),
```

`1<=d<=r/2` implies

```text
Q_r(d)<=C,
|Q_r(d)-1|<=Cd/r,
|Q_r(d+1)-Q_r(d)|<=C/r.               (6.3)
```

All statements include bounded indices after enlarging the same absolute
constant. These facts will be used only in finite sums.

## 7. Paired disjoint-kernel stabilization

Extend `U_r` by zero unless `1<=x<r`. Formula `(2.2)` simplifies, including
the boundary `x=r-1`, to

```text
U_r(x)=1/R [4(r-1)/r
            +(r-x-3)b_x b_(r-x)/b_r].              (7.1)
```

For `1<=r<=D-1`, define on the half-profile, with zero padding at `d=0,k`,

```text
Z_r(d)=U_r(d)+U_r(D-d),
B_r(d)=(r/R)b_d+4/R,             1<=d<=k-1.        (7.2)
```

### Lemma 1 (proved: one-component stabilization)

Uniformly in `k>=3` odd and `1<=r<=D-1`,

```text
TV_(d=0,...,k)[Z_r-B_r] <= C/R.                    (7.3)
```

#### Proof

The cases `r=1,2` are direct: `U_1` is empty and `U_2(1)=0`; the reference
has endpoint-inclusive variation `O(1/R)`.

Assume `r>=3`. On the active range `1<=d<r`, subtracting `B_r` from the
first term `U_r(d)` gives

```text
1/R [e_r(d)-4/r],

e_r(d)=b_d[(r-d-3)Q_r(d)-r].                       (7.4)
```

For `d<=r/2`, `(6.2)--(6.3)` imply

```text
|(r-d-3)Q_r(d)-r|<=C(d+1),
|Delta_d[(r-d-3)Q_r(d)-r]|<=C.
```

Therefore `|Delta e_r(d)|<=C b_d`, whose sum is bounded.

For `d>r/2`, put `a=r-d<r/2`. Then

```text
e_r(r-a)=(a-3)b_a b_(r-a)/b_r-rb_(r-a).           (7.5)
```

The first term in `(7.5)` has total variation `O(1)`: by `(6.2)--(6.3)`,
`|(a-3)b_a|<=C/sqrt(a)`, its adjacent difference is `O(a^-3/2)`, the ratio
`b_(r-a)/b_r` is bounded, and its adjacent difference is `O(1/r)`. The
resulting extra series is

```text
(1/r)sum_(a<=r/2)a^(-1/2)=O(r^-1/2).
```

The second term in `(7.5)` has adjacent differences summing to
`O(r^-1/2)`. Thus `e_r` has total variation `O(1)` over the entire active
range, including the midpoint junction.

On the inactive range `d>=r`, the difference from `B_r` is

```text
-1/R [r b_d+4].                                    (7.6)
```

Its internal variation is `O(1/R)`. At the `d=r-1/r` cutoff, both brackets
in `(7.4)` and `(7.6)` are `O(1)` (use `(7.5)` with `a=1` and
`rb_r=O(r^-1/2)`), so the cutoff costs `O(1/R)`. Zero padding at `d=0,k`
also costs `O(1/R)`.

It remains to include the reflected term `U_r(D-d)`. It is supported only
when `d>D-r`. There put

```text
a=r-(D-d)=d-(D-r).
```

Because `d<=k-1` and `D=2k-1`, every active `a` satisfies `a<r/2`.
Equation `(7.1)` becomes

```text
U_r(D-d)=1/R [4(r-1)/r
              +(a-3)b_a b_(r-a)/b_r].             (7.7)
```

The same first-half estimate used for `(7.5)` gives bracket variation
`O(1)`. Its two support endpoints are also `O(1)`, so zero padding makes
the complete reflected variation `O(1/R)`. Combining `(7.4)--(7.7)` proves
`(7.3)`. QED.

For a conditioned first split `s`, the complete paired unnormalized kernel
in `(3.1)` is

```text
V_s=Z_s+Z_(D-s).
```

Define the `s`-independent half-profile, again zero at `0,k`,

```text
B(d)=(D/R)b_d+8/R,                1<=d<=k-1.       (7.8)
```

Since `s+(D-s)=D`, Lemma 1 gives exactly

```text
TV(V_s-B)<=C/R.                                    (7.9)
```

Also `TV(B)<=C`: `b_d` is decreasing and summable, while the constant term
has only its two zero-padding jumps. This proves the required uniform
stabilization without any adjacent-`Phi` or CDV norm.

## 8. Signed weights and the first-edge coefficient

The exact normalizer ratio is

```text
delta_s:=a_F(s)/a_L(s)-1
 =2(k-1)/[R(k-s)(D-s)a_L(s)],       1<=s<k/2.      (8.1)
```

Here `a_L(s)>=1/2`, and direct denominator bounds give the accepted uniform
inequality

```text
0<=delta_s<=16/(3k^2).                             (8.2)
```

Since `sum p_s=sum q_s=1`, equations `(1.1)` and `(8.1)` give the exact
cancellation

```text
sum_s W_s
 =sum_s p_s-sum_s q_s(1+delta_s)
 =-sum_s q_s delta_s,                              (8.3)
```

and therefore

```text
|sum_s W_s|<=16/(3k^2),
sum_s|W_s|<=sum_s p_s+sum_s q_s(1+delta_s)<=3.     (8.4)
```

The bound in `(8.3)` is exact and uniform, not an asymptotic expansion.

### Lemma 2 (proved: first-edge half-BV)

With `A_0=A_k=0`,

```text
sum_(s=0)^(k-1)|A_(s+1)-A_s|<=C/k.                (8.5)
```

#### Proof

The exact split laws are

```text
p_s=[D/(D-1)]b_s b_(D-s)/b_D,
q_s=[k/(k-1)]b_s b_(k-s)/b_k.                     (8.6)
```

Put `j=(k-1)/2`. For `1<=s<=j`, write `A_s=b_s H_k(s)`. Substitution of
`(8.6)` and the explicit rational formulas for `a_L,a_F` gives

```text
H_k(s)=[D/(D-1)]Q_D(s)a_L(s)
       -[k/(k-1)]Q_k(s)a_F(s).                    (8.7)
```

The product bounds `(6.3)`, the prefactor differences, and

```text
a_L(s)=[D-6+2/s+2/(D-s)]/R,
a_F(s)=[D-6+2/s+2/(k-s)]/R                        (8.8)
```

give, uniformly through `s=j`,

```text
|H_k(s)|<=Cs/k,
|H_k(s+1)-H_k(s)|<=C/k.                           (8.9)
```

Indeed each ratio product is bounded; its adjacent increment is `O(1/k)`,
the two products differ by `O(s/k)`, and the rational factors in `(8.8)`
have adjacent increments `O(1/(ks^2)+1/k^3)`. Combining `(8.9)` with
`|Delta b_s|<=Cb_s/s` yields

```text
|A_(s+1)-A_s|<=Cb_s/k                              (8.10)
```

on the low range, whose sum is `O(1/k)`.

For `j<s<=k-1`, `q_s=0`. Both `s` and `D-s` are comparable to `k`, so
Stirling and the exact adjacent ratio in `(8.6)` give

```text
p_s<=Ck^(-3/2),
|p_(s+1)-p_s|<=Ck^(-5/2).                         (8.11)
```

Formula `(8.8)` gives `a_L(s)=O(1)` and
`|Delta a_L(s)|=O(k^-3)` there. Hence the bulk contributes
`O(k^-3/2)` variation. At the `j/j+1` junction, both neighboring values are
`O(k^-3/2)`. Finally `A_1=O(1/k)` closes against `A_0=0`, and
`A_(k-1)=O(k^-3/2)` closes against `A_k=0`. The same inequalities include
`k=3` after enlarging the absolute constant; no asymptotic threshold is
used. This proves `(8.5)`. QED.

For completeness, `(8.5)`, the uniform full-range bound `a_L>=2/9`
(equality at `k=3,s=2`), and the exact adjacent difference from `(8.8)`
also give

```text
TV(0,W_1,...,W_(k-1),0)=O(1/k).                   (8.12)
```

This diagnostic bound is not used as a BV-nonexpansive surrogate for the
kernel proof.

## 9. ACBV and CSBV

Let

```text
M(d)=sum_(s=1)^(k-1)W_s V_s(d),       0<=d<=k.
```

Using `(8.3)` *before* taking any norm,

```text
M=(sum_s W_s)B+sum_s W_s(V_s-B).                   (9.1)
```

Equations `(7.9)`, `(8.4)`, and `TV(B)<=C` now imply

```text
TV(M)
 <=|sum_sW_s|TV(B)+sum_s|W_s|TV(V_s-B)
 <=C/k^2+C/R
 <=C/k.                                             (9.2)
```

This is the required coefficient-level signed cancellation. It neither
norms adjacent conditional profiles nor invokes the refuted CDV route.

On the half-profile, `(3.1)` is exactly

```text
c_s=A_s+M(s).
```

Lemmas 1--2 and `(9.2)` prove

```text
TV(0,c_1,...,c_(k-1),0)<=C/k,                      (9.3)
```

which is ACBV. Combining `(9.3)`, `(5.1)`, `(5.2)`, and `D=2k-1` proves:

### Theorem (proved: CSBV)

There is an absolute, non-optimized constant `C` such that for every odd
`k>=3`, retaining all literal lag, phase, ordered-factor, disjoint-kind, and
support-collision coordinates,

```text
|| E_(k-1)Phi_(k-1)^D
   +sum_(u=1)^(k-2)E_u(Phi_u^D-Phi_(u+1)^D) ||_1
 <=C/k,                                             (9.4)
```

where

```text
E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)].
```

The norm in `(9.4)` is taken only after the exact coefficient collapse and
the signed common-profile cancellation `(9.1)`.

## 10. Finite falsification only

After all formulas above were fixed, `coefficient_probe.py` evaluated them
with exact rational arithmetic at `k=3,5,7,9,15,31`. Its embedded CSBV norms
at `k=3,5,7` reproduce M272's independent values exactly; in particular
`k||CSBV||_1` is respectively approximately

```text
0.960000, 0.854298, 0.964216.
```

The observed `k TV(c)` stays between about `1.45` and `1.56` from `k=7`
through `31`. In contrast, `R` times the maximum raw paired-kernel variation
grows from `9.0` to `64.34`. This is finite evidence against the raw-row
shortcut, not an asymptotic proof. The analytic reason the shortcut fails is
already explicit in `(7.8)--(7.9)`: the raw row contains the common profile
`B`, whose endpoint-inclusive variation is
`2(D/R)b_1+16/R`, while only `V_s-B` is `O(1/R)`. Lemma 1 subtracts this
common profile before applying the signed identity `(8.3)`.

These rows are exact finite falsification/reproducibility evidence only.
The all-rank proof is Sections 6--9.
