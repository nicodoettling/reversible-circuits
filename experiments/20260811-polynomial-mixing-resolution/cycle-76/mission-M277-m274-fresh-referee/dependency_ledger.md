# M277 immutable dependency ledger

Date: 2026-08-14 UTC.

Every listed value is the SHA-256 digest of that mission's `SHA256SUMS`
file.  Every payload named by every inventory passed `sha256sum -c` on the
audit date.

```text
M274  c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e
M91   0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703
M94   47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562
M100  bc5a915fc10aef4b546542938e9289e516e97a13553d4888d7b0395acd8965a2
M161  17bd62a9b121a10058f87c576275411186e1c3c5039fa07a9cf29c9bea7358d8
M166  344b6c76e538ecc82ac64ace908a21aabfb805330bad8a72c6ba042831e869c3
M168  3f86fc364d1809752d06085eddad8b2e75132ea03c1d27d5a87e9ec3b1cb84bd
M171  c47a095db5925fe69fe1756080943523376b4194b5a4cb3f6d112d8c7306fe2d
M174  fea1f624d6b65fb8404eee0324832aa601e1bf4f202598b60a6608b1a23a51ba
M178  6ca82e9fe821c5a56b4d590dab28b29bf5e4cbc3c0af0a91c0538a53abd51fba
M261  b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b
M264  b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f
M266  6203ef0dca1e2c46696cec5bc1446da9656ace2b8a3a4ce9b2131267b200c052
M268  62976d7adca32d4ea7819ad36c7623430e26f75eced98a7b88bec58a4d0de2ef
M267  001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6
M270  6c0c6e13c62885a0c56e8c232c0f2ddc48922be56b3edce97a4f9c9b9ca5491e
```

The M274 inventory contains ten payloads and excludes itself, as declared.
The two frozen result hashes are

```text
exact_sign_k9.json         98ed5a1e81c0e4ccd448a80648b5db872c937e9f561a6004e66ac9b0cf57c3fb
monotonicity_results.json  ba0dc258b390d0e304235cb20b963cdabd18a82efca9adaa4b5e2a77b79c2cee
```

The fresh M274 monotonicity rerun is byte-identical to the frozen JSON.  The
fresh M161 `k=9` rerun differs only at `/command` (the output path) and
`/results/0/runtime_seconds`; all mathematical leaves agree exactly.

Dependency-metadata correction: `check_monotonicity.py` loads M91, M91 loads
M83, and M83 imports NumPy unconditionally.  Therefore the frozen claim
`nonstandard_dependencies: null` is literally false for that invocation.
The installed version was NumPy `1.26.4`.  This does not affect the exact
`Fraction` arithmetic, and M277's replacement checker has no nonstandard
dependency.
