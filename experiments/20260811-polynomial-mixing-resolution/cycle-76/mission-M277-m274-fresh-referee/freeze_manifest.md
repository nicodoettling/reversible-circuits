# M277 freeze manifest

Date: 2026-08-14 UTC.

## Verdict

```text
ACCEPT M274 WITH NONMATERIAL CORRECTIONS.
```

The accepted core is the exact PCS--MS equivalence given PCS, literal raw and
two-channel formulas, exact MON/FOSD refutations, and arbitrary-odd-rank
sign-indefiniteness of the displayed raw ordered atoms.  CP, OS+, MS, FCL1,
all later-cell/direct-L1 statements, every gap or mixing statement, and all
Terminal claims remain open.

## Frozen payload

- `plan.md`
- `checkpoint.md`
- `halfway_checkpoint.md`
- `dependency_ledger.md`
- `independent_reconstruction.md`
- `cleanroom_sign_audit.py`
- `cleanroom_results.json`
- `report.md`
- `run_manifest.md`
- `fresh_synthesis_request.md`
- this `freeze_manifest.md`

`SHA256SUMS` is generated after this manifest, inventories every payload
above, and excludes itself.

## Two corrections and one scope firewall

- M274's transitive NumPy dependency was omitted from its metadata; M277's
  checker removes it.
- The `k=9` minimum is tied at reflected lags `y=7,18`.
- The all-rank obstruction is to literal raw ordered-atom positivity, not to
  every imaginable regrouped representation.

No M274 or predecessor file was edited.
