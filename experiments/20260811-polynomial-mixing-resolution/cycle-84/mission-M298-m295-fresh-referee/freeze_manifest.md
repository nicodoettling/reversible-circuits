# M298 freeze manifest

Date frozen: 2026-08-14 UTC.

Verdict:

```text
M295: ACCEPT
material objections: 0
nonmaterial objections: 1
refuted claim: FMCP_1 only
positive full-channel firewall: every complete eta_1 lag at k=5 is positive
downstream inference: none
```

The frozen referee payload is:

```text
plan.md
checkpoint.md
halfway_checkpoint.md
dependency_audit.md
proof_audit.md
independent_fmcp_audit.py
independent_results.json
compare_frozen.py
frozen_comparison.json
report.md
run_manifest.md
fresh_synthesis_request.md
freeze_manifest.md
```

`SHA256SUMS` is the authoritative byte inventory.  No payload file may be
changed after that inventory is created; any correction requires a new
append-only mission or an explicitly versioned replacement package.
