# M327 freeze manifest

Frozen: 2026-08-14 UTC.

Verdict: **ACCEPT M324; zero material and zero nonmaterial objections.**

The immutable payload is:

1. `plan.md`
2. `checkpoint.md`
3. `halfway_checkpoint.md`
4. `dependency_audit.md`
5. `proof_audit.md`
6. `report.md`
7. `run_manifest.md`
8. `final_checkpoint.md`
9. `freeze_manifest.md`

`SHA256SUMS` records all nine payloads.  Its own SHA-256 is the package top
digest reported out of band.  No M327 file may now be changed.

AATSD, HPRN, and every downstream claim remain unresolved.
