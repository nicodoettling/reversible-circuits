# M265 Freeze Manifest

Status: frozen after `SHA256SUMS` is written.

The immutable payload is:

```text
plan.md
checkpoint.md
proof_audit.md
independent_guard.py
independent_guard_results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` inventories those seven files.  Any later change requires a new
mission rather than mutation of this directory.

