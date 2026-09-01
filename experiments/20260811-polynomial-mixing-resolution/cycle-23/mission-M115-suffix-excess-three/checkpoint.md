# M115 halfway checkpoint

Status: a closed all-`j` `L=3` envelope has been derived and its scalar sign
has an exact universal Bernstein certificate; the proof write-up and final
self-audit remain in progress.

- Scope is only the auxiliary full nonlazy minimal-long-cycle parking reset
  excursion.  No gap, original-chain mixing, or project-terminal conclusion
  is claimed.
- For `B=s-3`, exactly eight root compositions have nonzero contextual mean.
  They occupy seven exceptional canonical basins.  Exactly four root groups
  can send live deep mass: `(2,s-2)`, `(3,s-2)`, `(2,s-1)`, and `(1,s)`;
  the first two are inactive at `s=4`.  Every `j=1,...,k` is retained.
- The first two groups land at `L=0`; the unary group lands at a right-heavy
  `L=2` context.  The group `(2,s-1)` has both a right-heavy and a
  non-right-heavy `L=1` child.  A direct general-attachment `L=1` basin bound
  handles both without extending M109's theorem beyond its stated scope.
- Exact exceptional currents plus `beta_e<=degree(e)` on all ordinary basins
  give a closed rational envelope `H/q<=E_s(z)`, `z=1/(K+1)`.
- The positive clearing
  `1728(1+z)^2(1+2z)^2[1-q-E_s(z)]` has degree at most six in `z`.
  Exact degree-six Bernstein coefficients are positive for every
  `s=4,...,20`.
- For `s>=21`, the four consecutive Cayley ratios lie in `[1/3,2/5]`.
  Replacing the two path-height parameters by one only enlarges the envelope.
  The resulting cleared slack has multidegree `(2,2,2,2,6)` in
  `(r,u,v,y,z)`; all 567 exact tensor-Bernstein coefficients on
  `[1/3,2/5]^4 x [0,1/2]` are positive.  The minimum is
  `682328/28125` at tensor index `(2,2,2,0,0)`.
- `l3_exact.py` is standalone standard-library `Fraction` code.  Its current
  run has zero failures, 68 bounded full-resolvent rows, 17 finite
  certificates, and the complete 567-coefficient box certificate.

The strongest remaining self-check is the seven exceptional-current
normalizations and the aggregation of the two non-right-heavy child ranks;
these will be displayed explicitly in the proof note and retested directly.
