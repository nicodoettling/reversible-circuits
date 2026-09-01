# M275 freeze manifest

Status: frozen after `SHA256SUMS` is written.

## Immutable payload

```text
plan.md
checkpoint.md
cleanroom_derivation.md
guard.py
guard_results.json
proof_audit.md
report.md
freeze_manifest.md
```

`SHA256SUMS` inventories these eight files.  Any subsequent edit requires a
new mission rather than mutation of this directory.

## Reproduction

```text
repository base commit  502a6f031c6d5a4bc0064ee5b370a4fa3914f993
command                 python3 -B guard.py
Python                  3.12.3
nonstandard dependencies none
seed                    none (deterministic)
```

The guard is finite calibration only.  The arbitrary-rank acceptance rests
on the analytic derivation and proof audit.
