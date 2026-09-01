# M193 fresh immutable audit request

Audit frozen M193 independently and do not edit it.

1. Verify the complete `SHA256SUMS` inventory before conclusions.
2. Re-derive why the retained set `a=0,...,d-1` has `d` terms, why
   `pi_a=1/(d+1)` is internal to `G_(d,a)`, and why no survival factor occurs.
3. Check the exact beta-moment average (3.2)--(3.4) in
   `coupled_trace_theorem.md` against the accepted M185/M190 history.
4. Audit the `B>=2` Cayley bounds, `b` monotonicity, unconstrained `q`
   maximization, decreasing `y` certificate, and shifted slack polynomial.
5. Audit `B=1` by inactive-coordinate deletion and exact nominal formula.
6. Verify `sum_a B_(d,a)<3d/4`, the exact exterior with `r=n`, and the
   `36/125` maximum without adding or deleting a factor of `d`, `d+1`, or
   `pi_a`.
7. Recheck `n=0` from the exact `d=1` matrix and one-history envelope, and
   confirm that `3/8` is a loose separate boundary bound.

Return ACCEPT/REJECT with numbered objections. Strict scope: no reset,
`h>=4`, total AMV, all-`L`, gap, original-chain, or terminal inference; no
`L=7` enumeration.
