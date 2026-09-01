# M286 freeze manifest

Date: 2026-08-14 UTC.

## Frozen verdict

```text
ACCEPT M282 AS FROZEN AT CSBV SCOPE ONLY.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL OBJECTIONS: NONE.
```

## Frozen payload

- `plan.md`
- `checkpoint.md`
- `proof_audit.md`
- `cleanroom_csbv_audit.py`
- `cleanroom_results.json`
- `report.md`
- `run_manifest.md`
- this `freeze_manifest.md`

`SHA256SUMS` is generated after this manifest, inventories every payload
above, and excludes itself.  There are no cache or temporary files.

## Scope firewall

The maximum accepted conclusion is M282's `CSBV` theorem for odd `k>=3` at
the auxiliary balanced fixed-cell scope.  `CEBV`, `CIBV`, `DOR`, `SET`,
`PBV`, `FD`, `FCL1`, the global identity-word law, the local heat-bath gap,
polynomial mixing, and Terminal A/B remain unresolved.
