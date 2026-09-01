# M50 plan: full actual parking flow

Date: 2026-08-11.  Convention: permutations compose as
`(pq)(x)=p(q(x))`; minimal long-cycle factor tuples multiply left-to-right.

## Exact target

For every `r>=2`, let

```text
J_r={m in N^r:sum_i m_i=r and sum_(i=0)^k m_i>=k+1 for k<r},
pi_r(m) proportional to 1/product_i m_i!.
```

Let `A_r^ideal` be the accepted adjacent-value restriction of the
Lorentzian down-up parking chain and `bar P_r` the full nonlazy
stationary-flow projection of the uniform scan of adjacent exact rank-two
heat baths.  Prove

```text
gap(bar P_r)>=r^-C
```

by a comparison from `A_r^ideal`, with exact path length and total
stationary-flow congestion; or rigorously refute a named full-`bar P_r`
comparison or cut.

## Frozen inputs and corrections

- `gap(A_r^ideal)>=r^-7`.
- Actual aggregate departure from a duplicated label `h` is exactly
  `2m_h(m_h-1)/[3r(r-1)]`.
- M35 leaf rotations and all transition normalizations are accepted.
- The cycle-lemma law gives the maximum-degree occupancy tail.
- The restricted leaf-rotation chain is superpolynomially slow, but its
  maximum-degree cut has full-projection flow at least
  `4(beta-bprime)/[3r(r-1)]`; do not lift that cut.
- Universal two-hop flow, deterministic canonical hubs, fixed codebooks or
  buffers, and direct associahedron/Caraceni transfer are failed routes.

## First approach

Derive an all-move marked-outcome representation of projected stationary
flow.  Use aggregate duplicate-label departures to seek randomized buffer
or aggregate-layer flows for every adjacent ideal commodity, with the
random choices recoverable from a used edge plus polynomial metadata.
Test exact claims only through `r<=7` or `r<=8` as bounded falsifiers.
