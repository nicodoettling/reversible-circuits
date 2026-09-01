# M292 Fresh Referee Plan

## Role and scope

Act as a genuinely fresh immutable referee of frozen mission M289.  Audit only
the claimed channel-two embedding bounded-variation estimate (CEBV), with no
inference to CIBV, DOR, PBV, FD, FCL1, a spectral gap, mixing, or a terminal
claim.

## Target and convention

The target under audit is the exact fixed-length uniform transposition
identity-bridge law used by the frozen proof package.  The referee will first
recover the package's permutation/product and index conventions verbatim, then
check that every reconstructed formula uses the same convention.

## Tasks

1. Verify the frozen M289 top `SHA256SUMS` digest
   `327176968d69eb447ff862354eb566ed00cfd2c56b2e77079231bcc077f93680`,
   its exact inventory, and all cited predecessor artifacts.
2. Reconstruct independently the raw B/A support-pair masses and their
   subprobability normalizer; audit the `E_D`/`E_k` seam maps.
3. Audit Lemma 1, including endpoints, tails, the constant-profile case, and
   all constants actually needed by the conclusion.
4. Audit generalized `Z_(M,r)` stabilization, including `r=1,2`, cutoff,
   reflection, untouched-component BV, triangular-cross BV, and the `k=3`
   boundary.
5. After formulas are fixed, implement one compact checker without importing
   any M289 code and record machine-readable output.
6. Decide ACCEPT or REJECT with numbered objections, exact hashes, repository
   hygiene, and a strict statement of what CEBV alone does and does not imply.

## Expected failure modes

- A probability mass is silently conditioned or normalized twice.
- A seam-map endpoint is missing or double-counted.
- A BV lemma assumes zero boundary values but is applied to a constant or
  truncated profile.
- `Z_(M,r)` asymptotics omit `r=1,2`, reflection, or a cutoff boundary.
- A finite `k=3` exception is folded into an asymptotic statement without a
  direct check.
- Total variation of the constructed signed/subprobability object is mistaken
  for the exact CEBV norm.

## Reproducibility

Record the repository commit, exact commands, Python version, source and
checker hashes, and a fresh-reference implementation independent of M289.
