# M143 plan: fresh referee of frozen M141

Date: 2026-08-13 UTC.

## Objective

Independently referee immutable M141's multisource common-parity theorem.
Verify provenance before use, audit every universal proof step and exceptional
rank, rerun a compact clean-room bounded checker, and issue an explicit
`ACCEPT` or `REJECT` without attempting common-braid realization.

## Frozen inputs

The assigned hashes correspond to the actual frozen filenames
`report.md`, `multisource_subgroup_theorem.md`,
`multisource_subgroup_audit.py`, `results.json`, `freeze_manifest.md`, and
`SHA256SUMS`.  All six were verified before substantive audit.

## Audit obligations

1. Distinguish arbitrary matchings from perfect matching colors and verify
   distinct source/target global-orbit endpoints for arbitrary representatives.
2. Check the exact use of M135/M137's graph-versus-parity dichotomy.
3. Reprove the passage from pair projections of `Gamma` to pair projections
   of `N=Gamma intersect A_d^s`.
4. Reprove the pairwise-full simple-power lemma, including kernel normality,
   the graph alternative, and the `s=1` case.
5. Audit ranks `d=5,6`, recovery of the odd coset, and exceptions `d=3,4`.
6. Confirm that generated-subgroup equality is claimed only as necessary,
   never sufficient, for simultaneous signed-braid realization.
7. Run a bounded independent checker, preserve machine-readable output, and
   report hashes, manifest, and repository hygiene.

## Expected failure modes

- Confusing one chosen perfect color with an arbitrary matching.
- Assuming M135's pair theorem only for canonical representatives.
- Treating `Gamma intersect A_d^s` as automatically pairwise-full without a
  parity-lifting argument.
- Using an invalid induction kernel-normality argument.
- Missing the `S_6` outer-automorphism or nonsimple `A_4` exception.
- Inferring a common braid from equality of aligned generated subgroups.

