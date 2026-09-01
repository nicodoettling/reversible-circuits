# M312 source lock

Date: 2026-08-14 UTC.

Every payload row in the following frozen inventories passes
`sha256sum -c SHA256SUMS`; the displayed value is the independently
reproduced SHA-256 digest of the inventory itself.

| mission | rows | top digest | imported scope |
|---|---:|---|---|
| M112 | 13 | `43b5255f014d8d7e480aa6d17130bb982e30b12a763c20a94e8c453de38f9cb3` | exact minimal-sector count/root quotient |
| M119 | 8 | `1fa3bddcbc228cdf61e9be9fb316f9da88b38f44fb8d1c8fb8dd4638bac966a8` | fresh count audit |
| M135 | 7 | `8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358` | actual matching-selected H-orbit edges |
| M137 | 6 | `47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5` | fresh matching/incidence audit |
| M291 | 7 | `cc60538b886df2a332dd06e6b3fc8ee1fb9cb2d032ef77b39c269c1fdafbc4b0` | two-sided short endpoint frames |
| M294 | 5 | `64f2e3305855de7d9eaa57e4b315e7d379442acc6a1588389106f222feb9333a` | fresh frame/fiber audit |
| M296 | 7 | `9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f` | transporter-coset residualization and finite/literal split |
| M299 | 5 | `1654bcd6319b3020fe49a34e54a9961b2687ba5daab107baca11873749065b8d` | fresh transporter audit |
| M301 | 8 | `ae7ca4a3089259ac59df8e15ea3ff8d957c01956d842454f2dd1dcf3a881adcd` | agreement hypergraph and MRAD reduction |
| M304 | 10 | `5518f47facfab896ca1d32d4d3f9626a52c25e05cf970861395d4e19c2a0f4cf` | fresh agreement audit |
| M306 | 9 | `f5d3c549d4fc7562953b2b577ba1b272e75f4d7a82e208f230983e77294bfe7f` | WRAD dual and conditional-overlap obstruction |
| M309 | 9 | `3c1ea181084844d56350b81f2d31e4c6391072080bdf3820cadbaa67460a2c54` | fresh acceptance of M306 |

All 94 listed payloads pass.  M13 predates the inventory format; its two
directly used proof artifacts reproduce as

```text
diameter_audit.md  536fd8acf9b263984736b0f7bc2f986e8aa27bde14bf4392b4c60efc60febb67
report.md          4cf19e45d9b0306b8e8744ae1cfc0935bba5ca7bbb64f62599f0e85dc7064324
```

M13 supplies individual signed-Hurwitz routes of length at most `50Nm^3`
within the fixed weighted-component fiber, hence transitivity of the finite
action on `Z_d`; it supplies neither simultaneous agreement nor congestion.
M135/M137's matching color selects actual edges but its conflict independence
is not common realization.  M291/M294 supplies separate source and target
frames, not a common prefix.  M296/M299 preserves finite common
nonemptiness exactly but explicitly does not preserve shortest literal braid
length.  M306/M309, now integrated by the coordinator as L-0322/CP-209,
leaves actual WRAD/MRAD open.

No rank-lift package is imported in M312 because no genuine common base
schedule has yet been proved.
