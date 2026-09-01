# M245 plan: weighted adjacent-split profile variation (DV)

## Objective

Reconstruct and resolve exactly the `(DV)` hypothesis used by accepted missions
M192/M195, using the literal profile formulas and domain audited in M199/M207.
The desired output is either a fully quantified proof or an exact/asymptotic
counterexample.

## Source lock

- `HANDOFF.md`, `GOAL_SPEC.md`
- `.codex/skills/reversible-circuit-sampler/SKILL.md`
- `.codex/skills/reversible-circuit-sampler/references/sampling-problem.md`
- accepted/frozen M192, M195, M199, M207 artifacts
- M211 only for the pointwise `(IKBE-b)` refutation; it is not evidence about
  `(DV)` unless its literal formula specializes to the same aggregate.

## Scope and target

The mathematical target is only the weighted adjacent-split profile variation
bound `(DV)`.  The global fixed-length uniform identity-word law and local
`{3,4,5}` heat-bath kernel remain the project context, but this mission makes no
claim about DE, J2, PCR, the gap, mixing, or a terminal outcome.

## Work plan

1. Transcribe the exact DV statement, normalization, admissible parameter
   domain, kind split, seam conventions, and collision terms from M192/M195.
2. Derive the literal split-profile formulas independently from M199/M207 and
   reconcile any mismatch before attempting a bound.
3. Seek a direct adjacent-split telescoping or cyclic-averaging identity that
   controls the weighted aggregate rather than each pointwise kernel term.
4. Only after the formula is fixed, implement bounded exact rational checks for
   `k <= 9`, including empty/small/boundary domains and collision cases.
5. Freeze a theorem or refutation, checker, machine-readable results, report,
   fresh-audit request, and SHA-256 manifest.

## Expected failure modes

- Confusing DV with the refuted pointwise IKBE-b inequality.
- Dropping a seam/collision contribution or using the wrong cyclic
  normalization.
- Proving only a finite-range fact or a bound for one kind.
- Dividing by a vanishing profile mass at an exceptional parameter.

