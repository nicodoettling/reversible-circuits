# M206 fresh immutable audit request

Audit frozen M206 without editing it.

1. Verify the complete M206 payload inventory and every SHA256 entry before
   reading its conclusions.
2. Independently derive the exact identity
   `(1-q)-T_1=S_1+S_2+S_3-X` from the stated definitions and audit all signs.
3. Prove cleanly that `Phi_(2,kappa,D,2)=0` for every valid `kappa,D`, hence
   fresh `B=2` has `T_h1=0` at every height limit.
4. Reconstruct the full vector-history rows `(B,L)=(2,4)` and `(3,4)` without
   importing M204, retaining all likelihood-weighted Gram cross terms,
   covariance subtraction, and killed `a=d`.
5. Verify exactly that `S_1-X>0` at `B=2`, while at `B=3` one has
   `S_1-X<0` and `S_1+S_2-X>0`.
6. Confirm that the negative row refutes only universal terminal-only
   transfer, the two-rung positive row is finite only, and true contraction
   remains positive in both rows.

Return `ACCEPT` or `REJECT` with numbered objections. Strict scope: no new
scan, universal two-rung claim, tail theorem, total AMV, gap, mixing, or
Terminal inference.
