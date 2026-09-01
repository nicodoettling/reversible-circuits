# Mission M244 Plan: DPS Initial-Defect Lemma

Date: 2026-08-14

## Objective

Audit and, if possible, prove exactly the Initial-Defect Lemma (IDL-a through
IDL-d, including the closed equality) isolated by frozen M240, starting from
the actual plus-mirror doubled-plane-star (DPS) stack / hairy-tree
construction at arbitrary rank `d`.

## Immutable inputs

- M240 all-rank `Z2` strict reduction, freeze digest
  `2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3`.
- M242 fresh audit, freeze digest
  `49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663`.
- Accepted M231/M234 and M236/M237 are finite calibration only.

## Scope and conventions

- Lock the exact DPS primary source cited by M240 and translate its
  permutation and Hurwitz-action conventions explicitly.
- Preserve `N-1`: do not use the generic fixed-edit `(R^{-1})^2` identity.
- Establish the analytic all-rank coordinate recurrence before any finite
  calculation. A tiny symbolic `d=5,6` falsifier may then test that recurrence.
- If full IDL fails, record the first exact coordinate counterexample. If the
  source construction stops short, reduce IDL to the first standalone stack
  lemma with all quantifiers and boundary cases.
- Make no every-color, voltage, total-length, spectral-gap, mixing, or
  Terminal inference.

## Deliverables

- `checkpoint.md` and a halfway checkpoint.
- A theorem or sharp reduction with explicit source/convention translation.
- A minimal symbolic checker and machine-readable output if useful.
- `report.md`, freeze manifest, hashes, and a request for fresh audit.

## Claim labels

All statements will be marked `proved`, `conditional`, `empirical`,
`refuted`, or `unresolved`. Finite checks are calibration and cannot prove an
all-rank identity.
