# M36 plan: Lorentzian ideal chain for parking multisets

Date: 2026-08-11.  Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective

Construct a quantitatively useful, exactly stationary ideal chain on sorted
parking-label multisets in the minimal long-cycle factorization sector.  The
claim tested is that their exact multinomial orbit weights arise from a
Lorentzian measure whose down-up walk has inverse-polynomial gap and
inverse-polynomial positive transition probabilities.

This is a proof mission.  It does not claim that the actual adjacent
rank-two heat-bath projection dominates the ideal chain; M35 owns the
remaining comparison-flow problem.

## Convention and calibration

Permutations compose as `(pq)(x)=p(q(x))`, and factor tuples multiply
left-to-right.  A sorted length-`r` parking vector has entries in
`{0,...,r-1}` and satisfies `beta_i<=i-1` in one-based indexing.  Its count
vector is tested at `r=2` and against the exact orbit mass
`r!/[n^(n-2) product_i m_i!]`, where `n=r+1`.

## Expected failure modes

- Prefix-feasible count vectors might fail the symmetric exchange axiom.
- Polarization might change the desired macro stationary weights.
- Clone multiplicities might make a positive projected down-up edge
  exponentially small.
- A polynomial ideal gap would still leave the actual-flow comparison open.

