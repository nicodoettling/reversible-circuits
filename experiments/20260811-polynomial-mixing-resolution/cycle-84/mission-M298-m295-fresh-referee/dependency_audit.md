# M298 dependency and integrity audit

Date: 2026-08-14 UTC.

## 1. Frozen M295 gate

The supplied top digest is reproduced exactly:

```text
42fa1c38b08359ae949fa0076557c2d42fdda232d1e7b318432e6787795ca3e5  SHA256SUMS
```

The directory contains exactly the following authoritative payload plus the
inventory file itself:

```text
plan.md
checkpoint.md
dependency_audit.md
proof.md
fmcp_k5.py
fmcp_k5.json
report.md
fresh_audit_request.md
run_manifest.md
freeze_manifest.md
SHA256SUMS
```

Every payload hash passes.  The authoritative M295 values are:

```text
4aa5e8004c86b9e654b593fc1029dd7fb2a88689ef51667a857fc5e4e62f2262  plan.md
17699c3711bff2d6a32496bb090d9a6b6adbaa862612b6bd19775053b9896bec  checkpoint.md
100f3ad0db014f0c01907a6c2f58cd5d67b0f96a2a6b2cebed6a6fa258d93e10  dependency_audit.md
92b5d0ec38e0715fd8b3f08c2fc5248b52d8a10811288d866ec8ccb599c8393c  proof.md
4beb596c924fc7ad515b6b69c623b9d5d744db88ce90db22acd0de7a5db637ab  fmcp_k5.py
6a3609c86cab162b530f4543b2b98a9165c7243a545252d9b583d3164e3e7c05  fmcp_k5.json
0602bdf57c8901790764c172b23a01c8d4a0a0ce6a1933806555a116f67193e5  report.md
456cdbf499df14d5aae9424f8364a0177860b5ee926e785015aeda2f66619b11  fresh_audit_request.md
c05583063c099eff93c9603c808292333e49099295f008252f8b89acc75e9437  run_manifest.md
b8ca553b1a3af1605aeba0c7233960fd9d0ee2ee87f4ee616f6ff1f4d8725087  freeze_manifest.md
```

Replaying the frozen command into `/tmp/m298-m295-replay.json` produces SHA-256
`6a3609c86cab162b530f4543b2b98a9165c7243a545252d9b583d3164e3e7c05`,
identical to the frozen raw output.

## 2. Prerequisite inventories and ledger entries

All eight prerequisite `SHA256SUMS` files pass `sha256sum -c`; their top
digests agree exactly with the coordinator ledger:

| mission | top inventory digest | ledger checked | accepted input relevant here |
|---|---|---|---|
| M266 | `6203ef0dca1e2c46696cec5bc1446da9656ace2b8a3a4ce9b2131267b200c052` | L-0302 | PCS is only a signed-total bound |
| M268 | `62976d7adca32d4ea7819ad36c7623430e26f75eced98a7b88bec58a4d0de2ef` | L-0302 | fresh acceptance of the same restricted PCS assembly |
| M274 | `c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e` | L-0306 | channel/minority-sign hierarchy and finite `k=5` weighted value |
| M277 | `c419b7c95e7c6fe4086d1098d6f0578445a1c3af700cabe4e90cf90d7c39d890` | L-0306 | clean-room acceptance and reflected-lag corrections |
| M280 | `60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9` | L-0309 | exact CP/owner-response normalization and lag domain |
| M283 | `156fa5207e088f38ae71b69e48332a8a708bae8f03f1447c77e9710128572cdf` | L-0309 | independent normalization, no extra channel-two half |
| M285 | `54eed4258da59ee1b8491815f182f05ac7c57c809e0f002bc2a2a79666098ac8` | L-0311 | positive-composition and repaired-autocorrelation reduction |
| M287 | `0298ecf0d0f3ca2970f4a817469a01e247b125b4b0211eb748b752146e73fc35` | L-0311 | fresh acceptance of multiplicities, intervals, and scope |

No disagreement was found between the package, the cited frozen artifacts,
and the accepted ledger.  M266/M268 are deliberately unused in the finite
FMCP refutation: they would enter only a later minority-sign-to-FCL1 closure.

The independently reconstructed minimum weighted channel-one score is

```text
469380953030255528575240193615921483304253622141733093283
/62593163860600167157006651607817304625660070187459136716800,
```

which is the exact `k=5,j=1` value in M274 and M277.

## 3. Scope ledger

The audited target is the first separated auxiliary fixed cell for odd
`k>=3`, `n=3k`, and lags `2<=ell<=n-2`.  It is neither a theorem about the
global uniform identity-word law nor a direct analysis of the lazy exact
same-product `{3,4,5}` heat-bath kernel.

The accepted consequence is only: universal `FMCP_1` is refuted by an exact
`k=5` cell.  `GOCI_1`, `GOCI_2`, `OCI`, `CP`, `OS+`, `MS`, `FCL1`, FD,
every gap, polynomial mixing, and both Terminals remain unresolved.
