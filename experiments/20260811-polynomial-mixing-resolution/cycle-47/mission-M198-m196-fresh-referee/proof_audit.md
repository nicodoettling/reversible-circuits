# M198 proof and convention audit

Date: 2026-08-13 UTC.

## 1. Audited statement

In M191's finite `d=5` quotient action `X=Q_5`, with signed Hurwitz symbols
acting chronologically on the right, every one of the 54 named width-two
target pairs lies in the diagonal-action component of source `(16,0)`.

## 2. Action and target reconstruction

The clean-room checker imports no predecessor Python. Starting from the two
physical source words, it independently implements global-label
canonicalization, positive and negative Hurwitz moves, and breadth-first
closure. It obtains 8,400 canonical connected identity words. Its fourteen
generator permutations match every entry of M191's frozen action rows; all are
bijections and each signed pair is mutually inverse. The packed action digest
is

```text
160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae.
```

The checker also reconstructs the Prüfer trees, boundary closure, rooted DPS
inverse descriptors, seven adjacent-value edits, and all 25 root pairs per
edit. It reproduces all ten rooted descriptors and partitions the 175
edit/root occurrences into exactly the same 54 sorted target rows.

## 3. Chronological stabilizer criterion

Fix source `(v,u)`, target `(v',u')`, and a right-action word `alpha` with
`v^alpha=v'`. Put `z=u'^(alpha^(-1))`. Then

```text
(v',u') is reachable from (v,u)
iff z is reachable from u by a word in Stab(v).
```

Indeed, a route `r` gives `h=r alpha^(-1)`, which fixes `v` and maps `u` to
`z`. Conversely, such an `h` makes `h alpha` a route to `(v',u')`. Word
concatenation is chronological, so the displayed order is forced. The
clean-room BFS transversal reaches all 8,400 first-coordinate states, has
maximum depth 13, and all tree words replay. The 54 target tree words produce
exactly 41 adjusted second IDs.

## 4. Meet-in-the-middle convention

For adjusted target `(v,z)`, M196 stores `f` from `(v,u)` to meeting point `m`
and `b` from `(v,z)` to the same `m`. Signed inversion is

```text
b^(-1) = reverse(b) with every symbol negated.
```

Because the seven signed action pairs are literal inverses, `f b^(-1)` maps
`(v,u)` to `(v,z)`. The referee checked the two meeting equations, exact stored
concatenation, and final stabilizer endpoint for all 41 adjusted IDs. It also
rebuilt the entire radius-eight forward ball independently: 154,393 states at
levels `1,6,40,190,795,2976,10416,34256,105713`. Every stored forward word is
the corresponding clean-room BFS-tree word. Fifteen certificates are direct
hits; 26 use a nonempty backward segment.

## 5. Full endpoints and conclusion

For every named target, the referee recomputed `alpha` and `z`, checked the
stored stabilizer word, checked the literal equality `w=h alpha`, and replayed
`w` on both coordinates. All 54 pass. Maximum lengths are forward 8, backward
7, stabilizer 15, named-target tree 9, and complete word 22. The result digest
is

```text
e40c220ea10798b82d7225cbde54daec751f25e581028c926e2a11ba3e33a4b2.
```

Thus M196's exact finite positive classification is proved by explicit
certificates. The bounded search supplies no negative result, nor is one
needed because every named target is positive.

## Numbered objections

None.

The accepted conclusion is restricted to the 54 named `d=5`, width-two
targets. No every-color, all-`d`, polynomial route-length, gap, mixing, or
Terminal consequence follows.
