# M316 dependency audit

Date: 2026-08-14 UTC

Frozen M313 has the assigned top digest and all 14 rows pass:

```text
M313  9b67c63e98361bd31e03919295c673d55235a6f7395730b477ca04a5e267f0b1  14
```

Every cited source package was measured independently at its stated top, and
every inventory row passes:

```text
M91   0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703  13
M276  882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db   9
M279  3910c66a134083117e8defce4bf6a3d57fdce3a48b519e7c8271c1864bf52f66   8
M297  a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792  12
M302  1009b8d3fbe40dc75aa9a10d3071d74a978ab6a97951a270e57a01916b9fdd27   7
M305  4e81c82223820cde35a8eecb7e8eb837733c5cd97ccb0375ae44d2a012392b46  11
M310  310e5708d48b5ad63d6ad4928be02c98de343d9e0cd91e363fe48eade047f276   8
```

The finite guard's imported M297 primitive script is also the exact
inventory-gated payload
`9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73`.
No source file was modified.
