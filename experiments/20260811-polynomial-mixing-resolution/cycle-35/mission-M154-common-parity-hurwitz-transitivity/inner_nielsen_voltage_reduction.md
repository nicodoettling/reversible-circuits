# Inner-Nielsen lifting and the exact parity-voltage frontier

Date: 2026-08-13 UTC.

## 1. Scope, target, and convention

For `d>=3`, put `m=2d-2` and

```text
Z_d={(t_1,...,t_m): each t_j is a transposition in S_d,
                         t_1...t_m=id,
                         support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  The chronological signed right-Hurwitz moves are

```text
R_j(a,b)=(b,b^(-1)ab),
R_j^(-1)(a,b)=(aba^(-1),a).                           (1.1)
```

For transpositions these are the project's formulas `(b,bab)` and
`(aba,a)`.  A “literal orbit” below means the orbit under these moves only.
It does **not** silently quotient by simultaneous conjugation.

For `s>=1`, define

```text
P_(d,s)={(g_1,...,g_s) in S_d^s:
                         sgn(g_1)=...=sgn(g_s)},       (1.2)
C_(d,s)={(t_1,...,t_s): every t_q is a transposition}.
```

The target in this note is a Hurwitz action orbit on product-one generating
`C_(d,s)`-factorizations.  No Markov kernel, spectral gap, or global sampler
claim is made.

## 2. Inner conjugation is already a literal braid

The following elementary observation removes one convention ambiguity from
the remaining DPS problem.

### Lemma 2.1 (last-factor conjugation braid; **PROVED**)

Let `G` be any group and let

```text
X=(x_1,...,x_m),             x_1...x_m=1.             (2.1)
```

Perform the following `2(m-1)` positive Hurwitz moves in chronological
order:

```text
R_(m-1),R_(m-2),...,R_1, R_1,R_2,...,R_(m-1).        (2.2)
```

The result is

```text
x_m^(-1) X x_m
=(x_m^(-1)x_1x_m,...,x_m^(-1)x_mx_m).                (2.3)
```

**Proof.**  The descending half of (2.2) moves the last factor to the first
slot and gives

```text
(x_m,x_m^(-1)x_1x_m,...,x_m^(-1)x_(m-1)x_m).         (2.4)
```

Write the trailing factors as `y_1,...,y_(m-1)`.  The ascending half moves
the first factor to the final slot and gives

```text
(y_1,...,y_(m-1),(y_1...y_(m-1))^(-1)
                         x_m(y_1...y_(m-1))).         (2.5)
```

Equation (2.1) makes `y_1...y_(m-1)=x_m^(-1)`, so the last entry in (2.5)
is `x_m`; all other entries are already those in (2.3).  QED.

### Theorem 2.2 (generated inner conjugations; **PROVED**)

If the factors of `X` generate `Gamma<=G`, then every simultaneous
`Gamma`-conjugate of `X` lies in the literal signed-Hurwitz orbit of `X`.

More quantitatively, if `p in Gamma` has word length `ell` in the symmetric
generating set `{x_1^(+/-1),...,x_m^(+/-1)}`, then a braid word of length at
most

```text
(4m-4) ell                                               (2.6)
```

maps `X` to `p^(-1)Xp` (up to replacing `p` by `p^(-1)`, which has the same
word length).

**Proof.**  To use factor `x_i`, chronologically apply

```text
R_i^(-1),R_(i+1)^(-1),...,R_(m-1)^(-1).               (2.7)
```

At every step the left entry of the moved pair becomes the unchanged right
entry, so (2.7) carries the original `x_i` unchanged to the final slot.
Apply Lemma 2.1 there, then undo (2.7).  Hurwitz moves commute with
simultaneous conjugation, so the net result is `x_i^(-1)Xx_i`.  Its length
is at most

```text
2(m-i)+2(m-1) <= 4m-4.                                (2.8)
```

The inverse braid realizes conjugation in the other direction.  Concatenate
these words along any length-`ell` expression for `p`.  QED.

### Corollary 2.3 (literal orbit equals inner Nielsen orbit; **PROVED**)

On product-one factorizations that generate `Gamma`, two tuples are in one
literal signed-Hurwitz orbit if and only if their simultaneous
`Gamma`-conjugacy classes are in one braid orbit.

**Proof.**  One direction is quotienting.  Conversely, if a braid maps `X`
to `pYp^(-1)` for some `p in Gamma`, Theorem 2.2 supplies a further literal
braid that removes this conjugation.  QED.

This result applies to the **inner** quotient only.  It does not identify the
coarser quotient by a larger normalizer.

## 3. Application to aligned M135 matching families

Fix `d>=5`, one M135 incidence matching, and a nonempty subfamily `I` of
size `s`.  Choose physical representatives `u^q` and put
`v^q=tau_i(u^q)`.  Package their aligned factors as

```text
X_j=(u_j^q)_(q in I),       Y_j=(v_j^q)_(q in I),
1<=j<=m.                                               (3.1)
```

Accepted M141/M143 proves literally that

```text
<X_1,...,X_m>=<Y_1,...,Y_m>=P_(d,s).                 (3.2)
```

### Corollary 3.1 (exact inner-Nielsen reduction; **PROVED**)

For every such aligned `d>=5` subfamily, `X` and `Y` are connected by one
literal common signed braid if and only if their simultaneous
`P_(d,s)`-conjugacy classes are connected by a braid.

Thus a theorem stated only modulo **inner** `P_(d,s)` conjugacy is sufficient
for qualitative physical realization.  A theorem stated modulo all of
`S_d^s` is not sufficient without the parity check in Section 4.

The length clause is material.  If a quotient braid has length `L` and its
remaining inner transporter has aligned-generator word length `ell`, the
literal lift supplied here has length at most

```text
L+(4m-4)ell.                                           (3.3)
```

M141 proves generation but no polynomial bound on `ell`; no polynomial braid
length is inferred from Corollary 3.1.

## 4. Absolute quotient and the parity-voltage criterion

Let

```text
Q_d=Z_d/S_d                                             (4.1)
```

for simultaneous global relabeling in one physical coordinate.  The action
is free for `d>=3`: a relabeling that fixes a connected word centralizes its
transposition factors, hence all of `S_d`, whose center is trivial.

Fix physical aligned representatives `U=(u^1,...,u^s)` and
`V=(v^1,...,v^s)`.  Suppose a braid `b` maps every source absolute class to
its target class.  Freeness gives unique transporters `rho_q in S_d` with

```text
b.u^q=rho_q.v^q=(rho_q v_1^q rho_q^(-1),...,
                 rho_q v_m^q rho_q^(-1)).             (4.2)
```

Define the relative voltage

```text
epsilon_b(U,V)=(sgn(rho_1),...,sgn(rho_s)) mod Delta
                 in F_2^s/Delta,                      (4.3)
Delta={(e,...,e):e in F_2}.                           (4.4)
```

### Theorem 4.1 (exact quotient-voltage criterion; **PROVED**)

Assume the aligned factors of `V` generate `P_(d,s)`.  There is a literal
common signed braid from `U` to `V` if and only if there is a braid `b` such
that

```text
b.[u^q]=[v^q] in Q_d for every q,
epsilon_b(U,V)=0.                                     (4.5)
```

If `b` has length `L` and the transporter tuple
`rho=(rho_1,...,rho_s)` has word length `ell` in the aligned factors after
`b`, the constructed literal braid has length at most (3.3).

**Proof.**  A literal endpoint equality gives (4.5) with every transporter
the identity.  Conversely, zero voltage says that all transporter parities
agree, so `rho in P_(d,s)`.  Equation (4.2) says `b.U=rho.V.rho^(-1)`.
Theorem 2.2, applied after `b`, removes `rho` and reaches `V`.  Its
quantitative construction gives (3.3).  QED.

This theorem is the precise repair to an unsafe “modulo conjugacy implies
literal realization” inference.  The normalizer quotient is

```text
S_d^s/P_(d,s) ~= F_2^s/Delta.                         (4.6)
```

The triviality of the centralizer of the generated group makes each
transporter unique, but it does **not** alone prove that a braid stabilizer
cannot carry nonzero voltage.  That would be an additional Nielsen-orbit
statement.

## 5. Exact rank-three framing split

The independent checker closes the full signed-Hurwitz action on the `24`
words of `Z_3`.  There are four free global `S_3`-orbits.  The quotient image
has order `12` and is `A_4` on these four points.

Consider all ordered physical pairs whose two entries lie in distinct global
orbits.  M135's rank-three Goursat dichotomy makes every such pair generate
`P_(3,2)`.  There are

```text
4*3*6^2=432                                             (5.1)
```

such pairs.  Exact diagonal action closure splits them into two literal
orbits, each of size `216`.  From one representative pair:

```text
even/even coordinate conjugation   reachable,
odd/odd coordinate conjugation     reachable,
even/odd or odd/even                not reachable.     (5.2)
```

The two orbits are therefore the two relative framing classes in
`S_3^2/P_(3,2)`.  This is an **EXACT FINITE** refutation of the unqualified
framed strong theorem at `d=3`.  It is not a counterexample to the assigned
`d>=5` statement.

It also demonstrates why an absolute quotient orbit cannot be promoted as a
literal common braid without (4.3).

## 6. The exact rank-four exceptional block

Let

```text
pi:S_4 -> S_3                                             (6.1)
```

be the action on the three perfect matchings of `K_4`.  Its kernel is `V_4`.
Every transposition of `S_4` swaps two of the matchings, hence maps to a
transposition of `S_3`.  Applying `pi` factorwise defines a Hurwitz-equivariant
map

```text
Phi:Q_4 -> Q_(3,6),                                    (6.2)
```

where `Q_(3,6)` is the set of global-conjugacy classes of connected
product-one length-six transposition words in `S_3`.  Connectedness is
automatic: if every projected factor were the same `S_3` transposition,
every original factor would lie among one pair of disjoint `S_4`
transpositions, contradicting connected support on four vertices.

The exact clean-room reconstruction gives

```text
|Q_4|=120,       |Q_(3,6)|=40,
every Phi-fiber has size 3.                            (6.3)
```

These fibers form a braid block system.  Independent Schreier--Sims closure
of the five positive quotient generators gives

```text
image order = 20652142670561646642588549120
            = 2^22 * 3^44 * 5,
subdegrees  = [1,2,36,81],
40 minimal blocks of size 3.                          (6.4)
```

The minimal blocks in (6.4) equal the `Phi`-fibers literally.  Hence the
candidate assertion that the quotient image is alternating in every rank is
**REFUTED at `d=4`**.

This invariant also detects the accepted M135 rank-four pair witness.  Its
two sources have equal `Phi`-value, while its two targets have unequal
`Phi`-values.  A common braid preserves equality of `Phi`-values, so the
pair cannot have a common literal braid.  This is the same rank-four
exception already handled by M135's singleton patch; it supplies no
`d>=5` obstruction.

For calibration, the reconstructed deterministic Hall decompositions were
also tested.  At every adjacent DPS edit, only `126` of the `480` incidence
edges keep the same absolute `Phi` label, and most matching-color maps break
the `Phi` block relation on many pairs.  These are exact rank-four facts, not
an asymptotic claim.

## 7. Tightly capped rank-five quotient test

At `d=5`, exact orbit closure from one quotient state reaches

```text
5^(5-3)*(8!)/5! = 8400                                (7.1)
```

states, the full accepted DPS quotient count.  The seven positive quotient
Hurwitz generators are all even permutations and generate a transitive,
primitive degree-`8400` group.  Their common cycle histogram is

```text
1^660 2^1440 3^1620.                                  (7.2)
```

The degree-`8400` group was deliberately not closed.  Primitivity is an
**EXACT FINITE** falsification check; it proves neither an alternating image
nor high transitivity.

For comparison, the exact quotient actions at `d=3,4` are also transitive;
`d=3` is primitive and `d=4` is imprimitive by Section 6.  All positive
generators are even in the three tested ranks.  No universal parity theorem
is inferred from these rows.

## 8. Exact remaining lemma

The accepted polynomial matching-coset obligation can now be restated more
concretely.

> **POLYNOMIAL MATCHING QUOTIENT-VOLTAGE ROUTING.**  For `d>=5`, every
> adjacent DPS edit and every M135 perfect matching can be refined into at
> most `d^C` total subfamilies `I` such that, for each `I`, there is a braid
> of length at most `d^C` mapping every ordered source point in `Q_d` to its
> matched target, with zero relative voltage (4.3), and with the remaining
> `P_(d,|I|)` transporter having aligned-generator word length at most
> `d^C`.

This is **UNRESOLVED**.  It is strictly more explicit than the prior abstract
intersection of action cosets: the two independent obligations are quotient
routing and a zero/short voltage lift.

A tempting further candidate is:

> **QUOTIENT ALTERNATING IMAGE.**  For `d>=5`, the positive Hurwitz image on
> `Q_d` is `Alt(Q_d)`.

This candidate is **UNRESOLVED** and is only finitely consistent with the
primitive even image at `d=5`; its all-rank version is refuted by Section 6.
Even a proof for `d>=5` would address quotient existence after splitting a
matching into proper subfamilies, but would not by itself prove zero voltage
or a `d^O(1)` word-length bound.

Any Conway--Parker-style or connected-Hurwitz classification invoked here
must state whether it classifies literal, inner, or absolute Nielsen classes,
its stable range, its class and generation hypotheses, and whether it gives
an effective polynomial braid word.  No such unverified theorem is used in
this note.

## 9. Dependency and claim ledger

- **Proved here:** Lemma 2.1, Theorem 2.2, Corollary 2.3, Corollary 3.1,
  Theorem 4.1, and the elementary construction of `Phi`.
- **Accepted frozen input:** M135/M137 incidence matchings and rank-four
  witness; M141/M143 common-parity generation for every nonempty `d>=5`
  matching subfamily; M146/M148 factor-class collapse; M150/M153 constancy
  of the reduced Pin descriptor.
- **Exact finite:** the complete `d=3` framing split; the `d=4` quotient
  image, minimal blocks, exceptional-quotient identification, witness, and
  deterministic matching rows; `d=5` quotient transitivity/primitivity and
  generator cycle data.
- **Refuted:** unqualified framed transitivity at `d=3`; all-rank quotient
  alternating image at `d=4`; any inference from absolute quotient
  transitivity alone to literal realization.
- **Unresolved:** the assigned `d>=5` broad transitivity theorem, the narrower
  M135 quotient-voltage routing lemma, polynomial correction length, and any
  complete Nielsen classification.
- **Not claimed:** a physical minimal-sector gap, all-edge comparison,
  original lazy exact `{3,4,5}` heat-bath gap, Terminal A, or Terminal B.
