# M336 immutable dependency audit

Date: 2026-08-14 UTC

M335's `SHA256SUMS` hashes to the required
`a819a4ef99f8160219d881e5fe9c5e96448e3aa9f2f2ab3c1fe2ed461bf7df74`.
Its inventory has exactly 14 rows and all 14 pass `sha256sum -c`.

The independently reproduced frontier locks are:

| mission | rows | top SHA-256 |
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
| M333 | 8 | `2adcfc35a9e2296b0ba6fd9129d5b8fd1f2e4d8e4b4e77d1ea064251ed855c3b` |

Every well-formed frontier row passes. M326 retains its known 63-hex row 8;
M329 independently records the correct 64-hex `run_manifest.md` hash, so
this is provenance only and M326's mathematical REJECT remains unchanged.

The raw-law packages M91/M261/M264/M267/M270/M276/M279/M282/M286/M289/
M290/M292/M293/M297/M302 reproduce respectively:

```text
0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703
b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b
b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f
001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6
6c0c6e13c62885a0c56e8c232c0f2ddc48922be56b3edce97a4f9c9b9ca5491e
882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db
3910c66a134083117e8defce4bf6a3d57fdce3a48b519e7c8271c1864bf52f66
cac6e77151401e708acb5a812097ccce44ed1dce45acefada9a3c13ebcfe5ed7
3778a3884212e4b5403df1d37a1145a2810b77f94b55e84dd84aac1dec6c0f0a
327176968d69eb447ff862354eb566ed00cfd2c56b2e77079231bcc077f93680
85373b13ab4799f59d98dd20bf5b0496fa61d119b45b0ffe34900094564df687
8fefffab69cca864c9260429e9eef34671aab23a497e36fb05cb6b89c378740f
b7020fb3ee6cfc9b2536b500928320ff4ce0bc8fc0983c65989ff092d9ac3f1f
a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792
1009b8d3fbe40dc75aa9a10d3071d74a978ab6a97951a270e57a01916b9fdd27
```

All 136 raw-law rows pass. The directly loaded M297 primitive hashes to
`9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73`.

One isolated replay of the frozen `k=9,H_2` guard exited zero. Its result
and M335's frozen JSON both hash to
`b4374e23d9d6ebb40dd03125727a1da112d0b09837701241bc8061511ef9077f`;
`diff -u` is empty. No other cell, row, rank, or surgery was evaluated.
