# M227 fresh immutable audit request

Please audit this frozen directory without importing or reading M227 code or
data in the clean-room reconstruction.

1. Verify every payload against `SHA256SUMS` and report the checksum-ledger
   digest.
2. Independently derive the degree-six elevation
   `e=(1,5/6,2/3,1/2,1/3,1/6,0)` and the exact uniform first-Jacobi charge
   matrix `G`.
3. Confirm `<G,ee^T>=1/4` and justify deletion of the zero sixth coordinate,
   equivalently extension by a zero final row/column.
4. Re-derive the banded primal and PSD-completion dual and check that the
   dual constraint is `X_ij=G_ij` on `|i-j|<=w`.
5. For `w=1,2`, transcribe the rational matrices from `results.json` and
   independently verify band support, all on-band dual equalities, every exact
   positive `LDL^T` pivot for `X_w` and `C_w-ee^T`, and the four endpoint
   contractions.
6. Verify exactly

   ```text
   lower(p_1)-upper(p_2)=10951531/155232000,
   lower(p_1)-1/4=15605731/180180000,
   lower(p_2)-1/4=9820697/630630000.
   ```

7. Audit the generic rank-one elevation formula, positive homogeneity under
   each exact `eta/pi_a`, and preservation of killed `a=d` deletion.
8. Return explicit `ACCEPT` or `REJECT` with numbered objections. Reject any
   claim of exact optimal values, a degree-uniform bounded factor, aggregation,
   recursive closure/contraction, all-state control, gap, mixing, or Terminal.

