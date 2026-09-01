# M287 immutable dependency audit

Date: 2026-08-14 UTC.

## M285 source gate

The frozen M285 checksum-file digest is exactly

```text
54eed4258da59ee1b8491815f182f05ac7c57c809e0f002bc2a2a79666098ac8.
```

Its `SHA256SUMS` contains exactly ten payloads, all of which pass:

1. `plan.md`
2. `checkpoint.md`
3. `dependency_audit.md`
4. `coefficient_reduction.md`
5. `psd_obstruction_k3.py`
6. `psd_obstruction_k3.json`
7. `report.md`
8. `run_manifest.md`
9. `fresh_audit_request.md`
10. `freeze_manifest.md`

The directory contains precisely these ten payloads plus `SHA256SUMS`, which
correctly excludes itself.  No M285 file was edited.

## Declared predecessor ledgers

Every declared checksum-file digest and listed-payload count agrees with
M285, and every listed payload passes `sha256sum -c SHA256SUMS`:

| mission | checksum-file SHA-256 | listed payloads | result |
|---|---|---:|---|
| M280 | `60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9` | 10 | all pass |
| M283 | `156fa5207e088f38ae71b69e48332a8a708bae8f03f1447c77e9710128572cdf` | 10 | all pass |
| M91 | `0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703` | 13 | all pass |
| M94 | `47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562` | 15 | all pass |
| M261 | `b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b` | 9 | all pass |
| M264 | `b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f` | 6 | all pass |

The controlling claims were checked in the proof ledgers themselves:

- M280/M283 prove the exact positive-prefactor identity
  `CP_j=Lambda_n eta_j(F_ell)/[(n-3)(n-4)]`, including the channel-two
  fair-component convention; they leave OCI and every downstream sign claim
  unresolved.
- M91 proves the normalized `J=1,2` channel laws and the measure-valued
  Borel--Abel identity; `BA2` and the balanced L1 estimate remain unresolved.
- M94 proves a central-double obstruction reduction and finite diagnostics;
  `BD`, `BA2`, and direct L1 remain unresolved.  M285 imports no asymptotic
  conclusion from it.
- M261/M264 prove the literal rooted-owner coefficient and the
  collision/decorated affine identity; PBV, FD, minority sign, and FCL1
  remain unresolved.

These statuses match M285's dependency ledger.  No predecessor was edited.

