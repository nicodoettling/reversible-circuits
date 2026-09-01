# M311 Halfway Checkpoint

Date: 2026-08-14 UTC
Status: analytic identity proved; QBP_1 frozen; no computation yet

The quantile support is exactly a monotone staircase.  Labeling a cell by
`h=min(c,d)` yields a canonical rung order; every off-diagonal rung direction
is forced by `sgn R_h`.  The mass endpoints
`M_h=max(A_h,B_h)` prove that maximal constant-sign runs of `R_h` cut the
staircase into disjoint contiguous blocks without slicing a cell.

This proves the unconditional block identity QBD_1.  The predeclared QBP_1
requires each complete sign-block sum to be nonnegative and is sufficient
for MCLP_1.  No cellwise sign, fixed-middle split, MON/FOSD, or PSD argument
is used.

The first unproved step is now standalone:

> Prove QBP_1 for every stated parameter, or refute it at the sole authorized
> exact rank `k=11` while retaining QBD_1.

No finite checker has yet been executed.
