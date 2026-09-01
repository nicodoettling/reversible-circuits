# Independent referee plan: M05 shuttle comparison

Date: 2026-08-11  
Base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## Frozen claim

For every `N>=3`, even `m>=4`, and feasible macro datum `alpha`, audit

```text
gap(P_H^alpha)>=delta/m^10,
gap(K^alpha)>=(m-1)delta/[2|R_m|(m-2)M^2m^10],
M=binom(N,2),
delta=min(1,min_a gap(P_a)).
```

The convention is `(pq)(x)=p(q(x))`; the right Hurwitz generator is
`R_i(p,q)=(q,qpq)` and its inverse is `(pqp,p)`.

## Audit obligations

1. Re-derive the product-coordinate gap with the exact mixture weights.
2. Symbolically execute both shuttle orientations and all endpoint cases.
3. Try to construct two distinct sources with the same directed physical
   edge and metadata `(a,u,v,epsilon,s)`; include repeated colors, duplicate
   generator outputs, self-loops, and collisions between path phases.
4. Recompute canonical-path load and the direct color load.
5. Re-audit the original padded-H3 comparison rather than relying only on
   the frozen summary.
6. Check singleton, `m=4`, near-minimal, rare-color, and exact small-case
   calibrations.

The frozen bundle will not be edited.  This directory contains only the
independent referee record.

