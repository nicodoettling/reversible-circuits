# M225 final report: exact finite full child-contour correction

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
PROMOTE CANDIDATE B AS AN EXACT FINITE d=6 -> 7 THEOREM.
REJECT CANDIDATE A'S DISPLAYED MAP ON 16 EDIT-7 ROWS.
```

Candidate B succeeds on the complete declared finite template.  It is not an
all-rank child-contour lemma.

## Field 2 — immutable provenance

Every frozen payload in M214/M218 and M220/M223 passed its checksum inventory.
Top digests are

```text
M214 cb63ac879b036d096af369fabf02da9abecba786bcf746ba34d809b8ceaada3f
M218 3929f738afcb9834e74eea9610d284ca5cabe2589da05b691bf3b4447b58f656
M220 0b953e9c517cfeb379d32abe04b32ea928dd2a83e67bc1ac40d61f87fccd1316
M223 538eb1e0351a7ff005ca262261a1bd8056d868b98307b79e5948b9f1fd5b929d
```

No predecessor was edited.

## Field 3 — exact target, convention, and source order

There is no probability distribution or Markov kernel in this mission.  The
target is deterministic physical endpoint correction

```text
N_(T,i)=F_6(T,s_i pi_6)(06)^2,
A_(T,i)=F_7(T+{{1,7}},s_i pi_7)
```

under chronological signed right-Hurwitz action

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

Before any M225 replay, `candidate_descriptors.md` fixed exactly two nested
candidates.  Candidate A retains the complete ordered larger-child vector.
Candidate B additionally records the entire stopped parent path and all
ordered off-path child incidences, and predeclares identity for late-ancestor
or internal-contour-ascent paths.  No third candidate was introduced.

## Field 4 — proved symbolic transport

For distinct symbols, the five-move carrier satisfies

```text
R_p^- R_(p+1) R_(p+2)^- R_(p+1)^- R_p^-
  [(xy),(zx),(zy),(zn)]
= [(xn),(zy),(zy),(zx)].
```

The checker verifies all 840 ordered distinct-symbol specializations.  The
full child vector drives a predeclared sign automaton: a present child resets
the sign to inverse, while an absent child reverses the preceding sign.  The
carrier algebra is formal; sufficiency of the asserted DPS closure regimes is
proved here only by the complete finite reconstruction.

## Field 5 — exact complete-table result

Two exact Prüfer constructions agree on the complete 125-tree root-leaf
`d=6` template.  All nine edits produce 1,125 literal endpoint replays, with
no quotient enumeration and no route search:

```text
edit                  1   2   3   4   5   6   7   8   9
Candidate A passes  125 125 125 125 125 125 109 125 125
Candidate B passes  125 125 125 125 125 125 125 125 125
```

Candidate A therefore passes 1,109 and fails 16. Candidate B passes all 1,125.
Normalized complete-row digests are

```text
Candidate A 85b01dc81f7175b8df32d198181e7b898507ec71d0862ca963c431695f0a15f6
Candidate B 80ba2016f66f6f8bd9d6cb8a53b276c0ee4403a4ec6747fdd85568299817f78e
```

## Field 6 — classwise common words and controlled finite length

Candidate B yields 407 descriptor classes: 101 for each of the four odd edits
and three shared non-odd classes.  The checker asserts a single assigned route
inside every class, and every replay in every class passes.  Yet the displayed
map uses only 14 distinct correction words:

```text
length       0    1    2    5    9   13   17
rows       568  125  125  108   84   65   50
```

The finite maximum length is 17.  The large class count comes from recording
the complete path and its off-path incidences; the route formula factors
through the edited vertex, child-sign vector, and late/ascent closure choice.
Thus the rich descriptor prevents hidden collisions, while its 407 classes do
not imply 407 separately fitted words.

## Field 7 — retained Candidate-A obstruction and next lemma

Candidate A fixes all eleven M220 edit-1 failures but fails 16 edit-7 rows.
Its first same-descriptor collision is

```text
D_A=("odd_A",5,false,[],false),
T_0={{1,2},{1,3},{1,4},{1,5},{1,6}},
T_1={{1,3},{1,4},{1,6},{2,3},{2,5}}.
```

The common five-move carrier passes `T_0`.  For `T_1`, path `(5,2,3,1)` has
an internal ascent and the naive endpoint already equals the actual endpoint;
the carrier instead fails at factors 8 and 11.  Candidate B distinguishes the
path and assigns identity exactly as predeclared.

The next standalone obligation is an all-rank local DPS closure/induction
lemma proving the ascent decision and child-sign automaton under one-leaf
extension, while showing how much of the nearly tree-specific contour record
is actually necessary.

## Field 8 — reproduction and hygiene

Environment: Python 3.12.3; dependencies `{}`; seed `null`. Command:

```text
python3 -B child_contour_audit.py
```

The checker imports no predecessor code or data, performs no route search, and
enumerates neither `Q_6` nor `Q_7`.  Consecutive runs produced identical
`child_contour_results.json` hashes.  All writes are confined to M225, and no
bytecode cache is retained.

## Field 9 — strict boundary and audit request

```text
PROMOTE: the formal carrier identity, Candidate A's exact obstruction, and
Candidate B's complete 125-tree / nine-edit finite correction theorem with
407 classes, 14 words, and maximum length 17.

DO NOT INFER: intrinsic or all-rank descriptor completeness, an all-d local
lemma, every-color or arbitrary-representative routing, voltage-corrected or
total route length, polynomial gap/mixing, or Terminal.
```

Freeze M225 and commission a fresh immutable clean-room referee focused on the
source order of both predeclared candidates, formal carrier identity, complete
125-tree/1,125-row reconstruction, Candidate-A collision, Candidate-B class
and word counts, both row digests, finite length histogram, and strict scope.
