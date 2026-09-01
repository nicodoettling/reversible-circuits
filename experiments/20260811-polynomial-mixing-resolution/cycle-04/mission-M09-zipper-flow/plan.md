# M09 coordinator plan: non-hub zipper flow for fixed-endpoint bridges

## Exact target

Fix `N>=3`, pair length `l>=2`, and a feasible even endpoint `h`.  Let
`Omega_h(l)` be the length-`2l` transposition words with ordered product
`h`, with the uniform law.  Let `G_h` be the whole-word heat bath, so
`G_h(x,y)=1/|Omega_h(l)|` and `gap(G_h)=1`.  Let `B_h` be the nonlazy average
of the `l-1` aligned length-four same-product heat baths.

Construct a deterministic or randomized path flow simulating every `G_h`
transition by `B_h` edges with

```text
max_e 1/[pi(e_-)B_h(e_-,e_+)]
  sum_(x,y) pi(x)G_h(x,y)
  E[ number of traversals of e times path length ]
    <= (Nl)^C
```

for universal `C`, at least for `l<=s_*(N)+2=O(N log N)`.  Combined with
the accepted M10 recursion, this statement would prove a polynomial gap for
`B` and then for the original `K`.

## Proposed zipper encoding

A local aligned heat-bath edge has capacity at least

```text
pi(e_-)/[(l-1)M^4],       M=binom(N,2),
```

because a four-transposition same-product fiber has at most `M^4` words.
Thus it is enough to map every charged source-target path occurrence into

```text
(directed edge e, complementary bridge z in Omega_h(l), polynomial metadata)
```

injectively, with polynomial path length.  The desired route should retain a
target prefix and source suffix separated by a moving bounded-description
interface; the complementary bridge retains the overwritten source prefix
and unused target suffix.  This is the usual zipper information balance, but
the interface must remain an exact transposition factorization of the current
nonabelian product defect.

Randomizing the interface factorization is allowed and may be necessary to
spread flow.  Routing through one identity-heavy or doubled-tree normal form
is forbidden: at a hub edge the complementary bridge cannot encode the
quadratically many source-target pairs, reproducing the inherited exponential
congestion.

## Obligations and falsification

1. State the exact local rewrite sequence and show every intermediate word
   has product `h`.
2. Bound interface width, path length, and all heat-bath output probabilities
   polynomially in `N,l`.
3. Prove source-target recovery from the used edge, complementary bridge, and
   only polynomial metadata; repeated factors and multiple local outputs must
   be aggregated.
4. If a bounded-width zipper is impossible, give a precise family of product
   defects requiring growing interface width.  That refutes only this flow
   design, not polynomial mixing.
5. Check whole-word `l=2`, all endpoint fibers in the M08 suite, `m=4`, and
   the known failure of arbitrary length-two subwindow simulation.

No finite congestion scan can prove the universal target.  A calculation may
only falsify a proposed recovery map or local rewrite lemma.

