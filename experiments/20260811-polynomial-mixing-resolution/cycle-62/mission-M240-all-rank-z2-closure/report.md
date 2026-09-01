# M240 final report: exact symbolic reduction to the DPS Initial-Defect Lemma

Date: 2026-08-13 UTC. Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Verdict

```text
PROMOTE A STRICT CONDITIONAL ALL-RANK REDUCTION.
DO NOT PROMOTE UNCONDITIONAL Z2 CLOSURE.
```

M240 does not close the all-rank DPS theorem.  It replaces the former broad
contour obligation by one exact coordinatewise DPS Initial-Defect Lemma
(IDL), then proves that IDL implies the full ordinary-edit M231 route-normal
formula by literal Hurwitz identities.

## Exact target and convention

For `d>=5`, a Cayley tree `T` on `[d]` rooted at leaf `d` adjacent to 1, and
ordinary odd inherited edit `i=2v-3` with `2<=v<=d-1`, set

```text
N=F_d(T,s_i pi_d)(0,d)^2,
A=F_(d+1)(T+{{1,d+1}},s_i pi_(d+1)).
```

Factors are displayed left to right; moves act chronologically by

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

The target is deterministic endpoint equality.  There is no distribution or
Markov kernel in this mission.

## Strongest proved statement

Let `P(v)=(v,p(v),...,1)`.  The M231 open condition is exactly that `P(v)`
is strictly decreasing.  M240 states IDL with every factor position fixed:

- initial cursor at position `2v-2`;
- one doubled slot `(2r-3,2r-2)` for every `v<r<d`;
- explicit direct-child versus common-parent-edge cases; and
- the four root-boundary positions `2d-3,...,2d`.

Assuming IDL, the accepted word

```text
Q(v,epsilon) B_d Q(v,epsilon)^-1
```

is correct for every open row, while the identity word is correct for every
closed row.  The proof uses:

```text
R_j R_(j+1)       (c,h,h)=(h,h,c),
R_j^-1 R_(j+1)^-1(c,h,h)=(chc,chc,c),
```

direct-child equalization

```text
(xy)(uy)(xy)=(ux)=(xn)(un)(xn),
```

and the accepted five-move carrier.  The only sign fact required is that a
direct larger child receives inverse sign; the alternating signs at absent
children are endpoint-correct but not necessary for this induction.

Conditional on IDL, the literal route length is exactly

```text
4(d-v-1)+5 <= 4d-7.
```

This is a one-endpoint conditional length, not a synchronized or congestion
bound.

## Exact unresolved lemma

IDL itself remains unresolved.  It asserts that the two edited plus-mirror
DPS closures have exactly the stated initial cursor, child-square, common
slot, and boundary factors when `P(v)` decreases, and are equal when it does
not.  DPS Proposition 3 supplies the hairy tree and DPS Lemma 2/Theorem 5
supply the valid stack closure, but none states this comparison of two edited
closures.  Accepted `d=5,6,7` passes calibrate IDL only finitely.

This is the first unproved step and should be the sole target of a next proof
lane.  Another finite rank cannot prove it.

## Symbolic checker

Command:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-62/mission-M240-all-rank-z2-closure/symbolic_identity_check.py
```

The checker generates no trees, runs no DPS closure, constructs no endpoints,
and performs no finite-rank census.  It verifies only generic transposition
identities on seven abstract labels:

```text
positive square transport       441
negative square transport       441
direct-child equalization      2520
terminal carrier               2520
disjoint-square both signs     5040
double-inverse boundary         210
single-inverse boundary         441
```

All pass.  The normalized check-count digest is
`7abdc0e2aaa785ccad996759bd40e341c5b513b709008c5ea87dbce2f7268993`.
Two consecutive result files have SHA-256
`b16858ec31079ef321d5e0130bc5289ba596dab83f905aa13beb4a491fa03f51`.
Python is 3.12.3; dependencies are empty and no seed is used.

## Fixed-edit and scope boundary

Ordinary `Z_2` edits are `1,3,...,2d-5`.  Internal even and final boundary
edits are not covered by IDL.  Their generic one- and two-inverse identities
are proved, but their arbitrary-rank DPS boundary shapes remain separate
obligations.  The accepted `d=5,6,7` artifacts cover them only finitely.

No result here proves every-color or arbitrary-representative routing,
synchronized matching compatibility, voltage correction, route recovery,
comparison congestion, a physical or original-chain gap, polynomial mixing,
or either Terminal.

## Audit request

Freeze M240 and commission a fresh clean-room referee.  The referee should
check the exact IDL position indexing and label translation, both square
transport signs, direct-child equalization, the `Q` induction, terminal
four-block, inverse-word chronology, conditional length, fixed-edit exclusion,
and the explicit refusal to treat finite `d=5,6,7` evidence as induction.

