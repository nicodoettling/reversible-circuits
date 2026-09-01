# M339 immutable dependency audit

Date: 2026-08-14 UTC

M337's `SHA256SUMS` hashes to the required
`912ee2dd7379d5fde38a39429f7754aacd2741b41d234f8de30bb795da9030f7`.
Its exact 11-row inventory passes completely:

```text
86a7fc4b550b51acef42de8cde1b3b327ba0775b7e9ba7adf69f5b8c7b7cbf66  plan.md
48cdde01f5f638778e07e0f745c99460347608fecb71ff533eb071fc48209f62  checkpoint.md
506be32030e63435355ce697467a11b69985ab4675da4c8ea6b1ee12bf9793c7  source_lock.md
44ed7411b2f05237cf02878398138d55746d1c19a080762c42175dbf97ea23ff  candidate.md
ef9a87a951978dcbc1fe12e78be9695bb4ced7900bbafcc76bc4819244588633  pivot_averaging.md
d100a25dd332e91a6f1ad16f29e3df27f5e224acb1b5f8c003694da9bef84ff3  halfway_checkpoint.md
9af8fc575560d8f030d1031bb213cfc318831f778c2cdb6e247224d7a92e0cf6  report.md
f98d11eeb0518a4728bc7a50af6d903aca661d72f813040a12b3fabe214752fd  run_manifest.md
7885e6fa26920466a602d3029478cc0c4f1031659073b0c1c3b829942d6ac30b  audit_request.md
b9a63281d0b8e8cd889fbd17bd339af60361bdcdabe71090185bdce7fb4d70bd  final_checkpoint.md
44c75d103a8400795fdb2cae5bbeaf62ad77d489b1528acfacf9137c413382a7  freeze_manifest.md
```

The cited author/referee pairs independently reproduce:

| mission | rows | top SHA-256 |
|---|---:|---|
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
| M324 | 10 | `d42ba8d98c5d8c00501a01d458a1d6598bdfc8cce324344ae1e46b7081280aab` |
| M327 | 9 | `e2ab1d2f0af271687323b801953e25348a7cb5e187b3cc902644ed06ddc863c3` |
| M328 | 10 | `7f730f4344630522e1ee781d4651990c789f2e791a7846678eec5d8aa198725e` |
| M331 | 8 | `a549f57c3915920bd871c3315aa71fb06de1e7c6697d9b963a560d60980d9e92` |

All 123 payload rows pass. The corrected M296 top above is used; M317's
historical citation typo is not imported. No package was modified.
