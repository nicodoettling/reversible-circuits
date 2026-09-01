# M85 fresh referee report on M84

Date: 2026-08-12.  Repository commit recorded by the independent exact
artifact: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Referee decision

```text
ACCEPT M84.
Material objections: none.
```

The accepted statement is exactly the following scoped result.

> For M78/M81's voltage word `W_L`, every reachable preliminary state of
> canonical positive elimination has zero safe duplicate pairs when `L>=11`.
> Hence its safe-prefix probability is `eta_L=0`.  After adjoining one
> disjoint doubled edge, the resulting two-nontrivial-component minimal
> exterior state has a zero row for M75's literal simple-positive-braid
> marked set.

This refutes M75's proposed universal inverse-polynomial row lower bound for
that one canonical braid law.  It does **not** prove a stationary bottleneck,
a heat-bath conductance upper bound, a superpolynomially small heat-bath gap,
or Terminal B.

## 2. Frozen provenance

The three assigned M84 digests match:

| frozen artifact | required SHA-256 | observed |
|---|---|---|
| `report.md` | `c55f51c6ff05d7af7e79b3679a707fcf252112dfe6c3e7de4ef6213a501f8b12` | match |
| `zero_row_theorem.md` | `78130a18f581c9d6a2fdcb6ed2c854287fba43dd9128d5dc2405b9771598364e` | match |
| `SHA256SUMS` | `7107346acc1a140177f51052e2eb2d25af6204d4622ca1aab074d16e43275372` | match |

Running `sha256sum -c SHA256SUMS` in M84's frozen directory returned `OK`
for all eighteen entries.  No frozen or shared file was edited.

The audit uses the convention `(pq)(x)=p(q(x))`, evaluates tuple factors
left-to-right, and uses the right Hurwitz move

```text
R(a,b)=(b,bab).
```

The background target remains uniform on `Omega(N,m)` for the literal lazy
exact same-product `{3,4,5}` heat-bath kernel.  The audited probability law is
instead M75's explicitly separate canonical positive-permutation-braid law.

## 3. Audit of the nine required proof interfaces

### 3.1 Subset state and order invariance — accepted

For a selected original-label set `S`, let

```text
H_j(S)=product_(s in S, s>j) t_s
```

in increasing chronological order.  Increasing extraction emits the literal
original factors `(t_s:s in S)` and gives

```text
r_j(S)=H_j(S)^(-1)t_jH_j(S).                       (3.1)
```

There is also a direct order-free induction.  Suppose the invariant (3.1)
holds for `S` and select `s` next.  For `j>s`, nothing changes.  For `j<s`,
write

```text
H_j(S)=A C,  H_s(S)=C,
```

where `A` contains selected labels strictly between `j` and `s`.  The current
pivot is `p=C^(-1)t_sC`, and conjugating the current `j` factor gives

```text
p [C^(-1)A^(-1)t_jAC] p
 = C^(-1)t_sA^(-1)t_jAt_sC
 = H_j(S union {s})^(-1)t_jH_j(S union {s}).
```

Thus the residual is a function of the set, not its selection order.
Swapping two neighboring selection requests applies one Hurwitz move to the
two corresponding outputs and leaves the just-proved residual invariant;
adjacent swaps connect all orders.  Hence every output prefix has the same
labeled support-component partition as the increasing-order prefix, namely
the original selected-edge subgraph.

For unselected `i<j`, write `H_i=B H_j`, where `B` is the increasing product
of selected factors strictly between them.  Cancelling `H_j` in (3.1) gives

```text
r_i(S)=r_j(S) iff t_i=B t_j B^(-1).                (3.2)
```

This validates M84's static subset reduction.

### 3.2 Outside-interval erasure — accepted

Selections before `i` cross neither candidate strand.  A selected factor
after `j` crosses both.  The latter crossings are transparent after the equal
pair is deleted because, literally,

```text
(p,p,c) --R_2,R_1--> (c,cpc,cpc),
(c,p,p) --R_1,R_2--> (p,p,c).                      (3.3)
```

Deleting the displayed equal pair leaves `c` on both sides.  Erasing all
outside candidate strands from the braid therefore leaves a Hurwitz braid on
the surviving factors.  Hurwitz moves preserve labeled support components,
so deletion connectivity depends only on the selected between-set `B`.

This argument is not merely a conjugacy heuristic: it handles every outside
strand locally and is compatible with arbitrary orders by Section 3.1.  The
independent exhaustive audits found zero outside-selection failures over all
`23040` duplicate subset-pairs of `W_1` and all `18720` duplicate subset-pairs
in the connected genus-one `S_3` test class.

### 3.3 Chronological ribbon surface and Hurwitz slide — accepted

At every symbol vertex, order incident factor darts by chronological factor
index.  If `alpha` reverses an edge and `sigma` advances to the next dart at
the reached vertex, a boundary step is `sigma alpha`.  This is exactly one
step of cyclic token tracing: cross the current transposition edge and advance
to the next time that the token's new vertex participates.  Consequently the
boundary components are the cycles of `eval(w)`.  For connected support,
capping those boundary circles yields a cellular closed oriented surface with

```text
chi(Sigma(w))=v-k+c(eval(w)).                       (3.4)
```

The local Hurwitz identification is also correct.  Disjoint adjacent factors
only exchange global timestamps and do not change any local cyclic order;
equal factors are fixed.  In the remaining case, after relabeling,

```text
((xy),(yz)) -> ((yz),(xz)).                        (3.5)
```

The `yz` band is fixed while the `y` endpoint of the `xy` band slides along
it to `z`.  The relevant darts are consecutive because the factor times are
globally adjacent.  This is an orientation-preserving homeomorphism of the
thickened ribbon graph, fixed off the local rectangle.  It maps boundary
circles to boundary circles and therefore extends across their cap disks.
Composing these local homeomorphisms transports the collision annulus through
the full elimination braid.

This point matters: a Hurwitz move is not being treated only as an abstract
genus-preserving operation.  The local edge-slide homeomorphism tracks the
specific pair annulus used later.

### 3.4 Embedded equal-pair curve and deletion criterion — accepted

At an endpoint containing consecutive factors `p,p`, their darts are
consecutive at both endpoints.  Because the whole word evaluates to identity,
the factorization faces are individual token trajectories.  The first `p`
swaps two distinct tokens and the second swaps them back; hence the two dual
edges join the same two **distinct** token faces.

The two pair bands together with the two chronological vertex sectors have
an annular regular neighborhood.  Joining the two dual crossings through the
corresponding face sectors gives an embedded two-edge circle `gamma`, a core
of that annulus.  Pullback by the homeomorphisms in Section 3.3 therefore
remains an embedded simple closed curve.  This is why the proof does not make
the false inference that an arbitrary self-intersecting null-homologous graph
walk separates.

The exact primal/dual criterion is

```text
delete p,p and retain connected support
  iff gamma is nonseparating.                      (3.6)
```

If pair deletion disconnects, the two parallel edges are the cut
`delta(U)` between the components containing the two endpoints.  Their dual
cycle is the boundary of the union of dual 2-cells associated with primal
vertices in `U`, so `gamma` separates.  Conversely, either side of a
separating dual circle is a nonempty proper union of those dual cells; its
cellular boundary consists exactly of the two crossed primal edges.  They
are therefore a cut.  The two sides cannot be empty because each open
complementary region contains a dual 2-cell.

On an oriented torus, an embedded circle is nonseparating exactly when its
integral homology class is nonzero.  This is the precise topological input
used by M84.

### 3.5 Inverse-slide collision contour — accepted

Let `t_j=(c d)`.  Under increasing extraction of the selected between-set,
the selected band is fixed in every local move while the still-residual left
candidate band is slid.  Tracking its two endpoints gives the two trajectories
of `B`.  Pulling the pair annulus back consequently has the skeleton homology
representative

```text
c --B--> B(c) --t_i--> B(d)
  --B^(-1)--> d --t_j--> c.                        (3.7)
```

Formula (3.2) closes this walk.  An unselected interval factor behaves in the
opposite local role when the right pair strand is bubbled left: the pair band
is fixed and that unselected band is slid to the exterior of the annulus.
It therefore contributes no segment to (3.7).  This selected/unselected
distinction is the delicate point in the argument, and the local move (3.5)
resolves it.  If a tracked current edge happens to equal a selected pivot,
the two endpoint traversals add only a cancelling backtrack to the skeleton
representative; the annular core itself is still transported homeomorphically.

The walk (3.7) may revisit graph vertices or edges.  That is harmless: it is
used only to compute the homology of the separately established embedded
pullback curve.

The independent cellular computation verified that (3.7) is a cycle and
that its homology is nonzero exactly for safe deletion in every tested
duplicate state: zero failures on the `23040` `W_1` states and zero failures
on the `18720` generic `S_3` states.

### 3.6 Integral voltage basis and torus cover — accepted

The base chronological surface has

```text
V=8, E=16, F=8, chi=0,
```

and is connected, hence is a torus.  All eight facial boundaries have
integer voltage `(0,0)`, so the displayed `x,y` edge labels define classes in
`H^1(Sigma_1;Z)`.  Their evaluations on

```text
0-7-2-6-0 = (-1,0),
0-7-1-6-0 = ( 0,1)                                (3.8)
```

are unimodular.  Therefore the cohomology map
`H_1(Sigma_1;Z)->Z^2` is an isomorphism.

Reducing modulo `L` gives the connected graph cover `W_L`.  Zero voltage on
every face lets all cap disks lift, so this is a connected unbranched surface
cover.  The chronological rotation does lift: each base factor becomes one
full matching block and supplies exactly one incident dart at each lifted
vertex over either base endpoint, in inherited base-factor order.  Thus its
1-skeleton is exactly the chronological ribbon graph of `W_L` and

```text
V_L=8L^2, E_L=16L^2, F_L=8L^2.
```

In the unimodular coordinates (3.8), the covering subgroup is `L Z^2`.
Since `pi_1(T^2)=H_1(T^2;Z)=Z^2`, the induced homology map is injective with
image `L Z^2`.  A closed curve upstairs consequently has projected integer
voltage in `L Z^2`, and zero projected voltage forces zero homology upstairs.

### 3.7 Uniform voltage bound and zero row — accepted

Each of the sixteen chronological base blocks is a perfect matching.  During
one endpoint trajectory through the selected subset of a block, a token can
traverse at most one edge: after that traversal the matching has no second
edge incident to its new vertex.  Each endpoint sees every chronological
block only once.

There are two endpoint trajectories.  Exactly four blocks have nonzero
`x` voltage and four have nonzero `y` voltage, with coordinate magnitude one.
The two closing factors contribute at most one each.  Hence, without relying
on cancellation,

```text
|V_x| <= 2*4+2 = 10,
|V_y| <= 2*4+2 = 10.                              (3.9)
```

For `L>=11`, closedness gives `V in L Z^2`, while (3.9) forces `V=0`.
Section 3.6 makes the embedded collision curve null-homologous upstairs; on
the torus it separates.  Section 3.4 then says its pair deletion is unsafe.
This applies to every selected subset and every available duplicate pair, so
every reachable preliminary state has safe-pair count `a=0`.  The exact next
two hazard `2a/[s(s-1)]` and total hit probability `eta_L` are both zero.

### 3.8 Doubled-edge ambient state and M75's marked set — accepted

Appending a doubled edge on two new vertices gives components

```text
(v,k,g)=(8L^2,16L^2,1), (2,2,0)
```

and therefore

```text
N_L=8L^2+2,
m_L=16L^2+2=2N_L-2.                               (3.10)
```

Both support components are nontrivial, exactly as M75's minimal exterior
scope requires.  Cross-component Hurwitz moves are commutations, so a uniform
ambient requested order induces the same uniform relative order and the same
canonical action on the `W_L` labels.  M75's literal `G_Gamma` marks only a
globally adjacent square in the genus-one component whose deletion leaves
that component connected.  Any such endpoint square is a consecutive
collision in the relative `W_L` output order and, by the accepted
safe-prefix/marked-endpoint equivalence, would give a safe duplicate at its
emission prefix.  Section 3.7 rules this out.  A square in the doubled-edge
component is not a `G_Gamma` mark.

Thus the row is exactly zero on the explicit infinite sequence (3.10), and
no absolute `C` can give M75's proposed `(Nm)^(-C)` lower bound for every
source.

### 3.9 Scope and terminal status — accepted

The proof concerns one state-independent family of bijective Hurwitz words.
It supplies no stationary-mass cut, no heat-bath boundary flow estimate, and
no upper bound on the spectral gap of the literal exact `{3,4,5}` chain.
Another randomized braid law or a direct partial-macro flow could bypass this
zero row.  M84 labels all of these distinctions correctly.  Terminal A and
Terminal B both remain unresolved.

## 4. Independent exact reproduction

`independent_audit.py` imports no M84 or predecessor code.  Its deterministic
standard-library run produced `independent-results.json` with these decisive
results.

| audit | exact result |
|---|---:|
| frozen base selected subsets | `65536` |
| stable-formula failures | `0` |
| decreasing-order residual failures | `0` |
| selected-prefix component failures | `0` |
| base duplicate subset-pairs | `23040` |
| outside-selection failures | `0` |
| contour-cycle failures | `0` |
| safety/homology failures | `0` |
| base safe duplicate pairs | `14592` |
| maximum base contour-voltage coordinate | `1` |
| connected genus-one `S_3` words | `240` |
| generic duplicate subset-pairs | `18720` |
| generic outside/contour/homology failures | `0/0/0` |
| null-pair identities in `S_5` | `100`, zero failures |
| `W_2` surface | `V/E/F=32/64/32`, connected identity torus |
| `W_11` surface | `V/E/F=968/1936/968`, connected identity torus |

The base face voltages were all zero and the two basis-cycle voltages were
`(-1,0)` and `(0,1)`.  The exact base voltage and path-length histograms also
match M84.  At `L=11`, adjoining the doubled edge independently gives
`N=970,m=1938=2N-2` and component genera `(1,0)`.

Reproduction command from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M85-m84-fresh-referee/independent_audit.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M85-m84-fresh-referee/independent-results.json
```

Python was `3.12.3`; seed `null`; nonstandard dependencies `{}`.  These finite
facts are falsification checks, not the proof of the all-`L` quantifier.

## 5. Corrections and objections

### Material objections

None.

### Nonmaterial correction

1. In M84 `report.md`, Section 2.4 calls `(x,y)` an integral `H1` basis.
   Strictly, the voltage cochains form an integral `H^1` basis; the two
   displayed cycles give the corresponding unimodular `H_1` coordinates.
   `zero_row_theorem.md` already uses the correct cohomological language, and
   the proof and conclusion are unaffected.

### Provenance note

`AGENTS.md` names `references/experiments.md`, which is absent in this
checkout.  The available required experiment reference at
`.codex/skills/reversible-circuit-sampler/references/experiments.md` was read
in full.  This repository-path discrepancy is unrelated to M84's theorem.

## 6. Claim ledger and final verdict

| claim | referee status | independent basis | action |
|---|---|---|---|
| subset residual and order invariance | proved | algebra plus exhaustive base audit | accept |
| outside-selection erasure | proved | local identities plus two exhaustive classes | accept |
| chronological torus and Hurwitz homeomorphism | proved | dart tracing and local edge slide | accept |
| embedded pair curve; deletion iff nonseparating | proved | annulus plus cellular primal/dual cut theorem | accept |
| pulled-back contour formula | proved | local selected/unselected slide induction | accept |
| integral voltage surface cover | proved | zero face sums and unimodular cycles | accept |
| uniform coordinate bound `10` | proved | perfect-matching block count | accept |
| `eta_L=0` for all `L>=11` | proved | preceding exact implications | accept |
| doubled-edge M75 marked row is zero | proved | exact macro scope and relative-order reduction | accept |
| M75 canonical row lower bound | refuted | explicit infinite zero-row sequence | retain negative result |
| heat-bath Terminal B | unresolved | no stationary bottleneck follows | do not promote |

Final decision:

```text
ACCEPT M84 WITH ZERO MATERIAL OBJECTIONS.
PROVED: eta_L=0 FOR EVERY L>=11 FOR THE CANONICAL LAW.
REFUTED: M75'S SIMPLE-POSITIVE-BRAID WORST-ROW LOWER BOUND.
NO TERMINAL HEAT-BATH CLAIM.
```
