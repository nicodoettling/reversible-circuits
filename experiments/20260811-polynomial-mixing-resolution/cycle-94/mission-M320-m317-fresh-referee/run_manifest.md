# M320 run manifest

Date: 2026-08-14 UTC

## Role and scope

- role: genuinely fresh immutable referee for frozen M317 only
- owned write directory:
  `experiments/20260811-polynomial-mixing-resolution/cycle-94/mission-M320-m317-fresh-referee`
- target distribution: unchanged global fixed-length uniform identity-bridge
  target for the lazy exact same-product `{3,4,5}` heat-bath chain; this audit
  addresses only the finite-action residual agreement reduction
- convention: M317's chronological signed-Hurwitz right action

## Inputs

- frozen M317 top requested and observed:
  `88a2480ec93ee6b3deb2d3e2e14b9a49a3f7e6ea71dca59997424c1356255245`
- cited frozen missions: M135, M137, M296, M299, M301, M304, M306,
  M309, M312, M315
- project safeguards: `AGENTS.md` and the
  `reversible-circuit-sampler` skill

## Method

Read-only SHA-256 inventory verification followed by an independent finite-set
action proof audit.  No stochastic procedure, seed, nonstandard dependency,
external source, theorem search, or computational rank guard was used.

## Reproducibility

Run `sha256sum SHA256SUMS`, `wc -l SHA256SUMS`, and
`sha256sum -c SHA256SUMS` in M317 and each cited predecessor directory.  The
observed top digests and row counts are recorded in `dependency_audit.md`.
The audit derivations are recorded in `proof_audit.md`.
