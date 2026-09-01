# M311 Report: Abel Sign Blocks Still Require Global Cancellation

Date: 2026-08-14 UTC

## Verdict

```text
KEEP QBD_1 AS AN EXACT ALL-RANK STAIRCASE/BLOCK IDENTITY.
REJECT THE PREDECLARED QBP_1 BLOCKWISE SIGN INEQUALITY.
MCLP_1 REMAINS UNRESOLVED.
```

## Proved analytic result

The canonical quantile support is a coordinatewise monotone staircase.  A
supported cell's rung `h=min(c,d)` is nondecreasing along the path, and every
off-diagonal rung direction is fixed by `sgn R_h`.  With

```text
M_h=max(A_h,B_h),
```

the cells having `a<=min(c,d)<=b` occupy exactly the mass interval
`(M_(a-1),M_b]`.  Therefore maximal constant-sign runs of `R_h` give a
canonical disjoint partition of every supported cell, including zero runs,
and

```text
P_(k,ell)(u)=sum_q C_q(k,u,ell).                    (QBD_1)
```

This holds for all odd `k>=3`, `1<=u<k/2`, and `2<=ell<=3k-2`, with all
middle phases retained.

## Refuted candidate

QBP_1 required each complete sign-block sum `C_q` to be nonnegative.  The
sole authorized standard-library exact guard at `k=11` refutes it first at

```text
(u,ell,block)=(1,2,1),  h=5,...,9,  sgn R_h=+1,
C_1 approximately -0.03599141613051397.
```

The full exact fraction and all ten cell contributions are stored in
`obstruction.md` and `qbp_k11.json`.  The result is not marginal: 154 of 450
block instances are negative, across 118 of 150 rows.

## Finite survival and exact stop

All 150 full aggregates at `k=11` are exactly positive, with reflected
minimum approximately `0.09958803705967692` at `(2,10),(2,23)`.  Hence
QBP_1 fails because cancellation crosses the canonical Abel sign-change
boundary; the guard does not refute MCLP_1.

No replacement block, prefix, cellwise, fixed-middle, MON/FOSD, or PSD
candidate was searched.  No second rank was run.

## Claim ledger

| Claim | Status | Evidence | Action |
|---|---|---|---|
| M307/M308 source locks | verified | top and per-file hashes | retain |
| canonical monotone support path | proved | cumulative endpoint partition | retain as QBD_1 input |
| rung orientation from `R_h` | proved | strict overlap inequalities | retain |
| maximal sign-block partition | proved | exact interval `(M_(a-1),M_b]` | retain |
| QBD_1 | proved | disjoint complete cell partition | promote for fresh audit |
| QBP_1 | refuted | first exact `k=11` block | do not reuse |
| 154/450 negative blocks | exact finite only | `qbp_k11.json` | cancellation obstruction |
| 150/150 positive aggregates | exact finite only | same artifact | do not extrapolate |
| MCLP_1 | unresolved | QBP_1 false | keep open |
| GOCI and downstream claims | unresolved/out of scope | no inference | keep open |

This auxiliary coefficient mission makes no claim about the global identity
bridge or the lazy exact same-product `{3,4,5}` heat-bath chain.  It implies
no OCI, CP, MS, FCL1, gap, mixing, or Terminal conclusion.
