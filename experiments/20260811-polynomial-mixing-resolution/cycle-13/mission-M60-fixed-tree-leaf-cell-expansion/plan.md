# M60 plan: fixed-tree leaf-cell expansion

## Exact target and convention

Use `(pq)(x)=p(q(x))`, `m=2N-2`, the exact lazy uniform same-product
`r in {3,4,5}` chain, and the global uniform law on `Omega(N,m)`.  For a
fixed labeled join tree `T`, write `F_N(T)` for its minimal full-support
fiber.  For a leaf `v` and `z in F_(N-1)(T-v)`, define the deletion cell

```text
C_(v,z)={w in F_N(T):Del_v(w)=z}.
```

Analyze the random-leaf exact cell heat bath `P_T^leaf` and its comparison to
the literal rejected-exit restriction `K_T`.  Prove a universal polynomial
gap/comparison without multiplying a polynomial once per deleted leaf, or
construct a globally oriented full-K superpolynomial cut with complete
`H3/H4/H5` flow.

## Positive lane

1. Test whether the cell hypergraph is connected in every N=4 and N=5 fixed
   tree fiber using the exact M59 enumeration.
2. Derive exact cell sizes, overlaps, transition probabilities, and finite
   gap/conductance diagnostics only to falsify named universal lemmas.
3. Seek a one-scale variance inequality from overlapping deletion maps, such
   as an Efron--Stein/approximate-tensorization inequality, rather than a
   recursive fixed-leaf induction.
4. Compare one cell resampling to local `H3/H4/H5` moves through randomized
   insertion-history paths, auditing whether cell cardinality
   `<=binom(m,2)(N-1)^2` is enough for polynomial congestion.

## Independent Terminal-B lane

Search for cuts supported on insertion-coordinate histories that are
simultaneously thin for every leaf deletion.  Include middle rank intervals,
leaf-null separation bands, and intersections across leaves.  Any candidate
must be oriented in global `Omega`, include every tree-changing/macro-exit
outcome, and have exact stationary mass and boundary flow.  A slow
`P_T^leaf` or rejected-exit `K_T` alone is nonterminal.

## Named bounded claims

- **LEAF-CELL CONNECTIVITY:** `P_T^leaf` is irreducible for every labeled T.
  A finite disconnection refutes it.
- **PAIRWISE CELL OVERLAP:** a proposed uniform lower overlap/correlation
  estimate must survive path and star trees.  Exact N<=5 can refute but not
  prove it.
- **LOCAL CELL COMPARISON:** every complete-graph cell heat-bath edge admits
  polynomial-congestion simulation in `K_T`.  Explicit high-load local
  fibers can refute a proposed routing.

## Calibration and failure modes

Retain N=3,m=4 whole-word H4 normalization, S4,m4 and S4,m6 counts, stars,
paths, doubled trees, ordered factors, and the length-two failure.  Do not use
a fixed adjacent-square hub.  The main expected obstruction is that
`P_T^leaf` can change a whole strand history while `K_T` may need a long,
high-load route; conversely, cell heat baths may themselves preserve a hidden
deck statistic.

