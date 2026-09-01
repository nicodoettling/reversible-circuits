# Halfway checkpoint: exact l=3 incidence quotient survives through N=12

## Exact bounded claim and convention

Permutations satisfy `(pq)(x)=p(q(x))`.  Fix `N>=3` and an even endpoint
`h`.  At pair length `l=3`, a state is a six-transposition word grouped as
three ordered pairs `(A,B,C)`, with pair products `(a,b,c)` and `abc=h`.
The nonlazy aligned chain chooses the left or right four-factor window with
probability `1/2` and then resamples exactly uniformly from its same-product
fiber.

The finite calculation can falsify:

> Every nonempty fixed-endpoint pair-length-three microfactorized Q bridge is
> connected under its two aligned H4 heat baths.

A failure would also refute the broader arbitrary-length base-connectivity
premise.  Finite survival proves neither statement and says nothing about a
uniform gap.

## Exact quotient lemma

For fixed `h`, define a bipartite multigraph with:

- a left vertex for each ordered first transposition pair `A`;
- a right vertex for each ordered last pair `C`;
- an incidence `A--C` exactly when

  ```text
  b=a^{-1} h c^{-1} belongs to supp(Q).
  ```

Every actual state `(A,B,C)` maps to this incidence.  States with fixed `C`
form exactly one left-window heat-bath clique, because the product of the
first four factors is forced by `(h,C)`; states with fixed `A` form one
right-window clique.  Multiple middle pairs `B` on the same incidence are in
both cliques.  Hence two six-factor states communicate if and only if their
incidences lie in the same connected component of this bipartite graph.

The graph may be quotiented further from ordered pair labels to pair products.
For every `q in supp(Q)`, its ordered microfactor copies have identical
neighborhoods, and every active copy has a common neighbor with all other
copies.  Thus the product-support quotient preserves the exact number of
components.  The harness explicitly reconstructs the ordered-pair graph and
asserts equality through `N=6`; no microfactor label is silently discarded.

Simultaneous conjugation by any element of `S_N` intertwines the heat baths,
so one representative of each ordinary endpoint cycle type is complete for
fixed `N`, including the two `A_N` classes when an `S_N` class splits.
An endpoint is feasible at six transpositions exactly when its transposition
defect `N-#cycles` is even and at most six: use a minimal factorization and
pad by adjacent squares.

## Decisive priority result

At `N=6,l=3`, all six feasible endpoint cycle types have one component.  The
ordered-pair graph has `M^2=225` possible vertices per side, compared with
the naive `15^6=11,390,625` six-letter words.  The exact endpoint fiber sizes
are

```text
24,300; 24,640; 31,250; 39,382; 46,413; 72,315,
```

listed in increasing order (the JSON retains the cycle-type order).  The conjugacy-
class-weighted sum of those fibers is exactly `15^6`.  Both quotient levels
return one component for every type.

The same run reproduces:

```text
|Omega(3,4)|=27,
|Omega(4,4)|=120,
|Omega(4,6)|=3936,
```

and matches the prior `N=5,l=3` fiber range `15,625` through `20,860` without
enumerating its million words.

## Extension along the same named claim

The product-support quotient tested every feasible endpoint cycle type for
all `3<=N<=12`.  Every tested graph is connected.  In particular, `N=12` is
the first case containing a defect-six endpoint that moves twelve labels;
all nineteen feasible endpoint types survive.  Exact class-mass assertions
account for `M^6` words in every N, reaching

```text
66^6=82,653,950,016
```

at `N=12` without word enumeration.

This extension is still finite falsification.  It does not establish a
stability theorem in N: the first/last pair products can use labels outside
the endpoint support, and a proof must show how those external-label sectors
communicate uniformly.

## Exact frontier and next attack

The first qualitative proposition after the bounded result is:

> **UNIVERSAL l=3 INCIDENCE CONNECTIVITY.**  For every `N>=3` and every even
> permutation `h` of transposition defect at most six, the bipartite graph on
> `supp(Q_N)` with `a--c` iff `a^{-1}hc^{-1} in supp(Q_N)` is connected after
> deleting isolated vertices.

Even that proposition covers only pair length three.  The full M10 base also
requires every `l<=O(Nlog N)` and an inverse-polynomial Hamiltonian gap.
The next bounded falsification target is the first untested pair length four,
using a constraint/transfer encoding rather than enumerating `M^8` words.

## Halfway verdict

The universal connectivity claim has not been refuted.  The exact priority
case and all structural endpoint types through `N=12` survive, but the result
remains nonterminal finite evidence.
