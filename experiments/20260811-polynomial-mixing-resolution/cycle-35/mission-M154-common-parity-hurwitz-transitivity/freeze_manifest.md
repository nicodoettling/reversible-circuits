# M154 freeze manifest

Date: 2026-08-13 UTC.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen artifacts

```text
plan.md
checkpoint.md
inner_nielsen_voltage_reduction.md
hurwitz_framing_audit.py
results.json
d4_exceptional_block_audit.py
d4_results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes precisely these nine payload files and is not
self-hashed.

## Exact reproduction

Run from this mission directory with Python `3.12.3`, SymPy `1.12`, and no
network access:

```text
python3 -c 'from pathlib import Path; [compile(Path(f).read_text(),f,"exec") for f in ("hurwitz_framing_audit.py","d4_exceptional_block_audit.py")]; print("compile ok")'
python3 -B hurwitz_framing_audit.py --output results.json
python3 -B d4_exceptional_block_audit.py
python3 -c 'import json; q=json.load(open("results.json")); assert q["d3"]["generating_ordered_pair_orbit_sizes"]==[216,216]; assert [(r["d"],r["transitive"],r["primitive"],r["all_positive_generators_even"]) for r in q["quotient_components"]]==[(3,True,True,True),(4,True,False,True),(5,True,True,True)]; r=json.load(open("d4_results.json"))["d4"]; assert r["sympy_blocks_equal_S4_mod_V4_fibers"] and r["accepted_M135_rank4_witness"]["therefore_common_literal_braid_obstructed"]; print("assertions ok")'
sha256sum -c SHA256SUMS
```

Both payloads are deterministic with `seed=null`. The checkers import no
predecessor code or result. They use predecessor reports read-only only to
record their SHA-256 provenance.

## Frozen claim scope

The freeze proves an explicit braid realization of every generated-group
inner conjugation and the exact inner-Nielsen/absolute parity-voltage
reduction for accepted `d>=5` M135 matching subfamilies. It records the
complete `d=3` two-orbit parity-framing split, the exact `d=4` exceptional
`S_4/V_4` block system and accepted-witness obstruction, and tightly capped
`d=5` quotient transitivity/primitivity.

It does not prove the broad `d>=5` one-orbit theorem, quotient alternating
image, zero-voltage routing, polynomial transporter length, common M135
braid, gap, mixing theorem, or terminal outcome. No cache directory is part
of the freeze. No file outside the owned M154 mission directory was modified.
