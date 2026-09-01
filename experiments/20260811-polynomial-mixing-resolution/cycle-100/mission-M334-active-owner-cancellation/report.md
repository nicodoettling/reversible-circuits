# M334 final report — active-owner cancellation

Date: 2026-08-14 UTC

Verdict: **REJECT `AOEC_1` exactly at the sole `k=7` guard; retain AOTI and the coefficient-resolved coboundary.**

## Result

The strictly weaker active-owner positivity target proposed after the `k=5` TOEC obstruction is still false. At the first canonical `k=7` prefix with `u=1`, `ell=2`, and active type `S_14`, the positive mass is zero and the combined internal-plus-seam negative mass gives

```text
Delta_T(S_14)=-20633990196069360/30120839742579859 < 0.
```

This is an exact rational counterexample after all required exterior, middle, target, topology, completion, seam, and weight data are retained.

## Claims retained

1. The active-owner expansion
   `Psi(T)=sum_A kappa_A Delta_T(A)` is exact.
2. The block increment identity
   `Psi(T_q)-Psi(T_(q-1))=sum_A kappa_A delta_(q,A)` is exact.
3. Ownerwise causal flows are equivalent to ownerwise prefix nonnegativity, but the exact `k=7` obstruction shows those flows do not universally exist.
4. The accepted `k=5` TOEC obstruction remains a strict firewall against full-signature transport.

## Scope

The guard was predeclared before computation and is the only rank tested. Its 2,920 negative and 7,364 nonzero prefix counts are finite `k=7` facts only. Cross-active-type weighted compensation was not resolved, so GQAC and MCLP remain open. No replacement lemma, additional rank, downstream theorem, spectral-gap, mixing, or Terminal claim is made.

Fresh immutable audit is required before integrating the exact identities or AOEC refutation.
