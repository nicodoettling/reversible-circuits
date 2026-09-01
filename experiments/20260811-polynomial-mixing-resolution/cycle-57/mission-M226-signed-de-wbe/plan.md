# M226 plan: signed weighted boundary envelope

## Objective

Resolve, refute, or strictly reduce the exact signed weighted boundary-envelope lemma

    |S_Z+K_Z| <= C sqrt(ell)/k,

uniformly for odd `k>=3`, `2<=ell<=(3k-1)/2`, and
`Z=X_ell,Y_ell`, using M217/M222's audited literal three-block definitions.

## Source and immutable lock

- `HANDOFF.md`, `GOAL_SPEC.md`, the project skill, its sampling and experiment references
- M192/M195, M199/M207, M211/M215, and M217/M222

Verify every predecessor `SHA256SUMS` entry and checksum-file digest before use. Never edit a predecessor mission.

## Proof route

1. Rewrite `S_Z+K_Z` at coefficient level, retaining the two observables, all B/A kinds, both seams, the complementary X face, collisions, and exact normalizers already isolated by M217.
2. Identify cancellation between surviving-face coefficients and fragmentation-kernel coefficients before applying absolute values.
3. Treat fixed/small `ell` and `ell` comparable with `k` analytically. The audited macroscopic `qhat` tail may be used, but it does not solve fixed `ell`.
4. Use only compact exact formula checks at odd `k<=15` to falsify proposed signs or identities, never as universal evidence.
5. If WBE is false, prove an exact or asymptotic infinite counterexample. If it remains open, freeze a strict scalar reduction to the first coefficient/moment lemma, including a precise sufficiency proof and failed routes.

## Exclusions

No DV, conditional J2, PCR, downstream spectral-gap or mixing inference, or Terminal claim unless WBE itself is fully proved and the later implication is separately scoped. No broad scans.

## Deliverables

`checkpoint.md`, a proof or strict scalar-reduction note, a compact exact checker and machine-readable output, `report.md`, `freeze_manifest.md`, and `SHA256SUMS`, followed by a request for a fresh immutable audit.

