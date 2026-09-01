# M92 halfway checkpoint

Date: 2026-08-12 UTC. Commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Sources and frozen boundary read

Read in full or in the task-relevant sections:

- `HANDOFF.md`, `GOAL_SPEC.md`;
- the project skill, `sampling-problem.md`, and `experiments.md`;
- the relevant theoretical-status/Hurwitz/next-steps manuscript sections;
- frozen M75/M77, M84/M85, and M86/M89 reports, plus M84's
  `zero_row_theorem.md` and M86's `signed_cover_theorem.md`;
- the conditional Classification-H/transitivity audit and the relevant
  M60/M68/M74 canonical-routing failures.

No predecessor or shared durable file has been edited.

## Named claim at halfway

The arbitrary-macro cover is not proved.  The positive topological lead and
the negative arborescence result now separate cleanly.

### Proved elementary topological step

For a connected genus-one identity component on `d` labels and `2d`
factors, the chronological ribbon graph is a cellular torus with

```text
V=d, E=2d, F=d.
```

Choose a primal spanning tree `T`; choose a dual spanning tree `T*` using
only edges outside `T`.  Exactly two edge occurrences remain.  Contracting
`T` and merging faces along `T*` leaves the one-vertex, one-face, two-edge
torus cellulation, so the two leftover fundamental cycles form an integral
homology basis.  This is an elementary tree--cotree certificate and invokes
no unverified trisection literature.

It does **not** yet give a connected-deletable square.  A literal braid
surgery must turn one of these nonseparating cycles into an adjacent equal
pair annulus.  Conditional on the project's still-unverified Classification
H input, some polynomial adaptive path exists, but this does not show that
the path depends on polynomially many fixed transcripts.  The checkpoint's
proved topological and obstruction claims do not use that input.

### Exact metadata falsification

`tree_cotree_metadata_audit.py` independently enumerates actual connected
genus-one identity words in `S_4` at length eight.  It found two words after
only 1,589 candidates for which ascending primal/dual Kruskal gives:

```text
tree positions       (0,3,5) in both words
cotree positions     (1,4,6) in both words
leftover positions   (2,7) in both words
leftover labels      (01),(13) in both words
```

but the fundamental path for leftover `(13)` is respectively

```text
(0,3,5)    and    (0,5).
```

Thus the leftover positions and labels—even together with the tree/cotree
position sets—do not determine the tree-path surgery transcript.  This is a
finite exact refutation of that specific metadata sufficiency claim, not a
refutation of every constant-metadata certificate.

### Proved arborescence/root-compression obstruction

Let a direct routing send demand from every source of a macro `Gamma` to a
set `C` of marked roots and then use terminal edges from those roots.  If the
terminal support has `R` actual directed edges and every source sends
terminal demand at least `eta`, then some terminal edge has weighted
occupation at least

```text
eta |Gamma|/R.
```

This is immediate by summing terminal demand and pigeonhole, and it applies
to `S=Gamma`, where no within-macro prefix can be charged as an earlier exit.
If each root has at most `b=poly(N,m)` designated refresh choices and
`|C|=q`, then `R<=bq`.  Polynomial occupation therefore requires

```text
q >= eta |Gamma|/[b poly(N,m)].
```

In particular a random spanning arborescence rooted at one, or polynomially
many, canonical marked templates cannot prove the desired direct coarea
bound.  For fixed tree randomness its endpoint map also sends every source
to the same root, so it is not a bijection and cannot be substituted into
M75's inverse-prefix theorem.

There are explicit two-component macros `Gamma_d`, with ambient
`N=d+2,m=2d+2=2N-2`, satisfying

```text
|Gamma_d| >= d^(d-2).
```

Merely doubling every edge of each of Cayley's `d^(d-2)` labeled trees would
give genus zero.  The genus-one unmarked construction instead chooses two
incident edges `a_T,b_T` and uses

```text
u_T=(a_T b_T)^3 product_(e in T minus {a_T,b_T}) e^2.
```

The alternating prefix is an identity of length six and contains no square;
every tail square is the unique pair on a bridge.  Appending/interleaving the
disjoint two-label minimal component gives distinct unmarked states of the
same macro.  Hence polynomial-root arborescence occupation is
superpolynomial on this family.

### Natural uniform-tree law refuted

For `d>=3`, put path edges `e_i=(i,i+1)` and

```text
u_d=(e_0 e_1)^3 e_2^2 e_3^2 ... e_(d-2)^2.
```

This is a connected genus-one identity word of length `2d`.  It has no
connected-deletable adjacent square: the alternating six-prefix has no
square, while deleting any tail leaf square disconnects the path.  Appending
a disjoint doubled edge gives a literal unmarked two-component minimal
exterior source.

A source-independent law which guesses a uniformly random labeled Cayley
tree and invokes its tree-supported normalizer only when the guessed tree is
contained in the source support has success probability at most

```text
d^(-(d-2))
```

on this source, because the path support has a unique spanning tree.  If it
instead samples a spanning tree conditional on the source support, its law
is source-dependent.  The usual guess-and-abort implementation is also a
piecewise adaptive map rather than a fixed bijective signed braid.  This
rigorously refutes the natural uniform-tree guess/conditional-tree
normalizer, but not a different fixed-word law that acts nontrivially when
its guessed tree is absent.

The exact script verifies the path family through `d=12`; the all-`d` claim
uses `(e_0e_1)^3=id` in `S_3` and the disjoint square identities, not finite
extrapolation.

## Second-half target

Write the full proofs and probability/occupation constants.  The surviving
positive lemma will require a **distributed-root reversible surgery**: a
state-independent law of fixed signed words (or direct flow) whose successful
endpoints occupy at least an inverse-polynomial fraction of the exponentially
many marked terminal edges.  A canonical/trisection algorithm must retain its
branch information reversibly or prove polynomial transcript overlap; merely
computing a tree/cotree from the source is insufficient.
