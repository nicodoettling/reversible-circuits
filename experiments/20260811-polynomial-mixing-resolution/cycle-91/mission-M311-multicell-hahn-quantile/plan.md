# M311 Plan: Multi-cell Hahn--Quantile Cancellation

Date: 2026-08-14 UTC
Role: author

## Objective and target

Starting only from accepted M307/M308 QTI_1, derive the canonical monotone
support path of the quantile transport and partition every supported cell
into maximal blocks determined by cumulative-mass/Abel sign changes.  Freeze
one explicit block- or prefix-compensation inequality `QBP_1` which is
sufficient for

```text
P_(k,ell)(u)>=0
```

before any computation.  The target is only the auxiliary channel-one
all-middle coefficient statement MCLP_1 for odd `k>=3`, `n=3k`,
`1<=u<k/2`, and `2<=ell<=n-2`.  Every `Xbar_c,Ybar_d` must retain all `k`
middle phases.

## Source locks

- M307 frozen checksum top:
  `41d6096e07da79c374a06947a882820a3e470aa9fb6415217909cb4404bf765e`.
- M308 frozen checksum top will be measured from its owned package before
  importing its verdict.
- Only the QTI_1 identity, exact quantile marginals, mixed-`R` support
  orientation, and finite `k=9` obstruction/survival facts may be imported.

## Work order

1. Verify M307/M308 immutable inventories and inspect only their relevant
   proof/audit passages.
2. Derive the staircase support path and an exact cell-prefix/telescoping
   identity, including endpoints and zero cumulative differences.
3. Define maximal sign-change blocks without dropping or duplicating any
   transport cell.
4. Write and freeze one explicit `QBP_1` sufficient inequality in a separate
   precomputation artifact.
5. Attempt an all-rank proof analytically.  Only if it remains unresolved,
   run at most one standard-library exact falsifier at the sole new rank
   `k=11`.
6. Freeze either the proof or the first exact counterexample together with
   the strongest surviving identity, then request fresh immutable audit.

## Forbidden shortcuts

Do not split fixed middle phases, discard cells, assume cellwise QCP signs,
invoke MON/FOSD/PSD, or search alternate weaker candidates after seeing
finite output.  Do not infer GOCI or any downstream OCI/CP/MS/FCL1, gap,
mixing, or Terminal conclusion.  MCLP_1 itself remains unresolved unless an
all-rank proof is completed.

## Expected failure modes

- A proposed block definition fails to partition the staircase support at a
  shared endpoint or at `R_c=0`.
- The compensation inequality is merely a restatement of total positivity
  and gives no local signable structure.
- The `k=11` guard refutes `QBP_1` although the full aggregate remains
  positive, reproducing the cancellation obstruction at a coarser scale.
- A finite positive result is accidentally promoted to an all-rank theorem.
