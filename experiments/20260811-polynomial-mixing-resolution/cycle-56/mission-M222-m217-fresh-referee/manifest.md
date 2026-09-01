# M222 reproducibility and freeze manifest

Date: 2026-08-13 UTC.

## Environment

- Repository commit at audit start:
  `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python: `3.12.3`
- Nonstandard dependencies: none
- Random seed: none; checker is deterministic

## Immutable input

Frozen M217 directory:

    experiments/20260811-polynomial-mixing-resolution/cycle-54/
      mission-M217-signed-averaged-de/

Verification command from that directory:

    sha256sum -c SHA256SUMS && sha256sum SHA256SUMS

Observed digest:

    7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557

## Reproduction

From this M222 directory:

    python3 checker.py

The single JSON line must agree exactly with `results.json` modulo whitespace
and object-key order. The checker has no import statement, uses no input
artifact, and is capped at `k=3,5`.

## Frozen verdict and scope

Verdict: **ACCEPT** M217's strict exact reduction, with no material or
nonmaterial M217 objections. WBE and DE remain open. DV, J2, PCR, downstream
gap claims, and both Terminals were excluded.

## Frozen file set

- `plan.md`
- `checkpoint.md`
- `proof_audit.md`
- `checker.py`
- `results.json`
- `report.md`
- `manifest.md`

`SHA256SUMS` is generated last over precisely this set. No cache or temporary
file belongs in the mission.
