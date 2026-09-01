# M180 plan: fixed-cell signed boundary response

Date: 2026-08-13 UTC.

## Objective

Attack exactly the accepted M174/M178 boundary-response obligation, for
`n=3k`, odd `k>=3`,

```text
(BR)  eta(B_k)=2 sum_(j=1)^2 alpha_j
                    Cov_(mu_j)(B_k,sigma_j)=O(1).
```

The target is M73's nonlazy cyclic rank-two quotient under the uniform
minimal long-cycle factorization law, at the balanced sources and first fixed
separated cell. It is not the global identity-word target or the `{3,4,5}`
heat-bath chain.

## Work program

1. Verify and read the named accepted predecessors, preserving their exact
   conventions and frozen boundaries.
2. Expand the full signed `J=1,2` response by triangle/double kind, positive
   gap composition, collision terms, and every small-component correction.
3. Derive one explicit channel-combined coefficient or cancellation identity.
4. Prove its uniform `O(1)` bound, or isolate a strictly narrower scalar
   lemma/asymptotic obstruction with a proved nontrivial step.
5. Use deterministic exact arithmetic only at `k=3,5` if calibration is
   needed; do not infer asymptotics or signs from it.
6. Freeze a nine-field report, proof, compact checker/results, hashes,
   provenance, and hygiene, then request fresh independent audit.

## Anti-loss rules

- Keep `L_T=0`, `L_D=-2`.
- Sum the two signed channels and triangle/double contributions before any
  absolute value.
- Retain collisions and all `(a-2)_+` small-component boundary terms.
- Do not run broad shell/quotient computations or split channels by absolute
  value.

## Scope firewall

No FD-bound, direct-L1, H0, spectral-gap, original heat-bath mixing, or
Terminal inference.

## Reproducibility

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
Any checker is deterministic, standard-library Python, `seed=null`, and
capped at exact `k=3,5`.
