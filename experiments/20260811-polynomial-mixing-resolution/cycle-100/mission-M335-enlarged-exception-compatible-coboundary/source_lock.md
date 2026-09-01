# M335 immutable source lock

Date: 2026-08-14 UTC

All named frontier packages and the exact raw-law chain cited by M323 were
authenticated before substantive proof inspection.

## Frontier packages

| mission | rows | reproduced top `SHA256SUMS` digest |
|---|---:|---|
| M305 | 11 | `4e81c82223820cde35a8eecb7e8eb837733c5cd97ccb0375ae44d2a012392b46` |
| M310 | 8 | `310e5708d48b5ad63d6ad4928be02c98de343d9e0cd91e363fe48eade047f276` |
| M313 | 14 | `9b67c63e98361bd31e03919295c673d55235a6f7395730b477ca04a5e267f0b1` |
| M316 | 10 | `1b6caa11e6bb7409e7420d75cd2131f5753707b80736bed1bd9b5fe3f4dbc149` |
| M319 | 11 | `10f3435003684d4a32570028c314882bbfa28daf0ddc4b8a12d6ba02319ea009` |
| M321 | 8 | `50d153ff89699d893bd44df6fdc346eec66fd001f843c28ff4d84a19cdfcb960` |
| M323 | 15 | `0aa6cfccd9d5feaf16ded0c4c5b5bf42d552c1f36ff4f4ce58998c927cbac39c` |
| M326 | 10 | `a1ea699e4086cb967875c9408f586afc0854c85096a278e32eed9697b5ba2a2a` |
| M329 | 7 | `6f3c67dadba4475b70f3372f4b61be575f917f463dd3c62db1afc14813aa11df` |
| M330 | 12 | `623ec4026179c81cc2a1ec49ce3318af470562924d7a34ac5bc6a6ba76547f93` |

All 96 well-formed frontier-manifest rows pass directly. M326's ten payloads
were independently rehashed against M329's corrected 64-character
`run_manifest.md` row, so all 106 frontier payloads are authenticated. M326
itself remains frozen and unedited.

## Raw-law chain

| mission | rows | reproduced top `SHA256SUMS` digest |
|---|---:|---|
| M91 | 13 | `0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703` |
| M261 | 9 | `b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b` |
| M264 | 6 | `b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f` |
| M267 | 8 | `001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6` |
| M270 | 9 | `6c0c6e13c62885a0c56e8c232c0f2ddc48922be56b3edce97a4f9c9b9ca5491e` |
| M276 | 9 | `882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db` |
| M279 | 8 | `3910c66a134083117e8defce4bf6a3d57fdce3a48b519e7c8271c1864bf52f66` |
| M282 | 9 | `cac6e77151401e708acb5a812097ccce44ed1dce45acefada9a3c13ebcfe5ed7` |
| M286 | 8 | `3778a3884212e4b5403df1d37a1145a2810b77f94b55e84dd84aac1dec6c0f0a` |
| M289 | 9 | `327176968d69eb447ff862354eb566ed00cfd2c56b2e77079231bcc077f93680` |
| M290 | 10 | `85373b13ab4799f59d98dd20bf5b0496fa61d119b45b0ffe34900094564df687` |
| M292 | 9 | `8fefffab69cca864c9260429e9eef34671aab23a497e36fb05cb6b89c378740f` |
| M293 | 10 | `b7020fb3ee6cfc9b2536b500928320ff4ce0bc8fc0983c65989ff092d9ac3f1f` |
| M297 | 12 | `a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792` |
| M302 | 7 | `1009b8d3fbe40dc75aa9a10d3071d74a978ab6a97951a270e57a01916b9fdd27` |

Every one of the 136 raw-law payload rows passes. In particular the M297
permutation/completion primitive is locked at
`9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73`.

## Imported boundary

Only frozen exact raw laws, combined token normalization, signed flux
identities, source-local exception predicates, and audited negative findings
may be imported. No predecessor claim of MPCF, compatible coboundary,
exceptional Borel control, or downstream mixing is assumed.

