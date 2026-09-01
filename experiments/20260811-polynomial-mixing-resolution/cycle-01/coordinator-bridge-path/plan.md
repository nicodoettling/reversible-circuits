# Coordinator Bridge-Path Lane

## Objective

Reduce the exact `{3,4,5}` chain to the cleanest quantitatively sufficient
fixed-endpoint path dynamics, then seek a Poincare inequality that is
polynomial in `N` and `m` and survives bipartiteness and sparse bridges.

## First target

Compare `K_{N,m}` from below, in Dirichlet form, with the lazy adjacent-pair
same-product heat-bath chain. Interpret the latter as single-prefix-site
Glauber dynamics on paths in `Cay(S_N,T_N)` from identity to identity.

## Failure modes

- confusing an off-block pointwise comparison with a mixing-time comparison;
- forgetting that the Cayley graph is bipartite;
- invoking fixed-target-graph `H`-colouring results with constants exponential
  in `|S_N|`;
- using a pair-chain slow mode as an upper bound for the larger exact chain.
