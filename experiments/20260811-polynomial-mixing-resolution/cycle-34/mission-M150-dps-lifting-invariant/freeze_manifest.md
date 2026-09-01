# M150 freeze manifest

Date: 2026-08-13 UTC.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen artifacts

```text
plan.md
checkpoint.md
lifting_invariant_theorem.md
lifting_invariant_audit.py
results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes precisely these seven payload files and is not
self-hashed.

## Exact reproduction

Run from this mission directory with Python 3.12.3:

```text
python3 -m compileall -q lifting_invariant_audit.py
python3 -B lifting_invariant_audit.py
python3 -c 'import json; q=json.load(open("results.json")); assert q["clifford_identity_audit"]["localized_commutator"]=="-1"; assert q["d3_split_cover_and_matching_audit"]["subfamilies_checked"]==135; assert not q["d3_split_cover_and_matching_audit"]["unequal_residual_vectors"]; assert all(not r["failures"] for r in q["d5_localized_centralizer_audit"]); print("assertions ok")'
sha256sum -c SHA256SUMS
```

The result payload is deterministic with `seed=null` and dependencies `{}`;
two consecutive runs produced identical SHA-256
`5735acbd9e22567557e797c854b3c5f6aedc4a0bc00fdc74708bd1fa88a1195a`.
The frozen M137 checker is a read-only dependency whose expected digest is
embedded and verified before import.

## Frozen claim scope

The freeze proves exact signed-Hurwitz invariance of the reduced Pin class
lift. For the aligned transposition-tuple class, it proves that the full
common-parity centralizer kills every coordinate kernel generator for
`d>=4`, while the rank-three cover splits and yields identity on every
product-one sequence. Thus the natural reduced Pin descriptor is constant on
all relevant M135 source and target factorizations.

This closes only the natural reduced Pin descriptor, not all central
extensions or Nielsen invariants. It proves no common braid,
matching-coset intersection, polynomial word length, gap, or terminal
outcome. No cache directory is part of the freeze. No file outside the owned
M150 mission directory was modified.

