# M112 freeze manifest

Date: 2026-08-12

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen artifacts

```text
plan.md
checkpoint.md
marked_leaf_reduction.md
marked_leaf_audit.py
marked_leaf_results.json
lift_transfer_audit.py
lift_transfer_results.json
aggregate_projection_audit.py
aggregate_projection_results.json
dps_local_audit.py
dps_local_results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes precisely these files and is not self-hashed.

## Exact reproduction

Run from this mission directory with Python 3.12.3:

```text
python3 -B marked_leaf_audit.py --d 2 3 4 --output marked_leaf_results.json
python3 -B lift_transfer_audit.py --base-q 1 2 3 4 --output lift_transfer_results.json
python3 -B aggregate_projection_audit.py --d 3 4 --output aggregate_projection_results.json
python3 -B dps_local_audit.py --d 2 3 4 --output dps_local_results.json
python3 -B -m compileall -q .
python3 -c 'import json, pathlib; [json.loads(p.read_text()) for p in pathlib.Path(".").glob("*.json")]; print("json ok")'
sha256sum -c SHA256SUMS
```

Every experiment is deterministic, uses `seed=null`, and has no nonstandard
dependency.  The DPS audit's word enumeration is deliberately complete only
for `d<=4`.

## Scope and hygiene

The freeze proves no asymptotic physical-chain gap.  It retains exact finite
negative findings and labels them as such.  No cache directory is part of the
freeze.  No file outside this mission directory is modified by the worker.
