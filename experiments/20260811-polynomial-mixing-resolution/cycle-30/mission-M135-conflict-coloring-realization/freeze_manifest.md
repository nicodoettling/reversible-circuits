# M135 freeze manifest

Date: 2026-08-13 UTC.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen artifacts

```text
plan.md
checkpoint.md
orbit_incidence_reduction.md
conflict_coloring_audit.py
results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes precisely these seven payload files and is not self-hashed.

## Exact reproduction

Run from this mission directory with Python 3.12.3:

```text
python3 -B conflict_coloring_audit.py --d 3 4 --output results.json
python3 -c 'from pathlib import Path; p=Path("conflict_coloring_audit.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
python3 -c 'import json; q=json.load(open("results.json")); a,b=q["rows"]; assert all(r["root_stabilizer_equivariance_failures"]==0 for x in q["rows"] for r in x["adjacent_rows"]); assert all(r["exact_color_pair_conflicts"]==0 for r in a["adjacent_rows"]); assert all(r["maximum_agreement"]==6 and r["minimum_schedule_cover"]==5 for r in a["complete_action_cover"]); w=b["rank_four_exception_witness"]; assert (w["source_pair_subgroup_order"],w["target_pair_subgroup_order"])==(96,288); print("assertions ok")'
sha256sum -c SHA256SUMS
```

The main experiment is deterministic with `seed=null` and dependencies `{}`.
Elapsed wall time in `results.json` is metadata and may vary on a rerun; every
mathematical field is deterministic.

## Frozen claim scope

The freeze proves `chi(C_(d,i))<=d` for `d=3` and every `d>=5`, and the
uniform exceptional-case bound `chi(C_(d,i))<=d^6` for every `d>=2`. It also
refutes automatic one-braid realization of the resulting matchings at `d=3`
and gives the exact polynomial matching-coset refinement obligation.

It proves no simultaneous-realization theorem, schedule-length bound, UST
route, all-edge comparison, physical gap, `Gamma_0`, original heat-bath gap,
or Terminal outcome. No cache directory is part of the freeze. No file
outside the owned M135 mission directory was modified.
