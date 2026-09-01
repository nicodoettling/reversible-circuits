# M307 fresh immutable audit request

Please audit the frozen M307 package without importing its conclusions.

1. Verify the M300 and M303 top digests and every payload; retain the
   nonmaterial fact that M300 has 15 checksum entries although M303 says 14.
2. Independently derive the equal-mass cut interval coupling, its row/column
   marginals, and QTI_1.
3. Check that `R_c=A_c-B_c` and that opposite signs force quantile support
   across both diagonal directions; do not turn this into one-direction
   monotonicity.
4. Verify that QCP_1 was frozen before computation and that it retains all
   middle phases.
5. Run at most one no-import reconstruction at exactly `k=9`; verify the
   first `(u,ell,c,d)=(1,2,2,2)` rational witness, 778/1440 negative cells,
   a negative cell in every row, reflection, and 96/96 positive MCLP
   aggregates.
6. Treat QCP_1 alone as refuted.  MCLP_1/GOCI_1 remain unresolved, and no
   GOCI_2/OCI/CP/MS/FCL1/gap/mixing/Terminal inference is offered.

Freeze `ACCEPT` or `REJECT` with numbered objections.
