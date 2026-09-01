# M329 freeze manifest

Date: 2026-08-14 UTC

Seven payloads are frozen:

```text
plan.md
checkpoint.md
integrity_audit.md
report.md
run_manifest.md
final_checkpoint.md
freeze_manifest.md
```

`SHA256SUMS` authenticates these exact payloads and is not self-listed.

M329 is an append-only checksum-provenance salvage. It does not replace or
modify M326, and it leaves M326's mathematical verdict unchanged: `REJECT`
M323 for the missing non-Touch A-side partner, with the bad-B-prefix rank
obstruction retained only conditionally and `N_A > 0` as the exact first
salvage obligation.

