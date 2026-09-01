# M141 freeze manifest

Date: 2026-08-13 UTC.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen artifacts

```text
plan.md
checkpoint.md
multisource_subgroup_theorem.md
multisource_subgroup_audit.py
results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes precisely these seven payload files and is not
self-hashed.

## Exact reproduction

Run from this mission directory with Python 3.12.3:

```text
python3 -c 'from pathlib import Path; p=Path("multisource_subgroup_audit.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
python3 -B multisource_subgroup_audit.py
python3 -c 'import json; q=json.load(open("results.json")); rows=q["actual_d3_matching_rows"]; assert len(rows)==3; colors=[c for r in rows for c in r["matching_colors"]]; assert len(colors)==9; assert all(c["source"]["order_histogram_by_width"]["2"]=={"18":6} and c["target"]["order_histogram_by_width"]["2"]=={"18":6} for c in colors); assert all(c["source"]["order_histogram_by_width"]["3"]=={"18":4} and c["source"]["order_histogram_by_width"]["4"]=={"18":1} for c in colors); assert all(c["aligned_source_target_comparison_by_width"]["4"]["equal_literal_subgroups"]==0 for c in colors); a=q["abstract_d3_pairwise_full_counterexample"]; assert (a["subgroup_order"],a["common_parity_group_order"])==(18,54); print("assertions ok")'
sha256sum -c SHA256SUMS
```

The result payload is deterministic with `seed=null` and dependencies `{}`;
elapsed wall time is printed to the console but deliberately omitted from the
hashed JSON.  The frozen M137 checker is a read-only dependency whose expected
digest is embedded and verified before import.

## Frozen claim scope

The freeze proves that for `d>=5`, every nonempty subfamily of any matching
in M135's orbit-incidence graph has source and target aligned generated
subgroup exactly the same common-parity group.  This includes every M135
perfect-matching color and every choice of physical representatives.  It also
records the exact actual and abstract `d=3` failures and the `d=4` exclusion.

This is a negative sharpening only.  It proves no common braid,
matching-coset intersection, polynomial word length, gap, or terminal
outcome.  No cache directory is part of the freeze.  No file outside the
owned M141 mission directory was modified.
