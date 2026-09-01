# M122 freeze manifest

Date: 2026-08-12.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen artifacts

```text
plan.md
checkpoint.md
star_cascade_obstruction.md
star_cascade_audit.py
star_cascade_results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes precisely these files and is not self-hashed.

## Exact reproduction

Run from this mission directory with Python 3.12.3:

```text
python3 -B star_cascade_audit.py --min-d 3 --max-d 24 \
  --output star_cascade_results.json
python3 -c 'from pathlib import Path; p=Path("star_cascade_audit.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
python3 -c 'import json, pathlib; q=json.loads(pathlib.Path("star_cascade_results.json").read_text()); assert q["all_finite_checks_pass"]; assert q["disjoint_last_factor_counterexample"]["short_endpoints_differ"]; assert q["disjoint_last_factor_counterexample"]["full_twist_succeeds"]; assert all(not r["failures"] for r in q["rows"]); print("json/assertions ok")'
sha256sum -c SHA256SUMS
```

The experiment is deterministic, uses `seed=null`, and has no nonstandard
dependency.  The universal DPS contour and full-twist arguments are proofs in
`star_cascade_obstruction.md`; the `d=3..24` run is a convention and
falsification audit only.

## Scope and hygiene

The freeze proves one infinite rooted ideal-edge family and two physical
routes for its square-prefix conjugation: an arbitrary-suffix `O(d^2)` full
twist and a sharper shared-endpoint `O(d)` route.  It refutes only universal
`O(1)` output/route locality.  All-edge stationary congestion, the full rooted
product comparison, arbitrary-product `Gamma_0`, and the original heat-bath
gap remain unresolved.  No cache directory is part of the freeze.  No file
outside this owned mission directory is modified by M122.
