# M212 freeze manifest

Date: 2026-08-13 UTC.

## Verdict

```text
ACCEPT M208 AS FROZEN. NUMBERED OBJECTIONS: NONE.
```

The clean referee reproduced:

- the named `T_5 -> T_6` descriptor extension;
- all fourteen correction-word endpoint equalities;
- correction lengths `13,0,9,0,5,2,1`;
- certificate digest
  `0bcfdab81369a4fca73367bee84169dd313c698b42685b8053dae2e764ef4223`;
- all 16 trees and 112 known-word checks;
- 21 failures with histogram `1:11,3:9,5:1` and the exact first witness;
- the formal d5 fixed-endpoint-route composition, including its qualitative
  voltage dependency and absence of a corrected length.

## Strict boundary

Acceptance covers only the finite two-pattern d5-to-d6 theorem, inherited
edits 1 through 7, and failure of the specific schedule table on the declared
template. It proves no general d6, every-color, arbitrary-representative,
all-d, voltage-length, polynomial-length, gap, mixing, or Terminal claim.

## Frozen payload

`SHA256SUMS` hashes `plan.md`, `checkpoint.md`, `immutable_gate.md`,
`halfway_checkpoint.md`, `fresh_rooted_referee.py`, `referee_results.json`,
`proof_audit.md`, `report.md`, and this manifest. The checksum file is not
self-listed.

M208 was not edited. No `Q_6` graph, route search, or bytecode cache was
created by the authoritative replay.

