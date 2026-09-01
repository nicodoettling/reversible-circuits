# Fresh immutable audit request for M301

Please audit frozen M301 independently and do not edit it.

## Required gates

1. Verify every M301 checksum and the exact package inventory.  Reproduce the
   M296 top digest
   `9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f`,
   the M299 top digest
   `1654bcd6319b3020fe49a34e54a9961b2687ba5daab107baca11873749065b8d`,
   and every row in both predecessor manifests.
2. Fix `(pq)(x)=p(q(x))` and chronological signed right-Hurwitz action.
   Confirm the actual M135 finite fibers
   `K_Q={a:a(w_Q)=tau_i(w_Q)}` and keep finite actions distinct from literal
   braid representatives and residual doubled-star stabilizer elements.
3. Reprove the generic `F_2^2` coset example.  Treat it only as denial of a
   formal arbitrary-coset Helly theorem, not as an actual project witness.
4. Rerun the one exact diagnostic.  Check the frozen M135 SHA gates, the
   closure `|A_3|=216`, `|Z_3|=24`, twelve actual `H`-orbit edges, every
   perfect matching, and the size-nine endpoint fibers.
5. Audit actual-edge scope of witness `[0,2,9]`: it must be contained in the
   actual perfect matching `[0,1,2,9]`, have distinct left and right endpoints,
   use the displayed source/target words under `tau_1`, and satisfy
   ```text
   K_0 intersect K_2={45},
   K_0 intersect K_9={49},
   K_2 intersect K_9={89},
   K_0 intersect K_2 intersect K_9=empty.
   ```
6. Enforce the central qualification: no complete `d=3` perfect matching is
   pairwise compatible.  Therefore the pre-registered whole-matching MT2H
   implication is not refuted; its premise is vacuous at this guard.  Only
   hereditary matching-subfamily 2-Helly and the unqualified pairwise-graph
   shortcut are refuted.
7. Reprove that the action-cover number `kappa(M)` equals the minimum
   common-intersection partition number.  Check both directions without
   assuming disjoint agreement hyperedges.
8. Reprove the residual-density equivalence, including the greedy
   `ceil(q(1+ln|M|))` bound and
   `|M|=d^(d-3)(2d-2)!/d!`, `ln|M|=O(d log d)`.
9. Check the mean-agreement identity only under finite-action transitivity:
   `average_a |E_a(M)|=1/d!`.  Do not infer a maximum-agreement upper bound
   or a cover obstruction from the mean.
10. Preserve the stopping line.  MRAD is unresolved for `d>=6`; even MRAD
    omits the polynomial literal-lift condition.  No all-rank Helly failure,
    every-color route, rank lift, voltage, congestion, spectral gap, mixing,
    or Terminal conclusion is accepted.
