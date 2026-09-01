# M151 proof audit of frozen M147

Date: 2026-08-13 UTC.

## 1. Immutable gate and scope

All six coordinator-supplied SHA-256 values match their frozen M147 files:

```text
e760b6b7620e0278c8a21969112cb5675e268217d64d2319230f9642baecee11  report.md
6084710041b5cb0797fefc05f477bc230bc70d893bb5e8ff2bb3dad9a9004d62  all_suffix_functional_obstruction.md
bcf02d860baf08f6774f858f44ab76c3307632de90d683434e355189fcf763b6  all_suffix_exact.py
441000e76bc60c12093355bda4272ee9fefc9b621c3e4b30b30d17bcb39cb06b  all_suffix_exact.json
8989d0998e819a24dd6b22f50df75a2199b4860fede1dcdd2aacf67625a63cea  freeze_manifest.md
3fddbaf63f38f9ff014ad5f1ee6f537e4ca994c85d8c4511da6f439f91b3c96c  SHA256SUMS
```

The accepted scope is only the auxiliary unweighted full-reset excursion.
Nothing below proves an auxiliary gap, `ROOT-MEAN LIFT`, a result for the
original lazy `{3,4,5}` chain, polynomial mixing, or a project terminal.

## 2. Attachment law, child coordinates, and killing

The accepted original law is

```text
nu_(K,R,d)(j)
 =binom(R+j,j)binom(K-R-1+d-j,d-j)/binom(K+d,d).
```

Put `kappa=K+1` and `D=K-R`. Expanding the three binomial coefficients into
rising factorials gives exactly

```text
nu_(kappa,D,d)(j)
 =binom(d,j)(D)^(rise)_(d-j)(kappa-D)^(rise)_j
   /(kappa)^(rise)_d.                              (2.1)
```

Vandermonde, or the beta-binomial normalization, proves that (2.1) sums to
one for `j=0,...,d`. The child `(K+d,R+j)` has

```text
(kappa',D')=(kappa+d,D+d-j).                       (2.2)
```

Every attachment rank `j=1,...,d` is retained when the target is active.
The `j=0` branch is killed. Independently, the target is killed unless
`t>B` and `t-1>=2`; in suffix coordinates `t=B+h`, this is exactly
`h>=1` and `B+h-1>=2`. Thus M147's phrase “rank-one children” means targets
with state rank `t-1=1`, not attachment rank `j=1`. No positive attachment
rank was dropped.

Every retained child has suffix excess `h-1<L`. The recurrence therefore
terminates after at most `L` descendant steps even though `K` can increase.

## 3. Root support, group mass, and contextual mean

For `s=B+L`, write a root as `(alpha,B+h)`, where `alpha` is an ordered
composition of `L-h` and `d=length(alpha)+1`. Its stationary mass divided
by `q_(B,L)` is directly

```text
prod_i w_(alpha_i)/[d! w_(L+1)(w_B/w_(B+h))].       (3.1)
```

Summing over prefixes of length `d-1` and using
`[z^n]T(z)^p=c(n,p)` gives M147's grouped mass. There are

```text
1+sum_(n=1)^L 2^(n-1)=2^L
```

literal roots. Substitution in the accepted contextual mean gives exactly

```text
d(D)^(rise)_(d-1)/(kappa)^(rise)_(d-1),             h=0,

q_(B,h-1)[1-(D)^(rise)_d/(kappa)^(rise)_d],         h>=1.
```

The normalized mean identity can also be checked without a finite table.
With `a_p=(D)^(rise)_p/(kappa)^(rise)_p`, its numerator is

```text
sum_p c(L,p)a_p/p!
+sum_(n=0)^(L-1) sum_p c(n,p)w_(L-n)(1-a_(p+1))/(p+1)!.
```

The `a`-terms cancel because
`sum_n c(n,p-1)w_(L-n)=c(L,p)`. The remainder is

```text
[z^L] T(z) sum_(p>=0)T(z)^p/(p+1)!
 =[z^L](exp(T(z))-1)=w_(L+1),
```

using `T=z exp(T)`. Division by `w_(L+1)` proves the root mean is one for
all valid `(B,L,kappa,D)`. This confirms the all-suffix identity rather than
extrapolating the finite `L<=5` tables.

Combining (2.1)--(3.1) with `H=A_0+QH` yields M147's exact normalized
recurrence with all `j=1,...,d` terms and precisely the boundary indicator
above.

## 4. Correct one-power majorant and one notation correction

The accepted predecessor bound, after division by the parent split mass, is

```text
A_0/q <= q[C_s-sum_E a_E lambda_E]
          +sum_E theta_E^2/(q c_E),                (4.1)
```

because `b_E=c_E lambda_E`, `0<=a_E<=b_E`, and the unremoved ordinary
amount is `q(b_E-a_E)lambda_E>=0`. With

```text
cbar=c/q, abar=a/q, thetabar=theta/q,
```

the right side of (4.1) is

```text
q[C_s-q sum_E abar_E lambda_E]
 +sum_E thetabar_E^2/cbar_E.                       (4.2)
```

There is one nonmaterial typo in frozen M147 `report.md`, Field 4: it writes
`A/q<=` even though the preceding normalized recurrence uses `A=A_0/q`.
The left side there should be `A<=`; alternatively an unnormalized symbol
would require `A_0/q<=`. Frozen `all_suffix_functional_obstruction.md`,
Section 5, has the correct `A<=R` statement, and all subsequent calculations
use the correct normalization. This does not affect the theorem.

The bound is a finite context-dependent functional prescription, not a
scalar closed form: the `a_E` and `theta_E` data still depend on the state.
The substitution `C_s<3/4` is available only for `s>=100`; below that, exact
`C_s` or another valid bound is required. The rejected M131 two-power term is
not used.

## 5. Exact `L=1` obstruction and threshold

For `(s,B,L)=(3,2,1)`, the only two canonical basins give

```text
A_0/q=1/16+[2D/(K+1)-3/8]^2/4.                    (5.1)
```

The only nominal deep target is `(s',B)=(2,2)` and its reset energy is zero,
so (5.1) is the complete `H/q`, not merely a one-step value.

For `R=1`, put `p=(K-1)/(K+1)`. Since the squared term is on its positive
branch for the relevant range,

```text
H/q>5/8 iff 2p-3/8>3/2 iff p>15/16 iff K>31.
```

Thus equality is exact at `K=31`, and strict failure begins at `K=32`. For
the right-heavy state `D=1`, direct expansion shows `H/q<5/8` for every
`K>=1`. At `K=32` the exact values are

```text
H_bad /q =175033/278784,   H_bad =175033/743424,
H_good/q = 24313/278784,   H_good= 24313/743424,
H_bad-15/64=793/743424.
```

Both contexts have exactly the same `L,B,s,q,C_3=9/32,K,z` and Cayley-ratio
data; these quantities do not depend on `R`. Their exact values differ
because `D` differs. Hence a pointwise majorant dominating the bad state
cannot also remain below its local `1-q` budget. The needed new coordinate
is any equivalent deficit-sensitive coordinate; `D` or `p=D/kappa` is the
natural exact choice.

## 6. Reachability

For every target `K>=32`, the fresh right-heavy parent is
`(s,K_parent,R_parent,B)=(K+2,1,0,2)`. The literal root

```text
(1,...,1,4)
```

has `K-2` initial ones, degree `d=K-1`, last part four, and strictly positive
mass. Fresh attachment is uniform, so its `j=1` branch has probability
`1/(d+1)=1/K` and child `(3,K,1,2)`. The `j=d` branch, also of probability
`1/K`, reaches the paired right-heavy child `(3,K,K-1,2)`. The obstruction
therefore lies in the actual accepted closure at every such `K`.

## 7. Fixed-moment theorem and exact limitation

Let `n=r+1`. The difference between M147's even- and odd-parity measures is

```text
2^(-(n-1)) sum_(i=0)^n (-1)^i binom(n,i) f(1+i).
```

It vanishes for every polynomial `f` of degree at most `r=n-1`. For
`f(D)=(D)^(rise)_n`, whose leading coefficient is one, the `n`th finite
difference gives exactly

```text
(-1)^n n!/2^(n-1) !=0.
```

Choosing `kappa>=r+4` makes every support point `1<=D<=r+2<=kappa-2` a valid
active deficit. The killed `j=0` attachment mass at degree `n` is
`(D)^(rise)_n/(kappa)^(rise)_n`, so the two averaged attachment operators
differ despite agreement on all degree-`<=r` polynomial, rising-factorial,
and falling-factorial moments.

This is only an unrestricted-measure non-identifiability theorem. It does
not show that either parity measure is a single-parent attachment law or a
reachable descendant mixture, and it does not obstruct deterministic
tracking of `(kappa,D)`. M147 states this limitation correctly.

## 8. A verified next route, not a new theorem claim

Writing `X=d-j`, (2.1) is the beta-binomial law

```text
X~BetaBinomial(d,D,kappa-D),
(kappa',D')=(kappa+d,D+X).
```

Equivalently, sample `Theta~Beta(D,kappa-D)`, then
`X|Theta~Binomial(d,Theta)`; the child parameters are the posterior beta
parameters. In particular `E[X]=dD/kappa` and

```text
E[D'/kappa' | kappa,D]=D/kappa.
```

Thus `p=D/kappa` is a martingale for the full attachment law. This is a
plausible coordinate for the next deficit-aware amortization attempt. It is
not itself a contraction: the excursion subkernel kills `j=0`, so a future
argument must charge that killing explicitly rather than silently condition
it away.

