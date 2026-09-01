# M258 two-run adjacent-variation theorem

Date: 2026-08-14 UTC.

Status: **proved**, subject to a fresh independent audit. This proves only
the literal B-side two-run statement `(TAV)` below. It makes no inference
about full DV, conditional J2, WPCR, SCBR, response, a spectral gap, mixing,
or either Terminal.

## 1. Exact target and decomposition

The target in this mission is the normalized literal ordered-disjoint-double
B profile under the uniform minimal-factorization law, not the global bridge
law. Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, odd `k>=3`, and

```text
D=2k-1,       R=2k-3,       2<=ell<=(3k-1)/2,
b_t=e^-t t^(t-1)/t!,
K(r,t)=b_t b_(r-t)/(R b_r),
h(r)=(r-1)(r-2)/(rR),
H_s=h(s)+h(D-s).
```

For `f:{1,...,D-2}->R`, define the reversed symmetric Borel operator

```text
Wtilde_r(f)=sum_(t=2)^(r-1)(t-1)K(r,t)f(t),         (1.1)
Ltilde_s(f)=[Wtilde_s(f)+Wtilde_(D-s)(f)]/H_s.      (1.2)
```

Empty sums are zero. Kernel symmetry and the rooted-tree convolution give

```text
Wtilde_r(1)=h(r),       Ltilde_s(1)=1.              (1.3)
```

Thus adjacent responses of `Ltilde` annihilate constants exactly.

From `tav_cyclic_coefficient.md`, put

```text
Q_ell(t)=D^-1{
 (D-2t)1{t<=ell}+t1{t<=ell-1}+t1{t<=ell-k}
},                                                   (1.4)

S_r(t)=1{2<=t<=r-1} K(r,t)J_(r,t)/D,                (1.5)
Z_s(t)=[S_s(t)+S_(D-s)(t)]/H_s,                     (1.6)
```

and set `Z_s(t)=0` outside `2<=t<=D-2`. The exact unweighted profile is

```text
Theta_s(ell)
 =Phi_s^D(X_ell)-Phi_s^D(Y_ell)
 =Ltilde_s(Q_ell)+Z_s(ell)-Z_s(ell-k).              (1.7)
```

Both parent orientations and the shrinking-long-parent sign remain inside
each adjacent difference. There is no `q` or `qhat` averaging.

## 2. Reversed-head response

For `u>=1`, let `e_u(t)=1{t<=u}` and

```text
G_r(u)=Wtilde_r(e_u),
P_s(u)=[G_s(u)+G_(D-s)(u)]/H_s.                     (2.1)
```

### Lemma 1 (proved: reversed-head variation)

Uniformly for `1<=u<=(3k-1)/2`,

```text
sum_(s=1)^(k-2) sqrt(s)|P_(s+1)(u)-P_s(u)|
 <=26 sqrt(u).                                      (2.2)
```

#### Proof

Write

```text
rho_m=b_(m-1)/b_m=e(1-1/m)^(m-2),       m>=2.
```

The logarithmic derivative calculation already accepted in M251/M255 gives
that `rho_m` is decreasing. For fixed `t`, the nonzero coefficient

```text
c_r(t)=(t-1)K(r,t),       r>=t+1,
```

satisfies

```text
c_(r+1)(t)/c_r(t)=rho_(r+1)/rho_(r+1-t)<=1.         (2.3)
```

If `r<=u+1`, every allowed `t<=r-1` lies in the head, so
`G_r(u)=h(r)`, which is increasing. After `r=u+1`, no new coefficient is
admitted and every old coefficient decreases by (2.3). Hence the complete
sequence `r -> G_r(u)`, `1<=r<=D-1`, is unimodal. Its total variation is at
most twice its peak, and

```text
TV_r G_r(u)<=2u/R.                                  (2.4)
```

This remains valid when the peak is truncated by `D-1`, since then the
sequence is simply increasing and its endpoint is at most `u/R`.

Put `q=D-s`. The raw paired increment is

```text
[G_(s+1)-G_s]+[G_(q-1)-G_q].                        (2.5)
```

The short edges `1,...,k-2` and long edges `k,...,D-2` are disjoint subsets
of the full `r`-variation. Since `sqrt(s)<=sqrt(k)`, (2.4) yields

```text
sum_s sqrt(s)|Delta raw|
 <=2u sqrt(k)/R
 <=2u/sqrt(k)
 <=3sqrt(u),                                        (2.6)
```

where the last step uses `u<3k/2`.

The accepted exact bounds from M251/M255 are

```text
H_s>=2/9,
sum_(s=1)^(k-2)sqrt(s)|H_(s+1)-H_s|<=8/3.           (2.7)
```

Also `0<=P_s(u)<=1`, because `0<=G_r(u)<=h(r)`. The exact quotient identity
and (2.6)--(2.7) give

```text
sum_s sqrt(s)|Delta P_s(u)|
 <=(9/2)[3sqrt(u)+8/3]
 <=26sqrt(u).
```

This proves (2.2). QED.

## 3. The scalar cutoff/head term

### Lemma 2 (proved: cutoff variation)

```text
sum_(u=1)^(D-3)sqrt(u)|Q_ell(u+1)-Q_ell(u)|
 <=4sqrt(ell).                                      (3.1)
```

#### Proof

If `ell<=k`, the nonzero profile is

```text
Q_ell(t)=(D-t)/D,        1<=t<=ell-1,
Q_ell(ell)=(D-2ell)/D.                              (3.2)
```

If `ell>k`, put `a=ell-k`; then

```text
Q_ell(t)=1,              1<=t<=a,
Q_ell(t)=(D-t)/D,        a+1<=t<=ell-1,
Q_ell(ell)=(D-2ell)/D.                              (3.3)
```

It is zero afterwards. Empty or coincident ranges only remove changes. The
weighted changes consist of: at most one plateau-to-slope jump of magnitude
at most one; a slope interval with increment `1/D`; the slope-to-special
jump of magnitude `(ell+1)/D<=1`; and the special-to-zero jump of magnitude
at most one. Their weights are at most `sqrt(ell)`, while the slope interval
contributes at most

```text
D^-1 sum_(u<=ell)sqrt(u)<=ell sqrt(ell)/D<=sqrt(ell).
```

This proves (3.1). QED.

### Corollary 3 (proved: base response)

```text
sum_(s=1)^(k-2)sqrt(s)
 |Ltilde_(s+1)(Q_ell)-Ltilde_s(Q_ell)|
 <=104sqrt(ell).                                    (3.4)
```

Indeed, finite Abel expansion on the used domain gives

```text
f(t)=f(1)+sum_u[f(u+1)-f(u)]1{t>u}.
```

The constant term has zero adjacent response by (1.3), and
`1{t>u}=1-e_u(t)`. Apply Lemma 1 only after this exact expansion, then use
Lemma 2. QED.

## 4. Simultaneous-seam placement moment

Recall that

```text
J_(r,t)=sum_(a=1)^(t-1)
 #{x in E_(r,t,a):x+k in E_(r,t,a) mod D}.
```

In particular,

```text
0<=J_(r,t)<=t(t-1)<=t^2.                            (4.1)
```

The overlap also has the following exact support description. If
`r<=k-1`, the ambient interval `[0,r)` contains no directed pair at cyclic
distance `k`, so

```text
J_(r,t)=0.                                           (4.1a)
```

If `r=k+c`, `0<=c<=k-2`, the complete list of directed ambient pairs
`(x,x+k mod D)` contained in `[0,r)` is

```text
(u,u+k),       0<=u<c,
(u+k-1,u),     0<=u<=c.                              (4.1b)
```

There are exactly `2c+1` such pairs. For a placement
`E=[0,a) union [a+k+c-t,k+c)`, suppose `t<=c`. Both retained intervals
then have length less than `k`, so a listed pair cannot lie inside one
retained interval. A pair `(u,u+k)` crossing from left to right would require
simultaneously `u<=a-1` and `u>=a+c-t`, which is impossible. A wrapped pair
`(u+k-1,u)` crossing from right to left would require simultaneously
`u<=a-1` and `u>=a+c-t+1`, also impossible. Hence

```text
J_(k+c,t)=0 for t<=c,
J_(k+c,t)<=(t-1)(2c+1) always.                       (4.1c)
```

Thus a fixed overlap spike is supported only on long parents with `c<t`.
The proof below deliberately uses the coarser universal bound (4.1), which
already closes uniformly; (4.1a)--(4.1c) record the exact support and give
an independent check that no short-parent seam pair was introduced.

### Lemma 4 (proved: spike mass and adjacent response)

Uniformly for `2<=t<=(3k-1)/2`,

```text
sum_(r=t+1)^(D-1) S_r(t)<=16sqrt(t/k),              (4.2)

sum_(s=1)^(k-2)sqrt(s)|Z_(s+1)(t)-Z_s(t)|
 <=160sqrt(t).                                      (4.3)
```

Terms with `t>D-2` are zero.

#### Proof

Put `r=t+v`. The uniform Stirling bounds used in M235/M238 imply

```text
b_v/b_(t+v)
 <=2(1+t/v)^(3/2)
 <=4[1+(t/v)^(3/2)],                                (4.4)

b_t<=1/(2t^(3/2)),       sum_(v>=1)v^(-3/2)<=3.
```

Therefore

```text
sum_(r=t+1)^(D-1)K(r,t)
 <=4b_t/R [D+3t^(3/2)]
 <=4/t^(3/2)+6/k.                                   (4.5)
```

By (4.1), `D>=k`, `k>=3`, and `x=t/k<3/2`,

```text
sum_r S_r(t)
 <=t^2/D[4/t^(3/2)+6/k]
 <=4sqrt(t)/k+6(t/k)^2
 <=16sqrt(t/k).                                     (4.6)
```

For the raw paired numerator, positivity gives

```text
sum_s sqrt(s)|
 (S_(s+1)-S_s)+(S_(q-1)-S_q)|
 <=2sqrt(k)sum_r S_r(t)
 <=32sqrt(t).                                       (4.7)
```

Each `S_r(t)<=(t-1)K(r,t)`, because `J_(r,t)/D<=t-1`.
Consequently `0<=Z_s(t)<=1`. Apply the same exact quotient identity,
denominator bound, and normalization variation (2.7):

```text
sum_s sqrt(s)|Delta Z_s(t)|
 <=(9/2)[32sqrt(t)+8/3]
 <=160sqrt(t).
```

This proves the lemma. QED.

## 5. TAV

### Theorem 5 (proved: literal two-run TAV)

For every odd `k>=3` and integer `2<=ell<=(3k-1)/2`,

```text
sum_(s=1)^(k-2)sqrt(s)
 |Theta_(s+1)(ell)-Theta_s(ell)|
 <=500sqrt(ell).                                    (TAV)
```

#### Proof

Use the exact signed decomposition (1.7). Corollary 3 bounds the base term
by `104sqrt(ell)`. Lemma 4 bounds the `t=ell` spike by
`160sqrt(ell)`. If `ell-k>=2`, it bounds the second signed spike by
`160sqrt(ell-k)<=160sqrt(ell)`; otherwise that spike is identically zero.
Thus the left side is at most

```text
(104+160+160)sqrt(ell)=424sqrt(ell)
                      <=500sqrt(ell).
```

Every triangle inequality occurs after the exact short/long pairing for the
corresponding base or spike profile. QED.

## 6. Dependency and scope ledger

- **Accepted immutable inputs:** M199/M207 literal ordered-double formulas;
  M235/M238 exact two-seam geometry; M251/M255 normalization identities,
  `H_s>=2/9`, normalization variation, and monotonicity of `rho_m`.
- **New proved identities:** `tav_cyclic_coefficient.md`, including the four
  seam-pattern counts and the two signed overlap spikes.
- **New proved estimates:** reversed-head variation, cutoff variation, spike
  mass/response, and TAV with constant `500`.
- **Finite falsification only:** the mission checker is restricted to
  `k=3,5,7` and is not used for the universal proof.
- **Not claimed:** full DV or any J2, WPCR, SCBR, response, spectral-gap,
  mixing, or Terminal consequence.
