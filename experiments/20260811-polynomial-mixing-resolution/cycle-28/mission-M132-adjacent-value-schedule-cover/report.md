# M132 final report: adjacent-value schedule cover

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and exact scope

```text
FINAL VERDICT: KEEP AS A SCOPED METADATA OBSTRUCTION.
REFUTED at d=4: one schedule per tested polynomial two-label contour key.
PROVED: schedule-conflict graph is a necessary coloring obstruction.
EXACT d=3: conflict chromatic number 3, true minimum schedule cover 5.
UNRESOLVED: ADJACENT-VALUE POLYNOMIAL SCHEDULE COVER.
```

The strongest reusable negative is a hand-checkable pair of `S_4` sources
which have identical tested local/scalar contour metadata but cannot share
any signed braid schedule. This rules out the proposed metadata selector; it
does **not** prove a superpolynomial schedule lower bound. Complete contour
histories have superpolynomial raw cardinality, so the surviving proof needs a
new polynomial compression/coloring plus simultaneous-realization theorem.

```text
candidate                  | fixed schedules selected by two-label contour metadata
claimed target             | uniform physical minimal identity sector Z_d
identity ok                | exact d=3,4; DPS and Hurwitz preserve identity generally
crosses Hurwitz components | not applicable; one connected minimal identity orbit
exact diagnostics          | DPS roots, local keys, pair subgroups, d=3 action/conflict
verdict                    | reject named key; general polynomial cover unresolved
```

This mission proves no UST basis-exchange route, all-edge rooted-product
comparison, physical gap, arbitrary-product `Gamma_0` result, original lazy
exact `{3,4,5}` heat-bath gap, Terminal A, or Terminal B.

## Field 2 — target, convention, kernel, and dependencies

For `d>=2`, the auxiliary target is uniform on

```text
Z_d={(t_1,...,t_(2d-2)):t_1...t_(2d-2)=id,
                              support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors multiplied
left-to-right. Signed right-Hurwitz moves are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

The associated half-lazy physical kernel, not bounded spectrally here, is

```text
P_(0,d)=I/2+[1/(4(2d-3))] sum_j (R_j+R_j^(-1)).
```

Accepted dependencies are:

- M112/M119: rooted DPS is exactly
  `Cayley_d x S_(2d-2)` with `d` roots over every physical word;
- M122/M126: fixed square-prefix routes can be linear/quadratic and scheduled
  prefix inversion is source-recoverable, but total descriptor load is open;
- M127/M130: adjacent-value swapping descends to an involution `tau_i` on
  `Z_d`, one global fixed braid is refuted, and coordinate-pair generated
  subgroups are invariant under a common schedule.

The checker independently reimplements the accepted `+` DPS closure and
imports no predecessor experiment module or result file. No new literature
theorem is used.

## Field 3 — polynomial contour metadata is insufficient

Define `D_i(w)` from the canonical lexicographically first rooted DPS
preimage by retaining, for the two swapped labels:

- exact ordered physical factors;
- hairy black/white endpoints;
- oriented first/second black face endpoints;
- both directed contour traversal positions; and
- closure counts, first/last closure steps, and distance-three closure step.

This is genuinely polynomial-cardinality. With

```text
E=binom(d,2), B=(2d-1)(2d-2), S=(d-2)(2d-2),
```

a conservative bound is

```text
|range(D_i)| <= E^2[d(d-1)]^4 B^4(S+1)^10 = O(d^40).
```

Nevertheless, at `d=4,i=1`, let

```text
x =((12),(13),(13),(12),(34),(34)),
y =((12),(13),(13),(34),(12),(34)),

x'=((12),(23),(13),(24),(23),(34)),
y'=((12),(23),(13),(34),(24),(34)).
```

The exact DPS certificates share

```text
T={(1,2),(1,3),(2,4)},
pi_x=(3,2,1,4,6,5),    pi_y=(3,2,1,5,6,4).
```

Swapping values `1,2` reconstructs `x',y'`, so
`tau_1(x)=x'` and `tau_1(y)=y'`. The two sources have identical `D_1` data,
including boundary positions `((7,19),(2,20))` and closure scalars
`((1,1,5,11,{5}),(1,1,4,10,{10}))` in the checker's zero-based event
coordinates.

Yet no schedule serves both. Thus

```text
one fixed schedule for every D_i metadata class: REFUTED at d=4.
```

The complete proof and field definitions are in
`contour_metadata_obstruction.md`.

## Field 4 — exact subgroup obstruction

For two factor tuples, a common signed braid is the ordinary Hurwitz action
on their coordinatewise pairs in `S_4 x S_4`; it preserves the literal
generated subgroup.

For `(x,y)`, the factor-pair generators give

```text
H=(V_4 x V_4)Diag(S_4),       |H|=16*24/4=96.
```

Indeed diagonal transpositions generate `Diag(S_4)`, while an off-diagonal
pair yields `(12)(34)` in one coordinate; conversely both coordinates have
the same image modulo `V_4`.

For `(x',y')`, an off-diagonal pair yields a 3-cycle in one coordinate, whose
normal closure is `A_4`, while all pairs have equal parity. Hence

```text
K=(A_4 x A_4)Diag(S_4)
 ={(p,q):sgn(p)=sgn(q)},       |K|=144*24/12=288.
```

Since `H!=K`, a common braid is impossible at arbitrary length. This is a
symbolic finite-rank proof, not a bounded BFS obstruction.

## Field 5 — schedule-conflict graph and sharp reduction

For fixed `d,i`, define the schedule-conflict graph `C_(d,i)` on `Z_d` by
joining `u,v` whenever their coordinate-pair generated subgroup differs from
that of `tau_i(u),tau_i(v)`.

Every fixed-schedule agreement set is an independent set, so every schedule
cover has at least `chi(C_(d,i))` classes. This implication is **PROVED**.
The converse need not hold: pairwise invariant compatibility does not supply
one simultaneous braid.

The complete `d=3` audit makes the distinction exact. For every adjacent
index:

```text
|Z_3|=24, signed action image order=216,
conflict edges=80, omega=3, chi=3,
true minimum fixed-schedule cover=5,
maximum one-schedule agreement=6.
```

Thus conflict coloring alone undercounts the actual schedule requirement.
The new precise frontier is:

> **CONFLICT-COLORING PLUS SIMULTANEOUS REALIZATION.** Cover `Z_d` by
> `d^O(1)` conflict-independent classes and prove each class lies in one
> agreement set of a fixed signed braid of length `d^O(1)`.

This statement remains **UNRESOLVED**. It cleanly separates the necessary
pair-invariant part from the missing braid-realization part.

## Field 6 — exact small-rank metadata audit

The independent checker exhausts all rooted DPS coordinates:

| `d` | rooted pairs | `|Z_d|` | root fiber |
|---:|---:|---:|---:|
| 3 | 72 | 24 | exactly 3 |
| 4 | 11,520 | 2,880 | exactly 4 |

At `d=3`, even the exact affected physical-factor pair gives nine classes but
two classes are not contained in any one action-image agreement set. Closure
scalar histories happen to give 8--12 realizable classes, while the full
tested `D_i` summary is injective on all 24 sources. These are complete
finite facts.

At `d=4`, `D_i` has respectively

```text
2741, 2717, 2745, 2782, 2758
```

observed classes for `i=1,...,5`, on 2,880 sources. Every index has a
size-two class containing a paired-subgroup obstruction. The simpler exact
physical-pair key also fails for every index. The raw search stops after the
first certificate (or the declared 1,200-pair cap for descriptors without a
found certificate); no capped non-finding is promoted.

The M122 full-twist schedule is not overgeneralized: among the 360 `d=4`
sources with a square in the first two positions, it realizes `tau_1` on 180,
not all 360. M122's proved structured star family remains valid.

## Field 7 — class count, recovery, and root quotient

Recording every closure event of both labels can separate more sources, but
each label has exactly `d-2` events. The raw history alphabet therefore has
`d^{O(d)}` possibilities. The whole contour has length `O(d^2)` over a
polynomial alphabet, hence `d^{O(d^2)}` possible words. Neither is a
polynomial schedule key without a new compression theorem.

Conditionally suppose a future theorem supplies `q(d)=d^O(1)` fixed schedules
of maximum scheduled length `L(d)=d^O(1)` with deterministic class assignment.
Given `(i,class,scheduled time,direction)` and a directed physical action,
prefix inversion recovers at most one physical source. Scheduled holds remain
bijections. If holds are deleted and only compressed path time is kept, at
most `L(d)` scheduled times are candidates.

There are `2d-3` adjacent indices. The rooted lift has exactly `d` roots, and
deterministic root tracking incurs the one factor `d` audited by M122/M126.
Thus index, class, time, compressed-time, and root losses would all be
polynomial. This conditional conclusion applies only to adjacent-value
demands and supplies no UST exchange routing.

## Field 8 — reproduction, artifacts, and hygiene

Deterministic command, Python `3.12.3`, dependencies `{}`, seed `null`:

```text
python3 -B schedule_cover_audit.py --d 3 4 --paths-through-d 3 \
  --max-metadata-pairs 1200 --output results.json
```

The final run took `33.159361839294434` seconds. `results.json` stores every
certificate, exact `d=3` action/conflict result, class histogram, search cap,
and whether each descriptor search was exhaustive. `results_d3.json` and
`results_d4_metadata.json` are earlier deterministic development snapshots;
no claim depends on them instead of the final combined output.

Owned artifacts are `plan.md`, `checkpoint.md`,
`contour_metadata_obstruction.md`, `schedule_cover_audit.py`, the three JSON
outputs, this report, `freeze_manifest.md`, and `SHA256SUMS`. No predecessor,
coordinator, manuscript, project skill, or file outside this mission directory
is edited.

## Field 9 — final decision and remaining obligations

```text
KEEP THE d=4 LOCAL-CONTOUR METADATA OBSTRUCTION.
KEEP THE SCHEDULE-CONFLICT GRAPH AS A NECESSARY REDUCTION.
DO NOT CLAIM AN ASYMPTOTIC SCHEDULE LOWER BOUND.
```

The assigned **ADJACENT-VALUE POLYNOMIAL SCHEDULE COVER** remains unresolved.
The next admissible positive result must compress global contour/closure
information into polynomially many conflict-compatible classes and prove
simultaneous braid realization with polynomial length. A negative result
would require an asymptotic chromatic/cover lower bound, not another isolated
finite collision.

UST basis exchanges, total rooted-product congestion, arbitrary-product
`Gamma_0`, `gap(P_(0,d))`, the original exact heat-bath gap, and both terminal
outcomes remain open.
