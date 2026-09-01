# M269 fresh audit request

Please audit M269 independently from frozen M257/M260 CP-1--CP-6 and
M250/M254 metric pruning. Do not import M269's checker or transition table as
a premise.

1. Verify the cyclic coordinate `q_j`, the slot position map `t(h)`, and the
   literal canonical child gadget (2.3).
2. Re-derive the two distance-three macro rows (2.4), including the actual
   side count and black endpoint when the gadget is paired with `B_v` versus
   `B_b`.
3. Expand the full initialization row with arbitrary siblings. Check that a
   child of `v` persists precisely for `t(h)<r` and discharges for `t(h)>r`.
4. Independently prove both internal cases `s<r` and `s>r`, including every
   special distance-three row, persistent/discharged ports, and the exact
   residual `F_v(s)` or `C_b`.
5. Audit slot-boundary coverage: no gadget may straddle `q_0`, `r`, or `s`;
   post-wrap children and empty intervals must be included.
6. Check `C_a -> C_b` from the accepted canonical macro, and independently
   verify the two arbitrary-rank `O^+`/`O^-` paired tree families.
7. If useful, rerun only the four declared symbolic rows or write a
   clean-room equivalent. Treat them as guards, not proof.
8. Confirm that Theorem 4.1 stops before `a=1`, and that DL-RST, CPR/RSPT,
   IDL, routing, gap, mixing, and both Terminals remain unresolved.

Please give numbered material and nonmaterial objections. A rejection should
name the first literal token pair whose side count, endpoint, or residual
differs.

