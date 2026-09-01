# M318 plan: full-aggregate Hahn/quantile compensation

Date: 2026-08-14 UTC.

## Target and exact scope

The ambient target remains the uniform fixed-length identity bridge for the
lazy exact same-product `{3,4,5}` heat-bath chain.  This mission addresses
only the accepted all-middle Hahn--Abel coefficient frontier leading to
`MCLP_1`.  It works at the complete aggregate `P_(k,l)(u)` with every middle
phase retained.

Accepted predecessor results already refute cellwise positivity and maximal
sign-block positivity.  Neither may be reintroduced, and no fixed-middle
sign, MON/FOSD, PSD, one-direction Abel monotonicity, or finite-trend
argument is authorized.

## Candidate fixed before computation: GQAC_1

Use the accepted QBD expansion to regard every full aggregate as a finite
signed collection of staircase rungs.  Write `R^+_(k,l)` and `R^-_(k,l)`
for the positive and negative rungs after retaining their middle phase,
cell, sign block, Hahn coefficient, and Abel kernel.  For a positive rung
`p` and negative rung `n`, let

```text
C_(p,n)(u)
```

denote their exact coefficient-weighted two-rung exchange contribution, not
an order comparison.

The predeclared **GLOBAL QUANTILE ABEL COMPENSATION lemma `GQAC_1`** is:

> For every admissible odd `k`, every `l`, and every allowed `u`, there is a
> nonnegative rational exchange matrix `pi_(p,n)`, allowed to pair rungs
> across different middle phases and different Abel sign blocks, such that
> 
> 1. every negative rung is used with exact unit demand;
> 2. every positive rung is used with capacity at most one;
> 3. the complete paired exchange has an exact global coboundary form
>    ```text
>    sum_(p,n) pi_(p,n) C_(p,n)(u)
>      =sum_t (J_(t+1)(u)-J_t(u)),
>    ```
>    with the accepted endpoint terms retained, and the boundary-plus-
>    staircase total is nonnegative;
> 4. every unused positive remainder contributes nonnegatively.

Equivalently, `GQAC_1` requires an exact full-aggregate compensation flow in
which the algebraic paired coboundaries, not the individual cells or blocks,
have nonnegative total.  It is a finite coefficient lemma at each symbolic
`(k,l,u)` and is sufficient for `P_(k,l)(u)>=0`, hence for `MCLP_1` once the
accepted reduction is verified.  No claim that `GQAC_1` holds is made in the
plan.

## Work plan

1. Source-lock M274/M277, M280/M283, M285/M287, M295/M298, M300/M303,
   M307/M308, and M311/M314 before importing notation or claims.
2. Reconstruct the full QBD staircase/rung/sign-block identity and QBP
   sufficiency with all middle phases.
3. Derive an exact global staircase-exchange/coboundary identity before any
   computation.
4. Express `GQAC_1` in the frozen notation and prove it, or isolate its first
   exact obstruction and the strongest surviving identity.
5. Only after the analytic derivation, run at most one exact `k=13` guard.
   Do not search for replacement groupings or any other rank.
6. Freeze reproducible artifacts and request a genuinely fresh audit.

## Expected failure modes

- Dropping a middle phase or endpoint/reflection term.
- Reusing a cellwise or maximal-block positivity claim already refuted.
- Turning a signed exchange identity into a MON/FOSD, PSD, or Abel-kernel
  monotonicity assertion.
- Inferring an all-rank theorem from `k=13`.
- Changing the rung grouping after seeing a finite failure.

## Firewall

Absent a complete proof and fresh audit, infer no MCLP, GOCI, OCI, CP, MS,
FCL1, spectral gap, mixing theorem, or Terminal conclusion.

