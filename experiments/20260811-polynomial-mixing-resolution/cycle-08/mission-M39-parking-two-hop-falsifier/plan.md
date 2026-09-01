# M39 plan: exact parking-flow two-hop falsifier

## Objective

Test the named universal implication left by M36:
whether every positive transition of the Lorentzian parking ideal chain
`D_r` can be routed through the actual stationary-flow projection of the
minimal long-cycle rank-two heat bath by a path of length at most two with
only inverse-polynomial capacity loss.

## Exact target and convention

The raw law is uniform on minimal transposition factorizations of the long
cycle in `S_n`, represented bijectively by zero-based parking functions of
length `r=n-1`. Composition is `(pq)(x)=p(q(x))`, with tuple products
left-to-right. The actual chain is the nonlazy uniform scan of the
`r-1` exact rank-two heat baths. Its stationary-flow projection is by the
sorted parking multiset. The ideal chain `D_r` deletes one uniformly chosen
parking coordinate and reinserts it uniformly among feasible values.

The finite calculation can refute either of these universal statements:

1. every ideal edge has actual projected graph distance at most two;
2. for a stated exponent `C`, every ideal edge has a length-at-most-two
   route whose two actual stationary capacities are each at least
   `r^(-C)` times the ideal stationary flow.

Finite positive results are calibration only and cannot prove either claim.

## Method

Enumerate parking functions directly, not all transposition words. Use the
corrected recursive inverse of Stanley's labeling to reconstruct the maximal
noncrossing-partition chain. At each internal rank, enumerate the two or
three possible intermediate partitions exactly. Accumulate projected flow
with the common integer scale `6(r-1)`, verify detailed balance, construct
all ideal `D_r` edges, and compute direct and best two-hop capacity ratios.
After the two-hop claim fails, also compute an exact widest path for every
ideal edge. These individually optimized paths test whether the obstruction
is merely path length; they do not constitute a simultaneous multicommodity
flow or a congestion bound.

## Parameters and failure modes

- Exact exhaustive range: `3<=n<=8`.
- No randomness or seed.
- Required checks: Dénes count `n^(n-2)`, inverse-label identity, interval
  sizes two or three, exact projected detailed balance, ideal detailed
  balance, graph distances, and rational capacity ratios.
- A missing route is a decisive counterexample to the two-hop claim. A small
  rational ratio only refutes a predeclared numerical exponent if it violates
  that bound; apparent scaling is not an asymptotic theorem.
