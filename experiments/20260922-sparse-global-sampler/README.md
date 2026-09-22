# Sparse global identity-bridge sampler

Read [proof.md](proof.md) for SG-T1.v1 and [coordinator_report.md](coordinator_report.md) for audit status. The requested H0 and separately labeled H1 use one fixed top-level work cutoff. Their exact conditional laws have an explicit negligible global error for every even m³<=N², hence the requested m⁵<=N³; see the theorem for conservative constants and small cases.

Run from repository root:

```sh
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 82 --m 14 --certificate-only
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 4 --m 6
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 4 --m 6 --policy H1
```

H0 is the default. Each JSON response reports its conditional target and exact global-TV certificate. CLI labels are1-based; Python API labels are0-based. Large certificate integers/rationals use lossless hexadecimal objects when decimal serialization would exceed the interpreter's limit. No interpreter limit is changed. `--seed` is for reproducible diagnostics; exactness is stated in the fair-bit model.

The reusable APIs and implementation details are in [roles/r3-sampler/README.md](roles/r3-sampler/README.md). Historical dependencies are hash-checked before execution. All work is standard-library Python3.12.3; use `-B` to avoid bytecode artifacts. `changed_files.txt` is the precise attributable inventory. Launcher-owned metadata and pre-existing September7 work are excluded.
