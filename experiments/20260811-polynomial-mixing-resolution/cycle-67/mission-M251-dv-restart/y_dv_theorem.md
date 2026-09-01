# M251 one-run adjacent-split variation theorem

Date: 2026-08-14 UTC.

Status: Theorem 3 below is **proved**, subject only to the already accepted
M199/M207 literal profile formula.  The final two-run lemma in Section 5 is
**unresolved**.

## 1. Exact scalar operator

Fix odd `k>=3`, and put

```text
D=2k-1,                 R=2k-3,
b_d=e^-d d^(d-1)/d!,    K(r,d)=b_d b_(r-d)/(R b_r),
h(r)=(r-1)(r-2)/(rR),   H_s=h(s)+h(D-s).
```

For a scalar function `f:{1,...,D-1}->R`, define

```text
W_r(f)=sum_(d=1)^(r-2)(r-d-1)K(r,d)f(d),

L_s(f)=1/H_s * {
 h(s)f(D-s)+h(D-s)f(s)+W_s(f)+W_(D-s)(f)
}.                                                        (1.1)
```

The accepted M199/M207 formula says exactly

```text
Phi_s^D(Y_l)=L_s(F_l),
```

where `F_l` is the cyclic two-seam incidence profile.  Since
`W_r(1)=h(r)`, constants are annihilated by adjacent differences:

```text
L_s(1)=2,             L_(s+1)(1)-L_s(1)=0.              (1.2)
```

For a head cutoff `e_t(d)=1{d<=t}`, write

```text
P_s(t)=L_s(e_t),
W_r(t)=W_r(e_t),
B_t=sum_(d=1)^t b_d.                                    (1.3)
```

## 2. Borel cumulative increment lemma

### Lemma 1 (proved)

Uniformly for `1<=t<=D-2` and `1<=r<=D-2`,

```text
|W_(r+1)(t)-W_r(t)| <= 3/R.                            (2.1)
```

If additionally `r>=2t+2`, then

```text
|W_(r+1)(t)-W_r(t)-B_t/R|
 <=120 sqrt(t)/(Rr).                                    (2.2)
```

#### Proof

Put

```text
A_r(d)=(r-d-1)b_(r-d)/b_r,       c=r-d,
rho_m=b_(m-1)/b_m=e(1-1/m)^(m-2).
```

On the common domain `c>=2`, direct division gives

```text
A_(r+1)(d)-A_r(d)
 =[b_c/b_r]{1-c[1-rho_(r+1)/rho_(c+1)]}.              (2.3)
```

For real `x>=2`, let

```text
L(x)=log rho_x=1+(x-2)log(1-1/x).
```

The convergent logarithmic series gives

```text
0 <= -L'(x)
 =-log(1-1/x)-(x-2)/[x(x-1)]
 <=3/x^2.                                               (2.4)
```

Thus `rho_m` decreases to one.  Also

```text
L(c+1)=1+(c-1)log(c/(c+1)) <=2/(c+1).                 (2.5)
```

Set `q=rho_(r+1)/rho_(c+1)`.  Then `0<q<=1`, while
`q>=1/rho_(c+1)>=exp[-2/(c+1)]`.  Hence

```text
0<=c(1-q)<2,
|1-c(1-q)|<=1.                                         (2.6)
```

The exact Borel convolution is

```text
sum_(d=1)^(r-1)b_d b_(r-d)=2(r-1)b_r/r.               (2.7)
```

Equations (2.3), (2.6), and (2.7) bound the sum of the
absolute common-domain increments by `2`.  If the cutoff admits the new
boundary atom `d=r-1`, its coefficient is

```text
b_(r-1)b_2/b_(r+1)=b_2 rho_r rho_(r+1)<=e^-2 e^2=1.
```

After division by `R`, this proves (2.1).  The cases `r=1` and empty
domains are immediate.

For (2.2), `d<=t` and `r>=2t+2` imply `c>=r/2`.  From (2.4)--(2.5),

```text
log[b_c/b_r]=sum_(m=c+1)^r L(m) <=4d/r <=2,

0<=L(c+1)-L(r+1)<=12d/r^2.
```

Therefore

```text
|b_c/b_r-1|<=4e^2 d/r,
1-rho_(r+1)/rho_(c+1)<=12d/r^2.
```

Substitution in (2.3) yields

```text
|A_(r+1)(d)-A_r(d)-1| <=120 d/r.                     (2.8)
```

The elementary Stirling lower bound gives

```text
b_d<=1/(sqrt(2 pi)d^(3/2))<=1/(2d^(3/2)),
sum_(d<=t)d b_d<=sqrt(t).                              (2.9)
```

There is no new boundary atom in the far regime.  Summing (2.8) with
weights `b_d/R` and using (2.9) proves (2.2).  QED.

## 3. Head-response variation

### Lemma 2 (proved)

Uniformly for `1<=t<=D-2`,

```text
sum_(s=1)^(k-2)sqrt(s)|P_(s+1)(t)-P_s(t)|
 <=2300 sqrt(t).                                       (3.1)
```

#### Proof

Write `q=D-s`.  The raw fragmentation difference is exactly

```text
[W_(s+1)(t)-W_s(t)]
 -[W_q(t)-W_(q-1)(t)].                                (3.2)
```

For `s<2t+2`, (2.1) bounds (3.2) by `6/R`.  Splitting according as
`2t+1<=k-2` or not, and using `R>=k`, gives

```text
sum_(s<2t+2)sqrt(s)|(3.2)| <=16 sqrt(t).              (3.3)
```

For `s>=2t+2`, both `s` and `q-1` satisfy the far condition.  The common
`B_t/R` terms in (2.2) cancel before absolute values, so

```text
|(3.2)|<=240 sqrt(t)/(Rs).
```

Using `sum_(s<=k)s^(-1/2)<=2sqrt(k)` gives a far contribution at most
`480sqrt(t)`.  Thus the raw fragmentation contribution is at most
`496sqrt(t)`.

The raw survivor term is

```text
h(s)1{D-s<=t}+h(D-s)1{s<=t}.                          (3.4)
```

Since `0<=h<=1` and

```text
0<=h(r+1)-h(r)=[1-2/(r(r+1))]/R<=1/R,
```

each term in (3.4) has one cutoff jump plus a smooth part.  Their combined
weighted adjacent variation is at most `4sqrt(t)`.

Finally

```text
H_(s+1)-H_s
 =(2/R){1/[(q-1)q]-1/[s(s+1)]},                     (3.5)
```

and `0<=P_s(t)<=2`.  Directly,

```text
sum_s sqrt(s)|H_(s+1)-H_s| <=8/3.
```

Moreover `H_s>=2/9`: this is checked directly when `k=3`, while for
`k>=5`, `H_s>=(D-6)/(D-2)>=3/7`.  Applying the exact quotient identity to
the raw numerator, (3.3)--(3.5) give

```text
sum_s sqrt(s)|P_(s+1)(t)-P_s(t)|
 <=(9/2)[496sqrt(t)+4sqrt(t)+16/3]
 <=2300sqrt(t).
```

QED.

## 4. The one-run DV theorem

The accepted seam-incidence law gives the following exact `F_l` profile.

If `2<=l<k`,

```text
F_l(1)=1/D,
F_l(x)=(D-x)/D       for 2<=x<=l-1,
F_l(l)=(D-2l)/D,
F_l(x)=0             otherwise.                     (4.1)
```

If `l=k`,

```text
F_l(1)=1/D,
F_l(x)=(D-x)/D       for 2<=x<=k-1,
F_l(x)=0             for x>=k.                       (4.2)
```

If `k<l<=(3k-1)/2`, put `a=l-k`.  Then

```text
F_l(1)=2/D,
F_l(x)=1             for 2<=x<=a,
F_l(x)=(D-x)/D       for a+1<=x<=l-1,
F_l(x)=0             for x>=l.                       (4.3)
```

The empty ranges in (4.1)--(4.3) cause no exception.  In all cases, direct
summation of the few jumps and the slope-`1/D` interval gives

```text
sum_(t=1)^(D-2)sqrt(t)|F_l(t+1)-F_l(t)|
 <=8sqrt(l).                                            (4.4)
```

### Theorem 3 (proved: `Y` clause of DV)

For every odd `k>=3` and `2<=l<=(3k-1)/2`,

```text
sum_(s=1)^(k-2)sqrt(s)
 |Phi_(s+1)^D(Y_l)-Phi_s^D(Y_l)|
 <=18400sqrt(l).                                       (Y-DV)
```

#### Proof

For any `f`, finite Abel expansion gives

```text
f(d)=f(1)+sum_(t=1)^(D-2)[f(t+1)-f(t)]1{d>t}.
```

Since `1{d>t}=1-e_t(d)` and constants have zero adjacent response by
(1.2),

```text
L_(s+1)(f)-L_s(f)
 =-sum_t[f(t+1)-f(t)][P_(s+1)(t)-P_s(t)].            (4.5)
```

Take `f=F_l`, then apply the triangle inequality only after (4.5), Lemma 2,
and (4.4).  The resulting constant is `2300*8=18400`.  QED.

The constant is intentionally loose.  No asymptotic conclusion is drawn
from the finite diagnostic; it merely did not falsify this theorem.

## 5. Exact first remaining lemma for `X`

Put

```text
Theta_s(l)=Phi_s^D(X_l)-Phi_s^D(Y_l).
```

By the literal M199/M207 tuple formula,

```text
Theta_s(l)=1/[D H_s]
 sum_i sum_(r in {s,D-s}) sum_(d=1)^(r-2)K(r,d)
 sum_(a=1)^(r-d-1)
 1{2<=n-A(i+r,D-r)-A(i+a,d)<=l}.                    (5.1)
```

Every same/cross kind and repeated-size collision remains in (5.1).

> **TWO-RUN ADJACENT VARIATION `(TAV)` (unresolved).** Uniformly in the
> same domain,
>
> ```text
> sum_(s=1)^(k-2)sqrt(s)
>  |Theta_(s+1)(l)-Theta_s(l)| <= C sqrt(l).          (TAV)
> ```

The triangle inequality with `(Y-DV)` shows that `(TAV)` is now the sole
remaining scalar obligation for the `X` clause of `(DV)`.  The exact
paired-domain decomposition of its common-kernel, common-seam, boundary,
and normalization edits is already (2.1)--(4.1) of
`paired_difference_identity.md`.  No bound on `(TAV)` is claimed here.

