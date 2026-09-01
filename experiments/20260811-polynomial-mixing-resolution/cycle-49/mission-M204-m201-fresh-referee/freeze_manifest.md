# M204 freeze manifest

Date: 2026-08-13 UTC.
Status: frozen `ACCEPT` referee package.

## Immutable source gate

- M201 exact inventory: `9` files, comprising `SHA256SUMS` plus `8` payloads.
- M201 payload check: `8/8 OK`.
- M201 SHA-ledger digest:
  `9ede2ffaf0815cc76d8a7811d542d4a967370ee10791af73a590692ecacd524a`.
- Accepted dependency ledgers checked: M173/M177, M179/M184, M193/M197.
- Predecessor edits: none.

## Frozen M204 payload inventory

1. `plan.md`
2. `checkpoint.md`
3. `independent_exact.py`
4. `independent_results.json`
5. `proof_audit.md`
6. `report.md`
7. `freeze_manifest.md`

`SHA256SUMS` contains hashes of exactly these seven payloads and is excluded
from its own ledger. The checker command is

```text
python3 -B independent_exact.py --output independent_results.json
```

No cache, bytecode, temporary file, predecessor import, or broad scan belongs
to this package.
