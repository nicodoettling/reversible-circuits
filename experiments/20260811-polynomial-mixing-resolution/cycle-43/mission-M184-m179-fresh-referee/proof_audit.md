# M184 independent proof audit of frozen M179

Date: 2026-08-13 UTC.

## 1. Integrity, source, and scope gate

Before reading M179's mathematical payload, I ran its complete frozen ledger.
All seven listed payloads passed, the directory inventory matched the freeze
manifest, and the `SHA256SUMS` digest was

```text
edaf37e884fbd4fb970a38ce626ef850b5eac2490fa8083ed78eb92a73c2c03d.
```

M179 was not edited.  The required project source lock was then read, and the
complete frozen ledgers for M109/M114, M115/M116, M147/M151, M157/M160,
M162/M165, and M173/M177 all passed.

The object audited below is only the normalized full unweighted reset
excursion `F=H/q` in the auxiliary nonlazy minimal-long-cycle parking
projection.  The project target remains uniform fixed-length identity
transposition words, with `(pq)(x)=p(q(x))` and displayed factors
left-to-right.  No reset-plus-descendant budget, gap, original-chain theorem,
polynomial mixing, Terminal A, or Terminal B is under audit.

## 2. Suffix-one affine collapse

At a fresh right-heavy parent

```text
xi=(B+L,2,1,B),       mu_parent=Beta(1,1),
```

fix a last-root height `h=2`, degree `d`, and retained observation `a<d`.
The accepted state update gives

```text
xi_a=(B+1,d+2,a+1,B),
mu_a=Beta(a+1,d-a+1).                              (2.1)
```

The child suffix excess is `(B+1)-B=1`.  M162/M165 proves that every
actual-history feature at suffix excess `ell` is a Hilbert-valued polynomial
of degree at most `ell`.  Hence this entire child feature lies in the span of
the constant and centered-linear modes.  With

```text
p=(a+1)/(d+2),
v=(a+1)(d-a+1)/[(d+2)^2(d+3)],
M=E_a Phi,       C=E_a[(U-p)Phi],
```

one has exactly

```text
Phi(u)=M+(u-p)C/v,       Z=0.                     (2.2)
```

Setting `V=C/sqrt(v)`, direct integration yields

```text
S_a:=E_a||Phi||^2=||M||^2+||V||^2.               (2.3)
```

This `S_a` is the full child diagonal trace.  Since the child has degree at
most one, child `T_1=F=||M||^2`; those smaller quantities are not the
quadratic form used in M179's operator comparison.

## 3. Exact Bayes-normalized branch matrix

Let

```text
L_a(u)=binom(d,a)u^a(1-u)^(d-a),
pi_a=E_parent L_a=1/(d+1),
delta=p-1/2.
```

The actual-history coordinate is

```text
f_a=sqrt(eta/pi_a)L_a Phi.
```

Bayes' identity `L_a dmu_parent=pi_a dmu_a` must be applied after one
likelihood remains in the trace.  It gives

```text
E_parent||f_a||^2
 =(eta/pi_a)E_parent[L_a^2||Phi||^2]
 =eta E_a[L_a||Phi||^2],                          (3.1)

E_parent[(U-1/2)f_a]
 =sqrt(eta*pi_a)(delta M+C).                      (3.2)
```

Thus the parent first-mode subtraction is exactly
`12 eta pi_a||delta M+C||^2`, including its signed cross term.  Observation
`a=d` is the killed attachment rank and is absent before any direct-sum norm
is taken; there is no conditioning on survival.

Multiplying the child beta density by `L_a` produces the second posterior

```text
Betahat=Beta(2a+1,2d-2a+1),
phat=(2a+1)/[2(d+1)],
vhat=(2a+1)(2d-2a+1)/[(2d+2)^2(2d+3)].            (3.3)
```

Define

```text
lambda_0=E_a L_a
 =(d+1)/(2d+1) binom(d,a)^2/binom(2d,2a),
lambda_1=lambda_0(phat-p),
lambda_2=lambda_0[vhat+(phat-p)^2].               (3.4)
```

Expanding (3.1)--(3.2) in `(M,V)` gives, after division by `eta`,

```text
B_(d,a)=<(M,V),G_(d,a)(M,V)>,                     (3.5)

G_(d,a)=
 [ lambda_0          lambda_1/sqrt(v) ]
 [ lambda_1/sqrt(v)  lambda_2/v         ]
 -12pi_a
 [ delta^2           delta sqrt(v)      ]
 [ delta sqrt(v)     v                  ].        (3.6)
```

This is a scalar matrix tensored with the history Hilbert identity, so its
ordinary largest eigenvalue is the generalized eigenvalue relative to (2.3).
The clean-room checker recomputes (3.1) directly at the asymmetric row
`(d,a,M,C)=(5,3,-4/7,5/13)` and obtains the same charge as (3.4)--(3.6),
including the cross term.

## 4. Independent Loewner audit

For `(d,a)=(1,0)`, direct substitution gives

```text
p=1/3, v=1/18, delta=-1/6, pi=1/2,
lambda_0=2/3, lambda_1=-1/18, lambda_2=4/135,
G_(1,0)=diag(1/2,1/5).                             (4.1)
```

Hence the exact degree-one factor is `1/2`.

Now let `d>=2`.  Vandermonde's convolution contains
`binom(d,a)^2` as one nonnegative summand of `binom(2d,2a)`, so

```text
lambda_0<=lambda_*=(d+1)/(2d+1).                  (4.2)
```

The positive part of (3.6) is

```text
lambda_0 E_Betahat[(1,(U-p)/sqrt(v))
                   (1,(U-p)/sqrt(v))^T].          (4.3)
```

Therefore increasing `lambda_0` to `lambda_*` increases `G` in Loewner
order while leaving the covariance subtraction unchanged.  Let the resulting
upper matrix be `G_*`, put `x=(2a-d)^2`, and set
`R=(2/3)I-G_*`.  Independent simplification gives

```text
R_00=
 [(d-1)(d+1)(d+2)^2+(18d+9)x]
 /[3(d+1)(d+2)^2(2d+1)]>0,                       (4.4)

R_11=N_11/
 [3(d+1)(d+2)^2(d+3)(2d+1)(2d+3)],               (4.5)

N_11=5d^6+44d^5+180d^4+424d^3+562d^2+360d+72
     -(36d^2+72d+27)x.
```

Since `0<=x<=d^2`, the second numerator is at least

```text
(d+1)(5d^5+39d^4+105d^3+247d^2+288d+72)>0.      (4.6)
```

The determinant is

```text
det R=P_d(x)/
 [9(d+1)(d+2)(d+3)(2d+1)^2(2d+3)((d+2)^2-x)],    (4.7)

P_d(x)=A_0+A_1x-A_2x^2,
A_0=(d-1)(d+2)^3(5d^4+24d^3+64d^2+72d+18),
A_1=-5d^6+43d^5+480d^4+1658d^3
    +2729d^2+2025d+414,
A_2=90d^3+387d^2+603d+216.                        (4.8)
```

The denominator is positive on the full interval because
`(d+2)^2-x>=(d+2)^2-d^2=4(d+1)`.  Since `A_2>0`, `P_d` is concave.  Its
endpoint values are

```text
P_d(0)=A_0>0,
P_d(d^2)=(d+1)(2d+1)
 (d^5+152d^4+557d^3+658d^2-216d-144)>0.          (4.9)
```

For completeness, the only negative portion of the final factor is already
dominated by `658d^2-216d-144`, which is positive at `d=2` and increasing
thereafter.  Concavity now gives `P_d(x)>0` on `[0,d^2]`.  Equations
(4.4)--(4.9) prove `R` positive definite and therefore

```text
B_(d,a)<=2S_a/3       (d>=2,a<d).                 (4.10)
```

No separate bound on `M` and `C` has been taken.

## 5. Actual-history-only child trace

It remains to bound `S_a` for the actual suffix-one history, not for an
arbitrary affine input.  Let `B>=2` and write

```text
y=w_B/w_(B+1),       b=w_B/w_(B+2),
h=B/(B+2),           z=1/(d+3).                   (5.1)
```

At `s=B+1`, the only nonzero contextual root values are those of `(1,B)`
and the unary root.  The canonical basin of `(1,B)` has mass `b/2` and
capacity `b`; dividing its current by `sqrt(qc)=b` gives the exact reset
coordinate

```text
U-b/2.                                                (5.2)
```

All other reset currents are constant.  For an ordinary endpoint `e`, its
squared normalized constant is

```text
b rho(B_e)^2/c_e<=b rho(B_e),                       (5.3)
```

by the accepted basin ratio `rho(B_e)/rho(e)<=degree(e)`.  Total basin mass
with path multiplicity is `h`; the exceptional basin uses `b/2`.  Thus the
ordinary reset trace is at most `b(h-b/2)`.

The sole live descendant is the unary root.  Its normalized exterior is
exactly one:

```text
[w_(B+1)/w_(B+2)] [w_B/w_(B+1)]/[w_B/w_(B+2)]=1.
```

The retained likelihood is `1-U`, with probability `1-p`.  Its suffix-zero
child feature `Phi_0` is constant, and M109/M114 gives
`||Phi_0||^2<=1-y`.  Hence the descendant coordinate is
`(1-U)Phi_0/sqrt(1-p)`.  Since `Var(U)=p(1-p)z`, the full trace obeys

```text
S_a<=b(h-b/2)+(p-b/2)^2+p(1-p)z
     +(1-p+pz)(1-y).                               (5.4)
```

For `d=1`, `p=1/3,z=1/4`.  Using `h-p<=2/3`, `b<=y^2`, and dropping
`-b^2/4` bounds (5.4) by

```text
11/12+(2/3)y^2-(3/4)y.
```

This is at most `3/4` because `8y^2-9y+2<=0` on the accepted interval
`1/3<y<=2/3`.

For `d>=2`, (5.4) is convex in `p`.  On the retained interval its upper
endpoint exceeds its lower endpoint by a positive multiple of

```text
(1-z)y-b=y(1-z-w_(B+1)/w_(B+2))>0,                (5.5)
```

using `z<=1/5` and the decreasing Cayley ratio bound
`w_(B+1)/w_(B+2)<=9/16`.  The maximum is therefore at
`p=d/(d+2)`.  To use the remaining bounds sign-safely, first combine the
first two terms in (5.4) as

```text
p^2+b(h-p)-b^2/4<=p^2+b(1-p)<=p^2+3(1-p)/8.       (5.6)
```

Then `1-y<=2/3` gives

```text
S_a<=p^2+3(1-p)/8+p(1-p)z+(2/3)(1-p+pz).
```

With `p=(1-3z)/(1-z)`, this upper bound minus one is

```text
z(16z-5)/[4(1-z)]<=0.                             (5.7)
```

Thus `S_a<=1`.  Finally, if `B=1`, there is no active reset endpoint at
`s=2`, and the unary target has rank one.  Both feature sectors are absent,
so `S_a=0`.  This proves exactly the history-specific bounds

```text
S_a<=3/4  (d=1),       S_a<=1  (d>=2).             (5.8)
```

The clean-room checker reconstructs the reset currents and basin traces from
composition definitions at eight named rows and independently verifies the
exceptional coordinate, ordinary bound, descendant envelope, and `B=1`
zero boundary.

## 6. Exterior normalization and quarter aggregation

Put `n=L-2`, `r=d-1`.  A root of height two has last part `B+2`; summing all
prefixes of total `n` and length `r` gives

```text
m_group=w_(B+2)c(n,r)/[(r+1)!w_(B+L+1)].          (6.1)
```

The child and parent splits are

```text
q_child=w_B/w_(B+2),
q_parent=w_(n+3)w_B/w_(B+L+1).
```

Consequently the normalized exterior is exactly

```text
eta^(2)_(n,r)=m_group q_child/q_parent
 =c(n,r)/[(r+1)!w_(n+3)].                         (6.2)
```

There is no observation, survival, or extra split factor in (6.2).

At `n=0`, only `(r,d)=(0,1)` occurs and `eta=1/w_3=2/3`.  Equations (4.1)
and (5.8) give the separate boundary

```text
(2/3)(1/2)(3/4)=1/4.                              (6.3)
```

For `n>=1`, `r=1,...,n`, including `r=n` with `c(n,n)=1`.  The binomial
identity

```text
sum_(r=1)^n c(n,r)/r!=(n+1)^(n-1)/n!
```

and the definition of `w_(n+3)` give

```text
sum_(r=1)^n(r+1)eta^(2)_(n,r)
 =(n+1)^n(n+2)/(n+3)^(n+1).                       (6.4)
```

Bernoulli's inequality bounds (6.4) by

```text
(n+1)(n+2)/[(3n+1)(n+3)]<=3/8,
```

where the final cleared slack is `(n-1)(n+7)`.  Degree `d=r+1` has exactly
`d` retained observations.  Applying (4.10) and (5.8) to each
observation-dependent child before summing gives

```text
T_1^(h=2)(xi)
 <=(2/3)sum_(r=1)^n(r+1)eta^(2)_(n,r)
 <=1/4.                                           (6.5)
```

No common-vector assumption or scalar child-`T_1` replacement appears.

## 7. Numbered objections and disposition

1. **Material objections: none.**  Every frozen theorem-critical identity,
   inequality, normalization, and boundary passed independent derivation.
2. **Nonmaterial proof-detail clarification:** M179's transition to its
   trace bound (5.10) is sign-safe after the `b`-terms are first combined as
   in (5.6).  The frozen result is correct; displaying this intermediate
   line would make the monotonic substitutions immediate.
3. **Nonmaterial proof-detail clarification:** positivity of the final
   determinant endpoint in M179 (4.10) follows uniformly because
   `658d^2-216d-144>0` already at `d=2` and is increasing.  No hidden finite
   base check is needed.
4. **Scope guard:** the accepted statement covers only fresh actual-history
   `h=2` descendants.  It contains no parent reset, `h>=3`, total AMV,
   nonfresh, all-suffix, gap, or project-terminal conclusion.

```text
FINAL REFEREE VERDICT: ACCEPT FROZEN M179'S STRICT h=2 SECTOR THEOREM.
```

## 8. Reproducibility

Run from this M184 directory:

```text
python3 -B independent_exact.py --output independent_results.json
```

The script uses Python standard-library `Fraction` arithmetic, imports no
M179 or predecessor code/data, and reports `status=pass`, `failures=[]`.  It
checks one new asymmetric Bayes/cross-term specialization, the exact
degree-one matrix, eight selected Loewner rows and their factor identities,
eight reconstructed actual-history trace rows, five direct exterior
cancellations, and four first moments through `L=6`.  It performs no `L=7`,
`h>=3`, or broad enumeration.  The universal conclusion rests on the
analytic proof above, not on the finite rows.
