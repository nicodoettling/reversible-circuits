# M318 frozen source lock

Date: 2026-08-14 UTC.

Every row of each named frozen inventory passes `sha256sum -c`.  The values
below are independently reproduced SHA-256 digests of `SHA256SUMS`.

| mission | rows | top digest | imported scope |
|---|---:|---|---|
| M274 | 10 | `c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e` | minority-sign reduction and MON obstruction |
| M277 | 11 | `c419b7c95e7c6fe4086d1098d6f0578445a1c3af700cabe4e90cf90d7c39d890` | fresh audit of M274 |
| M280 | 10 | `60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9` | channel-combined coefficient target |
| M283 | 10 | `156fa5207e088f38ae71b69e48332a8a708bae8f03f1447c77e9710128572cdf` | fresh audit of M280 |
| M285 | 10 | `54eed4258da59ee1b8491815f182f05ac7c57c809e0f002bc2a2a79666098ac8` | owner-correlation reduction and PSD obstruction |
| M287 | 10 | `0298ecf0d0f3ca2970f4a817469a01e247b125b4b0211eb748b752146e73fc35` | fresh audit of M285 |
| M295 | 10 | `42fa1c38b08359ae949fa0076557c2d42fdda232d1e7b318432e6787795ca3e5` | signed-composition coefficient reduction |
| M298 | 13 | `d56bd6de3307284a8c5a135f5282ed1f1a3a793125ca056bb72f675e64f38cf8` | fresh audit of M295 |
| M300 | 15 | `24964f0c5c8e8588715a98fc22a80d7b268b8e6abe683bd95772f51acecbebc8` | all-middle exterior Hahn--Abel identity |
| M303 | 9 | `a3a708c95c72be4d665a47bcfe14196c1bc11bb281c9e26ee3b625b843cf1e72` | fresh audit of M300 |
| M307 | 10 | `41d6096e07da79c374a06947a882820a3e470aa9fb6415217909cb4404bf765e` | exact quantile identity and QCP obstruction |
| M308 | 9 | `37dbb530c567545cc25effa6902708a847c40daae3ff79487e46e0a4d91d1b4f` | fresh audit of M307 |
| M311 | 15 | `a022f56fc8f66dd4ea4d5a07b355e5e7612b57bb537c29fb3f94120cc155f842` | QBD staircase/rung/sign-block identity and QBP obstruction |
| M314 | 12 | `87c66bea153cc25e8d2bdbc21d9a5530b0fa68e82d7e06c9fbf2f30d3a5d39c8` | fresh audit and sole clean-room `k=11` guard |

All 154 listed payloads pass.  The imported semantic boundary is equally
strict: M307/M308 refutes its quantile-cell candidate while retaining positive
full aggregates at its sole guard; M311/M314 refutes cellwise and maximal
sign-block positivity at the first `k=11` failure while retaining the exact
QBD/QBP identities and positive complete aggregates.  No predecessor proves
MCLP, GOCI, OCI, CP, MS, FCL1, a gap, mixing, or Terminal.
