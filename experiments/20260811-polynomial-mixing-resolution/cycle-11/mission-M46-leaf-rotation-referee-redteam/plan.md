# M46 plan: leaf-rotation count referee and macro-chain red team

## Exact objects

Use `(pq)(x)=p(q(x))` and tuple products left-to-right.  For `r>=1`, let

```text
J_r={d in Z_+^r: sum_i d_i=r,
                    sum_{i=0}^k d_i>=k+1 for 0<=k<r},
pi_r(d)=r!/[(r+1)^(r-1) product_i d_i!].
```

The first task is to audit M35's frozen theorem that a canonical nonlast leaf
`j` with parent `i` induces the actual projected adjacent-rank-two heat-bath
edge `d -> d-e_i+e_j` with forward rate
`2d_i/[3r(r-1)]` and reverse rate `2/[3r(r-1)]`.  The audit will reconstruct
the marked parking-word deletion/insertion bijection and independently charge
the factor-three scan normalization.  It will treat repeated labels, the last
leaf, root/endpoint cases, both orientations, and the corrected raw capacity
denominator `3(r-1)TQ`.

Conditional on acceptance, define the reversible leaf-rotation chain `L_r`
by retaining every such undirected macro edge at its exact projected rate and
putting the unused mass on the diagonal.  The second task is to seek either a
polynomial Poincare/comparison bound for `L_r` or an explicit asymptotic cut
with stationary mass and boundary flow.  A slowdown of `L_r` alone will not
be presented as Terminal B without a valid lift to the original word chain.

## Inherited facts and failed routes

- The exact parking pushforward is `pi_r` above.
- The ideal adjacent-value chain has gap at least `r^-7`.
- Uniform two-hop routing fails for `0^a12^b -> 0^a2^(b+1)`; balanced binary
  direct capacity is exponential but has a polynomial high-label bypass.
- Deterministic canonical hubs are forbidden by exponential congestion.
- Uniform-plane-tree leaf chains in Caraceni--Stauffer have a different
  stationary law and different moves.
- Exact widest paths only through `n<=8` are finite calibration.

## Spectral approaches

1. Express the canonical leaf and parent directly in the Łukasiewicz path of
   `d`; test whether leaf rotation is a standard corner-transfer chain.
2. Attempt a recursive decomposition at the root into ordered subtree sizes,
   using exact factorial stationary weights and a block-dynamics comparison.
3. Compare ideal adjacent transfers to distributed leaf rotations without a
   fixed hub; charge paths by recoverable marked leaf/subtree metadata.
4. Red-team cuts based on root degree, long unary spines, rare labels,
   condensation into one degree, and balanced subtree size.  Every cut must
   include exact `pi_r` mass and all leaf-rotation boundary flow.

No finite convergence result will be used as an asymptotic proof.
