# M287 Fresh Referee Plan: M285 Owner-Correlation Reduction

Date: 2026-08-14

## Objective and scope

Independently audit the frozen M285 artifact in
`cycle-79/mission-M285-owner-correlation-inequality`.  The only possible
promotion is a strict reduction from the owner-correlation inequalities to a
generalized owner-correlation inequality (GOCI), together with an exact
obstruction to the naive positive-semidefinite route.  This referee does not
claim OCI, CP, OS+, MS, FCL1, FD, a spectral gap, polynomial mixing, or a
Terminal outcome.

## Target and conventions

The ambient target remains the uniform fixed-length bridge law on
`Omega(N,m)`, with the lazy exact same-product `{3,4,5}` block heat-bath kernel
defined in `GOAL_SPEC.md`.  The audited calculation concerns odd auxiliary
rank `k >= 3`, the rooted-owner/cyclic-composition representation used by
M280/M283, and only admissible lags declared in the frozen artifact.  Every
normalization, owner interval, boundary case, and exceptional size-2 deletion
will be reconstructed from definitions before comparison with M285.

## Claims to test

1. Frozen-artifact integrity: exact inventory and top-level
   `SHA256SUMS` digest
   `54eed4258da59ee1b8491815f182f05ac7c57c809e0f002bc2a2a79666098ac8`.
2. The M280/M283/M91/M94/M261/M264 dependencies are quoted with their exact
   status and hypotheses.
3. The `beta_1` and `beta_2` product coefficients and all normalizations follow
   from the positive cyclic-composition multiplicities: three triangle
   placements and four double placements, with no extra factor of `n`.
4. The owner interval formula, rooted-owner autocorrelation decomposition,
   delta log-convexity, and the size-2 deletion at lag zero are exact.
5. GOCI is equivalent to the intended OCI inequalities on precisely the
   admissible lags, and is a strict/narrower formulation only in the sense
   stated by M285.
6. At `k=3`, channel 2 has an exact non-PSD quadratic witness, refuting the
   proposed universal PSD proof route without refuting GOCI itself.

## Method

- Verify the immutable tree and hashes before reading its substantive proof.
- Read each cited predecessor ledger directly and reconstruct the dependency
  chain rather than trusting M285's summary.
- Derive coefficients algebraically on paper/in referee notes.
- If useful, write one compact checker in this directory.  It must not import
  M285 code and may only validate exact conventions or a finite falsifier.
- Freeze this directory with `report.md`, numbered objections (if any), exact
  inventory, and `SHA256SUMS`.  Verdict is `ACCEPT` only if every material
  claim survives; otherwise `REJECT`.

## Expected failure modes

- hidden ordered/unordered or rooted/unrooted multiplicity factor;
- an accidental extra cyclic factor `n`;
- using delta log-convexity outside its valid index range;
- deleting the size-2 term at nonzero lag;
- claiming GOCI on nonadmissible lags or claiming it proves positivity;
- mistaking a non-PSD quadratic representation for a counterexample to GOCI.

