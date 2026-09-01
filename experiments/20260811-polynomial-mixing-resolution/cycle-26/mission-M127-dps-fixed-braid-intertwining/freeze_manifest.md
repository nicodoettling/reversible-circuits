# M127 freeze manifest

Date: 2026-08-13 UTC.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen artifacts

```text
plan.md
checkpoint.md
fixed_braid_obstruction.md
fixed_braid_audit.py
fixed_braid_results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes precisely these files and is not self-hashed.

## Exact reproduction

Run from this mission directory with Python 3.12.3:

```text
python3 -B fixed_braid_audit.py --d 3 4 --action-table-d 3 4 \
  --output fixed_braid_results.json
python3 -c 'from pathlib import Path; p=Path("fixed_braid_audit.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
python3 -c 'import json, pathlib; q=json.loads(pathlib.Path("fixed_braid_results.json").read_text()); assert q["verdict"].startswith("REFUTED at d=3"); assert [(r["d"],r["z_size"],r["root_fiber_size_histogram"]) for r in q["rows"]]==[(3,24,{"3":24}),(4,2880,{"4":2880})]; assert all(r["identity_failures"]==r["connected_support_failures"]==0 for r in q["rows"]); assert all(r["all_adjacent_indices_have_two_source_subgroup_obstruction"] for r in q["rows"]); a=q["rows"][0]["complete_signed_hurwitz_action_image"]; assert a["action_image_order"]==216; assert all((not x["target_in_signed_hurwitz_action_image"] and x["maximum_sources_served_by_one_fixed_braid"]==6 and x["minimum_fixed_braid_schedule_classes"]==5) for x in a["target_rows"]); print("json/assertions ok")'
sha256sum -c SHA256SUMS
```

The experiment is deterministic, uses `seed=null`, and has no nonstandard
dependency.  The all-rank root-fiber descent and paired-source subgroup
invariant are proofs in `fixed_braid_obstruction.md`; the `d=3,4` run supplies
the explicit counterexamples, convention check, and finite action-cover data.

## Scope and hygiene

This freeze refutes only a source-independent fixed braid for an entire DPS
adjacent-value action.  It proves that the endpoint edit descends without
root metadata and gives a reusable paired-source obstruction.  The five-class
schedule cover is exact finite data at `d=3` only.  All-edge congestion,
ROOTED PRODUCT LOCAL COMPARISON, every physical gap, arbitrary-product
`Gamma_0`, and the original heat-bath gap remain unresolved.  No cache
directory is part of the freeze.  No file outside this owned mission directory
is modified by M127.
