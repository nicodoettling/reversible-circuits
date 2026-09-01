# M101 checkpoint: proof-critical M97 audit complete

Date: 2026-08-12.  Provisional verdict: **ACCEPT with zero material
numbered objections**.

## Frozen integrity

The assigned frozen digests match:

```text
73ab5bec4d5ba48bb1b4511099df056525fe1f6b6f1b6caa6f79b7964feb3c99  M97 report.md
6d0c28f8a4414175a3226b77fb1cff3217599f14ad707eaf5a7d3e3470babc4f  M97 freeze_manifest.md
```

The M92 report/proof/manifest hashes imported for the zero-fiber family also
match M97's frozen dependency list, and the fresh M95 acceptance report has
SHA-256
`feeb86aa8fcd18cf0af9342928adb7c4780beaff25fc453f3416d66794bfe237`.

## Independent proof audit

The prefix-genus proof is correct.  Starting from zero, appending an edge has
the exhaustive changes

```text
different support blocks:             (Delta q,Delta c,Delta g)=(-1,-1,0)
same support block, same p-cycle:      (0,+1,0)
same support block, different cycles:  (0,-1,+1).
```

This proves nonnegative integrality and prefix monotonicity without an
external factorization theorem.  Since total genus is one, the forward and
reversed words each have one handle.  At a hypothetical common handle `e`,
if `p` is the preceding prefix product then forward creation says `pe` joins
two `p`-cycles; identity gives the reversed suffix product `pe`, and appending
`e` changes `pe` back to `p`, a cycle cut.  It cannot be the reverse handle.
Together with the incidence Euler inequality this proves `b<h`.

For every cut, cycles of the prefix product lie in unique left and right
support blocks.  Their bipartite incidence multigraph has connected
components equal to the join of the two support partitions.  Connected total
support therefore makes it connected.  The exact identity

```text
g(left)+g(right)=q(left)+q(right)-c(prefix)=V-E
```

then gives tree, connected-unicyclic, tree in the three handle regions.
Genus is the sum of the same formula over support blocks; nonnegativity of
each summand proves the claimed componentwise genus-zero conclusion.

For the lift, with `U f(w,j)=f(w)` and `R F(w)` the uniform cut average,
`RU=I` and direct evaluation gives `L=UP_dR`.  Hence

```text
functions on A_d = im(U) direct-sum ker(R),
L|im(U) similar to P_d,       L|ker(R)=0.
```

This proves the complete spectrum union, not merely the nonzero spectrum.
Half-laziness puts `spec(P_d)` in `[0,1]`, so added zeros do not alter the
Poincare gap.  If reducible, both chains retain eigenvalue-one multiplicity
greater than one and have gap zero.  At `d=2`, both spaces are singletons,
`h=3,b=2,J={2}`, and the declared singleton gap is one.

The square insertion/deletion correspondence is an exact bijection once the
square position is distinguished.  Forgetting that mark gives weight exactly
`r(w)`, bounded by the `2d-1` adjacent positions, but gives zero weight to
unmarked words.  The imported M92 family has identity because two incident
transpositions have order-three product, support exactly the chosen tree,
and no deletable connected square because every tail square is a unique tree
bridge.  Thus the dependency and zero-fiber conclusion are correct.

## Independent finite audit

`independent_audit.py` imports no M97 code.  It exhaustively checked `d=2,3,4`:

| `d` | states | all cuts | unmarked | insertion incidences |
|---:|---:|---:|---:|---:|
| 2 | 1 | 5 | 0 | 3 |
| 3 | 240 | 1,680 | 24 | 360 |
| 4 | 131,040 | 1,179,360 | 41,472 | 120,960 |

Every cut passed the exact genus/Euler/profile and componentwise checks;
every insertion incidence matched one deletion mark.  Handle histograms,
pair histograms, row-signature counts, and mark histograms exactly reproduce
M97.  At `d=3`, the 240-state base matrix and 336-state lift have the same
gap (`0.02771319171181641` versus `0.02771319171181541`) and the lift has
exactly 96 additional numerical zeros.  The factorization residual is
`1.8e-15` and the spectrum-union residual `3.0e-15`.

The frozen-handle path family passed for every `3<=d<=12`.  All `3,16,125`
M92 tree words for `d=3,4,5` were distinct and unmarked.

No finite result is used as asymptotic gap evidence.  The genus-one gap,
worst-source marked hitting, partial-fiber expansion, and global heat-bath
mixing all remain unresolved exactly as M97 states.
