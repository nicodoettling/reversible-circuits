# M309 immutable-package and dependency audit

Date: 2026-08-14 UTC.

## Frozen M306 package

The SHA-256 digest of M306's `SHA256SUMS` is exactly

```text
f5d3c549d4fc7562953b2b577ba1b272e75f4d7a82e208f230983e77294bfe7f
```

All nine listed payload rows pass `sha256sum -c SHA256SUMS`:

| payload | SHA-256 |
|---|---|
| `plan.md` | `880d971292d9d4f9004d179114c2df18f42c9bf8f0cd4b061a2eb988ac2e4b8f` |
| `checkpoint.md` | `fd922c8ff2d9f428dc461629aebdfb1ce7e05a7ba40485af3aa9a02e55e04402` |
| `halfway_checkpoint.md` | `3b98b2356ad7a215a9f1523c6a4ee99f26563531f81bcac70d625f38d4aae210` |
| `conditional_overlap_obstruction.md` | `c9234334e0e7caca59e8b0137bf2ac7be1e645b4077252b5d9180c71fba7b9a9` |
| `report.md` | `4c08e13d1c1bd30538ce39799eb72c68fc39aca3972f69f2be893ff6be380b39` |
| `audit_request.md` | `9086ca7900080901be4167adac9461c475b09e2ec92e53cd13d4ffb80534aa15` |
| `final_checkpoint.md` | `fd18f4a66f8d551a37fac20f1a5c52fbe0e86268b678deef58818f95c251f55c` |
| `run_manifest.md` | `42041a0d29aae90eb6dbbcef9ad49d5a1d83fa5f3fceec6be5f8befb8248e88b` |
| `freeze_manifest.md` | `d7142b60b9ba3f4190cc46a465aa11ac40cd7c277a2fae84b3ffa9450ce368cd` |

## Direct frozen dependencies

The four top digests cited by M306 reproduce exactly, and every row of each
manifest passes:

| mission | payload rows | reproduced top digest | audited import |
|---|---:|---|---|
| M296 | 7 | `9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f` | finite-action nonemptiness and literal-length separation |
| M299 | 5 | `1654bcd6319b3020fe49a34e54a9961b2687ba5daab107baca11873749065b8d` | fresh acceptance of M296's exact transporter reduction |
| M301 | 8 | `ae7ca4a3089259ac59df8e15ea3ff8d957c01956d842454f2dd1dcf3a881adcd` | agreement hypergraph, matching count, residual density, and `d=3` witness |
| M304 | 10 | `5518f47facfab896ca1d32d4d3f9626a52c25e05cf970861395d4e19c2a0f4cf` | independent acceptance and no-import reconstruction of M301 |

The semantic imports are correctly limited.  M296/M299 proves that finite
action common nonemptiness lifts to literal nonemptiness but does not control
shortest braid length.  M301/M304 proves the exact action-cover formulation
and the finite `d=3` obstruction, but leaves MRAD at actual `d>=6` open.  No
dependency supplies MRAD, SSTID, routing, voltage correction, congestion, a
spectral gap, mixing, or Terminal.

