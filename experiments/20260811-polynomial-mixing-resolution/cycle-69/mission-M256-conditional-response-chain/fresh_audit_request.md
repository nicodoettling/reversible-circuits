# M256 fresh immutable audit request

Audit the frozen M256 bundle without editing it or any dependency.

1. Run every dependency `SHA256SUMS` gate recorded in
   `dependency_audit.md` and compare the checksum-file digests.
2. Re-derive the M252 channel mixture, including `n=3k`, the conditional
   J2 normalization, shared-endpoint term, and unequal-mass endpoint.
3. Check the decisive implication `WPCR=>SCBR`: retain `M_1(1)u_1(1)`, the
   endpoint `A_m u_2(m)+C_m r_m`, and every `d^-2` interior term.
4. Check M180's large-component tail and bounded remainder before inferring
   BR/BIR.
5. Check M174's affine kind transfer, `R_n`, `pi_y`, and the PCS scaling.
6. Verify that M168's `(FD-bound)` remains independent and that PCS alone is
   not promoted to `FCL1` or `A_k(1,1)=O(1)`.
7. Run `algebra_checker.py` only as compact secondary falsification evidence.

Return numbered material and nonmaterial objections. Accept at most the
conditional theorem through PCS, plus the separate corollary under FD. Make
no DV/TAV proof attempt and no gap, mixing, or Terminal inference.
