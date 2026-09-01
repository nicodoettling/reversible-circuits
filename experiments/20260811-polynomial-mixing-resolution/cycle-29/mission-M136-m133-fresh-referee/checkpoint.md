# M136 halfway checkpoint

Date: 2026-08-13 UTC.

## Status

The frozen M133 checksum inventory passes, and every supplied assignment hash
matches.  Required project sources and the accepted M113/M118 and M125/M129
dependency reports have been inspected.  The target remains the auxiliary
incidence-key coefficient law, not the original identity-word sampler.

## Independent proof audit so far

The core bijection survives.

- An ordered partition pair gives an edge-labelled bipartite multigraph;
  join-indiscreteness is connectivity.
- On `L+R=c`, the graph has `E=V=c`, hence is connected unicyclic.  Degree-one
  pruning leaves one even cycle, including the length-two parallel-edge case.
- Starting from the least core edge and taking its other edge at the *left*
  endpoint determines a unique alternating traversal.  Thus no rotation or
  orientation factor is missing.  Direct inventories for core lengths
  `2,4,6,8` have respectively `1,6,120,5040` fixed-first sequences, the same
  number of distinct coloured cores, each with multiplicity one.
- Deleting the core leaves tree components, each meeting exactly one core
  vertex.  Root deletion uniquely partitions its edge set into branches and
  uniquely selects the child edge incident to the root.  This is exactly the
  planted alternating-tree recurrence and preserves every incidence-block
  weight.

## Exact clean-room result

`independent_referee.py` imports no M133 or M125 code.  In `small_results.json`
it reports zero failures:

- 58 integer cycle types through total size eight were checked against a
  separately rooted connected-component recurrence;
- all 37 eligible types through total size seven were also checked by literal
  ordered partition pairs, totaling 864,261 pairs;
- leaf pruning verified every literal core and every off-core attachment root;
- reconstructed core profiles through `d=8` match the frozen reported values;
- at `d=4`, core lengths two and four give
  `(80136,109440,44928)` and `(0,0,216)` across `c=2,3,4`;
- the pairwise polarized margin is independently
  `-80136*216=-17309376`.

The remaining work is the independent dynamic-root multiset recomputation of
the targeted `d=23,24,25,26` triples, followed by the strict referee verdict
and frozen artifact inventory.
