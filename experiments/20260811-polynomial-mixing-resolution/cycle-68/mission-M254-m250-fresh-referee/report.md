# M254 final report: fresh referee of M250

Date: 2026-08-14 UTC.  Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Verdict

```text
ACCEPT:
  M250 exact metric canonical pruning;
  M250 open common-nonchild h_r^2 endpoint and disjointness;
  M250 conditional RSPT-to-IDL coordinate exhaustion.

UNRESOLVED:
  RSPT itself, repaired RSMI+, IDL, and unconditional all-rank Z2.

MATERIAL OBJECTIONS: none.
```

Every M250 inventory entry verifies, and its top digest is exactly
`243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7`.
All four dependency inventories and the locked DPS PDF also verify.

The metric proof survives clean-room reconstruction.  A canonical leaf
reduces to `S W^(R_a) S S`.  A canonical child contributes the two exact
rows

```text
W^q S S S B_a^q -> S,
W^(q-1) S S S B_a^(q-1) -> S,
```

so both slot labels record parent black `x_a`; ordinary rows have one side.
All consumed intervals are complete nested LIFO nodes, and the reversed
edited slot `x_v` remains on the retained path.

For a high common nonchild whose parent lies on the decreasing path, the
cyclic suffix also closes to one side.  This remains true across the label
seam, including lower-index children after the wrap and the new child `d` at
`a=1`.  Thus both ranks give the literal common slot
`h_r^2`, disjoint from `{v-1,d-1,d}`.

RSPT remains a hypothesis.  Conditional on its endpoint tables, the low
labels and four root labels form a disjoint exhaustive partition and give
closed equality or IDL-a--d exactly, including the empty intermediate scan.
No rejected M244 RSMI clause is used.

The no-import clean-room checker ran exactly the four predeclared `d=7` rows,
found zero failures, and independently reproduced M250's normalized digest
`d285b53ae1646d9ab241c17f51c92a55d563ad5de2095d9f77dfdfc133e59c59`.
This is finite calibration only.

Three numbered nonmaterial clarifications are recorded in `proof_audit.md`:
one child-row phrase, explicit cyclic-order wording at the seam, and the fact
that `RSMI+` names M247's five obligations rather than a separately boxed
lemma.  None changes a theorem or supplies RSPT.

No fixed edit, every-color route, voltage correction, route length,
congestion, gap, mixing theorem, or Terminal is promoted.

