# M71 plan: marked weighted Green contraction

Date: 2026-08-12.  Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and scope

The target is the full **nonlazy** stationary-flow parking-degree
projection `Pbar_r` in the minimal factorization sector of
`(0 1 ... r)`, with stationary law

```text
pi_r(d)=r!/[(r+1)^(r-1) product_i d_i!].
```

This is an auxiliary chain, not the original fixed-length uniform identity
bridge chain `K`.  Permutations compose as `(pq)(x)=p(q(x))`; factor tuples
multiply left-to-right.

Starting from frozen/refereed M56 and M65, replace the refuted scalar
recurrence based on `delta+a` by its exact child-rank-resolved form.  The
primary claim to test is:

> There is a fixed exponent `p` for which the deep-continuation mass and
> the quotient electrical energy, each weighted by the actual lower child
> rank to the power `p`, contract relative to `s^p` uniformly over every
> contextual mark `(K,R;B)`.

If this survives, prove the resulting separated-capacity Green induction
and then bound the collision incurred when marked histories are forgotten.
If it fails, seek an explicit infinite obstruction and determine whether
it defines a consistent function/cut on unmarked `Pbar_r` states.  After
the rank-only template was refuted, the frozen continuation is to use the
M50 first-boundary canonical flow, retain `(K,R,B)`, and seek a
suffix-excess/actual-edge occupation estimate rather than return to a
scalar maximum recurrence.

## Exact normalization under test

Use `G_s=R_s/alpha_s`, where

```text
alpha_s=2/[3s(s-1)],
rho_s(C)=Z_s^(-1) [1/(number of parts)!] product_i w_(c_i),
w_t=t^(t-1)/t!.
```

For `H(C)=E[Phi_(K,R;B)|C]`, solve

```text
(-G_s) u = H-E H,
```

in the mean-zero space.  For a quotient edge merging adjacent parts
`A,B`, attach lower rank `A+B-1`; for deep continuation through last part
`t>B`, attach lower rank `t-1`.  Retain the exact stationary-flow edge
capacity `rho(C)G_s(C,C')` and the standard undirected Dirichlet
normalization.

## Work plan

1. Derive the rank-resolved recurrence from M56 without taking a maximum
   over child ranks; audit every `alpha/gamma`, stationary-flow, and
   electrical-energy factor.
2. Build a bounded exact-state/numerical falsifier for the weighted
   coefficient over all compositions through feasible small `s`, scanning
   contextual `(K,R;B)` including the M65 right-heavy family.  These tests
   are falsifiers only.
3. Prove a universal polynomial Lyapunov contraction, or exhibit a family
   for which every fixed polynomial rank weight fails.
4. Separately audit unmarking: count sufficient context labels at an actual
   edge and determine whether grouping by current marks avoids exponential
   history multiplicity.  Do not turn a synthetic history into a state
   observable without a consistency proof.
5. Freeze a halfway checkpoint and a nine-field final report, including
   boundary ranks, probability/path/congestion accounting, dependencies,
   strongest self-attack, reproduction commands, and a scoped verdict.

## Expected failure modes

- The electrical optimizer may put substantial energy on edges whose
  merged part has rank `s-O(1)`, defeating every fixed polynomial weight.
- A favorable separated-capacity contraction may still fail after
  unmarking because histories with different synthetic `(K,R)` labels
  collide on the same actual edge.
- A bad marked coefficient need not yield a slow mode: the mark may not be
  state-measurable, and literal ambient fibres have inverse-polynomial
  root-merge escape.
- Finite spectral or Green calculations cannot prove a universal bound.

## Computation record

Any new script and machine-readable output will live in this directory.
No random sampling is planned; seed is `null`.  Python/dependency versions,
the exact command, commit, residuals, and finite-scope warning will be
recorded in raw output.
