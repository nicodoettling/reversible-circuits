# M163 Plan: quotient stabilizer voltage

## Objective

Resolve the exact stabilizer-voltage interface left by accepted M154/M158.
For an ordered M135 matching subfamily in `Q_d^s`, define the voltage image
of its braid point stabilizer in `F_2^s/Delta`.  Prove that all voltages of
braids routing one fixed ordered quotient tuple to another form one coset of
this subgroup, and characterize when that coset contains zero.

## Scope

- Target: a Hurwitz action-orbit lifting criterion, not a sampler or spectral
  gap.
- Literal signed-Hurwitz action, inner `P_(d,s)` quotient, and absolute
  `S_d^s` quotient remain distinct.
- Inner conjugation by `P_(d,s)` has zero relative voltage and must not be
  counted as a nonzero stabilizer voltage.
- Polynomial quotient word length and short inner-transporter length remain
  separate from the qualitative stabilizer-voltage question.
- M154 remains immutable. All new artifacts are confined to this directory.

## Work packages

1. Reconcile frozen accepted M135/M137, M141/M143, M146/M148, M150/M153,
   and M154/M158 at their exact scopes.
2. Define the voltage cocycle on the action groupoid of the free
   `S_d^s`-cover over ordered quotient tuples. Prove composition, inverse,
   stabilizer-subgroup, and endpoint-coset laws.
3. Characterize stabilizer voltage using literal tuple stabilizers and
   explicit braid loops. State precisely why generated inner-conjugation
   loops have zero class in `F_2^s/Delta`.
4. Exhaust `d=3`; audit the accepted `d=4` witness and exceptional block.
   Cap `d=5` at widths at most three and bounded orbit/stabilizer operations.
5. Seek either a universal `d>=5` full-voltage theorem, a counterexample, or
   a strict smaller lemma. Do not close a broad degree-8400 group.
6. Freeze a nine-field report, proof/checker/raw output, hashes, and manifest
   for independent review.

## Candidate verdicts

- `promote`: a self-contained full-voltage theorem or strict stabilizer-
  voltage reduction with a nontrivial proved step.
- `reject`: an exact nonzero endpoint coset with deficient stabilizer voltage
  that obstructs an M135 matched tuple.
- `inconclusive`: only after isolating the first exact unresolved lemma and
  preserving all finite negative findings.

