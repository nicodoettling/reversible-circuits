# M163 freeze manifest

Date: 2026-08-13 UTC.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen artifacts

```text
plan.md
checkpoint.md
proof.md
stabilizer_voltage_audit.py
results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes precisely these seven payload files and is not
self-hashed.

## Exact reproduction

Run from this mission directory with Python `3.12.3` and no network access:

```text
python3 -B stabilizer_voltage_audit.py
sha256sum -c SHA256SUMS
```

The checker is deterministic with `seed=null`. It verifies the frozen M158
checker SHA-256 before importing its elementary exact group/word primitives.
It writes `results.json` deterministically.

## Frozen claim scope

The freeze proves the abstract groupoid cocycle, stabilizer-voltage subgroup,
and exact endpoint affine-coset/zero-adjustability criterion for every
`d>=3`. It characterizes voltage by literal braid tuple stabilizers and
proves that the accepted inner `P_(d,s)` correction loops have zero relative
voltage. It exactly exhausts all `d=3` quotient tuples through width four and
finds trivial stabilizer voltage throughout. It exactly checks trivial
stabilizer voltage at both endpoints of the accepted `d=4` witness, whose
source and target are already quotient-separated by the `S_4/V_4` block.

It does not prove full stabilizer voltage for `d>=5`, zero membership of an
M135 endpoint coset, a quotient transporter, polynomial word length, short
inner correction, a gap, mixing, or a terminal outcome. The unsuccessful
bounded d5 stabilizer attempt is recorded only as a negative finding. No
cache directory is part of the freeze, and no predecessor file was modified.
