# M238 freeze manifest

Date: 2026-08-13 UTC.

## Source lock

- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: `3.12.3`.
- Frozen M235 checksum-file digest:
  `7e929497029ae0c007d0544d30f0ad3c0198947ce55f946ee7eb0aaa88b19527`.
- All dependency inventory digests are recorded in `proof_audit.md` through
  the verified M235 manifest.
- Permutation convention: `(pq)(x)=p(q(x))`.
- No network, nonstandard package, randomness, Magma, SAT, or ILP was used.
- No predecessor code or generated data is imported by the checker.

## Reproduction commands

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-61/mission-M238-m235-fresh-referee/cleanroom_tcm_referee.py
python3 -m compileall -q experiments/20260811-polynomial-mixing-resolution/cycle-61/mission-M238-m235-fresh-referee
```

The first command produces the payload frozen as `results.json`.

## Frozen files

```text
plan.md
checkpoint.md
proof_audit.md
cleanroom_tcm_referee.py
results.json
report.md
manifest.md
```

`SHA256SUMS` records these seven files.  After that inventory is written,
M238 is immutable.

## Scope

The verdict accepts only M235's TCM theorem with constant 160.  It makes no
claim about YCM, WBE, DE, conditional J2, PCR/WPCR, downstream responses, a
spectral gap, mixing, or either Terminal.
