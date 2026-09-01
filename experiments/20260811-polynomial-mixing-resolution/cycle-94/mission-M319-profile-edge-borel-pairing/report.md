# M319 report: canonical edge-preimage pairing is not a reduction

Date: 2026-08-14 UTC

## Verdict

```text
KEEP the exact global edge-coefficient identity J_e=L_e^+-L_e^-.
PROVE the qualitative atom-split orientation-reversing involution.
REJECT canonical PEBP as proof progress: its boundary bound is exactly MPCF.
MPCF and every downstream statement remain unresolved.
```

## Exact obstruction

After all required combinations and the corrected `c_X` factor, let `L_e^+`
and `L_e^-` be the total literal preimage masses directed along and against a
fixed orientation of unordered profile edge `e`.  Then exactly

```text
J_e=L_e^+-L_e^-.
```

The frozen PEBP involution canonically matches mass
`min(L_e^+,L_e^-)`.  Its unpaired boundary has mass

```text
|L_e^+-L_e^-|=|J_e|.
```

Therefore total PEBP boundary mass is `||J||_edge` identically.  The proposed
Borel-scale PEBP bounds are MPCF itself, not a narrower lemma.  The pairing
also yields no conserved grading or source-local boundary: its unmatched
tokens depend on arbitrary ordering after global sign aggregation.

An exact two-profile abstract realization shows that the accepted Borel
coupling axioms alone can give `|J_e|=c_X`; literal owner/source localization
is indispensable.  This is not an actual owner-law counterexample.

## Strongest surviving result and next lemma

The residual-product edge formula and `J_e=L_e^+-L_e^-` are exact all-rank
identities.  The first genuinely stronger obligation is a source-local raw
coboundary: a fixed surgery, chosen without consulting final edge surpluses,
must reverse each nonexceptional token and leave only an explicitly localized
seam/head-incidence exception set with the required H/A/C Borel masses.  No
such surgery is proved here.

## Exact stop

No `k=15` guard was run because canonical PEBP and its equality to MPCF hold
identically; a finite constant could not test the missing source-local map.
No alternative pairing, rank, row, residual/cell/channel/type/orientation
bound, or scalar path-length argument was used.

```text
global residual-product edge formula                    proved exact
qualitative canonical PEBP involution                   proved exact
PEBP as a strict/narrower reduction                     refuted (circular)
quantitative PEBP / MPCF                                unresolved/equivalent
source-local edge coboundary certificate                unresolved
CMPAD/CBPV/SOCL and all downstream claims               unresolved
```
