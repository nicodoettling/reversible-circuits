# M295 freeze manifest

Date frozen: 2026-08-14 UTC.

The package freezes one predeclared candidate and one exact rank:

```text
candidate: FMCP_1 fixed-middle fully recombined channel-one pairing
rank: k=5, n=15 only
result: FMCP_1 refuted by an exact negative cell
GOCI/OCI consequence: none; every full channel-one lag remains positive
```

Frozen artifacts:

```text
plan.md
checkpoint.md
dependency_audit.md
proof.md
fmcp_k5.py
fmcp_k5.json
report.md
fresh_audit_request.md
run_manifest.md
freeze_manifest.md
```

`SHA256SUMS` is the authoritative byte inventory.  No package file may be
changed after that inventory is created; any correction requires a new
append-only mission or an explicitly versioned replacement package.

