# M311 Fresh Immutable Audit Request

Please audit frozen M311 without editing this directory.

1. Verify the M311 top digest and every inventory row, then verify the locked
   M307/M308 tops and inventories.
2. Independently derive the monotone support path, including coincident
   cumulative endpoints and the `2(k-1)-1` support bound.
3. Check that rung `h=min(c,d)` has the asserted off-diagonal orientation
   from `R_h=A_h-B_h`.
4. Check the exact equivalence between `a<=min(c,d)<=b` and the mass interval
   `(max(A_(a-1),B_(a-1)),max(A_b,B_b)]`; verify no cell is sliced,
   duplicated, or omitted at sign changes or zero runs.
5. Audit QBD_1 and that QBP_1 was explicit and sufficient before execution.
6. At most once, replay the no-import `k=11` guard.  Check the first exact
   block witness, 154/450 and 118/150 counts, all 150 full-positive
   aggregates, minimum/reflection, and exact scope.
7. Freeze ACCEPT/REJECT with numbered objections.

Do not infer MCLP, GOCI, OCI, CP, MS, FCL1, a gap, mixing, or a Terminal.
