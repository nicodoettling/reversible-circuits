# M271 freeze manifest

Date: 2026-08-14 UTC.

Status: frozen after `SHA256SUMS` is written.

## Verdict and boundary

```text
ACCEPT M269's decorated cyclic-width transducer for initialization and every
strict internal CP-2 path row.  Material objections: none.

Do not promote across a=1 or as DL-RST, RSPT, IDL, routing, a routing-length
bound, a spectral gap, polynomial mixing, or Terminal A/B.
```

## Immutable payload

`SHA256SUMS` inventories exactly these seven files:

```text
plan.md
checkpoint.md
proof_audit.md
cleanroom_lens_guard.py
cleanroom_lens_guard_results.json
report.md
freeze_manifest.md
```

Any later change requires a new mission rather than mutation of this
directory.

## Reproduction

```text
repository commit        502a6f031c6d5a4bc0064ee5b370a4fa3914f993
command                  python3 -B cleanroom_lens_guard.py
Python                   3.12.3
nonstandard dependencies none
seed                     none (deterministic)
predecessor imports      none
rank/tree census         none
```

The checker covers only the four frozen M269 symbolic schemas and four
rank-nine direction-witness rows.  The all-rank theorem is supported by the
analytic proof audit, not by those finite cases.
