# M52 final report: macro-closed leaf and centroid thresholds have polynomial full-`K` escape

Date: 2026-08-11.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

This report proves inverse-polynomial conductance for both ways of assigning
the entire nonminimal complement to one side of a leaf-count or
centroid-balance threshold.  The placement that seals the old high-side
deletion certificate is handled by a new low-side reservoir.  The result is
scoped and nonterminal; the verdict is `PROVED`.

## 1. Exact claims, quantifiers, and convention

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and words evaluate as
`t_1...t_m`.  The exact chain is

```text
K=(1/2)I+(1/(2|R_m|)) sum_(r in R_m)
       (1/(m-r+1)) sum_i H_(i,r),
R_m={r in {3,4,5}:r<=m},
```

with every `H_(i,r)` uniform on the same-product transposition fiber.  Its
stationary target `pi` is uniform on global `Omega(N,m)`.

Fix `N>=4`, `m=2N-2`, and let `F_N` be the minimal connected full-support
identity macro.  For a tree `T`, let `ell(T)` be its number of leaves and

```text
b(T)=max_(e in E(T)) min{|C_e|,N-|C_e|}
```

its edge balance, equivalently its minimum largest centroid branch.  For a
statistic `s in {ell,b}` and a threshold `q`, put

```text
H_q^s={w in F_N:s(T_J(w))>=q},
L_q^s=F_N\\H_q^s,
A_(q,+)^s=F_N^c union H_q^s,
A_(q,-)^s=F_N^c union L_q^s.                         (1.1)
```

The nontrivial threshold ranges are

```text
leaf count:
  A_(q,+)^ell, 3<=q<=N-1;
  A_(q,-)^ell, 2<=q<=N-1;

edge balance:
  A_(q,+)^b,   2<=q<=floor(N/2);
  A_(q,-)^b,   1<=q<=floor(N/2).                     (1.2)
```

The omitted `+` endpoints have empty complements.  For every cut in (1.2),

```text
Phi_pm^K(A)
 :=Q_K(A,A^c)/min{pi(A),pi(A^c)}
 >=1/(24N^7).                                        (1.3)
```

Thus neither orientation of these macro-closed scalar profile thresholds can
give a superpolynomial bottleneck.

## 2. Full proof

### 2.1 Exact stationary masses

Let

```text
Z_N=|Omega(N,2N-2)|,
C_0(N)=|F_N|=(2N-2)!N^(N-3),
h_q^s=|H_q^s|, l_q^s=|L_q^s|=C_0(N)-h_q^s.          (2.1)
```

The global count is exactly

```text
Z_N=(1/N!) sum_(lambda partition N)(f^lambda)^2 c_lambda^(2N-2),
c_lambda=sum_((i,j) in lambda)(j-i).                 (2.2)
```

Indeed the transposition class sum acts by content scalar `c_lambda` in the
irreducible representation `lambda`, and regular-trace coefficient extraction
gives (2.2).  Therefore

```text
pi(A_(q,+)^s)=1-l_q^s/Z_N,
pi((A_(q,+)^s)^c)=l_q^s/Z_N,
pi(A_(q,-)^s)=1-h_q^s/Z_N,
pi((A_(q,-)^s)^c)=h_q^s/Z_N.                        (2.3)
```

No claim that `pi(F_N)` lies on a particular side of `1/2` is required.

### 2.2 Strand deletion and its multiplicity

The statistic-free input is the following leaf-strand lemma.  If `v` is a
leaf of `T_J(w)` for `w in F_N`, erase `v` from every prefix permutation.
Every induced increment on the other `N-1` labels is a transposition or the
identity; exactly two are identities.  Deleting them produces a word in
`F_(N-1)` with join tree `T_J(w)-v`.

For completeness, encode a permutation above its `v`-erasure by the
predecessor of `v` in its cycle, or by `bottom` when `v` is fixed.  A
non-`v` transposition projects unchanged and swaps the insertion coordinate.
A factor `(v,x)` is null precisely when it enters from `bottom` at `x` or
exits from coordinate `x`; otherwise it projects to the transposition between
`x` and the current coordinate.  The unique join edge incident to `v` gives
one null.  The nonnull projected word is connected and identity, so it has
length at least `2N-4`; sign forces the positive null count to be even, hence
exactly two.  Internal projected factors remain within leaf-deleted prefix
components, proving the join-tree statement.

For fixed deleted label, output word, and the two null positions, there are at
most `(N-1)^2` lifts.  There are `N-1` first insertion coordinates.  A
projected support join has a forced lift; a projected cut may branch, but its
two descendants occupy distinct permutation cycles in one support component.
Minimality forbids those cycles from rejoining internally, so one initial
coordinate has at most `N-1` descendants.  After summing the null positions,
the deletion fiber is bounded by

```text
Lambda_N=binom(m,2)(N-1)^2.                           (2.4)
```

### 2.3 A new low-leaf reservoir

Write `l_N^ell(q)=|L_q^ell|`.  Deleting a tree leaf does not increase leaf
count:

```text
ell(T-v)=ell(T)-1+1{the neighbor of v has degree 2}<=ell(T).
```

Choose one leaf in each low state, apply strand deletion, and sum over its
`N` possible labels.  Then

```text
l_N^ell(q)<=N Lambda_N l_(N-1)^ell(q).               (2.5)
```

Conversely, fix new label `v=N`.  From every base word counted by
`l_(N-1)^ell(q)`, choose a canonical leaf `u` of its join tree and insert the
adjacent square `(v,u)^2` in any of the `m-1` gaps.  Old leaf `u` becomes
degree two and `v` becomes a leaf, so total leaf count is unchanged and the
new word is still low.  Since `v` appears exactly in this square, deletion
recovers the base, gap, and attachment.  The new source set has exact size

```text
|S_low^ell|=(m-1)l_(N-1)^ell(q).                     (2.6)
```

This source set is distinct from the high-profile reservoir counted in M51.

### 2.4 A new low-balance reservoir

Write `l_N^b(q)=|L_q^b|`.  Deleting a tree leaf cannot increase edge balance.
For every surviving edge, if the deleted leaf lay on a side of size `a`, its
new smaller-side size is `min(a-1,N-a)<=min(a,N-a)`; the removed leaf edge
disappears.  Hence the same deletion count gives

```text
l_N^b(q)<=N Lambda_N l_(N-1)^b(q).                   (2.7)
```

For the reverse reservoir, choose a canonical centroid `u` of each base join
tree and insert `(v,u)^2`.  For every old edge, the side not containing `u`
lies in one centroid branch and has size at most half the base tree.  Adding
`v` to the `u` side leaves that smaller-side size unchanged.  The new edge has
balance one, so total balance is exactly unchanged.  Again uniqueness gives

```text
|S_low^b|=(m-1)l_(N-1)^b(q).                         (2.8)
```

This is the new certificate needed when the old high-balance exit is sealed.

### 2.5 Exact low-side transition and the `+` placement

For a source from (2.6) or (2.8), use the `H3` window beginning with its
marked square, or ending with it if the square is last.  With padding
transposition `a` and a fixed base-label transposition `f`, specify

```text
((vu),(vu),a)->(f,f,a),
(a,(vu),(vu))->(a,f,f).                              (2.9)
```

Both block products are `a`.  The target omits label `v`, hence lies in
`F_N^c subset A_(q,+)^s`, while the source lies in the complementary low
profile side.  For fixed `a`, the exact triple-fiber size is

```text
D_N=(3N^2+N-12)/2,                                   (2.10)
```

so laziness, three block sizes, `m-2` windows, and the uniform fiber give

```text
p_N=1/[6(m-2)D_N].                                   (2.11)
```

For either statistic, (2.4)--(2.8) imply

```text
|S_low^s|/l_N^s(q)>=2/[Nm(N-1)^2].                  (2.12)
```

Using the exact complement mass in (2.3),

```text
Phi_pm(A_(q,+)^s)
 >=Q(A_(q,+)^s,(A_(q,+)^s)^c)/(l_q^s/Z_N)
 >=1/[3Nm(N-1)^2(m-2)D_N]
 >=1/(24N^7).                                        (2.13)
```

The first inequality is valid even if the macro-closed side is the smaller
one, because the minimum of the two masses is at most `l_q^s/Z_N`.

### 2.6 The opposite placement

For `A_(q,-)^s`, the complement is the high-profile side.  The same adjacent
square now starts in that high side and refreshes into
`F_N^c subset A_(q,-)^s`.

For leaves, strand deletion lowers leaf count by at most one.  It gives

```text
h_N^ell(q)<=N Lambda_N h_(N-1)^ell(q-1).             (2.14)
```

From a base with exactly `q-1` leaves, its `N-q` nonleaves raise the new tree
to `q`; from a deeper base choose `N-q` canonical attachments.  Thus the high
source size is `(N-q)(m-1)h_(N-1)^ell(q-1)`, and

```text
Phi_pm(A_(q,-)^ell)
 >=(N-q)/[3Nm(N-1)^2(m-2)D_N]
 >=1/(24N^7).                                        (2.15)
```

For balance and `q<N/2`, deletion plus all `N-1` leaf attachments gives

```text
Phi_pm(A_(q,-)^b)
 >=1/[3Nm(N-1)(m-2)D_N]
 >=1/(24N^6).                                        (2.16)
```

At the even endpoint `N=2q`, deletion lands in the maximum base layer
`q-1`; attach to one of the `q-1` vertices on the smaller side of a canonical
`q-1,q` edge.  This gives

```text
Phi_pm(A_(q,-)^b)
 >=(N-2)/[6Nm(N-1)^2(m-2)D_N]
 >=1/(96N^6)
 >=1/(24N^7).                                        (2.17)
```

Equations (2.15)--(2.17) use `min mass <=h_q^s/Z_N`, exactly as (2.13) used
the low-side mass.  They include leaf `q=2` and balance `q=1`, where the high
side is all of `F_N`.

### 2.7 Complete `H3/H4/H5` and internal/macro accounting

For either orientation, split the literal boundary flow into

```text
Q_K=Q_(3,macro)+Q_(3,internal)
   +Q_(4,macro)+Q_(4,internal)
   +Q_(5,macro)+Q_(5,internal).                      (2.18)
```

Here `macro` means exactly one endpoint lies in `F_N`; `internal` means both
do.  The specified refresh contributes to `Q_(3,macro)`.  Every other triple
outcome, every within-`F_N` leaf-reattachment crossing, and all `H4,H5`
contributions remain in (2.18) and are nonnegative.  A direct internal
reattachment is also explicit: `(v,u)^2,a ->(v,u')^2,a` has the same exact
probability (2.11).  It is not needed for the lower bound.

Because this is a lower-flow theorem, retaining all those terms as
nonnegative is complete accounting.  An upper-flow Terminal-B claim could
not make the same simplification.

## 3. Probability, runtime, path length, and congestion accounting

- Every certificate is one transition of the original chain; there is no
  comparison path, path length, congestion, or vertex load.
- The exact transition probability is (2.11), `Omega(N^-3)`.
- Every new low source fraction is at least `2/[Nm(N-1)^2]`,
  `Omega(N^-4)`; their product gives (2.13).
- The high source fractions and exceptional endpoint are displayed exactly
  in (2.15)--(2.17).
- Constructing a join tree, finding a leaf or centroid, and recognizing the
  marked source are polynomial in `N,m`; exact triple-fiber enumeration is
  `O(N^2)`.
- The finite audit postprocesses exact fixed-tree layers through `N=8` and
  evaluates the character sum over partitions.  The upstream state/tree
  enumeration is exponential and is only a bounded falsifier.

## 4. Dependencies, each labeled

1. **PROVED HERE:** both new low-side deletion inequalities, canonical leaf
   and centroid insertion reservoirs, exact global orientation, full flow
   decomposition, and theorem (1.3).
2. **PROVED HERE / INDEPENDENTLY PRESENT IN M49:** strand deletion and its
   lift multiplicity, restated in section 2.2.
3. **PROVED HERE / INDEPENDENTLY PRESENT IN M49--M51:** the high-side counts,
   including both exceptional endpoints, rederived in section 2.6.
4. **INHERITED PROVED:** uniform stationarity/reversibility, minimal
   factorization count `C_0(N)`, and exact polynomial block sampling.
5. **PROVED STANDARD CHARACTER CALCULATION:** global count (2.2), checked
   against `S_4,m=6` and the exact finite bridge counts.
6. **EXACT FINITE:** 24 low-tail thresholds and exact global masses through
   `N=8`; finite agreement is not used as the universal proof.
7. **REFUTED / NOT USED:** identification with an auxiliary uniform
   plane-tree or parking chain.
8. **EMPIRICAL:** none.

## 5. First unproved standalone proposition

> **MACRO-CLOSED JOINT-PROFILE FLOW.**  For feasible `q,r`, let
>
> ```text
> J_(N,q,r)={w in F_N:ell(T_J(w))>=q and b(T_J(w))>=r}.
> ```
>
> Both global cuts `F_N^c union J_(N,q,r)` and
> `F_N^c union (F_N\\J_(N,q,r))` have conductance at least `cN^-C` for
> universal `c,C`, uniformly in `N,q,r` whenever both sides are nonempty.

The scalar deletion/insertion choices here need not preserve two profile
constraints simultaneously.  This is the first natural refinement capable
of excluding both canonical low reservoirs without becoming an arbitrary cut.

## 6. Strongest self-attack / failure mode

The result still relies on a one-label macro exit.  It is stronger than
M49/M51 because it constructs the previously missing low-profile reservoirs
and treats both placements of `F_N^c`, but it proves no internal mixing of
`F_N`.  A refinement can select only profile-layer states that avoid the
canonical leaf/centroid insertions, and a joint profile can make each safe
attachment violate the other constraint.

The strand map remains a counting map rather than a Poincare intertwining.
Nothing here controls arbitrary cuts, surplus lengths, or the global gap.
Hence the theorem rules out this larger candidate family but is not Terminal
A or Terminal B.

## 7. Calibration suite

- **Odd `m`:** `Omega(N,m)` is empty; the theorem uses even `m=2N-2`.
- **`m=0`, `N=2`:** singleton cases lie outside `N>=4`.
- **`m=2,N>=3`:** excluded; no length-two simulation is used.
- **`S_3,m=4`:** 27 words and four pure-Hurwitz components.  Since
  `R_m={3,4}`, whole-word `H4` has coefficient `1/4`; the present theorem
  starts at `N=4,m=6` and does not alter that normalization.
- **`S_4,m=4`:** 120 words and 13 Hurwitz components; whole-word `H4` remains
  part of the exact chain.
- **`S_4,m=6`:** `Z_4=3936`, `C_0(4)=2880`, and
  `pi(F_4)=30/41`.  For leaf `q=3`, the new `+` cut has exact masses
  `75/164` and `89/164`; this shows why orientation cannot be guessed.  For
  balance `q=2`, its masses are `133/164` and `31/164`.  Both low source sets
  have exactly `5*24=120` states.
- **Exact `N<=8`:** all 24 low-tail rows pass; exact `pi(F_N)` decreases from
  `30/41` at `N=4` to
  `6376469299200/29610634152901` at `N=8`.
- **Near-minimal doubled trees:** all states in `F_N` are covered; adjacent
  squares are constructed only in the counted reservoir, not assumed in an
  arbitrary input.
- **Order/components:** every source and target is a literal ordered word;
  leaving `F_N` still lands in global `Omega`.  No graph-only quotient is
  used.
- **Parity:** sign appears only in strand deletion; degree/edge parity is not
  used as an identity characterization.
- **Canonical hub / `L=2`:** neither appears.
- **Mass orientation:** exact formulas (2.3), rather than conditional mass or
  a presumed `pi(F_N)<1/2`, handle both sides.

## 8. Artifact paths and reproduction commands

Owned artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M52-macro-closed-tree-profile-redteam/
  plan.md
  checkpoint.md
  report.md
  macro_closed_audit.py
  macro-closed-N4-N8.json
```

Exact deterministic command (`seed=null`, Python 3.12.3, no nonstandard
dependency):

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M52-macro-closed-tree-profile-redteam/macro_closed_audit.py --source-dir experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M52-macro-closed-tree-profile-redteam/macro-closed-N4-N8.json
```

SHA-256 hashes:

```text
349e310147fec2e0379d366c2a68c1990456b291dbf6324e15160eea742acf5a  macro_closed_audit.py
602743a38f61557d3aeef050744ab7a09e7d5113f0f21b96017f74d02758a2c6  macro-closed-N4-N8.json
```

The JSON records the exact character masses, all low-tail counts, source
counts, threshold inequalities, convention, commit, and finite-scope warning.
No bytecode cache is present.

## 9. Verdict

**PROVED.**

This verdict is scoped to both macro-closed orientations of every nontrivial
leaf-count and centroid/edge-balance threshold.  It is not Terminal A or
Terminal B.  The first stronger named cut is the joint-profile proposition
in section 5.
