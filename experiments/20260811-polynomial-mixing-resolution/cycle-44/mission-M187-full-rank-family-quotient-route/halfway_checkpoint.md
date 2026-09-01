# M187 halfway checkpoint

Date: 2026-08-13 UTC.

## Immutable gate

All fourteen assigned frozen manifests passed before their payloads were
used: M135/M137, M141/M143, M146/M148, M154/M158, M169/M172,
M175/M176, and M181/M183.  No frozen mission was edited.

The reconciled interfaces are exact.  A perfect-matching color contains one
`H=Stab(d)`-orbit edge over each left global orbit, but it does not choose a
canonical physical representative.  The DPS map `tau_i` is `H`-equivariant
only.  By contrast, M181's source stabilizer loops transfer through arbitrary
coordinatewise `G`-conjugation.  Therefore M181's full source voltage does
not itself put its matched DPS target tuple in the source quotient component.

## Proof status

The every-color synchronized quotient-route theorem is not proved.  The
matching axioms do not force the color-selected `H`-orbit edge over a source
quotient vertex to be the rooted/anchored edge on which a local DPS formula is
available.  Generated subgroup and factor-conjugacy data are retained only as
necessary tests and are not assumed sufficient.

A conditional block-local route survives.  For a doubled-tree word, a
rooted DPS coordinate can make an adjacent edit quotient-trivial when the two
edited values are the two labels of one doubled edge.  At a boundary between
two doubled edges, the edit is represented by the literal signed-Hurwitz
generator `R_i` under the checked local incidence condition (the consecutive
tree edges are disjoint or meet at the distinguished root).  This statement
is conditional on the matching choosing those rooted `H`-orbit edges; no
argument shows that every color does so.

## Minimal symbolic audit

The clean-room checker reconstructed only the two explicit `d=5` M181 source
words and their five possible distinguished roots, applied the seven DPS
adjacent-value edits, and canonically compared quotient tuples.  It did not
enumerate `Z_5`, `Q_5`, an action group, or a quotient component.

There are 54 distinct eligible matched target quotient tuples in this
targeted family.  A bounded breadth-first search to radius five from the one
ordered source pair visited 4,008 quotient tuples and supplied exact positive
routes for 14 of the 54 targets, with lengths

```text
0,1,1,1,1,1,1,2,2,3,3,3,3,5.
```

These fourteen are positive certificates only.  The forty misses are not
nonreachability evidence and will support no obstruction claim.  A separate
bounded `d=3,4` doubled-tree falsification audit supports the local incidence
condition above; the all-`d` proof must be stated from the DPS construction,
not inferred from those finite rows.

## Remaining work

Freeze the narrow conditional representative-selection theorem and the exact
positive `d=5` witnesses.  State that arbitrary-color quotient reachability
remains unresolved; do not extend the BFS, search a new voltage invariant,
address route length, or infer a gap/mixing/Terminal result.
