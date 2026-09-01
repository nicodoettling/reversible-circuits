# M297 proof addendum: size-one convention

Date: 2026-08-14 UTC.

This addendum is controlling for the two boundary-case sentences in Sections
4--5 of `proof.md`.

- A size-one residual owner has no generic phase.  Hence every `H_1`,
  `C^off_(1,e)`, `C^off_(d,1)`, and `A_1` row is identically zero, regardless
  of the formal value assigned to `u_1`.
- For `d=2,3`, `Delta A_d` vanishes throughout the target range.  A size-two
  owner has at most one generic phase.  A one-run size-three owner has two
  consecutive generic phases, while a two-run size-three owner has at most
  one; their self-overlaps are supported only at circular lags `0,1,n-1`.
- Therefore the SOCL-to-SOCT summation uses `u_d=O(1/d)` only for `d>=2`,
  discards all `d=1` rows exactly, and discards the `d=2,3` self rows exactly.

No theorem statement, coefficient normalization, or verdict changes.

