# M96 plan: fresh referee of frozen M90

Date: 2026-08-12. Repository base commit recorded by M90:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and frozen source

Independently referee the frozen M90 weighted-reset-resolvent bundle. The
required source digests are:

```text
report.md     36230c7e509eff638eb5888b2e61703957dcc32f2f06fae582739d7f1414d458
SHA256SUMS    3d63f177659abae99b6c3a4247aee67b6dfc087cd1270df40e806f5a9f99b5b8
```

The audit concerns only the full nonlazy stationary-flow parking-degree
projection `Pbar_r` in the minimal long-cycle sector. It must not promote a
gap for `Pbar_r` or for the original lazy `{3,4,5}` heat-bath chain.

## Checks

1. Re-derive the all-attachment-rank transformed recurrences and strict
   descent, including direct-composition versus grouped reset energy.
2. Check the finite-DAG defect identity and the proposed fresh/nonfresh
   sufficient conditions, including exact reachability closure.
3. Reproduce the smallest decisive exact counterexamples to variance,
   Bessel, local-budget, and scalar-interpolant routes.
4. Check the stronger unweighted recurrence and its implication to the
   weighted target without assuming a Bernoulli representation.
5. Reproduce predecessor calibration values and inspect every executable and
   retained JSON for exclusion of the stale `j=k`-only discovery recurrence.
6. Audit the conditional occupation conclusion and retain its auxiliary-only
   scope.

## Independent method

Use a new standard-library `fractions.Fraction` implementation based on
literal ordered compositions and literal canonical-basin sums. It imports no
M90 or predecessor module. Compare this implementation against selected
frozen exact numerators and separately verify the grouped Cayley identities.
All runs are deterministic with seed `null`, and Python is invoked with `-B`.

## Verdict rule

Issue `ACCEPT` only if every proved identity, exact witness, finite range, and
conditional implication is correct and precisely scoped. Any substantive
normalization, quantifier, or scope error produces a numbered objection and
`REJECT`. Finite survival never proves an open inequality.
