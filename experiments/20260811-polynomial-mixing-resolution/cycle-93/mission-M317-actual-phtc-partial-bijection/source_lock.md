# M317 Source Lock

Date: 2026-08-14 UTC.

Every payload row in the following frozen inventories passes
`sha256sum -c SHA256SUMS`; each displayed value is the independently
reproduced digest of that inventory.

| mission | rows | top digest | imported scope |
|---|---:|---|---|
| M135 | 7 | `8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358` | actual matching conflict coloring |
| M137 | 6 | `47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5` | fresh conflict-color audit |
| M296 | 7 | `9ab0978c92fee4f92d000604eac4610dbbe6c7aeeebe3fe86968514990d1f7f` | framed chart-stabilizer transporters |
| M299 | 5 | `1654bcd6319b3020fe49a34e54a9961b2687ba5daab107baca11873749065b8d` | fresh transporter audit |
| M301 | 8 | `ae7ca4a3089259ac59df8e15ea3ff8d957c01956d842454f2dd1dcf3a881adcd` | agreement hypergraph and exact `d=3` triple |
| M304 | 10 | `5518f47facfab896ca1d32d4d3f9626a52c25e05cf970861395d4e19c2a0f4cf` | fresh agreement audit |
| M306 | 9 | `f5d3c549d4fc7562953b2b577ba1b272e75f4d7a82e208f230983e77294bfe7f` | WRAD dual and formal Sym/Alt guard |
| M309 | 9 | `3c1ea181084844d56350b81f2d31e4c6391072080bdf3820cadbaa67460a2c54` | fresh WRAD audit |
| M312 | 10 | `e38d8eb38b8ee261cd399dc1bdfd654928b634a4cc41057bbf6bc2dcd727f745` | anchored residual hierarchy and PHTC |
| M315 | 8 | `50264b377b4b4db21afa9e722a42fdf76bc3d9c5fbf659845afa63112e9c2ac9` | fresh PHTC-reduction audit |

All 79 rows pass.  The source scopes retain the following firewalls:

- M135 conflict independence is generated-paired-subgroup equality, not
  exact pair transporter compatibility and not common realization.
- M296 projection preserves finite common nonemptiness, not shortest literal
  braid length.
- M301's actual `d=3` triple is a boundary obstruction only.
- M306's natural `Sym/Alt` action is formal, not the actual M135 action.
- M312/M315 leave actual `d>=6` PHTC/WRAD and literal length unresolved.
