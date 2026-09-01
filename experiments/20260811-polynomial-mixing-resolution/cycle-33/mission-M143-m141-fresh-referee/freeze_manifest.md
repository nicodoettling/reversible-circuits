# M143 freeze manifest

Date: 2026-08-13 UTC.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen verdict

```text
ACCEPT M141 AT ITS EXACT NONTERMINAL SCOPE.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

The accepted theorem is the `d>=5` multisource common-parity negative
sharpening. It proves no common signed braid, matching-coset intersection,
polynomial braid length, spectral gap, Terminal A, or Terminal B outcome.

## Frozen artifacts

```text
plan.md
checkpoint.md
independent_referee.py
independent_results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes exactly these six payload files and is not self-hashed.
No Python cache directory is part of the freeze.

## Input provenance

The checker verifies but never imports or executes these immutable M141
files:

```text
report.md                           ebda7181e031603f598648d2409f8a484645022f24acd34e92ef5813459afb87
multisource_subgroup_theorem.md     7c9588dc64e3731a90e3e59bbe60a4d15dc8a42c4f98ce7ed60c386c7e8b8678
multisource_subgroup_audit.py       44f8fd167808bb41d2823bb10943951d6404d88aa4530697760a914b1e321d93
results.json                        548ddf460a9184ebdc36c449ba35e8e2b8c3719b4994200808afa8868590c241
freeze_manifest.md                  b45f4a80ca8745a9f7e6291b5118b27a64e22040a7799f872773624aff671e62
SHA256SUMS                           9aa52349d288f04b7f46895cf7fe01373dcea807abf69892ef3ccea705acc057
```

## Exact reproduction

Run from this M143 mission directory with Python `3.12.3`:

```text
python3 -c 'from pathlib import Path; p=Path("independent_referee.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
python3 -B independent_referee.py
python3 -c 'import json; q=json.load(open("independent_results.json")); a=q["actual_d3_matching_audit"]["aggregate"]; assert a["colors"]==9 and a["equal_literal"]=={"1":36,"2":54,"3":3,"4":0}; b=q["abstract_d3_counterexample"]; assert (b["subgroup_order"],b["common_parity_order"])==(18,54); c=q["d4_pair_dichotomy_exception"]; assert (c["source_group_order"],c["target_group_order"])==(96,288); assert all(x["every_nonidentity_class_normally_generates"] for x in q["boundary_rank_simplicity_checks"]); print("assertions ok")'
sha256sum -c SHA256SUMS
```

The checker is deterministic with `seed=null`, dependencies `{}`, and finite
ranks capped at `3,4,5,6`. Elapsed wall time is printed to the console but
omitted from the hashed JSON. It writes only `independent_results.json` in
this owned directory. No file outside this M143 mission directory was
modified.

