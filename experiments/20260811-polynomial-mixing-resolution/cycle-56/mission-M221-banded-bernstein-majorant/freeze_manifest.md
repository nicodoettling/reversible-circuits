# M221 freeze manifest

Date: 2026-08-13 UTC.
Status: frozen exact one-row minimal-bandwidth theorem and closure obstruction.

## Verdict

At `(B,L,kappa,D)=(1,6,2,1)`, the least feasible degree-six Bernstein
coefficient bandwidth is exactly one: width zero has an exact dual
obstruction, while an exact tridiagonal primal has positive domination and
budget margins. Raw width one is not stable under unsaturated retained lifts;
a cost-controlled recursive envelope remains unresolved.

## Ownership and immutable sources

- Owned directory:
  `cycle-56/mission-M221-banded-bernstein-majorant/`.
- M210/M213 and M216/M219 were checksum-verified and remained immutable.
- No shared durable project file or predecessor artifact was edited.

## Frozen payload inventory

1. `plan.md`
2. `checkpoint.md`
3. `bandwidth_theorem.md`
4. `banded_bernstein_exact.py`
5. `results.json`
6. `report.md`
7. `fresh_audit_request.md`
8. `freeze_manifest.md`
9. `SHA256SUMS` (ledger over the eight payloads above)

No numerical guidance, cache, bytecode, temporary output, or predecessor
import is part of the frozen directory.

## Reproduction

```text
cd experiments/20260811-polynomial-mixing-resolution/cycle-56/mission-M221-banded-bernstein-majorant
python3 -B banded_bernstein_exact.py --output results.json
sha256sum -c SHA256SUMS
```

Environment: Python 3.12.3, standard library only, exact `Fraction`
arithmetic, `seed=null`, one named top row and its forced recursion.

## Scope hygiene

Least bandwidth one is proved only for the exact named row. Saturated lifts
preserve bandwidth, but an unsaturated retained lift expands a width-one atom
to width five. No recursive width-one envelope, contraction, total AMV,
spectral gap, mixing, or Terminal result is frozen.

