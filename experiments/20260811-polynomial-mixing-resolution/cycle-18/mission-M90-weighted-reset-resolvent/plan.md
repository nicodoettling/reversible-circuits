# M90 plan: weighted deep-eliminated reset resolvent

Date: 2026-08-12. Frozen predecessor base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and exact scope

This mission concerns only the full nonlazy stationary-flow parking-degree
projection `Pbar_r` in the minimal long-cycle factorization sector. It makes
no claim about the original lazy `{3,4,5}` same-product heat-bath kernel `K`.

For every active reachable right-heavy seed `x=(s,K,K-1,B)`, test and seek a
proof or exact refutation of

```text
K_reset W(x) <= W(x),
K_reset=(I-D)^(-1)J_can,
W(x)=(1-q_x)K/(R+1),
q_x=w_(s+1-B)w_B/w_(s+1).
```

M82's normalization is frozen: both `D` and `J_can` retain division by the
parent `q_x`; `J_can=theta_e^2/[Q_G(e)q_x]`. The phase is
`P(x)=s+K-R`, and every retained child strictly lowers `P`, so the resolvent
is the finite DAG sum `sum_(d>=0)D^dJ_can`.

## Method

1. Derive an exact grouped recurrence for
   `F(x)=K_reset W(x)=J_can W(x)+D F(x)`, grouping compositions by the Cayley
   coefficient and aggregating identical child contexts before recursion.
2. Audit that recurrence against direct exact enumeration at small ranks and
   against M82/M87's frozen values.
3. Search right-heavy seeds beyond the previously tested ranks using exact
   rational arithmetic. Floating or asymptotic scans may select candidates,
   but every reported sign is certified exactly and finite survival is never
   promoted to a theorem.
4. Analyze scaled/asymptotic regimes suggested by the extrema. If the
   inequality survives, seek a whole-excursion telescoping or filtration
   identity; raw constant and `P^dW`, `d=0,1,2`, Bellman templates are treated
   as refuted and will not be reused.
5. If a right-heavy counterexample appears, freeze the smallest exact witness
   and stop the universal claim. Otherwise state the first remaining
   standalone proof obligation without claiming an auxiliary `Pbar` gap.

## Exact conventions and reproducibility

- `w_a=a^(a-1)/a!` and
  `rho_s(C)=prod_i w_(c_i)/[k! w_(s+1)]`.
- The negative-hypergeometric attachment probability is exactly M82 Field 2.
- Permutations compose as `(pq)(x)=p(q(x))`; tuple factors are displayed
  left-to-right.
- Deterministic computation, seed `null`, Python `3.12.3`, standard library
  only unless the final metadata reports otherwise.
- Exact raw output is machine-readable JSON; every owned artifact receives a
  SHA-256 digest. Python is invoked with `-B`, and cache hygiene is checked.

## Expected failure modes

- Exact `Fraction` denominators may dominate before ranks large enough to
  expose an asymptotic reversal.
- Grouping by `(k,t,j)` may still leave too many contextual descendants;
  identical child coefficients must be merged before recursive evaluation.
- A positive event interpretation for one reset edge may fail to telescope
  across overlapping canonical basins.
- A finite margin below one, even at much larger ranks, proves no universal
  inequality.
- Any conclusion applies only to separated marked occupation for the
  auxiliary `Pbar` route and remains conditional on all upstream comparison
  inputs.
