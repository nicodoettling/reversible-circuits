# M327 final report

Date: 2026-08-14 UTC.

```text
ACCEPT M324 AT ITS FROZEN EXACT SCOPE.
MATERIAL OBJECTIONS: 0.
NONMATERIAL OBJECTIONS: 0.
```

M324's required top digest and all ten parent payloads pass.  All 99 cited
source rows pass independently, including the actual corrected M296 digest.

Independent reconstruction confirms the exact residual incompatibility graph
and the child law

```text
D_child(Q)=(D_I(P) intersect D_I(Q));h_P^-1.
```

The child cell is the parent compatibility neighborhood, while child bad
edges are empty parent triple intersections.  The outer anchor and all
already-pivoted constraints have signature `H_I`; hence a global
compatibility-score maximizer is isolated and cannot strictly shrink the
cell.  The actual matching size

```text
d^(d-3)(2d-2)!/d!
```

also exactly refutes the proposed fixed-polynomial support bound.

The `d=3` star/triple-shadow calculation correctly refutes only a generic
graph-only density argument and is not promoted to `d>=6`.  Corrected AATSD
is a coherent sufficient formulation but remains entirely unresolved, as do
actual HPRN and every downstream gate.  No finite census or replacement
search was performed.
