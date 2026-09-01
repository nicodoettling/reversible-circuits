# M225 freeze manifest

Date: 2026-08-13 UTC.

## Frozen verdict

`PROMOTE` Candidate B as an exact finite `d=6 -> 7` full child-contour
correction theorem.  `REJECT` only Candidate A's displayed map, which fails 16
edit-7 rows.  No all-rank lemma is claimed.

## Exact certificates

```text
formal carrier substitutions                 840 / 840
rank-six root-leaf trees                     125
edits per tree                               9
endpoint rows                                1125
Candidate A passes / failures                1109 / 16
Candidate A passes by edit                    125,125,125,125,125,125,109,125,125
Candidate A descriptor classes / words       32 / 14
Candidate A complete-row digest              85b01dc81f7175b8df32d198181e7b898507ec71d0862ca963c431695f0a15f6
Candidate B passes / failures                1125 / 0
Candidate B passes by edit                    125,125,125,125,125,125,125,125,125
Candidate B descriptor classes / words       407 / 14
Candidate B maximum finite route length      17
Candidate B complete-row digest              80ba2016f66f6f8bd9d6cb8a53b276c0ee4403a4ec6747fdd85568299817f78e
results-file digest                          97337a247906623ffe68f3d1baf5c3ed79c72adb80d984ce5705dbee6ecfca38
checker-file digest                          c92cc5cbc1774cdf9757f451e1cc5a842b2d519959715946c11bec73b23ce47f
```

The Candidate-B route-length histogram is
`{0:568,1:125,2:125,5:108,9:84,13:65,17:50}`.  Consecutive deterministic runs
produced the same results-file digest.

## Candidate-A collision retained

At edit 7, the star and
`{{1,3},{1,4},{1,6},{2,3},{2,5}}` share Candidate-A descriptor
`("odd_A",5,false,[],false)`.  Their common five-move carrier passes the
star and fails the second tree at factors 8 and 11.  Candidate B records the
second path `(5,2,3,1)` and its ascent and assigns identity.

## Source order and method

`candidate_descriptors.md` declares both nested candidates and
`symbolic_transport.md` records the carrier derivation before the first M225
endpoint replay.  The deterministic checker reconstructs endpoints from
scratch, imports no predecessor implementation/data, performs no route search,
and enumerates no quotient graph.  Its compact JSON retains all class
summaries, first failure/collision witnesses, counts, and cryptographic digests
of the complete internal row tables.

## Logical boundary

Candidate B's 407 classes use a descriptor that nearly records an entire root
contour, even though the displayed formula collapses them to 14 words.  The
finite success proves no intrinsic completeness, all-`d` sufficiency or route
length, every-color or arbitrary-representative routing, voltage-corrected or
total route length, polynomial gap/mixing, or Terminal statement.

## Payload and audit

The frozen payload is exactly the files listed in `SHA256SUMS`; no cache is
included.  Request a fresh immutable clean-room audit of the source-order
claim, symbolic identity, complete tree/edit universe, both candidate tables,
first collision, class/word/length counts, row digests, deterministic output,
and scope boundary.
