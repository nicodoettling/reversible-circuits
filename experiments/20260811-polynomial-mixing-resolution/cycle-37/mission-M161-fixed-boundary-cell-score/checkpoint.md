# M161 initial checkpoint

Date: 2026-08-13.

The required project skill, `HANDOFF.md`, `GOAL_SPEC.md`, sampling and
experiment references, and accepted M91, M94/M100, M102/M105, M155/M159
artifacts have been read. M73's exact quotient-kernel formulas and the
accepted finite implementations have also been inspected.

The controlling constraint is now fixed: for the separated target cell
`(1,y,1,n-2-y)`, the score must be evaluated through M94's complete signed
posterior convolution. Both M91 source channels and all intermediate
triangle/double, collision, and lower-support strata must be combined before
`|.|` and before averaging in `y`. M102/M105 forbid replacing this by a
generic double/double bulk integral.

No new theorem is claimed at this initial checkpoint. The next step is a
literal specialization of the exact convolution to this target family and a
schema-by-schema reduction in `y`; compact finite computation will follow
only after that formula exists.

## Final checkpoint

The score is now an exact circular correlation in lag `y+1`, with all
triangle/double and `IS,IN,X` terms signed before absolute value.  Reflection
symmetry is exact.  A raw-state checker (no quotient matrix) passes at
`k=3,5,7`.  The finite values decrease, but `(FCL1)` remains unresolved.

Final verdict: **EXACT FIXED-CELL CONVOLUTION REDUCTION; ASYMPTOTIC
BOUNDEDNESS UNRESOLVED.**
