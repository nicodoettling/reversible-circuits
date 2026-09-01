# M98 halfway checkpoint: nonfresh defect sign refuted

Date: 2026-08-12. Scope: the auxiliary full nonlazy stationary-flow
parking-degree projection `Pbar_s` in the minimal long-cycle sector, not the
original identity-word heat-bath chain. Permutations compose as
`(pq)(x)=p(q(x))`; factors are displayed left-to-right.

## Decisive exact result

The proposed universal nonfresh sign

```text
r_U(x)=U(x)-A(x)-Q U(x)>=0,       K>R>=1,
```

is **refuted** on a reachable right-heavy context. Retaining every attachment
rank `j=1,...,k`, exact rational arithmetic gives

```text
x=(s,K,R,B)=(16,710,709,4),
r_U(x)<0.
```

The exact numerator is

```text
-661615179812287703733401538288146672176656056694303980320445480238015535840763927227096436539021950529551118381660089830702424942161641416917615391141563,
```

over the positive denominator recorded in `defect_counterexample.json`.
Numerically, `r_U=-4.2795012885e-8` and `r_U/U=-6.3297315165e-7`.
The adjacent calibration `K=709` is positive. This adjacency is not yet a
claim that `710` is the first failure over every smaller `K`.

## Exact limiting sign decomposition

For a right-heavy context `(s,K,K-1,B)`, let `K` tend to infinity. The
negative-hypergeometric law concentrates at `j=k`, and the root conditional
mean converges to

```text
H_infty(k,t)=0                         (t<B),
              1                       (t=B,k=1),
              0                       (t=B,k>=2),
              q_(t-1,B)               (t>B).
```

Writing `m_(s,t)` for stationary last-part mass and `e_(s,t)` for the
reset-weighted canonical basin-energy coefficient in last-part fibre `t`,
the defect has the exact finite-sum limit

```text
r_infty(s,B)
 =sum_(t=1)^s [m_(s,t)-e_(s,t)] [H_infty(t)-q_(s,B)]^2.       (H.1)
```

Indeed

```text
q(1-q)-Q_infty U=Var_rho(H_infty),
A_infty=sum_t e_(s,t)[H_infty(t)-q]^2.
```

Thus (H.1) is a genuine positive/negative coefficient decomposition, not a
finite-margin extrapolation. The last-part masses are explicit:

```text
m_(s,t)=w_t A_(s-t)/w_(s+1),
A_0=1,
A_n=sum_(p>=1)[z^n]T^p/(p+1)!=n w_n/(n+1),  n>=1.
```

For the basin coefficient

```text
L_(A,ell)=sum_(p=1)^A [z^A]T(z)^p/(p+ell)!,
```

beta integration and Lagrange inversion give the positive closed form

```text
L_(A,ell)
 =1/(ell-1)! integral_0^1 (1-u)^(ell-1)
    u(u+A)^(A-1)/A! du.                            (H.2)
```

Substitution of (H.2) into the canonical endpoint sum gives the explicit
`e_(s,t)` values stored in the raw certificate.

At `(s,B)=(16,4)`, (H.1) is an exact negative rational. More explicitly,
put

```text
P(K)=r_U(16,K,K-1,4) product_(i=1)^16 (K+i)^2.
```

The right-heavy formulas show that `P` is a rational-coefficient polynomial
of degree at most `32`: terminal and deep contextual values have only factors
`K+i` in their denominators, reset energies square them, and the all-`j`
deep term introduces no exponent above two. The exact Newton coefficients

```text
Delta^d P(710),       0<=d<=32,
```

are all strictly negative, while `Delta^33 P(710)=0`. They are frozen in
`defect_counterexample.json`. Hence for every integer `n>=0`,

```text
P(710+n)=sum_(d=0)^32 Delta^d P(710) binom(n,d)<0.
```

Therefore the family

```text
(16,K,K-1,4)
```

has negative defect for **every integer `K>=710`**. This is a rigorous
explicit infinite counterfamily to the proposed nonfresh local sign. It is not a
counterexample to the full weighted resolvent inequality: later nonfresh
layers may compensate this negative defect just as the first layer can
compensate a fresh negative defect.

## Status of the second target and retained refutations

The fresh two-level sign `r_U+Qr_U>=0` has not been refuted by this result;
its accepted exact finite checks remain finite only. However, the conjunction
of the fresh and nonfresh signs no longer proves the weighted resolvent,
because the nonfresh premise is false.

Nor does the counterfamily refute either full resolvent frontier. At the
exact local-defect witness `(16,710,709,4)`, independent finite-DAG sums give

```text
weighted full-excursion ratio =0.4080533675...<1,
unweighted full-excursion ratio=0.5988444278...<1.
```

Both positive margins are exact and recorded in the raw artifact. They are
finite survival facts only. The counterexample therefore says that any proof
of the surviving weighted or stronger unweighted frontier must allow
compensation across at least two nonfresh depths; the old fresh/nonfresh
boundary-layer truncation is too short.

The earlier raw contextual-variance, local Bessel, and scalar-compensator
routes remain refuted by the frozen M90/M96 exact witnesses. No Bernoulli
random variable is inferred from the scalar shape `q(1-q)`.

## Reproduction

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M98-reset-defect-sign/defect_counterexample.py
```

The script imports no predecessor module and uses only standard-library exact
rational arithmetic. `defect_counterexample.json` records every numerator,
denominator, all-`j` normalization, last-part coefficient, and contribution.
Seed is `null`; bounded positive values are not promoted.
