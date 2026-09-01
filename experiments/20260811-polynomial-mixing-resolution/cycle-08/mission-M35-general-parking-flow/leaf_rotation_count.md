# Exact leaf-rotation count and Cayley lift

Date: 2026-08-11.  Permutations compose as `(pq)(x)=p(q(x))`, and
factor tuples are multiplied left-to-right.  This note concerns the nonlazy
uniform scan of the `r-1` adjacent rank-two same-product heat baths on
minimal transposition factorizations of

```text
c=(0 1 ... r) in S_(r+1).
```

It proves an exact local-flow theorem.  It does not prove a polynomial gap
for the full parking-macro projection.

## 1. Statement

For a factorization word `w`, orient every factor edge `{h,k}` from its
smaller endpoint `h` to its larger endpoint `k`, and let

```text
m_h=#{(h,k) in w:k>h},       0<=h<r.
```

The vector `m=(m_0,...,m_(r-1))` is a parking count vector: it has total
mass `r` and every prefix through `s<r` has mass at least `s+1`.  Adjoin
`m_r=0` and let `T(m)` be the unique rooted plane tree whose vertices have
preorder `0,...,r` and outdegrees `m_0,...,m_r`.

Suppose that `j` is a leaf child of `i` in `T(m)` and is not the last child
of `i`.  Define

```text
m^rot=m-e_i+e_j.
```

Then `m^rot` is joined to `m` by the actual projected heat bath and

```text
bar P_r(m,m^rot)=2m_i/[3r(r-1)].                    (1.1)
```

Equivalently, if

```text
O_m={minimal long-cycle factorizations with count vector m},
```

then the number of marked source pairs (a source word together with its
favourable scan position) is

```text
#marked=m_i |O_m|/r,                                (1.2)
```

and each marked pair has exactly two favourable outcomes in its three-word
rank-two fibre.  Consequently the raw favourable-outcome count is

```text
2m_i |O_m|/r.                                       (1.3)
```

With `pi_r(m)=|O_m|/(r+1)^(r-1)`, the stationary capacity is exactly

```text
Q_r(m,m^rot)=pi_r(m) 2m_i/[3r(r-1)].                (1.4)
```

The factor `3(r-1)` in (1.1)--(1.4) is the three-element conditional
fibre times the uniform scan.  It must not be omitted.

## 2. Interval decomposition of every factor tree

The following deterministic lemma is the structural input.

**Lemma 2.1 (canonical interval components).**  Let `G` be any noncrossing
spanning tree drawn on the cyclically ordered vertices `0,...,r`, and put
`d_h=#{(h,k) in E(G):h<k}`.  Form the preorder plane tree `T(d)` from
`(d_0,...,d_(r-1),0)`.  For every vertex `v`, the child-subtree intervals
of `v` in `T(d)` are exactly the consecutive vertex intervals forming the
components obtained after deleting `v` from the induced tree on the
preorder interval of the subtree rooted at `v`.

**Proof.**  Start with the whole interval `[0,r]`.  Deleting its least
vertex `0` from a noncrossing tree leaves components with consecutive
vertex sets in their cyclic order.  This is the standard boundary-vertex
separation fact: two different components with interlacing boundary
vertices, together with their two distinct attachment paths to `0`, would
force a crossing.  Since every neighbour of `0` is larger than `0`, the
number of components is `d_0`.

Let one such component have interval `I=[a,b]`.  It is a tree and its
only edge to `0` has lower endpoint `0`.  Thus

```text
sum_(h in I) d_h=|I|-1.                              (2.1)
```

For every proper initial interval `J=[a,t]` of `I`, let `c_J` be the
number of components of the induced forest `G[J]`.  It has
`|J|-c_J` internal edges.  Each of its `c_J` components needs an edge to
`I\J`, and every such edge has its lower endpoint in `J`.  Hence

```text
sum_(h in J)d_h >= |J|-c_J+c_J=|J|.                 (2.2)
```

Therefore `b` is the first index at which the running sum of `d_h-1`,
starting at `a`, reaches `-1`.  This is precisely the first-subtree return
rule for a preorder/Łukasiewicz degree sequence.  It uniquely identifies
the first child interval, and iteration identifies all `d_0` child
intervals.  Each component is itself a noncrossing tree on a consecutive
interval.  Its one possible attachment to an earlier vertex has its lower
endpoint outside the interval and hence does not alter its displayed
forward degrees.  Applying the same argument recursively proves the
claim.  QED

Apply Lemma 2.1 to the chord tree of a factorization with macro `m`.
Because `j` is a leaf child of `i`, its child interval is the singleton
`{j}`, so the tree contains `(i,j)`.  Since `j` is not the last child, the
next child component is a nonempty interval beginning at `j+1`, and its
unique attachment to `i` is an edge `(i,k)` with `k>j`.  No edge from an
earlier ancestor can also meet `j`: it would cross `(i,k)`.  Since
`m_j=0`, no edge from `j` goes to a larger vertex.  Thus `(i,j)` is the
unique raw factor incident with `j` in every word of `O_m`.

Moreover, `(i,j)` and `(i,k)` are consecutive in the clockwise order of
the factor chords incident with `i`; their two child intervals are
consecutive and there is no other attachment edge between them.

## 3. Exact contraction bijection

Let `m^-` be obtained by decreasing `m_i` by one, deleting the zero
coordinate `m_j`, and shifting all later coordinate names down by one.
It is the preorder degree vector obtained by deleting leaf `j` from
`T(m)`.  Stanley--Biane gives

```text
|O_m|=r!/product_h m_h!,
|O_(m^-)|=(r-1)!/[(m_i-1)! product_(h!=i,j)m_h!]
          =m_i|O_m|/r.                               (3.1)
```

We now give a bijection between `O_(m^-)` and the marked source pairs in
(1.2).

Take a marked source.  Its consecutive factors have the form

```text
(i,k),(i,j),             i<j<k.                      (3.2)
```

Delete vertex `j` and the second factor, shift all vertex names greater
than `j` down by one, and close the gap in the factor numbers.  Lemma 2.1
shows that the remaining chords form a noncrossing spanning tree with
forward degrees `m^-`.  Goulden--Yong's clockwise-decreasing incident-edge
condition remains true after deleting one chord and order-preservingly
closing one gap in the numbers.  Their sufficiency theorem therefore says
that the resulting numbered diagram is the chord diagram of a unique word
in `O_(m^-)`.

Conversely, start from a word in `O_(m^-)`.  Undo the vertex-name shift.
Lemma 2.1 identifies the child interval of `i` that immediately follows
the deleted singleton position `j`; let `(i,k)`, `k>j`, be its unique
attachment edge and let its factor number be `q`.  Insert the new vertex
`j`, add the chord `(i,j)`, give it factor number `q+1`, and increase every
old factor number greater than `q` by one.  The new chord is noncrossing.
At every vertex other than `i`, applying the increasing map
`s -> s+1{s>q}` preserves the clockwise inequalities.  At `i`, the new
chord is immediately clockwise before `(i,k)` and the local numbers become

```text
... > q+1 > q > ... .                                (3.3)
```

Thus the clockwise-decreasing condition still holds.  Goulden--Yong
Proposition 2.4 and Lemma 2.5 imply that this numbered chord diagram is a
long-cycle factorization.  It has macro `m`, and the consecutive pair is
exactly (3.2).  This insertion and the preceding deletion are inverse.
Equation (3.1) proves (1.2).

For completeness, under the project convention the ordered product in
(3.2) has exactly the following three ordered transposition
decompositions:

```text
(i,k)(i,j),       (i,j)(j,k),       (j,k)(i,k).       (3.4)
```

The first has lower-label multiset `{i,i}` and the other two have
`{i,j}`.  Therefore a marked scan changes `m` to `m^rot` with probability
`2/3`.  Dividing (1.2) by `|O_m|`, multiplying by `1/(r-1)` for the scan,
and then by `2/3` proves (1.1)--(1.4).

The literature convention check is the same as in the accepted M27
report: Goulden--Yong use one-based cyclic labels and right-to-left action.
After cyclic relabeling to `0,...,r`, their word order agrees with our
left-to-right tuple product, so no word reversal is introduced.

## 4. Uniform-Cayley lift

The stationary weight has a useful exact interpretation.  Root a Cayley
tree on labels `0,...,r` at label `0`, sort every vertex's children by
their numeric labels, traverse in preorder, and forget the numeric labels.
For a fixed resulting plane tree with preorder degree vector `m`, the
children of each preorder vertex impose one increasing chain of length
`m_i` on the `r` nonroot labels.  These chains are disjoint.  Hence the
number of Cayley trees in the fibre is

```text
r!/product_i m_i!,                                    (4.1)
```

and the pushforward of the uniform Cayley-tree law is exactly `pi_r`.

A leaf rotation lifts geometrically.  In a source Cayley tree, let the
preorder positions `i,j,k` be respectively the parent, the leaf, and the
root of the next sibling subtree.  Delete the parent--`k` edge and attach
`k` below the leaf at `j`.  The numeric-label order of the siblings makes
the preorder label sequence unchanged; only the degree transfer
`m -> m-e_i+e_j` occurs.  The lift is injective from the source Cayley
fibre into the target fibre, whose size is `m_i` times larger.  Distributing
the macro capacity (1.4) equally over these lifted edges gives symmetric
per-edge conductance

```text
2m_i/[3r(r-1)(r+1)^(r-1)].                           (4.2)
```

Thus a polynomial gap for this weighted Cayley subtree-slide chain would
imply a polynomial gap for the leaf-rotation macro chain.  No such gap is
proved here.  A naive unweighted slide or a uniform-plane-tree chain has
the wrong stationary law.

## 5. Scope, dependencies, and falsification

- **Proved here:** Lemma 2.1, the deletion/insertion bijection, exact
  counts (1.1)--(1.4), and the uniform-Cayley pushforward/lift.
- **Cited and convention-checked:** Richard Stanley, *Parking Functions
  and Noncrossing Partitions*, EJC 4(2) (1997), Theorem 3.1 and
  Proposition 4.1; P. Biane, *Parking Functions of Types A and B*, EJC 9
  (2002), Theorem 3.1; I. Goulden and A. Yong, *Tree-like Properties of
  Cycle Factorizations*, JCTA 98 (2002), Theorem 2.2(f1)--(f3),
  Proposition 2.4, and Lemma 2.5.
- **Empirical falsifiers only:** `leaf_rotation_probe.py` verifies the
  count through `n=7`; `leaf_contraction_audit.py` verifies the displayed
  contraction bijection through `n=7`; `leaf_insertion_probe.py` verifies
  the equivalent suffix-trajectory inverse through `n=7`.  None of those
  finite checks is used as universal proof.
- A stronger fixed-coordinate characterization is false already at
  `n=5`.  The still stronger claim that the factor immediately before
  `(i,j)` is always `(i,j+1)` is also false at `n=5`.  The proof above uses
  the unique attachment `(i,k)` of the whole next child interval, not a
  prescribed endpoint.
- Caraceni--Stauffer's polynomial gap for leaf translation is for the
  uniform law on plane trees.  Here the law is proportional to
  `1/product_i m_i!`; direct measure comparison can lose exponentially and
  is not invoked.

The exact remaining proposition is **ADJACENT-VALUE PARKING FLOW**: route
the adjacent-value ideal chain (already proved to have gap at least
`r^-7`) through these leaf rotations, or prove an inverse-polynomial gap
for the weighted Cayley lift, with polynomial total stationary-flow
congestion and recoverable metadata.
