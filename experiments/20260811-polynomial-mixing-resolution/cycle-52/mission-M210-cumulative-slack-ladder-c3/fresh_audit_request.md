# M210 fresh immutable audit request

Audit frozen M210 without editing it.

1. Verify the complete M210 payload inventory and every SHA256 entry before
   reading its conclusions.
2. Independently derive `C_3-X_3=(1-q)-T_1` and confirm this makes universal
   cumulative `C_3` exactly the original fresh first-Jacobi boundary.
3. Audit the full Gram-kernel recursion, `eta/pi_a` normalization, exact
   omission of killed `a=d`, and parent covariance subtraction.
4. Prove that the likelihood lift preserves PSD kernels and the parent
   first-Jacobi functional is positive linear, hence establish the stated
   full-kernel monotonicity.
5. Confirm that the direct functional-order inequality is only a restatement,
   and that constant rank-one PSD domination forces a constant feature.
6. Reproduce the exact normalized `P_2/P_3` common summaries and distinct
   charges `18/35`, `32/63`; audit the limited nonclosure inference.

Return `ACCEPT` or `REJECT` with numbered objections. Strict scope: no fresh
row scan, universal `C_3`, total AMV, gap, mixing, or Terminal inference.
