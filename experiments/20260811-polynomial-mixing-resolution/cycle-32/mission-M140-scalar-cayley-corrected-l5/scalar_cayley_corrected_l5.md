# M140 scalar Cayley lemma and corrected auxiliary L=5 theorem

Date: 2026-08-13 UTC.

## 1. Scope, target, and conventions

The project target is uniform on fixed-length identity transposition words.
This note concerns only the auxiliary full **nonlazy stationary-flow
parking-degree projection** in the minimal-long-cycle sector.  Permutations
compose as `(pq)(x)=p(q(x))`, with factors displayed left-to-right.

Put

```text
w_n=n^(n-1)/n!,
c(n,p)=p n^(n-p-1)/(n-p)!,

lambda(A,k)
 =(k-1)! sum_(p=1)^A [p/(p+k-1)!](A)_p/A^p,

m_s(A,k)=k w_A c(s-A,k-1)/(k!w_(s+1)).
```

The scalar coefficient left open by M131 and M138 is

```text
C_s=sum_(k=2)^s sum_(A=1)^(s-k+1) m_s(A,k)lambda(A,k)^2.       (1.1)
```

The first theorem below proves `C_s<3/4` for every `s>=100`.  The second
uses the corrected one-power exceptional subtraction identified by M138 to
prove the complete right-heavy suffix-excess-five inequality

```text
H(s,K,K-1,s-5)<=q(1-q),
q=w_6 w_(s-5)/w_(s+1), s>=6, K>=1.                            (1.2)
```

Every attachment rank `j=1,...,k` is retained.  Only `j=0` and auxiliary
rank-one targets are killed in the accepted recurrence.  No auxiliary gap,
ROOT-MEAN LIFT, original-chain gap, polynomial mixing result, Terminal A, or
Terminal B follows from (1.2).

## 2. Exact first moment from the tree equation

Let

```text
T(z)=sum_(n>=1)w_n z^n.
```

The rooted-tree equation is `T=z exp(T)`.  Lagrange inversion gives

```text
[z^n]T(z)^p=c(n,p).                                            (2.1)
```

Also, directly from the definitions,

```text
w_A p(A)_p/A^p=c(A,p).                                        (2.2)
```

For fixed `s` and `k`, substitute the formula for `lambda` into the first
moment.  The factors `(k-1)!` cancel, and (2.1)--(2.2) give

```text
sum_A m_s(A,k)lambda(A,k)
 =1/w_(s+1) sum_(A,p>=1)
    c(A,p)c(s-A,k-1)/(p+k-1)!

 =[z^s] sum_(j>=k)T(z)^j/j! / w_(s+1).                        (2.3)
```

For `1<=j<=s`, another application of Lagrange inversion yields

```text
[z^s]T^j/j! / w_(s+1)
 =binom(s-1,j-1)s^(s-j)/(s+1)^(s-1).
```

The right side is the mass at `j-1` of
`X_s~Bin(s-1,1/(s+1))`.  Therefore the exact first-moment identity is

```text
sum_A m_s(A,k)lambda(A,k)=P[X_s>=k-1].                         (2.4)
```

There is no limiting argument and no omitted endpoint: coefficients with
`j>s` vanish automatically.

## 3. A universal Poisson majorant

Define

```text
L_k=(k-1)! sum_(p>=1)p/(p+k-1)!.
```

Because `(A)_p/A^p<=1`, extending the finite nonnegative sum gives
`0<lambda(A,k)<L_k`.  Hence the exact identity

```text
lambda^2=L_k lambda-lambda(L_k-lambda)                         (3.1)
```

turns (1.1) into

```text
C_s=M_s-D_s,
M_s=sum_(k>=2)L_k P[X_s>=k-1],
D_s=sum_(k,A)m_s(A,k)lambda(A,k)(L_k-lambda(A,k))>=0.          (3.2)
```

The stochastic-order direction in the next step is important.  Put
`p=1/(s+1)` and let `Y_i` be independent Poisson variables with parameter
`mu_0=-log(1-p)`.  Then

```text
1[Y_i>=1]~Bernoulli(p),
sum_i 1[Y_i>=1] <= sum_i Y_i.
```

The Poisson sum has parameter

```text
mu=(s-1)log(1+1/s)<(s-1)/s<1.                                 (3.3)
```

Adding an independent `Pois(1-mu)` variable therefore couples

```text
X_s <=st Pois(1).                                               (3.4)
```

Write `Y~Pois(1)` and `j=k-1`.  A beta integral gives

```text
L_(j+1)=integral_0^1 (1+t)e^t(1-t)^j dt.                       (3.5)
```

Indeed, the coefficient of `t^(p-1)` in `(1+t)e^t` is
`p/(p-1)!`, and its beta integral against `(1-t)^j` is
`p j!/(p+j)!`.  For `0<=x<1`, Tonelli's theorem and a finite geometric sum
give

```text
sum_(j>=1)P[Y>=j]x^j
 =E[sum_(j=1)^Y x^j]
 =x(1-e^(x-1))/(1-x).                                         (3.6)
```

Using `x=1-t` in (3.5)--(3.6),

```text
M_s<=U
 :=integral_0^1 (1-t^2)(e^t-1)/t dt
 =sum_(n>=1) 2/[n(n+2)n!].                                    (3.7)
```

The first seven terms and a geometric factorial-tail bound are

```text
sum_(n=1)^7 2/[n(n+2)n!]=10388003/12700800,

sum_(n>=8)2/[n(n+2)n!]
 <=2 sum_(n>=8)1/n!
 <=9/(4*8!)=1/17920.
```

Consequently

```text
U<41554847/50803200<409/500.                                  (3.8)
```

The first inequality is strict because the termwise tail estimate is strict.

## 4. Uniform finite correction

It remains to retain enough of `D_s` in (3.2).  Use the nine pairs

```text
F={(A,k): k=2,1<=A<=4;
           k=3,1<=A<=4;
           (A,k)=(1,4)}.                                      (4.1)
```

### 4.1 Uniform endpoint-mass lower bound

Fix a pair in (4.1), and put

```text
n=s-A, u=A+1, h=k-2.
```

Thus `n>=96`, `2<=u<=5`, and `0<=h<=2`.  Expanding the factorials in
`m_s(A,k)` gives the exact ratio

```text
m_s(A,k) / [w_A e^(-u)/(k-2)!]
 =R(n,u,k)
 =e^u (n/(n+u))^(n+u-1)
    product_(r=-h)^u(1+r/n).                                  (4.2)
```

We now prove a uniform lower bound, not merely check finite values.  For
`0<x<1`, use

```text
log(1+x)<x-x^2/2+x^3/3,
log(1+x)>x-x^2/2,
log(1-x)>-x-x^2/[2(1-x)].                                    (4.3)
```

The last inequality follows by bounding
`sum_(r>=2)x^r/r < (1/2)sum_(r>=2)x^r`; the first two follow from the
alternating expansion or integration of the corresponding rational
remainders.  Applying (4.3) to (4.2) and collecting powers gives

```text
log R > [3u/2-h(h+1)/2]/n
        +u^2(u-1)/(2n^2)
        -u^3/(3n^2)-u^3(u-1)/(3n^3)
        -[sum_(r=1)^u r^2]/(2n^2)
        -sum_(a=1)^h a^2/[2n(n-a)].                           (4.4)
```

The first displayed coefficient is nonnegative throughout the rectangle;
its minimum is zero at `(u,h)=(2,2)`.  Drop it and the other positive term.
Every retained error term increases with `u,h` and decreases with `n`, so
the worst permitted values are `(n,u,h)=(96,5,2)`.  Exact arithmetic gives

```text
u^3/(3n^2)+u^3(u-1)/(3n^3)
 +[sum_(r=1)^u r^2]/(2n^2)
 +sum_(a=1)^h a^2/[2n(n-a)]

 <=23612897/2962759680
 <1/100,                                                       (4.5)
```

with exact slack `30073499/14813798400`.  Hence

```text
R>e^(-1/100)>1-1/100=99/100.                                  (4.6)
```

This proves uniformly for every selected pair and every `s>=100` that

```text
m_s(A,k)>(99/100) w_A e^(-u)/(k-2)!.                          (4.7)
```

Finally,

```text
e<sum_(r=0)^6 1/r!+(1/7!)sum_(j>=0)8^(-j)
 =1957/720+1/4410
 =31967/11760<87/32,                                          (4.8)
```

so `e^(-u)>(32/87)^u`.

### 4.2 Exact selected correction

Telescoping gives `L_2=1`.  Five positive terms give

```text
L_3>473/840>9/16,
L_4>2557/6720>3/8.                                            (4.9)
```

For the selected pairs the exact lambdas are

| `k` | `A=1` | `A=2` | `A=3` | `A=4` |
|---|---:|---:|---:|---:|
| 2 | `1/2` | `2/3` | `3/4` | `4/5` |
| 3 | `1/3` | `5/12` | `41/90` | `153/320` |
| 4 | `1/4` | -- | -- | -- |

Thus each lower value in (4.9) still exceeds its selected lambda.  Let
`ell_2=1`, `ell_3=9/16`, and `ell_4=3/8`.  Retaining only (4.1) in `D_s`,
then using (4.7)--(4.9), gives

```text
D_s>(99/100)D_0,

D_0=sum_((A,k) in F)
 w_A(32/87)^(A+1)/(k-2)!
 lambda(A,k)[ell_k-lambda(A,k)]

 =78988317872/1121447071575
 >69/1000.                                                     (4.10)
```

The factor `99/100` is outside `D_0`; it must not be silently dropped.  The
actual displayed lower correction is

```text
(99/100)D_0=217217874148/3115130754375.                        (4.11)
```

Combining (3.2), (3.8), and (4.10) proves the standalone statement.

> **Theorem 4.1 (proved scalar lemma C).** For every integer `s>=100`,
> ```text
> C_s<409/500-(99/100)(69/1000)
>    =74969/100000<3/4.                                       (4.12)
> ```

This is a universal analytic proof.  The exact values of `C_s` stored by the
checker are diagnostics only.

## 5. Corrected auxiliary L=5 envelope

For a canonical endpoint `E`, use M138's notation

```text
c_E=degree(E)rho(E),
b_E=rho(B_E)=c_E lambda_E,
a_E=rho(B_E intersect S_x),
0<=a_E<=b_E.
```

After division by the initial split mass `q`, the ordinary contribution of
the whole basin is `q b_E lambda_E`.  Replacing the supported exceptional
part by its exact current square may therefore subtract
`q a_E lambda_E`, because the unremoved ordinary amount is exactly

```text
q(b_E-a_E)lambda_E>=0.                                        (5.1)
```

The corrected reset envelope is consequently

```text
R_corr=q[C_s-sum_E a_E lambda_E]
       +sum_E theta_E^2/(q c_E).                              (5.2)
```

Formula (5.2) uses one power of `lambda_E`.  The frozen M131 display with
`a_E lambda_E^2` is valid but too loose, fails its asserted certificate, and
is not used anywhere in this mission.  The standalone scalar checker verifies
`a_E<=b_E=c_E lambda_E` and (5.1) for all 31 supported occurrences at each
of `s=6,7`.

Add the accepted descendant envelope: all 11 live groups and all 31 nominal
positive attachment-rank terms are represented before the smallest-rank
boundary is imposed.  Right-heavy children use the accepted `L<=4` theorem,
and the other children use the accepted arbitrary-deficit `L<=3` envelope.
Denote the resulting corrected envelope by `E_5`.

For each `s=6,...,99`, the independent M140 checker forms

```text
T_s(z)=product_(a=1)^5(1+az)^2[1-q-E_5(z)].                   (5.3)
```

All 1,222 exact degree-12 Bernstein coefficients on `z in [0,1/2]` are
positive.  The exact minimum is

```text
5307578203959502651/4736091661711441920000
```

at `s=7`, index zero.

The smallest boundary is strict and explicit.  At `s=6`, `B=1`; every
nominal `t=2` child has auxiliary rank one and is inactive, its displayed
terminal charge vanishes because `b_1=1`, and exactly 17 children remain.
The 13 `s=6` coefficients in the new result artifact are all strictly
positive; their minimum is `13461835439971/11861248695609600` at index
zero.  Thus (5.3) is positive for every actual
`z=1/(K+1) in (0,1/2]`, including `K=1`.

For `b_n=(n/(n+1))^(n-1)`, the function
`(x-1)log(1+1/x)` is increasing: its derivative is
`log(1+1/x)-(x-1)/(x(x+1))>1/(x+1)-(x-1)/(x(x+1))>0`.
Thus `b_n` decreases.  Also
`(n-1)log(1+1/n)<(n-1)/n<1`, so `b_n>1/e>4/11` by (4.8), while the exact
integer comparison

```text
500*95^94<187*96^94
```

gives `b_95<187/500`.  Therefore, for `s>=100`, every one of the six Cayley
ratios lies in `[4/11,187/500]`.  Replacing all path heights by one and
replacing `C_s` by `3/4` only enlarges the corrected envelope.  The cleared
tail slack has multidegree

```text
(1,1,2,2,2,2,12).
```

All 4,212 exact tensor Bernstein coefficients on the ratio box times
`z in [0,1/2]` are positive.  The exact minimum is

```text
4360847276079323/50118750000000000000
```

at index `(1,1,2,2,2,0,0)`.  Exact finite and tail off-grid interpolation
identities pass.  M140 regenerated these coefficients without importing
predecessor source, then found exact post-hoc equality with every coefficient
in M138.

Theorem 4.1 now discharges the only assumption in the corrected tail
certificate.

> **Theorem 5.1 (proved corrected auxiliary right-heavy L=5 theorem).**
> Relative only to the accepted all-rank recurrence and the proved lower-
> excess envelopes, for every `s>=6` and `K>=1`,
> ```text
> H(s,K,K-1,s-5)<q(1-q),
> q=w_6 w_(s-5)/w_(s+1).
> ```
> In particular, the weak inequality (1.2) holds with no remaining scalar
> assumption.

## 6. Dependencies, exact checks, and exclusions

Proved within M140:

- the tree-EGF first-moment identity (2.4);
- the binomial-to-Poisson coupling (3.3)--(3.4);
- the integral/series bound (3.5)--(3.8);
- the uniform endpoint-mass bound (4.2)--(4.8);
- the exact finite correction and Theorem 4.1;
- the one-power normalization (5.1), with literal small-boundary checks; and
- an independent exact regeneration of both corrected Bernstein
  certificates.

Accepted proved inputs:

- M109/M114: all-rank finite-DAG recurrence and lower sectors;
- M115/M116 and M117/M121: arbitrary-deficit lower-excess envelopes and
  right-heavy contraction through `L=4`; and
- M138 Sections 6--8: corrected one-power reset decomposition and the
  structural conditional implication, now independently rebuilt and with
  its scalar assumption discharged.

M131's frozen theorem is not an accepted dependency because its displayed
two-power subtraction was rejected.  No generic basin-frame/Bessel estimate,
raw one-step defect sign, two-layer sign argument, finite monotonicity
extrapolation, or unproved asymptotic estimate is used.

Reproduce the exact checks from this directory with

```text
python3 -B scalar_cayley_exact.py --output scalar_cayley_exact.json

python3 -B corrected_l5_certificates.py \
  --output corrected_l5_certificates.json \
  --reference-json \
  ../../cycle-31/mission-M138-m131-fresh-referee/independent_m131_referee.json
```

Both scripts use Python 3.12.3, standard-library exact `fractions.Fraction`
arithmetic for every theorem-critical computation, no nonstandard
dependencies, and deterministic `seed=null`.  The high-precision Poisson
tail sweep in the scalar checker is explicitly diagnostic; the universal
stochastic domination is proved by the coupling above.
