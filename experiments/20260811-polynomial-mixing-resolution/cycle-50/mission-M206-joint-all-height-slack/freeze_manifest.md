# M206 freeze manifest

Date: 2026-08-13 UTC.
Status: frozen strict exact slack-ladder reduction; fresh audit requested.

## Immutable dependencies

Complete checksum ledgers passed before use for M173/M177, M179/M184,
M193/M197, and M201/M204. No predecessor was edited. The reproducibility
script additionally verifies frozen M204's literal-composition checker hash

```text
c55162114f0f89b1d6f2a0dd2721cce23f8a538bc834c11a84557e3d419be6d3
```

before importing it.

## Frozen payload inventory

1. `plan.md`
2. `checkpoint.md`
3. `slack_ladder_reduction.md`
4. `slack_ladder_exact.py`
5. `slack_ladder_results.json`
6. `report.md`
7. `fresh_audit_request.md`
8. `freeze_manifest.md`

`SHA256SUMS` hashes exactly these eight payloads and is excluded from its own
ledger.

## Reproduction and hygiene

```text
python3 -B slack_ladder_exact.py --output slack_ladder_results.json
```

The final checker evaluates only `(B,L)=(2,4),(3,4)`, uses exact
standard-library `Fraction` arithmetic, and has `seed=null`. No cache,
bytecode, temporary file, package, configuration, commit, or remote-state
change belongs to this package.
