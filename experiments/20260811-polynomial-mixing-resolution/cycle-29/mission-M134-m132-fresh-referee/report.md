# M134 fresh referee report on frozen M132

Date: 2026-08-13 UTC. Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict and exact scope

```text
ACCEPT M132 AT ITS STATED NONTERMINAL SCOPE.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

M132 correctly refutes one schedule per class of its defined polynomial
two-label contour descriptor, proves that every fixed-schedule agreement set
is independent in the schedule-conflict graph, and computes the complete
`d=3` conflict/action calibration. It correctly leaves the general
**ADJACENT-VALUE POLYNOMIAL SCHEDULE COVER** unresolved.

```text
candidate                  | schedules selected by two-label contour metadata
claimed target             | uniform physical minimal identity sector Z_d
identity ok                | brute and independent DPS checks at d=3,4
crosses Hurwitz components | not applicable; one connected minimal sector
exact diagnostics          | roots, descriptor, pair subgroups, action/conflict
verdict                    | accept scoped obstruction; general cover unresolved
```

No UST basis-exchange routing, all-edge rooted-product comparison, physical
gap, arbitrary-product `Gamma_0` theorem, original lazy exact `{3,4,5}`
heat-bath gap, Terminal A, or Terminal B result is proved or refuted here.

## 2. Frozen provenance

Every assigned digest matches:

| M132 artifact | observed SHA-256 |
|---|---|
| `report.md` | `ca8cef32a17cfe62c38eaaa92eeb994affcf6706a9018c8fcc5a1c8fe0951a7d` |
| `contour_metadata_obstruction.md` | `8b7a2c222fc5cb55b95e7473378d9321c9145d1fa13025a71da8290205ea6eee` |
| `schedule_cover_audit.py` | `8b1f8abba35872b00e7921dcff7222b9f305894e5d396b2af9817028ef7c1b99` |
| `results.json` | `cebc4b8b07d007b31e1f52785c7fb63079f132205020bb1d650bfde6611cee53` |
| `freeze_manifest.md` | `8660e71b4f5f040f12a95241a50f79ddc634c1ea7643fd78ef84752f2e20b4b4` |
| `SHA256SUMS` | `c67708f2d636275d94836795d754cf078f41ed2b6775f3431f86c943c37823f4` |

`sha256sum -c SHA256SUMS` also validates every payload listed by M132. The
fresh checker imports no predecessor module or result file.

## 3. Target, convention, and dependencies

The auxiliary target is uniform on

```text
Z_d={(t_1,...,t_(2d-2)):t_1...t_(2d-2)=id,
                              support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors multiplied
left-to-right. Signed right-Hurwitz moves are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

The associated half-lazy physical kernel, not bounded here, is

```text
P_(0,d)=I/2+[1/(4(2d-3))] sum_j (R_j+R_j^(-1)).
```

The accepted M112/M119 input gives the literal rooted product and exact
white-root quotient

```text
rooted Z_d <-> Cayley_d x S_(2d-2),       d roots per physical word.
```

M127/M130 give the all-rank root-independent involutions `tau_i` and the
common-schedule pair-subgroup invariant. M132 uses no new literature theorem.

## 4. Independent DPS and target reconstruction

The checker separately brute-enumerates each physical target and constructs
the accepted plus-mirror DPS image from all Cayley trees and permutation
coordinates. The two sets coincide:

| `d` | rooted coordinates | brute `|Z_d|` | root fiber | target collisions |
|---:|---:|---:|---:|---:|
| 3 | 72 | 24 | exactly 3 | 0 |
| 4 | 11,520 | 2,880 | exactly 4 | 0 |

Every reconstructed word evaluates to identity and has connected support.
Every adjacent-value edit descends to a bijective involution on the physical
target. These checks independently fix the convention used below.

## 5. Exact `d=4` descriptor collision

For `i=1`, the fresh reconstruction reproduces

```text
x =((12),(13),(13),(12),(34),(34)),
y =((12),(13),(13),(34),(12),(34)),

x'=((12),(23),(13),(24),(23),(34)),
y'=((12),(23),(13),(34),(24),(34)).
```

All four words are in brute `Z_4`, and `tau_1(x)=x'`, `tau_1(y)=y'`. The
canonical rooted certificates are exactly

```text
T={(1,2),(1,3),(2,4)},
pi_x=(3,2,1,4,6,5),       pi_y=(3,2,1,5,6,4).
```

Every field of M132's defined descriptor agrees, not merely a projection:

```text
physical pair:               ((12),(13))
hairy black/white endpoints: ((2,2),(1,2))
oriented face endpoints:     ((2,1),(1,3))
boundary positions:          ((7,19),(2,20))
closure scalars:             ((1,1,5,11,{5}),
                              (1,1,4,10,{10}))
```

The contour and closure positions are zero-based; displayed vertices are
one-based. Thus `D_1(x)=D_1(y)` exactly as claimed.

## 6. Pair-subgroup obstruction and hand descriptions

Write `A=(12), B=(13), C=(34), D=(23), E=(24)`. The coordinatewise source
generators reduce to

```text
(A,A),(B,B),(A,C),(C,A),(C,C).
```

The diagonal generators give `Diag(S_4)`. Multiplication by a diagonal
generator isolates a double transposition in either coordinate, whose normal
closure is `V_4`. Conversely every generator has equal image modulo `V_4`.
The independently enumerated group is therefore exactly

```text
H=(V_4 x V_4)Diag(S_4),       |H|=96.
```

The target pairs contain diagonal `A,D,B,C`, hence `Diag(S_4)`, and an
off-diagonal pair that isolates a 3-cycle in one coordinate. Its normal
closure is `A_4`, while every pair has equal parity. Direct enumeration gives

```text
K=(A_4 x A_4)Diag(S_4)
 ={(p,q):sgn(p)=sgn(q)},       |K|=288.
```

Both set equalities, not only the orders, are checked. A common signed braid
acts as ordinary Hurwitz motion on the pair tuple in `S_4 x S_4` and preserves
its literal generated subgroup. Since `H!=K`, no schedule can serve both
sources at any length. M132's descriptor obstruction is therefore proved.

## 7. Polynomial descriptor range

The only potentially hidden large field is the tuple of distance-three
closure steps. In the accepted DPS closure a distance-three event is the
event that creates the unique quadrangle of that indexed face, so a label has
at most one such event. The independent implementation asserts this invariant
during every closure and sees maximum one over all rooted coordinates at
`d=3,4`. Each label has exactly `d-2` total closure events.

With

```text
E=binom(d,2),  B=(2d-1)(2d-2),  S=(d-2)(2d-2),
```

the safe fieldwise count is:

- `E^2=O(d^4)` for the two exact physical factors;
- `[d(d-1)]^4=O(d^8)` for the hairy and oriented endpoint pairs;
- `B^4=O(d^8)` for four directed boundary positions;
- `(S+1)^10=O(d^20)` for five closure fields per label, including an empty
  or singleton distance-three step.

Hence the displayed bound is valid:

```text
|range(D_i)| <= E^2[d(d-1)]^4 B^4(S+1)^10 = O(d^40).
```

At the trivial boundary `d=2`, first/last closure values should be read as an
empty marker. M132's computation intentionally starts at `d=3`; `Z_2` is a
singleton, so this is a nonmaterial notation clarification.

## 8. Conflict graph and complete `d=3` calibration

For sources `u,v`, define a conflict when their coordinate-pair subgroup
differs from that of `tau_i(u),tau_i(v)`. If one fixed schedule serves an
agreement set, the common-schedule invariant forbids any conflict inside it.
Assigning each source to one schedule in a cover therefore gives a proper
coloring. Thus

```text
number of schedule classes >= chi(C_(d,i))
```

is proved. The converse is not asserted: pairwise subgroup compatibility
does not construct one simultaneous braid.

For each `i=1,2,3`, the independent exhaustive `d=3` calculation gives

```text
signed action image order              216
tau_i in that image                    no
conflict vertices / edges              24 / 80
maximum clique / chromatic number      3 / 3
distinct nonempty agreement masks      23
maximum one-schedule agreement         6
minimum fixed-schedule cover           5
```

The clique calculation supplies a triangle and exhausts the absence of a
four-clique; an explicit proper three-coloring supplies the upper bound.
Exact union DP over all action-image agreement masks has frontier sizes

```text
1, 23, 206, 811, 1640, 2021,
```

and first contains the full 24-source mask at five schedules. Therefore the
strict gap `chi=3 < 5=true cover` is exact.

The ancillary `d=3` metadata rows also match: the exact physical pair gives
nine classes with two unrealized classes; closure scalars give `12,9,8`
realizable classes; and the full descriptor is injective with 24 classes.

## 9. Complete finite `d=4` descriptor audit

The fresh checker exhausts every pair lying in one full-descriptor class,
rather than stopping at the first certificate:

| `i` | classes | within-class pairs | conflicting pairs |
|---:|---:|---:|---:|
| 1 | 2,741 | 158 | 15 |
| 2 | 2,717 | 179 | 21 |
| 3 | 2,745 | 141 | 12 |
| 4 | 2,782 | 101 | 15 |
| 5 | 2,758 | 139 | 27 |

Every index has a conflicting size-two descriptor class. The simpler exact
physical-factor pair also has a conflict at every index. The M122 structured
full-twist calibration is reproduced: its length-20 schedule serves 180 of
the 360 square-prefix sources for `tau_1`, not all 360.

These are exact finite refutations of named universal selectors, not an
asymptotic lower bound on the number of schedules.

## 10. Capped searches and finite labels

Inspection of frozen `results.json` confirms that M132 marks every search
which stops at a first certificate or the declared 1,200-pair cap as
`search_exhaustive=false`. In particular, capped `d=4` non-findings for the
coarsest relation key and some closure-scalar rows are not promoted. The full
descriptor claim needs only one exact collision, and this referee independently
exhausts all of its within-class pairs.

M132 also correctly labels the `d=3` action, conflict, and cover values
**EXACT FINITE**, and does not infer polynomial asymptotics from them.

## 11. Conditional recovery and root quotient

Suppose a future cover supplies `q(d)=d^O(1)` fixed schedules of scheduled
length at most `L(d)=d^O(1)` and a deterministic class assignment. Given
`(i,class,scheduled time,direction)` and the directed physical action, the
known schedule prefix is bijective, so prefix inversion recovers at most one
physical source. Scheduled holds do not change bijectivity. If holds are
deleted, one compressed time has at most `L(d)` scheduled-time preimages.

There are `2d-3` adjacent indices. The accepted rooted DPS quotient has
exactly `d` white roots over every physical word. Therefore index, class,
time, compressed-time, and root losses are polynomial under the hypothesized
cover. M132 correctly restricts this statement to adjacent-value demands; it
does not supply UST routes or complete stationary congestion.

## 12. Reproduction and hygiene

Deterministic command, Python `3.12.3`, dependencies `{}`, seed `null`:

```text
python3 -B independent_referee.py
```

The final exact run took about eight seconds and wrote
`independent_results.json`. The checker uses no predecessor code/data and
reimplements brute targets, DPS closure, subgroup closure, action images,
clique/coloring search, and cover DP.

M134 owns only `plan.md`, `checkpoint.md`, `independent_referee.py`,
`independent_results.json`, this report, `freeze_manifest.md`, and
`SHA256SUMS`. No M132, predecessor, coordinator, manuscript, project-skill,
or other mission file is edited.

## 13. Final decision

```text
ACCEPT. ZERO MATERIAL NUMBERED OBJECTIONS.
```

Promote only M132's exact scope: the `d=4` obstruction to its defined
`O(d^40)` contour selector and the conflict graph as a necessary reduction.
Retain every small-rank number as an exact finite fact. The general
**ADJACENT-VALUE POLYNOMIAL SCHEDULE COVER**, simultaneous realization, UST
basis exchanges, full rooted-product comparison, every gap claim, and both
terminal outcomes remain unresolved.
