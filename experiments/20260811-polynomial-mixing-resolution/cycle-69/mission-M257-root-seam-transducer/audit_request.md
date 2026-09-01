# M257 fresh-audit request

Audit the frozen M257 payload without editing it or importing a predecessor
checker.

1. Verify all predecessor and DPS digests.
2. Reconstruct the actual parent incidence of the reversed child and confirm
   `kappa(v)=L_v`, while every canonical child has `kappa(c)=R_c`.
3. Derive equations (3.1) and (3.4) directly from the increasing-white,
   decreasing-black DPS contour, including both sides of every tree edge.
4. Check that accepted metric pruning gives exactly the five-token parent
   block (3.3), and that complete-node commutation licenses the nesting.
5. Audit cyclic wrap, lower-index children, `a=1`, `v=d-1`, empty intervals,
   and unnamed-label exhaustion.
6. Confirm that CPR and RST are genuinely separate unresolved obligations
   and that no sentence promotes RSPT or IDL.

Return numbered material objections and a split ACCEPT/REJECT verdict.  Do
not run a rank census or infer any downstream routing, gap, mixing, or
Terminal statement.
