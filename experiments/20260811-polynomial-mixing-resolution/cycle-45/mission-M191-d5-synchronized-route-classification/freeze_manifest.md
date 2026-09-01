# M191 freeze manifest

Date: 2026-08-13 UTC.

## Verdict boundary

```text
INCONCLUSIVE: complete synchronized-component classification of the 54 named
d=5 width-two target tuples.

PROVED: exact stabilizer-orbit membership criterion.
EXACT: complete 8,400-state single-coordinate Q5 action and 54 target IDs.
ACCEPTED IMMUTABLE INPUT: M188's fourteen explicit positive routes.
UNCLASSIFIED: every other target; no negative result.
```

Every stale geometric all-`d` claim in M187 is excluded. No radius-limited
miss, every-color conclusion, asymptotic route length, gap, mixing, or Terminal
claim is included.

## Computation cap

Magma V2.29-4 did not complete the exact 8,400-point source stabilizer/orbit
construction within the six-minute cap and created no output certificate. The
process was terminated; this is not mathematical evidence.

## Frozen payload

`SHA256SUMS` hashes every regular file listed below except itself:

```text
plan.md
checkpoint.md
pre_enumeration_checkpoint.md
halfway_checkpoint.md
proof.md
report.md
exact_classifier.py
export_q5_action.py
q5_action.json
classify_q5.m
cap_results.json
freeze_manifest.md
```

No file outside M191 was edited.
