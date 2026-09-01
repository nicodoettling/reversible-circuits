# M283 halfway checkpoint

Date: 2026-08-14 UTC.

## Immutable gates

M280's checksum-file digest is exactly

```text
60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9.
```

Its exact frozen payload is the ten entries named in `SHA256SUMS` (plan,
two checkpoints, reduction note, checker, JSON, report, run manifest,
fresh-audit request, and freeze manifest); every entry passes
`sha256sum -c SHA256SUMS`, and the checksum file excludes itself.

All ten required cited inventories also pass.  Their independently observed
checksum-file digests equal M280's source-lock table exactly:

```text
M161 17bd62a9b121a10058f87c576275411186e1c3c5039fa07a9cf29c9bea7358d8
M166 344b6c76e538ecc82ac64ace908a21aabfb805330bad8a72c6ba042831e869c3
M168 3f86fc364d1809752d06085eddad8b2e75132ea03c1d27d5a87e9ec3b1cb84bd
M171 c47a095db5925fe69fe1756080943523376b4194b5a4cb3f6d112d8c7306fe2d
M174 fea1f624d6b65fb8404eee0324832aa601e1bf4f202598b60a6608b1a23a51ba
M178 6ca82e9fe821c5a56b4d590dab28b29bf5e4cbc3c0af0a91c0538a53abd51fba
M266 6203ef0dca1e2c46696cec5bc1446da9656ace2b8a3a4ce9b2131267b200c052
M268 62976d7adca32d4ea7819ad36c7623430e26f75eced98a7b88bec58a4d0de2ef
M274 c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e
M277 c419b7c95e7c6fe4086d1098d6f0578445a1c3af700cabe4e90cf90d7c39d890
```

## Provisional formula audit

Independent completion-count cancellation gives, for a residual owner pair,

```text
F_(n-5)(cut residual)/F_(n-3)(residual)
 = kappa_ab/[(n-3)(n-4)].
```

The target double lift two cancels the same factor in
`pi_y=2nF_T/n^(n-2)`, leaving

```text
Lambda_n=n^(n-2)/(nF_T)
        =(n-2)(1-2/n)^(-(n-3)).
```

Thus the provisional verdict is that M280's
`CP_j=Lambda_n eta_j(F_ell)/[(n-3)(n-4)]` normalization is correct.  M91's
normalized source laws also confirm the direct channel formulas, including
the absence of an extra `1/2` in channel two.  No material objection has
emerged.  The clean compact-rank reconstruction and frozen-`k=11`
self-consistency audit remain to be completed; CP/OCI remain unresolved.
