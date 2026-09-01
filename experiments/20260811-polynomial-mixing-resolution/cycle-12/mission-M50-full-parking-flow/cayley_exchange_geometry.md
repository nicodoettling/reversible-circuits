# A linear child-sorting obstruction for Cayley exchange

Date: 2026-08-11.  This is an exact calibration for the proposed comparison
from the Cayley basis-exchange projection `C_r` to `Pbar_r`.  It refutes only
bounded-length or pointwise one-move domination.  Linear length is polynomial
and is not a congestion obstruction.

## Proposition

For every integer `q>=3`, put `r=2q`.  There are labelled rooted Cayley trees
`T_q,Tprime_q` on `{0,...,r}` which differ by one graphic-matroid basis
exchange, but whose child-sorted preorder degree vectors `d,dprime` satisfy

```text
||d-dprime||_1=4(q-2)=2r-8.                          (1.1)
```

Every `Pbar_r` path between their parking macros therefore has length at
least

```text
(1/2)||d-dprime||_1=r-4.                             (1.2)
```

The exact nonlazy Cayley down-up transition probability for this exchange is

```text
U_r(T_q,Tprime_q)=1/[r q(q+1)].                      (1.3)
```

## Construction and proof

Give the root `0` two branches.  The first branch `A` is the labelled path

```text
0--1--(q+2)--(q+3)--...--(2q),
```

so `A` has `q` nonroot vertices.  The second branch `B` is the star whose
centre is `2`, joined to `0` and to leaves `3,...,q+1`; it also has `q`
vertices.  Since the root children are `1<2`, numeric child sorting puts `A`
before `B`.  Its preorder degree vector is

```text
d=(2, 1^(q-1), 0, q-1, 0^(q-1)).                    (1.4)
```

Delete `{0,1}` and add `{0,2q}`.  This is one spanning-tree basis exchange.
It reroots the path branch at its other endpoint without changing its plane
shape.  The root children are now `2<2q`, so child sorting puts `B` before
`A`, and

```text
dprime=(2, q-1, 0^(q-1), 1^(q-1), 0).               (1.5)
```

Comparing (1.4) and (1.5), the four disjoint contributions to the `L^1`
distance are: `q-2` at position `1`; `q-2` across positions `2,...,q-1`;
`q-2` at position `q+1`; and `q-2` across positions
`q+2,...,2q-1`.  This proves (1.1).

Every off-diagonal `Pbar_r` move transfers one unit of outdegree from one
preorder coordinate to another, and therefore changes `L^1` distance to a
fixed target by at most two.  This proves (1.2), independently of which
right-spine destinations have positive rate.

After deleting `{0,1}`, the two components have `q` and `q+1` vertices.
The Cayley down-up chain chooses the deleted edge with probability `1/r`
and the replacement uniformly among the `q(q+1)` crossing edges, including
the deleted edge.  Choosing `{0,2q}` gives (1.3).  Reversing the exchange has
the same normalization.

## Scope

The example shows why child sorting cannot be suppressed in a Cayley-flow
proof and why a single exchange cannot be identified with one actual branch
rotation.  It does **not** refute `CAYLEY-EXCHANGE-TO-PARKING FLOW`: the
necessary path length is only linear, and no superpolynomial stationary-flow
load or small-capacity cut follows from (1.1).
