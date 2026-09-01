# M300 dependency audit

Date: 2026-08-14 UTC.

All eight required frozen inventories were checked from inside their own
mission directories with `sha256sum -c SHA256SUMS`; every listed payload
reported `OK`. Their checksum-file digests are:

```text
M274  c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e
M277  c419b7c95e7c6fe4086d1098d6f0578445a1c3af700cabe4e90cf90d7c39d890
M280  60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9
M283  156fa5207e088f38ae71b69e48332a8a708bae8f03f1447c77e9710128572cdf
M285  54eed4258da59ee1b8491815f182f05ac7c57c809e0f002bc2a2a79666098ac8
M287  0298ecf0d0f3ca2970f4a817469a01e247b125b4b0211eb748b752146e73fc35
M295  42fa1c38b08359ae949fa0076557c2d42fdda232d1e7b318432e6787795ca3e5
M298  d56bd6de3307284a8c5a135f5282ed1f1a3a793125ca056bb72f675e64f38cf8
```

## Accepted imported statements

- M274/M277: the normalized two-channel formulas, PCS--MS equivalence,
  and the exact refutations of conditioned MON/FOSD and literal raw-atom
  positivity at their stated scopes.
- M280/M283: `CP_j=Lambda_n/R_n eta_j(F_ell)`, complete normalization,
  owner response, topology retention, and lag reflection.
- M285/M287: exact `beta_1,beta_2`, three/four composition multiplicities,
  the repaired statewise owner-autocorrelation response, and the fact that
  GOCI remains a signed coefficient theorem; signed PSD dominance is
  refuted only in the stated channel-two sense.
- M295/M298: the atom-summed fixed-middle disintegration and exact refutation
  of `FMCP_1`; the scalar `beta_1(ef)` shorthand is accepted only with its
  designated exterior/middle qualifier.

No predecessor sign, GOCI/OCI, CP, OS+, MS, FCL1, gap, mixing, or Terminal
claim is imported as proved.

## Source-path discrepancy

`AGENTS.md` names `references/experiments.md`, which is absent. The actual
file is
`.codex/skills/reversible-circuit-sampler/references/experiments.md`, the
path named by the project skill; that file was read. This is a documentation
path discrepancy only and does not alter a mathematical claim.
