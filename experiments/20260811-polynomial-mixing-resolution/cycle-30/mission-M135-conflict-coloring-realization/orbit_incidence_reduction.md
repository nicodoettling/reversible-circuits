# Orbit-incidence coloring and the remaining braid-coset problem

Date: 2026-08-13 UTC.

## 1. Scope, target, and convention

For `d>=2`, put `m=2d-2` and

```text
Z_d={(t_1,...,t_m): t_1...t_m=id,
                         support connected on [d]}.
```

The target is uniform on this physical minimal identity sector. Permutations
compose as `(pq)(x)=p(q(x))`, and displayed factors multiply left-to-right.
The signed right-Hurwitz actions are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

For `1<=i<m`, `tau_i` is the accepted M127/M130 physical involution obtained
by swapping values `i,i+1` in any rooted DPS permutation coordinate. This
note proves the polynomial conflict-coloring half of M132's surviving
reduction. It does **not** prove simultaneous realization by fixed braids.

## 2. The distinguished-root equivariance group

Let `G=S_d` act on `Z_d` by simultaneous global conjugation:

```text
rho.w=(rho t_1 rho^(-1),...,rho t_m rho^(-1)).          (2.1)
```

Let

```text
H={rho in S_d:rho(d)=d} ~= S_(d-1).                    (2.2)
```

### Lemma 2.1 (root-stabilizer equivariance; **PROVED**)

For every `d>=2`, every adjacent index `i`, every `rho in H`, and every
`w in Z_d`,

```text
tau_i(rho.w)=rho.tau_i(w).                              (2.3)
```

**Proof.** Use the accepted plus-mirror rooted DPS construction. Its Cayley
tree is rooted at `d`. For a rooted coordinate `(T,pi)` and `rho in H`,
replace `T` by `rho T`; for every `k<d`, move the ordered pair
`(pi(2k-1),pi(2k))` to the two slots indexed by `rho(k)`. The parent relation,
the black/white hairy incidences, the directed boundary walk, and every
distance-one or distance-three closure are carried to their `rho`-images.
The conventional start at the gap `(y_1,1)` only linearizes one cyclic
boundary: after relabeling, using `(y_1,1)` rather than the image gap gives a
cyclic rotation of that same boundary, and the intrinsic noncrossing closure
is unchanged. Consequently the closed word is exactly `rho.F(T,pi)`.

Swapping the *values* `i,i+1` of `pi` commutes with this permutation of the
ordered black-vertex slots. Closing after the swap therefore gives (2.3).
Root independence of `tau_i`, proved in M127/M130, removes the choice of DPS
preimage. QED.

The restriction to `H` is material: `tau_i` need not commute with conjugation
by a permutation moving `d`. The exact `d=3,4` audit has zero failures in
(2.3), while source global-conjugacy orbits split into as many as `d` target
global-conjugacy orbits.

### Lemma 2.2 (free conjugation actions; **PROVED**)

For `d>=3`, `G` and `H` act freely on `Z_d`. Hence every `G`-orbit has size
`d!`, every `H`-orbit has size `(d-1)!`, and every `G`-orbit is the disjoint
union of exactly `d` `H`-orbits.

**Proof.** The transpositions appearing in a connected support graph generate
`S_d`. If `rho.w=w`, then `rho` centralizes every factor and hence all of
`S_d`. The center of `S_d` is trivial for `d>=3`. QED.

## 3. Pair subgroups away from the rank-four exception

For `u,v in Z_d`, define the literal paired subgroup

```text
D(u,v)=< (u_1,v_1),...,(u_m,v_m) > <= S_d x S_d.        (3.1)
```

Put

```text
P_d={(p,q):sgn(p)=sgn(q)}.                             (3.2)
```

### Lemma 3.1 (Goursat dichotomy; **PROVED**)

If `d=3` or `d>=5`, exactly one of the following holds:

1. `v=rho.u` for a unique `rho in S_d`, and
   `D(u,v)={(p,rho p rho^(-1)):p in S_d}`;
2. `u,v` are not globally conjugate, and `D(u,v)=P_d`.

**Proof.** Connected support implies that each coordinate projection of
`D(u,v)` is all of `S_d`, so `D(u,v)` is a subdirect product. Every displayed
generator is odd in both coordinates, hence `D(u,v)<=P_d`.

Goursat's elementary kernel argument associates normal subgroups `N_1,N_2`
of the two `S_d` factors and an isomorphism `S_d/N_1 ~= S_d/N_2`. For
`d=3` the only proper nontrivial normal subgroup is `A_3`; for `d>=5` it is
`A_d`. Goursat's full-product case has kernels `S_d`, but that would give
`S_d x S_d`, which is impossible because the literal generators already
proved `D(u,v)<=P_d`. If the kernels are `A_d`, the quotient is `C_2` and
the subdirect product is exactly `P_d`.
If the kernels are trivial, the subgroup is the graph of an automorphism
`alpha` of `S_d` and `v_j=alpha(u_j)` for every `j`.

The graph case is inner. Indeed `alpha` sends at least one transposition to a
transposition and therefore sends the whole transposition conjugacy class to
itself. Here is a self-contained class argument. Identify transpositions with
the edges of `K_d`; two are incident exactly when they do not commute. For
`d>=5`, the unique maximum pairwise-incident families are the `d` stars of
size `d-1` (a non-star pairwise-incident family is a triangle, of size three).
Thus `alpha` permutes the stars, inducing some `rho in S_d`, and the unique
intersection of stars `a,b` gives
`alpha((a,b))=(rho(a),rho(b))`. Hence `alpha=Ad_rho`. At `d=3` every
automorphism is inner directly. In particular, an outer automorphism of
`S_6` cannot preserve transpositions. Since automorphisms preserve element
order and conjugacy-class size, and the two size-15 involution classes in
`S_6` are transpositions and triple transpositions, the exceptional outer
automorphism sends the former class to the latter. It therefore cannot occur
in this graph case. Conversely, if
`v=rho.u`, connected support makes the generated paired subgroup the full
graph of `Ad_rho`. Uniqueness follows from the trivial center. QED.

Rank four is excluded for a precise reason: `S_4` has the additional normal
subgroup `V_4`. The M132 witness, independently reconstructed here, has
neither its sources nor its targets globally conjugate but changes paired
subgroup order `96 -> 288`. Thus Lemma 3.1 is false at `d=4`; this is not a
notation artifact.

## 4. The orbit-incidence multigraph

Fix `d,i`. Let `X=Z_d/H` be the set of `H`-orbits. Form a bipartite
multigraph `B_(d,i)` as follows:

- a left vertex is a global `G`-orbit in `Z_d`;
- a right vertex is a second copy of a global `G`-orbit;
- for every `Q in X`, add one edge `e_Q` from the `G`-orbit containing `Q`
  to the `G`-orbit containing `tau_i(Q)`.

The target endpoint is well-defined by Lemma 2.1.

### Lemma 4.1 (regular incidence; **PROVED**)

For `d>=3`, `B_(d,i)` is a `d`-regular bipartite multigraph, counting
parallel edges with multiplicity.

**Proof.** Lemma 2.2 gives exactly `d` `H`-orbits in every source `G`-orbit,
so every left degree is `d`. Lemma 2.1 and bijectivity of `tau_i` show that
`tau_i` permutes the `H`-orbits. Every target `G`-orbit again contains exactly
`d` of them, each with a unique preimage, so every right degree is `d`. QED.

Every finite `d`-regular bipartite multigraph is the disjoint union of `d`
perfect matchings: Hall's condition gives one perfect matching because
`d|S|` incident edges from a left set `S` enter at most `d|N(S)|` slots;
delete that matching and induct on `d`. Thus fix any proper edge-coloring

```text
kappa:X -> {1,...,d}.                                  (4.1)
```

For a color `c`, define the physical class

```text
C_c=union {Q: kappa(Q)=c}.                              (4.2)
```

### Theorem 4.2 (polynomial conflict coloring; **PROVED**)

If `d=3` or `d>=5`, every `C_c` is independent in M132's schedule-conflict
graph `C_(d,i)`. Consequently

```text
chi(C_(d,i)) <= d.                                     (4.3)
```

**Proof.** Take `u,v in C_c`.

- If they lie in the same `H`-orbit, `v=rho.u` for some `rho in H`.
  Lemma 2.1 gives `tau_i(v)=rho.tau_i(u)`, so Lemma 3.1 identifies the same
  literal graph subgroup before and after the edit.
- If they lie in different `H`-orbits, the proper edge coloring says their
  edges share neither a left nor a right endpoint. Hence `u,v` are not
  globally conjugate and `tau_i(u),tau_i(v)` are not globally conjugate.
  Lemma 3.1 makes both paired subgroups equal to `P_d`.

In either case the paired subgroup is unchanged, so the pair is not a
conflict edge. QED.

### Corollary 4.3 (uniform all-rank polynomial bound; **PROVED**)

For every `d>=2` and every adjacent index,

```text
chi(C_(d,i)) <= d^6.                                   (4.4)
```

**Proof.** At `d=2`, `Z_2` is a singleton. At `d=3` use Theorem 4.2. At
`d>=5` use Theorem 4.2. At `d=4`, the DPS count

```text
|Z_4|=4^(4-3)(2*4-2)! = 4*6! = 2880 < 4^6
```

allows singleton color classes. QED.

This proves the conflict-coloring half of the M132/M134 frontier. It is an
existence theorem: an edge coloring can be fixed once for each `(d,i)`. No
claim of a compact algorithm for evaluating `kappa(w)` is needed or made.

## 5. Why coloring does not imply one fixed braid

Let `A_d` denote the finite image of the signed braid action on `Z_d`. Every
`a in A_d` commutes with the full global-conjugation action of `G`, because
each Hurwitz generator does. Together with Lemma 2.1 this gives:

### Lemma 5.1 (atomic agreement orbits; **PROVED**)

For a fixed action `a`, its agreement set

```text
Agree_i(a)={w:a(w)=tau_i(w)}                            (5.1)
```

is a union of `H`-orbits.

For an `H`-orbit `Q`, choose `w_Q in Q` and define

```text
K_Q={a in A_d:a(w_Q)=tau_i(w_Q)}.                       (5.2)
```

This set is independent of the chosen representative up to the same equality,
and is either empty or a coset of a point stabilizer. A family `S` of
`H`-orbits is simultaneously realized by one fixed braid action if and only
if

```text
intersection_(Q in S) K_Q != empty.                    (5.3)
```

**Proof.** If `a(w)=tau_i(w)` and `rho in H`, then
`a(rho.w)=rho.a(w)=rho.tau_i(w)=tau_i(rho.w)`. This proves the union claim
and representative independence. Equation (5.3) is the literal conjunction
of the endpoint constraints. The point-stabilizer coset description is the
standard fiber of a transitive group action; nonemptiness for each individual
`Q` additionally uses qualitative Hurwitz connectivity of the sector. QED.

The nonemptiness qualification matters because the project's general
connected-support Hurwitz transitivity input remains a separately audited
dependency. The coloring theorem itself does not use it.

### Proposition 5.2 (automatic matching realization; **REFUTED at `d=3`**)

It is false that every matching color from Section 4 is contained in one
agreement set.

**Exact certificate.** At `d=3`, `B_(3,i)` has four vertices on each side,
is 3-regular, and has 12 edges. Every proper three-edge-coloring therefore
has four `H`-orbits per color. Since `|H|=2`, every physical color class has
eight states. Independent complete closure of the signed-Hurwitz action image
gives order `216` and

```text
max_a |Agree_i(a)|=6,       exact schedule-cover number=5              (5.4)
```

for each `i=1,2,3`. Thus none of the three eight-state matching colors is
one-schedule realizable, despite having zero paired conflicts. This finite
counterexample refutes only automatic realization, not a polynomial
refinement after excluding small ranks.

## 6. Exact remaining lemma

The surviving asymptotic obligation is now:

> **POLYNOMIAL MATCHING-COSET REFINEMENT.** For `d>=5`, choose a `d`-edge-
> coloring of `B_(d,i)`. Refine its matchings into at most `d^C` total
> subfamilies `S`. For every `S`, prove that `intersection_(Q in S) K_Q`
> contains an action represented by a signed braid word of length at most
> `d^C`, for one universal constant `C`.

This is **UNRESOLVED**. It is strictly the simultaneous-realization step:
Corollary 4.3 has discharged polynomial conflict coloring. It is also sharper
than another contour descriptor search: the only remaining data are coset
intersections on matchings of the intrinsic orbit-incidence multigraph.

No claim is made that generated-subgroup equality is sufficient for Hurwitz
equivalence in a direct product. The `d=3` calculation explicitly warns that
it is not sufficient for simultaneous realization.

## 7. Conditional schedule recovery and root cost

Suppose the remaining lemma supplies `q(d)` classes and fixed schedules of
scheduled length at most `L(d)`. Given `(i,class,scheduled time,direction)`
and a directed physical action, inverting the known schedule prefix recovers
at most one physical source. If scheduled holds are deleted, one compressed
time has at most `L(d)` scheduled-time preimages.

Including all `2d-3` adjacent indices and the exact `d` white roots, the
corresponding descriptor multiplicities are bounded by

```text
2 d (2d-3) q(d) L(d)       with scheduled time,
2 d (2d-3) q(d) L(d)^2     with only compressed time.   (7.1)
```

Thus polynomial refinement and polynomial word length would retain the
accepted polynomial source-recovery accounting for the adjacent-permutation
coordinate. This does not supply UST basis-exchange routes or total
stationary congestion.

## 8. Dependencies and scope boundary

Proved inputs used here are the accepted M112/M119 rooted DPS bijection and
exact root quotient, M127/M130 descent of `tau_i`, elementary connected-graph
generation of `S_d`, the normal-subgroup classification of `S_3` and `S_d`
for `d>=5`, Goursat's kernel argument, and Hall's theorem. The new
root-stabilizer equivariance and orbit-incidence coloring are proved above.

The exact `d=3,4` script is a convention/falsification audit, not the proof of
Theorem 4.2. No UST basis exchange, all-edge rooted-product comparison,
physical `P_(0,d)` gap, arbitrary-product `Gamma_0`, original lazy exact
`{3,4,5}` heat-bath gap, Terminal A, or Terminal B claim follows.
