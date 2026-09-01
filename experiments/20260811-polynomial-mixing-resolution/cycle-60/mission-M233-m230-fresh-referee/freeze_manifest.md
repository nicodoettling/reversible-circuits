# M233 freeze manifest

Date: 2026-08-13 UTC.
Status: `FROZEN — ACCEPT M230 CORRECTED SALVAGE; REJECT M227 AS FROZEN`.

## Scope and result

M233 is the fresh immutable referee of M230. It verifies M230's frozen
inventory, independently confirms the material defect in M227, and replays
the corrected full-seven-dimensional dual and primal certificates with exact
arithmetic. It accepts only the one-atom conclusion `p_1>p_2>1/4` and no
downstream uniform or recursive statement.

## Frozen artifacts

```text
plan.md
checkpoint.md
cleanroom_exact.py
results.json
audit_report.md
freeze_manifest.md
SHA256SUMS
```

`SHA256SUMS` hashes the first six payloads and does not self-hash. Its own
SHA-256 is the M233 freeze digest.

## Reproduction

```text
python3 -B cleanroom_exact.py --output results.json
python3 -m compileall -q cleanroom_exact.py
sha256sum -c SHA256SUMS
```

Python 3.12.3, standard library only, exact `Fraction`, `seed=null`. The
checker imports/reads no M230 or M227 code/data. Both predecessors remained
unchanged.
