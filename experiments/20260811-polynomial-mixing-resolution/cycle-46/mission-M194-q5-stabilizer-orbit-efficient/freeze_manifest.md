# M194 freeze manifest

Date: 2026-08-13 UTC.

## Verdict boundary

```text
INCONCLUSIVE: exact stabilizer orbit and 54-target classification.
EXACTLY CHECKED: immutable action digest/bijections/inverses and the complete
8,400-point chronological BFS transversal.
NO NEW MEMBERSHIP OR NONMEMBERSHIP CLAIM.
```

The exact streamed Schreier orbit hit its internal 300-second cap and wrote no
classification output. No more Schreier attempts are part of this mission.
There is no every-color, all-`d`, route-length, gap, mixing, or Terminal claim.

## Frozen payload

`SHA256SUMS` hashes `plan.md`, `checkpoint.md`, `halfway_checkpoint.md`,
`proof.md`, `schreier_orbit.py`, `schreier_orbit_fast.py`, `cap_results.json`,
`report.md`, and this manifest. The checksum file is not self-listed. No file
outside M194 was edited.
