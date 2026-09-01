# M137 plan: fresh referee of frozen M135

Date: 2026-08-13 UTC.

## Objective

Audit the frozen M135 orbit-incidence conflict-coloring theorem without
editing or importing M135.  The auxiliary target is the uniform physical
minimal identity sector

```text
Z_d={(t_1,...,t_(2d-2)):t_1...t_(2d-2)=id,
                              support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  Signed adjacent Hurwitz moves are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

## Assigned claims

1. Verify the immutable artifact hashes.
2. Audit `H=Stab(d)` equivariance of every descended DPS edit `tau_i`.
3. Audit freeness of global conjugation and the exact `d`-to-one splitting
   of each `S_d` orbit into `H`-orbits.
4. Audit the `d`-regular bipartite orbit-incidence multigraph and its
   `d`-edge-coloring.
5. Audit the Goursat graph-versus-parity dichotomy, including exclusion of
   the full product and the `S_6` outer-automorphism case.
6. Audit conflict independence of each matching color and the rank-four
   singleton `d^6` patch.
7. Independently reconstruct the exact `d=3` action calibration and the
   rank-four exception witness.

## Method and scope

The universal group-theoretic argument will be checked line by line.  A new
standard-library-only checker will independently implement the accepted
plus-mirror DPS construction, global/root-stabilizer orbits, paired subgroup
closure, signed Hurwitz action closure at `d=3`, and bipartite matching
decomposition.  Finite calculations are convention checks and universal-
claim falsifiers only.

No sampler, spectral gap, UST route, arbitrary-product `Gamma_0` theorem,
original heat-bath theorem, Terminal A, or Terminal B claim is in scope.

## Reproducibility

The computation is deterministic (`seed=null`), uses Python 3 and no
nonstandard dependencies, and writes machine-readable `independent_results.json`.
