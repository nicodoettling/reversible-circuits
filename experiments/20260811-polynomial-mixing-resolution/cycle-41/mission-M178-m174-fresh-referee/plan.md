# M178 plan: fresh immutable audit of M174

Date: 2026-08-13 UTC

## Scope

Audit the frozen M174 fixed-cell PCS reduction without editing M174 or any
coordinator-owned artifact.  The target remains the global fixed-length
uniform identity-word bridge law.  This audit makes no mixing or asymptotic
gap claim.

## Checks

1. Verify every frozen checksum before reading or using M174.
2. Reconstruct the definitions of `P_g`, `f`, the signed fixed-cell response,
   and the `pi_y` normalization.
3. Check `PCS-bound` equivalently as `n^2 |Delta(C_k)| = O(1)`.
4. Reconstruct the `J=0` cancellation and the two-channel covariance identity.
5. Audit the cycle-index/Borel `U,V` response, with affine constants
   `L_T=0`, `L_D=-2`; explicitly reject the transient `7/5` interpretation.
6. Independently prove uniform boundedness of `u_1,v_1,u_2,v_2`, including
   all positive two-run lengths and `(a-2)_+` boundary terms, or flag a gap.
7. Check the exact triangle term `eta(T)`, including its simplified
   denominator, and the reduction
   `Delta=e^-2/R_n [2n eta(T)+eta(B_k)]`.
8. Check the equivalence between PCS-bound and `eta(B_k)=O(1)`.
9. Independently reproduce only `k=3,5` exact/literal checks.

## Exclusions

No `k=7` requirement, FD-bound, broad matrix computation, asymptotic inference,
direct-L1/H0/gap claim, or Terminal inference.

## Deliverables

Clean-room derivation/check script and machine-readable results; a nine-field
report with numbered objections; immutable freeze manifest and hashes.
