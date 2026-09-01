# M220 freeze manifest

Date: 2026-08-13 UTC.

## Frozen verdict

`REJECT` the explicit late-ancestor / initial-run / forward-exception
recurrence stated in `symbolic_transport.md`. `KEEP` the formal Hurwitz
transport identities, its exact rank-five specialization, and the first exact
same-key next-rank obstruction.

## Exact certificates

```text
d5 trees / rows / failures       16 / 112 / 0
d6 trees / edits / rows          125 / 9 / 1125
d6 passes / failures             1098 / 27
d6 failures by edit              edit 1: 11; edit 7: 16; otherwise 0
new edit 8 passes                125 / 125
new edit 9 passes                125 / 125
complete d6-row digest           f0deca809ef570f7d557a88a94d517e3885f971f0178ac7ef2938bad651341c0
results-file digest              853ea8fcec9fbd3d4d0523b4157c7a17fa4c2c977b65e0dd15563c8f4a606867
```

The first same-key pair is the rank-six star and
`{{1,2},{1,3},{1,4},{1,6},{2,5}}` at edit 1. Their common 17-move route
succeeds on the first and fails on the second exactly at factor positions 7
and 8.

## Method and logical boundary

`rooted_recurrence_audit.py` is deterministic, generates the tree template in
two independent exact ways, reconstructs all DPS endpoints, and literally
replays the closed words. It imports no predecessor implementation or data,
does no route search, and enumerates no quotient graph.

The obstruction rejects only the declared descriptor-to-word map. It proves
no nonreachability, no failure of a richer descriptor, no general-rank
negative theorem, and no length, gap, mixing, or Terminal claim.

## Payload inventory and audit request

The frozen payload is exactly the files listed in `SHA256SUMS`; no cache is
included. Request a fresh immutable audit of every exact count, the first
witness, both digests, the analytic identities, and the strict scope.

