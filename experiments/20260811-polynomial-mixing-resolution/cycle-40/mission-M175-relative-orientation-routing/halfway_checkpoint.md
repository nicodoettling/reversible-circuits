# M175 Halfway checkpoint — synchronized orientation gain graph

## Reconciled accepted starting point

All checksum lists for M135/M137, M141/M143, M146/M148, M154/M158,
M163/M164, and M169/M172 pass.  The accepted `d>=5` matching input is

```text
1 -> P_(d,s) -> K_mon(q) -> V_stab(q) -> 1,
```

where `V_stab(q)<=W_s=F_2^s/Delta` is relative white-root orientation
monodromy.  No predecessor determines this image.

## Exact reduced target now pinned down

Fix a section `sigma:Q_d->Z_d`.  For a signed Hurwitz generator `g` and
`a in Q_d`, let `rho_g(a)` be the unique relabeler satisfying

```text
g sigma(a)=rho_g(a) sigma(ga),
kappa_g(a)=sgn(rho_g(a)) in F_2.
```

On an ordered tuple vertex `x=(a_1,...,a_s)`, the local relative-orientation
gain is therefore the explicit vector

```text
gamma_g(x)=[kappa_g(a_1),...,kappa_g(a_s)] in W_s.
```

Let `Gamma(q)` be the actual synchronized signed-Hurwitz Schreier component
of `q` in `Q_d^s`, retaining generator labels and parallel edges.  The
candidate theorem is the following exact voltage-graph reduction.

> Choose a spanning tree `T` of `Gamma(q)`.  Give every vertex the sum of
> local gains on its tree path from `q`.  For every non-tree edge `e:u->v`,
> form its fundamental-cycle column
> `z_e=p(u)+gamma(e)+p(v) in W_s`.  Then
> `V_stab(q)=span_F2{z_e}`.  Consequently `K_mon/P` is this binary column
> space, full voltage is exactly rank `s-1`, and trivial voltage is exactly
> balance of this gain graph (all chord columns zero).

For fixed physical endpoints in one base component, the same matrix gives
the source-to-target zero-coset test: the endpoint-corrected gain of one tree
route must lie in the chord span.  Independent endpoint lifts translate the
route vector by the accepted coboundary; the physical test is invariant.

## Realizability versus a merely formal cycle space

This distinction is material.

- A local edge vector `gamma_g(x)` is a route gain, not by itself a
  stabilizer voltage.
- Arbitrary sums of local vectors, or cycles in a graph that forgets the
  synchronized tuple endpoints, need not be realizable.
- The cycle space used above is the cycle space of the **actual labeled
  synchronized Schreier component**.  Every fundamental cycle is an actual
  closed signed braid word and hence gives an actual stabilizer monodromy.
  Conversely every stabilizer braid traces a closed walk.  Thus the image of
  this particular cycle space is exactly realizable, not a relaxation.
- Concatenating fundamental cycles realizes sums of their columns, but gives
  no polynomial word-length bound.

This is the current durable theorem target.  It is a strict finite binary
linear-algebra reduction of the accepted orientation quotient; it is not a
uniform full-voltage or zero-voltage theorem.

## Bounded exact calibration

`relative_orientation_cycle_audit.py` independently reconstructs only
`d=3,4`; it imports no predecessor code and performs no `d=5` enumeration.

- `d=3`: `|Q_3|=4`.  The ordered-pair synchronized action has components of
  sizes `4` and `12`; both chord spaces have rank zero.  Thus every pair
  stabilizer has trivial relative voltage, reproducing the accepted finite
  behavior by the new cycle criterion.
- `d=4`: `|Q_4|=120`.  The four ordered-pair components have `(size,rank)`
  equal to `(120,0)`, `(240,0)`, `(4320,1)`, and `(9720,0)`.  In the rank-one
  component, the actual positive braid word
  `R_4 R_3 R_5 R_4` closes the ordered quotient pair `(0,1)` and has relative
  voltage one.  Thus universal trivial stabilizer voltage is already false
  at the exceptional rank four, while three other components remain
  balanced.
- The stronger ansatz
  `kappa_j(a)=theta(a)+theta(R_j a)+c_j` is inconsistent already at `d=3`
  (and also at `d=4`).  Trivial relative voltage on a component therefore
  must not be conflated with a global vertex-potential plus generator-only
  character.

These are exact finite calibration/falsification facts only.  Rank four is
outside the accepted `d>=5` M141 matching theorem, and no all-rank inference
is made.

## Next steps and status

1. Prove the synchronized gain-graph/fundamental-cycle theorem carefully,
   including inverse edges, parallel edges, section changes, and fixed
   physical endpoints.
2. State the first unresolved realization problem as a named chord-rank or
   balancedness criterion on accepted `d>=5` matching subfamilies.
3. Validate the finite certificate directly and freeze a compact checker,
   nine-field report, manifest, and hashes.

No `d=5` quotient orbit is enumerated; no polynomial braid length, gap,
mixing, or Terminal claim is made.

