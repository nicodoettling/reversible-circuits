# M203 substantive checkpoint: locality route obstructed

Date: 2026-08-13 UTC.

The bounded exact audit has identified a decisive obstruction to the proposed
all-`d` blockwise proof route. No `Q_d` for `d>=6` was enumerated.

For all roots and edits of M181's explicit words at `d=5,6`, the checker
inverted only those rooted words through the exact DPS closure. Among 178 rows,
106 fail literal six-factor-region locality. At `d=6`, there are 29 cases
where an edit indexed inside the active six-factor block changes added filler
factors, and 22 converse cases where a filler-region edit changes active-block
factors.

The obstruction persists at the quotient level for the distinguished root.
Compare each of the fourteen `(pattern,edit)` cases with the naive construction
“take the `d=5` DPS target and append the new doubled leaf `(05)^2`.” Only 5 of
14 resulting quotient classes equal the actual `d=6` DPS target; 9 differ.
The first failure is pattern `0`, edit `1`, with canonical digests

```text
naively stabilized d5 target:
bd651af9408f609196bcf37c3b6bfec37a7c126bd7b1ff2cfc11c7492e8d324f

actual d6 target:
bed555f8c63642f18b33d3c0f2d6175fd96ff5afa467e8def150a7c44f5ee35b.
```

Thus DPS adjacent-value edits are global closure operations, even when their
two values lie in factor positions internal to the active block. The matched
target cannot generally be decomposed into independent `d=5` target blocks
with fixed filler, so M196's `d=5` route words cannot be embedded by the
proposed locality argument.

This is an exact no-go for that structural proof route, not a proof that the
actual `d=6` pairs are unreachable and not an obstruction to some different
all-`d` theorem. The narrow surviving conditional statement requires literal
quotient-level target factorization (or separate simultaneous routes for the
actual coupled targets). Freezing this strict obstruction now; no broader
search is warranted.
