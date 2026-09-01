# M289 freeze manifest

Date: 2026-08-14 UTC.

## Frozen verdict

**CEBV PROVED FOR EVERY ODD `k>=3`, SUBJECT TO FRESH IMMUTABLE AUDIT.**

The proof is the exact raw support-pair coefficient collapse in
`cebv_coefficient_reduction.md`.  The sole computation is a clean-room exact
formula/convention falsifier and is not the asymptotic proof.

## Frozen payload inventory

1. `plan.md`
2. `checkpoint.md`
3. `cebv_coefficient_reduction.md`
4. `cleanroom_cebv_check.py`
5. `cleanroom_results.json`
6. `report.md`
7. `run_manifest.md`
8. `audit_request.md`
9. `freeze_manifest.md`

`SHA256SUMS` contains the complete per-payload hashes in exactly this order.
The digest of `SHA256SUMS` is the mission top digest and is reported to the
coordinator and fresh referee.

No cache or temporary artifact belongs to the frozen inventory.  After the
ledger is created, every listed payload is immutable; any correction requires
a new mission.

## Scope firewall

This freeze concerns CEBV only.  CIBV assembly, DOR, SET, PBV, FD, FCL1,
all gap and mixing claims, and Terminal A/B remain open.
