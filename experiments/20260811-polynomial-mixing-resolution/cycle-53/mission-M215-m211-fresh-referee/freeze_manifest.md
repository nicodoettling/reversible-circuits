# M215 freeze manifest

Date: 2026-08-13 UTC.

## Frozen verdict

ACCEPT M211's refutation of pointwise IKBE-b and therefore the two-clause
IKBE conjunction. Zero material objections; two nonmaterial exposition
qualifications.

IKBE-a/DV, signed averaged DE, conditional J=2, and every downstream claim
remain open.

## Immutable input

M211 directory:

    experiments/20260811-polynomial-mixing-resolution/cycle-52/mission-M211-interval-kernel-boundary-edit

Every M211 SHA256SUMS entry passed before audit. Its checksum-file digest is
79f3e0f614a6cde4e3e4bd36ce55e217b35416f68470c6deab93598877874225.
No M211 file was modified.

## Reproduction

From this directory:

    python3 cleanroom_witness.py cleanroom_results.json

The checker is deterministic, standard-library only, seed null, formula-only,
and imports no M211 code/data. It checks q=1 only. The universal conclusion
comes from proof_audit.md, not the finite calibration.

## Frozen file set

- plan.md
- checkpoint.md
- proof_audit.md
- cleanroom_witness.py
- cleanroom_results.json
- results.json
- report.md
- freeze_manifest.md

SHA256SUMS is generated last over this exact set. No caches or temporary
outputs are included. A new referee should first verify all hashes and keep
M211/M215 immutable.
