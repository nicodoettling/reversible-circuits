# M68 final report: polynomial whole-macro action, but one-radius exterior expansion remains open

## 1. Exact claim, convention, and scoped outcome

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and a word is evaluated
as the ordered product `t_1...t_m`.  Throughout this report

```text
N>=5,                 m=2N-2,               M=binom(N,2),
Omega=Omega(N,m),     pi=Unif(Omega),        R_m={3,4,5},

K=(1/2)I+(1/6) sum_(r=3)^5
       (1/(m-r+1)) sum_(i=1)^(m-r+1) H_(i,r).       (1.1)
```

Thus every probability below includes the outer laziness, the uniform choice
of block size, the uniform window scan, and the exact same-product
conditional-fiber normalization.  `H4` and `H5` are never removed from the
chain.  Some lower bounds retain only a favorable `H3` contribution and use
nonnegativity of all remaining terms.

Let `F_N` be the connected full-support minimal macro at length `2N-2`, and
let `A subset F_N` be the fixed nonempty proper path-tree cell chosen in the
accepted M63--M64 construction.  Define the literal exterior breadth-first
closure

```text
E_0={y in F_N^c: K(x,y)>0 for some x in A},
E_(k+1)=E_k union {y in F_N^c: K(x,y)>0 for some x in E_k},
L_0=E_0,                L_k=E_k minus E_(k-1),
C_k=A union E_k.                                         (1.2)
```

The assigned target was to prove a universal inverse-polynomial two-sided
conductance bound for every growing intermediate radius
`0<=k<2R_ext`, where

```text
R_ext=50N^2m^3+N+1,                                     (1.3)
```

or to construct an explicit infinite family for which the complete literal
`H3/H4/H5` conductance is superpolynomially small.

Neither alternative is proved.  The exact M64 boundary identity remains

```text
Q_K(C_k,C_k^c)
=W^(-1)[
   sum_(x in C_k)K(x,F_N minus A)
  +sum_(x in L_k)K(x,L_(k+1))
 ],

Phi_pm^K(C_k)
= [the bracket above]/s_k,

W=|Omega|,       s_k=min{|C_k|,W-|C_k|}.             (1.4)
```

Equation (1.4) includes every boundary transition of all three block sizes
and has the correct global smaller-side orientation.

This mission does prove the following scoped results.

1. Every whole exterior labeled weighted support-component macro has a
   uniform inverse-polynomial *average* probability of exposing and using a
   connected genus-lowering square.  For two-component macros this gives
   direct flow to `F_N minus A`; for three or more components it gives a
   component merger while remaining exterior.
2. A polynomial fixed-word marked cover would turn that average statement
   into a genuine M60-style first-crossing bound, with exact path length,
   transition probability, and source recovery.
3. Several natural constructions of such a cover are rigorously refuted:
   direct connected two-deletion, a one-level four-null strand certificate,
   pointwise direct exit, a colors-only marked-Hurwitz handle, and the
   unreduced full connecting-arc lift.
4. A concrete insertion certificate has a polynomial *upper* Radon--Nikodym
   density, but zero-certificate words and pure-braid monodromy prevent the
   proposed pointwise equivariant lift.

These results are auxiliary.  They prove neither a gap upper bound nor a gap
lower bound for the original chain.

## 2. Full argument

### 2.1 Exact marked-incidence identity

Fix one exterior labeled weighted support-component macro `Gamma`.  Count
isolated labels as support components.  If the macro has `c>=2` components,
write every nontrivial component as

```text
(V_j,k_j,g_j),
d_j=|V_j|>=2,
k_j=2(d_j-1)+2g_j.                                  (2.1)
```

Since `sum_j k_j=2N-2` and `sum_j(d_j-1)=N-c`, including the zero-length
isolates, one has the exact genus balance

```text
sum_j g_j=c-1.                                       (2.2)
```

In particular some component has positive genus.  Choose one such component
`U` deterministically, put `d=|U|`, `g=g_U>=1`, and
`k=2(d-1)+2g`.  Let `C_g(d)` be the number of connected identity
transposition words on this fixed labeled `d`-set at length `k`.

A marked internal adjacent square is a position containing `e,e` such that
deleting the two entries leaves a connected word in the genus-`g-1` fiber.
Insertion and deletion give a bijection between

```text
(connected genus-(g-1) word z,
 one of k-1 insertion gaps,
 one of binom(d,2) transpositions e)
```

and a genus-`g` word with one marked deletable adjacent square.  Therefore,
if `Z_int` is the number of such marks in a uniform connected genus-`g`
word,

```text
E[Z_int]
=(k-1)binom(d,2) C_(g-1)(d)/C_g(d).                 (2.3)
```

The accepted positive DYZ recurrence consequence is

```text
[C_g(d)/k!]/[C_(g-1)(d)/(k-2)!] <= d^3/12.          (2.4)
```

Combining (2.3)--(2.4) gives, uniformly in `g`,

```text
E[Z_int]
 >=12 binom(d,2)/(d^3 k)
 =6(d-1)/(d^2 k).                                   (2.5)
```

Conditional on `Gamma`, the component words are independent and uniform and
their colors are uniformly interleaved.  For any fixed consecutive pair of
internal occurrences in a color of multiplicity `k`, the exact probability
that the pair is also consecutive in the global length-`m` word is

```text
binom(m-1,k-1)/binom(m,k)=k/m.                       (2.6)
```

Let `Z` count globally adjacent marked squares supplied by `U`.  Linearity,
not independence, now yields

```text
E_Gamma[Z]>=6(d-1)/(d^2m).                           (2.7)
```

Since `Z<=m-1` and, for `2<=d<=N`,
`(d-1)/d^2>=1/(2N)`,

```text
Pr_Gamma(Z>=1)
 >=E_Gamma[Z]/(m-1)
 >=3/[Nm(m-1)].                                     (2.8)
```

This is a whole-macro statement.  It does not assert that every word has a
mark.

### 2.2 Exact favorable `H3` action

For a transposition `a`, the exact number of length-three transposition words
with ordered product `a` is

```text
D_N=(3N^2+N-12)/2.                                  (2.9)
```

On a word certified by (2.8), select one marked pair `e,e`.  Pad it on the
right unless it is final, in which case pad it on the left.  If `V` is a
different support component and `s` is a cross edge between `U` and `V`, the
specified heat-bath outcome is

```text
(e,e,a) -> (s,s,a),       or       (a,e,e)->(a,s,s).
                                                               (2.10)
```

Both triples have ordered product `a`.  The exact probability of this one
specified outcome is

```text
1/[6(m-2)D_N].                                      (2.11)
```

Deleting `e,e` first leaves `U` connected.  Adding `s,s` merges exactly the
components `U,V`.  The genus of the merged component is

```text
g_U+g_V-1>=0.                                       (2.12)
```

Define

```text
theta_N=1/[2Nm(m-1)(m-2)D_N].                       (2.13)
```

Equations (2.8) and (2.11) imply:

- if `c>=3`, the uniform law on `Gamma` has average `K` probability at least
  `theta_N` of moving to component count `c-1` while remaining in `F_N^c`;
- if `c=2`, (2.2) forces the positive-genus component to have genus one and
  the other component genus zero.  Deleting the marked pair leaves two
  minimal connected components.  There are `d(N-d)>=N-1` cross edges, while
  at most one can produce the one fixed path tree underlying `A`.  Therefore

  ```text
  E_Gamma K(x,F_N minus A)>=(N-2)theta_N.            (2.14)
  ```

The “at most one” assertion is exact: the target support tree is the union
of the two fixed component support trees and the inserted cross edge, and a
fixed tree has at most one edge across a fixed bipartition.

No transition normalization is hidden in (2.13)--(2.14).  They use one
specified `H3` output.  Every `H4/H5` contribution is still in `K` and is
discarded only as a nonnegative term in this lower bound.

### 2.3 What survives for a partial macrofiber

Let `S=E_k` and, for an exterior macro `Gamma`, put

```text
u_Gamma=1-|S intersect Gamma|/|Gamma|.               (2.15)
```

Let `q(x)<=1` be the favorable downward probability from Section 2.2, with
whole-macro mean lower bound

```text
theta_Gamma=theta_N                 if c>=3,
theta_Gamma=(N-2)theta_N            if c=2.          (2.16)
```

Removing a set of uniform macro mass `u_Gamma` can remove at most that much
of the mean, so

```text
(1/|Gamma|)sum_(x in S intersect Gamma)q(x)
 >=theta_Gamma-u_Gamma.                              (2.17)
```

Consequently a macro missing at most `theta_Gamma/2` of its states retains at
least half of its whole-macro action.  For dense two-component macros this is
already exterior boundary flow:

```text
Q_K(C_k,C_k^c)
 >=[(N-2)theta_N/2]
   pi(union of dense two-component macro portions). (2.18)
```

For a sparse partial macro there is a multiradius consequence, but not a
one-radius consequence.  The accepted quantitative Hurwitz classification
gives within-macro diameter

```text
H_N=50Nm^3.                                          (2.19)
```

Every step of that path is a padded positive literal `H3` move and stays in
the macro.  Hence

```text
Gamma intersect E_k nonempty  implies  Gamma subset E_(k+H_N). (2.20)
```

If `u_Gamma>theta_Gamma/2`, then

```text
|Gamma intersect (E_(k+H_N) minus E_k)|
 >=[theta_Gamma/(2-theta_Gamma)]|Gamma intersect E_k|
 >=(theta_N/2)|Gamma intersect E_k|.                 (2.21)
```

This is polynomial `H_N`-window volume growth.  It does not imply a lower
bound on the single boundary term
`sum_(x in L_k)K(x,L_(k+1))` in (1.4).

For dense macros with `c>=3`, stationary inflow gives the useful but
nonclosing absorption relation

```text
(theta_N/2)pi(union of dense c-component portions)
 <=Q_K(C_k,C_k^c)
   +pi(E_k intersect {component count c-1}).         (2.22)
```

Naively iterating (2.22) through up to `N` component levels multiplies the
factor `theta_N`; the resulting loss is superpolynomial.  The needed charge
must be additive and stop at its first exterior boundary.

### 2.4 Exact fixed-word cover theorem and source recovery

The following theorem isolates a sufficient M60-style mechanism.  Fix a
two-component exterior macro `Gamma`, and let `G_Gamma` be the words with a
globally adjacent square in the genus-one component whose deletion leaves
that component connected.

Suppose there are `L>=1` fixed, state-independent Hurwitz words
`beta_1,...,beta_L`, each of length at most `D>=1`, such that

```text
Gamma=union_(j=1)^L beta_j^(-1)G_Gamma.              (2.23)
```

Then every `S subseteq Gamma` satisfies

```text
sum_(x in S)K(x,Omega minus S)
 >= |S|/[6(m-2)M^2LD].                              (2.24)
```

Moreover the target in (2.24) can be restricted to the union of the
within-`Gamma` boundary and `F_N minus A`.

Proof: assign each `x` to the least covering word `beta_j`.  Follow its
prefixes.  If a prefix first leaves `S`, charge that first crossing.  If all
prefixes remain in `S`, the endpoint is marked, so use one safe cross-edge
square refresh from Section 2.2 and charge its edge into `F_N minus A`.

One adjacent Hurwitz generator can be padded to a specified `H3` output.  A
length-three same-product fiber has at most `M^2` words because the first two
transpositions determine the third.  Hence every directed path edge has

```text
K(x,y)>=p_H:=1/[6(m-2)M^2].                          (2.25)
```

For fixed `(j,t)`, the length-`t` prefix of `beta_j` is a bijection of
`Gamma`; thus a charged directed edge recovers at most one source for that
pair.  There are at most `LD` pairs.  A final square-refresh edge has at most
one source for each `j`, hence load at most `L<=LD`.  Dividing the unit demand
of every source by this recovery multiplicity and using (2.25) proves
(2.24).  This is exact path, capacity, and source-recovery accounting; it
does not route through a fixed canonical word.

The unproved issue is the polynomial cover (2.23), not the implication from
such a cover.

### 2.5 Exact failures of proposed deletion covers

#### The initial exterior layer is not macro-saturated

At `N=5,m=8`, exact enumeration finds 90 exterior labeled weighted macros.
`E_0` fully contains 2, partially contains 47, and misses 41.  Its exact
occupancy by component count is

```text
c=2: 308409/739200,
c=3:   6362/23730,
c=4:      0/10.                                      (2.26)
```

Thus the whole-macro mean (2.14) cannot simply be applied to `E_k`.

#### Uniform pointwise direct exit is false

The exact full `H3/H4/H5` audit at `N=5,m=8` finds 90 three-component words
and all 10 four-component words with

```text
K(x,F_5 minus A)=0.                                  (2.27)
```

The all-equal repeated-edge word is the first witness.  There is also an
infinite support-size obstruction.  For `N>=13`, let
`y_N=e^(2N-2)` for one fixed edge `e`.  One update changes at most five
factors, so every one-step target has support on at most twelve labels and

```text
K(y_N,F_N)=0.                                        (2.28)
```

A connected word contains at least `N-1` distinct support edges, so it
agrees with `y_N` in at most `N` positions and has Hamming distance at least
`N-2`.  A local update changes at most five positions.  Hence its exterior
layer radius is at least `ceil((N-2)/5)-1`, with the `-1` accounting for the
definition of `E_0`.  This refutes pointwise exit even at growing radii, but
it gives no cut because the word may have substantial exterior flow.

#### Direct connected two-deletion is false

If positions `i<j` in a component word are written as

```text
P x U y S,
```

deleting `x,y` preserves the ordered identity product exactly when

```text
x=UyU^(-1).                                          (2.29)
```

Right-bubbling `x` through `U` changes it to `U^(-1)xU=y`, producing an
adjacent square.  Therefore a connected identity-preserving two-deletion
pair in every positive-genus word would prove (2.23) with
`L=binom(m,2)` and `D<=m`.

That universal lemma is false already at `N=5,m=8`.  In lexicographic edge
indexing,

```text
[0,1,2,1,0,1,2,1]
=(01)(02)(03)(02)(01)(02)(03)(02)                  (2.30)
```

has one connected genus-one component on `{0,1,2,3}` and isolated label 4.
Of its 28 position pairs, only `(0,4)` and `(2,6)` delete to an identity
word, and both deletion cores are disconnected.  Exhaustively, 240 exterior
words fail the lemma.

#### A one-level four-null strand certificate is also false

The proposed repair was: either a word has a deletable adjacent surplus
square, or deleting one label gives four null prefix-erasure increments and
a connected minimal base.  Among the 657,610 distinct genus-one component
words occurring through ambient `N=5,m=8`, exactly 37,200 fail this
disjunction.  The first is

```text
(01)(12)(01)(12)(01)(12)(13)(13).                   (2.31)
```

Deleting the visible bridge square `(13)^2` disconnects label 3, and no
label supplies four null increments with connected minimal output.  This
refutes the one-level cell partition, not every recursive strand argument.

#### Bounded-radius square exposure has an infinite obstruction

For `q>=7`, put `N=2q`, choose pairwise disjoint edges

```text
e_i=(2i-2,2i-1),        R_a=e_1...e_a,
w_q=R_q R_q R_(q-1) R_(q-1).                        (2.32)
```

Then `w_q` is an identity word of length `4q-2=2N-2`.  It has `q` support
components: the first `q-1` have genus one and the last has genus zero.
Equal copies are initially separated by at least `q-1` positions.

Every window of length at most five initially contains distinct disjoint
transpositions.  Its product has transposition length equal to the window
length, so every factorization in that exact conditional fiber consists of
the same disjoint factors in some order.  Until an equal pair becomes local,
each update therefore only permutes such a reduced window and can decrease
the minimum equal-factor separation by at most four.  Consequently

```text
dist_K(w_q,{words with an adjacent square})
 >=ceil((q-2)/4).                                    (2.33)
```

This rules out a universal constant-radius deletion-cell cover.  The bound
is only linear and carries no stationary-mass estimate, so it is not a
slow-mixing result.

#### A global coalescence hub has unavoidable terminal collisions

The accepted minimal-macro estimate gives, for `N>=6`,

```text
pi(F_N)<=U_6 theta^(N-6),
U_6=114688/234375<1/2,
theta=16 exp(-23/8)<1.                               (2.34)
```

Hence

```text
|F_N^c|/|F_N|
 >=U_6^(-1)theta^(-(N-6))-1
 >2theta^(-(N-6))-1.                                 (2.35)
```

If a deterministic recursive construction sends all exterior words to
`F_N x H_N` and keeps only a polynomial-size terminal history alphabet, one
terminal marked state has at least

```text
[2theta^(-(N-6))-1]/|H_N|                            (2.36)
```

exterior preimages.  Thus terminal source recovery is superpolynomially
bad.  This is why a successful construction must charge the first boundary
edge and stop, rather than erase all merge history at a minimal hub.
Equation (2.36) is a collision obstruction to that routing template, not a
conductance upper bound.

### 2.6 Marked-Hurwitz handles and algebraic insertion certificates

#### Two branch-point colors are insufficient

Transporting two marks as branch-point colors does give a finite surjective
colored orbit.  Each uncolored length-`k` word has between 1 and
`binom(k,2)` unordered colored lifts, so the projected density relative to
the uniform word law lies between `1/binom(k,2)` and `binom(k,2)`.  The two
positions move as two cards under the adjacent interchange chain, with its
polynomial time scale.

But adjacent colored positions need not be an equal canceling pair.  In
`S_3`, index

```text
0=(01),       1=(02),       2=(12),
```

and start from

```text
(1_M,1_M,0,0,2,2).                                  (2.37)
```

Deleting the marks leaves the connected minimal identity word
`(01)^2(12)^2`.  With

```text
R(a,b)=(b,bab),            R^(-1)(a,b)=(aba,a),     (2.38)
```

apply `R_1^(-1)` and then `R_0`, transporting the colors with their branch
points.  The exact result is

```text
(2,0_M,1_M,0,2,2).                                  (2.39)
```

The marks are adjacent but unequal.  Deleting them leaves the nonidentity
3-cycle `[2,0,1]`, while the full six-factor product remains the identity.

#### The unreduced connecting-arc lift has infinite fibers

Retaining the isotopy class of a connecting arc restores the topological
handle, but loses finite multiplicity.  In `S_4`, let

```text
a=(01),       b=(23),       c=(12),
w=a_M a_M b b c c a a.                              (2.40)
```

The word is connected genus one, and deleting the marked `a^2` leaves the
connected minimal word `b^2c^2a^2`.  The second marked `a` and the following
`b` commute.  The pure braid `sigma_2^2` on these two branch points fixes the
entire factor tuple and returns both colors to their original positions.
After the marked strand is forgotten, it also induces the trivial braid on
the deletion word.  On the connecting arc, however, `sigma_2^2` is a Dehn
twist about the two punctures.  Its powers have distinct winding numbers
(equivalently, distinct intersection numbers with a fixed transverse arc).
Thus infinitely many full-arc marks lie above the same factor tuple, colored
positions, and direct deletion data.

The colors-only lift has polynomial fibers but fails actual deletability;
the unreduced full-arc lift preserves deletability but has infinite fibers.
This leaves open a finite handle-framing quotient.

#### Exact direct-certificate density

For a connected genus-`g` word `w`, let `r(w)` be its number of direct
connected deletion certificates `(z,p,e)`: a connected genus-`g-1` word
`z`, insertion gap `p`, and inserted square edge `e`.  The same bijection as
in (2.3) gives

```text
S:=sum_w r(w)=(k-1)binom(d,2)C_(g-1)(d),
mu:=E_pi_g r=S/C_g(d)>=6(d-1)/(d^2k).                (2.41)
```

If `nu` is uniform on the `S` certificates and the mark is forgotten, then

```text
d nu_proj/d pi_g(w)=r(w)/mu.                         (2.42)
```

Since `r(w)<=k-1`,

```text
r(w)/mu
 <=(k-1)d^2k/[6(d-1)]
 <=dk^2/3.                                           (2.43)
```

Thus exact incidence supplies a polynomial upper RN bound.  It supplies no
positive lower bound: (2.30)--(2.31) include words with `r(w)=0`.
Weighting every existing certificate by `1/r(w)` uniformizes only the set
`{r>0}`.

Transporting `(z,p,e)` equivariantly under Hurwitz requires enough braid
history to resolve the winding in (2.40).  Keeping that history gives the
infinite arc fiber; quotienting it all away makes the local transported
action noninjective.  “Canonical re-reduction” has only two interpretations:

1. reselect a direct certificate of the current word, which is undefined at
   `r(w)=0`; or
2. choose a separate insertion representative and canonical braid path,
   whose path can reset globally after one local generator.

Bounding the aggregate loads of the second reset is exactly the missing
multicommodity-flow theorem.  It does not follow from the one-point density
(2.43).  The argument does not rule out every finite quotient; it sharply
refutes the literal full-history and pointwise re-reduction templates.

## 3. Probability, runtime, path length, stationary density, and congestion

The quantitative accounting used above is summarized here.

| object | exact/worst-case accounting | scope |
|---|---:|---|
| specified favorable square refresh | `1/[6(m-2)D_N]` | includes laziness, block scan, window scan, exact `H3` fiber |
| whole-macro marked probability | `>=3/[Nm(m-1)]` | uniform in component genus |
| whole-macro downward action | `theta_N=1/[2Nm(m-1)(m-2)D_N]` | one favorable cross edge |
| two-component direct safe action | `>=(N-2)theta_N` | target in `F_N minus A` |
| arbitrary padded Hurwitz edge | `>=1/[6(m-2)M^2]` | specified `H3` output |
| fixed-word cover path length | `<=D` | hypothesis (2.23) |
| fixed-word cover recovery load | `<=LD` | edge plus `(j,t)` recovers source |
| resulting subset boundary | `>=|S|/[6(m-2)M^2LD]` | theorem (2.24) |
| within-macro diameter | `H_N=50Nm^3` | reachability/window growth only; no congestion |
| direct certificate projected RN density | `0` possible; upper `<=dk^2/3` | exact marked-incidence law |
| disjoint-family square distance | `>=ceil((q-2)/4)` | `N=2q`, only linear |
| deterministic terminal collision | `>[2theta^(-(N-6))-1]/|H_N|` | rules out polynomial terminal metadata |

The exact block samplers have polynomial cost because `r<=5` is fixed; none
of the new arguments introduces a superpolynomial per-step operation.  The
fixed-cover theorem is constructive in time polynomial in `L,D,N,m` if the
cover is supplied.  No such universal cover is claimed.

The deterministic exact calculations used Python 3.12.3, seed `null`, and no
nonstandard dependency.  Their observed runtimes were approximately 8.36 s
(macro saturation), 16.46 s (pointwise exit), 15.64 s (square domination),
18.16 s (two-deletion), 59.78 s (four-null), and negligible time for the
two-generator colored-handle witness.  Runtime observations are not proof
dependencies.

## 4. Dependencies, each labeled

1. **PROVED / ACCEPTED M64, independently ACCEPTED M66:** the definitions
   (1.2), exact full boundary and two-sided orientation (1.4), fixed-radius
   leakage, exterior connectivity, `R_ext`, and exact saturation by radius
   `2R_ext`.  Durable source:
   `cycle-14/mission-M64-multistep-minimal-exterior-closure-redteam/report.md`.
2. **PROVED / INHERITED M60--M63:** the fixed minimal-cell set `A`, its direct
   leakage, and the accepted minimal/full-support cell expansion inputs.
3. **PROVED / INHERITED M18:** the positive normalized DYZ recurrence (2.4).
   This is the only enumerative inequality used in the universal marked-mass
   lower bound.
4. **PROVED / INHERITED Classification H, ledger L-0037:** labeled weighted
   support-component Hurwitz classification, the project/source inverse
   convention translation, and diameter `50Nm^3`.
5. **PROVED / INHERITED:** conditional macrofactorization into independent
   connected component words and a uniform color interleaving; connected
   feasibility `k=2(d-1)+2g`; reversibility and uniform stationarity; exact
   transposition-product `H3` fiber count (2.9).
6. **PROVED / INHERITED M13:** the minimal-macro mass estimate
   (2.34)--(2.35).
7. **PROVED HERE:** the marked-incidence/interleaving estimate
   (2.3)--(2.8), whole-macro action (2.13)--(2.14), dense/partial dichotomy
   (2.17)--(2.22), fixed-cover implication (2.23)--(2.25), disjoint-family
   distance (2.32)--(2.33), terminal collision (2.35)--(2.36), and direct
   certificate RN bound (2.41)--(2.43).
8. **RIGOROUSLY REFUTED HERE AT THE STATED SCOPE:** universal pointwise exit,
   direct connected two-deletion, one-level four-null deletion, colors-only
   handle invariance, finite multiplicity of the unreduced full-arc lift, and
   polynomial source recovery for deterministic global coalescence into only
   polynomial terminal metadata.
9. **EXACT FINITE ONLY:** all `N=5,m=8` counts and the `S_3` colored-handle
   witness.  Positive finite behavior is not used to infer an asymptotic
   theorem.
10. **UNRESOLVED:** a polynomial one-radius boundary or recoverable
    first-crossing flow for arbitrary partial exterior macrofibers, and any
    asymptotic full-chain cut with superpolynomially small conductance.

## 5. First unproved standalone proposition

> **ONE-RADIUS PARTIAL-MACRO MARKED-COVER / COAREA.**  There are universal
> constants `C<infinity` and a polynomial `P(N)<=N^C` such that, for every
> `N>=5` and every `0<=k<2R_ext`, one can assign total demand `s_k` to states
> of `C_k` (for example demand `s_k/|C_k|` per state) and route it by literal
> positive `H3/H4/H5` paths that stop at their first edge out of `C_k`, with
> path length at most `P(N)` and directed-edge load at most
> `P(N)K(x,y)`.  The construction must use short bijective marked covers or
> an equivalent one-radius coarea argument inside partial macrofibers, and
> component mergers must be charged additively rather than multiplying
> `theta_N` through the component depth.

Indeed, every routed path uses exactly one boundary edge.  Summing the load
bound over those edges gives

```text
s_k<=P(N) sum_(x in C_k)K(x,C_k^c),                 (5.1)
```

which, by (1.4), is the required inverse-polynomial two-sided conductance.
The fixed-word theorem proves this proposition on any two-component macro
portion satisfying (2.23).  Equations (2.17)--(2.22) show why only partial
macrofibers and additive recovery across component levels remain.

An equally valid refutation would be an explicit infinite `(N_j,k_j)` family
for which the *complete* bracket in (1.4), including `H3/H4/H5` and the
`F_N minus A` term, is superpolynomially small relative to `s_(k_j)`.  No such
family is obtained here.

## 6. Strongest self-attack

The principal new estimate is an average over a whole macro.  A breadth-first
ball can select precisely the atypical zero-certificate or low-certificate
part of many macros; (2.17) becomes useless when the missing macro fraction
exceeds `theta_N`.  The diameter statement (2.20) spreads this missing mass
over an `H_N`-wide annulus and supplies no control at the particular radius
appearing in (1.4).

The fixed-cover theorem is therefore only a conditional implication.  Its
most appealing direct cover is genuinely false, and the enhanced handle
audit shows that “two marked cards become adjacent” is not synonymous with
“a deletable square becomes adjacent.”  On the other hand, those failures do
not prove that all randomized finite handle quotients have bad load.  The
infinite arc fiber could admit a carefully chosen finite quotient, and the
zero direct-certificate states could be covered by a multilevel construction.

The global collision estimate attacks only paths that erase their histories
at `F_N`.  A first-crossing flow can stop much earlier and need not suffer
that collision.  Likewise, the disjoint family (2.32) proves only linear
distance to a square, with no nonnegligible stationary mass or full boundary
upper bound.  `H4/H5` may bypass any proposed sparse-subchain separator.

Thus none of the negative results is a conductance bottleneck for the literal
chain, and none is Terminal B.

## 7. Calibration and exceptional cases

- The M68 theorem is intentionally restricted to `N>=5,m=2N-2>=8`, the
  regime in which the inherited set `A` and all three block sizes are
  available.  Odd `m`, `m=0`, `m=2`, and `N=2` are outside this scoped cut
  construction; no claim about those cases is inferred.
- At `N=5,m=8`, exact enumeration checks the literal full `H3/H4/H5` graph,
  all 762,940 exterior states, all 90 exterior macros, and every stated
  pointwise zero.  It also finds that all exterior states are within one
  literal move of a marked square state in the same macro.  This positive
  finite fact can falsify a small-case obstruction but cannot prove the
  universal cover.
- The first direct two-deletion failure is (2.30); its only two
  identity-preserving deletion pairs both disconnect the component.
- The repeated-edge family (2.28) calibrates sparse support and shows direct
  connected leakage can vanish for all `N>=13`.
- The disjoint-component family (2.32) calibrates many rare colors and high
  component count at the exact minimal global length.  It rules out bounded
  square exposure without asserting slow mixing.
- Equation (2.14) explicitly treats the delicate two-component case and
  excludes the one cross edge that could land in the fixed tree underlying
  `A`.
- The `S_3` colored-handle counterexample uses a connected genus-one word and
  a connected minimal deletion core, so its failure is not caused by a
  disconnected starting component.
- All lower transition estimates retain the exact `1/2` laziness and the
  `1/3` block-size probability.  For `m=2N-2`, the `H3` window denominator is
  exactly `m-2`.

## 8. Artifacts, hashes, and reproduction

All artifacts are under

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-15/mission-M68-intermediate-exterior-layer-action/
```

They record repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python 3.12.3, seed `null`,
the multiplication convention, and the exact universal claim each finite
calculation could falsify.

Reproduction commands from the repository root are:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact_n5_macro_saturation_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact-n5-macro-saturation.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact_n5_pointwise_exit_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact-n5-pointwise-exit.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact_n5_square_domination_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact-n5-square-domination.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact_n5_two_deletion_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact-n5-two-deletion.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact_n5_four_null_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact-n5-four-null.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/colored_handle_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/colored-handle-audit.json
```

Frozen artifact hashes before adding this report are:

```text
ef66bbd0d0ed8c07bf9ea55ff069a5690110baf28ed48e440765bb0eac673017  checkpoint.md
092f8072e793b29e94698b457bef1dc9bee4c65e339e6cc206da1f1509cffbd9  recovery_obstruction.md
b89d004ec4736884605ef29714ba6c6669e16166015f3b6701cd8e3e2164bb31  enhanced_marked_handle_audit.md
750008849a926cc8a6431602a52b551caec590caf5c40c0c9b0bc438be44ad26  algebraic_insertion_certificate_audit.md
72258e7a54456ddd0fa535b8a9f55052e796e160a1b08a6f9b6d7296ff4a7746  colored_handle_audit.py
aadaf4502aa461c768b07efa413d78ab775b328f0b372692ba4851859d2bac3e  exact_n5_four_null_audit.py
c2d6d9af8653606815239a66feffb0f4476fa5ef8cb0e471c41556bfc83b0ea0  exact_n5_macro_saturation_audit.py
79c1a6dd616c5403398f0bc73c6fbfe81a5ff6c5772db5b7759abc87a6e96adb  exact_n5_pointwise_exit_audit.py
145e52af176d7bfe054c024aa007eba8759f3b68198f526a3b880822198ff5e1  exact_n5_square_domination_audit.py
2de01a8532448f840938088b242baaa88da215640014064ce6385789a4391181  exact_n5_two_deletion_audit.py
5a347357f9a1d63cd98afe623a52b8ac96a6df42f8c51f17bcc45e70917bbae1  colored-handle-audit.json
ca84d1e1454230c17b087c0c0a15a5894a7c0078682fcda06b405c99c93562d5  exact-n5-four-null.json
e9dfb18c5652048e6aa03be8887f341d1a7dd7ddb3abd492500939a3ae3548d1  exact-n5-macro-saturation.json
26c55e00e6f6faf1b796603b46140f57f1252a0fb3183494f37c7baa6e2e16a4  exact-n5-pointwise-exit.json
3a5ae4c2a47ee6e661b19322a35847b00b7c56ce81a706849f0a05e7b7cef52d  exact-n5-square-domination.json
c9ca3536aa8245f23312911e93e544625d535231bec115b155ea644759ca4eb6  exact-n5-two-deletion.json
```

No disposable `/tmp` result is a dependency.

## 9. Verdict

**OPEN AT A NAMED STEP: ONE-RADIUS PARTIAL-MACRO MARKED-COVER / COAREA.**

