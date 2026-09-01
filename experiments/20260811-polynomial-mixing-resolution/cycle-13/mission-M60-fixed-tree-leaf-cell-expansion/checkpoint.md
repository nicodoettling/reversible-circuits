# M60 halfway checkpoint: leaf-cell refutation and full-minimal-macro escape

## 1. The named leaf-cell expansion is false

Let `L(T)` be the original leaf set of a fixed labeled tree and define the
multi-strand core

```text
Core_T(w)=Del_(L(T))(w).
```

Permutation-cycle erasure commutes between labels.  Therefore, if
`Del_v(w)=Del_v(w')` for one original leaf `v`, applying the other deletions
gives `Core_T(w)=Core_T(w')`.  Every transition of `P_T^leaf` preserves this
core.

For a path tree on `N>=5`, deleting its two leaves leaves a path on `N-2>=3`
vertices.  That fixed-tree fiber has at least two words (different orders of
adjacent doubled edges), and appending the two deleted leaf squares lifts
each core word back to the original path tree.  Hence `P_T^leaf` is reducible
for every path `N>=5`.  This rigorously refutes the M59 named proposition.

The exact N=5 path audit has eight components, exactly the eight core words
in the fixed three-vertex path fiber, with sizes

```text
1068,1068,997,997,997,997,842,842.
```

Their literal full-K escape probabilities are `0.4301...` through
`0.4424...`; their rejected-exit fixed-tree escape is `0.0140...` through
`0.0428...`.  Thus auxiliary reducibility does not lift to a global
bottleneck.

## 2. Universal local strand canonicalization

Fix a minimal word with join tree `T`, a tree leaf `v` with edge
`f={v,u}`, and its base `z=Del_v(w)`.  The insertion-coordinate table gives
two null increments.  The first is the opening factor `h_a=(v,a)` (initially
`f`) and the second closes the coordinate.

If an opening null is followed by one projected base factor `s`, exactly one
of the following same-product Hurwitz identities moves the null right:

```text
(h_a,s)   -> (s,s h_a s),
(h_a,h_b) -> ((a,b),h_a),  when s=(a,b).
```

Padding the pair with the unchanged next factor makes this a literal H3
outcome.  Repeat until the two nulls are adjacent, producing a square
`h h`.  Refresh `h h` to `f f` with one padded H3 update, then slide it to
the end using

```text
f f c -> c f f.
```

Every step preserves `Del_v=z`, word product, length, and connected full
support; the join tree may temporarily change.  The endpoint is the canonical
hub `z f f`, and the path has length at most `2m-3`.  Each specified step has
literal K probability at least

```text
p_*=1/[2|R_m|(m-2)M^3],  M=binom(N,2),
```

because a length-three fiber has at most `M^3` words.

The exact falsifier checked this construction on every leaf of every state
in the N=4 and N=5 representative fixed-tree fibers: 914 and 75,802
state-leaf pairs respectively, zero failures, maximum observed lengths 5 and
7.

## 3. Arbitrary-cut theorem inside the entire minimal macro

For each labeled tree `T`, select one leaf `v(T)`.  Its deletion cells have
size at most

```text
Lambda_N=binom(m,2)(N-1)^2.
```

Let `A` be any nonempty subset of the whole minimal macro `F_N`.  In a cell
with `a` points of `A`:

- if the hub `z f f` is in `A`, a specified H3 refresh to `z s s`, with `s`
  avoiding `v`, exits `F_N` and hence `A`;
- if the hub is outside `A`, route every `A` point to it by the canonical
  path and select the first boundary edge.

Every path edge preserves `(v,z)`.  Given such an edge, there are at most
`N(N-1)` possible original pairs `(v,u)`, which with `z` determine the
original tree and cell, and each cell has at most `Lambda_N` starts.  Thus a
boundary edge is charged by at most `N(N-1)Lambda_N` states.  Macro edges and
internal first-exit edges are disjoint.  Under global uniform stationarity,

```text
Q_K(A,A^c)/pi(A)
 >= p_*/[N(N-1)Lambda_N]
 =1/[2|R_m|N(N-1)binom(m,2)(N-1)^2(m-2)M^3]
 >=1/(24N^13).                                      (3.1)
```

Consequently the two-sided conductance has the same lower bound, regardless
of whether `pi(A)` exceeds one half.  This controls every original-K cut
contained in `F_N`, not only a fixed-tree or core-measurable cut.  It remains
nonterminal because a global cut may include states outside `F_N` and thereby
seal the macro exits.

## 4. Current first gap

**MINIMAL-MACRO MEAN-LIFT WITH EXTERIOR OVERLAP.** Extend (3.1) to arbitrary
global cuts whose intersection with `F_N` varies internally while their
outside portion may contain the canonical macro-exit targets.  Equivalently,
prove that internal first-exit flow plus the exterior boundary of those
targets loses only a universal polynomial, without assuming the cut contains
all or none of `F_N^c`.

