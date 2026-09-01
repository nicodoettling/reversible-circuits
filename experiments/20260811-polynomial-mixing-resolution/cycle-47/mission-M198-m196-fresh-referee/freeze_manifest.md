# M198 freeze manifest

Date: 2026-08-13 UTC.

## Verdict boundary

```text
ACCEPT M196: all 54 named d=5 width-two targets have exact positive words.
INDEPENDENTLY REBUILT: 8,400-state Q5 action, 10 descriptors, 54 targets.
INDEPENDENTLY REPLAYED: 41 adjusted stabilizers and 54 full endpoints.
NUMBERED OBJECTIONS: NONE.
```

The accepted maximum full-word length 22 is an exact finite certificate fact
only. There is no every-color, all-`d`, polynomial-length, gap, mixing, or
Terminal inference.

## Frozen payload

`SHA256SUMS` hashes `plan.md`, `checkpoint.md`, `immutable_gate.md`,
`halfway_checkpoint.md`, `replay_checkpoint.md`, `fresh_referee.py`,
`referee_results.json`, `proof_audit.md`, `report.md`, and this manifest. The
checksum file is not self-listed. No file outside M198 was edited.
