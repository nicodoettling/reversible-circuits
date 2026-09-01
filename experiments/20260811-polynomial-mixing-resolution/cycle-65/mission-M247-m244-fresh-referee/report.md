# M247 final report: fresh referee of frozen M244

Date: 2026-08-14 UTC. Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Verdict

```text
ACCEPT M244 THEOREM 3.1: CANONICAL UNEDITED ONE-OPEN COLORED STACK PRUNING.
REJECT M244'S FROZEN RSMI AND ITS CLAIMED FULL RSMI-TO-IDL PACKAGE.
DO NOT ACCEPT IDL OR UNCONDITIONAL ALL-RANK Z2 CLOSURE.
```

All frozen M244 payloads and the M240/M242 dependencies pass SHA verification.
The DPS primary PDF hash also matches.  Independent reconstruction confirms
the canonical formula `L_a=2a-3`, `R_a=L_a+1`, the literal bridge-contour
factorization, the bottom-up deletion of complete internal LIFO nodes, the
single survivor `W^{R_a}`, the one-open/virtually-balanced correction, and
the exclusion of reversed edited `x_v`.

## Material objections

1. **RSMI(2) is refuted as written.**  At `d=7`, `v=4`, with
   `T={{1,7},{1,3},{1,6},{2,3},{2,4},{4,5}}`, the stopped path
   `(4,2,3,1)` is closed by an ascent while 5 is a larger direct child of 4.
   Exact clean-room DPS closure gives `N=A` and common slot
   `I_5=((2,4),(2,4))`.  Unqualified RSMI(2) predicts old/new root endpoints
   `((4,6),(4,6))` versus `((4,7),(4,7))`.
2. **IDL-a is missing.**  No RSMI clause identifies the old/new second black
   endpoint of the edited factor at position `2v-2`.
3. **IDL-c is missing.**  Rank-to-rank endpoint stability does not identify
   the common endpoint as `x_{p(r)}` and hence does not give `h_r^2` or the
   required disjointness.
4. **The closed case is missing.**  “Absorbs” has no factor-level transition
   or sealed-root equality clause, so it does not prove `N=A` and conflicts
   with the literal unqualified larger-child rule.

A repaired `RSMI+` must restrict the larger-child root-endpoint clause to the
strictly-decreasing/open case and explicitly add IDL-a, the IDL-c
`h_r^2`/disjoint endpoint, sealed-root equality after absorption, the exact
open root four-block, and equality at every unnamed coordinate.  This repaired
obligation remains unresolved.

## Scope

The clean-room script checks one declared boundary row only; it is an exact
counterexample to the frozen formulation, not a census or evidence against a
repaired open-only statement.  M244's `d=5,6` census remains finite
calibration and cannot repair the quantifiers.

No IDL, all-rank `Z_2`, fixed-edit, every-color, voltage, route-length,
comparison, gap, mixing, or Terminal conclusion follows.

