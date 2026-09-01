# M201 plan: fresh reset plus `h>=4` AMV budget

Date: 2026-08-13 UTC.

## Objective

Resolve or strictly narrow the remaining fresh-parent AMV budget after the
accepted actual-history descendant bounds at heights one through three.
Derive the exact compatible slack, then treat the parent's reset term and the
aggregated `h>=4` descendants while preserving the full vector/Jacobi history,
all likelihood-weighted cross terms, and every killed observation.

Seek one of:

1. a precise amortized reset-plus-tail lemma closing the fresh-parent budget;
2. an exact obstruction to the proposed compatible budget; or
3. a strict reduction isolating the first standalone tail inequality.

## Immutable gate and accepted inputs

- Own only `cycle-48/mission-M201-fresh-reset-plus-hge4-budget/`.
- Never edit M173/M177, M179/M184, M193/M197, or their dependencies.
- Verify their complete frozen ledgers and inventories before conclusions.
- Accepted sector inputs, to be used with their actual parameter dependence:

```text
h=1 <=(1-q0)/4,
h=2 <=1/4,
h=3 <=27/125 for its n>=1 branch and <3/8 at its separate n=0 boundary.
```

Do not sum incompatible worst-case constants across mutually exclusive
exterior/boundary regimes.

## Exact target

At a fresh right-heavy parent `xi=(B+L,2,1,B)`, derive from the exact AMV
recursion:

- the reset contribution with its true `B,L,q0` normalization;
- which `h=1,2,3` boundary values can coexist for a fixed `L`;
- the resulting pointwise budget slack;
- the exact exterior and observation multiplicities for every `h>=4` group.

Then seek an amortized vector/history tail estimate. Keep the killed `a=d`
before direct-sum aggregation and never replace the child feature by a scalar
or finite summary that loses Jacobi cross terms.

## Prohibited routes and conclusions

- No enumeration by `L` or broad state scan; only named compact diagnostics.
- No addition of incompatible sector suprema.
- No scalar-`T1`, diagonal, Jensen, finite-summary, or generic-operator
  shortcut for `h>=4`.
- No all-state, all-`L`, gap, original-chain mixing, or terminal conclusion
  unless actually proved from the full remaining budget.

## Deliverables

Substantive halfway checkpoint, exact budget derivation, compact reproducible
diagnostics where needed, theorem/obstruction/strict reduction, nine-field
report, freeze manifest and hashes, hygiene record, and fresh-audit request.
