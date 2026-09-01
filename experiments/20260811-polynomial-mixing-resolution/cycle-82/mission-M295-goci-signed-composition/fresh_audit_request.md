# M295 fresh-audit request

Please audit the frozen M295 package independently.

1. Verify `SHA256SUMS` and the eight prerequisite inventory digests in
   `dependency_audit.md`.
2. Re-derive `beta_1(ef)=gamma_k(e)nu_M(f)` and the implication
   `(FMCP_1) => (GOCI_1)` without importing M295 code.
3. Recompute only the displayed `k=5`, `f=(6,9)`, `ell=6` exact witness,
   preferably by an independent positive-composition interval
   implementation.
4. Check the no-extra-`1/2`, `1/3`/`1/4`, no-extra-`n`, admissible-lag, and
   reflection conventions.
5. Confirm that the negative fixed-middle cell is not misreported as a
   GOCI/OCI counterexample and that all downstream claims remain open.

Requested verdict: ACCEPT / REVISE / REJECT with material and nonmaterial
objections separated.

