# M82 plan: deep-eliminated reset substochasticity

Date: 2026-08-12. Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and scope

This mission concerns only the full nonlazy stationary-flow parking-degree
projection `Pbar_r` in the minimal factorization sector of the long cycle.
It does not concern the original lazy `{3,4,5}` identity-word heat-bath
chain `K`.

For a contextual mark `x=(s,K,R,B)`, use M65/M71's exact deep kernel `D`
and M50's first-boundary canonical reset kernel `J_can`, with

```text
K_reset=(I-D)^(-1)J_can.
```

The primary claim to prove or refute is

```text
K_reset 1(x)<=1
```

for every right-heavy reachable reset seed `x=(s,K,K-1,B)`.  The preferred
stronger claim is

```text
K_reset 1(x)<=(K-R)(1-q_x),
q_x=w_(s+1-B)w_B/w_(s+1),
```

for every reachable contextual mark.  Raw one-step Bellman inequalities
are known false and will not be reused.

## Method

1. Reproduce M79's exact rational scan and grouped Cayley-coefficient scan,
   independently recording ordinary row masses and the proposed bound.
2. Rewrite `(I-D)^(-1)J_can 1` as a sum over complete pure-deep histories
   and identify the canonical basin currents as conditional-expectation or
   Haar increments on an augmented attachment/composition tree.
3. Test exact identities suggested by that interpretation: total variance,
   Efron--Stein/Haar orthogonality, and first-reset event mass.  Any claimed
   identity will be checked on all contexts through at least `s=7,K<=6`.
4. If the bound fails, extract an exact finite or infinite counterfamily and
   isolate the weakest viable occupation potential.  If it holds, state the
   universal proof, strict-`P` nilpotence, and the conditional
   `O(P^3 log P)` marked-occupation implication without claiming a `Pbar`
   or `K` gap.

## Exact conventions and diagnostics

- Permutations compose as `(pq)(x)=p(q(x))`; factors are displayed
  left-to-right.
- Root-composition weights are
  `rho_s(C)=prod_i w_(c_i)/(k! w_(s+1))`, `w_a=a^(a-1)/a!`.
- Reset coefficients are `theta_e^2/[Q_G(e)q_x]`, with
  `Q_G(e)=rho_s(refined) k`.
- Deep coefficients retain the exact negative-hypergeometric mark weight.
- Exact bounded scans use `fractions.Fraction`; grouped larger scans are
  explicitly empirical finite diagnostics.
- Seed: `null` (deterministic). Python: `3.12.3`.

## Expected failure modes

- Canonical path currents need not be orthogonal, even after deep
  elimination.
- A multitype inequality may fail away from the right-heavy reachable set.
- Binary64 grouped calculations may hide a near-one violation; decisive
  signs will be certified exactly.
- A row-mass bound proves only separated marked occupation; actual-edge
  unmarking and all upstream comparison dependencies remain separate.

