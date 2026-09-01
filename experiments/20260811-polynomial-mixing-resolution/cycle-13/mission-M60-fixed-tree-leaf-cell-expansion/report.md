# M60 final report: leaf-cell refutation and arbitrary minimal-macro cuts

## 1. Exact claims, quantifiers, and convention

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and words evaluate as
`t_1...t_m`.  The literal chain is

```text
K=(1/2)I+(1/(2|R_m|)) sum_(r in R_m)
       (1/(m-r+1)) sum_i H_(i,r),
R_m={r in {3,4,5}:r<=m},
```

with `H_(i,r)` exactly uniform on the ordered length-`r` transposition words
having the same ordered product.  The target `pi` is uniform on the global
`Omega(N,m)`.

For `N>=3`, put `m=2N-2`, `M=binom(N,2)`, and let `F_N` be the connected
full-support minimal identity macro.  For a labeled tree `T`, let
`F_N(T)={w in F_N:T_J(w)=T}`.  If `v` is a leaf of `T`, define the exact
strand-deletion cell

```text
C_(T,v,z)={w in F_N(T):Del_v(w)=z},
Lambda_N=binom(m,2)(N-1)^2.                         (1.1)
```

This mission proves the following sharply separated statements.

**Claim A (the named leaf-cell chain is reducible; proved infinite family).**
Let `P_T^leaf` choose uniformly among the original leaves of `T` and exactly
heat-bath resample inside the current cell `C_(T,v,z)`.  For every path tree
on `N>=5` vertices, `P_T^leaf` is reducible.  It preserves the ordered word
obtained after deleting all original leaves.  At `N=5`, the path restriction
has exactly eight components, one for each word in the fixed-tree
three-vertex core fiber.

**Claim B (universal strand-cell canonicalization; proved).** For every
`N>=3`, every `T`, every leaf `v` with incident edge `f`, every base `z`, and
every `w in C_(T,v,z)`, there is an explicit path of at most `2m-3` literal
H3 transitions from `w` to the cell hub `z f f`.  Every intermediate word is
in `F_N` and has `Del_v=z`, although its join tree may differ from `T`.
Every specified path transition has probability at least

```text
p_* = 1/[2|R_m|(m-2)M^3].                           (1.2)
```

**Claim C (every cut contained in the entire minimal macro leaks
polynomially; proved).** For every `N>=3` and every nonempty `A subseteq F_N`,

```text
Q_K(A,A^c)/pi(A)
 >= p_*/[N(N-1)Lambda_N]
 =1/[2|R_m|N(N-1)binom(m,2)(N-1)^2(m-2)M^3]
 >=1/(24N^13).                                      (1.3)
```

Consequently

```text
Phi_pm^K(A)=Q_K(A,A^c)/min{pi(A),pi(A^c)}>=1/(24N^13)
```

without any assumption on which side has mass at most one half.  Claim C
includes arbitrary internal cuts spread across all labeled join trees, not
only tree-saturated or fixed-tree cuts.

Claims A--C are scoped results.  Claim C does not cover a cut that contains
some states of `F_N^c`, because such a cut can absorb the macro-exit targets.
It therefore does not prove Terminal A or Terminal B.

## 2. Full argument and construction

### 2.1 Multi-strand core invariant and infinite reducibility

For a permutation, erasing labels from its disjoint cycles is order
independent.  If `L` is a set of labels, write `d_L(sigma)` for the resulting
permutation.  Then

```text
d_L=d_(L minus {v}) composed with d_v.               (2.1)
```

Apply (2.1) to every prefix permutation of a word and remove the identity
increments.  Sequential strand deletion therefore commutes: deleting `v`
and then the labels in `L minus {v}` gives the same ordered nonidentity word
as deleting all of `L` directly.

Let `L(T)` be the original leaf set and define

```text
Core_T(w)=Del_(L(T))(w).                             (2.2)
```

If two words lie in one `v`-cell, their `Del_v` words agree, so (2.1) implies
that their cores (2.2) agree.  Every edge of `P_T^leaf` preserves the core.

For a path `T_N` with `N>=5`, deleting the two endpoints leaves a path on
`N-2>=3` vertices.  Its fixed-tree minimal fiber has at least two words: take
the adjacent doubled-edge word and change the order of two doubled edge
pairs.  Conversely, any such core word `z` lifts to `T_N` by embedding `z`
and appending the two deleted leaf-edge squares.  Hence at least two core
values occur and `P_(T_N)^leaf` is reducible.  This is an explicit infinite
counterexample to the M59 named leaf-cell expansion proposition, but not to
global `K`.

At `N=5`, exact calculation makes the invariant sharp.  For

```text
T={(0,1),(0,3),(1,2),(2,4)},  L(T)={3,4},
```

the eight components have sizes

```text
1068,1068,997,997,997,997,842,842,
```

and are exactly the fibers of the eight possible four-factor core words.
Every component has zero `P_T^leaf` escape, but its exact full-K escape lies
between

```text
2195811215790837089/5105186281653120000
=0.4301138283008563...
```

and

```text
7122880167270846929/16099501307685120000
=0.4424286213058493....
```

The exact rejected-exit fixed-tree escapes lie between `0.0139904...` and
`0.0427978...`.  Thus the auxiliary invariant is heavily bypassed by the
literal chain.

### 2.2 Insertion-coordinate table

Fix a leaf `v` and put `X=[N] minus {v}`.  Erase `v` from every prefix
permutation.  A lift of the erased prefix is described by an insertion
coordinate `a in X union {bottom}`: `bottom` means that `v` is fixed, while
otherwise `v` follows `a` in its permutation cycle.

The accepted strand-deletion table has the following consequence.  A minimal
leaf lift has exactly two null projected increments.  The first opens the
coordinate with a factor `h_a=(v,a)`; because `v` is a join-tree leaf, this
first incident factor is initially the fixed tree edge `f=(v,u)`.  The second
null factor closes the coordinate.  Between them, if the next projected base
factor is `s=(a,b)`, its lift is either

```text
s,       which transports the coordinate from a to b, or
h_b,     which keeps the coordinate at a.
```

If `s` misses the current coordinate, its lift is forced to be `s`.

### 2.3 Moving the opening null and making a square

Let the moving opening null be `h_a`.  The two exhaustive cases in the table
are handled by the group identities

```text
h_a s   = s (s h_a s),                              (2.3)
h_a h_b = (a,b) h_a.                                (2.4)
```

Identity (2.3) is a right Hurwitz swap; (2.4) follows from
`(a,b)=h_a h_b h_a` and is the inverse swap.  Both identities use the project
multiplication convention because they are equalities of the ordered group
products as displayed.

While the two nulls are nonadjacent, the pair in (2.3) or (2.4) has an
unchanged factor immediately to its right.  Padding by that factor turns the
pair identity into one literal same-product length-three replacement.  The
projected base factor moves left and the opening null moves right by one
position.  Repeat until the two null increments are adjacent.  Since opening
and immediately closing an insertion coordinate use the same factor, the
adjacent pair is a square `h h`.

All factors now outside that square are the base word `z`, in its original
order.  Refresh the square label with one padded H3 move:

```text
c h h = c = c f f,  or  h h c = c = f f c.          (2.5)
```

Then slide `f f` right through the remaining base factors using

```text
f f c = c = c f f.                                  (2.6)
```

The endpoint is `z f f`.  There are at most `m-2` null swaps, one refresh,
and at most `m-2` slides, hence at most `2m-3` transitions.

Every replacement in (2.3)--(2.6), after padding where needed, has exactly
the same ordered three-factor product.  It preserves word length and the
identity endpoint.  It also preserves `Del_v=z`.  The base `z` has connected
support on `X`, and throughout the path two factors still attach `v`, so
every intermediate factorization remains in `F_N`.  The join edge at `v`
may change during (2.3)--(2.4); this is why the lemma is a full-K path and not
a fixed-`T` restriction path.

For any length-three product `g`, its conditional fiber has at most `M^3`
ordered words.  Selecting `r=3`, the one relevant window, and the specified
outcome therefore has probability at least (1.2).  This accounts for
laziness, the exact `|R_m|`, window count `m-2`, and conditional-fiber size.

### 2.4 Cell sizes and hubs

The accepted M49 strand-deletion lemma gives the uniform cell bound (1.1):
for fixed base and fixed two null positions there are at most `(N-1)^2`
lifts, and there are `binom(m,2)` choices of positions.

For each labeled tree `T`, choose one leaf `v(T)` deterministically, let
`f=(v,u)`, and partition `F_N(T)` by the cells `C_(T,v,z)`.  The hub of a cell
is

```text
h_(T,v,z)=z f f.                                     (2.7)
```

Choose any transposition `s` on `X`.  If `c` is the final factor of `z`, the
last H3 window of (2.7) changes

```text
c f f -> c s s.                                     (2.8)
```

The target is `z s s`, which omits `v` and is outside `F_N`.  The exact
fiber here has size `D_N=(3N^2+N-12)/2`, but the weaker uniform probability
lower bound `p_*` is enough.

### 2.5 First-boundary charging proof of Claim C

Let `A subseteq F_N` be nonempty.  In each chosen cell put
`a_C=|A intersect C|`.

If the hub (2.7) is in `A`, the transition (2.8) is an `A`-boundary edge,
because its target is outside `F_N` while `A subseteq F_N`.  Distinct cells
have distinct hubs.  Since `a_C<=Lambda_N`, these cells contribute at least

```text
(p_*/|Omega|) sum_(hub in A) a_C/Lambda_N.           (2.9)
```

If the hub is outside `A`, route every `x in A intersect C` by Claim B to
that hub and assign `x` to the first directed edge on its path that leaves
`A`.  This edge stays inside `F_N`.  Every such edge has K probability at
least `p_*`.

The assignment multiplicity is polynomial.  If an edge is used by a
canonical path for a candidate deleted label `v`, both endpoints determine
the preserved base `z=Del_v`.  There are at most `N` choices for `v` and at
most `N-1` choices for the original leaf neighbor `u`.  Given `(v,z,u)`, the
original tree is the join tree of `z` with the leaf edge `(v,u)` added, so the
cell is determined.  That cell contains at most `Lambda_N` starts.  Hence one
directed boundary edge is charged by at most

```text
N(N-1)Lambda_N                                      (2.10)
```

states.  The hub-outside cells contribute at least

```text
(p_*/|Omega|) sum_(hub outside A) a_C/[N(N-1)Lambda_N].  (2.11)
```

There is deliberately no path-length factor in (2.10).  This is a
conductance cut-counting injection, not a Poincare multicommodity-flow
comparison: each starting state is assigned only once, to its first cut
crossing.  The path length `2m-3` controls construction time, while the number
of starts assigned to one crossing is bounded directly by cell recovery.
Were the full path used in a Dirichlet comparison, a length factor would be
required.

The edges in (2.9) leave `F_N`, whereas those in (2.11) stay in `F_N`, so the
two counted families are disjoint.  Summing, using global uniformity
`pi(A)=|A|/|Omega|`, and weakening the first denominator to the second proves
(1.3).  Finally, with `|R_m|<=3`, `m-2<=2N`, `M^3<=N^6`, and
`Lambda_N<=2N^4`, the exact bound is at least `1/(24N^13)`.

All H4 and H5 boundary flow remains present and nonnegative; Claim C uses
only specified H3 outcomes.

## 3. Worst-case probability, runtime, path length, and congestion

- Every canonical path step has probability at least
  `p_*=1/[2|R_m|(m-2)M^3]` and path length at most `2m-3`.
- Every deletion cell has size at most `Lambda_N`.
- The first-boundary assignment load is at most `N(N-1)Lambda_N`; no path
  length is omitted because only one first crossing is charged per state.
- The resulting escape is exactly the first expression in (1.3), safely at
  least `1/(24N^13)`.
- Constructing a path is polynomial: with prefix deletion coordinates
  maintained, at most `2m-3` local rewrites are produced in `O(mN)` direct
  arithmetic time (or `O(m^2N)` under naive full revalidation).
- The exact N=5 leaf-cell run enumerated three tree shapes and completed in
  35.811897728126496 seconds.  The canonical-path falsifier checked 75,802
  state-leaf pairs in 21.42183013795875 seconds, with maximum observed path
  length 7 and zero failures.  These finite runtimes are not an asymptotic
  sampler claim.

## 4. Dependencies, with status

1. **PROVED HERE:** commuting multi-strand core invariant; infinite path-tree
   reducibility; identities (2.3)--(2.6); universal canonical path; exact
   first-boundary recovery; and Claim C.
2. **PROVED / INHERITED FROM ACCEPTED M49:** leaf-strand deletion has exactly
   two null increments, outputs `F_(N-1)(T-v)`, preserves the surviving join
   tree, and satisfies the lift bound (1.1).
3. **PROVED / INHERITED COMMON CORE:** exact adjacent-square H3 refresh and
   `D_N`; only the trivial upper bound `|F_3(g)|<=M^3` is needed for general
   path steps.
4. **PROVED / INHERITED:** global uniform heat-bath reversibility and
   stationarity; global K irreducibility.  Claim C itself uses uniformity but
   not irreducibility.
5. **EXACT FINITE FACT, NONASYMPTOTIC:** N=4/N=5 component and flow audits;
   exhaustive canonical-path validation through all representative fixed
   tree shapes at those sizes.
6. **UNRESOLVED:** arbitrary cuts that contain both minimal-macro and exterior
   states.

## 5. First unproved standalone proposition

**MACRO-CLOSED CORE-LIFT LEAKAGE.** Let `T_N` be a path, let `Core` delete its
two original leaves, and let `B_N` be a stationary-mass-balanced subset of the
fixed core fiber.  Put

```text
A_N={w in F_N(T_N):Core(w) in B_N},
S_N=F_N^c union A_N.                                 (5.1)
```

Either prove a universal inverse-polynomial lower bound on
`Phi_pm^K(S_N)` for every such `B_N`, including all internal H3/H4/H5 flow
and exact global mass orientation, or exhibit an explicit sequence `B_N`
for which the conductance is superpolynomially small.  The macro targets in
(2.8) lie inside `S_N`, so Claim C does not decide (5.1).  A stronger version
must allow core-defined partial cells across many join trees, because cuts
with whole tree fibers are already controlled by M58.

## 6. Strongest self-attack / failure mode

Claim C is not a fixed-tree restriction gap: its canonical paths temporarily
change the join tree, and its hub certificate exits `F_N`.  Therefore it does
not supply the missing restriction constant in a standard decomposition.
More importantly, a global cut can include `F_N^c` together with selected
internal states, absorbing every explicit macro target `z s s`.  The proof
then loses its hub-in-`A` case completely.  This is precisely the gap in
(5.1), not a normalization detail.

The reducibility of `P_T^leaf` also shows that no argument may silently use a
positive leaf-cell gap.  Its exact N=5 components are not evidence of a
global bottleneck: literal K crosses them at constant finite rates.  Finally,
the finite canonical-path validation checks the universal local identities
but does not replace their algebraic proof.

## 7. Calibration suite

- Odd `m`: `Omega` is empty; Claims A--C concern `m=2N-2` only.
- `m=0` and `N=2` even are singleton calibrations.  The disconnected
  `m=2,N>=3` case is excluded; no length-two simulation is used.
- `N=3,m=4`: `Omega` has 27 words and pure Hurwitz has 4 components.  The
  theorem applies with `|R_m|=2`; H4 is a whole-word heat bath and is retained
  as extra flow.  Deleting both leaves of a path leaves one vertex, so the
  infinite reducibility argument correctly starts only at `N=5`.
- `S_4,m=4`: 120 words and 13 Hurwitz components; H4 is whole-word.  This is
  not the four-label minimal full-support length used in Claim C.
- `S_4,m=6`: the exact audit uses all 3,936 bridge words and all minimal fixed
  tree fibers; the inherited pure-Hurwitz count is 17.  Both star and path
  leaf-cell chains are connected at this size, consistent with a singleton
  pruned core.
- Path and star trees are treated separately: path `N>=5` refutes
  `P_T^leaf`, while star cores are trivial.  Claim C is uniform over both.
- Doubled-tree words calibrate nonempty fibers and core lifts.  No global
  doubled-tree or adjacent-square hub is used: each cell has polynomial size,
  and (2.10) recovers the cell from a boundary edge up to only `N(N-1)`
  choices.
- Ordered factors and strand histories are retained exactly.  No parity,
  degree-parity, commuting-component, or graph-only quotient is used.
- The known length-two local-simulation failure is untouched; every path step
  is a literal H3 outcome.
- No stationary-mass assumption is hidden.  Claim C proves `Q/pi(A)` first,
  and `min{pi(A),pi(A^c)}<=pi(A)` gives the two-sided statement for either
  orientation.

## 8. Artifacts and reproduction commands

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-13/mission-M60-fixed-tree-leaf-cell-expansion/
```

Commands from repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M60-fixed-tree-leaf-cell-expansion/leaf_cell_audit.py \
  --N 4 --shape all \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M60-fixed-tree-leaf-cell-expansion/leaf-cell-N4.json

PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M60-fixed-tree-leaf-cell-expansion/leaf_cell_audit.py \
  --N 5 --shape all \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M60-fixed-tree-leaf-cell-expansion/leaf-cell-N5.json

PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M60-fixed-tree-leaf-cell-expansion/strand_canonical_path_falsifier.py \
  --N 4 --shape all \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M60-fixed-tree-leaf-cell-expansion/strand-path-N4.json

PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M60-fixed-tree-leaf-cell-expansion/strand_canonical_path_falsifier.py \
  --N 5 --shape all \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M60-fixed-tree-leaf-cell-expansion/strand-path-N5.json
```

Metadata: commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python
3.12.3, seed `null`, no nonstandard dependency.  The audit can optionally use
SciPy for numerical finite spectra, but no spectrum was used in the frozen
claims.

SHA-256:

```text
2ae9efde577df777a41565981452a0836f4b1e4a8ce292028630e701c30dceac  leaf_cell_audit.py
e028ef941520c4bed7eaafe444ce2484ead867ed768ede46eb16e06fe1c98021  leaf-cell-N4.json
afd3dbf88f727ed31f01b7dfa8b44ab9870770f6be077a610079a5a937656f79  leaf-cell-N5.json
fb49226dd025d74a5541c3e22c5be520fb8dbd2973e47db54551cfb43a39631e  strand_canonical_path_falsifier.py
64a96e0dde781e6f65b0fac912ead4ace31ef49c8fd3ba630bdc3f189630d834  strand-path-N4.json
0ba2b7eb39c603b961d7bfbfe6ab529b3e1c4a86447ed5c5fea44474579c4dd2  strand-path-N5.json
```

The preliminary `leaf-cell-N5-path-core.json` is retained append-only; the
all-shape `leaf-cell-N5.json` supersedes it.

## 9. Verdict

**PROVED.** The scoped M60 full-K claim is proved: every cut contained in the
entire minimal macro has inverse-polynomial escape (1.3).  Separately, the
proposed auxiliary leaf-cell gap is rigorously refuted by an explicit
infinite path-tree family.  This verdict is nonterminal for the global goal.

