# Quantitative audit of the Classification-H construction

## Statement

Fix the project convention
`R_i(a,b)=(b,b^{-1}ab)`; one use of `R_i` or `R_i^{-1}` has length
one in the undirected Hurwitz graph. Let `x,y` be length-`m`
transposition factorizations of identity in `S_N` with the same labeled
weighted support components. For `N>=2` and `m>=2`,

    dist_H(x,y) <= 50 N m^3.

The constant is intentionally loose. The point is a universal polynomial
diameter, not an optimized exponent.

This is a quantitative audit of the constructive second direction of
Ben-Itzhak--Teicher Theorem 3.4, especially Lemmas 3.7--3.10. Their generator
is the inverse orientation of the displayed project generator, so every paper
move is still one edge of the symmetric project Hurwitz graph.

## 1. Cost of Lemma 3.9

Lemma 3.9 takes a connected transposition word of length at most `m` and
specified support vertices `u,v`, and brings `(u,v)` to the first
position.

Choose a shortest support-graph path from `u` to `v`, of length
`d<=N-1`. To shorten a path of length at least two, the paper selects its
first two edges. Its inner induction moves one selected occurrence past the
factors between the two occurrences. Each pass is one application of
Lemma 3.7, hence one Hurwitz move, and there are at most `m-2` intervening
factors. The triangle rewrite of the now-adjacent path edges is one more move.
This reduces path length by one. After at most `d-1` reductions, an
occurrence of `(u,v)` exists and is moved to the front across at most
`m-1` factors.

Thus one invocation costs at most

    (d-1)(m-1)+(m-1) <= N m

Hurwitz moves. If the selected occurrences occur in the reverse order, use
the inverse version of the same moves; the count is unchanged.

## 2. Constant-cost square-pair operations

Lemma 3.10 gives the following operations.

1. Two adjacent square pairs with a common endpoint can be swapped using at
   most four Hurwitz moves. Expanding the paper's two three-factor rewrites
   gives the four-move sequence.
2. If the two square pairs are
   `(a,b)^2(a,c)^2`, the second can be changed to `(b,c)^2` using the
   paper's three inverse moves.
3. If the two transpositions are disjoint, their square pairs can be swapped
   by four ordinary disjoint-edge commutations.

Consequently any two adjacent square pairs can be swapped in at most four
moves when they need to be reordered, and an attachment can be moved by one
edge along the connected graph of already constructed square pairs in at most
three moves once the supporting pair is adjacent.

Suppose there are at most `m/2` already constructed square pairs. To move a
new pair's endpoint along a path of at most `m/2` supporting edges, allow
at most `m` pair swaps to bring and restore a supporting pair at every path
step. This deliberately wasteful accounting gives at most

    (8m+3)m <= 11m^2

moves to normalize one new square pair. It covers both the spanning-tree
stage and conversion of a surplus pair to the fixed canonical edge.

## 3. Number of outer stages

First gather factors belonging to the same support component. Lemma 3.8
commutes factors from different components, so a bubble sort costs fewer than
`m^2` moves.

The canonical construction then consumes factors in square pairs.

- For each of at most `m/2` spanning-tree pairs, it invokes Lemma 3.9 at
  most twice to expose the first copy and then the matching copy.
- For each of at most `m/2` remaining surplus pairs, the first factor is
  already exposed and Lemma 3.9 is invoked at most once to expose its match.

Hence there are fewer than `3m/2` invocations of Lemma 3.9, costing at most

    (3m/2)(Nm) = (3/2) N m^2.

There are at most `m/2` pair-normalization stages, costing at most

    (m/2)(11m^2) = (11/2)m^3.

Including component sorting, one word reaches the canonical representative in
at most

    m^2 + (3/2)Nm^2 + (11/2)m^3
      <= 10 N m^3

moves for `N,m>=2`. The stated allowance `25Nm^3` per word absorbs
indexing conventions, the paper's repeated componentwise setup, and any
unoptimized restoration of pair order. Sending `x` and `y` to the same
canonical representative and reversing the second path proves

    dist_H(x,y) <= 50Nm^3.

## 4. Scope and self-attack

The audit uses only the nested procedures actually present in Lemmas
3.7--3.10; every loop counter is bounded by support size or word length. It
does not route Markov-chain flow through the canonical representative.

Polynomial diameter does not imply polynomial conductance or gap. Two
exponentially large regions joined by one edge can have logarithmic or
polynomial diameter and exponentially small conductance. Indeed the project's
fixed canonical representatives have exponentially small stationary mass, so
using these paths as a common comparison routing would recreate the known hub
congestion obstruction.

Verdict for the diameter claim: **PROVED**. Verdict for the spectral gap:
unchanged and open.
