# M146 freeze manifest

Date: 2026-08-13 UTC.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen artifacts

```text
plan.md
checkpoint.md
tuple_conjugacy_theorem.md
tuple_conjugacy_audit.py
results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes precisely these seven payload files and is not
self-hashed.

## Exact reproduction

Run from this mission directory with Python 3.12.3:

```text
python3 -c 'from pathlib import Path; p=Path("tuple_conjugacy_audit.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
python3 -B tuple_conjugacy_audit.py
python3 -c 'import json; q=json.load(open("results.json")); assert all(not r["failures"] for r in q["centralizer_parity_audit"]); assert all(not r["formula_failures"] and r["all_transposition_class_count"]==1 for r in q["direct_class_splitting_audit"]); assert q["d3_aggregate_by_width"]=={"1":{"class_multiset_equal":36},"2":{"class_multiset_equal":54},"3":{"class_multiset_equal":3,"literal_group_changed":33},"4":{"literal_group_changed":9}}; print("assertions ok")'
sha256sum -c SHA256SUMS
```

The result payload is deterministic with `seed=null` and dependencies `{}`;
two consecutive runs produced identical SHA-256
`7c49849f8ddae03922223c91f7f3414b531f0785d80ff48374bc0dfe3ff8a5aa`.
The frozen M137 checker is a read-only dependency whose expected digest is
embedded and verified before import.

## Frozen claim scope

The freeze proves the exact common-parity conjugacy-class splitting formula.
Using the accepted M141/M143 theorem, it proves that for `d>=5` every
nonempty subfamily of any M135 matching has a constant aligned-factor
conjugacy-class multiset on both source and target: `2d-2` copies of the
unique all-transposition tuple class. It also records the complete `d=3`
calibration.

This is a negative sharpening only. It proves no common braid,
matching-coset intersection, polynomial word length, gap, or terminal
outcome. No cache directory is part of the freeze. No file outside the owned
M146 mission directory was modified.
