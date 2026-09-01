# M219 freeze manifest

Date: 2026-08-13 UTC.
Status: frozen fresh-referee acceptance of M216.

## Verdict

`ACCEPT`, with no material or nonmaterial objections. The exact M216
degree-cap diagonal Bernstein obstruction reproduces independently. The
actual named row has positive contraction slack. No broader-kernel,
contraction, gap, mixing, or Terminal claim is accepted.

## Immutable source

- Source directory:
  `cycle-54/mission-M216-full-kernel-psd-majorant/`.
- Verified source ledger digest:
  `2c25bb31839bf8ff64181b9e4437fe70f5530bf5e7d0aa4eca8de4c21388d414`.
- All nine source payloads pass and M216 was not edited.

## Frozen payload inventory

1. `plan.md`
2. `checkpoint.md`
3. `independent_reconstruction.py`
4. `results.json`
5. `proof_audit.md`
6. `report.md`
7. `freeze_manifest.md`
8. `SHA256SUMS` (ledger over the seven payloads above)

No cache, bytecode, predecessor import, parameter scan, or temporary output is
part of the M219 directory.

## Reproduction

```text
cd experiments/20260811-polynomial-mixing-resolution/cycle-55/mission-M219-m216-fresh-referee
python3 -B independent_reconstruction.py --output results.json
sha256sum -c SHA256SUMS
```

Environment: Python 3.12.3, standard library only, exact `Fraction`
arithmetic, `seed=null`. The checker reconstructs only the named top row
`(B,L,kappa,D)=(1,6,2,1)` and its forced recursive descendants.

## Scope hygiene

The accepted conclusion refutes only final majorants in the degree-six
diagonal Bernstein cone. It does not refute the larger all-degree Bernstein
dictionary, arbitrary nondiagonal Bernstein/Jacobi/Green kernels, fresh
contraction, total AMV, a spectral gap, mixing, or Terminal A/B.

