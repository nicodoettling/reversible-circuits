# Post-referee resource note: arbitrary-product Hurwitz orbits and the sixth-power braid quotient

## Scope and status

This note records two primary-source audits requested after the M05 shuttle
referee.  It does not change the frozen M05 referee report.

1. The arbitrary-fixed-product transposition Hurwitz classification is
   **proved**, using Douvropoulos--Lewis published Theorem 18 (Theorem 4.2 in
   arXiv v2).  Kluitmann's original
   1988 chapter is useful historical provenance but is not needed as a
   mathematical dependency.
2. The idea of obtaining all needed Schreier gaps from property `(T)` of the
   universal quotient in which the braid generators have sixth power one is
   **refuted as a uniform route**: already the three- and four-strand
   quotients have an infinite virtually abelian quotient.  This says nothing
   against property `tau` for the particular finite Hurwitz actions.

Throughout, `(pq)(x)=p(q(x))`; the product of a word is read from left to
right as the abstract group product `t_1...t_k` with this convention.
Douvropoulos--Lewis use the left Hurwitz generator

```text
(a,b) -> (b,b^{-1}ab).
```

For transpositions this is `(a,b)->(b,bab)`.  Its inverse is the other common
project convention.  Replacing every braid generator by its inverse does not
change the orbit relation.

## 1. Exact primary theorem

The relevant source is:

> Theo Douvropoulos and Joel Brewster Lewis, "Hurwitz Orbits on Reflection
> Factorizations of Parabolic Quasi-Coxeter Elements," *Electronic Journal of
> Combinatorics* **31**(1) (2024), #P1.27,
> [doi:10.37236/11787](https://doi.org/10.37236/11787),
> [primary PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v31i1p27/pdf).

The exact chain of statements is below.  **Version-numbering correction:**
the published EJC article renumbers results consecutively: its definition is
Definition 5 and its main result is Theorem 18 (p. 12).  The arXiv v2 PDF
(`2209.00774v2`) instead labels the same passages Definition 2.4 (pp. 3--4)
and Theorem 4.2 (pp. 8--9).  Earlier drafts of this note used the arXiv labels
next to the published citation; the paired labels here supersede that
bibliographic mismatch.

- Equation (1.1), p. 1, defines the displayed Hurwitz convention.
- Conjecture 1.1 in arXiv v2, pp. 1--2, says that two reflection factorizations of a fixed
  `g` have the same Hurwitz orbit exactly when they generate the same subgroup
  `H` and have the same multiset of `H`-conjugacy classes.
- Published Definition 5 (arXiv v2 Definition 2.4, pp. 3--4) defines a
  parabolic quasi-Coxeter element as an
  element possessing a reduced reflection factorization whose factors
  generate a parabolic subgroup.
- Published Theorem 18 (p. 12; arXiv v2 Theorem 4.2, pp. 8--9) proves the
  criterion whenever `g` is a parabolic quasi-Coxeter element of a finite
  Coxeter group.  The theorem treats
  arbitrary-length, not only reduced, reflection factorizations.

The paper's introductory sentence that the symmetric-group orbit structure
was already understood cites Kluitmann and Ben-Itzhak--Teicher, but it is not
the dependency used here.  The original Kluitmann source is Paul Kluitmann,
"Hurwitz action and finite quotients of braid groups," in *Braids (Santa
Cruz, CA, 1986)*, Contemporary Mathematics **78** (1988), 299--325,
[doi:10.1090/conm/078/975086](https://doi.org/10.1090/conm/078/975086).
Its original theorem text was not accessible during this audit.  That source
access remains unresolved, but Douvropoulos--Lewis published Theorem 18
(arXiv v2 Theorem 4.2) supplies a direct modern proof of the needed statement.

## 2. Why published Theorem 18 covers every element of `S_N`

**Lemma.** Every `g in S_N` is a parabolic quasi-Coxeter element of the finite
Coxeter group `S_N` (type `A_{N-1}`).

**Proof.** Let `r(g)` be the number of cycles of `g`, including fixed points.
Multiplication by a transposition changes the number of cycles by exactly one,
so every transposition factorization of `g` has length at least `N-r(g)`.
Factor each disjoint cycle of length `d` into `d-1` transpositions.  The union
of these factorizations has length `N-r(g)`, so it is reduced.  On each cycle
support its factors generate the full symmetric group, and altogether they
generate the Young subgroup which is the direct product of the symmetric
groups on the disjoint cycle supports.  This is a parabolic subgroup of
`S_N`.  Published Definition 5 (arXiv v2 Definition 2.4) applies.  QED.

Consequently published Theorem 18 (arXiv v2 Theorem 4.2) gives the following
exact type-`A` theorem.

**Arbitrary-product transposition orbit theorem.** Fix `N>=2`, `g in S_N`,
and `k>=0`.  Two length-`k` transposition factorizations of `g` lie in the
same Hurwitz orbit if and only if they generate the same subgroup `H<=S_N`
and have the same multiset of `H`-conjugacy classes.

## 3. Exact specialization to graph components and weights

For a transposition tuple `w`, let `Gamma(w)` have vertex set `[N]` and one
edge for every factor, with multiplicity.  Let its labeled connected
components, including isolated vertices, be `C`, and let `k_C` be the number
of factors supported in `C`.

1. Transpositions on the edges of a connected graph on `C` generate `S_C`.
   Hence

   ```text
   <factors of w> = product_C S_C,
   ```

   omitting trivial singleton factors.
2. Conjugation by this direct product cannot move a transposition between
   different components, while all transpositions inside a fixed component
   `C` are conjugate under `S_C`.  Thus the multiset of subgroup-conjugacy
   classes is exactly the list of component weights `k_C` attached to the
   labeled components.
3. Since the fixed product `g` belongs to this direct product, every component
   `C` is invariant under `g`; equivalently, `C` is a union of cycles of `g`.

Therefore:

**Graph form.** Two same-length transposition factorizations of the same
arbitrary `g in S_N` are Hurwitz-equivalent if and only if their factorization
graphs have the same labeled connected components and the same weight on
each component.  There are no additional arbitrary-product invariants.

This strictly extends the identity-only use of Ben-Itzhak--Teicher in the
project.  It is qualitative and supplies no Hurwitz diameter or gap bound.

## 4. Consequence: qualitative arbitrary-endpoint aligned-`H_4` connectivity

Let `m=2l>=4`, let `g in S_N` have a nonempty length-`m` transposition fiber,
and update only the aligned windows

```text
[1,4], [3,6], ..., [m-3,m].
```

Each update is the exact same-product length-four heat bath.  The support
graph of this auxiliary chain is connected for every `N>=3`.

### 4.1 Every adjacent Hurwitz move is present

Every adjacent pair of positions is contained in at least one aligned
four-window.  Applying a Hurwitz move to that pair and leaving the other two
entries unchanged preserves the ordered four-factor product, so it is one of
the positive-probability outputs of that heat bath.  The graph-form theorem
therefore makes every fixed component-and-weight macro-fiber connected.

### 4.2 Square moves connect the macro-fibers

For a component `C`, put `v_C=|C|`, let `q_C` be the number of cycles of
`g|_C`, and let `k_C` be its weight.  Douvropoulos--Lewis Proposition 2.7(4),
specialized to `S_C`, or the standard cycle-count argument, gives

```text
k_C = v_C + q_C - 2 + 2 g_C,       g_C >= 0
```

for every nonsingleton connected component; an isolated fixed point has all
terms zero.  A factorization realizing any required `g_C` is obtained from a
minimum full factorization by appending `g_C` adjacent squares `(e,e)`.

The following operations are in the aligned-`H_4` support:

- An exposed adjacent square `(e,e)` may be replaced by any other square
  `(f,f)`, because both have product identity.  A containing aligned
  four-window always exists, including at either boundary.
- If `f` joins two current components, that replacement merges them and uses
  one square of surplus.
- Conversely, suppose a component `C=A union B` is to be split along unions
  of cycles of `g`.  Choose full factorizations on `A` and `B` with the desired
  remaining surplus and append a bridge square `(f,f)`, `f` crossing `A,B`.
  This is a factorization with the original product, support component, and
  weight, so the graph-form theorem moves the current word to it by Hurwitz
  moves.  Replacing `(f,f)` by a square in a chosen nonsingleton component
  splits `C` and transfers the released pair there.

Here is a direct canonicalization which also handles fixed points.  If `g` has
a nontrivial cycle `D`, split every other cycle away from its current
component and transfer every released bridge square and every surplus square
to an edge inside `D`.  This reaches the macro in which every cycle of `g` is
its own component, every fixed point is isolated, and all excess pairs are
stored on `D`.  At every split, a pre-update target of the form

```text
(full factorization on A) (full factorization on B) (bridge f,f)
```

exists with the original component weight; the orbit theorem supplies the
Hurwitz path to that target.

If `g=id`, choose any active edge pair as a temporary anchor.  Since `m>=4`,
some nonsingleton component exists.  Split all other vertices into isolates,
replacing each released bridge square by a square on the anchor, and transfer
all remaining squares to it.  Finally replace the anchor squares by squares
on the fixed designated edge `(1,2)`.  The result is the word consisting of
`m` copies of `(1,2)`, with every other vertex isolated.  Thus all words reach
one canonical macro.

### 4.3 Boundary audit

- If `m=4`, the only aligned window is the whole word, so connectivity is also
  immediate from the whole-word heat bath.
- At absolute minimum length `m=N-r(g)`, there is no square surplus.  Every
  cycle of `g` is necessarily its own component (fixed points are isolated),
  so the macro is unique and the Hurwitz theorem alone connects it.  Thus the
  absence of a square does not create an unhandled minimal endpoint.
- `m=2` has no aligned four-window and is excluded.  Odd `m` cannot represent
  an even endpoint; the auxiliary bridge statement is only for nonempty
  even-length fibers.  `N=2` is outside the requested regime and is elementary.
- This is only support connectivity.  The cited theorem gives no polynomial
  path length, congestion, or spectral gap.

## 5. Why each local Hurwitz generator has sixth power one

On a pair of transpositions `(a,b)`, a Hurwitz generator has order

```text
1  if a=b,
2  if a and b are disjoint,
3  if they share exactly one vertex.
```

Thus, as a permutation of any transposition-word fiber, its order divides
`lcm(1,2,3)=6`.  The braid action factors through

```text
B_k(6) := B_k / << sigma_1^6 >>,
```

where one normal relation suffices because the standard braid generators are
conjugate.

The exact primary finiteness result is reproduced as Theorem 4 in:

> Renato Diniz, Oscar Ocampo, and Paulo Cesar Cerqueira dos Santos Júnior,
> "Coxeter-type quotients of surface braid groups," *Comptes Rendus
> Mathématique* **364** (2026), 27--37,
> [doi:10.5802/crmath.813](https://doi.org/10.5802/crmath.813),
> [primary PDF](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.813.pdf).

Their Theorem 4 (p. 30), citing Coxeter's original theorem, states that for
`p>=3`, `B_n(p)` is finite exactly for

```text
(n,p) in {(3,3),(3,4),(3,5),(4,3),(5,3)}.
```

In particular `B_n(6)` is infinite for every `n>=3`.  Infinitude alone does
not preclude property `(T)`, but the low-strand quotients have a sharper
obstruction.

Write `B_3=<a,b | aba=bab>`.  Quotienting by its center gives

```text
B_3/Z(B_3) = <x,y | x^2=y^3=1>,    a=y^{-1}x.
```

Imposing `a^6=1` and then quotienting by the center therefore gives

```text
<x,y | x^2=y^3=(y^{-1}x)^6=1> = Delta(2,3,6),
```

the Euclidean triangle group, which is virtually `Z^2`.  Hence `B_3(6)` does
not have property `(T)`.  The assignment

```text
sigma_1 -> a,  sigma_2 -> b,  sigma_3 -> a
```

defines a surjection `B_4 -> B_3` (both adjacent braid relations become
`aba=bab`, and the nonadjacent pair maps to `(a,a)`).  It descends to
`B_4(6) -> B_3(6)`.  Thus `B_4(6)` also lacks property `(T)`.

Property `(T)` passes to quotients, so there is no theorem asserting property
`(T)` for this universal sixth-power quotient uniformly over all strand
counts.  This rejects that automatic route to the required Schreier gaps.

It does **not** reject either of the following:

- property `tau` for the particular family of finite permutation images
  arising from transposition Hurwitz actions;
- a direct polynomial gap bound for their marked Schreier graphs.

Even when an image is a full symmetric or alternating group, its abstract
isomorphism type supplies no uniform gap for the particular adjacent-Hurwitz
generating tuple.  Kassabov's explicit expanding generating sets cannot be
substituted without a bounded comparison.  No primary theorem giving the
needed property-`tau`/Kazhdan bound for these exact marked actions was found
in this focused audit.

## 6. Exact outcome

**PROVED:** for every `N>=2`, every `g in S_N`, and every length `k`, fixed-
product transposition Hurwitz orbits are classified exactly by the generated
subgroup and its factor-class multiset, equivalently by labeled graph
components and weights.  Consequently every nonempty even-length
arbitrary-endpoint aligned-`H_4` fiber is qualitatively connected for
`N>=3,m>=4`.

**REFUTED AS A ROUTE ONLY:** property `(T)` of the universal quotient
`B_k(6)` cannot be the uniform source of polynomial Schreier gaps.  The first
unproved quantitative statement remains a polynomial spectral-gap or
property-`tau` theorem for the exact finite Hurwitz actions; neither the orbit
classification nor the sixth-power relation supplies it.

## Reproduction trail

Primary PDFs were inspected with:

```text
pdftotext -layout /tmp/m08-reflection-orbits.pdf /tmp/m08-reflection-orbits.txt
sed -n '235,315p' /tmp/m08-reflection-orbits.txt
sed -n '625,655p' /tmp/m08-reflection-orbits.txt

pdftotext -layout /tmp/m08-coxeter-quotients.pdf /tmp/m08-coxeter-quotients.txt
sed -n '300,332p' /tmp/m08-coxeter-quotients.txt
```

No finite computation is used as evidence for either universal statement.
