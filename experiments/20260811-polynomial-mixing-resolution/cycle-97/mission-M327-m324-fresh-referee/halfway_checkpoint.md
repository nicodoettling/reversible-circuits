# M327 substantive audit checkpoint

Date: 2026-08-14 UTC.

The immutable gate is clean:

- M324 top digest is
  `d42ba8d98c5d8c00501a01d458a1d6598bdfc8cce324344ae1e46b7081280aab`;
- its inventory has exactly ten payload rows, all passing;
- all 99 cited source rows pass independently;
- the actual frozen M296 digest is
  `9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f`.

The substantive reconstruction presently finds no defect.  In particular,
right translation by the chosen pivot witness gives

```text
D_child(Q)=(D_I(P) intersect D_I(Q));h_P^(-1),
```

so the child vertex set is exactly the parent's compatibility neighborhood,
whereas child bad pairs are empty parent triple intersections.  The outer
anchor and every pivot already in `I` have signature `H_I`; their
compatibility weight is all of `W_I`.  Hence a global `c_I` maximizer is
isolated and cannot strictly shrink the vertex set.

The matching size calculation also checks exactly:

```text
|M|=|Z_d|/d!=d^(d-3)(2d-2)!/d!,
```

which refutes a universal `|U|<=d^K` premise under uniform positive weights.
The remaining audit is confined to the `d=3` triple-shadow boundary scope and
the quantifiers of unresolved AATSD.  No new rank or search is being run.
