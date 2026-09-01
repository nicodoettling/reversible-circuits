# M273 freeze manifest

Status: frozen after `SHA256SUMS` is written. The immutable payload consists
of:

```text
plan.md
checkpoint.md
halfway_checkpoint.md
decorated_root_seam.md
root_seam_guard.py
root_seam_guard_results.json
report.md
audit_request.md
freeze_manifest.md
```

`SHA256SUMS` inventories these nine files. Any later change requires a new
mission rather than mutation of this directory.

