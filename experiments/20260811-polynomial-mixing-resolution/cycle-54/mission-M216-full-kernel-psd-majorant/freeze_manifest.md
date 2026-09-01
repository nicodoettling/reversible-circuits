# M216 freeze manifest

Date: 2026-08-13 UTC.
Status: frozen exact named-ansatz obstruction.

## Verdict

The degree-cap diagonal Bernstein PSD-envelope ansatz is refuted exactly at
`(B,L,kappa,D)=(1,6,2,1)`. Arbitrary nondiagonal or all-degree kernel
majorants and fresh contraction remain unresolved.

## Ownership and immutable inputs

- Owned directory:
  `cycle-54/mission-M216-full-kernel-psd-majorant/`.
- M157/M160 through M210/M213 were read-only, and every cited frozen ledger
  passed before substantive work.
- No shared durable project file or predecessor artifact was edited.

## Frozen payload inventory

1. `plan.md`
2. `checkpoint.md`
3. `bernstein_ansatz.md`
4. `bernstein_obstruction_theorem.md`
5. `bernstein_obstruction_exact.py`
6. `bernstein_obstruction_results.json`
7. `report.md`
8. `fresh_audit_request.md`
9. `freeze_manifest.md`
10. `SHA256SUMS` (ledger over the nine payloads above)

No cache, bytecode, temporary, imported predecessor, or broad scan artifact is
present.

## Reproduction

```text
cd experiments/20260811-polynomial-mixing-resolution/cycle-54/mission-M216-full-kernel-psd-majorant
python3 -B bernstein_obstruction_exact.py \
  --output bernstein_obstruction_results.json
sha256sum -c SHA256SUMS
```

Environment: Python 3.12.3, standard library only, exact `Fraction`
arithmetic, `seed=null`. The frozen checker reconstructs only the decisive
fresh row and performs no parameter scan.

## Scope hygiene

The raw lift is exactly Bernstein-multiplicative, but unsaturated
degree elevation is nondiagonal. The named ansatz uses an explicit
positive-linear diagonal PSD envelope. The rational dual refutes every final
degree-cap diagonal majorant, not the larger all-degree Bernstein dictionary
or arbitrary full kernels. The actual row has positive contraction slack.
No total AMV, gap, mixing, or Terminal inference is frozen.
