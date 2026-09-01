# M103 plan: global two-layer reset defect

Date: 2026-08-12.

## Objective and exact scope

For the auxiliary full nonlazy stationary-flow parking-degree projection in
the minimal long-cycle sector, test the proposed sufficient condition

```text
(I+Q)r_U(x)>=0
```

on every reachable active context `x=(s,K,R,B)`, retaining every live
attachment rank `j=1,...,k`.  Here `r_U=U-A-QU` is the frozen M90 transformed
weighted defect.  This mission concerns neither the original lazy
`{3,4,5}` identity-word heat-bath kernel nor a spectral gap.

Permutations compose as `(pq)(x)=p(q(x))`; factors are displayed
left-to-right.

## Work plan

1. Independently reconstruct M90/M98 formulas and derive the right-heavy
   `K->infinity` two-layer limit.
2. Search that exact limiting family for a sign obstruction, emphasizing
   growing `s` and fresh/right-heavy boundaries.
3. Implement an all-rank exact finite countersearch over the reachable
   closure and, if a negative family appears, seek a rational infinite-tail
   certificate by denominator clearing/Newton coefficients.
4. Check whether any local obstruction also violates the complete weighted
   or stronger unweighted resolvent; do not infer this from a local sign.
5. Freeze proof/obstruction, raw JSON, nine-field report, hashes, cache and
   repository-status records.

## Expected failure modes

- A `j=k`-only finite recurrence would be invalid; it is permitted only in a
  proved right-heavy `K->infinity` limit.
- Finite positive scans do not establish the universal inequality.
- `q(1-q)` is an algebraic budget, not a Bernoulli-variable license.
- A negative local block need not be a resolvent failure or slow mode.

