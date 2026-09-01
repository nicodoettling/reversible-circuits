# M137 freeze manifest

Date: 2026-08-13 UTC.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen artifacts

```text
plan.md
checkpoint.md
independent_referee.py
independent_results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes precisely these six payload files and is not self-hashed.

## Immutable source audit

The checker verifies the six assigned M135 digests before accepting.  It
imports no M135/predecessor module or result file; source payloads are read
only as bytes for SHA-256 verification.

## Exact reproduction

Run from this mission directory with Python 3.12.3:

```text
python3 -B independent_referee.py
python3 -c 'from pathlib import Path; p=Path("independent_referee.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
python3 -c 'import json; q=json.load(open("independent_results.json")); assert q["verdict"]=="ACCEPT"; d3,d4=q["rows"]; assert all(r["root_stabilizer_equivariance_failures"]==0 for x in q["rows"] for r in x["adjacent_rows"]); assert all(r["maximum_agreement"]==6 and r["minimum_schedule_cover"]==5 for r in d3["complete_action_cover"]); assert d4["rank_four_exception"]["source_pair_group_order"]==96 and d4["rank_four_exception"]["target_pair_group_order"]==288; print("assertions ok")'
sha256sum -c SHA256SUMS
```

The computation is deterministic with `seed=null` and dependencies `{}`.
Elapsed wall time is metadata and may differ when regenerating the raw JSON;
all mathematical fields are deterministic.

## Frozen claim scope

```text
VERDICT: ACCEPT M135.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

This audit accepts the `d`-color theorem for `d=3` and `d>=5`, the uniform
`d^6` rank-four-patched conflict coloring, and the `d=3` refutation of
automatic matching realization.  Polynomial matching-coset refinement,
polynomial braid length, UST routing, all comparison/gap claims, and both
terminal outcomes remain unresolved.

No cache directory is part of the freeze.  No file outside the owned M137
mission directory was modified.
