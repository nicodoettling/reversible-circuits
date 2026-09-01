# M120 Plan: Local Unicycle-Incidence Gap

## Objective

For the exact weighted connected-unicycle key chain `A_d` reduced in M113 and
fresh-audited in M118, prove an inverse-polynomial spectral-gap lower bound in
`d`, or exhibit a rigorous asymptotic obstruction/counterfamily with stationary
mass and boundary-flow estimates.

## Declared target and kernel

The target is the M113 raw-incidence law on realizable keys
`kappa=(j,p,Q_L,Q_R)`, proportional to the exact incidence-cell cardinality.
The kernel is the holding cut-refresh chain `A_d`: choose a current incidence,
hold with probability `1/2`, and otherwise perform the exact adjacent
coagulation/fragmentation compatibility update with its M113 overlap flow.
Before claiming any estimate I will transcribe and independently check the
normalization, all cell weights, and boundary cases (especially `d=2`).

## Claims to test

1. A projection by permutation cycle type and/or unicycle-incidence shape has
   inverse-polynomial projection gap.
2. Conditional fibers at fixed projection coordinate have polynomial
   expansion using a non-hub forest-basis exchange comparison.
3. If those fail, aggregate singleton-split/reverse flow supplies a polynomial
   drift/minorization away from balanced and hub-like traps.
4. Candidate balanced, hub, and highly unbalanced cuts do not have
   superpolynomial conductance—or furnish an explicit obstruction if they do.

## Method

- Audit M113/M118 formulas and reconstruct `A_d` independently.
- Enumerate exact states/flows for `d<=5` when feasible; report finite facts
  only as finite.
- Compute exact stationary masses, conductances of named statistic cuts, and
  spectra for the smallest cases.
- Derive symbolic aggregate flow identities/inequalities, keeping all
  factorial and component-size weights and the `1/2` holding.
- Stress-test constants on `d=2`, balanced shapes, stars/hubs, paths, and
  singleton-rich shapes.
- Prefer projection/restriction or canonical-path families dispersed over
  non-hub intermediates; do not use the refuted natural Lorentzian polynomial
  or a pointwise minimum-edge argument.

## Falsification and stopping rules

A theorem claim must survive exact boundary cases and an independent
reconstruction. A negative result must name a cut family and prove both
stationary mass and boundary flow asymptotics. If neither closes, freeze the
narrowest proved reduction and state the first open lemma.

## Reproducibility

Record exact commands, Python version, repository commit, deterministic seeds
(if randomness is used), machine-readable JSON, and SHA-256 hashes. Produce a
halfway checkpoint and a final nine-field report. Edit only this directory.
