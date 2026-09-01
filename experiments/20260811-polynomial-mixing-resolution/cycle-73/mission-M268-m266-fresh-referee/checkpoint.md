# M268 Checkpoint

## Status

Halfway audit complete.  No material defect has been found, but the final
verdict remains pending the independent checker replay and frozen report.

## Completed setup

- Read the repository source-of-truth documents and the reversible-circuit-sampler skill/reference files.
- Fixed the audit scope to the frozen M266 assembly and its cited accepted dependencies.
- Fixed the theorem boundary: this audit can at most certify PCS in the stated odd near-minimal regime; FD-bound/minority-sign and all downstream FCL1/gap/mixing claims remain outside the conclusion.
- Recomputed M266's ten-file inventory: every entry passes.
- Recomputed all fourteen direct predecessor inventories and their checksum-file digests: every digest agrees with M266's dependency table.
- Recomputed the six delicate transitive inventories M174/M178, M180/M182,
  and M186/M189: every entry passes.
- Recomputed M166's historical `freeze_manifest.md` digest as
  `a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897f28dfbb6185e30498`,
  confirming M259/M266's correction.
- Independently traced the exact source interfaces.  The M186 summation by
  parts contains the singleton, both `m` endpoints, and precisely the
  `d=2,...,m-1` first differences paired with WPCR's `d^-2` weights.  The
  M174 target-mass identity makes the final Delta/PCS statement a genuine
  two-way equivalence, not a one-way implication.

## Next checks

- Run and inspect the no-import exact checker.
- Freeze the line-by-line proof audit, nine-field report, manifest, and
  complete checksum inventory.
