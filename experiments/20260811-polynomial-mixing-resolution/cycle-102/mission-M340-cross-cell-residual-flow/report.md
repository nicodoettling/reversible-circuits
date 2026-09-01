# M340 final report

Date: 2026-08-14 UTC

## Verdict

```text
OBSTRUCTION PROGRESS.
REJECT THE FROZEN COMPLETE-LABEL XCRF.
KEEP THE EXACT HALL/CELL-DIVERGENCE IDENTITIES AND M335 J SPLIT.
```

The candidate retains the exact canonical residual signs, quantile-cell
masses, corrected `c_X`, raw source-switch labels, zero slots, both channels,
all `T/S/N`, phases, seams, and incidences before norms.  Its exception is
exactly the accepted source-geometric `Exc_pf^*`.

Complete-label retention makes the raw source switch deterministic, so its
cross-cell transport graph has degree at most one.  Rational transport
therefore cannot pool mass among different cells: atomwise Hall requires an
actual supported different-cell reverse token of exactly equal weight.

The accepted M335/M336 off-exception `k=9,H_2,(1,1)` token is an exact
counterexample.  Its raw switch stays in `(1,1)`, while canonical residual
signs give

```text
a_11(Q)=0,                b_11(P)=0.
```

The token has the strictly positive complete weight displayed in `(2.1)` of
`analytic_obstruction.md`.  It has no allowed neighbor, so singleton Hall is
the false inequality `w(omega_0)<=0`.  This failure precedes weight matching,
norms, and final signs.  No M340 finite guard was required or run.

## Strongest surviving statements

- Atom-refined Hall plus total mass equality is necessary and sufficient for
  the frozen rational transport.
- Cell aggregation obeys the exact row/column, cut, and divergence identities
  in Section 5 of `candidate.md`.
- For a partial flow,
  `M_c^+-M_c^-=div F(c)+r_c^+-r_c^-` exactly; the witness forces unmatched
  positive mass at least `w(omega_0)` in its literal label component.
- `J=J_compatible+J_exceptional` and M335's combined exceptional scalar
  reduction survive unchanged.

The unmatched literal component does not by itself prove a nonzero final edge
coefficient.  H/A/C exceptional Borel scales, a broader source-local
cross-cell relation, compatible cancellation, MPCF, CMPAD, SOCL, gap, mixing,
Terminal, and all downstream conclusions remain open.

## Scope

No new rank, row, cell, guard, source surgery, alternate grouping, arbitrary
sign pairing, scalar path length, or separate constituent bound was used.

