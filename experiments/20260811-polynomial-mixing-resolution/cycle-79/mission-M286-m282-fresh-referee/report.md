# M286 report: fresh immutable audit of M282

Date: 2026-08-14 UTC.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Verdict

```text
ACCEPT M282 AS FROZEN.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL OBJECTIONS: NONE.
```

The accepted theorem is exactly `CSBV`: for every odd `k>=3`, at M282's
auxiliary balanced fixed-cell scope,

```text
|| E_(k-1)Phi_(k-1)^D
   +sum_(u=1)^(k-2)E_u(Phi_u^D-Phi_(u+1)^D) ||_1
 =O(1/k),

E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)].
```

## Audit result

- M282's checksum-file digest is
  `cac6e77151401e708acb5a812097ccce44ed1dce45acefada9a3c13ebcfe5ed7`.
  Every payload passes and its exact inventory has no extra file.
- Every payload in all nine declared predecessor ledgers passes, and all
  nine checksum-file digests match M282's source-lock table.
- The endpoint-bearing Abel collapse was independently reconstructed.
- Completion-count disintegration independently gives M282's `U_r`,
  symmetric abstract profile `c`, and literal two-seam profile `J`, with all
  ordered factors and collision multiplicities retained.
- The analytic `TV(Z_r-B_r)=O(1/R)` proof survives detailed checks at
  `r=1,2`, both Borel half-ranges, the midpoint, active/inactive cutoff,
  reflected support, and both zero endpoints.
- The exact identity `sum W=-sum q delta=O(k^-2)` removes the common profile
  before norms.  The low/bulk/junction/endpoint decomposition proves
  `TV(A)=O(1/k)`, including the explicit `k=3` case.
- The seam map gives the restricted CSBV derivative with only
  `O(D^-1)sum|c|`, and `sum|c|<=24`.

The clean-room checker reconstructs the full coefficient law exactly at
`k=3,5`; it reads no M282 code or data.  A separate boundary scan through
`k=65` is finite falsification only.

## Exact stop

This acceptance closes `CSBV` only.  `CEBV`, `CIBV`, `DOR`, `SET`, `PBV`,
`FD`, `FCL1`, every spectral-gap or polynomial-mixing statement, and both
Terminals remain unresolved.  No claim about the global identity-word target
or lazy exact `{3,4,5}` heat-bath chain follows directly from this audit.
