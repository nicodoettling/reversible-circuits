# M273 fresh immutable audit request

Please audit frozen M273 independently from accepted M269/M271,
M257/M260, and M250/M254. Do not import M273's theorem, transition table, or
guard as a premise.

1. Verify every predecessor inventory and the locked DPS source digest.
2. Re-derive `s=m-R_v`, the old root slot, the new child-`d` slot, the new
   root slot, and the inherited position map `(2.5)`.
3. Reconstruct the full root-white complement `(3.1)--(3.2)` directly from
   the DPS contour, including both crossings of the root edge.
4. Expand the new child block literally and verify the `beta` then `alpha`
   distance-three rows to `x_1`. Check that it lies on the current-parent arm
   in direct initialization, contraction, expansion, and canonical input.
5. Independently prove all three cases of Lemma 4.1. Include arbitrary
   siblings, post-wrap slots, empty intervals, and the impossibility of
   `r=s`.
6. Check the exact three sides in the old `alpha -> x_v` and new
   `gamma -> x_v` top-lens rows. Then verify that every lower black-arm row
   has one side and list the remaining white for every label.
7. Audit ports individually. In particular, verify the first-width-crossing
   endpoint for smaller children can be nonroot and that `(2.5)` chooses the
   same crossing at both ranks. Confirm that only larger direct-child ports
   survive an open root.
8. Check the inherited-low-label exhaustion and the equivalence between a
   decreasing numerical path and final open completion.
9. Reproduce every entry of the open and sealed
   `alpha,beta,gamma,delta` tables without using finite data.
10. Audit the formal conditional composition: accepted M269/M271 plus DL-RST
    should imply M250 `(4.3)--(4.5)` without reviving its refuted `(4.2)`;
    only then do M250/M254 and M240/M242 imply IDL and the ordinary-edit
    route.

If useful, rerun only the four declared cases or write a clean-room
equivalent. Treat finite success as calibration. Give numbered material and
nonmaterial objections. A rejection should identify the first literal
half-edge pair, port, endpoint, or residual that differs.

