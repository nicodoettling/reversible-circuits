# M304 Fresh Referee Report on M301

Date: 2026-08-14 UTC

## Verdict

**ACCEPT M301 AS FROZEN AT ITS EXACT FINITE-ACTION SCOPE.**

Material objections: none.  Nonmaterial objections: none.

## Accepted content

- Common-intersection partition number equals action-cover number exactly.
- A `q`-action cover gives residual agreement density at least `1/q`;
  uniform residual density `1/q` gives a cover of size at most
  `ceil(q(1+ln|M|))`.
- Since `|M|=d^(d-3)(2d-2)!/d!`, the loss is `O(d log d)`.
- Under finite-action transitivity, uniform mean agreement is exactly
  `1/d!`; this is not a maximum-agreement bound.
- At `d=3`, actual edges `[0,2,9]` have singleton pair intersections
  `{45}`, `{49}`, `{89}` and empty triple intersection inside matching
  `[0,1,2,9]`.
- No complete `d=3` matching is pairwise compatible.  Thus hereditary
  2-Helly is refuted exactly, while registered whole-matching MT2H remains
  vacuous at this guard and is not refuted.

The clean-room checker independently reconstructs `|Z_3|=24`, `|A_3|=216`,
four global orbits, twelve `H`-orbits, and all 36 indexed perfect matchings.

## Exact stop

MRAD remains unresolved for `d>=6`.  Even MRAD supplies only finite-action
nonemptiness; polynomial literal braid length remains a separate obligation.
No SSTID, routing, voltage, congestion, gap, mixing, or Terminal conclusion
is accepted.

