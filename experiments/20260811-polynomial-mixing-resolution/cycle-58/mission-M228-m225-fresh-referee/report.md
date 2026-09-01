# M228 final report: fresh immutable referee of M225

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
ACCEPT M225 AS FROZEN, AT ITS STRICT FINITE SCOPE.
```

Candidate A's exact obstruction and Candidate B's complete finite
`d=6 -> 7` theorem both survive no-input clean-room reconstruction.

## Field 2 — immutable provenance and source order

Every one of M225's 12 frozen payloads returns `OK`. Its complete
`SHA256SUMS` digest is

```text
e61d77f0765c9aaba177ef0e0bca8b6f7f94758b7814bb7243846dff3f9f0acd
```

M225 remains immutable. Its candidate and symbolic files explicitly assert
predeclaration and have equal `21:58:28 UTC` mtimes, preceding the checker
(`22:04:17`) and result (`22:04:40`). This supports the declared order of
exactly two nested candidates and no third refinement. The inventory was
created at final freeze, however, so it cryptographically fixes contents but
does not itself timestamp that earlier chronology.

## Field 3 — target, convention, and clean-room method

There is no probability law or Markov kernel in this mission. The target is
deterministic endpoint correction under chronological signed right-Hurwitz
action

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

`cleanroom_referee.py` has no input files, predecessor import, or predecessor
data read. It uses a separately written heap-based Prüfer decoder and DPS
rotation/closure implementation. It performs no quotient enumeration, route
search, or route-output lookup.

## Field 4 — both formulae and symbolic transport

The referee transcribes Candidate A's full ordered larger-child vector and
initial forward exception, then Candidate B's strict refinement by the whole
stopped path and all off-path child lists. Candidate B assigns identity to
late-ancestor or internal-ascent cases; all other odd cases use the explicit
signed `Q B Q^-1`. The three non-odd cases are formula-fixed as well.

The formal five-move carrier passes all 840 ordered distinct-symbol
substitutions. The sign automaton passes all 21 initial-run specializations
through length five. In particular `(0,0,0)` gives `(+,−,+)`, while the M220
witness vector `(0,0,1)` gives `(+,−,−)`, changing only the last stage. The
automaton's general DPS interpretation remains a local hypothesis outside the
finite table, exactly as M225 states.

## Field 5 — complete finite reconstruction and digests

Direct filtered Prüfer generation and extension of all trees on `[5]` agree
on the complete 125-tree rank-six root-leaf template. The checker also verifies
all 125 unedited leaf extensions, then reconstructs and literally replays all
nine edits:

```text
edit                  1   2   3   4   5   6   7   8   9
Candidate A passes  125 125 125 125 125 125 109 125 125
Candidate B passes  125 125 125 125 125 125 125 125 125
```

Thus Candidate A has 1,109 passes and 16 failures; Candidate B has 1,125
passes and no failures. The independent normalized row digests exactly equal
M225's:

```text
A 85b01dc81f7175b8df32d198181e7b898507ec71d0862ca963c431695f0a15f6
B 80ba2016f66f6f8bd9d6cb8a53b276c0ee4403a4ec6747fdd85568299817f78e
```

## Field 6 — formula assignment, classes, and finite length

For every row, the checker calls

```text
formula_assignment(tree,d,edit,candidate)
```

before constructing `naive` or `actual`. The assignment function accepts no
endpoint or target argument, and expected certificates occur only as terminal
assertions. This independently confirms that the 14 words are formula outputs,
not paths discovered from replay targets.

Candidate B has 404 odd descriptor classes plus three shared non-odd classes,
hence 407 total; every class has one assigned word and every replay passes.
Its length histogram is

```text
length       0    1    2    5    9   13   17
rows       568  125  125  108   84   65   50
```

The exact finite maximum is 17.

## Field 7 — first collision and descriptor-richness audit

The first Candidate-A same-descriptor collision is independently reproduced
at edit 7:

```text
D_A=("odd_A",5,false,[],false),
T_0={{1,2},{1,3},{1,4},{1,5},{1,6}},
T_1={{1,3},{1,4},{1,6},{2,3},{2,5}}.
```

The common five-move carrier passes `T_0`; `T_1` already has `N=A`, and the
carrier fails at factors 8 and 11. Candidate B records path `(5,2,3,1)`, sees
its internal ascent, and formulaically assigns identity.

Candidate B is very fine: on each odd edit, 125 trees split into 101 classes
(83 singletons, 12 doubletons, 6 tripletons). Across four odd edits, 332 of
404 classes are singletons. It therefore nearly records the full contour/tree.
The fact that this rich partition still maps to only 14 formula words is an
exact finite collapse, not evidence of intrinsic or all-rank sufficiency.

## Field 8 — numbered objections

Material objections:

1. None.

Nonmaterial objections:

1. The claimed precomputation source order is supported by explicit frozen
   assertions and consistent filesystem mtimes, but not by a cryptographic
   timestamp or intermediate commit. This does not affect the independently
   reconstructed mathematical table.

## Field 9 — reproduction, disposition, and strict boundary

Environment: Python 3.12.3; dependencies `{}`; seed `null`. Command:

```text
python3 -B cleanroom_referee.py
```

Consecutive runs produce identical `referee_results.json` hashes. No cache is
retained, and all writes are confined to M228.

```text
ACCEPT: M225's formal carrier identity, initial-run sign specialization,
Candidate-A collision, and Candidate-B complete 125-tree/nine-edit finite
theorem with 407 classes, 14 formula words, and maximum length 17.

DO NOT INFER: cryptographically proved source chronology, intrinsic or all-d
descriptor sufficiency, every-color or arbitrary-representative routing,
voltage-corrected or total route length, spectral gap, mixing, or Terminal.
```

Freeze this referee and stop without expanding the audit scope.
