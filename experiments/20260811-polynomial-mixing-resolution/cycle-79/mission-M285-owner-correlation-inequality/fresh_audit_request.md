# M285 fresh immutable audit request

Please audit M285 as a strict exact reduction, not as an OCI proof.

Required checks:

1. Verify the M285 `SHA256SUMS` digest and every listed payload before
   inspecting the substantive proof.
2. Reconstruct `beta_2` from full two-cycle completion counts and confirm
   that `F_(2k-2)(F)=(2k-2)!tau(k)^2` already contains the fair first-
   component choice, so no additional `1/2` is licensed.
3. Check the raw lift multiplicities and the positive-composition law:
   every supported triangle has exactly three anchor representations and
   every supported double exactly four across `S/N`, with no factor `n`.
4. Check the residual owner intervals/sizes and retention of outer `T/D`
   plus inner `IS/IN/X` before summation.
5. Verify log-convexity of `tau`, the sign of `delta_d`, and that deleting
   the size-two diagonal correction changes only lag zero, hence preserves
   exact equality at every admissible `2<=ell<=n-2`.
6. Independently evaluate the frozen `k=3` channel-two circulant at

   ```text
   v=(10,8,2,-5,-9,-9,-5,2,8)
   ```

   and confirm

   ```text
   v^T M v=-310962953715709/12252303000000.
   ```

7. Confirm that every frozen admissible `k=3` OCI entry is positive and
   that the negative PSD witness refutes only signed spectral dominance,
   not OCI.

Keep `(GOCI_j)`, OCI, CP, OS+, MS, FCL1, every gap/mixing claim, and both
Terminals unresolved unless an independent all-rank proof is supplied.
