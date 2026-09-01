# M243 clean-room proof audit of immutable M241

Date: 2026-08-14 UTC.

Verdict: **ACCEPT**.  Frozen M241 proves `R1`, `R2`, and `R3` on their
stated domains and proves exactly the local consequences `SG=128` and
`GG2=70`.  This audit makes no `YCM`, `WBE`, `DE`, or downstream claim.

## 1. Immutable gate and exact interface

Every file in M241's frozen inventory passed before inspection.  Its
checksum-file digest is

    07918bbf968c93f34cbd252f938b1e6e21566ba2907836872592bb744ef53936.

The frozen M226 and accepting M229 inventories also pass, with digests
`a40efd...a78a` and `6b3f53...688`.  M229's domain correction is enforced:
only `1<=x<=L-1`, where `L=(3k-1)/2`, is used for `G_k(x)`.

For odd `k>=3`, set

    j=(k-1)/2, D=2k-1, R=2k-3,
    b_n=e^(-n)n^(n-1)/n!,
    q_s=[k/(k-1)]b_s b_(k-s)/b_k.

The Borel convolution and symmetry about `k/2` give

    sum_(s=1)^j b_s b_(k-s)=(k-1)b_k/k,

so `q_s>0` and `sum_s q_s=1` exactly.  This normalization, not a
conditional or asymptotic replacement, is used below.

## 2. Ratio calculus and product indexing

Direct cancellation gives, for `n>=2`,

    rho_n=b_(n-1)/b_n=e(1-1/n)^(n-2).

The elementary logarithm bounds imply

    1/(n-1) <= log rho_n <= 2/n,

where only the weaker lower bound zero is needed.  For real `t>=2`,

    d/dt log rho_t
      =log(1-1/t)+(t-2)/(t(t-1))<0,

because the second term is strictly below `1/t` and the first below
`-1/t`.  Thus `rho_n` and `b_n` decrease.

If `r>=2x>=2`, telescoping has exactly `x` factors:

    b_(r-x)/b_r=product_(n=r-x+1)^r rho_n.

The first index is at least two, including `r=2,x=1`.  Hence, writing the
logarithm of this ratio as `u`,

    0<=u<=2 sum_(n=r-x+1)^r 1/n<=4x/r<=2.

Since `(e^u-1)/u` increases and its value at two is below four,

    0<=b_(r-x)/b_r-1<=16x/r.                      (2.1)

This independently verifies the recurrence direction and every product
endpoint used by M241.

## 3. R1

On the R1 domain put

    H=b_x b_(k-s)/(b_k b_(D-s)).

The first ratio is largest at `x=j`.  For
`g(n)=b_n/b_(n+k-1)`,

    g(n+1)/g(n)=rho_(n+k)/rho_(n+1)<=1,

so the second ratio is largest at `s=j`.  The endpoint `(j,j)` is
admissible; the extra condition `s<=D-x-2` only removes points.

Using

    e^(-1)n^(-3/2)<=b_n<=(2 pi)^(-1/2)n^(-3/2)

gives

    H <= [e^2/(2 pi)] [k(D-s)/(x(k-s))]^(3/2).

Writing `k=2j+1`, the bracket is at most

    (2j+1)(3j+1)/(j(j+1))<=6.

The crude elementary bounds `e<3`, `pi>3`, and `sqrt(6)<3` already make
the result less than `27`, hence certainly at most `36`.  This covers
`j=1` and proves R1 without a finite-rank exception.

## 4. R2 and R3

For `r>=2x`, let `Q=b_(r-x)/b_r`.  The useful exact rearrangement is

    a_r(x)-r/R=[(r-x-1)(Q-1)-(x+1)]/R.

Equation (2.1) therefore yields

    |a_r(x)-r/R|<=17(x+1)/R.                      (4.1)

On `1<=x<=k/4`, every long parent `r=D-s` exceeds `2x`; every short
parent in R2 is restricted to `s>=2x`.  Each of the two `q`-weighted
sums has mass at most one.  Thus their total is at most
`34(x+1)/R<=34(x+1)/k`, proving R2.  Formula (4.1) also explains why the
apparently missing factor `Q` in M241's displayed triangle estimate is not
missing: the rearrangement above is the operative one.

For `s<=j`, the same ratio product gives

    log[b_(k-s)/b_k]<=2s/(k-s+1)<2,

and hence `q_s<12b_s`.  On the strict strip `x<s<2x`, the comparison mass
is bounded by

    (12/R) sum_(s<2x) s b_s
      <=(12/R) sum_(s<2x)s^(-1/2)
      <=36 sqrt(x)/R<42 sqrt(x)/R.

For the actual mass, put `t=s-x`.  The factor `b_s` cancels before any
estimate:

    q_s a_s(x)<=(12/R)(t-1)b_t.

Summing `1<=t<=x-1` gives at most `24sqrt(x)/R`, hence the advertised
`28sqrt(x)/R`.  The strip is empty at `x=1`.  The entire SG domain is
empty at `k=3`; for every nonempty case `k>=5`.  This proves R3 with all
empty ranges interpreted literally.

## 5. Exact SG consequence

Dividing accepted M226's `G_k(x)` by `b_x` gives `U+F`, where `F` is the
two fragmentation sums and

    U=[k/(k-1)][b_(k-x)/b_k]
      [(D-x-1)/(D-x)][(D-x-2)/R].

Replacing each shifted Borel ratio in `F` by one gives exactly

    F0=1+2/R-(1/R)sum_(s<=x)sq_s.

R2 controls the long parents and `s>=2x`; R3 controls the strict strip
by the sum of its actual and comparison masses.  Therefore

    |F-F0|<=34(x+1)/k+70sqrt(x)/R<=104(x+1)/k,
    |F0-1|<=(x+2)/R<=2(x+1)/k.                    (5.1)

Write the rational part of `U` as `P=ABC`, with

    A=k/(k-1), B=1-1/(D-x), C=1-x/R.

Since `A>=1` and `0<B,C<=1`,

    |P-1|<=1/(k-1)+1/(D-x)+x/R<=2(x+1)/k.

For the nonempty SG domain, `k>=5` and `P<=A<=5/4`.  Applying (2.1) at
`r=k` then gives

    |U-1|<=|P-1|+P|b_(k-x)/b_k-1|<=22(x+1)/k.     (5.2)

The constants in (5.1)--(5.2) sum to `104+2+22=128`, proving exactly

    |G_k(x)-2b_x|<=128(x+1)b_x/k,

on `1<=x<=k/4`.

## 6. Exact GG2 consequence

For `j<=x<=L-1`, put `M=D-x`.  The short-parent sum is empty, and the
survivor exists only at `x=j`.  R1 and positivity bound the long-parent
part by

    (54/R) sum_(s=1)^(M-1)(M-s-1)b_s b_(M-s).

The sum is exactly `(M-1)(M-2)b_M/M`, so the coarse bound
`(M-1)b_M`, the upper Stirling estimate, and `R>=k` give

    long parent <=54/[k sqrt(M)].                  (6.1)

At `x=j`, `M=(3k-1)/2` and

    q_j <=(3/4) k^(3/2)/[j(j+1)]^(3/2).

Using `j>=k/3`, `j+1>=k/2`, and `M<=3k/2` shows

    q_j k sqrt(M)<=(3/4)sqrt(3/2)6^(3/2)=27/2<16.

Moreover `h(M)<=1`, because

    MR-(M-1)(M-2)=M(j+1)-2>0.

Thus the survivor contributes at most `16/[k sqrt(M)]`.  Adding it to
(6.1), only where it exists, proves exactly

    G_k(x)<=70/[k sqrt(D-x)].

The calculation remains valid at `k=3`, at `x=j`, and at `x=L-1`;
empty long sums are zero.

## 7. Independent falsification and objections

`boundary_check.py` is standard-library-only and imports no M241 module or
data.  With certified rational bounds for `e`, it checks decreasing `rho`,
telescoping endpoints, exact `q` normalization, all R1 tuples, R2/R3,
the rational prefactor, and direct SG/GG2 formulas for every odd
`3<=k<=35`.  All checks pass.  These finite checks prove no universal
statement; the proof is Sections 2--6.

Numbered objections:

1. **Material objections:** none.
2. **Nonmaterial clarification:** M241 (4.1) is correct via the exact
   rearrangement displayed above; writing that line explicitly would avoid
   the superficial appearance that a factor `Q` was dropped.
3. **Nonmaterial clarification:** M241's `36sqrt(x)/R` intermediate strip
   bound implicitly uses `2sqrt(2)<3`; this is harmless slack.

Final verdict: **ACCEPT** R1--R3 and only their `SG=128`, `GG2=70`
consequences.  `YCM`, `WBE`, `DE`, `J2`, `PCR`, gap, mixing, and both
Terminals remain open.
