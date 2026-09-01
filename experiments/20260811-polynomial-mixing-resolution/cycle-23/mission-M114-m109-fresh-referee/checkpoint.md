# M114 checkpoint

## Initial source and freeze gate

Required project sources read completely: `HANDOFF.md`, `GOAL_SPEC.md`, the
project sampler skill, `sampling-problem.md`, and `experiments.md`.

The frozen M109 directory contains no unlisted scratch file.  Direct hashes
match its `SHA256SUMS` manifest:

- `report.md`: `f68c3211d404d1cf045b101bdea26ccf105f38f708d5bbe0d64f9fb1aa1c6575`
- `excursion_reduction.md`: `6abb460e61592761bcb9be28095e578e6660138f67bb1ed110772fdca750062b`
- `boundary_exact.py`: `5832dedd8ba79d51c93a8e2b2c4cd721851fb73e9e1a9df750c5d6c0296662e3`
- `boundary_exact.json`: `934fd0d4f87cdb050b5d39c56352ad3d4793a01a43ab671f61f0d1118155fb55`
- `SHA256SUMS`: `65d0173dbc27df08c6ff653cdbe9e0619f41798a49ec025f3f92a0f0fbc35106`

Mathematical audit is in progress.  No claim is accepted at this checkpoint.

## Substantive halfway checkpoint

The independent `independent_exact_audit.py` now passes.  It contains no
import statement and reads no predecessor artifact.  Its exact checks include:

- the full attachment normalization with every `j=1,...,k` live rank retained,
  fresh uniformity, strict `P` descent, and strict `L` descent;
- literal-versus-grouped canonical basin energy at three small contexts;
- the `beta_e<=k` normalization and decisive boundary cases in `L=0,1,2`;
- the four-support `L=2` table, exceptional path mass, actual/augmented reset
  energies, both live groups, every live attachment rank, and the complete
  descendant charge at five selected contexts;
- an exact symbolic identity for the derivative-cleared quartic `N_s` and for
  both endpoint slack formulas;
- all coefficients in the three asymptotic Bernstein certificates and all 35
  coefficients in the seven finite `s=3,...,9` certificates; and
- all four full-resolvent calibration fractions.

A post-run, read-only comparison shows exact numerator/denominator equality
with every corresponding frozen M109 calibration and Bernstein coefficient.

One boundary wording nuance is retained for the final report: when `s=3` and
`L=2`, the nominal `(k,t)=(2,s-1)=(2,2)` child has rank one and is inactive.
The M109 envelope remains correct because its added charge is exactly zero
(`v=1`).  This is not a material mathematical objection.

## Final checkpoint

Verdict: **ACCEPT with zero material numbered objections**.  The `s=3`
inactive zero-charge child is recorded as nonmaterial correction NM-1.  The
exact rerun passes; JSON parses; there are no imports or cache artifacts in
the final checker directory.  Global all-`L` contraction and every gap,
mixing, and project-terminal claim remain unresolved.
