# Multisource common-parity theorem for one M135 matching

Date: 2026-08-13 UTC.

## 1. Scope, target, and convention

For `d>=2`, put `m=2d-2` and

```text
Z_d={(t_1,...,t_m):t_1...t_m=id,
                         support connected on [d]}.
```

The auxiliary target is uniform on `Z_d`.  Permutations compose as
`(pq)(x)=p(q(x))`; displayed factors multiply left-to-right.  Signed
right-Hurwitz moves are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

Fix an adjacent DPS edit `tau_i`.  Let `G=S_d`, let `H=Stab_G(d)`, and let
`B_(d,i)` be M135's bipartite orbit-incidence multigraph.  Its edges are the
`H`-orbits in `Z_d`; the endpoints of an edge are the source global
`G`-orbit and the target global orbit after `tau_i`.  A matching means any
set of edges with no common left or right endpoint.  In particular, every
color class in M135's proper `d`-edge-coloring of the `d`-regular graph
`B_(d,i)` is a perfect matching.  The theorem below is stated for an
arbitrary matching, which is slightly stronger than the mission's required
application to one such perfect-matching color.

This note proves a group-invariant theorem inside the accepted
**POLYNOMIAL MATCHING-COSET REFINEMENT** frontier.  It does not prove that a
matching, or any large part of one, is realized by a common signed braid.

## 2. The aligned multisource invariant

Let `M` be a matching in `B_(d,i)`.  For every edge `q in M`, choose an
arbitrary physical representative

```text
u^q=(u_1^q,...,u_m^q) in Z_d,
v^q=tau_i(u^q)=(v_1^q,...,v_m^q).
```

For a nonempty subfamily `I subseteq M` of size `s`, set

```text
Gamma_U(I)=<(u_j^q)_(q in I):1<=j<=m> <= S_d^s,       (2.1)
Gamma_V(I)=<(v_j^q)_(q in I):1<=j<=m> <= S_d^s.       (2.2)
```

The coordinate order is any fixed order on `I`.  Define

```text
P_(d,s)={(g_1,...,g_s) in S_d^s:
                       sgn(g_1)=...=sgn(g_s)}.         (2.3)
```

For `s=1`, the parity condition is vacuous and `P_(d,1)=S_d`.

### Lemma 2.1 (necessary diagonal-Hurwitz invariant; **PROVED**)

If one signed braid acts simultaneously on the words `(u^q)_(q in I)` and
maps them to `(v^q)_(q in I)`, then

```text
Gamma_U(I)=Gamma_V(I).                                (2.4)
```

**Proof.**  Package the factors at position `j` into one element
`x_j=(u_j^q)_(q in I)` of `S_d^s`.  A diagonal right-Hurwitz move replaces

```text
(x_j,x_(j+1)) by (x_(j+1),x_(j+1)^(-1)x_j x_(j+1)),
```

and its inverse performs the inverse Nielsen transformation.  Either pair
generates the same subgroup.  Iterate along the signed braid word.  QED.

Equality (2.4) is only necessary.  M135/M137's `d=3` calculation already
shows that pairwise generated-subgroup compatibility need not give a common
braid.

## 3. Pairwise-full direct powers

The only new abstract group input is the following elementary lemma.

### Lemma 3.1 (pairwise-full simple-power lemma; **PROVED**)

Let `S` be a nonabelian simple group and `L<=S^s`.  If

```text
pi_(a,b)(L)=S x S                                      (3.1)
```

for every distinct pair of coordinates, then `L=S^s`.  For `s=1`, the same
conclusion holds under the single-coordinate surjectivity assumption.

**Proof.**  The cases `s=1,2` are immediate.  Induct on `s>=3`.  By the
induction hypothesis, projection to the first `s-1` coordinates maps `L`
onto `S^(s-1)`.  Its kernel has the form

```text
{1}^(s-1) x K,
```

where `K` is normal in `S`: conjugate a kernel element by a lift in `L` of
an arbitrary last-coordinate element.  Simplicity gives `K=1` or `K=S`.

If `K=S`, the full kernel together with surjectivity onto the first `s-1`
coordinates gives `L=S^s`.

Suppose instead that `K=1`.  Then `L` is the graph of a surjective
homomorphism

```text
f:S^(s-1) -> S.                                        (3.2)
```

The image under `f` of each direct factor is normal in `S`, hence is either
trivial or all of `S`.  Images of distinct factors commute.  At least one
image is all of `S` by surjectivity, and at most one can be all of `S`
because `S` is nonabelian.  Consequently `f` is an automorphism composed
with projection onto one coordinate, say coordinate `a`.  The `(a,s)`
projection of `L` is then the graph of that automorphism, contradicting
(3.1).  Thus `K=S` and the induction closes.  QED.

This proof is the direct-power subdirect-product classification needed here.
In particular, every possible diagonal block coupling, whether twisted by an
inner or outer automorphism, creates a proper graph in some two-coordinate
projection and is excluded by (3.1).

## 4. Main theorem

### Theorem 4.1 (multisource common-parity theorem; **PROVED**)

Let `d>=5`, fix `i`, and let `M` be any matching in `B_(d,i)`.  For every
choice of representatives in Section 2 and every nonempty `I subseteq M`,

```text
Gamma_U(I)=Gamma_V(I)=P_(d,|I|).                       (4.1)
```

Thus every generated-subgroup invariant formed from any number of source
words in one matching is passed exactly by their DPS targets.

**Proof.**  Write `s=|I|`.  If `s=1`, connected transposition support means
that the factors of each word generate `S_d`, so both groups in (4.1) are
`S_d=P_(d,1)`.

Assume `s>=2` and first consider the sources.  Distinct edges of a matching
have distinct left endpoints.  Hence their representatives lie in distinct
global `S_d`-conjugacy orbits.  M135's accepted graph-versus-parity
dichotomy applies to the literal pair of any such representatives: its
hypothesis and conclusion depend only on whether the two physical words are
globally conjugate, not on how representatives were selected inside their
`H`-orbits.  It therefore gives, for every distinct `a,b in I`,

```text
pi_(a,b)(Gamma_U(I))
  =<(u_j^a,u_j^b):1<=j<=m>
  =P_d={(x,y):sgn(x)=sgn(y)}.                          (4.2)
```

Every generator in (2.1) is a tuple of transpositions, so all of its
coordinates are odd.  Products consequently have one common coordinate
parity, and

```text
Gamma_U(I) <= P_(d,s).                                 (4.3)
```

Put `A=A_d` and

```text
N=Gamma_U(I) intersect A^s.                            (4.4)
```

For arbitrary `(x,y) in A x A`, equation (4.2) supplies an element of
`Gamma_U(I)` whose `a,b` coordinates are `x,y`.  Equation (4.3) forces all
of that element's coordinates to be even, so the element lies in `N`.
Therefore every two-coordinate projection of `N` is `A x A`.  Since `A_d`
is nonabelian simple for every `d>=5`, Lemma 3.1 yields

```text
N=A_d^s.                                               (4.5)
```

The group `Gamma_U(I)` contains any displayed all-odd factor tuple, while
(4.5) contains every all-even tuple.  Multiplying that fixed odd tuple by
all of `A_d^s` gives every all-odd tuple.  Combined with (4.3), this proves
`Gamma_U(I)=P_(d,s)`.

Distinct matching edges also have distinct right endpoints.  Every selected
target lies in the target global orbit labeling its edge, so arbitrary target
representatives obtained as `tau_i(u^q)` lie in distinct target global-
conjugacy orbits.  The identical literal-pair argument using M135's
dichotomy proves `Gamma_V(I)=P_(d,s)`.  QED.

### Corollary 4.2 (representative and coloring independence; **PROVED**)

The conclusion is independent of the chosen physical representative inside
each `H`-orbit, of the chosen perfect-matching decomposition of the regular
incidence multigraph, and of the chosen nonempty subfamily.

**Reason.**  The proof uses only the no-shared-left/no-shared-right property
of a matching and membership of every representative and target in its
declared global orbit.  Both properties hold for every such choice.  QED.

## 5. The ranks five and six

There is no hidden exception at either boundary rank.

- At `d=5`, `A_5` is the smallest nonabelian simple alternating group, so
  Lemma 3.1 applies literally.
- At `d=6`, M135/M137's pair theorem already excludes the exceptional outer
  automorphism of `S_6`: it sends transpositions to triple transpositions and
  cannot describe a literal paired word of transpositions.  After (4.2) is
  established, the present proof uses only simplicity of `A_6`.  Even an
  exceptional automorphism of `A_6` could create only a diagonal graph in a
  pair projection, while (4.2)--(4.5) require that projection to be full.

Thus the proof is uniform for all `d>=5`.

## 6. Exceptional-rank falsification

### Proposition 6.1 (pairwise-full is insufficient at rank three;
**PROVED by construction**)

For arity `s=3`, there is a proper subgroup `D<P_(3,3)` whose every pair
projection is `P_3`.

**Construction.**  Identify `A_3` with the cyclic group of order three and
put

```text
N={(x_1,x_2,x_3) in A_3^3:x_1 x_2 x_3=id}.
```

Because `A_3` is abelian, `N` is a subgroup of order `3^2` and every pair
projection is `A_3^2`.  Let `t` be any transposition and extend by the
simultaneous odd tuple `(t,t,t)`.  Simultaneous conjugation inverts every
`A_3` coordinate and preserves the product-one condition, so

```text
D=N semidirect <(t,t,t)>
```

is a subgroup of order `18`.  Every pair projection is `P_3`, also of order
`18`, while `|P_(3,3)|=2*3^3=54`.  Arity three is smallest because at arity
two the full pair projection is the whole group by definition.  QED.

The deterministic exact checker finds the same phenomenon inside the actual
accepted `d=3` incidence construction.  For each of the nine colors in the
three deterministic M137 matching decompositions, all six two-source groups
are `P_3` of order `18`; all four three-source groups and the full four-source
group have order only `18`, versus common-parity orders `54` and `162`.
Moreover, each full source subgroup differs literally from the corresponding
full target subgroup.  Some triple subgroups agree and others do not.  These
are **EXACT FINITE** facts, not inputs to Theorem 4.1.

At `d=4`, `A_4` is not simple and M135's pair premise already has an exact
failure: a nonconjugate source pair can generate the order-`96` subgroup
`(V_4 x V_4)Diag(S_4)` while its target pair generates `P_4` of order `288`.
M135's uniform conflict-coloring theorem handles rank four by singleton
classes, not by its matchings.  No rank-four multisource claim is made.

At `d=2`, the minimal sector is degenerate and the free-orbit incidence
setup used by M135 begins only at `d>=3`.  This has no bearing on the
`d>=5` theorem.

## 7. Consequence and exact remaining lemma

Theorem 4.1 closes one whole obstruction family: no equality test based on
the literal subgroup generated by aligned factor tuples of any arity can
separate a `d>=5` matching subfamily from its DPS targets.  Pair, triple,
higher-order, and full-matching generated-subgroup tests all return the same
canonical group `P_(d,s)`.

This is not a diagonal Hurwitz transitivity theorem.  Equality of generated
subgroups is necessary by Lemma 2.1 but is not sufficient for two tuples of
generating vectors to occupy the same diagonal braid orbit.  The accepted
remaining obligation is unchanged in form:

> Refine the M135 matchings into polynomially many subfamilies `S` such that
> `intersection_(Q in S) K_Q` is nonempty, and give a representative signed
> braid of polynomial length.

Theorem 4.1 says that generated-subgroup invariants cannot perform or obstruct
that refinement for `d>=5`.  It supplies no common action, no bound on braid
diameter, no compact edge-color evaluator, and no polynomial bound on the
number of edges in a matching.

## 8. Dependencies and scope boundary

Proved inputs are the accepted M135/M137 root-stabilizer incidence theorem,
the fact that matching endpoints are distinct, M135's graph-versus-parity
pair dichotomy for `d>=5`, connected transposition support generating `S_d`,
and the standard simplicity of `A_d` for `d>=5`.  Lemma 3.1 and all lifting
steps are proved here.  No unverified literature theorem is introduced.

The finite checker uses the frozen M137 checker only after verifying SHA-256
`bb62d449c7cad72a448389f9f7dd7ee76618e8c71b68189db20e19f4e2244341`.
It is a small-rank falsification/convention audit and is not evidence for the
universal theorem.

No UST basis exchange, all-edge comparison, physical minimal-sector gap,
arbitrary-product `Gamma_0`, original lazy exact `{3,4,5}` heat-bath gap,
Terminal A, or Terminal B claim follows.
