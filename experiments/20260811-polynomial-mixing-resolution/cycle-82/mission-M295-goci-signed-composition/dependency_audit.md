# M295 dependency audit

Date: 2026-08-14 UTC.

## Integrity

Before fixing or testing a new candidate, I ran `sha256sum -c SHA256SUMS`
inside every required frozen author/referee directory.  Every listed file
passed.  The inventory digests agree exactly with the coordinator ledger:

```text
M266  6203ef0dca1e2c46696cec5bc1446da9656ace2b8a3a4ce9b2131267b200c052
M268  62976d7adca32d4ea7819ad36c7623430e26f75eced98a7b88bec58a4d0de2ef
M274  c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e
M277  c419b7c95e7c6fe4086d1098d6f0578445a1c3af700cabe4e90cf90d7c39d890
M280  60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9
M283  156fa5207e088f38ae71b69e48332a8a708bae8f03f1447c77e9710128572cdf
M285  54eed4258da59ee1b8491815f182f05ac7c57c809e0f002bc2a2a79666098ac8
M287  0298ecf0d0f3ca2970f4a817469a01e247b125b4b0211eb748b752146e73fc35
```

## Mathematical dependency ledger

| dependency | accepted input used here | M295 check | status |
|---|---|---|---|
| M266/M268 | PCS is a signed-total bound only; no minority sign follows | hashes and accepted scope checked; no PCS step is used in the FMCP falsifier | proved input, downstream unused |
| M274/M277 | `CP_j`, channel masses, MS hierarchy, and MON/FOSD/raw-atom firewalls | exact `k=5` minimum weighted `alpha_1 CP_1` is independently reproduced | proved input |
| M280/M283 | `CP_j=Lambda_n eta_j(F_ell)/[(n-3)(n-4)]`, literal owner response, lag/reflection domain | exact prefactor, literal/repaired equality, and reflection independently checked | proved input |
| M285/M287 | `beta_j`, `1/3` triangle and `1/4` S/N composition factors, no extra `n`, no channel-two `1/2`, repaired autocorrelation | direct residual-cycle response equals an independent S/N positive-composition interval reconstruction for all `k=5` states and lags | proved input |

The target is only the accepted auxiliary first separated fixed cell for odd
`k>=3`, `n=3k`; it is not the global uniform identity-word target and does
not analyze the lazy exact same-product `{3,4,5}` heat-bath kernel directly.

## Convention guard

Permutations use `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  Channel two's full two-cycle denominator already contains
the fair first-component choice, so M295 inserts no extra `1/2`.  The anchor
is a support vertex, so no factor `n` is inserted into the positive cyclic
composition law.  The exact response domain is `2<=ell<=3k-2`.

