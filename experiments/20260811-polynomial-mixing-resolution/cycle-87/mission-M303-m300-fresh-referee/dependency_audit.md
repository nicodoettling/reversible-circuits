# M303 dependency audit

Date: 2026-08-14 UTC.

Every listed payload in each inventory below passes `sha256sum -c
SHA256SUMS`.  The independently measured checksum-file digests are:

```text
M274  c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e
M277  c419b7c95e7c6fe4086d1098d6f0578445a1c3af700cabe4e90cf90d7c39d890
M280  60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9
M283  156fa5207e088f38ae71b69e48332a8a708bae8f03f1447c77e9710128572cdf
M285  54eed4258da59ee1b8491815f182f05ac7c57c809e0f002bc2a2a79666098ac8
M287  0298ecf0d0f3ca2970f4a817469a01e247b125b4b0211eb748b752146e73fc35
M295  42fa1c38b08359ae949fa0076557c2d42fdda232d1e7b318432e6787795ca3e5
M298  d56bd6de3307284a8c5a135f5282ed1f1a3a793125ca056bb72f675e64f38cf8
M300  24964f0c5c8e8588715a98fc22a80d7b268b8e6abe683bd95772f51acecbebc8
```

The M300 inventory has fourteen entries; the predecessor inventory entry
counts are respectively `10,11,10,10,10,10,10,13`.  No failure occurred.

The proof and controlling referee passages were inspected, not just their
hashes.  They support the exact inputs used by M300:

- M274/M277: normalized two-channel formulas and exact MON/FOSD/literal-
  raw-atom firewalls, with CP/MS/FCL1 still open.
- M280/M283: the positive-prefactor CP owner-response identity, complete
  normalization, topology/endpoints, and statewise lag reflection.
- M285/M287: exact channel coefficients, triangle/double lift counts,
  three/four composition multiplicities without an extra `n`, repaired
  owner autocorrelation, and GOCI as an unresolved signed coefficient law.
- M295/M298: the collision-safe atom-summed channel-one disintegration and
  exact fixed-middle refutation, with the scalar beta shorthand restricted
  to the designated exterior/middle support.

No imported package proves MCLP, GOCI, OCI/CP, MS/FCL1, a spectral gap,
mixing, or a Terminal conclusion.

`AGENTS.md` names `references/experiments.md`, which does not exist.  The
actual skill-owned file
`.codex/skills/reversible-circuit-sampler/references/experiments.md` was
read.  This matches M300's disclosed documentation-path note and is not an
objection to its mathematics.
