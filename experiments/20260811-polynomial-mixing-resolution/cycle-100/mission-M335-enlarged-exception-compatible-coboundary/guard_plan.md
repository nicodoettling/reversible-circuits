# M335 sole exact guard plan

Date: 2026-08-14 UTC

Status: predeclared after `Exc_pf^*`, the exact flux split, the source-switch
map, landing conditions `(4.1)`, weight ratio `(4.2)`, and scalar reduction
`(5.1)--(5.4)` were frozen in `candidate_formula.md`.

## Fixed universe

Run exactly one deterministic guard:

```text
k=9, n=27, row H_2 only.
```

Use the frozen common-quantile cells and fully combined raw marked endpoint
laws with both live channels and all literal slots, including zero slots.
Enumerate cells and raw token labels in frozen lexicographic order. Filter
only by the already-frozen `Exc_pf^*`.

## Ordered yes/no test

For each compatible token, apply the fixed product/prefix-preserving source
switch and stop at the first failure of:

1. supported reverse quantile cell `pi_(s',t')>0`;
2. reverse residual signs `a_(s',t')(Q)>0`, `b_(s',t')(P)>0`;
3. exact weight ratio `(4.2)=1`;
4. literal return under the second switch.

If a failure occurs, record the first exact atom/cell, all rational weights,
exception predicates, derived splits, and the strongest preceding identities.
If none occurs, record finite-only survival; do not infer an all-rank theorem.

## Firewall

No other rank, row, cell family, surgery, pairing, grouping, or search is
authorized. The guard may not estimate the exceptional scalar bound, MPCF,
or any downstream statement.

