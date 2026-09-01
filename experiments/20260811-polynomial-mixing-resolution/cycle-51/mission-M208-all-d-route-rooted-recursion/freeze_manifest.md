# M208 freeze manifest

Date: 2026-08-13 UTC.

## Disposition

```text
KEEP: exact finite synchronized one-leaf correction theorem for the two named
M181 patterns at d5->d6 and inherited edits 1..7.

REFUTED: universality of the displayed seven-word schedule table across all
16 Cayley trees in the same old-root-leaf extension template.

UNRESOLVED: another tree-dependent or general-d rooted contour recurrence.
```

Exact correction lengths are `13,0,9,0,5,2,1`; the fourteen named endpoint
replays pass. The schedule-table falsifier has 21 failures among 112 checks,
with the first at tree `{{1,2},{1,3},{1,5},{3,4}}`, edit 3.

## Artifact roles

- `rooted_extension_audit.py` and `rooted_extension_results.json` are the
  authoritative deterministic checker/result. They perform no route search.
- `correction_mitm_probe.py`, `correction_mitm_results.json`, and
  `correction_mitm_r5_results.json` retain bounded discovery history. Only
  positive words were used; recorded radius misses have no negative meaning.
- `rooted_recursion.md` proves the finite theorem and states the exact first
  unresolved lemma.
- `report.md` is the nine-field final report.

## Scope and hygiene

No `Q_6` graph was enumerated. No predecessor was edited. No cache remains.
There is no arbitrary-H-representative, every-color, all-d, polynomial-length,
voltage-correction-length, gap, mixing, or Terminal claim.

`SHA256SUMS` hashes `plan.md`, `checkpoint.md`, `immutable_gate.md`,
`halfway_checkpoint.md`, the two scripts, three JSON artifacts,
`rooted_recursion.md`, `report.md`, and this manifest. The checksum file is
not self-listed.

