# M290 immutable dependency audit

Date: 2026-08-14 UTC.

All twelve required `SHA256SUMS` files have the exact top digests below, and
every one of their 117 listed payloads passes `sha256sum -c`.  No predecessor
file was edited.

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

## Controlling ledgers

- M91/M94 supply exact normalized source/channel identities and warnings
  about unsigned Abel estimates; they prove no DOR-scale cancellation.
- M261/M264 prove the complete centered law `eta=P_B-P_A`, the literal
  rooted-owner formula, and `e^2 eta(E_ell)=eta(Delta I_ell+Delta Q_ell)`.
  DOR, PBV, FD, and FCL1 remain unresolved there.
- M267/M270 prove the null-owner endpoint law, the statewise `O(1)` envelope,
  and the first-order `rho` bounds.  SET/PBV remain unresolved.
- M276/M279 accept only the append-only repair of the `J=1` collision
  derivative at `O(1/k)`; they leave CIBV and every decorated estimate open.
- M280/M283 prove the exact rooted-owner coefficient and positive CP
  prefactor; OCI remains unresolved.
- M285/M287 prove the positive-composition owner law and autocorrelation
  repair and accept only a canonical signed-PSD obstruction.  GOCI/OCI remain
  unresolved.

These statuses are used literally.  No finite row or predecessor obstruction
is promoted to DOR or a downstream statement.
