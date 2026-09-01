# M164 Plan: fresh immutable referee of M163

## Objective and target

Independently audit frozen M163's stabilizer-voltage coset theorem for the
literal diagonal signed-Hurwitz action on ordered tuples in
`Q_d=Z_d/S_d`.  The target is an action-orbit lifting criterion, not a
sampler, spectral-gap bound, or terminal conclusion.

## Frozen inputs

Verify the coordinator-supplied SHA-256 values for M163's report, proof,
checker, raw results, manifest, and checksum file before reading them.  Treat
M163 and accepted M154/M158 as immutable.  Do not import or execute M163's
checker.

## Claims tested

1. The deck-transporter parity is a groupoid cocycle in
   `W_s=F_2^s/Delta` under the stated left-action convention.
2. Its image on a quotient-tuple stabilizer is a subgroup, and the voltages
   of all routes from one fixed quotient tuple to another form the correctly
   oriented affine coset.
3. The zero criterion has the stated section/base-lift caveat.
4. M154 inner `P_(d,s)` loops have zero relative parity voltage.
5. Clean-room finite reconstruction gives trivial stabilizer voltage for all
   `d=3` quotient tuples of widths one through four, and reproduces the
   accepted `d=4` witness/block facts.

## Independent computation

Implement permutation composition, relabeling, Hurwitz moves, quotient
canonicalization, transporter parity, augmented tuple-orbit closure, and the
`S_4/V_4` perfect-matching projection from scratch.  Enumerate only `d=3`
and `d=4`; use no stochastic branch (`seed=null`).

Expected failure modes include an incorrect transporter order, inverse-edge
voltage mismatch, nonfree relabeling, an endpoint-coset orientation error,
a nontrivial low-rank stabilizer voltage, or disagreement with the accepted
rank-four block witness.  Any such discrepancy triggers `REJECT`.

## Scope guard

No `d=5` group closure, quotient-routing existence, polynomial braid length,
short inner correction, physical-sector gap, original `{3,4,5}` heat-bath
gap, Terminal A, or Terminal B claim is in scope.
