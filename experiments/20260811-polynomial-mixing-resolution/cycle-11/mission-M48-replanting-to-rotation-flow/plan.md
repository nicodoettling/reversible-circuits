# M48 plan: weighted replanting-to-rotation flow

Date: 2026-08-11.  Convention: rooted plane trees are encoded by Dyck
words; the exact rotation is `UD P <-> U P D` for a nonempty Dyck
excursion `P`.  The target law on trees with `r` edges is proportional to
`product_v 1/d_v!`.

## Objective

Prove a polynomial stationary-flow comparison from the M41 weighted
leaf-replanting chain to the exact M35 leaf-rotation subchain, or refute a
named routing template and isolate the smallest surviving proposition.

## Bounded falsification

Enumerate Dyck words through a named small size, reconstruct rotation and
leaf-replanting graphs exactly, and test only explicit structural routing
lemmas (not asymptotic mixing).  Deterministic calculations require no
random seed.

## Expected failure modes

- Confusing `UDU <-> UUD` leaf translation with `UD P <-> U P D` for
  nontrivial `P`.
- Routing through the star, path, comb, or another exponentially light hub.
- Ignoring the factorial stationary density or reverse capacity.
- Using Fleurat deletion kernels pointwise rather than only through their
  aggregate balance identity.
