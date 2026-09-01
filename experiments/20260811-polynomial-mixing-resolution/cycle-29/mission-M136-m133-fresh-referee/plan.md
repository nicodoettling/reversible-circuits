# M136 plan: fresh referee of M133

Date: 2026-08-13 UTC.

## Objective and target

Independently audit frozen mission M133's subtraction-free unique-cycle
decomposition for the M113/M118 auxiliary incidence-key law

```text
rho(kappa)=|C_kappa|/Z_inc,
H[d,c]=M[d,d-c].
```

This is not an audit of the original uniform identity-word target or of the
lazy exact `{3,4,5}` heat-bath kernel.  The only possible verdict is `ACCEPT`
or `REJECT`, with numbered objections.  No continuation work is in scope.

## Frozen inputs

M133 is immutable.  Its supplied report, proof, two checkers/results,
manifest, and checksum-inventory hashes were verified before audit.  The
accepted dependency chain M113/M118 and M125/M129 will be checked only to the
extent needed to establish the coefficient interface and scope.

## Independent checks

1. Re-derive the bipartite incidence multigraph correspondence and prove or
   falsify the unique even-cycle plus planted alternating-tree bijection.
2. Audit the least-core-edge traversal, orientation count, and the special
   two-parallel-edge core for hidden rotation or reflection factors.
3. Implement an independent exact checker, without importing M133 code, for
   literal ordered partition pairs versus the positive recurrence on small
   indexed atom sets.
4. Independently reconstruct fixed-core profiles and total `H[d,c]` values,
   comparing them with literal partition-pair sums and the accepted M125
   coefficient formula on tractable small cases.
5. Verify the exact `d=4,c=3` pairwise-polarization counterexample and its
   cleared margin `-17309376`.
6. Recompute the claimed targeted `d=23,24,25,26` triples with an independent
   implementation where feasible; otherwise audit the recurrence and rerun
   the frozen exact computation, clearly separating independence from
   reproduction.
7. Check all exceptional-case and finite-scope labels, then issue the final
   verdict and freeze this referee directory.

## Expected failure modes

- an omitted orientation, rotation, or automorphism factor in core encoding;
- double counting when the unique core has two parallel edges;
- a planted branch attached to two core vertices or an omitted branch-root
  choice;
- mismatch between indexed atoms and cycle-type symmetry factors;
- an off-by-one conversion between cycle count `c` and defect `r=d-c`;
- finite evidence stated as universal log-concavity or as a sampler gap.

All computations are exact, deterministic, standard-library-only, with
`seed=null`.
