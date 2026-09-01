# M158 halfway checkpoint

Date: 2026-08-13 UTC.

- All eight assigned M154 digests match exactly before review.
- Required skill/core sources and accepted M135/M137 and M141/M143 scopes
  have been read.
- The universal conjugation calculation is consistent with the stated right
  Hurwitz convention: the descending pass moves the final factor left, the
  ascending pass restores it, and product one gives conjugation by that
  factor. Transporting an original factor to the final slot and back costs
  at most `4m-4` moves per generator letter.
- The quotient criterion has the correct orientation: zero relative parity
  puts the unique transporter tuple in `P_(d,s)`, where the explicit inner
  braid removes it. The bound remains conditional on aligned-generator word
  length; generation alone gives no polynomial bound.
- A clean-room exact checker is next. It will close only the small physical
  `d=3` action, use bounded degree-`120` Schreier--Sims for the `d=4` block
  audit, and cap `d=5` at orbit enumeration plus primitivity.

Provisional decision: no material objection found in the proof audit; final
decision awaits independent exact reproduction.
