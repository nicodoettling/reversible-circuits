# M321 Dependency Audit

Date: 2026-08-14 UTC.

## Parent gate

M319's `SHA256SUMS` has the required digest

```text
10f3435003684d4a32570028c314882bbfa28daf0ddc4b8a12d6ba02319ea009
```

and exactly eleven rows. Every row passes.

## Source ledgers

All nine inventories cited by M319 reproduce their recorded top digests and
pass every payload:

```text
M91   13  0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703
M276   9  882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db
M279   8  3910c66a134083117e8defce4bf6a3d57fdce3a48b519e7c8271c1864bf52f66
M297  12  a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792
M302   7  1009b8d3fbe40dc75aa9a10d3071d74a978ab6a97951a270e57a01916b9fdd27
M305  11  4e81c82223820cde35a8eecb7e8eb837733c5cd97ccb0375ae44d2a012392b46
M310   8  310e5708d48b5ad63d6ad4928be02c98de343d9e0cd91e363fe48eade047f276
M313  14  9b67c63e98361bd31e03919295c673d55235a6f7395730b477ca04a5e267f0b1
M316  10  1b6caa11e6bb7409e7420d75cd2131f5753707b80736bed1bd9b5fe3f4dbc149
```

Total: 92 predecessor payload rows, all passing. In particular, the four
direct ledgers M305/M310/M313/M316 pass all 43 rows.

The imported scope is limited to the complete marked Abel identity, fixed
zero-slot masses, corrected `c_X`, the combined common-part/residual-product
coupling, and accepted reduction boundaries. MPCF and every downstream
estimate remain unresolved.
