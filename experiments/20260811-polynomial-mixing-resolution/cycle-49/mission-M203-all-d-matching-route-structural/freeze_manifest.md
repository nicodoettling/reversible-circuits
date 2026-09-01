# M203 freeze manifest

Date: 2026-08-13 UTC.

## Verdict boundary

```text
EXACT OBSTRUCTION: DPS matched targets do not generally decompose into
independent d5-like blocks with fixed fillers, already at d=6.

REJECTED: automatic all-d quotient routing by shifting/composing M196 d5 words.
UNRESOLVED: actual d>=6 target reachability by any other method.
```

The first physical witness and its distinct quotient-class stabilization
digests are archived. No `Q_d` was enumerated for `d>=6`. No nonreachability,
polynomial quotient length, voltage-correction length, corrected total length,
gap, mixing, or Terminal conclusion is made.

## Frozen payload

`SHA256SUMS` hashes `plan.md`, `checkpoint.md`, `immutable_gate.md`,
`halfway_checkpoint.md`, `locality_probe.py`, `run_locality_d56.py`,
`locality_results.json`, `leaf_stabilization_probe.py`,
`leaf_stabilization_results.json`, `obstruction.md`, `report.md`, and this
manifest. The checksum file is not self-listed. No file outside M203 was
edited.
