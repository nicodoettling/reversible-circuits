# M228 method audit

## Formula assignment, not target lookup

The decisive row loop has this order:

```text
route, descriptor, details = formula_assignment(tree,d,edit,candidate)
naive, actual = endpoint_pair(tree,d,edit)
replay = chronological_action(naive,route)
```

`formula_assignment` accepts only `tree`, `d`, `edit`, and `candidate`.
Ordinary odd words are either identity or the explicit `Q B Q^-1`; non-odd
words are the three displayed fixed cases.  It receives no endpoint, mismatch,
pass/fail bit, expected digest, or route table.  There is no breadth-first
search, quotient graph, solver, shortest-path routine, or route-output map.
Expected counts/digests are asserted only after both complete audits return.

## Independent finite universe

The checker decodes every Prüfer word on `[6]` with a leaf heap and filters
for root 6 having unique incident edge `{1,6}`.  It cross-checks that ordered
list as a set against every Prüfer tree on `[5]` extended by `{1,6}`.  Both
give 125 trees.  It then constructs exactly edits 1 through 9, not a quotient
state graph or a `Q_6`/`Q_7` route enumeration.

## Symbolic scope

The five-move carrier is an exact tuple identity and passes all 840 ordered
distinct-symbol substitutions in seven symbols.  The sign automaton is a
definition; its claimed specialization to an initial run of children is
checked for all 21 `(length,run)` cases through length five, and the M220
vectors `(0,0,0)` and `(0,0,1)` yield `(+,−,+)` and `(+,−,−)` respectively.

The prose explanation that these signs track a general DPS contour is not an
all-rank proof.  Its sufficiency is established only for the exhaustively
checked finite `d=6 -> 7` template.

## Descriptor richness

Candidate B records Candidate A's full child bits and flags, the entire
stopped path, and every off-path child list along that path.  On each odd edit,
its 125 trees split into 101 classes (83 singletons, 12 doubletons, and 6
tripletons).  Thus “nearly records the full contour” is accurate.  The route
formula uses only the edited vertex, sign vector, and late/ascent decision,
which explains why these 407 total classes collapse to 14 distinct words
rather than being separately fitted.
