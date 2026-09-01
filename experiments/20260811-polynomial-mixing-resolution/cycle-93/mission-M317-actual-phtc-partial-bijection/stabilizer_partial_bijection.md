# M317: Stabilizer Partial-Bijection Extension for Actual PHTC

Date: 2026-08-14 UTC.

Status: **exact partial-map and orbital characterizations proved;
`SPBE => PHTC => WRAD` proved; generic use of M135 conflict coloring is
obstructed; actual `d>=6` SPBE remains unresolved.**

## 1. Scope, target, and convention

The ambient sampler target remains uniform on the global fixed-length
identity bridge for the lazy exact same-product `{3,4,5}` heat-bath chain.
This mission works only on the finite-action agreement problem for one actual
M135 perfect matching in the minimal connected sector

```text
Z_d={w in Transpositions(S_d)^(2d-2):
       product(w)=id, support(w) connected}.
```

Fix `d>=6`, one adjacent edit index, one actual matching `M`, and nonzero
weights `lambda>=0`.  Signed Hurwitz words act on the right and chronological
multiplication is

```text
w^(g;h)=(w^g)^h.
```

Let `A` be the finite signed-Hurwitz action image on `Z_d`, let `c` be the
doubled-star chart, and let

```text
Sbar=Stab_A(c).
```

M296/M299 identifies `Sbar` as the finite projection of the literal chart
stabilizer.  Everything below concerns finite nonemptiness.  Polynomial
shortest literal braid length is not inferred.

## 2. The exact residual partial map

Choose the positive-weight anchor used in M312's outer normalization.  At a
compatible ordered pivot tuple `I`, choose `s_I in T_I` and put

```text
H_I={h in Sbar:x_P^h=x_P for every P in I},
z_Q^I=y_Q^(s_I^(-1)),
D_I(Q)={h in H_I:x_Q^h=z_Q^I}.                       (2.1)
```

For any further family `V`, form tagged tuples

```text
a_(I,V)=((x_P)_(P in I),(x_Q)_(Q in V)),
b_(I,V)=((x_P)_(P in I),(z_Q^I)_(Q in V)).           (2.2)
```

Repeated points are retained in these tuples.

### Proposition 2.1 (partial-map realization; **PROVED**)

```text
intersection_(Q in V) D_I(Q)
 ={h in Sbar:a_(I,V)^h=b_(I,V)}.                    (2.3)
```

Consequently the intersection is nonempty exactly when the source and target
tuples in (2.2) lie in the same diagonal `Sbar`-orbit, equivalently when the
partial prescription

```text
f_(I,V)(x_P)=x_P,       P in I,
f_(I,V)(x_Q)=z_Q^I,     Q in V                       (2.4)
```

is the restriction of one element of `H_I`.

#### Proof

The equations on the pivot coordinates in (2.2) say exactly that `h` lies in
`H_I`.  The remaining coordinate equations are exactly membership in every
`D_I(Q)`.  This proves (2.3), and the orbit and restriction formulations are
definitions of the same simultaneous equations.  QED.

If nonempty, (2.3) is one left coset of the pointwise stabilizer in `H_I` of
the distinct points among `(x_Q)_(Q in V)`.  This coset description does not
make its nonemptiness automatic.

## 3. Exhaustive obstruction ladder

The exact characterization (2.3) separates every obstruction to extending
the displayed source-target prescription.

### 3.1 Equality, injectivity, and pivots

For tagged indices `R,R'` from `I union V`, any realizing permutation forces

```text
a_R=a_(R')  iff  b_R=b_(R').                         (3.1)
```

The forward implication makes (2.4) well-defined; the reverse implication
makes it injective.  Because each pivot target equals its source, (3.1) also
contains the base-pivot rules:

- a residual source equal to a pivot must target that same pivot;
- a residual source outside the pivot set cannot target a pivot;
- two equal residual sources must have equal targets, and two distinct
  residual sources must have distinct targets.

These conditions are necessary and sufficient for (2.4) to be an injective
partial map fixing the pivot set.  They are not sufficient for membership in
the actual stabilizer action.

### 3.2 One-orbit and pair-orbital constraints

Individual extendability is

```text
D_I(Q)!=empty
iff x_Q and z_Q^I lie in the same H_I-orbit.          (3.2)
```

For two residual constraints,

```text
D_I(Q) intersect D_I(R) != empty
iff (x_Q,x_R) and (z_Q^I,z_R^I)
    lie in the same diagonal H_I-orbit.              (3.3)
```

Thus a pairwise-consistent residual partial map preserves every orbital,
meaning every `H_I`-orbit on ordered pairs.  The diagonal orbital includes
the equality kernel (3.1).

### 3.3 Higher-tuple obstruction

For `r=|V|`, full extension is the `r`-tuple orbit condition (2.3).  Equality
of every corresponding pair orbital does not imply equality of the full
tuple orbit for a general permutation group.  Equivalently, the relational
structure having one binary relation for each `H_I` orbital need not extend
each of its partial isomorphisms to an element of `H_I`.

This is exhaustive: after (3.1)--(3.3), the sole remaining question is
whether the two complete tuples in (2.2) occupy one `H_I`-orbit.  Calling the
action "binary" would itself be a new theorem; neither transitivity nor equal
point-fiber size proves it.

### Proposition 3.1 (covariance; **PROVED**)

Changing the node witness by `s'_I=g;s_I`, `g in H_I`, sends every target
to `(z_Q^I)^(g^(-1))` and every residual signature to
`D_I(Q);g^(-1)`.  Hence all pair and full intersections are right-translated
uniformly.  Accepted frame changes conjugate `H_I` and every residual
signature uniformly by the reference source factor.  Therefore the
partial-map, orbital, pairwise-consistency, and extension predicates above
are intrinsic.

#### Proof

This is direct substitution into (2.1), followed by M312/M315's accepted
witness and frame covariance laws.  Uniform right translation and uniform
conjugation preserve every asserted nonemptiness equivalence.  QED.

## 4. The predeclared SPBE candidate

For `U=supp(lambda)`, M312 defines

```text
V_I(U)=G_I(U)={Q in U:D_I(Q)!=empty}.                 (4.1)
```

The candidate fixed in `plan.md` before computation is:

> **STABILIZER PARTIAL-BIJECTION EXTENSION (SPBE).**  There are universal
> constants `B,C` such that every weighted actual `d>=6` matching admits a
> positive-weight anchor and a compatible pivot tuple `I`, `|I|<=d^B`, for
> which, writing `V=V_I(U)`:
> 1. `lambda(V)>=||lambda||_1/d^C`;
> 2. `D_I(Q) intersect D_I(R)` is nonempty for every `Q,R in V`;
> 3. every pairwise-consistent partial map of the actual form (2.4) at this
>    node extends to an element of `H_I`.

Item 3 is an actual chart-stabilizer homogeneity assertion, not a theorem
about arbitrary permutation groups.

### Theorem 4.1 (`SPBE => PHTC => WRAD`; **PROVED conditionally on SPBE**)

SPBE implies M312's PHTC with the same pivot and weight exponents.  PHTC
implies WRAD with the same weight exponent.

#### Proof

By SPBE item 2, the map (2.4) on all of `V=G_I(U)` is pairwise consistent.
Item 3 and Proposition 2.1 give

```text
intersection_(Q in G_I(U))D_I(Q) != empty.           (4.2)
```

Together with item 1 and `|I|<=d^B`, this is exactly PHTC.

Choose `h` in (4.2).  M312's higher-arity law puts `h;s_I` in every
normalized constraint `C_Q`, `Q in G_I(U)`.  The fixed-anchor weighted score
is therefore at least `lambda(G_I(U))`.  Taking the outer maximum over the
chosen positive-weight anchor proves WRAD.  QED.

The whole set `G_I(U)` is material.  If an arbitrary heavy subcell
`J subsetneq G_I(U)` extends, its common action proves WRAD directly on the
retained weight, but it does **not** show that the original PHTC node is
collapsing.  No subcell-to-PHTC implication is used here.

## 5. Why M135 conflict coloring does not discharge SPBE

M135/M137 proves that an actual incidence matching is independent for the
paired-generated-subgroup conflict invariant.  This means the paired
subgroup before and after the edit is unchanged.  It is only a necessary
invariant for diagonal signed-Hurwitz realizability.

At a residual node, SPBE item 2 instead requires the exact orbit statement
(3.3) inside the pointwise chart stabilizer `H_I`.  No accepted implication
connects paired-subgroup equality to that exact orbital condition.

There are two exact boundary warnings:

1. M135/M137's `d=3` matching colors are conflict-independent, but
   M301/M304 proves that no complete `d=3` matching is pairwise compatible.
   Thus conflict independence does not formally imply exact pairwise
   transporter compatibility.
2. M301/M304's actual edges `[0,2,9]` have every pair of global endpoint
   fibers intersecting but empty triple intersection.  In tuple language,
   every corresponding pair of coordinates lies in one diagonal action
   orbit, while the three source and target coordinates lie in different
   full tuple orbits.  Thus pairwise-to-full extension fails in an actual
   finite Hurwitz action at the boundary rank.

Neither fact refutes SPBE as stated for actual `d>=6`.  Together they prove
that its pairwise-cell and extension clauses require new all-rank,
actual-specific theorems; neither follows from the accepted formal geometry.

## 6. Generic Sym/Alt extension and its exact limit

The formal natural actions from M306/M312 are useful calibration models, but
they are not the actual chart action.

### Proposition 6.1 (natural symmetric extension; **PROVED**)

Let `X` be finite, fix `B subset X` pointwise, and let
`H=Sym(X)_(B)`.  Every injective partial map on `X` that fixes `B`, maps no
outside point into `B`, and respects (3.1) extends to an element of `H`.

#### Proof

On `X\B`, the partial injection has equally many unused sources and targets.
Complete it by any bijection between those two finite sets and fix `B`.
QED.

### Proposition 6.2 (natural alternating extension with slack; **PROVED**)

Let `H=Alt(X)_(B)` and put `R=X\B`.  Such a partial bijection extends to
`H` whenever at least two points of `R` are outside its domain.  With zero or
one unused point, the bijective completion is unique and extension occurs
exactly when that completion is even.

#### Proof

First complete the partial map to a permutation of `R`.  If it is odd and
two source points are unused, precompose it with their transposition.  This
does not alter any prescribed source image and toggles parity.  With at most
one unused source, the remaining bijection is forced, so its parity is the
exact obstruction.  QED.

The parity qualification is genuinely higher arity.  For `|R|>=4`, prescribe
an odd permutation on all of `R`.  Every two-point restriction extends to an
even permutation because at least two points remain free, while the complete
map does not extend to `Alt(R)`.

The actual `Sbar=Stab_A(c)` is not known to be a full symmetric or alternating
group on the complement of the pivots, nor is its pointwise stabilizer
`H_I` known to have the extension property in Propositions 6.1--6.2.  The
M306/M312 formal Sym/Alt examples cannot be imported as actual M135
monodromy theorems.

## 7. Strongest surviving two-gate interface

SPBE factors into two separately falsifiable obligations:

> **HEAVY PAIRWISE RESIDUAL NODE (HPRN).**  Find the positive anchor and a
> compatible `|I|<=d^B` for which `V=G_I(U)` has inverse-polynomial weight
> and every pair of its residual signatures intersects.

> **ACTUAL PARTIAL-ORBITAL HOMOGENEITY (APOH).**  At every selected HPRN
> node, every actual residual partial map preserving all `H_I` orbitals
> extends to one element of `H_I`.

```text
HPRN + APOH  =>  SPBE  =>  PHTC  =>  WRAD.           (7.1)
```

HPRN is not supplied by M135's coarser conflict coloring.  APOH is not
supplied by transitivity, uniform fibers, transporter-coset form, or the
formal Sym/Alt calibration.  Both are **UNRESOLVED for actual `d>=6`**.

If one instead obtains only a polynomial-weight pairwise-compatible subcell
`J`, APOH would give one action agreeing on `J` and hence WRAD directly.  That
weaker route bypasses, rather than proves, PHTC.

No selected `d=6` guard was run.  Constructing the exact chart-stabilizer
orbitals at that rank would require the forbidden broad universe/action
census; a single unexplained finite matching would not prove either HPRN or
APOH asymptotically.

## 8. Exact stopping line

```text
residual signature = partial-map constraint             proved
full intersection = full tuple-orbit equivalence         proved
pairwise intersection = pair-orbital equivalence         proved
generic Sym extension                                    proved
generic Alt extension with two-point slack               proved
SPBE => PHTC => WRAD                                      proved conditional
M135 conflict independence => exact pair compatibility   refuted at d=3; no d>=6 implication
actual d>=6 HPRN                                          unresolved
pairwise residual consistency => full extension           unresolved at d>=6; false generically/boundary d=3
actual d>=6 SPBE/PHTC/WRAD                                unresolved
polynomial literal representative length                  unresolved separately
```

No MRAD, SSTID, literal route, voltage correction, congestion, spectral gap,
mixing, or Terminal conclusion is inferred.
