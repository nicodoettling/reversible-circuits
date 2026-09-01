# M154 Initial Checkpoint

Status: in progress.

The owned directory is

```text
experiments/20260811-polynomial-mixing-resolution/cycle-35/mission-M154-common-parity-hurwitz-transitivity/
```

The exact strong theorem under adversarial test is:

> For `d >= 5`, all length-`2d-2`, product-one factorizations by elements of `C_{d,s}` that generate `P_{d,s}` lie in one signed-Hurwitz orbit, or at minimum the aligned source/target factorizations arising from an M135 incidence matching do.

This is only a candidate.  At initialization, the precise meaning of “signed-Hurwitz” and whether simultaneous `P_{d,s}`-conjugation is included in the action still need to be reconciled from the predecessor artifacts.  The proof obligation is not discharged by equality of generated subgroups or factor conjugacy multisets.  Frozen M150 lifting calculations will be treated as unaccepted evidence until M153.

Immediate falsification targets are an additional Nielsen invariant, a braid-orbit split at exact small parameters, or a mismatch between the broad strong theorem and the narrower aligned M135 family.  Exact finite checks cannot prove the asymptotic theorem.

## Halfway checkpoint

The action is now fixed literally: no simultaneous conjugation is silently
included.  Three distinct quotients must be separated:

1. the literal diagonal braid orbit on framed factorizations;
2. the inner Nielsen quotient by simultaneous `P_(d,s)` conjugation;
3. the coarser absolute quotient by `S_d^s`, whose residual deck group is
   `S_d^s/P_(d,s) ~= F_2^(s-1)`.

### Proved structural step

For every product-one factorization `X=(x_1,...,x_m)` of any group, an
explicit braid of length `2(m-1)` sends `X` to its simultaneous conjugate by
`x_m`.  Conjugating this braid by inverse Hurwitz moves that carry `x_i`
unchanged to the final slot realizes simultaneous conjugation by every
original factor `x_i`.  Hence, if the factors generate `Gamma`, every inner
`Gamma`-conjugate of `X` is in its literal braid orbit.

Applied to accepted M141/M143, every nonempty `d>=5` M135 matching subfamily
generates `P_(d,s)`.  Literal simultaneous-braid equivalence is therefore
equivalent to equivalence modulo simultaneous `P_(d,s)` conjugation.  If one
instead works on the coordinatewise absolute quotient `Q_d=Z_d/S_d`, the
remaining exact condition is a parity voltage: a quotient braid mapping all
source classes to their target classes must have coordinate transporter
parities all equal.  The post-braid inner correction is then realizable by
the explicit loops above.

### Exact finite falsifiers and calibration

- At `d=3,s=2`, the `432` ordered pairs from distinct global classes split
  into exactly two literal diagonal-braid orbits of size `216`.  Common-
  parity conjugates are reachable; parity-mismatched coordinate conjugates
  are not.  This refutes the unqualified framed strong theorem at rank three
  and demonstrates that quotient transitivity cannot be conflated with
  literal realization.  No `d>=5` refutation is inferred.
- The quotient `Q_3` has degree `4`; its action image has order `12` and is
  `A_4`.  Each quotient action has two possible parity-voltage vectors in
  the exact framed action.
- At `d=4`, an independent Schreier--Sims reconstruction gives degree `120`,
  exact action-image order
  `20652142670561646642588549120=2^22*3^44*5`, subdegrees
  `[1,2,36,81]`, and `40` minimal blocks of size `3`.  Thus the proposed
  alternating quotient image is refuted at rank four.
- Those blocks are exactly the fibers of the factorwise exceptional quotient
  `S_4 -> S_4/V_4 ~= S_3`: the `120` global classes map to the `40` global
  classes of connected product-one length-six transposition words in `S_3`,
  with fiber size three.  Most deterministic M135 matching colors do not
  preserve this block relation; the obstruction is real but rank-four only,
  where M135 already uses singleton classes.
- At the tightly capped boundary `d=5`, quotient orbit closure has the
  accepted DPS size `8400`, and the seven positive Hurwitz generators act
  transitively and primitively.  The group was deliberately not closed;
  primitivity is an exact finite fact, not evidence sufficient for an
  alternating-image theorem.

### Current first unproved step

For `d>=5`, prove for the ordered source/target tuples attached to an M135
matching subfamily that some quotient braid maps every source global class
to its target global class and has diagonal parity voltage; also bound a
representative braid polynomially.  A general Conway--Parker or Hurwitz-space
completeness theorem would need its precise inner-versus-absolute convention,
stable range, class hypotheses, and word-length consequence checked before
use.  No such theorem is invoked here.
