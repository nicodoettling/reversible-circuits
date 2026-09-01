# M328 fresh-audit request

Please audit this mission immutably at its frozen obstruction scope.

1. Verify the top `SHA256SUMS` digest and every owned payload row.
2. Recheck all twelve source tops and all 100 cited payload rows, including actual M296 digest `9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f`.
3. Check that MIDEC's normalized parent capacities sum to `rho` and child demands sum to the exact full-child `rho'`, so the reserve clauses really imply AATSD (6.1)--(6.2).
4. Check the scaling obstruction: a genuinely regenerated pair uses retained coordinates, whereas every pivot-deleted parent edge uses at least one outside coordinate; scaling all outside weights destroys any universal weight-independent capacity bound.
5. Check the important limit: this obstructs the fixed source-local charge, not actual `d>=6` AATSD. A weight-dependent pivot could avoid the exposed regenerative pivot.
6. Check RATSD is strictly weaker and does not itself imply polynomial stopping without low-density terminality.
7. Confirm no computation, new rank, induced-graph substitution, polynomial-support assumption, or downstream inference appears.

Return `ACCEPT` or `REJECT` with numbered material and nonmaterial objections.
