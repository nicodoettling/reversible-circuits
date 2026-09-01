# M340 freeze manifest

Date: 2026-08-14 UTC

Eleven payloads are frozen:

```text
plan.md
checkpoint.md
source_lock.md
candidate.md
halfway_checkpoint.md
analytic_obstruction.md
report.md
run_manifest.md
audit_request.md
final_checkpoint.md
freeze_manifest.md
```

`SHA256SUMS` authenticates these exact payloads and is not self-listed.

Verdict: reject the frozen complete-label XCRF at the exact singleton Hall
condition.  Retain only its exact Hall/cell-divergence identities, M335's
token split, and the exceptional scalar reduction.  No predecessor was
edited; no finite guard or downstream inference occurred.
