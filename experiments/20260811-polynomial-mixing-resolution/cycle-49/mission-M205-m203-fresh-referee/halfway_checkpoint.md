# M205 halfway checkpoint

## Immutable gate

- `sha256sum -c SHA256SUMS`: all twelve frozen M203 payloads `OK`.
- Inventory digest:
  `584d5110354693e3d5979fc6c1e83193e24754fcba4f51f035c9415cba3816e6`.
- The gate passed before substantive comparison.

## Clean-room replay

- A fresh implementation, importing no M203 code, reconstructed 10 rooted
  descriptors at d=5 and 12 at d=6, then all 178 named root/edit rows.
- Complete normalized row-table digest:
  `3144898428d5ec658c5fcda682c445b79c92123703bb53b700af237a741fb3ac`.
  It equals the digest computed from frozen M203 JSON, with no row mismatch.
- Reproduced counts: 110 adjacent-factor failures; 106 literal six-factor
  region failures, split 43 at d=5 and 63 at d=6; d=6 directed
  cross-coupling counts 29 active-to-filler and 22 filler-to-active.
- The distinguished d=6 pattern-0/root-5/edit-1 descriptor is found after 37
  trials and changes positions `[2,5,6,9]`, including filler position 9.
- Fourteen exact quotient-representative comparisons give 5 equal and 9
  unequal classes. Their normalized digest is
  `90a3781b721fd01ad22ce0c77dd2e30df6a32957c61e74fac8356589494ab857`,
  again identical to frozen M203.
- First unequal pair: naive
  `bd651af9408f609196bcf37c3b6bfec37a7c126bd7b1ff2cfc11c7492e8d324f`
  versus actual
  `bed555f8c63642f18b33d3c0f2d6175fd96ff5afa467e8def150a7c44f5ee35b`.

## Scope checkpoint

The evidence refutes only the naive independent-d5-block plus fixed-filler
proof premise. It proves no d=6 target unreachable and settles no all-d route
theorem.

