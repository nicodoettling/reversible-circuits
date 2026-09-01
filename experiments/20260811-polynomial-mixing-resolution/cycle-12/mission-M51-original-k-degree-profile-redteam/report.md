# M51 final report: leaf-count and maximum-degree thresholds have polynomial full-`K` escape

Date: 2026-08-11.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

This report proves direct original-chain anti-bottleneck bounds for two
label-symmetric degree-profile statistics of the actual prefix join tree.  No
auxiliary plane-tree or parking stationary law is used.  The result is scoped
and nonterminal; the verdict is `PROVED`.

## 1. Exact claims, quantifiers, and convention

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and words evaluate as
`t_1...t_m`.  The chain is

```text
K=(1/2)I+(1/(2|R_m|)) sum_(r in R_m)
       (1/(m-r+1)) sum_i H_(i,r),
R_m={r in {3,4,5}:r<=m},
```

where every `H_(i,r)` is uniform on the exact same-product transposition
fiber.  Its stationary target `pi` is uniform on global `Omega(N,m)`.

Fix `N>=4`, `m=2N-2`, and let `F_N` be the connected full-support minimal
identity macro.  For a tree `T`, write `ell(T)` for its number of leaves and
`Delta(T)` for its maximum degree.  For `2<=q<=N-1`, define global cuts

```text
L_(N,q)={w in F_N:ell(T_J(w))>=q},
D_(N,q)={w in F_N:Delta(T_J(w))>=q}.                 (1.1)
```

All words outside `F_N` are in the complement.  Put

```text
D_N^3=(3N^2+N-12)/2.                                 (1.2)
```

The superscript distinguishes this triple-fiber size from the cut `D_(N,q)`.

### Theorem A: every leaf-count threshold

For all stated `N,q`,

```text
Phi_pm^K(L_(N,q))
 >=(N-q)/[3N(2N-2)(N-1)^2(2N-4)D_N^3]
 >=1/(24N^7).                                        (1.3)
```

### Theorem B: every maximum-degree threshold

For all stated `N,q`,

```text
Phi_pm^K(D_(N,q))
 >=1/[3N(2N-2)(N-1)^2(2N-4)D_N^3]
 >=1/(24N^7).                                        (1.4)
```

Here `Phi_pm(A)=Q_K(A,A^c)/min{pi(A),pi(A^c)}`.  Both sides of every cut are
nonempty.  Equations (1.3)--(1.4) include the extreme `q=N-1` star layer.

## 2. Full proof

### 2.1 Statistic-free strand deletion

The following lemma is proved directly because it is the common counting
input; it does not assume any distribution on trees.

**Leaf-strand lemma.**  If `w in F_N` and `v` is a leaf of `T_J(w)`, erase
`v` from every prefix permutation.  Each induced increment on
`[N]\\{v}` is a transposition or the identity, exactly two increments are
identities, and deleting them gives a word in `F_(N-1)` whose join tree is
`T_J(w)-v`.  For fixed `v`, fixed output word, and fixed locations of the two
identity increments, there are at most `(N-1)^2` inputs.

To prove it, represent a permutation above its `v`-erasure by the predecessor
`a` of `v` in its cycle, or `bottom` if `v` is fixed.  Right multiplication
by `(xy)` with `x,y!=v` projects to `(xy)` and sends `a` to `(xy)(a)`.
Right multiplication by `(v,x)` is null precisely when it enters from
`bottom` at `x` or exits from `a=x` to `bottom`; otherwise it projects to
`(a,x)` and leaves `a` fixed.

The unique support join incident to join-tree leaf `v` is a null increment.
All other join-tree edges survive, so the projected nonnull word has
connected support and evaluates to the identity.  Its length is at least
`2N-4`; sign makes the positive number of nulls even, so there are exactly
two.  A projected factor arising from an old internal `(v,x)` remains inside
one leaf-deleted prefix component, hence the output join tree is exactly
`T_J(w)-v`.

For multiplicity, choose the first insertion coordinate in `N-1` ways.  A
projected support join has a forced lift; a `v`-incident alternative would
give `v` a second join edge.  A projected cycle cut can branch a lift into
two, but its descendants occupy the two distinct cycles created by the cut.
Descendants of one initial coordinate can never reunite: they lie in the same
support component, and a later internal cycle join is impossible in a
minimal identity word.  Thus at most `N-1` descendants coexist.  This gives
`(N-1)^2` lifts for fixed null positions, and therefore

```text
Lambda_N=binom(m,2)(N-1)^2                           (2.1)
```

after summing over the two positions.

### 2.2 Leaf-count threshold counts

Let `J_N(q)=|L_(N,q)|`.  If `v` is a tree leaf with neighbor `u`, then

```text
ell(T-v)=ell(T)-1+1{deg_T(u)=2}.                      (2.2)
```

In particular, every tree with at least `q` leaves deletes at any chosen leaf
to a tree with at least `q-1` leaves.  Choose one leaf deterministically,
apply the leaf-strand lemma, and sum over its `N` possible labels.  This gives

```text
J_N(q)<=N Lambda_N J_(N-1)(q-1).                     (2.3)
```

For the reverse reservoir fix the new label `v=N`.  A base tree on `N-1`
vertices with exactly `q-1` leaves has exactly

```text
(N-1)-(q-1)=N-q                                      (2.4)
```

nonleaves.  Attaching `v` to any of them increases the leaf count to `q`.
If the base already has at least `q` leaves, every attachment preserves the
threshold; select the first `N-q` labels deterministically.  Insert the
adjacent square `(v,u)^2` in any of the `m-1=2N-3` gaps.  The only factors
incident to `v` recover `u`, the gap, and the base word, so no overlap factor
is lost.  The source set has exact size

```text
|S_L|=(N-q)(m-1)J_(N-1)(q-1).                       (2.5)
```

When `q=N-1`, the base layer consists of stars, (2.4) equals one, and the
unique nonleaf is the center.  Thus the endpoint is genuinely included.

### 2.3 Maximum-degree threshold counts

Let `A_N(q)=|D_(N,q)|`.  Deleting a tree leaf reduces every old degree by at
most one, so

```text
Delta(T-v)>=Delta(T)-1.
```

The same deletion count gives

```text
A_N(q)<=N Lambda_N A_(N-1)(q-1).                     (2.6)
```

If a base tree has maximum degree exactly `q-1`, attach `v` to the
lexicographically first maximum-degree vertex, raising the maximum to `q`.
If it already has maximum degree at least `q`, attach at the
lexicographically first vertex; membership is preserved.  One attachment per
base and all `m-1` gaps give a distinct source set of exact size

```text
|S_D|=(m-1)A_(N-1)(q-1).                             (2.7)
```

At `q=N-1`, this again attaches to the center of a base star.

### 2.4 Exact full-`K` boundary flow and global orientation

For each source in (2.5) or (2.7), choose the `H3` window starting with its
marked square, or ending with it when the square is the final pair.  With
padding transposition `a` and a fixed base-label transposition `f`, specify

```text
((vu),(vu),a)->(f,f,a),
(a,(vu),(vu))->(a,f,f).                              (2.8)
```

The block product remains `a`, and the target omits label `v`, so it lies
outside `F_N` and outside either cut.  The exact number of length-three
transposition words with product `a` is

```text
D_N^3=M+6(N-2)+2 binom(N-2,2)
     =(3N^2+N-12)/2,  M=binom(N,2).                  (2.9)
```

Including laziness, choice among three block sizes, choice among `m-2`
three-windows, and the exact conditional fiber, the specified outcome has
probability

```text
p_N=1/[6(m-2)D_N^3].                                 (2.10)
```

For either cut `C`, the complete boundary is

```text
Q_K(C,C^c)=Q_3(C,C^c)+Q_4(C,C^c)+Q_5(C,C^c)
          >=pi(S_C)p_N.                              (2.11)
```

All `H4,H5` flow remains in the exact chain as nonnegative flow.  The exact
global masses are `pi(C)=|C|/|Omega(N,m)|` and
`pi(S_C)=|S_C|/|Omega(N,m)|`.  Whichever side is smaller,

```text
min{pi(C),pi(C^c)}<=pi(C).                            (2.12)
```

For leaves, (2.1), (2.3), and (2.5) yield source fraction

```text
|S_L|/J_N(q)>=2(N-q)/[Nm(N-1)^2].                    (2.13)
```

For maximum degree, (2.1), (2.6), and (2.7) yield

```text
|S_D|/A_N(q)>=2/[Nm(N-1)^2].                         (2.14)
```

Multiplying by (2.10) proves the exact first inequalities in
(1.3)--(1.4).  Since `N-q>=1`, `m<=2N`, `m-2<=2N`, and `D_N^3<=2N^2`, both
are at least `1/(24N^7)`.

Paired star words show every cut is nonempty.  The disconnected global
identity word `(12)^m` belongs to every complement, including the thresholds
`q=2` that contain all of `F_N`.

## 3. Probability, runtime, path length, and congestion accounting

- Each certificate is one literal original-`K` transition, so comparison
  path length, congestion, and vertex load are absent.
- The exact transition probability (2.10) is `Omega(N^-3)`.
- The worst certified source fractions (2.13)--(2.14) are `Omega(N^-4)`;
  their products give `Omega(N^-7)`.
- Join-tree construction, statistic evaluation, strand deletion, and source
  recognition are polynomial in `N,m`.  Enumerating the exact triple fiber
  costs `O(N^2)`.
- The finite audit reads already exact fixed-tree dynamic-programming output;
  it processes 40 threshold rows in negligible polynomial postprocessing
  time.  The upstream enumeration itself is exponential and is not a sampler.

## 4. Dependencies, each labeled

1. **PROVED HERE:** Theorems A and B; the statistic-specific count and source
   lemmas; endpoint `q=N-1`; exact original-chain flow and orientation.
2. **PROVED HERE / INDEPENDENTLY PRESENT IN M49:** the leaf-strand deletion
   lemma and lift multiplicity (2.1).  The proof is restated in section 2.1;
   no unreviewed tree-distribution claim is imported.
3. **INHERITED PROVED:** exact heat-bath reversibility/stationarity; minimal
   join/cut counting; and polynomial exact block sampling.
4. **EXACT FINITE:** weighted leaf-count and maximum-degree layers through
   `N=8`; all 40 displayed threshold consequences pass.  Finite agreement is
   not used as proof.
5. **REFUTED / NOT USED:** equality with the auxiliary uniform plane-tree or
   parking law.
6. **EMPIRICAL:** none.

## 5. First unproved standalone proposition

> **MACRO-CLOSED TREE-PROFILE THRESHOLD FLOW.**  For either statistic
> `s in {ell,b_N}`, define the complement-enlarged cut
>
> ```text
> C_(N,q)^closed=F_N^c union {w in F_N:s(T_J(w))>=q}.
> ```
>
> There are universal `c>0,C<infinity` such that every nontrivial threshold
> satisfies
>
> ```text
> Q_K(C_(N,q)^closed,(C_(N,q)^closed)^c)
> /min{pi(C_(N,q)^closed),pi((C_(N,q)^closed)^c)} >=cN^(-C).
> ```

The macro-deletion edges used here remain inside the enlarged cut and supply
no boundary flow.  This proposition therefore requires genuine within-`F_N`
tree-profile action plus exact global stationary orientation.

## 6. Strongest self-attack / failure mode

Both proofs rely on cuts that place all of `F_N^c` in the complement.  Their
certified transition deletes the marked label.  If the cut is enlarged by
`F_N^c`, every certified edge is sealed.  The results also do not control
arbitrary subsets within one leaf/degree layer, the joint empirical degree
profile, surplus lengths, or the global gap.

The strand deletion map is a counting map, not a Markov intertwining or a
Poincare comparison.  Consequently the two scalar threshold theorems cannot
be iterated into arbitrary-cut expansion.  This is why the scoped result is
nonterminal despite its uniform exponent.

## 7. Calibration suite

- **Odd `m`:** `Omega(N,m)` is empty; the theorem uses even `m=2N-2`.
- **`m=0`, `N=2`:** singleton cases lie outside `N>=4`.
- **`m=2,N>=3`:** excluded; no length-two simulation is used.
- **`S_3,m=4`:** 27 words and four pure-Hurwitz components.  Here
  `R_m={3,4}` and the whole-word `H4` has coefficient `1/4`; it is not hidden
  in the theorem, whose range starts at `N=4,m=6`.
- **`S_4,m=4`:** 120 words and 13 Hurwitz components; the whole-word `H4`
  contribution remains essential in that separate case.
- **`S_4,m=6`:** 3936 global words, 17 Hurwitz components, and 2880 words in
  `F_4`.  Exact leaf layers are `2136` with two leaves and `744` with three;
  the maximum-degree layers are the reverse statistics on the same two tree
  shapes.  The star endpoint reservoir has exactly `5*24=120` sources.
- **Exact `N<=8`:** all 20 leaf thresholds and all 20 maximum-degree
  thresholds satisfy the count bounds in the machine-readable audit.
- **Near-minimal doubled trees:** every state here is minimal; no adjacent
  square in the input is assumed by deletion, and paired stars merely witness
  nonemptiness.
- **Order/components:** sources and targets are literal ordered words.  The
  target remains in global `Omega` while leaving `F_N`; no graph-only or
  color-word chain is substituted.
- **Parity:** sign is used only inside strand deletion; degree parity is not
  claimed to characterize identity.
- **Canonical hub / `L=2`:** neither appears.
- **Mass orientation:** (2.11)--(2.12) handles the exact global smaller side.

## 8. Artifact paths and reproduction commands

Owned artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M51-original-k-degree-profile-redteam/
  plan.md
  checkpoint.md
  report.md
  leaf_threshold_audit.py
  leaf-threshold-N4-N8.json
```

Exact deterministic command (`seed=null`, Python 3.12.3, no nonstandard
dependency):

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M51-original-k-degree-profile-redteam/leaf_threshold_audit.py --source-dir experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M51-original-k-degree-profile-redteam/leaf-threshold-N4-N8.json
```

SHA-256 hashes:

```text
a28e63a2bfc5ff08267dc13e2bc9dc8170485342be58de4c88b18a8cdebb2aa7  leaf_threshold_audit.py
8247ca799bcbee23a6aad9a1c023392b8e033300b484b9923e8bc90af40c8ad5  leaf-threshold-N4-N8.json
```

The JSON records commit, convention, exact finite claims, source artifacts,
all 40 integer rows, and the finite-scope warning.  No bytecode cache is
present.

## 9. Verdict

**PROVED.**

This verdict is scoped to the original full-`K` inverse-polynomial rejection
of every leaf-count and maximum-degree threshold cut (1.1).  It is not
Terminal A or Terminal B.  The first stronger adversarial cut is the
macro-closed proposition in section 5.
