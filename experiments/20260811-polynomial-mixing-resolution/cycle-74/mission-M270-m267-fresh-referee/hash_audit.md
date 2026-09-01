# M270 immutable provenance audit

Date: 2026-08-14 UTC.

## Frozen target

M267 was treated as immutable.  Every one of its eight payloads passes
`sha256sum -c SHA256SUMS`:

```text
plan.md: OK
checkpoint.md: OK
endpoint_profile_representation.md: OK
endpoint_profile_probe.py: OK
endpoint_profile_results.json: OK
report.md: OK
fresh_audit_request.md: OK
freeze_manifest.md: OK
```

The independently observed SHA-256 digest of M267's checksum file is

```text
001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6.
```

## Accepted dependency gate

Every file inventoried by each cited accepted dependency passes.  The
independently observed checksum-file digests are:

| mission | SHA-256 of `SHA256SUMS` |
|---|---|
| M91 | `0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703` |
| M94 | `47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562` |
| M161 | `17bd62a9b121a10058f87c576275411186e1c3c5039fa07a9cf29c9bea7358d8` |
| M166 | `344b6c76e538ecc82ac64ace908a21aabfb805330bad8a72c6ba042831e869c3` |
| M168 | `3f86fc364d1809752d06085eddad8b2e75132ea03c1d27d5a87e9ec3b1cb84bd` |
| M171 | `c47a095db5925fe69fe1756080943523376b4194b5a4cb3f6d112d8c7306fe2d` |
| M256 | `f55b7092a1cc079a8c2d46e978f42772b7c3b5d1747cede45c34d38547524261` |
| M259 | `c91571dbca9e1b7ebd8e014448530459bfade658168a76bac24b5a0ec4217aa2` |
| M261 | `b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b` |
| M264 | `b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f` |

The historical M166 freeze-manifest hash independently recomputes to the
accepted corrected value

```text
a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897f28dfbb6185e30498.
```

No M267 or predecessor file was edited by M270.

