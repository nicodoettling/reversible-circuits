# M142 plan: fresh audit of M139 two-edge-core reduction

Date: 2026-08-13 UTC.

## Objective

Independently referee the immutable M139 package in
`cycle-32/mission-M139-two-edge-core-curvature/`.  The audit target is the
auxiliary M113/M118 incidence-key coefficient profile `H_2[d,c]`, not the
uniform identity-word law and not a mixing theorem.

## Frozen inputs

The coordinator supplied hashes for M139's report, proof, checker, two raw
outputs, analytic certificate, manifest, and inventory.  The first action is
to verify those hashes and the complete `SHA256SUMS` inventory before using
the package.

## Claims tested

1. The common marked-pair characterization of a two-parallel-edge core and
   all binomial multiplicities in the marked connected recurrence.
2. The cycle-atom weight `q_a=a^(2a+1)/(a!)^2`, the unordered-pair factor
   `1/2`, and the coupled one-boundary `Phi` cavity.
3. The Lagrange identity `Psi_s=exp(s tau)/s`, including its `k=0` term, and
   the resulting `I_2(Q(X)^2)` core transform.
4. The beta substitution, its two cut exponents, and the exact `c=2,3`
   boundary formulas.
5. The claimed minimal shifted-ULC and `1+1/d` counterexamples, the mixed TP
   orientation obstruction, and the finite-only status of all positive
   scans.

## Independent checks

- Enumerate literal pairs of set partitions through six atoms, compute the
  bipartite two-core by leaf peeling, and compare it with the common-pair
  criterion.
- Implement a clean-room exact marked recurrence and compare it with literal
  weighted enumeration for all integer types through `d=5`; cap the recurrence
  at `d=16` only because the stated inverse-linear counterexample occurs there.
- Check the `q_a` translation, formal Lagrange coefficients, `Phi` integral
  coefficients, `I_2`, beta exponents, and boundary formulas with independent
  exact rational arithmetic.

Expected failure modes are a missing equal-size `1/2`, a wrong component
selection multiplicity, an omitted `k=0` term, swapped beta exponents, a
boundary factor of two, or an earlier counterexample than reported.  No work
will be spent on the unresolved universal log-concavity theorem.

## Reproducibility

The audit uses Python 3 standard-library exact arithmetic, is deterministic,
and has `seed=null`.  Artifacts are written only in this mission directory.
