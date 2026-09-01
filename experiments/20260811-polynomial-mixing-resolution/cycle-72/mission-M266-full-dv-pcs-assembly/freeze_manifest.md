# M266 freeze manifest

Date: 2026-08-14 UTC.

Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Immutable dependency gate

All fourteen named predecessor inventories passed `sha256sum -c` before
assembly.  Their checksum-file digests, together with M259's corrected M166
freeze-manifest hash, are in `dependency_manifest.md`.  No predecessor file
was edited.

## Claim-bearing payload

- `assembly_proof.md`: exact full-DV assembly and response chain through PCS.
- `dependency_manifest.md`: predecessor checksum digests and M166 correction.
- `verify_assembly.py`, `results.json`: deterministic arithmetic, domain,
  channel-normalization, and scope-guard checks.
- `report.md`: scoped verdict and exact FD/minority-sign stop.
- `fresh_audit_request.md`: independent-referee instructions.
- `run_manifest.md`: environment and reproduction commands.
- `plan.md`, `checkpoint.md`: mission provenance.
- this `freeze_manifest.md`.

All ten files above are recorded in `SHA256SUMS`.  M266 is immutable after
that checksum inventory is written.

## Reproduction

```text
python3 -B verify_assembly.py
python3 -m compileall -q verify_assembly.py
```

Python `3.12.3`, standard library only, deterministic, `seed=null`.  No
network, nonstandard package, Magma, SAT, ILP, or broad experimental census
was used.

## Frozen verdict and exclusions

The former DV hypothesis is discharged with common constant `18900`, and the
accepted auxiliary first-fixed-cell response chain is thereby unconditional
through PCS-bound.  FD-bound or minority-sign remains the exact independent
stop.  M266 claims no PCR, FCL1, direct-L1/all-edge estimate, H0, bridge gap,
polynomial mixing, or Terminal.

