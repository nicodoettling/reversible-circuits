# M241 freeze manifest

Date: 2026-08-13 UTC.

## Frozen verdict

R1--R3 are proved with explicit constants `36`, `34`, `42`, and
`28`; their exact accepted-interface sufficiency gives SG with constant
`128` and GG2 with constant `70`. YCM and all downstream claims remain
open.

## Reproduction

From this directory:

    python3 ratio_strip_check.py

The checker is deterministic, standard-library only, seed null, and uses
exact rational interval arithmetic. It is capped at odd `3<=k<=31`; finite
checks prove no universal statement.

## Immutable inputs

- M226 `SHA256SUMS` digest:
  `a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a`.
- M229 `SHA256SUMS` digest:
  `6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688`.
- M232/M239 snapshot hashes and source commit are in `checkpoint.md`.

## Frozen file set

- `plan.md`
- `checkpoint.md`
- `ratio_strip_lemmas.md`
- `ratio_strip_check.py`
- `results.json`
- `report.md`
- `freeze_manifest.md`

`SHA256SUMS` is generated last over exactly this set. No cache or temporary
file belongs in the mission.
