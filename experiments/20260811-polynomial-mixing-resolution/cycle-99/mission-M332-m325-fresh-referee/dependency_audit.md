# M332 dependency audit

Date: 2026-08-14 UTC

## M325 immutable gate

- Frozen directory: `cycle-97/mission-M325-owner-truncated-response-order`.
- Required top digest: `8fe1b7f9cf1ab650422eecee67c97ff6afa0f0608659a6bd0decce592358b882`.
- Independently observed top digest: exact match.
- Inventory: exactly 12 rows.
- Payload verification: 12/12 pass.

The exact inventory is `plan.md`, `checkpoint.md`, `source_lock.md`, `candidate_frozen.md`, `halfway_checkpoint.md`, `obstruction.md`, `active_owner_identity.md`, `report.md`, `final_checkpoint.md`, `run_manifest.md`, `freeze_manifest.md`, and `audit_request.md`.

## Cited package ledgers

Every cited `SHA256SUMS` top was recomputed independently and every row was checked from its package directory.

| package | rows | observed top digest | result |
|---|---:|---|---|
| M91 | 13 | `0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703` | pass |
| M94 | 15 | `47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562` | pass |
| M100 | 5 | `bc5a915fc10aef4b546542938e9289e516e97a13553d4888d7b0395acd8965a2` | pass |
| M161 | 6 | `17bd62a9b121a10058f87c576275411186e1c3c5039fa07a9cf29c9bea7358d8` | pass |
| M166 | 5 | `344b6c76e538ecc82ac64ace908a21aabfb805330bad8a72c6ba042831e869c3` | pass |
| M261 | 9 | `b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b` | pass |
| M264 | 6 | `b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f` | pass |
| M267 | 8 | `001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6` | pass |
| M270 | 9 | `6c0c6e13c62885a0c56e8c232c0f2ddc48922be56b3edce97a4f9c9b9ca5491e` | pass |
| M274 | 10 | `c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e` | pass |
| M277 | 11 | `c419b7c95e7c6fe4086d1098d6f0578445a1c3af700cabe4e90cf90d7c39d890` | pass |
| M280 | 10 | `60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9` | pass |
| M283 | 10 | `156fa5207e088f38ae71b69e48332a8a708bae8f03f1447c77e9710128572cdf` | pass |
| M285 | 10 | `54eed4258da59ee1b8491815f182f05ac7c57c809e0f002bc2a2a79666098ac8` | pass |
| M287 | 10 | `0298ecf0d0f3ca2970f4a817469a01e247b125b4b0211eb748b752146e73fc35` | pass |
| M295 | 10 | `42fa1c38b08359ae949fa0076557c2d42fdda232d1e7b318432e6787795ca3e5` | pass |
| M298 | 13 | `d56bd6de3307284a8c5a135f5282ed1f1a3a793125ca056bb72f675e64f38cf8` | pass |
| M300 | 15 | `24964f0c5c8e8588715a98fc22a80d7b268b8e6abe683bd95772f51acecbebc8` | pass |
| M303 | 9 | `a3a708c95c72be4d665a47bcfe14196c1bc11bb281c9e26ee3b625b843cf1e72` | pass |
| M307 | 10 | `41d6096e07da79c374a06947a882820a3e470aa9fb6415217909cb4404bf765e` | pass |
| M308 | 9 | `37dbb530c567545cc25effa6902708a847c40daae3ff79487e46e0a4d91d1b4f` | pass |
| M311 | 15 | `a022f56fc8f66dd4ea4d5a07b355e5e7612b57bb537c29fb3f94120cc155f842` | pass |
| M314 | 12 | `87c66bea153cc25e8d2bdbc21d9a5530b0fa68e82d7e06c9fbf2f30d3a5d39c8` | pass |
| M318 | 14 | `93501a792bd59a9aa6be808c87f404d80c928634360d522d300a34bc64b0ee03` | pass |
| M322 | 8 | `210c3169e91ee5e4c6874bece0133174756b21b473fa65ba0437173422964067` | pass |

Totals: the sixteen M274--M322 packages contribute 176/176 passing rows; the nine raw owner-law packages contribute 76/76 passing rows. Combined cited-ledger result: **252/252 pass**.

## Direct formula files

The nine direct formula hashes also reproduce exactly:

```text
fabcb2a73f52b7392296027d6399cbeda8801d1d2e8c829027e93d43f0e46596  M91/posterior_cancellation.md
f7d5369f58cf1e0f2aa34caf237fdc907a4012f15b49d5cff1ea9d3465517d09  M161/fixed_cell_convolution.md
de1959b27dbce09c2512c7abb45b2cbd0ff656868f3647fc862129a3bb8ebe82  M261/phase_difference_reduction.md
c90847fb0d9f884a2d6d111b3c466f6a39086410084530204edb5dcb181f2063  M285/coefficient_reduction.md
6025a23256427b43d0905ebac802e9aed953d718ad920b5564fc868d8081f564  M300/proof.md
501023406b52fa440f60362319a569143f13d2b6408559f071a43c4c2b1a12f6  M307/proof.md
5967ac262af3ea64de6c233f44944c2ad5bd019538c5bd9df4ac268d7cfd2138  M311/staircase_identity.md
26592ef0b81a201e76d5043702367f24927eeaa2f90e189bc2747d6f0c5f1806  M318/global_coboundary_identity.md
23931cf224ba63838adc3bc4dcc0151792533c6692f3f0efd9d06f3e92498208  M322/proof_audit.md
```

No dependency was edited or semantically promoted beyond its frozen scope.
