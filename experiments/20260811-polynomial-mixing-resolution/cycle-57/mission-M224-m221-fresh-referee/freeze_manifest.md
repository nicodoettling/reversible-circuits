# M224 freeze manifest

Date: 2026-08-13 UTC.
Status: frozen fresh-referee acceptance of M221.

## Verdict

`ACCEPT`, with no material or nonmaterial objections. Least degree-six
Bernstein coefficient bandwidth one at the exact named row, and failure of
raw width-one closure under unsaturated lifts, both reproduce independently.
No recursive envelope or contraction inference is accepted.

## Immutable source

- Source directory:
  `cycle-56/mission-M221-banded-bernstein-majorant/`.
- Verified source ledger digest:
  `ff5315e5930f3d8dc3c959acbb4413e32df4cf1f9870338e94ec892c18ec1983`.
- All eight source payloads pass and M221 was not edited.

## Frozen payload inventory

1. `plan.md`
2. `checkpoint.md`
3. `independent_referee.py`
4. `results.json`
5. `proof_audit.md`
6. `report.md`
7. `freeze_manifest.md`
8. `SHA256SUMS` (ledger over the seven payloads above)

No cache, bytecode, predecessor import, scan, or temporary output is part of
the frozen directory.

## Reproduction

```text
cd experiments/20260811-polynomial-mixing-resolution/cycle-57/mission-M224-m221-fresh-referee
python3 -B independent_referee.py --output results.json
sha256sum -c SHA256SUMS
```

Environment: Python 3.12.3, standard library only, exact `Fraction`,
`seed=null`, one named top row and its forced recursion.

## Scope hygiene

Least bandwidth one is accepted only at `(B,L,kappa,D)=(1,6,2,1)`. Raw
unsaturated lifts can expand width one to width five. No cost-controlled
recursive envelope, all-state majorant, contraction, total AMV, spectral gap,
mixing, or Terminal result is frozen.

