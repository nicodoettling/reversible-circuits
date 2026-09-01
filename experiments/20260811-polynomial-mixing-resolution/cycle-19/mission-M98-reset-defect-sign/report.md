# M98 final report: nonfresh reset-defect counterfamily

Date: 2026-08-12. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, convention, verdict, and scope

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. This mission concerns only the full **nonlazy
stationary-flow parking-degree projection** `Pbar_r` in the minimal
long-cycle factorization sector. It is not a theorem for the original lazy
exact same-product `{3,4,5}` heat-bath chain on identity words.

For a reachable context `x=(s,K,R,B)`, use M90's all-attachment-rank
transformed quantities

```text
Q(x,y)=rho_s(k,t)nu_(K,R,k)(j),       1<=j<=k,
U(x)=q_x(1-q_x)K/(R+1),
A(x)=sum_e [theta_e^2/Q_G(e)](1-q_(y_e)),
r_U(x)=U(x)-A(x)-Q U(x).                         (1.1)
```

The assigned statement

```text
(A) r_U(x)>=0 for every reachable nonfresh K>R>=1
```

is **REFUTED** by the explicit infinite right-heavy family

```text
x_K=(16,K,K-1,4),             every integer K>=710.             (1.2)
```

The second assigned statement

```text
(B) r_U(x)+Qr_U(x)>=0 for every fresh (K,R)=(1,0)
```

remains **UNRESOLVED**. Since (A) is false, the conjunction `(A)+(B)` can
no longer prove the weighted reset supersolution. Neither full weighted nor
full unweighted resolvent is refuted here; no `Pbar` gap, ROOT-MEAN LIFT,
Terminal A, or Terminal B is claimed.

## 2. Full proof and exact construction

For right-heavy `R=K-1`, the attachment law is

```text
nu(j)=binom(K-1+j,j)/binom(K+k,k).
```

As `K->infinity`, it concentrates at `j=k`. M65's exact conditional mean
converges to a last-part statistic

```text
H_infty(k,t)=0                 (t<B),
              1                 (t=B,k=1),
              0                 (t=B,k>=2),
              q_(t-1,B)         (t>B).             (2.1)
```

Let `m_(s,t)` be stationary last-part mass and `e_(s,t)` be the
reset-weighted canonical basin-energy coefficient in last-part fibre `t`.
The exact law-of-total-variance calculation is

```text
q(1-q)-Q_infty U=Var_rho(H_infty),                 (2.2)
```

while canonical basin summation gives

```text
A_infty=sum_t e_(s,t)[H_infty(t)-q]^2.             (2.3)
```

Therefore

```text
r_infty(s,B)=sum_t [m_(s,t)-e_(s,t)]
                    [H_infty(t)-q_(s,B)]^2.         (2.4)
```

This is a signed coefficient decomposition, not a finite-margin inference.
The coefficients have closed Cayley/Borel forms. With

```text
c(n,p)=[z^n]T^p=p n^(n-p-1)/(n-p)!,
L_(A,ell)=sum_(p=1)^A c(A,p)/(p+ell)!,
```

beta integration and Lagrange inversion give

```text
L_(A,ell)
 =1/(ell-1)! integral_0^1(1-u)^(ell-1)
    u(u+A)^(A-1)/A! du.                            (2.5)
```

Substituting (2.5) in the endpoint capacity formula gives the explicit
finite expression for every `e_(s,t)` in `right_heavy_limit.md`. At
`(s,B)=(16,4)`, (2.4) is the exact negative rational

```text
-9227444489897033899069928546555383705889289522405715688049247702588321735512746884149350887011428507035652533537
 /206939781608101554317882579170416040081179045783441942415142310077467888193085115142449958815210345070592000000000000.
```

For a concrete integer-tail proof, set

```text
P(K)=r_U(16,K,K-1,4) product_(i=1)^16(K+i)^2.
```

The displayed binomial formulas show that `P` is a rational polynomial of
degree at most `32`. Exact arithmetic gives

```text
Delta^d P(710)<0  for 0<=d<=32,       Delta^33P(710)=0.
```

Newton's series then proves `P(710+n)<0` for every integer `n>=0`, hence
(1.2). At `K=710`, the exact negative numerator is

```text
-661615179812287703733401538288146672176656056694303980320445480238015535840763927227096436539021950529551118381660089830702424942161641416917615391141563,
```

over the positive denominator frozen in `defect_counterexample.json`.
The context is reachable from fresh `(K+15,1,0,4)` through composition
`(1^(K-2),17)` and attachment rank `j=K-1`.

## 3. Probability, normalization, runtime, and occupation accounting

- Every attachment rank `j=1,...,k` is retained. No stale `j=k`-only finite
  recurrence is used; `j=k` appears alone only after the proved `K->infinity`
  limit.
- Root group mass is
  `rho_s(k,t)=w_t c(s-t,k-1)/[k!w_(s+1)]` and sums exactly to one.
- Canonical reset energy uses `theta_e^2/Q_G(e)`, with
  `Q_G(e)=rho_s(e)*(root degree)`, followed by exactly one factor
  `1-q_child` for the weighted target.
- Strict phase `P=s+K-R` lowers on every retained deep/reset child, so both
  full-resolvent checks are finite DAG sums.
- The principal exact script took about five seconds under Python `3.12.3`;
  the local-refutation recheck took under one second. Both are deterministic,
  use `seed=null`, and need no nonstandard dependency.
- The counterexample refutes a local potential sign only. It supplies no
  stationary-mass cut, comparison congestion, or spectral-gap upper bound.

## 4. Dependencies by status

- **Frozen/accepted M50/M56/M65/M69:** root-composition law, canonical basin
  current/capacity, contextual closed mean, and full
  negative-hypergeometric attachment law.
- **Frozen/accepted M71/M76/M79/M82/M87/M90/M96:** right-heavy reset
  geometry, strict phase descent, reachable closure, transformed all-`j`
  recurrence, weighted budget `U`, and the proposed boundary-layer
  sufficient conditions.
- **Proved here:** right-heavy limiting mean (2.1), variance identity (2.2),
  Cayley/Borel coefficient representation (2.5), signed decomposition
  (2.4), exact negative limit, polynomial denominator clearing, Newton tail
  certificate, and reachability of (1.2).
- **Refuted here:** universal nonfresh defect positivity (A).
- **Independently reproduced here:** raw contextual-variance failure, both
  direct Bessel failures, all eight scalar-compensator failures, and the
  non-probability contextual value `16182/6919`.
- **Exact finite only:** fresh two-level survival at the named calibration
  contexts and full weighted/unweighted survival at `K=710`.
- **Unresolved:** (B), the full weighted and unweighted reset inequalities,
  marked occupation, actual unmarked ROOT-MEAN LIFT, auxiliary `Pbar` gap,
  and every conclusion for the original heat-bath chain.

## 5. First surviving standalone proposition

The old one-layer boundary reduction is dead. A strictly broader sufficient
replacement is

> **GLOBAL TWO-LAYER DEFECT.** For every reachable active context `x`,
> ```text
> r_U(x)+(Qr_U)(x)>=0.                              (5.1)
> ```

Indeed nilpotence and positivity give the exact pairing

```text
U-g=sum_(d>=0)Q^d r_U
   =sum_(d>=0)Q^(2d)(I+Q)r_U.                      (5.2)
```

At the new negative local witness `(16,710,709,4)`, the first-layer
compensation is about `.0065140183`, so (5.1) has a positive exact margin
about `.0065139755`. This is one finite calibration, not a proof of (5.1).
Alternatively, the unchanged exact targets are the full weighted inequality
`(I-Q)^(-1)A<=U` or the stronger unweighted resolvent bound; neither has a
constructed global excursion variable yet.

## 6. Strongest self-attack

The negative local sign is not a slow mode. At the first finite witness,
independent exact DAG sums give

```text
full weighted ratio   =.4080533675130647...<1,
full unweighted ratio =.5988444277550840...<1.
```

Thus deeper compensation is large, and (1.2) does not even approach a full
resolvent violation at fixed `s=16`. The Newton proof certifies only the
local defect. Conversely, the fresh condition (B) cannot repair the old
argument, because negative defects now occur after a reset on nonfresh
right-heavy states. Finally, the scalar `q(1-q)` is not called a Bernoulli
variance: the accepted contextual statistic can exceed one away from the
right-heavy set, and its natural Bessel decompositions are exactly refuted.

## 7. Boundary cases and falsification calibrations

- Active local rank is `s>=2`, with `1<=B<=s`; the counterfamily uses
  `s=16,B=4` and valid `K>R>=1`.
- `K=709` has exact positive defect `1.9833596071e-8`; `K=710` has exact
  negative defect `-4.2795012885e-8`. The proof claims every `K>=710`
  negative, but does not claim that `710` is the first failure among every
  smaller positive integer without relying on the adjacent search.
- In the limit decomposition, last-part fibres `t=3,...,8` have negative
  coefficients; their weighted total exceeds the retained positive fibres.
- Fresh two-level blocks are independently positive at `(11,1,0,4)`,
  `(12,1,0,4)`, and `(20,1,0,6)`; these are finite checks only.
- The exact local variance failure remains `(6,2,1,2)`, with defect
  `-21394206021215/36917038301316768`.
- Odd identity length, `m=0,2`, and `N=2` are outside this auxiliary lemma;
  no new statement about those original-chain exceptional cases is made.

## 8. Artifacts, reproduction, and hygiene

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-19/mission-M98-reset-defect-sign/
```

Principal artifacts are `plan.md`, `checkpoint.md`,
`right_heavy_limit.md`, this report, and:

```text
defect_counterexample.py / .json
local_refutation_recheck.py / .json
```

Reproduction from repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M98-reset-defect-sign/defect_counterexample.py
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M98-reset-defect-sign/local_refutation_recheck.py
```

The first script imports no predecessor module. The second imports only the
owned exact core. All JSON values supporting signs include exact numerators
and denominators. Source compilation, JSON parsing, `git diff --check`,
manifest verification, and cache hygiene are checked before freeze. No
predecessor, coordinator note, manuscript, project skill, or shared source is
edited.

## 9. Final verdict and handoff

```text
VERDICT: REFUTE TARGET (A) BY AN EXPLICIT INFINITE AUXILIARY COUNTERFAMILY.
TARGET (B): UNRESOLVED.
FULL WEIGHTED/UNWEIGHTED RESET FRONTIERS: UNRESOLVED.
PBAR GAP / ORIGINAL K GAP / TERMINALS: UNRESOLVED.
```

Do not use nonfresh one-step positivity in the live proof. The clean next
falsifiable target is the global two-layer block (5.1), which pairs the
nilpotent defect expansion without distinguishing fresh from nonfresh. A
stronger route may instead prove the entire weighted or unweighted excursion
bound, but it must construct the global cancellation rather than infer a
Bernoulli variable from `q(1-q)`.
