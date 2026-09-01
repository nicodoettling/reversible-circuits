# M318 freeze manifest

Frozen: 2026-08-14 UTC.

Verdict: **INCONCLUSIVE / KEEP EXACT IDENTITY; GQAC_1 UNRESOLVED.**

The immutable payload consists of:

1. `plan.md`
2. `checkpoint.md`
3. `source_lock.md`
4. `candidate_frozen.md`
5. `halfway_checkpoint.md`
6. `global_coboundary_identity.md`
7. `gqac_k13.py`
8. `gqac_k13.json`
9. `guard_report.md`
10. `report.md`
11. `run_manifest.md`
12. `final_checkpoint.md`
13. `audit_request.md`
14. `freeze_manifest.md`

`SHA256SUMS` records the digest of every payload above.  Its own SHA-256 is
the package top digest and is reported out of band for the fresh referee.

No file in M318 may now be modified.  No MCLP, GOCI, OCI, CP, MS, FCL1,
spectral-gap, mixing, or Terminal conclusion is part of this freeze.
