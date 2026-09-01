# M126 plan: fresh referee of M122

Date: 2026-08-12.

## Objective

Independently referee the frozen M122 rooted-product local-comparison mission.
The audit targets the universal DPS star-contour identity, its exact Hurwitz
length claims, the two square-prefix conjugation routes, source recovery,
root-refresh capacity/load accounting, and the deliberately limited scope of
the result.

## Immutable source

Audit only the frozen directory
`cycle-25/mission-M122-rooted-product-local-comparison`.  Verify the five
coordinator-supplied hashes before relying on it, and do not edit it.

## Method

1. Read the repository source of truth, project skill, M112 DPS source, and
   M119 fresh audit.
2. Re-derive every universal formula under the stated left-to-right product
   and right-Hurwitz convention.
3. Write a compact independent checker for small `d`, with machine-readable
   output.  Its role is convention checking and counterexample search only.
4. Audit source recovery including deleted self-loops; recompute the capacity
   factor `d` and single-demand load.
5. Check artifacts, nine-field reporting, manifest, hashes, cache hygiene,
   and scope.  Issue `ACCEPT` or `REJECT` with numbered objections.

## Target and claim labels

The ambient target remains the uniform fixed-length identity bridge law from
`GOAL_SPEC.md`, but M122 proves only a rooted ideal-edge/local-route lemma.
Universal algebraic statements require proof; finite checks are `exact finite`
and cannot establish an asymptotic congestion or spectral-gap result.

## Expected failure modes

- an off-by-one in the DPS contour or `2d-4` Hurwitz count;
- confusing suffix conjugation by the DPS block with conjugation by its root;
- applying the `2L-1` route to disjoint endpoints;
- losing source information after a root refresh deletes self-loops;
- omitting proposal probabilities in the capacity/load normalization;
- silently promoting one ideal-edge family to an all-edge gap comparison.

