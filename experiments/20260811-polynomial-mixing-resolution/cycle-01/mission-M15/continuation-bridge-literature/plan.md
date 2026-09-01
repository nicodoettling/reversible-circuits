# M15 continuation plan: bridge literature and map transfer

Date: 2026-08-11  
Repository commit at start: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## Objective

Audit primary sources for a theorem that would imply an inverse-polynomial gap,
uniformly in `N` and bridge length `n`, for the aligned nonlazy length-four
heat-bath chain

```text
B_{N,n}=(1/(n-1)) sum_{j=1}^{n-1} H_{2j-1,4}
```

on the uniform length-`2n` transposition identity bridge.  Under adjacent
pairing, this is single-interior-vertex heat bath for a return path with
increment law `Q_N=P_N*P_N` on `A_N`, including uniform refresh of the two
transposition microfactorizations.

In parallel, audit whether Caraceni's polynomial-gap planar-map rotation/flip
chain transfers through the Duchi--Poulalhon--Schaeffer bijection for minimal
transitive identity factorizations by a stationary-measure-preserving bounded
simulation.

## Exact tested claims

1. **Bridge-theorem transfer claim.** There is a checked primary theorem whose
   literal hypotheses hold uniformly for the pinned `Q_N` path measure and
   whose stated constants are polynomial in `N,n`, thereby proving a
   polynomial gap for `B_{N,n}`.
2. **Map-chain transfer claim.** The Duchi--Poulalhon--Schaeffer bijection maps
   uniform minimal factorizations to Caraceni's uniform state space and maps
   either chain's elementary transition to a uniformly bounded simulation of
   the other, with polynomially controlled stationary flow.
3. **Influence falsification calculation.** For the closest path-homomorphism
   Glauber theorem, compute an exact one-neighbor conditional total-variation
   influence for the `Q_N` target.  This finite computation can falsify the
   theorem's positive Dobrushin-type hypothesis for a named `N`; it cannot
   prove or refute the bridge gap itself.

## Conventions

`(pq)(x)=p(q(x))`.  A path edge from prefix `a` to prefix `b` has weight
`Q_N(a^{-1}b)`.  The conditional law of an interior prefix `b` between fixed
neighbors `a,c` is proportional to

```text
Q_N(a^{-1}b) Q_N(b^{-1}c).
```

The spectral gap is the Poincare constant.  `B` is nonlazy but is a convex
average of heat-bath projections and hence positive semidefinite.

## Methods and expected failure modes

- Search repository literature and manuscript first, then primary journal,
  arXiv, and author-hosted sources.
- Record theorem/result numbers, exact hypotheses, normalization, and literal
  applicability.
- Treat an unproved strong-spatial-mixing, Dobrushin, minorization, or
  return-ratio condition as the missing bridge proposition, not as a result.
- Reject base-walk-to-bridge inference.
- For the map route, check state spaces, rooting, simplicity, labels,
  stationary measures, and local transition intertwining separately.
- A failure of either transfer is not a refutation of polynomial mixing.

## Reproduction

The deterministic influence calculation will be run with Python 3 and no
nonstandard dependencies.  No random seed is needed.
