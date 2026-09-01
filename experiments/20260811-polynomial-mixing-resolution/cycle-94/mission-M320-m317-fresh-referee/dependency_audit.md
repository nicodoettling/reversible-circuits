# M320 dependency audit

Date: 2026-08-14 UTC

## Frozen M317

Observed top digest:

```text
88a2480ec93ee6b3deb2d3e2e14b9a49a3f7e6ea71dca59997424c1356255245  SHA256SUMS
```

This equals the assigned digest.  The inventory has exactly ten payloads:

```text
plan.md
checkpoint.md
source_lock.md
halfway_checkpoint.md
stabilizer_partial_bijection.md
report.md
audit_request.md
run_manifest.md
final_checkpoint.md
freeze_manifest.md
```

All ten `sha256sum -c SHA256SUMS` checks pass.

## Cited predecessor ledgers

| mission | rows | independently observed top digest | result |
|---|---:|---|---|
| M135 | 7 | `8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358` | all rows pass |
| M137 | 6 | `47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5` | all rows pass |
| M296 | 7 | `9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f` | all rows pass |
| M299 | 5 | `1654bcd6319b3020fe49a34e54a9961b2687ba5daab107baca11873749065b8d` | all rows pass |
| M301 | 8 | `ae7ca4a3089259ac59df8e15ea3ff8d957c01956d842454f2dd1dcf3a881adcd` | all rows pass |
| M304 | 10 | `5518f47facfab896ca1d32d4d3f9626a52c25e05cf970861395d4e19c2a0f4cf` | all rows pass |
| M306 | 9 | `f5d3c549d4fc7562953b2b577ba1b272e75f4d7a82e208f230983e77294bfe7f` | all rows pass |
| M309 | 9 | `3c1ea181084844d56350b81f2d31e4c6391072080bdf3820cadbaa67460a2c54` | all rows pass |
| M312 | 10 | `e38d8eb38b8ee261cd399dc1bdfd654928b634a4cc41057bbf6bc2dcd727f745` | all rows pass |
| M315 | 8 | `50264b377b4b4db21afa9e722a42fdf76bc3d9c5fbf659845afa63112e9c2ac9` | all rows pass |

The total is `7+6+7+5+8+10+9+9+10+8=79` rows.

## Provenance defect

M317's `source_lock.md` displays the M296 digest as

```text
9ab0978c92fee4f92d000604eac4610dbbe6c7aeeebe3fe86968514990d1f7f
```

but the frozen M296 `SHA256SUMS` actually hashes to

```text
9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f
```

Thus the phrase “each displayed value is the independently reproduced
digest” is false for this one row.  This is nonmaterial: the actual M296
inventory and all seven payloads verify; M317 imports the proved finite
chart-stabilizer transporter scope from those payloads, not the mistyped
string; and no hypothesis, implication, or stopping line branches on that
string.  Frozen M317 was not edited.

## Reproduction commands

From the repository root, for M317 and for each cited mission directory:

```text
sha256sum SHA256SUMS
wc -l SHA256SUMS
sha256sum -c SHA256SUMS
```

These are read-only checks.  No stale `/tmp` artifact was used.
