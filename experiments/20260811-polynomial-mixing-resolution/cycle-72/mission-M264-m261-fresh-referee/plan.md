# M264 fresh referee plan

## Objective

Freshly audit only M261's strict PBV reduction.  The audit will not import
M261's derivation: it will first reconstruct the formulas independently and
only then compare them with the frozen artifact.

## Scope

- Verify M261's immutable inventory and advertised top digest.
- Re-derive the exact circular-completion coefficient, including same-owner
  and cross-owner values of `kappa` and every completion kind.
- Re-derive the endpoint-difference sign/index and prove `|E_ell| <= 8`.
- Check the M91 two-channel Abel normalization.
- Check `k^2 Lambda/R = Theta(n)` and `FD <=> PBV`.
- Check the pointwise affine split `n-8+2 1_T+I+Q`.
- Explain why the accepted `X_D`/`Y_D` DV/DE estimates do not directly
  control `E_ell`.
- Run a compact independent `k=3,5` falsification check.

## Claim discipline

This mission audits a conditional reduction only.  Finite checks cannot prove
PBV, FCL1, a spectral gap, polynomial mixing, or a terminal result.

## Expected artifacts

- `checkpoint.md`: independent derivation and comparison notes.
- `check_pbv_reduction.py`: compact no-M261-import falsification script.
- `results.txt`: exact small-case output.
- `final_report.md`: ACCEPT/REJECT with numbered objections and frozen hashes.
- `freeze_manifest.sha256`: immutable inventory.
