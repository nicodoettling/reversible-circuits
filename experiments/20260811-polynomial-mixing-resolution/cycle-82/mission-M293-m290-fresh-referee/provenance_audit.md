# M293 immutable provenance audit

Date: 2026-08-14 UTC.

## M290 boundary

The SHA-256 digest of frozen M290's `SHA256SUMS` is exactly

```text
85373b13ab4799f59d98dd20bf5b0496fa61d119b45b0ffe34900094564df687
```

The checksum file names exactly ten payloads. Every one passes
`sha256sum -c SHA256SUMS`, and the directory contains exactly those ten files
plus `SHA256SUMS`. In particular, the proof, report, and freeze-manifest
digests are

```text
40840d7efd2931e8329632b7c1f14351e0f8faba10e2057b589541aee3570bf6  decorated_ratio_reduction.md
7d482cf7856bf3ba5eaf717661ec58c01a0b72ead4d4c23ca0d303e7f29da7e1  report.md
7046aea97f6206af59dc4bb6cf223892e3df742b6a0dac0009e01679caab6412  freeze_manifest.md
```

## Twelve cited predecessor boundaries

Each top digest below was computed independently. Every listed payload passes,
and in each case the actual directory inventory is exactly the payload list
plus `SHA256SUMS`.

| mission | checksum-file SHA-256 | payloads | result |
|---|---|---:|---|
| M91 | `0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703` | 13 | all pass |
| M94 | `47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562` | 15 | all pass |
| M261 | `b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b` | 9 | all pass |
| M264 | `b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f` | 6 | all pass |
| M267 | `001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6` | 8 | all pass |
| M270 | `6c0c6e13c62885a0c56e8c232c0f2ddc48922be56b3edce97a4f9c9b9ca5491e` | 9 | all pass |
| M276 | `882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db` | 9 | all pass |
| M279 | `3910c66a134083117e8defce4bf6a3d57fdce3a48b519e7c8271c1864bf52f66` | 8 | all pass |
| M280 | `60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9` | 10 | all pass |
| M283 | `156fa5207e088f38ae71b69e48332a8a708bae8f03f1447c77e9710128572cdf` | 10 | all pass |
| M285 | `54eed4258da59ee1b8491815f182f05ac7c57c809e0f002bc2a2a79666098ac8` | 10 | all pass |
| M287 | `0298ecf0d0f3ca2970f4a817469a01e247b125b4b0211eb748b752146e73fc35` | 10 | all pass |

The payload total is `117`, exactly as M290 states.

## Controlling-status check

- M91/M94 prove the normalized two-channel source/Abel identities and the Borel coefficient scales; they do not prove the needed signed cancellation.
- M261/M264 prove the complete centered product law, `Q` definition, affine collision/decorated identity, and PBV reduction; PBV and FD remain open.
- M267/M270 prove the null-owner endpoint law and an `O(1)` statewise envelope; SET and the target-scale signed estimate remain open.
- M276/M279 accept only M276's append-only repair of M272's channel-one tail; frozen M272 remains rejected, and DOR is explicitly open.
- M280/M283 prove the exact owner-correlation reduction and positive prefactor; OCI/CP remain open.
- M285/M287 prove the normalized channel coefficients, three/four positive-composition multiplicities, owner rows, and admissible-lag autocorrelation repair. They leave GOCI/OCI open and refute only the stated signed-PSD shortcut.

M290 imports those statements at exactly their frozen strengths. No cited ledger licenses BODT, DOR, or any downstream conclusion, and M290 does not claim otherwise.
