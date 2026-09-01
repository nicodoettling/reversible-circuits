# Scoped zipper theorem when one increment has full group support

## Statement

Let `G` be a finite group and let `E` be a finite microstate set with a
surjective product map `p:E->G`.  For `l>=2` and `h in G`, put

```text
Omega_h={ (A_1,...,A_l) in E^l : p(A_1)...p(A_l)=h }
```

with its uniform law.  Let `B_h` choose one of the `l-1` adjacent pairs
uniformly and replace it uniformly by an element of `E^2` with the same
ordered product.  Then

```text
gap(B_h) >= 1/(l^3 |E|^3).                              (1)
```

In the project application, `E=T_N^2`, `|E|=M^2`, and `p` is surjective
onto `A_N` exactly for `N=3,4` (with the singleton `N=2` harmless).
Therefore every arbitrary-endpoint aligned-H4 bridge for `N=3,4` satisfies

```text
gap(B_h) >= 1/(l^3 M^6).                                (2)
```

The convention is `(pq)(x)=p(q(x))`; tuple products are written from left
to right in that convention.  This theorem is uniform in `l` but only covers
the fixed small degrees where a single paired increment realizes every even
permutation.  It is not Terminal A.

## Zipper path

Choose once and for all a canonical microstate `c(g) in p^{-1}(g)` for each
`g in G`.  Given source `x=(X_1,...,X_l)` and target
`y=(Y_1,...,Y_l)`, write `x_i=p(X_i)` and `y_i=p(Y_i)`.

Before stage `i`, the path has the form

```text
(Y_1,...,Y_(i-1),D_i,X_(i+1),...,X_l),                 (3)
```

where `D_1=X_1`, and for later stages `D_i=c(d_i)`.  The invariant is

```text
y_1...y_(i-1) d_i x_(i+1)...x_l=h.                     (4)
```

For `i<=l-2`, define

```text
d_(i+1)=y_i^(-1)d_i x_(i+1)
```

and use the adjacent heat bath once to replace

```text
(D_i,X_(i+1)) -> (Y_i,c(d_(i+1))).                     (5)
```

The two sides of (5) have the same ordered product.  At the final stage,
(4) and the common endpoint imply

```text
d_(l-1)x_l=y_(l-1)y_l,
```

so replace `(D_(l-1),X_l)` directly by `(Y_(l-1),Y_l)`.
Self-loop stages are omitted.  The path has at most `l-1` directed edges,
and every intermediate tuple remains in `Omega_h`.

## Complementary-bridge injection

Fix a used directed edge at stage `i`.  Its tail and head reveal the target
prefix `(Y_1,...,Y_i)` and the source suffix
`(X_(i+1),...,X_l)`.  Define

```text
e_i=(x_1...x_(i-1))^(-1) h (y_(i+1)...y_l)^(-1)
```

and the complementary bridge

```text
z=(X_1,...,X_(i-1),c(e_i),Y_(i+1),...,Y_l).             (6)
```

Equation (6) has length `l` and product `h`.  From

```text
(used directed edge, z, i, X_i)
```

one recovers all of `x` and `y`: `z` supplies the source prefix before `i`
and target suffix after `i`, the metadata supplies the omitted source
microstate, and the edge supplies the remaining two pieces.  Thus the map
from every charged source-target path occurrence to this data is injective.
There are at most `l|E|` metadata values and exactly `|Omega_h|` choices of
the complementary bridge.

## Congestion

Let `S=|Omega_h|`, so the stationary whole-word heat-bath flow of each
ordered pair `(x,y)` is `S^-2`.  A fixed directed `B_h` edge has capacity at
least

```text
S^-1 /[(l-1)|E|^2],                                    (7)
```

because the selected two-microstate conditional fiber has size at most
`|E|^2`.  For a fixed edge, the injection and the path-length bound give
total comparison load at most

```text
S (l|E|) S^-2 l = l^2|E|/S.                            (8)
```

Dividing (8) by (7) yields congestion at most

```text
l^2(l-1)|E|^3 <=l^3|E|^3.
```

The reference whole-word heat bath has gap one, proving (1).

## Boundary audit and first failure

- At `l=2`, `B_h` itself is the whole-word heat bath; (1) is conservative.
- All endpoints are covered, not only identity.
- Ordered pair microfactorizations are retained; duplicate group products do
  not affect recovery because `X_i` is recorded as a microstate.
- No common normal form or hub is used.  At every path edge, the visible
  target prefix/source suffix and complementary bridge balance the two-word
  information.
- For project `N>=5`, `p(T_N^2)` consists only of the identity, 3-cycles,
  and products of two disjoint transpositions, and is a proper subset of
  `A_N`.  The defect `e_i` in (6), or `d_(i+1)` in (5), can therefore lack a
  two-transposition microfactorization.  The proof does not extend by merely
  choosing a different canonical representative.

The next standalone proposition is a polynomial-width version of this zipper
in which the nonabelian defect is stored in several paired increments while
the complementary bridge still recovers all overwritten microfactors with
only polynomial metadata.
