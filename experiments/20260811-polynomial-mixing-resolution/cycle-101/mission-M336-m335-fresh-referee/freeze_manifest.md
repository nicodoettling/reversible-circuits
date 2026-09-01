# M336 freeze manifest

Date: 2026-08-14 UTC
Status: immutable referee package frozen
Verdict: ACCEPT

Exact payload inventory to be sealed by `SHA256SUMS`:

1. `plan.md`
2. `checkpoint.md`
3. `dependency_audit.md`
4. `proof_audit.md`
5. `report.md`
6. `run_manifest.md`
7. `final_checkpoint.md`
8. `freeze_manifest.md`

The checksum file is not self-listed. M335 and all dependencies remain
unchanged; no temporary output is frozen.
