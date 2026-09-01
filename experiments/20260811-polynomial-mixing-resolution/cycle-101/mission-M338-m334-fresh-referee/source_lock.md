# M338 immutable source lock

Date: 2026-08-14 UTC

## Audited M334 package

The observed SHA-256 digest of M334's `SHA256SUMS` is exactly

```text
c86c414e7d90fc01e0e13046afbbb5e1eaa66046b773d03a2f6cda78f350e29d
```

All 13 listed payloads pass: `aoec_k7.json`, `aoec_k7.py`,
`audit_request.md`, `candidate_frozen.md`, `checkpoint.md`,
`final_checkpoint.md`, `freeze_manifest.md`, `halfway_checkpoint.md`,
`obstruction.md`, `plan.md`, `report.md`, `run_manifest.md`, and
`source_lock.md`.

Filesystem timestamps are consistent with the declared freeze order:
`candidate_frozen.md` at 10:25:45 UTC, `aoec_k7.py` at 10:29:12 UTC, and
`aoec_k7.json` at 10:29:40 UTC on 2026-08-14. This is supporting chronology
evidence, not a cryptographic timestamp.

## Required 27-package source gate

Every listed top digest was independently recomputed and every inventory row
was checked in its own frozen directory.

| package | rows | observed top digest |
|---|---:|---|
| M91 | 13 | `0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703` |
| M94 | 15 | `47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562` |
| M100 | 5 | `bc5a915fc10aef4b546542938e9289e516e97a13553d4888d7b0395acd8965a2` |
| M161 | 6 | `17bd62a9b121a10058f87c576275411186e1c3c5039fa07a9cf29c9bea7358d8` |
| M166 | 5 | `344b6c76e538ecc82ac64ace908a21aabfb805330bad8a72c6ba042831e869c3` |
| M261 | 9 | `b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b` |
| M264 | 6 | `b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f` |
| M267 | 8 | `001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6` |
| M270 | 9 | `6c0c6e13c62885a0c56e8c232c0f2ddc48922be56b3edce97a4f9c9b9ca5491e` |
| M274 | 10 | `c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e` |
| M277 | 11 | `c419b7c95e7c6fe4086d1098d6f0578445a1c3af700cabe4e90cf90d7c39d890` |
| M280 | 10 | `60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9` |
| M283 | 10 | `156fa5207e088f38ae71b69e48332a8a708bae8f03f1447c77e9710128572cdf` |
| M285 | 10 | `54eed4258da59ee1b8491815f182f05ac7c57c809e0f002bc2a2a79666098ac8` |
| M287 | 10 | `0298ecf0d0f3ca2970f4a817469a01e247b125b4b0211eb748b752146e73fc35` |
| M295 | 10 | `42fa1c38b08359ae949fa0076557c2d42fdda232d1e7b318432e6787795ca3e5` |
| M298 | 13 | `d56bd6de3307284a8c5a135f5282ed1f1a3a793125ca056bb72f675e64f38cf8` |
| M300 | 15 | `24964f0c5c8e8588715a98fc22a80d7b268b8e6abe683bd95772f51acecbebc8` |
| M303 | 9 | `a3a708c95c72be4d665a47bcfe14196c1bc11bb281c9e26ee3b625b843cf1e72` |
| M307 | 10 | `41d6096e07da79c374a06947a882820a3e470aa9fb6415217909cb4404bf765e` |
| M308 | 9 | `37dbb530c567545cc25effa6902708a847c40daae3ff79487e46e0a4d91d1b4f` |
| M311 | 15 | `a022f56fc8f66dd4ea4d5a07b355e5e7612b57bb537c29fb3f94120cc155f842` |
| M314 | 12 | `87c66bea153cc25e8d2bdbc21d9a5530b0fa68e82d7e06c9fbf2f30d3a5d39c8` |
| M318 | 14 | `93501a792bd59a9aa6be808c87f404d80c928634360d522d300a34bc64b0ee03` |
| M322 | 8 | `210c3169e91ee5e4c6874bece0133174756b21b473fa65ba0437173422964067` |
| M325 | 12 | `8fe1b7f9cf1ab650422eecee67c97ff6afa0f0608659a6bd0decce592358b882` |
| M332 | 10 | `90f8e35700c233e850a4b8e9798605a0d0b765789e790dd3df00f8f2821049f6` |

The 23 raw/formula packages through M314 contribute 230/230 passing rows;
M318/M322 add 22/22; M325/M332 add 22/22. Total required source gate:
**274/274 passing rows**. Including M334 itself, all 287 checked payload rows
pass. No source package was edited.
