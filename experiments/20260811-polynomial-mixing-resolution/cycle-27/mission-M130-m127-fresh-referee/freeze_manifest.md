# M130 freeze manifest

Date: 2026-08-13 UTC.  Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen artifacts

```text
plan.md
checkpoint.md
independent_referee.py
independent_results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes precisely these six files and is not self-hashed.

## Exact reproduction

Run from this mission directory with Python 3.12.3:

```text
python3 -B independent_referee.py
python3 -c 'from pathlib import Path; p=Path("independent_referee.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
python3 -c 'import json; q=json.load(open("independent_results.json")); assert q["verdict"]=="ACCEPT"; assert q["d3_complete_action_image"]["action_image_order"]==216; assert all(x["minimum_schedule_cover"]==5 and x["maximum_agreement"]==6 and not x["tau_in_action_image"] for x in q["d3_complete_action_image"]["rows"]); print("assertions ok")'
sha256sum -c SHA256SUMS
```

The experiment is deterministic with `seed=null` and has no nonstandard
dependency.  It imports no M127 or predecessor code/data.  It independently
brute-forces physical `Z_2,Z_3,Z_4`, reconstructs the accepted plus-mirror DPS
map, enumerates paired generated subgroups, and closes the complete `Z_3`
signed-Hurwitz action image and schedule-cover union DP.

## Decision and scope

```text
ACCEPT M127.  ZERO MATERIAL NUMBERED OBJECTIONS.
```

Accepted scope: universal root-independent adjacent-label descent, the
diagonal paired-source subgroup invariant, the rigorous `d=3,i=3` fixed-word
counterexample, all-index `d=3,4` finite witnesses, and the finite `d=3`
action-image/cover figures.

No polynomial schedule cover, all-edge congestion, ROOTED PRODUCT LOCAL
COMPARISON, physical gap, original heat-bath gap, Terminal A, or Terminal B
is proved or refuted.  M130 edited no file outside its owned directory.
