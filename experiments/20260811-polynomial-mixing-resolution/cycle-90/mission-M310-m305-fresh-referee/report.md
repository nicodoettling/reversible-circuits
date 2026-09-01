# M310 fresh immutable referee report

Date: 2026-08-14 UTC.

## Verdict

```text
ACCEPT M305 AT ITS FROZEN REDUCTION-ONLY SCOPE.
MATERIAL OBJECTIONS: ZERO.
NONMATERIAL CLARIFICATIONS: TWO.
```

The exact 11-payload M305 gate passes with top digest
`4e81c82223820cde35a8eecb7e8eb837733c5cd97ccb0375ae44d2a012392b46`.
Every payload row and top digest in all 15 cited predecessor inventories also
passes.

Independent reconstruction accepts:

- exact deterministic `CBPV=>SOCL`, from profile bounds `32`, `4d`, and
  `4min(d,e)` after complete signed grouping;
- all-rank `sum_s|Delta(p_s-q_s)|=O(1/k)`, including `k=3`, the low/high
  junction, and the terminal endpoint;
- the abstract two-point refutation of a generic scalar-BV multiplier
  shortcut, without treating it as an owner-law counterexample;
- the exact two-channel marked Abel identity, including raw lifts, `1/3` and
  `1/4` representation factors, actual incidences, phases, seams, and
  `D_(k-1)=0`;
- the finite-only `k=11` replay, which matches all frozen semantic fields.

Two clarifications are nonmaterial: deleting a zero-profile coefficient atom
is response-equivalent but not measure-norm-equivalent; and the scalar
low/high jump includes the adjacent `p` difference as well as `q_h`, all of
order `k^-3/2`.

```text
CBPV => SOCL                                     proved exact implication
scalar Borel split BV                            proved all-rank
generic scalar-BV multiplier shortcut           refuted abstractly
marked Abel identity                            proved exact
CMPAD / reduced CBPV / SOCL                     unresolved
BODT/DOR/PBV/FD/FCL1/gap/mixing/Terminals        unresolved
```

Final action: retain M305 and pursue only the fully combined marked-profile
cancellation in a later mission.

