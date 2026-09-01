# M317 Fresh-Audit Request

Date: 2026-08-14 UTC.

Please audit this package without importing its conclusions.

1. Verify the M317 inventory and all ten predecessor inventories (79 rows).
2. Check the exact tuple identity
   `intersection_Q D_I(Q)={h:a_(I,V)^h=b_(I,V)}`.
3. Check that equality preservation gives both well-definedness and
   injectivity, including collisions with fixed pivots.
4. Check the one-orbit, pair-orbital, and full tuple-orbit equivalences and
   witness/frame covariance.
5. Check `SPBE => PHTC => WRAD`, including that SPBE applies to the whole
   `G_I(U)`; a proper heavy subcell is not promoted to PHTC.
6. Check the exact scope of the M135 conflict-color obstruction and the
   M301/M304 `d=3` tuple obstruction. Neither may be promoted to an actual
   `d>=6` counterexample.
7. Check the natural Sym extension and the Alt two-unused-point/parity
   qualification.
8. Check the HPRN/APOH factorization and every finite-versus-literal and
   downstream stopping rule.

Freeze `ACCEPT` or `REJECT` with numbered material and nonmaterial
objections. No rank computation or broad stabilizer census is requested.
