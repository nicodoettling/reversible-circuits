# M291 frozen dependency audit

Date: 2026-08-14 UTC.

## Byte-level verification

Every row named by the following frozen `SHA256SUMS` files passed
`sha256sum -c`.  This checked 166 payload rows in total.  The displayed
digest is the SHA-256 of the corresponding `SHA256SUMS` file itself.

| mission | rows | top digest |
|---|---:|---|
| M112 | 13 | `43b5255f014d8d7e480aa6d17130bb982e30b12a763c20a94e8c453de38f9cb3` |
| M119 | 8 | `1fa3bddcbc228cdf61e9be9fb316f9da88b38f44fb8d1c8fb8dd4638bac966a8` |
| M135 | 7 | `8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358` |
| M137 | 6 | `47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5` |
| M175 | 8 | `f2718a493b7e30a615da1f6e4dbafad9d6501bcbd07822fd791b21eafbb26d88` |
| M176 | 8 | `92fe0752f2014fd320f8bf3ff10e09266872865f705a66ed32787c876592fe4a` |
| M181 | 8 | `d2ae8d5a2af347eb74943db1221607d46fc706296ac2802d97abc0a024ec20b0` |
| M183 | 7 | `ddd2bf1d2ce8d22e2228624d8802b38a527fee27819b92f9f06c3393b567fa46` |
| M200 | 10 | `6561e28aa199fc1d463881f399f116bd3c05222d6d26e9f54992ff1b542f2045` |
| M202 | 10 | `33f34abf2f6d763b61fd15e6f64c895249792e70dab933894242584886491f70` |
| M240 | 9 | `2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3` |
| M242 | 7 | `49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663` |
| M269 | 9 | `c36c8fd777808d6664b30525dda2e5f562dd41d57e288d391bf6154d803606eb` |
| M271 | 7 | `ed22acab046adcc2af8960fd9690e1cb7e2bb20f5f337bb0fece53b64b7b1d73` |
| M273 | 9 | `4413c0f077009a07bced6addb014c76741a47059b2ba78b0cb7e8803e6f5c550` |
| M275 | 8 | `8f138666682868cb08a072d0be0ecc331eb1adb7e092f5bf4dcd6917db1932aa` |
| M278 | 8 | `352834e6752233b90b04f4c4205ff141208a3781ac458e7f2bf14c119c6014ad` |
| M281 | 10 | `8a775c75b63b897405a6fc29a455ba322eff7c6e70b13fca735b719ab0e89c8d` |
| M284 | 6 | `3176a4b175fd58f65ed2b71d81c5d2f1fc794cb9e7c7e2370ebcecaff19a62f3` |
| M288 | 8 | `fd4120e216b9140c4a8938724c3415393d6f5495a105f817cf681871545942ca` |

M13 predates this freeze format.  The observed proof-artifact hashes used
for provenance, not as a claim of prior immutability, are:

| M13 artifact | observed SHA-256 |
|---|---|
| `diameter_audit.md` | `536fd8acf9b263984736b0f7bc2f986e8aa27bde14bf4392b4c60efc60febb67` |
| `report.md` | `4cf19e45d9b0306b8e8744ae1cfc0935bba5ca7bbb64f62599f0e85dc7064324` |

## Semantic scope check

- **M112/M119:** accepted exact rooted DPS product and `d`-to-one root
  quotient imply `|Z_d|=d^(d-3)(2d-2)!`.  No physical gap comparison is
  imported.
- **M135/M137:** accepted free `G` and `H` actions, `d`-regular
  orbit-incidence multigraph, perfect matching colors, actual `H`-edge
  quantifier, and exact finite-action coset-intersection obligation.  The
  polynomial matching-coset refinement remains unresolved.
- **M175/M176 and M181/M183:** their voltage and chord conclusions require
  an actual synchronized quotient route.  They cannot supply the base
  schedule missing here.
- **M200/M202:** accepted only as exact rank-five width-two coverage.  No
  arbitrary-rank cover is imported.
- **M240/M242, M269/M271, M273/M275, M278/M281:** together form the accepted
  complete local old-padded/new-rank correction chain, including all edit
  boundaries.  They apply after a valid chart and common base route exist;
  they do not produce that common base route.
- **M284/M288:** accepted at literal word level, including the exact
  rank-lifted common-`c` intersection and the `V_D` chart-coverage
  obstruction.  Literal braid fibers remain distinct from finite
  action-image fibers, especially across ranks.  The true M135 refinement
  remains unresolved.

No predecessor or coordinator file was edited during this audit.
