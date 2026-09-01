# M327 immutable dependency audit

Date: 2026-08-14 UTC.

## Parent gate

Frozen M324 has exactly ten inventoried payloads.  Every row reports `OK`,
and the independently reproduced top digest is

```text
d42ba8d98c5d8c00501a01d458a1d6598bdfc8cce324344ae1e46b7081280aab.
```

## Source gate

Every cited source inventory was hashed independently and every payload row
passes:

| Mission | Rows | Reproduced top digest |
|---|---:|---|
| M135 | 7 | `8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358` |
| M137 | 6 | `47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5` |
| M296 | 7 | `9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f` |
| M299 | 5 | `1654bcd6319b3020fe49a34e54a9961b2687ba5daab107baca11873749065b8d` |
| M301 | 8 | `ae7ca4a3089259ac59df8e15ea3ff8d957c01956d842454f2dd1dcf3a881adcd` |
| M304 | 10 | `5518f47facfab896ca1d32d4d3f9626a52c25e05cf970861395d4e19c2a0f4cf` |
| M306 | 9 | `f5d3c549d4fc7562953b2b577ba1b272e75f4d7a82e208f230983e77294bfe7f` |
| M309 | 9 | `3c1ea181084844d56350b81f2d31e4c6391072080bdf3820cadbaa67460a2c54` |
| M312 | 10 | `e38d8eb38b8ee261cd399dc1bdfd654928b634a4cc41057bbf6bc2dcd727f745` |
| M315 | 8 | `50264b377b4b4db21afa9e722a42fdf76bc3d9c5fbf659845afa63112e9c2ac9` |
| M317 | 10 | `88a2480ec93ee6b3deb2d3e2e14b9a49a3f7e6ea71dca59997424c1356255245` |
| M320 | 10 | `132b871023f5fbdb0970c55c616d060fce1c3db8f8ac93277bdf29fc9a2b2d4d` |

The total is 99/99 passing source rows.  The displayed M296 value is the
actual frozen inventory digest; it agrees with M320's correction of M317's
nonmaterial transcription typo.

No predecessor, parent, coordinator, manuscript, guide, or project skill was
modified.
