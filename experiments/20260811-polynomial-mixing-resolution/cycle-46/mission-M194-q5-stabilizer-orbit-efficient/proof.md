# M194 exact Schreier method and cap outcome

Date: 2026-08-13 UTC.

For M191's immutable right action on `Q_5`, let `t_x` be the chronological BFS
word from source first coordinate `v=16` to `x`. For each signed generator
`g`, the word

```text
s_(x,g)=t_x g t_(xg)^(-1)
```

fixes `v`. The Schreier lemma says these words generate the action stabilizer
of `v`: every stabilizing word can be telescoped edge by edge against the
chosen transversal. Therefore closing second source `u=0` under all
`s_(x,g)` decides the exact stabilizer orbit used by M191's criterion.

The implementation rechecked the 8,400-point frozen action digest, all
generator bijections and inverse pairs, built the complete BFS transversal,
and replayed every `t_x`. It streamed literal Schreier loops on the second
coordinate and retained orbit-enlarging generators, closing under each retained
generator and inverse.

The internal 300-second deadline expired during this exact closure. No complete
orbit or output certificate was produced. Hence:

```text
PROVED: the stated Schreier method is exact under the right-action convention.
EXACTLY CHECKED: action integrity and complete 8,400-point transversal.
INCONCLUSIVE: the stabilizer orbit and all 54 target memberships.
```

No partial orbit is used as a negative certificate, and no new positive route
is inferred.
