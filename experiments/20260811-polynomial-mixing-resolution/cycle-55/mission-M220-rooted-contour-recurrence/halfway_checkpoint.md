# M220 halfway checkpoint: finite key breaks at the first next rank

Date: 2026-08-13 UTC.

## Analytic stage completed first

Before next-rank computation, `symbolic_transport.md` proved the four-factor
leaf-carrier identity and the one-/two-generator boundary identities, then
declared one explicit recurrence. The recurrence rewrites every nontrivial
ordinary odd correction as `Q B Q^-1`, where `Q` is determined only by edited
vertex, late-ancestor flag, initial consecutive direct-child run, and one
forward-chain exception flag.

The closed formula reproduces all 112 accepted M214 rows at `d=5 -> 6`.

## Exact `d=6 -> 7` outcome

Two independent Prüfer constructions agree on the complete 125-tree template.
The deterministic checker replays all nine edits on every tree, with no route
search and no `Q_6`/`Q_7` enumeration:

```text
rows       1125
passes     1098
failures     27

failure histogram: edit 1 -> 11, edit 7 -> 16; every other edit -> 0.
```

In particular, the two edits new relative to M214, edits 8 and 9, pass all
125 rows under the proposed boundary schedules. This is an exact finite fact,
not an all-rank theorem.

## First same-key obstruction

At edit 1, the rank-six star and the tree obtained by replacing edge `{1,5}`
with `{2,5}` have the same complete proposed descriptor:

```text
vertex 2; path (2,1); late=false; run=0; exception=false.
```

The common 17-move closed formula succeeds on the star and fails on the second
tree at literal factor positions 7 and 8, leaving `(45)^2` where the actual
endpoint has `(46)^2`. Thus the initial consecutive-child run ignores a
nonconsecutive larger child that changes factor transport.

## Current verdict

```text
REJECT THE EXPLICIT LATE/RUN/FORWARD-EXCEPTION RECURRENCE.
KEEP THE FORMAL CARRIER IDENTITIES AND THE EXACT FINITE SURVIVORS.
```

This does not prove that no alternative word works for the same pair, and it
does not reject a richer contour descriptor. Next: archive the exact witness,
freeze the no-go at this scope, and request a fresh immutable referee.

