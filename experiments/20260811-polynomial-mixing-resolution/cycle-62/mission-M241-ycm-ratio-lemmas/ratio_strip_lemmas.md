# M241 explicit ratio and strip lemmas

Date: 2026-08-13 UTC.

Status: R1--R3 and the stated SG/GG2 sufficiency corollaries are **proved**.
YCM and every downstream statement remain **unresolved**.

## 1. Definitions and exact domains

For odd `k>=3`, put

    j=(k-1)/2,  D=2k-1,  R=2k-3,  L=(3k-1)/2,
    b_n=e^(-n)n^(n-1)/n!,                         n>=1,
    q_s=[k/(k-1)] b_s b_(k-s)/b_k,                1<=s<=j,
    a_r(x)=[(r-x-1)/R] b_(r-x)/b_r,               1<=x<r,
    h(r)=(r-1)(r-2)/(rR).

The accepted Borel convolution gives `sum_(s=1)^j q_s=1`.

R1 is used only on

    j<=x<=L-1,  1<=s<=min(j,D-x-2).               (R1-domain)

Writing `M=D-x`, this is exactly the positive-support domain of the GG2
long-parent term. R2--R3 are used only on the integer SG domain

    1<=x<=k/4.                                    (SG-domain)

If an indexed range is empty, its sum is zero. In particular the SG domain
is empty at `k=3`, and the strict strip `x<s<2x` is empty at `x=1`.

## 2. Elementary Borel-ratio facts

For `n>=2`,

    rho_n:=b_(n-1)/b_n=e(1-1/n)^(n-2).             (2.1)

Moreover

    0<=log rho_n<=2/n,                             (2.2)

and `rho_n` is decreasing. Indeed
`log(1-u)>=-u/(1-u)` gives the lower bound in (2.2), while
`log(1-u)<=-u` gives the upper bound. For real `t>=2`,

    d/dt log rho_t
      =log(1-1/t)+(t-2)/(t(t-1)) < 0,

because the second summand is at most `1/t` and
`log(1-1/t)<-1/t`. Thus the discrete sequence decreases. In particular
`b_n` decreases.

For integers `r>=2x>=2`, exact telescoping gives

    b_(r-x)/b_r = product_(n=r-x+1)^r rho_n.        (2.3)

Every product index is at least two, including the boundary `r=2,x=1`.
By (2.2),

    0<=log[b_(r-x)/b_r]
      <=2 sum_(n=r-x+1)^r 1/n
      <=4x/r<=2.                                  (2.4)

For `0<=u<=2`, monotonicity of `(e^u-1)/u` and `e^2<8` give
`e^u-1<=4u`. Hence

    0<=b_(r-x)/b_r-1<=16x/r.                       (2.5)

We also use the standard elementary Stirling envelope

    e^(-1)n^(-3/2) <= b_n <= (2 pi)^(-1/2)n^(-3/2). (2.6)

The lower inequality follows from the usual upper Stirling bound
`n!<=e sqrt(n)(n/e)^n`; the upper one follows from
`n!>=sqrt(2 pi n)(n/e)^n`.

## 3. R1: the GG2 bracket

> **Lemma R1.** On the R1-domain,
>
>     H_(k,x,s):=b_x b_(k-s)/(b_k b_(D-s)) <=36.  (R1)

### Proof

Since `b_x` decreases, `b_x/b_k` is maximized at `x=j`. For fixed
`k`, let `g(n)=b_n/b_(n+k-1)`. Then

    g(n+1)/g(n)=rho_(n+k)/rho_(n+1)<=1

by decreasing `rho`. Thus `b_(k-s)/b_(D-s)=g(k-s)` increases with
`s`, and is maximized at `s=j`. The rectangle endpoint `(j,j)` is
admissible; the additional constraint `s<=D-x-2` can only shrink the
domain.

For an explicit constant, (2.6) gives directly on the whole domain

    H_(k,x,s)
      <=[e^2/(2 pi)] [k(D-s)/(x(k-s))]^(3/2).

Writing `k=2j+1`, monotonicity in `x,s` and `j>=1` give

    k(D-s)/(x(k-s))
      <=(2j+1)(3j+1)/(j(j+1))<=6.

Since `e<3`, `pi>3`, and `sqrt(6)<3`, the last display is less than
`27`, hence at most the advertised constant `36`. This includes all
small ranks and proves R1. ∎

## 4. R2: the smooth absolute aggregate

> **Lemma R2.** On the SG-domain,
>
>     sum_(s=1)^j q_s |a_(D-s)(x)-(D-s)/R|
>       +sum_(2x<=s<=j) q_s |a_s(x)-s/R|
>       <=34(x+1)/k.                               (R2)

### Proof

For every `r>=2x`, put `Q=b_(r-x)/b_r`. Equations (2.3)--(2.5) give
`1<=Q` and `Q-1<=16x/r`. Therefore

    |a_r(x)-r/R|
      =|(r-x-1)Q-r|/R
      <=[r(Q-1)+(x+1)]/R
      <=17(x+1)/R.                                (4.1)

For the first sum, `r=D-s>=D-j>=2x`; for the second, `r=s>=2x` by
definition. Each sum has total `q`-weight at most one. Thus their sum is
at most `34(x+1)/R`, which is at most `34(x+1)/k` because `R>=k`
for `k>=3`. Empty second sums cause no exception. ∎

## 5. R3: the nonsmooth strip

> **Lemma R3.** On the SG-domain,
>
>     sum_(x<s<2x, s<=j) q_s s/R
>       <=42 sqrt(x)/R,                            (R3c)
>
>     sum_(x<s<2x, s<=j) q_s a_s(x)
>       <=28 sqrt(x)/R.                            (R3a)

### Proof

For `1<=s<=j`, another use of (2.2) gives

    log[b_(k-s)/b_k]
      <=2s/(k-s+1)<2.

Since `k/(k-1)<=3/2` and `e^2<8`,

    q_s <12b_s.                                   (5.1)

From (2.6), `s b_s<=s^(-1/2)`, and
`sum_(s=1)^n s^(-1/2)<=2sqrt(n)`. Consequently

    sum_(x<s<2x, s<=j) q_s s/R
      <=(12/R) sum_(s<2x) s b_s
      <=36 sqrt(x)/R
      <=42 sqrt(x)/R.                             (5.2)

For the actual mass, (5.1) cancels the `b_s` denominator in `a_s`.
With `t=s-x`, where `1<=t<=x-1`,

    sum_(x<s<2x, s<=j) q_s a_s(x)
      <=(12/R) sum_(t=1)^(x-1) (t-1)b_t
      <=24 sqrt(x)/R
      <=28 sqrt(x)/R.                             (5.3)

The proof also covers the empty strip at `x=1`. ∎

## 6. Exact sufficiency for the two named skeleton estimates

This section checks what R1--R3 discharge. It does not assemble YCM.

### 6.1 R2+R3 imply SG with an explicit constant

Divide the two fragmentation sources in M226's `G_k(x)` by `b_x`.
Their actual mass is

    F=sum_s q_s a_(D-s)(x)+sum_(s>x)q_s a_s(x).

The no-shift comparison is

    F0=sum_s q_s(D-s)/R+sum_(s>x)q_s s/R
       =1+2/R-(1/R)sum_(s<=x)sq_s.                (6.1)

R2 handles all long parents and the short range `s>=2x`. R3 handles
`x<s<2x` by bounding actual and comparison masses separately. Hence

    |F-F0|
      <=34(x+1)/k+70sqrt(x)/R
      <=104(x+1)/k.                               (6.2)

Also `|F0-1|<=(x+2)/R<=2(x+1)/k`.

The surviving source divided by `b_x` is

    U=[k/(k-1)][b_(k-x)/b_k]
      [(D-x-1)/(D-x)][(D-x-2)/R].

The last three rational prefactors except the Borel ratio form a product
`P` with

    |P-1|<=1/(k-1)+1/(D-x)+x/R<=2(x+1)/k,
    P<=k/(k-1)<=5/4.

For completeness, write `P=ABC` with `A=k/(k-1)>=1` and
`0<B,C<=1`. The triangle decomposition
`|ABC-1|<=|(A-1)BC|+|BC-1|`, followed by
`1-BC=(1-B)+B(1-C)`, proves the first displayed product bound whether
`P` lies above or below one.

Equation (2.5), now with `r=k`, gives
`0<=b_(k-x)/b_k-1<=16x/k`. Therefore

    |U-1|<=22(x+1)/k.                              (6.3)

Combining (6.1)--(6.3) proves the fully quantified candidate estimate

    |G_k(x)-2b_x|<=128(x+1)b_x/k,  1<=x<=k/4.     (SG)

The domain is empty at `k=3`; when nonempty `k>=5`, which justified
`k/(k-1)<=5/4` above.

### 6.2 R1 implies GG2 with an explicit constant

For `j<=x<=L-1`, put `M=D-x`. The short-parent sum is empty; only the
long-parent sum and, at `x=j`, the survivor remain. Algebraically the
long-parent term is

    [k/(k-1)](1/R)
      sum_(s<=min(j,M-2))
       b_s(M-s-1)b_(M-s) H_(k,x,s).

By R1, positivity, and the weighted Borel convolution, this is at most

    (54/R) sum_(s=1)^(M-1)(M-s-1)b_s b_(M-s)
      <=54(M-1)b_M/R
      <=54/(k sqrt(M)).                            (6.4)

At `x=j`, (2.6), `j>=k/3`, `j+1>=k/2`, and
`M=(3k-1)/2<=3k/2` give

    q_j h(M)<=q_j<=16/(k sqrt(M)).                 (6.5)

Here `h(M)<=1`, since
`MR-(M-1)(M-2)=M(j+1)-2>0`. The displayed `q_j` bound follows because

    q_j <=(3/4) k^(3/2)/[j(j+1)]^(3/2),

while multiplication by `k sqrt(M)` and the three preceding elementary
bounds gives at most
`(3/4)sqrt(3/2)6^(3/2)=27/2<16`.

There is no survivor for `x>j`. Equations (6.4)--(6.5) prove

    G_k(x)<=70/[k sqrt(D-x)],  j<=x<=L-1.          (GG2)

Thus R1--R3 close exactly the candidate SG and GG2 constant gaps. They do
not audit or prove GG1, the four coefficient-region estimates, their prefix
summation, or the finite-rank raw bound. Consequently this mission makes no
YCM, TCM, WBE, DE, gap, mixing, or Terminal inference.

## 7. Boundary and falsification checks

The deterministic checker uses rational enclosures of `e` and exact
`Fraction` arithmetic. It checks all R1-domain tuples and every SG-domain
R2/R3 aggregate for odd `3<=k<=31`, including empty ranges. These finite
checks are only falsification tests; the universal result is the proof above.
