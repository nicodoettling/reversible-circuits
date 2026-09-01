# M240 fresh-audit request

Please audit M240 from the frozen files without importing its Python module or
trusting its result JSON.

Required checks:

1. Reconstruct the exact `N,A` definitions, zero-/one-based labels, factor
   positions, and chronological signed right-Hurwitz convention.
2. Check that `NOT(late OR ascent)` is exactly strict decrease of the stopped
   path.
3. Treat IDL as **unresolved**, not proved.  Audit whether its displayed
   positions and direct-child/common-slot cases are internally sufficient for
   the theorem.
4. Recompute both square identities and the direct-child conjugation identity
   without importing M240 code.
5. Audit the scan induction indices, especially cursor positions before and
   after every generator pair.
6. Audit the terminal four-block and five-move carrier under chronological
   convention.
7. Audit the final `Q^-1` chronology and exact conditional length.
8. Confirm ordinary versus fixed-edit scope and every explicit nonconclusion.
9. Independently implement only the generic identities if desired.  Do not
   run another finite DPS rank census.

Return `ACCEPT` or `REJECT` with material/nonmaterial objections, immutable
hashes, and a strict statement of what remains unresolved.

