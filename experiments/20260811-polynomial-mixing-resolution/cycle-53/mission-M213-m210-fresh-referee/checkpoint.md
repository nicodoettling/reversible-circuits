# M213 checkpoint

Date: 2026-08-13 UTC.
Status: substantive halfway audit complete; provisional `ACCEPT`.

## Immutable gate

- Ownership remains restricted to M213; M210 has not been edited.
- Before reading M210's conclusions, I enumerated its exact nine-file
  inventory (`SHA256SUMS` plus eight payloads) and verified every payload.
- M210 `SHA256SUMS` digest:
  `fe96d736dd4b0bd330d98975a47ad8e4e42a949d34ec27f5087daadd48120c7b`.
- Accepted dependency ledgers M162/M165, M173/M177, M179/M184, M193/M197,
  M201/M204, and M206/M209 also pass.

## Independent halfway findings

1. Direct expansion gives
   `C_3-X_3=(1-q)-[T_reset+sum_(h>=1)T_h]=(1-q)-T_1`.
   Thus `C_3>=X_3` is exactly the open fresh first-Jacobi boundary.
2. The block `sqrt(eta/pi_a)L_a Phi_child` reproduces the full-kernel lift
   `eta L_a(u)L_a(v)K_child(u,v)/pi_a`; killed `a=d` is absent.
3. `Q` is positive linear on PSD Gram kernels, likelihood lifting preserves
   PSD order, and the resulting child-charge map is PSD-monotone.
4. Nonmaterial precision clarification: the residual is affine and antitone
   in each child kernel because positive charges enter with a minus sign.
   M210's displayed formulas and monotonicity section have the sign correct.
5. The two-point `(1,-1)` test proves a constant `cJ` cannot PSD-dominate a
   nonconstant Gram feature.
6. Exact normalized `P_2/P_3` inputs share
   `(M,C,||Z||^2,T_1)=(0,0,1,1)` but have parent charges `18/35` and
   `32/63`, with zero first-mode subtraction. This rules out exact closure
   on the listed summaries only, as M210 itself states.

Provisional verdict: `ACCEPT`; no material objection. Freeze follows without
any finite scan or generalization.
