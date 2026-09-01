# M315 Dependency Audit

Date: 2026-08-14 UTC.

The SHA-256 digest of M312's `SHA256SUMS` reproduces exactly as

```text
e38d8eb38b8ee261cd399dc1bdfd654928b634a4cc41057bbf6bc2dcd727f745
```

and all ten parent payload rows pass.

All twelve cited predecessor inventories pass every row and reproduce their
recorded top digests:

```text
M112  13  43b5255f014d8d7e480aa6d17130bb982e30b12a763c20a94e8c453de38f9cb3
M119   8  1fa3bddcbc228cdf61e9be9fb316f9da88b38f44fb8d1c8fb8dd4638bac966a8
M135   7  8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358
M137   6  47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5
M291   7  cc60538b886df2a332dd06e6b3fc8ee1fb9cb2d032ef77b39c269c1fdafbc4b0
M294   5  64f2e3305855de7d9eaa57e4b315e7d379442acc6a1588389106f222feb9333a
M296   7  9ab0978c92fee4f92d000604eac4610dbbe6c7aeeebe3fe86968514990d1f7f
M299   5  1654bcd6319b3020fe49a34e54a9961b2687ba5daab107baca11873749065b8d
M301   8  ae7ca4a3089259ac59df8e15ea3ff8d957c01956d842454f2dd1dcf3a881adcd
M304  10  5518f47facfab896ca1d32d4d3f9626a52c25e05cf970861395d4e19c2a0f4cf
M306   9  f5d3c549d4fc7562953b2b577ba1b272e75f4d7a82e208f230983e77294bfe7f
M309   9  3c1ea181084844d56350b81f2d31e4c6391072080bdf3820cadbaa67460a2c54
```

Total: 94 predecessor payload rows, all passing.

M13's two directly cited pre-inventory artifacts reproduce as

```text
536fd8acf9b263984736b0f7bc2f986e8aa27bde14bf4392b4c60efc60febb67  diameter_audit.md
4cf19e45d9b0306b8e8744ae1cfc0935bba5ca7bbb64f62599f0e85dc7064324  report.md
```

The imported inputs supply finite transitivity, short individual frames,
exact transporter residualization, and the accepted rank-three subfamily
certificate. They do not supply actual all-rank WRAD/PHTC or polynomial
shortest literal representatives.
