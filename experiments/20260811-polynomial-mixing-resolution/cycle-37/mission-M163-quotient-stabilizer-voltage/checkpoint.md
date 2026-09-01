# M163 Initial Checkpoint

Status: halfway checkpoint completed; freezing followed after the bounded
finite audit.

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-37/mission-M163-quotient-stabilizer-voltage/
```

The candidate structure is the action groupoid of the literal braid group on
the free `S_d^s`-cover of ordered quotient tuples. For a quotient tuple `a`,
the voltage image of its braid stabilizer should be a subgroup

```text
V_stab(a) <= F_2^s/Delta.
```

For a fixed routed endpoint pair `(a,b)`, the voltage set is exactly one
coset of `V_stab`, with the chronological convention fixed in `proof.md`.
Zero voltage is adjustable exactly when that coset contains zero. The
groupoid cocycle, stabilizer homomorphism, endpoint-coset identity, and
section-change formula are now proved.

Exact halfway finite findings:

- `d=3`: all `4+16+64+256` ordered quotient tuples of widths one through
  four have trivial stabilizer voltage. In particular every ordered distinct
  matching tuple has `V_stab=0`.
- accepted `d=4` witness: both width-two endpoint stabilizers have trivial
  voltage. The source and target are in different quotient-tuple orbits by
  the accepted `S_4/V_4` block invariant, so there is no endpoint voltage
  coset to adjust.
- a preliminary `d=5` Schreier--Sims stabilizer attempt did not finish within
  its bounded phase and was interrupted without a result. It is not used.

Immediate safeguards:

- simultaneous conjugation by `P_(d,s)` represents the zero class;
- the stabilizer subgroup is section-independent, but an endpoint voltage
  coset is translated by arbitrary independent changes of its two endpoint
  lifts.  Thus zero-membership is stated only for fixed physical endpoints
  (and is preserved by the matched simultaneous relabelings used in M135);
- finite computations are falsifiers/calibration only;
- no quotient routing existence, polynomial word length, short transporter,
  gap, or terminal claim is presumed.

Verdict at checkpoint: keep the abstract coset theorem and exact finite
obstructions; leave the universal `d>=5` full-voltage claim unresolved.
