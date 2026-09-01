# M148 plan: fresh referee of frozen M146

Date: 2026-08-13 UTC.

## Objective

Independently audit the frozen M146 common-parity conjugacy theorem and its
application to aligned DPS transposition tuples.  Preserve its necessity-only
scope; do not pursue a common braid.

## Immutable inputs

Verify the six SHA-256 digests supplied in the assignment before relying on
M146.  Read the accepted frozen M141/M143 dependency only for the statement
that every nonempty `d>=5` matching subfamily has source and target generated
group `P_(d,s)`.

## Checks

1. Re-derive the centralizer parity criterion from cycle structure.
2. Re-derive the `P_(d,s)` class-splitting formula by centralizer parity images
   and normal-subgroup/double-coset orbit counting, including `r=0`.
3. Check the all-odd and aligned-transposition corollaries.
4. Audit the factor-class multiset as a necessary Hurwitz invariant and its
   automatic collapse under M141/M143.
5. Reconstruct the bounded `d=3` DPS calibration independently in owned code.
6. Issue an explicit ACCEPT/REJECT report with numbered objections, nine
   fields, reproducible artifacts, immutable hashes, and hygiene statement.

## Expected failure modes

- Confusing ambient coordinatewise conjugacy with conjugacy in `P_(d,s)`.
- Missing the diagonal parity direction when no coordinate is rigid.
- Treating a necessary factor-class invariant as sufficient for a common
  signed braid.
- Reusing M146 executable code rather than performing an independent check.

