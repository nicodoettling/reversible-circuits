# M298 halfway checkpoint

Status: initialized before inspecting frozen M295.

The audit plan is fixed.  No M295 file has yet been opened, searched, hashed, or interpreted.  The next actions are source-of-truth review followed by integrity and inventory verification, after which the mathematical reconstruction will proceed independently.

## Halfway update after the immutable gate

The frozen package has now passed the immutable gate:

```text
M295 SHA256SUMS digest
42fa1c38b08359ae949fa0076557c2d42fdda232d1e7b318432e6787795ca3e5
```

All ten files named by the authoritative inventory pass `sha256sum -c`, and
the directory contains exactly those ten payload files plus `SHA256SUMS`.
The eight cited M266/M268, M274/M277, M280/M283, and M285/M287 inventories
also pass byte-for-byte and agree with ledger entries L-0302, L-0306,
L-0309, and L-0311.

The clean-room exact-rational reconstruction is complete.  It imports and
reads no M295 artifact and obtains:

```text
cells checked                         120
negative FMCP_1 cells                  16
minimum middle chord                  (6,9)
minimum reflected lags                6 and 9
all fully weighted eta_1 lags         strictly positive
direct = repaired = composition       all admissible states/lags
```

The minimum is exactly

```text
-779985545058827083283361063988362608513
/11367752922135489592720891699200000000000.
```

The positive-composition enumeration independently gives multiplicities
three for triangles and four for the combined separated/nested doubles.
The anchor is already a support vertex, so there is no factor `n`.
Independent completion-count normalization gives channel-two mass one on
both sources, with split first-component masses `1/2,1/2`; adding another
`1/2` would be wrong.

Post-hoc comparison, performed only after generating the independent raw
output, matches all 120 frozen M295 cells, all twelve `eta_1` lag totals,
all twelve weighted `alpha_1 CP_1` values, and every scalar prefactor.
The likely verdict is ACCEPT with no material objection and one nonmaterial
scope qualifier concerning the shorthand scalar `beta_1(ef)` notation.
