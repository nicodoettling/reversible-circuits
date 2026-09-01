# M175 Plan — Relative-orientation routing

## Objective

Continue the accepted quotient/monodromy frontier by deriving one exact local-generator description of the relative-orientation voltage group on an accepted matching subfamily, or else a rigorous finite combinatorial reduction/obstruction.

## Scope and labels

- Target object: the qualitative connectivity/voltage obstruction in the relative-orientation cover of a fixed physical quotient fiber; this is not a sampler or mixing-time claim.
- Keep fixed physical endpoints and the endpoint-lift coboundary caveat explicit.
- Use only accepted predecessor definitions and claims after checking their artifacts.
- Calibrate only on minimal `d=3,4` cases.
- Do not enumerate a `d=5` quotient orbit, claim polynomial word length, claim a spectral gap, or claim Terminal.

## Work plan

1. Read the project source of truth and frozen predecessor missions M135/M137, M141/M143, M146/M148, M154/M158, M163/M164, and M169/M172.
2. Normalize notation for the root-monodromy group `K_mon`, pure subgroup `P`, and parity image `V_stab` at fixed physical endpoints.
3. Derive the parity vector of an elementary accepted local root-monodromy move and identify the generated binary subspace.
4. Attempt a uniform zero-coset/full-voltage criterion; if unavailable, prove an exact cycle-space or incidence-matrix reduction and state the first unresolved realization lemma.
5. Check boundary/minimal cases symbolically and write a halfway checkpoint.
6. Produce a compact proof/checker, nine-field final report, manifest, checksums, and frozen hygiene record; request fresh audit.

## Expected failure modes

- Confusing arbitrary endpoint section changes with a physical zero-voltage statement.
- Treating a marked-root hit as sufficient without tracking the sign of the root permutation.
- Assuming every formal local parity generator is realized by an accepted quotient loop.
- Promoting a finite `d=3,4` calibration to an all-`d` theorem.
- Silently replacing the physical quotient stabilizer by a larger abstract braid stabilizer.

