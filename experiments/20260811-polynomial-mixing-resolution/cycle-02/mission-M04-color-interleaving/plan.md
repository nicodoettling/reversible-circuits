# M04 recycled lane: fixed-content color interleavings

## Exact target

Fix `N>=3`, even `m>=4`, and feasible labeled weighted support-component
data `alpha=((C_a,k_a))`.  Multiplication is `pq = p after q`; words are
evaluated as `t_1...t_m`.  Let `K` be the exact lazy `{3,4,5}` heat-bath
kernel from `GOAL_SPEC.md`, and let `K^alpha` be its standard rejected-exit
restriction to the macro-fiber `Omega_alpha`.

Define the stationary-flow projection of `K^alpha` through the map recording
only the fixed-content color word.  The primary claim is that this projected
chain has a universal inverse-polynomial spectral gap, uniformly over all
feasible component sets and weights.  A one-color projection is treated as a
singleton.

## Proposed comparison

1. Prove the exact product factorization of the conditional uniform law into
   a uniform multiset color word and independent uniform connected identity
   words in the components.
2. For every adjacent unequal-color pair, commute its disjoint-support
   transpositions and pad the swap into a boundary-safe length-three window.
3. Retain the exact `K` normalization and bound the length-three fiber by
   `F_3(h)<=M^2`, where `M=binom(N,2)`.
4. Compare the projected chain to the lazy adjacent-transposition walk on
   multiset permutations.  Obtain its gap as a quotient of the interchange
   process on the path, citing Caputo--Liggett--Richthammer with the path
   eigenvalue checked directly.
5. Audit endpoints, `m=4`, rare colors, one color, duplicate transition
   aggregation, rejected exits, and near-minimal component weights.

## Quantities to track

- Exact one-swap probability in `K^alpha` and in its projection.
- Dirichlet-form comparison factor and final spectral-gap exponent.
- Reference-chain path length/congestion interpretation.
- Polynomial exact-block sampling cost.

## Calibration and failure modes

Check odd `m`, `m=0`, `m=2`, `N=2`, `S_3,m=4`, `S_4,m=4`, and
`S_4,m=6`; retain the whole-word `r=4` term at `m=4`.  The proof must not
silently assume all colors have multiplicity at least two beyond feasibility,
or mistake a projected gap for a full restricted-fiber gap.  If the color
projection theorem succeeds, identify the exact remaining two-stage
restriction implication rather than claiming the global goal.

No computation is planned unless it is needed to falsify a named
normalization or aggregation claim.
