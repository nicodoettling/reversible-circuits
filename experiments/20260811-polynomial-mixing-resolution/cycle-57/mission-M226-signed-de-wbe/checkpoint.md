# M226 checkpoint

## Start

- Mission initialized before substantive work.
- Target is exactly WBE for both `X_ell` and `Y_ell` on the full stated range.
- Predecessors are immutable; M226 owns only this directory.
- First actions: complete source/checksum gates, then derive coefficient-level signed cancellation before any diagnostics.

## Immutable gate

- Every checksum entry in M192/M195, M199/M207, M211/M215, and M217/M222 passed.
- Their checksum-file digests are respectively
  `4c6cd295...36c60`, `1f0c398b...3f0a`, `1de555bb...1c25ed`,
  `817988cd...1979d`, `79f3e0f6...74225`, `59b4bade...938928`,
  `7772f6ec...5557`, and `d2a43d90...e7ccd`.
- No predecessor was edited.

## Halfway and cap

- Derived exact coefficient-level cancellation for Y, including closed
  `G_k(x)`, `B^Y_{k,y}`, and `A^Y_{k,y}` formulas.
- Derived the exact signed two-run identity for X minus Y.
- Compact exact checks validate the Y identities for odd `k<=15` and the
  literal X/Y identities for `k=3,5,7`. Mixed coefficient signs refute a
  simple one-sign route.
- An unsigned placement-count shortcut is exactly false at `k=5`.
- Cap verdict: strict reduction to YCM and TCM. WBE and DE remain open.
