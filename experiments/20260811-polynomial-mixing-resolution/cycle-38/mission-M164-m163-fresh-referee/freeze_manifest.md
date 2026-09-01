# M164 Freeze Manifest

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

## Exact reproduction

Run from this mission directory with Python `3.12.3` and no network:

```text
python3 -B independent_referee.py
sha256sum -c SHA256SUMS
```

The checker is deterministic with `seed=null`. It reads frozen M163 files
only to verify the six assigned hashes and does not import or execute
predecessor code.

## Frozen claim scope

This referee accepts M163's universal qualitative stabilizer-voltage affine-
coset theorem and exact `d=3`/accepted-witness `d=4` results with zero
material objections. It makes no `d>=5` voltage inference and no claim about
quotient routing, polynomial word length, inner-transporter length, a
spectral gap, mixing, or a terminal outcome. No cache directory is frozen and
no file outside this M164 mission directory was edited.
