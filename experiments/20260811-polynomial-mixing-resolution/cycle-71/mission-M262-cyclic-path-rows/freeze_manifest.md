# M262 freeze manifest

Status: frozen after `SHA256SUMS` is written. The immutable payload consists
of:

```text
plan.md
checkpoint.md
halfway_checkpoint.md
cyclic_path_row_refutation.md
literal_row_check.py
literal_row_results.json
report.md
audit_request.md
freeze_manifest.md
```

`SHA256SUMS` inventories those nine files. Any later change requires a new
mission rather than mutation of this directory.
