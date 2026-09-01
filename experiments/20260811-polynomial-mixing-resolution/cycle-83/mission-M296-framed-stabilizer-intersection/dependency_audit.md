# M296 Frozen Dependency Audit

Date: 2026-08-14 UTC.

## Byte-level verification

Every payload row in the following frozen inventories passes
`sha256sum -c`. The displayed digest is the SHA-256 of `SHA256SUMS` itself.

| mission | rows | top digest |
|---|---:|---|
| M112 | 13 | `43b5255f014d8d7e480aa6d17130bb982e30b12a763c20a94e8c453de38f9cb3` |
| M119 | 8 | `1fa3bddcbc228cdf61e9be9fb316f9da88b38f44fb8d1c8fb8dd4638bac966a8` |
| M135 | 7 | `8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358` |
| M137 | 6 | `47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5` |
| M284 | 6 | `3176a4b175fd58f65ed2b71d81c5d2f1fc794cb9e7c7e2370ebcecaff19a62f3` |
| M288 | 8 | `fd4120e216b9140c4a8938724c3415393d6f5495a105f817cf681871545942ca` |
| M291 | 7 | `cc60538b886df2a332dd06e6b3fc8ee1fb9cb2d032ef77b39c269c1fdafbc4b0` |
| M294 | 5 | `64f2e3305855de7d9eaa57e4b315e7d379442acc6a1588389106f222feb9333a` |

M13 predates the freeze format. Its observed proof-artifact hashes reproduce
the hashes independently recorded by M291/M294:

| artifact | SHA-256 |
|---|---|
| `cycle-02/mission-M13-hurwitz-barbell/diameter_audit.md` | `536fd8acf9b263984736b0f7bc2f986e8aa27bde14bf4392b4c60efc60febb67` |
| `cycle-02/mission-M13-hurwitz-barbell/report.md` | `4cf19e45d9b0306b8e8744ae1cfc0935bba5ca7bbb64f62599f0e85dc7064324` |

## Semantic gate

- **M13:** supplies individual constructive signed-Hurwitz routes of length
  at most `50Nm^3` inside one labeled weighted-component fiber. It supplies
  neither a simultaneous route nor congestion.
- **M112/M119:** supplies the exact rooted DPS product law, the `d`-to-one
  root quotient, and `|Z_d|=d^(d-3)(2d-2)!`.
- **M135/M137:** supplies free `G=S_d` and `H=Stab_G(d)` actions, the actual
  `H`-orbit edge quantifier, the perfect-matching colors, and the finite
  action-coset intersection obligation. Conflict independence is necessary,
  not simultaneous realization.
- **M284/M288:** supplies word-level rank lifting only after a genuine common
  base schedule and a valid chart are present. Chart/local-type coverage of
  a full color is false.
- **M291/M294:** supplies short separate frames through the fixed
  doubled-star chart and the intrinsic fibers
  `alpha_Q;BStab_d;delta_Q^(-1)`. Its exponential theorem applies only to
  one-sided common chart prefixes or suffixes, not to stabilizer cancellation.

The active coordinator ledger agrees at L-0026/L-0037, L-0227, L-0238,
L-0312, and L-0314. The older source-of-truth wording about the external
classification audit is stale relative to the accepted ledger; this mission
uses only the accepted audited scope and does not edit coordinator files.
