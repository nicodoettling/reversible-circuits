# Exact zero marked row for the voltage family

All claims in this note are **proved** unless explicitly labeled otherwise.
The convention is `(pq)(x)=p(q(x))`, words are written left-to-right, and
the right Hurwitz generator is

```text
R(a,b)=(b,bab).
```

The conclusion refutes the M75 simple-positive-braid row lemma. It is not a
conductance or gap upper bound for the heat-bath chain and is not Terminal B.

## Theorem

Let `W_L` be the accepted M78/M81 `Z_L^2` voltage lift of the ordered
`K_(4,4)` word, with `d_L=8L^2` vertices and `k_L=16L^2=2d_L` factors. For
every `L>=11`, every canonical positive-elimination collision in `W_L` is
unsafe. Equivalently,

```text
eta_L = Pr[some elimination prefix is a connected deletable square] = 0.
```

Consequently, add a disjoint doubled edge on two new vertices. The resulting
two-nontrivial-component minimal exterior state has

```text
N_L=8L^2+2,  m_L=16L^2+2=2N_L-2,
```

and its M75 uniform simple-positive-braid marked row is exactly zero. Thus no
absolute `C` can make the proposed lower bound `(Nm)^(-C)` hold for every
two-component exterior state.

## 1. The exact subset state

Let `w=(t_0,...,t_(k-1))` and let `S` be the set of original labels already
selected. Extract the labels of `S` in increasing order. A selected label is
never conjugated by an earlier selected label, because elimination only
conjugates residual factors strictly to its left. Thus the emitted factors
are exactly `(t_s:s in S)` in chronological order. For an unselected `j`,
put

```text
H_j(S)= product of t_s over s in S with s>j, in increasing order.
```

Successive use of the elimination rule gives

```text
r_j(S)=H_j(S)^(-1) t_j H_j(S).                    (1.1)
```

The residual is independent of the order used to select `S`. One elementary
proof swaps two consecutive selection requests: the two emitted factors
undergo one Hurwitz move while all unselected current factors are unchanged.
Adjacent swaps connect every two orders. Hence different orders give
Hurwitz-equivalent emitted prefixes and the same residual. In particular,
the emitted prefix has the same labeled support-component partition as the
original selected subgraph `G[S]`.

For unselected labels `i<j`, let

```text
B(S;i,j)= product of t_s over s in S, i<s<j,
          in increasing order.
```

The common suffix `H_j(S)` cancels from (1.1), so

```text
r_i(S)=r_j(S)
  iff t_i=B(S;i,j) t_j B(S;i,j)^(-1).              (1.2)
```

Thus duplicate availability is a static subset property.

## 2. Selections outside the collision interval do not affect safety

Partition `S=A union B union C` at `i<j`, where `A<i`, `i<B<j`, and `C>j`.
After emitting the equal pair, delete it. The connectedness of the remaining
word depends only on `B`.

This follows directly from the braid diagram. Factors in `A` never cross the
two pair strands. A factor in `C` crosses both. An adjacent equal pair is
transparent to such a crossing:

```text
(p,p,c) --R_2,R_1--> (c,cpc,cpc),
(c,p,p) --R_1,R_2--> (p,p,c).                     (2.1)
```

Deleting the equal pair before or after either displayed operation leaves
the same singleton `c`. Erasing the pair strands from the full braid
therefore leaves a Hurwitz braid on the surviving factors. Undo all `A` and
`C` extraction crossings in this way. The deletion word for `S` is
Hurwitz-equivalent to the deletion word obtained with only `B` selected.
Hurwitz moves preserve labeled support components, proving the claim.

This also handles an arbitrary order reaching `S`: by Section 1 it changes
only the emitted prefix by Hurwitz moves and leaves the residual fixed.

## 3. The chronological factorization surface

For an ordered transposition factorization `u=(e_1,...,e_r)`, form the support
multigraph with one labeled edge ribbon for each occurrence. At every symbol
vertex, cyclically order incident half-edges by increasing factor time. This
is an oriented ribbon graph. Its boundary permutation is `sigma alpha`, where
`alpha` reverses an edge and `sigma` advances to the next chronological dart
at the reached vertex.

Tracing a boundary component is the token trajectory through the factors.
Consequently the boundary components are in bijection with the cycles of
`eval(u)`. Cap every boundary component by a disk and call the resulting
closed oriented surface `Sigma(u)`. If the support is connected, this is a
cellular embedding and

```text
chi(Sigma(u)) = v-r+c(eval(u)).                    (3.1)
```

In particular a connected identity word on `v` symbols with `r=2v` lies
cellularly on a torus.

A right Hurwitz move is a ribbon-surface homeomorphism. For disjoint factors
it merely exchanges two globally adjacent timestamps and changes no local
rotation. Equal factors do nothing. If

```text
a=(x y), b=(y z),
```

then `(a,b)->(b,(x z))` slides the `y` end of the `a` ribbon across the `b`
ribbon to `z`. The two relevant darts are consecutive at `y`, so this is an
orientation-preserving ribbon edge slide. It preserves the capped surface.
Composition proves the assertion for every elimination braid.

## 4. Embedded collision curve and the exact connectivity criterion

Suppose an elimination endpoint contains consecutive factors `p,p`. Their
half-edges are consecutive at both endpoints of `p`. In the cellular dual,
the two dual edges have the same two distinct endpoints: the two token faces
swapped by the first `p` and swapped back by the second. They therefore form
an embedded two-edge simple closed curve `gamma`.

Equivalently, take the annular ribbon neighborhood of the two parallel edge
bands and the two intervening vertex sectors. Both the dual two-edge curve
and the smoothed primal two-edge core are cores of this annulus, hence are
isotopic. This gives a concrete embedded curve; no claim is made that an
arbitrary graph walk without this annular origin is embedded.

The following equivalence is exact:

```text
delete p,p and retain connected support
  iff gamma is nonseparating in Sigma(u).          (4.1)
```

To prove it, work in the cellular dual over `F_2`. If deleting the two
parallel primal edges disconnects, the endpoints of `p` lie in different
components and the pair is exactly a primal cut `delta(U)`. Its two dual
edges are the boundary of the union of dual 2-cells corresponding to `U`, so
`gamma` separates. Conversely, if `gamma` separates, it is the cellular
boundary of a nonempty proper union of dual 2-cells. Those dual 2-cells are
the primal vertices, and their boundary edges are exactly the two crossed
primal edges. Removing the pair therefore disconnects. This is the
primal-cut/dual-separating-cycle theorem specialized to the literal pair;
it excludes the empty-side ambiguity.

Under the inverse Hurwitz edge slides, `gamma` pulls back to an embedded
simple closed curve. With only the between-set `B` selected, retract this
pullback to the original graph skeleton. If `t_j=(c d)`, it is represented by

```text
c --B--> B(c) --t_i--> B(d) --B^(-1)--> d --t_j--> c.   (4.2)
```

This is the **collision contour**. Formula (1.2) makes it closed. A local
inverse-slide check proves (4.2): when a selected transposition meets one of
the two tracked endpoints, the annular core is slid across that edge; when it
is disjoint, nothing changes. Induction over the chronological factors of
`B` gives (4.2). The graph representative may revisit a vertex or edge, but
the curve whose homology it represents is embedded because it is the
homeomorphic pullback of `gamma`.

Sections 2 and 4 jointly include all selections outside `[i,j]`: erase them
after pair deletion using (2.1), then analyze the `B`-only embedded contour.

## 5. The base torus and its integral voltage basis

For completeness, the sixteen base edges and integer voltage coordinates are

```text
edge order:
(35)(34)(15)(25)(16)(04)(37)(27)
(05)(36)(14)(17)(06)(24)(26)(07)

x=(-1,-1,-1,0,0,0,0,1,0,0,0,0,0,0,0,0)
y=(-1, 0, 0,0,1,1,0,0,0,0,1,0,0,0,0,0).
```

The chronological base ribbon graph has `V=8`, `E=16`, and eight facial
4-cycles. Direct dart tracing gives zero signed integer voltage around every
face. Hence `x,y` are cellular integral 1-cocycles on the capped base surface
`Sigma_1`. Since `8-16+8=0`, `Sigma_1` is a torus.

The oriented cycles

```text
0-7-2-6-0  has voltage (-1,0),
0-7-1-6-0  has voltage ( 0,1).                    (5.1)
```

Thus evaluation by `(x,y)` maps `H_1(Sigma_1;Z)` onto `Z^2`. Both groups
have rank two, and the displayed determinant is `-1`; the map is an integral
isomorphism. This is stronger than merely showing that the mod-`L` graph
cover is connected.

Reducing these cocycles modulo `L` gives the graph cover underlying `W_L`.
Because every face voltage is zero, all base face disks lift, so the graph
cover extends to a connected unbranched `L^2`-sheeted surface cover

```text
p_L: Sigma_L -> Sigma_1.                           (5.2)
```

Its 1-skeleton and rotation system are exactly the chronological ribbon graph
of `W_L`: each base factor block is a full matching and contributes one dart
at every vertex in the inherited base order. It has

```text
V=8L^2, E=16L^2, F=8L^2,
```

so `Sigma_L` is also a torus. In the basis (5.1), the covering subgroup is
`L Z^2`. Therefore `p_(L*)` identifies `H_1(Sigma_L;Z)` injectively with
`L Z^2` inside `H_1(Sigma_1;Z)=Z^2`. In particular, if a closed curve in
`Sigma_L` projects with integer voltage `V`, then

```text
V in L Z^2, and V=0 implies the lifted curve is null-homologous.   (5.3)
```

The injectivity is elementary here: a connected cover of a torus corresponds
to a subgroup of `pi_1(T^2)=Z^2`, and abelianization changes nothing.

## 6. Uniform bound on collision-contour voltage

Consider (4.2) for `W_L`. Each of the sixteen base factor blocks is a perfect
matching. During one endpoint trajectory through the selected subsequence of
a block, the token can traverse at most one matching edge: after that
traversal no other edge in the same matching is incident to it. This remains
true for an arbitrary selected subset of that block. There are two endpoint
trajectories.

Only four blocks have nonzero `x` voltage, namely indices `0,1,2,7`, and only
four have nonzero `y` voltage, namely `0,4,5,10`. Every nonzero coordinate has
absolute value one. Finally, the closing edges `t_i,t_j` contribute at most
one each to either coordinate. Counting with multiplicity, including the
possibility that both endpoint paths traverse the same factor, gives

```text
|V_x| <= 2*4+2 = 10,
|V_y| <= 2*4+2 = 10.                              (6.1)
```

There are no hidden repeated block crossings: each endpoint sees each
chronological matching block once in (4.2), and within that block the factors
are pairwise disjoint. The two closing edges are deliberately counted again,
even if their blocks already occurred on a path.

## 7. Completion of the proof

Assume `L>=11` and that a reachable preliminary state has a safe duplicate
pair. By Sections 1 and 2, discard all selected factors outside the original
label interval and retain the same safety decision. Sections 3 and 4 give an
embedded collision curve `gamma_L` on the torus `Sigma_L`, and safety says
that it is nonseparating.

Its projected voltage lies in `L Z^2` by (5.3), but both coordinates have
absolute value at most ten by (6.1). Hence the voltage is `(0,0)`. The
injectivity in (5.3) gives `[gamma_L]=0` in integral homology. An embedded
simple closed curve on an oriented torus is null-homologous exactly when it
separates. This contradicts safety via (4.1). Therefore no safe duplicate
exists at any preliminary state, and `eta_L=0`.

For the two-component ambient state, append a disjoint doubled edge. Hurwitz
moves between the components are only commutations, so the induced relative
order and action on the genus-one factors is exactly the canonical uniform
elimination just analyzed. A marked genus-one endpoint square would give a
safe consecutive collision in that relative order. None exists, proving the
zero marked row and the theorem.

## 8. Falsification and finite checks

The theorem does not rely on computation, but the owned exact audits test its
most failure-prone interfaces.

- `topology_voltage_audit.py` reconstructs all eight base faces, their zero
  integer voltages, the determinant-one basis (5.1), the `V/E/F` counts, and
  the exact lifted torus maps for `L=1,2,3,11`. It also checks both identities
  in (2.1) for all 100 choices of `p,c` in `S_5`.
- `exact_subset_contour_audit.py` exhausts all `2^16` base selected subsets
  and all unselected pairs. Across 23040 duplicate subset-pairs, safety and
  nonzero collision-contour homology agree with zero failures; selections
  outside the pair interval change safety in zero cases. It independently
  recovers the exact base hit count `1280342186496/16!`.
- `subset_tail_audit.py` exhausts `W_2` at unselected-complement sizes
  `2,3,4` and finds zero safe pairs over `2016+41664+635376` subsets.
- Fixed-seed diagnostics find no homology/safety mismatch in 508, 97, and 27
  sampled collision states for `L=1,2,3`, respectively. These last counts are
  empirical only.

The bound `L>=11` is conservative. No assertion is made here for the exact
total hit probabilities at `2<=L<=10`.
