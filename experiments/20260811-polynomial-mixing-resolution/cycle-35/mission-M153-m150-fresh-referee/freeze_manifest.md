# M153 freeze manifest

Date: 2026-08-13 UTC.

## Verdict and frozen scope

```text
FINAL VERDICT: ACCEPT.
NUMBERED OBJECTIONS: none.
```

The accepted claim is exactly that M150's explicit reduced Pin class lift is
signed-Hurwitz invariant and constant on aligned product-one transposition
factorizations: its centralizer quotient kills every kernel coordinate for
`d>=4`, and its rank-three cover splits.

This freeze does not claim completeness among central extensions or Nielsen
invariants, a common braid, an action-coset intersection, polynomial braid
length, a spectral gap, mixing, or a terminal outcome.

## Immutable predecessor gate

All six coordinator-supplied M150 hashes matched before substantive audit:

```text
report.md                    4c80fa05b6ef015f458a2f96fdf8a5c39e3f3e218fb16ac859e6c1f368ce3ad5
lifting_invariant_theorem.md f7a592f945213a565cb8bbbf07218396649e9cfdef3fd4d6a77e106a5fd8edfe
lifting_invariant_audit.py   349278984fcba6885caf6b4da2e2fdfedee69c14485ed87795f5b4c4a968c2e2
results.json                 5735acbd9e22567557e797c854b3c5f6aedc4a0bc00fdc74708bd1fa88a1195a
freeze_manifest.md           15825463c635a948f78df2b3d24b51e9deb6657c24660fdf951ef5a9b062eb97
SHA256SUMS                   70b2936be9deef248c12a77e1e08cf2b259f770976b7cf66eaaee5a08e46f0b3
```

The predecessor's own `sha256sum -c SHA256SUMS` passed all seven entries at
the end of this audit as well.  M150 was used read-only.

## Owned frozen payloads

```text
plan.md
checkpoint.md
cleanroom_pin_audit.py
results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes these six payload files and is not self-hashed.  Generated
Python cache files and `/tmp` console captures are not part of the freeze.

## Exact reproduction

Run from this directory with Python 3.12.3:

```text
python3 -m compileall -q cleanroom_pin_audit.py
python3 -B cleanroom_pin_audit.py
python3 -c 'import json; q=json.load(open("results.json")); assert all(x["kernel"]==["+1","-1"] for x in q["finite_pin_preimages"]); assert all(not row["failures"] for x in q["localized_kernel"] for row in x["rows"]); assert all(row["nonidentity_section_products"]==0 for row in q["d3_even_product_one"]["rows"]); print("M153 assertions ok")'
sha256sum -c SHA256SUMS
```

The checker is deterministic (`seed=null`), has no nonstandard dependencies,
and imports no M150 implementation.  Two consecutive runs produced identical
`results.json` SHA-256
`7af7c49eb042242d57c3ce66bb0786c5d62b86be5ca10ffd7cbdc56bbd0ed32f`.
