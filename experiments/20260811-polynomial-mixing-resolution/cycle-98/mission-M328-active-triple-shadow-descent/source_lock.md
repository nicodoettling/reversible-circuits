# M328 source lock

Date: 2026-08-14 UTC

All stipulated frozen packages were checked before substantive proof inspection. The digest shown is the SHA-256 digest of that package's `SHA256SUMS`; every row in each manifest was then verified with `sha256sum -c SHA256SUMS` from the package directory.

| package | frozen directory | top digest | rows | result |
|---|---|---|---:|---|
| M135 | `cycle-30/mission-M135-conflict-coloring-realization` | `8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358` | 7 | pass |
| M137 | `cycle-31/mission-M137-m135-fresh-referee` | `47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5` | 6 | pass |
| M296 | `cycle-83/mission-M296-framed-stabilizer-intersection` | `9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f` | 7 | pass |
| M299 | `cycle-84/mission-M299-m296-fresh-referee` | `1654bcd6319b3020fe49a34e54a9961b2687ba5daab107baca11873749065b8d` | 5 | pass |
| M301 | `cycle-85/mission-M301-sstid-coset-helly` | `ae7ca4a3089259ac59df8e15ea3ff8d957c01956d842454f2dd1dcf3a881adcd` | 8 | pass |
| M304 | `cycle-87/mission-M304-m301-fresh-referee` | `5518f47facfab896ca1d32d4d3f9626a52c25e05cf970861395d4e19c2a0f4cf` | 10 | pass |
| M312 | `cycle-91/mission-M312-actual-wrad-transporter-signatures` | `e38d8eb38b8ee261cd399dc1bdfd654928b634a4cc41057bbf6bc2dcd727f745` | 10 | pass |
| M315 | `cycle-92/mission-M315-m312-fresh-referee` | `50264b377b4b4db21afa9e722a42fdf76bc3d9c5fbf659845afa63112e9c2ac9` | 8 | pass |
| M317 | `cycle-93/mission-M317-actual-phtc-partial-bijection` | `88a2480ec93ee6b3deb2d3e2e14b9a49a3f7e6ea71dca59997424c1356255245` | 10 | pass |
| M320 | `cycle-94/mission-M320-m317-fresh-referee` | `132b871023f5fbdb0970c55c616d060fce1c3db8f8ac93277bdf29fc9a2b2d4d` | 10 | pass |
| M324 | `cycle-96/mission-M324-heavy-pairwise-residual-node` | `d42ba8d98c5d8c00501a01d458a1d6598bdfc8cce324344ae1e46b7081280aab` | 10 | pass |
| M327 | `cycle-97/mission-M327-m324-fresh-referee` | `e2ab1d2f0af271687323b801953e25348a7cb5e187b3cc902644ed06ddc863c3` | 9 | pass |

Total verified payload rows: **100/100**. M296's actual top digest is the value above; no stale typo is imported.

These locks establish provenance only. They do not promote any unresolved AATSD, HPRN, APOH, WRAD, literal-length, spectral-gap, mixing, or Terminal claim.
