# M75 final report: randomized partial-macro coarea and the radius-one obstruction

Date: 2026-08-12.  Recorded repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, convention, and scoped outcome

Permutations compose as `(pq)(x)=p(q(x))`, tuple products are evaluated
left-to-right, and a right Hurwitz generator acts by

```text
R_i(...,a,b,... )=(...,b,bab,...).
```

Its inverse is also allowed.  The target law is the global fixed-length
uniform law on

```text
Omega(N,m)={t in Trans(S_N)^m:t_1...t_m=id}.
```

The literal chain in scope is, at the minimal ambient length,

```text
N>=5,  m=2N-2,  M=binom(N,2),
K=(1/2)I+(1/6) sum_(r=3)^5
       (1/(m-r+1)) sum_i H_(i,r),                  (1.1)
```

where `H_(i,r)` is uniform on the transposition `r`-tuples having the same
ordered product as the selected block.  Boundary handling is exactly the
valid-window average in (1.1); `H4` and `H5` are retained and nonnegative,
although the lower bounds below use only specified `H3` outcomes.

Let `F_N` be the connected full-support minimal set from M64, let
`A subset F_N(T_N)` be the accepted nonempty proper core cell, and let
`E_k,C_k=A union E_k` be the accepted exterior balls and cuts.  A Hurwitz
macrofiber `Gamma` is specified by labeled weighted support-component data.
For a two-component minimal exterior macro, the component genera sum to one,
so one component has genus one and the other is minimal.  Let `G_Gamma` be
the states having a globally adjacent square in the genus-one component such
that deleting that square leaves the component connected.

This report has four deliberately separate outcomes.

1. **PROVED:** a state-independent randomized family of bijective Hurwitz
   words with worst-source marked hitting probability `eta` and expected
   length `Dbar` gives, for every partial subset `S subseteq Gamma`, the
   exact one-radius coarea bound

   ```text
   sum_(x in S) K(x,(Gamma minus S) union (F_N minus A))
      >=p_H eta |S|/(Dbar+1),                      (1.2)
   p_H=1/[6(m-2)M^2].
   ```

   When `S=E_k intersect Gamma`, every target in (1.2) is outside `C_k`.
   The cardinality of the word family does not occur.
2. **PROVED:** after one connected two-deletion certificate is selected,
   M60 null-pushing generalizes to a positive-genus component with a
   polynomial state-independent word family, `O(m)` path length, and exact
   actual-edge source recovery.
3. **REFUTED:** the strongest first shallow cover—one optional signed
   Hurwitz generator followed by a direct-certificate bubble—is not
   universal.  A minimal ambient `N=6,m=10` two-component state is at exact
   signed-Hurwitz distance two from the connected-certificate set.
4. **UNRESOLVED:** no worst-source polynomial marked-hit bound is proved for
   the surviving uniform positive-permutation-braid family, and no additive
   occupation theorem is proved for successive mergers from three or more
   components.

In particular, (1.2) is a conditional implication, not an unconditional
full exterior-cut theorem.  This report makes no Terminal-A or Terminal-B
claim and gives no superpolynomial conductance upper bound for a stationary
cut of the full original `K`.

## 2. Full argument

### 2.1 Randomized bijective marked-cover theorem

The following finite-state theorem is the main positive result.

**Theorem 2.1 (randomized first-crossing cover).**  Let `Gamma` be finite,
let `G subseteq Gamma`, and let `mu` be a state-independent probability law
on finite words in bijective generators of `Gamma`.  Write `ell(beta)` for
word length.  Suppose

```text
inf_(x in Gamma) Pr_(beta~mu)
  [some prefix beta_[0:t] sends x into G] >=eta,    (2.1)
E_mu ell(beta)<=Dbar.                               (2.2)
```

Let `T` be disjoint from `Gamma`.  For each `g in G`, designate a literal
edge `g -> delta(g) in T`.  If every used generator edge and every designated
terminal edge has `K`-probability at least `p`, then, for every
`S subseteq Gamma`,

```text
B_(Gamma,T)(S)
 :=sum_(x in S)K(x,(Gamma minus S) union T)
 >=p eta |S|/(Dbar+1).                              (2.3)
```

The law may have factorial, or even countably infinite, support.

**Proof.**  Give each successful pair `(x,beta)` mass `mu(beta)` and stop at
the first marked prefix time `tau`.  If the prefix path first leaves `S`,
charge its first directed edge from `S` to `Gamma minus S`.  If it has not
left `S` by time `tau`, charge the designated edge out of the first marked
state.  The total charged demand is at least `eta|S|`.

Fix a word `beta`, a prefix time, and a directed path edge.  The edge source
and the inverse prefix recover at most one original `x`, because every prefix
is a bijection.  Hence any path edge receives weighted load at most

```text
sum_beta mu(beta)ell(beta)=Dbar.                    (2.4)
```

For a fixed terminal directed edge, `beta` and the first-hit time recover
the source in the same way.  There are `ell(beta)+1` possible first-hit
times, so its weighted load is at most `Dbar+1`.  Thus every charged edge
has load at most `Dbar+1`; every such edge has `K(e)>=p`.  Dividing total
demand by maximal load proves (2.3).  This is actual directed-edge recovery,
not a projected or word-label count.  QED.

If only the endpoint event is used in (2.1), a terminal edge has load at
most one rather than `Dbar+1`.  The denominator in (2.3) then improves to
`max(Dbar,1)`.

### 2.2 Exact specialization to a two-component exterior macro

M68/M74 prove that every `g in G_Gamma` has a deterministic safe square
refresh into `F_N minus A`.  The corrected reason uses the two minimal
components' fixed prefix join trees `J_U,J_V`: after replacing the marked
square by a cross-edge square `s,s`, the target prefix join tree is

```text
J_U union J_V union {s}.
```

At most one `s` can complete this union to the fixed `T_N`, so at least
`N-2` cross edges land outside `A`.  This is a prefix-join-tree statement,
not the false support-tree wording corrected by M74.

For a transposition-product length-three fiber,

```text
D_N=M+6(N-2)+2binom(N-2,2)
   =(3N^2+N-12)/2.                                  (2.5)
```

Consequently a specified safe marked refresh has exact probability

```text
p_term=1/[6(m-2)D_N].                               (2.6)
```

A specified right or inverse Hurwitz move is a padded `H3` outcome.  Its
conditional fiber has at most `M^2` elements, because the first two output
transpositions determine the third.  Therefore

```text
p_path>=p_H=1/[6(m-2)M^2],                          (2.7)
```

including laziness, the `r=3` choice, the window scan, and the exact
heat-bath output.  Since `D_N<=M^2` for `N>=5`, Theorem 2.1 with
`T=F_N minus A` proves (1.2).

This is an arbitrary-partial-subset theorem under a worst-source cover
hypothesis.  It must not be conflated with the unconditional whole-macro
average inherited from M68/M74:

```text
Pr_(x~Unif Gamma)(x in G_Gamma)>=3/[Nm(m-1)],       (2.8)
theta_N=1/[2Nm(m-1)(m-2)D_N],                       (2.9)
E_(x~Unif Gamma)K(x,F_N minus A)>=(N-2)theta_N.     (2.10)
```

Equation (2.10) is for a whole two-component macro.  Deleting an arbitrary
portion of the macro can delete all marked states, so (2.8)--(2.10) alone do
not imply (1.2).

### 2.3 M60 null-pushing after a DYZ deletion certificate

Take two certified occurrences at positions `i<j` and write the full word
as

```text
w=P x U y S,                                        (2.11)
```

where deleting `x,y` leaves an identity word `z=P U S`, and the affected
positive-genus component remains connected.  Comparing the two products
gives

```text
x U y=U,  hence  x=U y U^(-1).                     (2.12)
```

Right-bubble `x` across the factors of `U`.  After the whole bubble its value
is `U^(-1)xU=y`, so the endpoint is

```text
P U y y S.                                          (2.13)
```

Factors belonging to other support components cause no problem: they are
disjoint from `x,y`, and the same global-position bubble remains valid.
The bubble word depends only on `(i,j)`, not on the source state, and has
length `j-i-1<=m-2`.  Thus the at most `binom(m,2)` fixed positive words
cover every source having a direct connected certificate.  Their prefixes
are bijections, so word index, prefix time, and an actual directed edge
recover at most one source.

For the literal M60-style cell canonicalization, refresh `y,y` to a fixed
internal `f,f` and slide the square through `S` via exact same-product
triples

```text
f f c -> c f f.
```

This reaches `z f f` in at most

```text
(j-i-1)+1+(m-j-1)=m-i-1<=m-1                     (2.14)
```

specified positive `H3` steps.  For fixed `z`, positions `(i,j)`, and later
transposition `y`, (2.12) forces `x`; a direct-certificate cell therefore
has at most `binom(m,2)M` such sources.

For coarea one does not route to this hub: after (2.13), use the safe cross
refresh of Section 2.2 and stop.  That avoids the global terminal collision
already identified in M68.  The audit therefore isolates the possibilities
requested in the mission:

- a chosen certificate causes neither exponential word-family growth nor
  actual-edge collision;
- the construction fails precisely when no chosen direct certificate is
  available;
- reaching a certificate by an arbitrary state-dependent Classification-H
  path has polynomial length, but its aggregate actual-edge congestion is
  still unproved.

### 2.4 Exact refutation of one-Hurwitz certificate domination

Order the transpositions of labels `0,...,4` lexicographically and consider

```text
(01),(02),(03),(24),(02),(14),(24),(34),(02),(24). (2.15)
```

The compact verifier checks directly that (2.15) is a connected identity
word of length ten and genus one.  Add isolated ambient label 5.  The result
is a two-component state at the required minimal ambient parameters
`N=6,m=10`.

The exhaustive finite checks are:

- among all `binom(10,2)=45` deletions, only zero-based pairs `(0,5)` and
  `(2,7)` preserve the identity, and both residual supports are disconnected;
- none of all `2(m-1)=18` signed adjacent Hurwitz moves yields a connected
  identity-preserving deletion pair; these moves have 15 distinct endpoints;
- among the 324 signed two-step paths, 104 reach a connected certificate.

The exact distance to the connected-certificate set is therefore two.  This
rigorously refutes the universal family

```text
{identity or one signed Hurwitz generator}
  followed by {one direct position-pair bubble}.    (2.16)
```

The failure in (2.16) is certificate nonexistence at radius one.  It is not
an exponential family-size problem and not a collision after the certificate
is selected.

### 2.5 The infinite M68 `w_q` boundary test

For M68's disjoint family

```text
w_q=R_q R_q R_(q-1) R_(q-1),  R_a=e_1...e_a,
```

M68 proves that for `q>=7` no literal `K`-neighbor has any adjacent square.
This decisively rules out extrapolating the `N=5` one-Hurwitz miracle to a
universal constant-radius claim.

It does not refute the present direct-certificate route.  Every
positive-genus two-label component `e_i`, `i<q`, has four occurrences;
deleting any two leaves the connected identity component `e_i^2`.  A fixed
position-pair bubble exposes the certificate in `O(q)=O(m)` Hurwitz moves,
with `O(m^2)` word choices and exact inverse-prefix recovery.  Thus the
correct target permits polynomial path length while requiring polynomial
congestion; constant literal radius is already false.

### 2.6 The surviving positive-permutation-braid law

For every `pi in S_m`, fix the canonical bubble-sort reduced positive braid
word `beta_pi`.  Uniform `pi` is state independent, is sampled and executed
in polynomial time, and satisfies

```text
max ell(beta_pi)=binom(m,2),
E ell(beta_pi)=m(m-1)/4.                            (2.17)
```

The factorial support `m!` is harmless in Theorem 2.1.  If its marked
**endpoint** probability is at least `eta` for every source, the endpoint
variant and (2.17) give the explicit bound

```text
B_(Gamma,F_N minus A)(S)
 >=2 eta |S|/[3(m-2)M^2 m(m-1)].                   (2.18)
```

There is an exact double count, but it is only an average theorem.  Make a
bipartite multigraph with one edge

```text
x -> beta_pi x
```

for each source and each `pi`.  Every row has degree `m!`.  For each fixed
`pi`, `beta_pi` is a bijection, so every target has one preimage; hence every
column also has degree exactly `m!`.  Parallel/stabilizer multiplicities are
included.  Consequently

```text
sum_(x in Gamma)#{pi:beta_pi x in G_Gamma}
   =m! |G_Gamma|.                                   (2.19)
```

This recovers (2.8) after averaging over `x`, but gives no minimum row sum.
The exact connected `S_3`, length-six incidence table already disproves row
constancy: marked row counts range from 608 to 720 out of 720 and assume nine
different values.  Individual rows have only 15--119 distinct endpoints,
and maximal parallel multiplicity is 12, 16, 24, or 48, while every column
still has indegree 720.  Stabilizers therefore preserve (2.19) but do not
flatten its rows.

Neither inversion nor Garside complementation repairs this.  The inverse of
a positive simple braid is not generally in the same positive family.  If
the left complement satisfies `beta^L beta=Delta`, then
`beta x in G_Gamma` is equivalent to
`Delta x in beta^L G_Gamma`; the marked set moves.  It is not invariant
under all braid actions—unmarked words and marked
words occur in the same Hurwitz orbit.  Thus complementation permutes the
total incidence behind (2.19), not the fixed-set row sums.  An asymptotic
zero-hit row under every simple positive braid is not found here, but it is
also not excluded by any average argument.

### 2.7 Why three or more components remain separate

For `c>=3`, M68/M74's marked refresh merges two components and stays in the
exterior with `c-1` components.  It can therefore remain inside `E_k`; it is
not a first-boundary edge.  Applying a success probability separately at up
to `N` merger levels and multiplying the losses is not polynomially valid.
Likewise, routing every source to a common minimal macro recreates M68's
superpolynomial terminal-preimage collision.

The two-component theorem and a multilevel theorem are consequently distinct:
the former needs a row-wise marked cover, while the latter additionally needs
additive control of actual-edge occupation across component mergers.

## 3. Probability, runtime, path, and congestion accounting

All factors used in the proof are displayed here.

| item | exact bound | role |
|---|---:|---|
| laziness/nonlazy `r=3` weight | `1/6` | already includes the `1/2 I` split |
| valid `H3` window count | `m-2` | uniform scan |
| arbitrary length-three same-product fiber | `<=M^2` | first two outputs force the third |
| used padded Hurwitz edge | `p_H=1/[6(m-2)M^2]` | path capacity |
| transposition-product fiber | `D_N=(3N^2+N-12)/2` | exact marked refresh normalization |
| specified safe refresh | `1/[6(m-2)D_N]>=p_H` | terminal capacity |
| inherited whole-macro mark mass | `>=3/[Nm(m-1)]` | average only |
| inherited whole-macro action | `theta_N=1/[2Nm(m-1)(m-2)D_N]` | average only |
| direct-certificate bubble family | `<=binom(m,2)` | state-independent choices |
| bubble length | `<=m-2` | positive Hurwitz words |
| full internal cell canonicalization | `<=m-1` | not used as coarea terminal |
| direct-cell source count over fixed core | `<=binom(m,2)M` | exact certificate audit |
| randomized prefix cover load | `<=Dbar+1` | no support-cardinality factor |
| randomized endpoint cover load | `<=max(Dbar,1)` | no first-hit-time factor |
| positive-braid expected/max length | `m(m-1)/4`, `binom(m,2)` | polynomial execution |

The positive-permutation-braid family has `m!` members but can be sampled by
a uniform random permutation and executed in `O(m^2)` elementary operations.
Theorem 2.1 charges it by expectation (2.17), not by enumerating its support.
All exact experiments are deterministic exhaustive calculations with no
random seed and no nonstandard dependency.

## 4. Dependencies and claim status

| input or claim | status here | dependence |
|---|---|---|
| M64 exterior sets, boundary identity, and first-boundary setup | inherited accepted | defines `A,E_k,C_k,F_N` |
| M68 marked incidence and DYZ normalization | inherited, accepted by M74 | gives (2.8) |
| M74 safe two-component refresh | inherited proved with correction | uses prefix join tree `T_J`; gives (2.6), (2.10) |
| exact same-product heat-bath reversibility | project proved input | declares the global uniform target; no new stationarity claim |
| randomized first-crossing Theorem 2.1 | proved here | elementary bijectivity and edge charging only |
| M60 positive-genus null-pushing after a certificate | proved here | direct product identity (2.12) |
| one-Hurwitz universal direct-certificate cover | refuted here | exact `N=6,m=10` witness |
| positive-permutation-braid row lower bound | unresolved | first two-component lemma below |
| multilevel additive merger occupation | unresolved | separate `c>=3` lemma below |
| quantitative Classification H | not used in Theorem 2.1 | supplies only context/polynomial state-dependent distance; no congestion |
| global polynomial mixing or inverse-polynomial gap | unresolved | not implied |

No new literature theorem is invoked.  In particular, the finite braid
incidence double count uses only that each fixed Hurwitz word is a bijection.

## 5. First unproved standalone steps

The sharp two-component next lemma is the following endpoint statement.

> **SIMPLE-POSITIVE-BRAID ROW LOWER BOUND.**  There is an absolute constant
> `C` such that for every `N>=5`, `m=2N-2`, every two-component exterior
> Hurwitz macro `Gamma`, and every `x in Gamma`,
>
> ```text
> (1/m!) #{pi in S_m: beta_pi x in G_Gamma}>=(Nm)^(-C).  (5.1)
> ```

Theorem 2.1 would then prove (2.18) with `eta=(Nm)^(-C)` for every arbitrary
partial subset of every two-component macro.  A weaker prefix version of
(5.1) is also sufficient, with denominator `m(m-1)/4+1`, but it is not
directly controlled by the endpoint double count (2.19).

For three or more components, even (5.1) leaves the distinct next lemma:

> **ADDITIVE MERGER OCCUPATION / FIRST-BOUNDARY LEMMA.**  Concatenate
> marked-braid paths and literal safe component-merger refreshes, stopped at
> the first edge leaving `E_k` (and at `F_N minus A` in the two-component
> terminal case), so that every actual directed `K`-edge has only
> `poly(N,m)` total weighted preimage occupation across all component levels.
> The bound must be additive over at most `N-2` mergers, not a product of
> per-level inverse success probabilities and not a coalescence through one
> minimal-macro hub.

These statements keep the whole-macro action (2.8)--(2.10), the arbitrary
partial-macro requirement (5.1), and the multilevel concatenation issue
logically separate.

## 6. Strongest self-attack

1. The exact state (2.15) kills the first universal shallow cover at the
   smallest ambient size found: every radius-one state lacks a connected
   deletion certificate.  A proof based on the `N=5` behavior is false.
2. M68's `w_q` family kills every constant-`K`-radius adjacent-square claim
   for infinitely many sizes.  Any viable cover must tolerate `Omega(m)`
   literal distance.
3. Double regularity cannot replace a row lower bound.  The exact `S_3`
   incidence multigraph is `m!`-regular on both sides yet has nonconstant
   marked row sums and large stabilizer multiplicities.
4. The DYZ/M68 marked density is a uniform-source average.  It is consistent
   with an asymptotic source having zero simple-positive-braid hits; this
   report neither constructs nor rules out such a family.
5. Garside complementation moves `G_Gamma`; it does not produce a hidden
   source-independent equality.
6. The internal `z f f` canonicalization is deliberately not used as a
   global terminal.  M68's cardinality argument shows why polynomial
   terminal metadata can suffer superpolynomial collision under full
   coalescence.
7. All positive small cases are calibrations only.  They do not establish
   (5.1), expansion, conductance, or mixing.

The only rigorous negative conclusion here is the cover refutation in
Section 2.4.  It is not a superpolynomial full-`K` stationary cut.

## 7. Boundary cases and exact calibrations

At minimal ambient length, exhaustive calculations give:

| ambient case | exact result | interpretation |
|---|---:|---|
| `N=3,m=4` | 27 identity words; 3 exterior; 0 direct-certificate failures | finite calibration outside theorem's `N>=5` range |
| `N=4,m=6` | 3936 identity words; 1056 exterior; 0 direct-certificate failures | finite calibration outside theorem's `N>=5` range |
| `N=5,m=8` | 762940 exterior; 240 direct failures; all 240 succeed under every one of 14 signed generators | exact finite miracle, refuted at `N=6` |
| `N=6,m=10` | witness (2.15) has exact certificate distance 2 | universal radius-one cover refuted |

Positive-permutation-braid endpoint calibrations are:

- all 240 connected genus-one `S_3` length-six words (equivalently embed an
  isolated ambient label): minimum `608/720`;
- all 20 displayed frozen `N=5,m=8` hard witnesses: minimum
  `25768/40320`;
- the `N=6,m=10` radius-one witness: exactly
  `1603960/3628800=40099/90720`, approximately `0.442008`.

The last value shows that the radius-one obstruction is not a finite
counterexample to the positive-braid row lemma.

If `m` is odd, `Omega(N,m)` is empty by sign.  The cases `m=0` and `m=2`
do not contain the positive-genus minimal exterior geometry used here.  At
`N=2,m=2`, the sole transposition square is connected and minimal.  The
case `S_4,m=4` is not on the relation `m=2N-2`, so no M75 theorem is asserted
there.  These exceptions do not alter (1.1)--(5.1).

## 8. Artifacts and reproduction

All artifacts are in this mission directory.  Exact hashes are in
`freeze_manifest.md`.  Python was 3.12.3; every run records the commit,
arguments, convention, elapsed time, null seed, and empty nonstandard
dependency map.

```text
python3 small_direct_cover_calibration.py --output small-direct-cover-N3-N4.json
python3 one_hurwitz_direct_cover_audit.py --output one-hurwitz-direct-N5.json
python3 direct_free_component_search.py --N 5 --max-states 200000 \
  --stop-on-counterexample --output direct-free-component-N5.json
python3 verify_radius_one_counterexample.py --output radius-one-counterexample-N6.json
python3 positive_permutation_braid_audit.py --output positive-permutation-braid-S3.json
python3 positive_braid_hard_witness_audit.py --output positive-braid-hard-N5.json
python3 positive_braid_counterexample_calibration.py --output positive-braid-counterexample-N6.json
python3 simple_braid_incidence_audit.py --output simple-braid-incidence-S3.json
```

The `direct_free_component_search.py` run was exploratory and stopped after
finding the witness; its JSON correctly says `component_exhausted=false` and
`search_exhausted_without_state_limit=false`.  The compact
`verify_radius_one_counterexample.py` is the definitive exhaustive verifier
for the displayed witness.  The other outputs state their own finite scope
warnings.  No predecessor/frozen directory was edited.

## 9. Verdict

**OPEN AT TWO NAMED STEPS: SIMPLE-POSITIVE-BRAID ROW LOWER BOUND FOR TWO
COMPONENTS, AND ADDITIVE MERGER OCCUPATION FOR THREE OR MORE COMPONENTS.**

Within that nonterminal verdict, Theorem 2.1 and the post-certificate M60
canonicalization are proved, and the universal one-Hurwitz direct-certificate
cover is refuted exactly.  The surviving two-component route is now a single
state-independent row-incidence lemma with explicit normalization (2.18),
not an unspecified canonical-path conjecture.
