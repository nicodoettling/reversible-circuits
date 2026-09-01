# M190 halfway checkpoint

Date: 2026-08-13 UTC.
Status: immutable gate passed; independent matrix and decisive boundary audit passed.

- Ownership remains restricted to M190; M185 was never edited.
- Before reading M185's conclusions, all seven payloads passed its complete
  `SHA256SUMS`; inventory matched the freeze manifest. Ledger digest:
  `9400d67948c99905bc1ce75081466d737247ed47af3fb42d7b7b5c2ae36b64b1`.
- All relevant accepted dependency ledgers M109/M114, M115/M116,
  M117/M121, M147/M151, M157/M160, M162/M165, M173/M177, and M179/M184
  passed.
- Clean-room derivation confirms suffix excess two forces exactly three
  Jacobi modes. Exact Bayes normalization leaves one likelihood under the
  child posterior; the parent subtraction is the rank-one matrix for
  `(delta,sqrt(v),0)`. All three off-diagonal entries remain, while killed
  `a=d` is omitted without survival conditioning.
- Exact independent rational arithmetic confirms
  `det((2/3)I-G_(20,0))=-1731224299/244943654967<0`.
- The universal `3/4` route passes independent algebraic audit so far:
  Vandermonde replacement is Loewner-monotone; the first leading minor is
  positive; the second is a concave quadratic in `x=(2a-d)^2` with both
  endpoints positive; and the determinant cubic has four Bernstein
  coefficient polynomials which become strictly coefficient-positive after
  `d=1+e`. The minimal `d=1,a=0` slack is separately positive. No material
  boundary defect has appeared.
- Independent history reconstruction reproduces
  `Sbar=R_2+D_0+(2/3)W_1` and the exact named obstruction
  `10249528643/7684875000>1` at `(B,d,a)=(3,20,19)`. This only refutes the
  envelope-cap-one route, not the exact child trace.
- Exterior rows independently give `eta=9/16` at `n=0`, `36/125` at
  `n=1` with `r=n` included, and the nominal `B=1` envelope remains an upper
  bound after inactive coordinates are removed.

## Final checkpoint

The clean symbolic beta-moment derivation regenerated every Sylvester minor
and all four Bernstein lists exactly. Final disposition is **ACCEPT**, with
no material objections. The only nonmaterial note is that M190 supplies the
symbolic regeneration absent from M185's compact row checker. Both exact
artifacts pass, and work stops at the strict reduction: no `S<=2`, complete
`h=3` sector, total AMV, gap, or terminal inference is made. The mission is
