# M80 plan: fresh referee of M73 and shared-factor continuation

Date: 2026-08-12. Repository commit at start:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Scope and target

Audit the frozen M73 minimal-long-cycle cyclic product kernel. Permutations
compose as `(pq)(x)=p(q(x))`; factor tuples multiply left-to-right. The target
is the uniform law on minimal length-`n-1` transposition factorizations of the
odd long cycle `h=(0 1 ... n-1)`, compressed first to pair products and then
to simultaneous-`h`-conjugacy orbits. This is neither an identity bridge nor
a global sampler claim.

## Referee obligations

1. Verify the frozen report and manifest hashes and every listed manifest
   entry.
2. Audit independently the raw and orbit kernels, stationary law,
   reversibility, covariance lower edge, cyclic-composition weights, four row
   schemas, conditioned-Borel formula, diameter-two graph proof, and the
   Dobrushin/eigenvalue implication.
3. Rerun the smallest decisive exact computations at `n=5,7` and independently
   reconstruct the exact `n=7,9` adjacent-TV certificates without altering the
   frozen source directory.
4. Issue `ACCEPT` or `REJECT` with numbered objections before doing new work.
5. Then attack the named shared-factor two-step influence inequality by an
   explicit posterior coupling, SDPI, or signed schema calculation. Preserve
   counterexamples and distinguish exact finite evidence from proof.

## Expected failure modes

- treating quotient orbit masses as uniform;
- confusing the forward correlation kernel with a heat-bath chain or assuming
  it is positive semidefinite;
- losing an orbit stabilizer in the balanced three-composition;
- taking absolute values before the sixteen-schema sum;
- using diameter alone without the adjacent `O(n^-2)` influence estimate;
- extrapolating finite `n` data to the universal lemma.

All outputs are deterministic (`seed=null`). No files outside this directory
will be edited.
