# M284 report: matching-coset route signatures

Date: 2026-08-14 UTC. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict and exact scope

```text
VERDICT: KEEP THE STRICT RANK-LIFTED SCHEDULE-INTERSECTION LEMMA,
         SUBJECT TO FRESH IMMUTABLE AUDIT.

CHART/LOCAL-TYPE-ONLY COVERAGE OF AN M135 MATCHING COLOR: REFUTED.
FULL POLYNOMIAL M135 MATCHING-COSET REFINEMENT: UNRESOLVED.
```

The proved result is a deterministic statement about endpoint fibers of
explicit signed braid words in the rooted minimal doubled-tree model. It is
not a probability, voltage-length, recovery, congestion, spectral-gap,
mixing, or Terminal statement.

## 2. Immutable source gate

Every entry in each assigned M135/M137, M175/M176, M181/M183, M200/M202,
M240/M242, M269/M271, M273/M275, and M278/M281 checksum inventory passed.
The independently recorded checksum-file digests are in `checkpoint.md`.
No predecessor was edited.

The dependency scopes are retained exactly:

- M135 supplies a left-perfect color of the orbit-incidence graph and the
  polynomial common-action-refinement obligation.
- M278/M281 supplies the complete local rooted adjacent-edit correction
  table. Its correction starts from an old-edited word padded to the new
  rank; it is not itself a same-rank M135 coset element.
- M181/M183 remains conditional on quotient routing into the synchronized
  component.
- M200/M202's every-color result remains finite rank `d=5` only.

## 3. Type firewall and exact recursive state

At old rank `d`, let

```text
Ktilde_Q={beta in B_(2d-2):beta(w_Q)=tau_i(w_Q)}
```

be the word-level preimage of M135's same-rank action fiber `K_Q`. For a
valid M278 extension chart, let `c_(T,i)` be the accepted correction from the
old-edited padded word `N_T` to the new-edited word `A_T`. M278 proves

```text
c_(T,i)(N_T)=A_T,
```

not `c_(T,i)(U_T)=A_T`. This separates the correction word in
`B_(2d)` from the lower and upper finite action fibers.

Let `j_d:B_(2d-2)->B_(2d)` be the standard injective braid embedding fixing
the last two strands. With `;` denoting chronological composition, first
`j_d(beta)` and then `c`, the exact liftable fiber is

```text
L_(T,i)={j_d(beta);c_(T,i):beta in Ktilde_(Q_T)}.
```

It lies in the upper endpoint fiber because `j_d(beta)` maps the unedited
padded source `U_T` to `N_T`, after which `c_(T,i)` maps `N_T` to `A_T`.
For a family sharing one literal correction word `c`, right cancellation and
injectivity of `j_d` give exactly

```text
intersection_T {j_d(beta);c:beta in Ktilde_(Q_T)}
 ={j_d(beta);c:beta in intersection_T Ktilde_(Q_T)}.
```

The common `c` is independent of the chart only within such a fixed literal
signature class. The equality is at braid-word level; upper action-image
intersections may be larger. The minimally safe state licensed by the frozen
inputs is therefore a valid chart, an explicit lower braid (or its full word
fiber), and the literal correction. A lower finite action alone has no
accepted rank embedding and loses the representative-length information.

## 4. Exact one-step class count

M240's ordinary scan permits either sign at a nonchild and requires the
negative sign at a direct larger child. Choosing every optional sign negative
gives a single tree-independent open correction; a closed ordinary edit uses
the identity. Internal even, cross-boundary, and last edits each have one
fixed correction. The four rows cover every index `1<=i<=2d-3`, including
the minimal old rank `d=5` and both seams. Thus, for every fixed `(d,i)`, the
literal local alphabet has size at most two.

Consequently, an explicitly declared extension-compatible lower cover by
`q` common braid schedules lifts in one rank step to at most `2q` classes,
with displayed length increment at most `4d-7`. This does not show that the
family is a full M135 matching color, nor that iterating the recurrence yields
a polynomial number of classes.

## 5. Analytic chart-coverage obstruction

For every upper rank `D>=6`, put `e_r=(0,r)` and

```text
U_D=e_1,e_1,e_2,e_2,...,e_(D-1),e_(D-1),
V_D=R_2(U_D)
   =e_1,e_2,e_2 e_1 e_2,e_2,e_3,e_3,...,
     e_(D-1),e_(D-1).
```

The first four factors multiply to `id`, all later factors are squares, and
all star edges remain in the support. Hence `V_D` is connected, has product
identity, and has minimal length `2D-2`. Every unedited M278 chart source has
equal factors in each canonical consecutive pair. Global conjugation
preserves equality at fixed positions, while the first two factors of `V_D`
are distinct. Thus no global conjugate of `V_D` is a chart source.

For every adjacent index, every M135 perfect-matching color contains exactly
one `H`-edge over the left global orbit `[V_D]`, by left-perfectness. That
edge is chartless. Therefore the chart/local-correction-type descriptor does
not cover a complete color.

This is not a lower bound on the number of genuine schedule classes and does
not refute a polynomial refinement using additional source-dependent base
routes. It refutes only deletion of the chartless/base-route clause.

## 6. First remaining lemma and action

The first unresolved interface is a polynomial-cardinality base-route
signature cover that includes every chartless left global orbit and the
actual `H`-edge selected by an arbitrary matching color, with common
translated embedded action intersections admitting polynomial-length
representatives. The rank-lifted lemma can concatenate local terminal pieces
only after that input is supplied.

Final action: **freeze M284 and request a fresh immutable referee focused on
the type/source ordering, word-versus-action distinction, all-negative local
standardization and index boundaries, and the arbitrary-rank chart-coverage
obstruction.**

