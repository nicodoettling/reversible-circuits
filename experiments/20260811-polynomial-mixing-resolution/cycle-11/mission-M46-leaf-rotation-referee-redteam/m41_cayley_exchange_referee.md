# Fresh referee report on M41 Section 10: Cayley basis exchange

Date: 2026-08-11.  Audited checkpoint:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-09/
  mission-M41-adjacent-parking-flow/checkpoint.md
SHA-256 b24c92123e4c7544cf80d43dbe2718971fdd8a98454d96d1bda6a0abf575d1df
```

## Verdict

**ACCEPT.**

Numbered objections: **none**.

The accepted theorem is: for every `r>=1`, the delete-uniform-tree-edge / 
add-uniform-cross-edge chain `U_r` on uniform labelled Cayley trees on
`{0,...,r}` has gap at least `1/r` (singleton convention at `r=1`), and its
stationary-flow projection `C_r^Cayley` under child sorting followed by
preorder outdegrees has stationary law

```text
pi_r(d)=r!/[(r+1)^(r-1) product_i d_i!]
```

and gap at least `1/r`.  Both chains admit exact polynomial-time steps.

## Hypotheses and normalization

Spanning trees of `K_(r+1)` are exactly the bases of its rank-`r` graphic
matroid.  The uniform basis generating polynomial is homogeneous of degree
`r`, multiaffine, nonnegative, and strongly log-concave.  Anari--Liu--Oveis
Gharan--Vinzant, *Log-Concave Polynomials II*, Theorem 1.1
(arXiv:1811.01816v3; Ann. Math. 199 (2024), 259--299) defines precisely the
following chain: delete one uniformly chosen element of the current
degree-`r` support set, then choose an extending support set with probability
proportional to its weight.  Its theorem gives spectral gap at least `1/r`.

After deleting a tree edge, the two components have sizes `a` and
`r+1-a`.  The graphic-matroid extensions are exactly the
`a(r+1-a)` complete-graph edges crossing that cut, and all resulting bases
have equal weight.  Uniform cross-edge addition, including the deleted edge,
is therefore exactly the cited down-up walk, not a Metropolis variant or a
nonlazy basis-exchange walk.  For a genuine exchange `T-e+f`, the reverse
move deletes `f` and sees the same forest and same cross-edge denominator,
so uniform Cayley measure is reversible directly as well.

## Exact pushforward and stationary-flow equality

Fix a plane-tree preorder degree vector `d=(d_0,...,d_r)` with `d_r=0`.
With root label fixed at zero, there are `r!` assignments of the other
labels to preorder positions.  Child sorting recovers the fixed plane shape
exactly when labels increase within each sibling group.  Those disjoint
groups have sizes `d_i`, so the fiber has exactly

```text
r!/product_i d_i!
```

labelled Cayley trees.  Division by Cayley's `(r+1)^(r-1)` gives `pi_r`
exactly.

Writing `phi(T)=d`, the stationary-flow projection is

```text
C(d,d')=[1/pi_r(d)]
 sum_(T:phi(T)=d) mu(T) sum_(T':phi(T')=d') U(T,T').
```

For every macro observable `f`, its lift `F=f o phi` satisfies

```text
Var_mu(F)=Var_pi(f),
E_U(F,F)=E_C(f,f)
```

by regrouping the exact stationary flow.  Applying the `U_r` Poincare
inequality proves `gap(C_r^Cayley)>=gap(U_r)>=1/r`.  Strong lumpability is
neither assumed nor needed.

## Small cases

- `r=1`: `K_2` has one spanning tree.  Both chains are singletons; the
  stated gap-one convention equals `1/r`.
- `r=2`: the three spanning trees of `K_3` have transition matrix with
  diagonal `1/2` and off-diagonal entries `1/4`, so `gap(U_2)=3/4>=1/2`.
  The child-sort projection has masses `1/3` on `(2,0)` and `2/3` on
  `(1,1)` and the same nonzero eigenvalue/gap `3/4`.

These checks also confirm that inclusion of the deleted edge among the
cross-edge choices supplies the correct holding probability.

## Exact runtime

For `U_r`, choose one of `r` edges, find the two components in `O(r)`, and
sample one endpoint uniformly from each component.  Given a macro degree
vector, construct its plane tree, assign a uniform random permutation of
labels to nonroot positions, and sort labels inside each sibling group.
Every valid conditional Cayley labeling has exactly `product_i d_i!`
preimages, so this samples the projection fiber uniformly.  Apply one
`U_r` step, child-sort, and traverse in preorder.  This implements one exact
`C_r^Cayley` step in `O(r log r)` time (or polynomial time under any
straightforward representation).

## Comparison assessment with M50

M50's accepted structural direction is genuinely complementary: the actual
parking projection has a polynomial-gap root-composition quotient and its
fixed-root-composition restriction factors into smaller independent parking
projections with only the exact action-rate loss
`s(s-1)/[r(r-1)]`.  Together with the `1/r` Cayley source, this suggests a
recursive variance/flow construction which first transports root
composition and then repairs child subtrees.

It does **not** yet prove a polynomial comparison.  A single labelled Cayley
edge exchange can move a subtree between branches and, after numeric child
sorting, reorder a linear number of preorder positions.  Its image need not
be one actual local parking move, and conditioning on a root composition
does not make the restricted Cayley-exchange kernel a product of smaller
`C_s^Cayley` chains.  Routing every recursion level through M50's polynomial
Radon bound would multiply polynomial losses to depth `Theta(r)`.  Child
sorting also discards the labels needed to recover a source exchange, so a
deterministic local route risks the same congestion problem as earlier
canonical hubs.

This nonlocality has an exact sharp calibration.  For `r=2q`, `q>=3`, take
two balanced root branches, one a specially labelled path and the other a
star, and exchange the root edge of the path for an edge to its far endpoint.
Child sorting swaps the two blocks.  The projected degree vectors have
`L^1` distance `4(q-2)`, while every off-diagonal `Pbar_r` move transfers
one degree unit and changes that distance by at most two.  Every simulation
therefore has length at least `r-4`; the source exchange rate is exactly
`1/[rq(q+1)]`.  The proof is in M50's `cayley_exchange_geometry.md`.
This refutes bounded-length and one-move domination, but not polynomial
flow: the lower bound is only linear and supplies no congestion cut.

The exact remaining proposition is therefore unchanged:

> **CAYLEY-EXCHANGE-TO-PARKING FLOW.**  Construct a stationary randomized
> flow from `C_r^Cayley` to the actual `Pbar_r` with polynomial congestion,
> including recoverable label/branch metadata and a telescoping rather than
> depth-multiplying mean-lift bound; or refute such a flow by an explicit
> stationary-capacity obstruction.

No pointwise domination or bounded-length simulation follows merely from
the two accepted quotient gaps.
