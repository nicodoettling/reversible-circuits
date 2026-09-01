# M320 freeze manifest

Date: 2026-08-14 UTC

This directory freezes ten payloads:

```text
plan.md
checkpoint.md
halfway_checkpoint.md
dependency_audit.md
proof_audit.md
report.md
run_manifest.md
audit_request.md
final_checkpoint.md
freeze_manifest.md
```

`SHA256SUMS` authenticates these exact ten payloads.  Its own SHA-256 digest is
the M320 top digest and is intentionally not included in itself.

Verdict: ACCEPT, zero material objections, two nonmaterial items.  Frozen
M317 and every predecessor remain unchanged.  No file outside this M320 role
directory was written by this mission.
