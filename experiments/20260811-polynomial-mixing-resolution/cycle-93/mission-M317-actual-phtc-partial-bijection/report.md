# M317 Final Report

Date: 2026-08-14 UTC.

## Verdict

```text
STRICT ANALYTIC REDUCTION AND PROOF-ROUTE OBSTRUCTION.
ACTUAL d>=6 SPBE/PHTC/WRAD REMAIN UNRESOLVED.
FRESH AUDIT REQUIRED.
```

All 79 payload rows across M135/M137, M296/M299, M301/M304,
M306/M309, and M312/M315 pass their frozen inventories.

## Proved exact content

1. At every compatible residual node, the intersection of signatures
   `D_I(Q)` is exactly the set of chart-stabilizer elements extending the
   source-target partial prescription that fixes the pivots and sends
   `x_Q` to `z_Q^I`.
2. Equality-kernel preservation is exactly well-defined injectivity.
   Individual compatibility is a one-orbit condition, pairwise compatibility
   is a diagonal pair-orbit condition, and common realization is the full
   tuple-orbit condition.
3. Witness and frame changes preserve this ladder by uniform right
   translation or conjugation.
4. The predeclared SPBE, applied to the whole
   `V=G_I(supp(lambda))`, implies `PHTC => WRAD` with the outer
   positive-weight anchor retained.
5. A natural symmetric pointwise stabilizer extends every admissible partial
   bijection. A natural alternating pointwise stabilizer does so with two
   unused points; with zero or one unused point, parity is the exact
   obstruction.

## Exact proof-route obstructions

M135 conflict independence preserves only a paired-generated-subgroup
invariant. It does not prove exact pair-orbital compatibility in the residual
chart stabilizer. This formal implication is already false at `d=3`, where
M135 matchings are conflict-independent but no complete matching is pairwise
compatible.

M301/M304's actual `d=3` triple is pairwise globally realizable but not
jointly realizable, giving an exact boundary failure of pairwise-to-full tuple
extension. Generic `Alt` supplies a separate parity failure: an odd total
map can have every two-point restriction extend to an even permutation.

Neither obstruction refutes actual `d>=6` SPBE or PHTC. They show that a new
actual-specific theorem is required.

## Surviving interface

```text
HPRN + APOH => SPBE => PHTC => WRAD.
```

HPRN asks for a heavy residual node whose whole individually extendable set
is pairwise compatible. APOH asks that the resulting actual orbital-preserving
partial map extend in the chart stabilizer. Both are unresolved for actual
`d>=6`.

A common extension of only a heavy proper subcell proves WRAD directly but
does not make the original PHTC node collapsing. No subcell-to-PHTC inference
is made.

No `d=6` computation was run. Finite action remains separate from polynomial
literal braid length. No MRAD, SSTID, route, voltage, congestion, gap, mixing,
or Terminal conclusion follows.
