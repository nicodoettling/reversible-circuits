# M179 fresh actual-history `h=2` affine-sector theorem

Date: 2026-08-13 UTC.

## 1. Scope and status

This note concerns only the normalized full unweighted reset excursion
`F=H/q` in the auxiliary nonlazy minimal-long-cycle parking projection.  The
project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors
left-to-right.

The following standalone statement is **proved**:

> At every fresh right-heavy parent, the complete retained actual-history
> descendant sector whose last-root height is exactly `h=2` contributes at
> most `1/4` to the parent's first-Jacobi remainder `T_1`.

The proof retains the exact affine child mean--covariance cross term and the
exact killed observation `a=d`.  The matrix comparison is to the child's
full diagonal trace `S=E_child ||Phi||^2`, not to child `T_1` or `F`.  The
subsequent bound on `S` uses the explicit actual-history suffix-one feature;
it is not a generic affine-operator supremum.

This theorem contains neither the parent reset term nor any `h>=3` term.  It
does not prove a total parent budget, the all-suffix boundary, a gap, an
original-chain result, polynomial mixing, Terminal A, or Terminal B.

## 2. Fresh parent and exact affine collapse

Fix

```text
xi=(B+L,2,1,B),       U_parent~Beta(1,1),          (2.1)
```

and a live root group with last part `t=B+2` and degree `d`.  For a retained
observation `a=0,...,d-1`, M162/M165's accepted child is

```text
xi_a=(B+1,d+2,a+1,B),
mu_a=Beta(a+1,d-a+1).                              (2.2)
```

Its suffix excess is exactly one.  The accepted feature-degree theorem
therefore makes the full actual-history child feature affine, with no
residual tail:

```text
p=(a+1)/(d+2),
v=Var_mu_a(U)=(a+1)(d-a+1)/[(d+2)^2(d+3)],

Phi_a(u)=M_a+(u-p)C_a/v,       Z_a=0,              (2.3)
M_a=E_mu_a Phi_a,
C_a=E_mu_a[(U-p)Phi_a].
```

Put `V_a=C_a/sqrt(v)`.  Finite vector Parseval, here simply direct affine
integration, gives the exact child trace

```text
S_a:=E_mu_a ||Phi_a(U)||^2=||M_a||^2+||V_a||^2.   (2.4)
```

This is the denominator quadratic form used below.  In particular, it is
not `T_1(xi_a)=||M_a||^2` and is not `F(xi_a)=||M_a||^2`.

## 3. Exact retained-branch matrix

At the fresh parent,

```text
pi_a=E_parent L_(d,a)=1/(d+1),
delta=p-1/2,
sigma_parent^2=1/12.                               (3.1)
```

As in M173/M177, the sensitive trace normalization is

```text
(eta/pi_a)E_parent[L_(d,a)^2 ||Phi_a||^2]
 =eta E_mu_a[L_(d,a)||Phi_a||^2].                 (3.2)
```

Let the second posterior proportional to `L_(d,a)dmu_a` have mean and
variance

```text
phat=(2a+1)/[2(d+1)],
vhat=(2a+1)(2d-2a+1)/[(2d+2)^2(2d+3)].            (3.3)
```

Then

```text
lambda_0=E_mu_a L_(d,a)
 =(d+1)/(2d+1) * binom(d,a)^2/binom(2d,2a),
lambda_1=lambda_0(phat-p),
lambda_2=lambda_0[vhat+(phat-p)^2].                (3.4)
```

M173's exact six-term formula has `Z_0=Z_1=Z_2=0` here.  After dividing the
parent branch contribution by its exterior `eta`, it is the quadratic form

```text
B_(d,a)=<(M_a,V_a), G_(d,a)(M_a,V_a)>,             (3.5)

G_(d,a)=
 [ lambda_0              lambda_1/sqrt(v) ]
 [ lambda_1/sqrt(v)      lambda_2/v         ]
 -12 pi_a
 [ delta^2               delta sqrt(v)      ]
 [ delta sqrt(v)         v                  ].     (3.6)
```

For Hilbert-valued `M_a,V_a`, (3.5) means the same scalar matrix tensored
with the identity.  Thus its largest generalized eigenvalue relative to the
child trace quadratic form (2.4) is the ordinary largest eigenvalue of
`G_(d,a)`.  The covariance subtraction in (3.6) keeps the exact
`2 delta <M_a,C_a>` cross term.  Observation `a=d` is killed and is absent;
there is no survival conditioning.

## 4. Uniform `2x2` operator bound

> **Lemma 4.1.** For the retained fresh branch,
>
> ```text
> B_(1,0)<=1/2 S_0,
> B_(d,a)<=2/3 S_a       (d>=2, 0<=a<d).           (4.1)
> ```

**Degree one.** Direct substitution gives

```text
G_(1,0)=diag(1/2,1/5),                             (4.2)
```

so the first line of (4.1) follows.

**All degrees `d>=2`.** Vandermonde gives

```text
binom(d,a)^2<=binom(2d,2a),
lambda_0<=lambda_*:=(d+1)/(2d+1).                 (4.3)
```

The first matrix in (3.6), divided by `lambda_0`, is the second-posterior
expectation of an affine vector outer product and is positive semidefinite.
It is therefore enough, in Loewner order, to replace `lambda_0` by
`lambda_*` in all of `lambda_0,lambda_1,lambda_2`.  Call the resulting
upper matrix `G_*`.

Put

```text
t=2a-d,       x=t^2,       0<=x<=d^2.              (4.4)
```

For the slack `S_*=(2/3)I-G_*`, exact simplification gives

```text
(S_*)_00=
 [(d-1)(d+1)(d+2)^2+(18d+9)x]
 /[3(d+1)(d+2)^2(2d+1)],                          (4.5)
```

and

```text
(S_*)_11=N_11/
 [3(d+1)(d+2)^2(d+3)(2d+1)(2d+3)],                (4.6)

N_11=
 5d^6+44d^5+180d^4+424d^3+562d^2+360d+72
 -(36d^2+72d+27)x.
```

The first diagonal is positive.  The second is minimized at `x=d^2`, where

```text
N_11(d^2)
 =(d+1)(5d^5+39d^4+105d^3+247d^2+288d+72)>0.    (4.7)
```

The determinant is

```text
det S_*=P_d(x)/
 [9(d+1)(d+2)(d+3)(2d+1)^2(2d+3)((d+2)^2-x)],    (4.8)

P_d(x)=A_0+A_1 x-A_2 x^2,

A_0=(d-1)(d+2)^3
    (5d^4+24d^3+64d^2+72d+18),
A_1=-5d^6+43d^5+480d^4+1658d^3
    +2729d^2+2025d+414,
A_2=90d^3+387d^2+603d+216.                        (4.9)
```

The denominator in (4.8) is positive and `P_d` is concave in `x`.  Its two
endpoint values on `[0,d^2]` are

```text
P_d(0)=A_0>0,
P_d(d^2)=(d+1)(2d+1)
 (d^5+152d^4+557d^3+658d^2-216d-144)>0           (4.10)
```

for every `d>=2`.  Concavity therefore gives `P_d(x)>0` throughout the
interval.  Equations (4.5)--(4.10) prove `S_*` positive definite.  Thus
`G_(d,a)<=G_*<=2I/3`, proving (4.1).  This comparison preserves the
mean--covariance cross term; `M_a` and `C_a` were never bounded separately.
QED.

## 5. Actual-history suffix-one trace envelope

The operator lemma still requires a bound on the actual child trace `S_a`.
This section uses the exact history feature at (2.2), not an arbitrary
affine function.

First let `B>=2` and abbreviate

```text
w_j=j^(j-1)/j!,
y=w_B/w_(B+1),        b=w_B/w_(B+2),
h=B/(B+2),            z=1/(d+3).                  (5.1)
```

The child split is `q_child=b`.  At suffix excess one, the only nonzero
contextual root values occur on `(1,B)` and the unary root.  The canonical
basin of `(1,B)` has mass `b/2` and capacity `b`, so its normalized reset
feature is exactly

```text
u-b/2.                                                   (5.2)
```

Every other reset coordinate is constant.  The accepted canonical-basin
bound `basin mass/capacity<=1`, together with total stationary path height
`h`, bounds the sum of their squared constants by

```text
b(h-b/2).                                           (5.3)
```

There is exactly one live deep group: the unary root.  Its grouped exterior
is one, its retained likelihood is `1-u`, and its probability is `1-p`.
Its suffix-zero child feature `Phi_0` is constant by the degree theorem and
the accepted all-deficit boundary gives

```text
||Phi_0||^2=F_0<=1-y.                              (5.4)
```

Consequently the sole descendant coordinate is exactly

```text
(1-u)Phi_0/sqrt(1-p).                              (5.5)
```

Using `Var(U)=p(1-p)z`, (5.2)--(5.5) give the full actual-history trace
envelope

```text
S_a<=Sbar_(B,d,a)
 :=b(h-b/2)+(p-b/2)^2+p(1-p)z
   +(1-p+pz)(1-y).                                 (5.6)
```

The last multiplier is exact because
`E(1-U)^2/(1-p)=1-p+pz`.

> **Lemma 5.1.** For the actual child (2.2),
>
> ```text
> S_0<=3/4                         if d=1,
> S_a<=1                           if d>=2,a<d.     (5.7)
> ```

**Degree one.** Here `p=1/3,z=1/4`.  The decreasing Cayley ratios give

```text
1/3<y<=2/3,       b<=y^2,       h-p<=2/3.
```

After discarding the negative `-b^2/4`, (5.6) is at most

```text
11/12+(2/3)y^2-(3/4)y<=3/4,                       (5.8)
```

because `8y^2-9y+2<=0` on `[1/3,2/3]`.

**Degrees at least two.** Expression (5.6) is convex in `p`.  The retained
range is

```text
1/(d+2)<=p<=d/(d+2).
```

The value at the upper endpoint minus the value at the lower endpoint has
the sign of

```text
(1-z)y-b=y(1-z-w_(B+1)/w_(B+2))>0,                (5.9)
```

since `z<=1/5` and `w_(B+1)/w_(B+2)<=9/16` for `B>=2`.  Hence the maximum
is at `p=d/(d+2)`.  Now use

```text
h<=1,       b<=3/8,       1-y<=2/3
```

in (5.6) to obtain

```text
Sbar<=p^2+(3/8)(1-p)+p(1-p)z
      +(2/3)(1-p+pz).                              (5.10)
```

Writing `p=(1-3z)/(1-z)`, the right side minus one is

```text
z(16z-5)/[4(1-z)]<=0                              (5.11)
```

because `z<=1/5`.  This proves (5.7) for `B>=2`.

If `B=1`, the actual suffix-one state has rank two.  Its reset target and
its deep unary target both have rank one and are inactive, so its entire
feature is zero: `S_a=0`.  This is a separate activity boundary, not an
application of the `B>=2` envelope.  QED.

## 6. Exact `h=2` exterior and quarter theorem

Put

```text
n=L-2,        r=d-1.                              (6.1)
```

Here `c(0,0)=1` and, for `1<=r<=n`,
`c(n,r)=r n^(n-r-1)/(n-r)!`.

For `n=0`, only `(r,d)=(0,1)` occurs.  For `n>=1`, the prefix of total `n`
has length `r=1,...,n`, so `d=r+1`.  Summing the root masses over such
prefixes and multiplying the exact child/parent split ratio gives

```text
m_group=w_(B+2)c(n,r)/[(r+1)!w_(B+L+1)],
q_child/q_parent=
 [w_B/w_(B+2)]/[w_(n+3)w_B/w_(B+L+1)],

eta^(2)_(n,r)=m_group q_child/q_parent
 =c(n,r)/[(r+1)!w_(n+3)].                         (6.2)
```

Thus the exterior is independent of `B`.  There is no extra observation,
split, or survival factor; `pi_a` has already been incorporated in the
branch matrix.  The killed `a=d` observation remains absent.

At `n=0`, `eta^(2)_(0,0)=1/w_3=2/3`.  Lemmas 4.1 and 5.1 give

```text
T_1^(h=2)(xi)<=(2/3)(1/2)(3/4)=1/4.               (6.3)
```

For `n>=1`, the binomial theorem gives, including `r=n`,

```text
sum_(r=1)^n c(n,r)/r!=(n+1)^(n-1)/n!,

sum_(r=1)^n (r+1)eta^(2)_(n,r)
 =(n+1)^n(n+2)/(n+3)^(n+1).                       (6.4)
```

Bernoulli's inequality yields

```text
(1+2/(n+1))^n>=(3n+1)/(n+1),
```

and hence the last expression in (6.4) is at most

```text
(n+1)(n+2)/[(3n+1)(n+3)]<=3/8,                    (6.5)
```

where the final cleared difference is `(n-1)(n+7)>=0`.

For each degree `d=r+1>=2`, there are exactly `d` retained observations.
Applying Lemmas 4.1 and 5.1 coefficientwise therefore gives

```text
T_1^(h=2)(xi)
 =sum_(r=1)^n eta^(2)_(n,r) sum_(a=0)^(r) B_(r+1,a)
 <=(2/3)sum_(r=1)^n(r+1)eta^(2)_(n,r)
 <=1/4.                                           (6.6)
```

Equations (6.3) and (6.6) prove the announced theorem.  Notice that the
observation-dependent actual child traces are each bounded before summing;
no common child vector or scalar `T_1` summary is assumed.

## 7. Boundaries, dependencies, and first open lemma

- `L=0,1`: no `h=2` root exists, so this sector is zero.
- `L=2`: the separate `n=0,d=1` calculation (6.3) applies.
- `B=1`: every suffix-one child feature is zero by activity, so the sector is
  zero even though the exterior formula remains defined.
- `a=d`: killed exactly and never included.
- The result is fresh-parent only.  It uses the accepted M109/M114
  all-deficit suffix-zero boundary, M147/M151 canonical-basin inequality,
  M157/M160 actual-history kernel, M162/M165 feature and degree theorem, and
  M173/M177 exact AMV recursion.

After separately reserving the accepted `h=1` theorem and the present `h=2`
theorem, the first open positive lemma is:

> Aggregate the exact fresh-parent reset term with every `h>=3` retained
> descendant in the AMV recursion, preserving the full Hilbert-valued
> residual and every likelihood-weighted cross term, and compare only that
> aggregate with the remaining parent budget.

This is a strict narrowing of the open AMV problem, not its solution.

## 8. Compact exact audit

Run from this directory:

```text
python3 -B h2_modal_exact.py --output h2_modal_exact.json
```

The standard-library checker uses exact `Fraction` arithmetic.  It audits an
asymmetric affine cross-term specialization, the exact degree-one matrix,
selected endpoint/interior rows of the all-degree determinant identity,
named actual-history trace boundaries, and selected exterior first moments.
These finite rows audit the formulas; Sections 4--6 prove the universal
claims analytically.  No `L=7` enumeration or broad scan is used.
