# M269 freeze manifest

Status: frozen after `SHA256SUMS` is written. The immutable payload consists
of:

```text
plan.md
checkpoint.md
halfway_checkpoint.md
directional_lens_transducer.md
four_row_guard.py
four_row_guard_results.json
report.md
audit_request.md
freeze_manifest.md
```

`SHA256SUMS` inventories these nine files. Any later change requires a new
mission rather than mutation of this directory.

