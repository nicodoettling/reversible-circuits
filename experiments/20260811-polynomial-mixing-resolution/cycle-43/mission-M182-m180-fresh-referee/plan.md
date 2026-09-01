# M182 Plan — Fresh Referee of Immutable M180

## Objective

Independently audit the frozen M180 fixed-cell boundary-response reduction and
issue an explicit `ACCEPT` or `REJECT` verdict.  M180 is immutable; all work is
confined to this directory.

## Mathematical target

The audited target is the boundary-response quantity

```text
eta(B_k) = 2 sum_{j=1}^2 alpha_j Cov_{mu_j}(B_k,sigma_j),
```

for the nonlazy cyclic rank-two coordinate kernel and the two fixed sources
`A=(0,k,2k)` and `B=(0,1)(k,2k)`, with `n=3k` and odd `k`.  This is not the
global identity-word heat-bath target.

## Frozen input

`cycle-42/mission-M180-fixed-cell-boundary-response/`, verified against its
own `SHA256SUMS` and stated top-level hashes before any conclusion is drawn.
No M180 file will be edited or imported by the clean-room checker.

## Claims to audit

1. The second ratio coefficient `22/3`.
2. The exact decomposition `B=2nQ-7/2-2I_D+R` and a uniform bound on `R`.
3. Raw signed component-coefficient normalization and moment identities.
4. The large-component contribution is `O(1/n)`.
5. The exact `KW` identity and equivalence with the bounded-incidence response
   (`BIR`).
6. Literal independent calibration at `k=3,5` only.

## Method

- Re-derive all algebra from the frozen definitions, recording a clean-room
  proof rather than copying M180 prose.
- Write an independent standard-library checker that does not import M180
  code and performs only exact `k=3,5` enumeration.
- Preserve the signed two-channel/kind combination; do not attempt SCBR and do
  not split channels by absolute value.
- Record numbered objections, including nonmaterial qualifications.

## Expected failure modes

- A normalization mismatch between raw source counts and normalized signed
  coefficients.
- A lost factor in passing from ordered kernel pairs to boundary incidences.
- An asymptotic expansion insufficiently uniform for the claimed remainder or
  tail.
- A finite check being misreported as an asymptotic proof.

## Deliverables

`checkpoint.md`, a clean-room derivation, a compact checker and JSON output, a
nine-field `report.md`, numbered objections, and a frozen checksum manifest.

## Verdict discipline

`ACCEPT` means every assigned M180 claim is independently verified, possibly
with explicitly numbered nonmaterial exposition qualifications.  `REJECT`
means at least one material claim fails.  No spectral-gap or terminal project
claim is authorized.
