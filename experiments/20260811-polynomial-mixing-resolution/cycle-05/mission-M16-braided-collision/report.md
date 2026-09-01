# M16 final report: braided binary collisions

Date: 2026-08-11  
Owned directory: `experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/`

## 1. Exact claim, quantifiers, and conventions

Throughout, `(pq)(x)=p(q(x))`.  Let `N>=3`, `G=A_N`,
`T=T_N`, `M=binom(N,2)`, `E=T^2`, and `p(s,t)=st`.  Conjugation notation is
`A^g=g^(-1)Ag`, componentwise on the two transpositions in `A`.  For
`l>=2` and feasible `h in G`, let `mu_(l,h)` be uniform on

```text
Omega^E_(l,h)={A in E^l: p(A_1)...p(A_l)=h}.
```

This is exactly the original transposition bridge after grouping positions
`(1,2),(3,4),...`; hence original length is `m=2l`.

For `i<j`, define `P_(i,j)` to be conditional expectation under `mu_(l,h)`
given every **raw micro coordinate** except `i,j`.  If
`W=p(A_(i+1))...p(A_(j-1))`, it samples `(X,Y)` uniformly from

```text
{(X,Y) in E^2: p(X) W p(Y)=p(A_i) W p(A_j)}.       (1)
```

The audited direct-transfer claim was that these natural complete-pair
projections obey a braid-covariant version of Caputo's binary-collision
algebra, including nonnegative disjoint-pair cross terms and the uniform
three-site threshold needed by his recursion, and that the complete dynamics
can be compared polynomially to adjacent aligned `H_4` updates.

The conjunction is **refuted**: crossing projections have a negative cross
term, and an exact `N=6` endpoint has three-site gap below `1/3`.  A separate
part survives: the complete-to-adjacent comparison has loss at most `2l^2`
in random-scan gap normalization.  A different leave-one-out recursion also
survives, but leaves a named coordinate-correlation estimate open.  None of
these route results is Terminal B.

## 2. Full argument and construction

### 2.1 The exact pair conditional expectation

Fixing the complement of `{i,j}` fixes `W` and the right side of (1).  The
current pair belongs to this finite fiber.  Uniform resampling on the fiber
is therefore the conditional expectation `P_(i,j)`.  In particular it is a
self-adjoint orthogonal projection, preserves `mu_(l,h)`, and preserves the
ordered endpoint.

On the group-increment quotient, put

```text
a_N(g)=#{(s,t) in T^2: st=g}.
```

Then

```text
a_N(e)=M,
a_N(g)=3  for a 3-cycle,
a_N(g)=2  for a product of two disjoint transpositions,
a_N(g)=0  otherwise.                                      (2)
```

Thus a group word has stationary weight `prod_k a_N(g_k)`.  Formula (1),
with weights (2), is exactly the quotient of the uniform micro conditional;
no multiplicity has been discarded.

An exact sampler is polynomial.  One may enumerate the `M^2` possible
micro labels `X`, compute the forced group product of `Y`, weight `X` by the
number of micro lifts of that product, then sample a lift of `Y`.  Even a
naive nested implementation costs at most `O(M^4)=O(N^8)` elementary
permutation operations; the class formula (2) reduces this to `O(M^2)`
candidate work.

### 2.2 Micro Hurwitz covariance, including the orientation

Define

```text
R(A,B)=(B,A^(p(B))).                                      (3)
```

If `a=p(A)` and `b=p(B)`, then the product after (3) is
`b(b^(-1)ab)=ab`.  Its inverse is

```text
R^(-1)(C,D)=(D^(p(C)^(-1)),C).
```

Conjugation permutes transpositions, so `R` is a measure-preserving bijection
of `E^2`.  Direct substitution proves the braid relation
`R_1R_2R_1=R_2R_1R_2`; the harness checks all `36^3` micro triples for
`N=4` as a falsification test.

For `i<j`, apply `R_i,R_(i+1),...,R_(j-2)`.  This moves the **earlier**
micro coordinate to site `j-1`; its group product becomes
`W^(-1)p(A_i)W`.  The adjacent constraint at sites `j-1,j` is therefore

```text
W^(-1)p(A_i)W p(A_j),
```

which is fixed exactly when `p(A_i)W p(A_j)` is fixed.  Applying the
adjacent heat bath and undoing the braid is consequently exactly `P_(i,j)`.
The exhaustive `N=4,l=3` check confirms equality of these kernels.

Orientation matters.  Moving the later strand left with the opposite
positive-braid shuttle gives another product-preserving kernel, not (1).  In
the recorded `N=4` witness its transition probability is zero while the
earlier-right/raw conditional probability is `1/18`.

### 2.3 Which disjoint projections commute

Separated chords `i<j<k<l` commute: after the complement is fixed, their two
conditional fibers are independent.  Nested chords `i<k<l<j` also commute.
The inner update preserves the full inner segment product and therefore the
middle product seen by the outer update; the outer update fixes all data seen
by the inner update.  Their fiber sizes and transition probabilities remain
unchanged in either order.  Hence every disjoint **laminar** pair commutes.

Crossing chords need not commute.  The smallest recorded positive-support
witness has `N=4,l=4`, endpoint identity, chords

```text
a={1,3}, b={2,4},
x=(e,e,e,e),
y=((2 3 4),(1 2)(3 4),(2 4 3),(1 3)(2 4)).              (4)
```

Chronologically applying `P_a` and then `P_b` gives probability `1/400` of
`x -> y`; applying `P_b` and then `P_a` gives zero.  Indeed, from `x`, the
first update chooses `(g,g^(-1))` with `g=(2 3 4)`.  The second chooses
`q=(1 2)(3 4)` and its forced conjugate.  Reversing the updates would require
`gqg^(-1)=q`, which is false.

The harness also gives the exact Caputo-sign witness.  With
`D_a=P_a-I`, `D_b=P_b-I`, it constructs a rational function `f` such that

```text
<D_a f,D_b f> = -194643/759200000 < 0.                  (5)
```

Specifically, for `A=I-P_a`, `B=I-P_b`, seed delta `d=1_x`, put
`u=Ad`, `v=P_aBu`,

```text
alpha=<u,Bu>=1323/292000,
beta=||v||^2=194643/759200000,
t=(alpha+beta)/beta=134609/7209,
f=u-tv.
```

Since `Av=0` and `<u,Bv>=||v||^2`, (5) equals `-beta`.  This directly
refutes the nonnegative disjoint cross term used in Caputo's equation (1.11).

### 2.4 Embedding the crossing witness as N grows

Witness (4) embeds by fixing labels `5,...,N`.  Set

```text
D_N=(3N^2+N-12)/2,
Z_N=sum_g a_N(g)^2
   =M^2+18 binom(N,3)+12 binom(N,4)
   =M D_N.                                               (6)
```

The two chronological transition probabilities in (4) become exactly

```text
36/Z_N^2  and  0.                                      (7)
```

In the stationary group quotient, the unnormalized weights of `x` and `y`
are `M^4` and `36`.  Therefore the corresponding entry after the `L^2`
stationary symmetrization of the commutator is

```text
sqrt(M^4/36) * 36/Z_N^2 = 6/D_N^2.                     (8)
```

Consequently

```text
||[P_a,P_b]|| >= 6/D_N^2 >= 3/(2N^4).                  (9)
```

This explicitly embedded matrix coefficient is polynomially diluted, of
order `N^-4`; it is not bounded away from zero.  Equation (9) is only a lower
bound on the whole commutator norm, so it does **not** rule out a different
constant-size mode.  The universal upper bound for two orthogonal
projections is `||[P,Q]||<=1/2`; no useful decaying upper bound was proved.

The same witness forces polynomial normalized negativity.  In a principal
two-projection block write

```text
P=[[1,0],[0,0]], Q=[[c^2,cs],[cs,s^2]], c^2+s^2=1.
```

Its commutator norm is `cs`.  For the vector `(2c/s,1)`, with
`A=I-P`, `B=I-Q`,

```text
<Af,Bf>=-c^2,
||Af||^2+||Bf||^2=1+c^2.
```

Using (9), some negative cross term therefore has normalized magnitude at
least

```text
c^2/(1+c^2) >= 18/D_N^4 = Theta(N^-8).                 (10)
```

This again certifies polynomial dilution, not a constant asymptotic limit.

For completeness, a perturbative Caputo statement can be written exactly.
Suppose every disjoint pair of chords obeyed

```text
<D_bf,D_cf> >= -(eta/2)(||D_bf||^2+||D_cf||^2).        (11)
```

If `lambda_3` is the worst conditional three-site gap in Caputo's
`(1/3) sum(I-P_b)` normalization, his triangle count with (11) would give

```text
gap((1/l)sum_b(I-P_b))
 >= {((3lambda_3-1)(l-2)+1)-eta binom(l-2,2)}/l.       (12)
```

The trivial Cauchy bound gives only `eta=1`; (10) shows any universal `eta`
must be at least `36/D_N^4`.  More importantly, the next subsection proves
that the required worst `lambda_3>1/3` is itself false, so even `eta=0` does
not make (12) useful in this model.

### 2.5 Exact refutation of the uniform three-site threshold

Let

```text
T_3=(P_12+P_13+P_23)/3.
```

At `N=6` take `h=(3 4)(5 6)`.  The group-product quotient has 2,020 states
and total micro mass 39,382.  The artifact
`exact_three_gap_witness.json` contains an integer coefficient vector in a
fully specified deterministic state order.  Exact integer and rational
conditional-class sums give mean zero and the gap Rayleigh quotient

```text
q = 11308644378456917647 / 39796565095659282750
  = 0.28416131772363395... .                            (13)
```

Since

```text
39796565095659282750 - 3*11308644378456917647
  = 5870631960288529809 > 0,
```

equation (13) is rigorously below `1/3`.  The function depends only on the
three group products and therefore lifts verbatim to the uniform micro
bridge, with the quotient weights (2).  Hence

```text
gap(T_3 at N=6,h=(3 4)(5 6)) <= q < 1/3.               (14)
```

This is an exact finite refutation of the Caputo threshold, not a floating
point inference.

For context, the deterministic eigensolver audited one representative of
every `S_N` conjugacy type in `A_N`.  Conjugation by any element of `S_N`
intertwines the micro chain, so this includes split `A_N` classes.  The
smallest numerical gaps were:

| N | worst endpoint type | quotient/full micro gap |
|---|---|---:|
| 3 | `(1,1,1)` or `(3)` | `0.6666666667` |
| 4 | `(1,1,1,1)` | `0.5606837607` |
| 5 | `(3,1,1)` | `0.4350812860` |
| 6 | `(2,2,1,1)` | `0.2841613177` |

Only (13)--(14) are used as a rigorous universal-claim falsifier; the rest
of the table is finite numerical diagnosis.

The table is genuinely microfactorized.  Conditional on the group word, the
micro labels are independent and uniform in their lift fibers.  Let `C_k`
average the internal lift label at coordinate `k` while fixing all group
increments and other lift labels.  The commuting `C_k` give an orthogonal
ANOVA decomposition indexed by `S subset {1,2,3}`.  If a pair projection
touches `S`, it annihilates that summand; if it is disjoint, it preserves it.
For nonempty `S`, at most one of the three pair projections survives, so
`||T_3||<=1/3` there and its gap is at least `2/3`.  The remaining summand is
exactly the weighted group quotient.  Thus whenever the quotient gap is at
most `2/3`, it equals the full micro gap.

### 2.6 A polynomial complete-to-adjacent comparison survives

Use the following explicit normalizations:

```text
T_l = [1/binom(l,2)] sum_(i<j) P_(i,j),                 (15)
C_l = (1/l) sum_(i<j)(I-P_(i,j))
    = (l-1)/2 (I-T_l),                                 (16)
H_l = sum_(k=1)^(l-1)(I-P_(k,k+1)),                    (17)
B_l = [1/(l-1)] sum_(k=1)^(l-1)P_(k,k+1).              (18)
```

Thus `T_l` has `binom(l,2)` chords each of coefficient
`1/binom(l,2)`; `C_l` has each collision projector with coefficient `1/l`;
and the aligned nonlazy `H_4` scan `B_l` has `l-1` adjacent chords each of
coefficient `1/(l-1)`.

Let `e_k=||(I-P_(k,k+1))f||_2^2`.  Since the adjacent Hurwitz map `R_k`
permutes each same-product fiber,

```text
||(U_(R_k)-I)f||_2^2 <= 4 e_k,                         (19)
```

and the same holds for `R_k^(-1)`.  To realize `P_(i,j)`, move site `i`
right through `d-1=j-i-1` Hurwitz swaps, apply the adjacent projection at
`j-1,j`, and undo.  A telescoping sum along this state path, followed by
change of variables under each measure-preserving prefix, gives

```text
||(I-P_(i,j))f||_2^2
 <= 2e_(j-1)+8(d-1)sum_(k=i)^(j-2)e_k
 <= 8d sum_(k=i)^(j-1)e_k.                             (20)
```

For edge `k`, the exact aggregate distance is

```text
sum_(i<=k<j)(j-i)=l k(l-k)/2.
```

Summing (20) and using `4k(l-k)<=l^2` yields

```text
E_(C_l)(f,f) <= l^2 E_(H_l)(f,f).                      (21)
```

Combining (16)--(18) and (21) gives the clean random-scan comparison

```text
gap(B_l) >= gap(T_l)/(2l^2).                           (22)
```

There is no canonical normal-form hub and no hidden exponential congestion;
the path length is at most `l-2`, and all capacity accounting is the exact
Dirichlet calculation above.

For original `m=2l`, `K_(N,m)` assigns each aligned length-four window
coefficient `1/[2|R_m|(m-3)]`.  Therefore

```text
E_K >= [(l-1)/(2|R_m|(2l-3))] E_B >= (1/12)E_B,        (23)
```

including `m=4`, where `|R_m|=2` and the actual factor is `1/4`.  Thus a
polynomial gap for `T_l` would transfer to `K` with all scan and laziness
normalizations accounted for.

### 2.7 A Carlen--Geronimo--Loss leave-one-out recurrence also survives

The noncommutation above does not obstruct the different recursion of
Carlen--Geronimo--Loss (CGL), Lemma 3.1 and equations (3.4)--(3.8).  Define

```text
T_l^(-k)=[1/binom(l-1,2)] sum_(i<j; i,j!=k)P_(i,j).
```

Every chord occurs in exactly `l-2` leave-one-out sums, so

```text
T_l=(1/l)sum_k T_l^(-k).                               (24)
```

Fix the full micro coordinate `A_k` and put `g=p(A_k)`.  Delete that site,
leave earlier micro coordinates unchanged, and conjugate every later
transposition by `x -> g x g^(-1)`.  The reduced product is

```text
p(A_1)...p(A_(k-1)) g[p(A_(k+1))...p(A_l)]g^(-1)
 = h g^(-1).                                           (25)
```

Conjugation preserves the uniform micro alphabet.  If a chord lies before
or after `k`, its conditional constraint is unchanged or globally
conjugated.  If it straddles `k`, its reduced segment product is exactly its
old segment product followed by `g^(-1)`.  Hence this bijection intertwines
**every** `P_(i,j)` avoiding `k` with the natural complete-pair projection on
the `(l-1)`-bridge of endpoint `h g^(-1)`.

Let `gamma_l(h)=gap(I-T_l)` and let

```text
R_l=(1/l)sum_k P_k,   P_k=E[ . | A_k],
mu_l(h)=sup_(f perp 1) <f,R_l f>/||f||^2.              (26)
```

Condition on `A_k`, apply the worst `(l-1)`-bridge gap to
`f-P_kf`, and average (24).  This proves

```text
gamma_l(h)
 >= [min_(feasible u) gamma_(l-1)(u)] [1-mu_l(h)].     (27)
```

Equivalently, for the gaps `Delta_l=gap(C_l)=(l-1)gamma_l/2`,

```text
min_h Delta_l(h)
 >= [(l-1)/(l-2)] [1-max_h mu_l(h)] min_u Delta_(l-1)(u), l>=3.  (28)
```

CGL's Lemma 5.1 does not finish (27).  It uses exchangeability to replace all
coordinate correlations by one self-adjoint operator and diagonalizes the
symmetric and antisymmetric coordinate sectors.  Here raw endpoint bridges
are not exchangeable.

There is nevertheless an exact nonexchangeable replacement formulation.
Let `I_k` embed a centered function of the marginal `A_k` as a function on
the bridge, and set `A(phi_1,...,phi_l)=sum_k I_k phi_k`.  Then

```text
R_l=(1/l) A A^*,
```

so its nonzero spectrum is that of the block Gram operator

```text
(1/l)A^*A = (1/l)[K_(ij)]_(i,j),
K_(ij)phi=E[phi(A_j)|A_i].                             (29)
```

Unlike the exchangeable CGL model, `K_(ij)` is not self-adjoint in general.
However, centrality of the increment law gives considerably more structure
than a generic nonexchangeable block matrix.  Write `q` for the group law of
`p(A)`.  In the group algebra, all convolution powers of `q` are central and
therefore commute past the two fixed increments.  Consequently, for every
`i<j`, the ordered pair marginal is position-independent and is proportional
to

```text
nu(A)nu(B) q^(*(l-2))((p(A)p(B))^(-1)h).               (30)
```

Let `K=K_(ij)` for any `i<j`, define
`theta(A)=h^(-1)Ah` componentwise, and let `Uf=f o theta`.  Formula (30)
implies both simultaneous `theta`-invariance and the cyclic identity

```text
(A_i,A_j) =_law (A_j,theta(A_i)).
```

Hence, with the operator convention in (29),

```text
K=K^*U,  KU=UK,  K^*=U^(-1)K.                         (31)
```

In particular `K` is normal.  Equation (29) is therefore exactly the block
matrix with `I` on the diagonal, one common `K` above the diagonal, and
`K^*` below.  If `K phi=kappa phi`, its restriction to the corresponding
coordinate copies is the scalar Hermitian matrix

```text
G_l(kappa)=(1/l) [ 1 on the diagonal,
                    kappa above it,
                    conjugate(kappa) below it ].       (32)
```

Thus the nonzero spectrum of `R_l` is the union of the spectra of (32) over
`kappa in spec(K)`.  Moreover, any one-coordinate function whose mean is zero
inside each micro product fiber `p^(-1)(g)` lies in `ker K`, because (30)
depends on a micro label only through its product.  Such modes give only the
eigenvalue `1/l`.  The nontrivial part of `K` consequently acts on

```text
supp(q)={e, 3-cycles, double transpositions},
|supp(q)|=1+2 binom(N,3)+3 binom(N,4)=O(N^4).           (33)
```

This confirms the coordinator's proposed normal-operator reduction and
corrects the generic-block concern: the blocks commute after all.  What is
still missing is an endpoint-uniform spectral bound on the exact
`O(N^4)`-dimensional correlation operator `K` and the scalar matrices (32).
For the product in (28) to lose only a polynomial, a sufficient useful form
is `max_h mu_l(h)<=A/l` above a universal base length; a generic bound merely
separating `mu_l` from one would compound exponentially.

For the exact threshold endpoint `N=6,l=3,h=(3 4)(5 6)`, note that
`R_3=T_3`.  The 258-dimensional Gram audit gives

```text
mu_3(h)=0.7158386822764471...                           (numerical),
1-mu_3(h)=0.2841613177235529... .
```

The exact Rayleigh certificate (13) rigorously gives the corresponding lower
bound on `mu_3`, but a global exact algebraic ordering of all 258 Gram modes
was not completed.  In the numerically leading endpoint-centralizer
character, `kappa=0.5737580234146701...` is exactly the largest real root of

```text
205875000 kappa^4 -113397500 kappa^3 -3948169 kappa^2
  +683815 kappa +14940=0,                              (34)
```

and the associated candidate is `mu_3=(1+2kappa)/3`, equivalently a root of

```text
4168968750 mu^4 -7089491250 mu^3 +4274645229 mu^2
  -1100121846 mu +102911461=0.                         (35)
```

The sector reduction and polynomials (34)--(35) are exact; the assertion that
this sector is globally top remains a deterministic numerical finding.  No
exact-top claim is needed for the rigorous `<1/3` refutation (14).

Primary sources:

- P. Caputo, *On the spectral gap of the Kac walk and other binary collision
  processes*, Theorem 2.1 and equations (1.7)--(1.15),
  [arXiv:0807.3415](https://arxiv.org/abs/0807.3415).
- M. Sasada, *On the spectral gap of the Kac walk and other binary collision
  processes on a lattice*, Lemmas 1.1--1.2 and Theorem 2.1,
  [arXiv:1308.5096](https://arxiv.org/abs/1308.5096).
- E. Carlen, J. Geronimo, and M. Loss, *Determination of the spectral gap for
  Kac's master equation and related stochastic evolutions*, Lemma 3.1,
  equations (3.4)--(3.8), and Lemma 5.1,
  [arXiv:0705.3729](https://arxiv.org/abs/0705.3729).

## 3. Probability, runtime, path length, and congestion accounting

- The exact crossing transition is `36/(M D_N)^2` in one order and zero in
  the other; its stationary-symmetrized coefficient is `6/D_N^2`.
- A raw nonadjacent pair conditional has an exact sampler in at most
  `O(M^4)=O(N^8)` naive time and `O(M^2)=O(N^4)` candidate time using (2).
- A pair at distance `d` uses `d-1<=l-2` forward Hurwitz swaps and the same
  number to undo.  The comparison is a Dirichlet telescoping argument; (20)
  and the exact sum below it contain all path/capacity multiplicities.
- `T_l` uses `binom(l,2)` projections of coefficient `1/binom(l,2)`;
  `C_l` coefficient `1/l`; `B_l` uses `l-1` projections of coefficient
  `1/(l-1)`; the original lazy `K` comparison is (23).
- All calculations are deterministic; no random seed is applicable.

## 4. Dependencies

- **Proved here:** formulas (1)--(12), exact pair normalization, micro Hurwitz
  covariance, laminar commutation, the crossing witness, the asymptotic
  embedded coefficient, the exact rational three-site Rayleigh certificate,
  the internal-label decomposition, comparison (22), leave-one-out gauge
  equivalence, recurrence (27), block-Gram identity (29), central pair law
  (30), normality (31), scalar reduction (32), and fiber-zero reduction (33).
- **Cited and hypothesis-audited:** Caputo Theorem 2.1/equation (1.11), Sasada
  Lemmas 1.1--1.2/Theorem 2.1, and CGL Lemmas 3.1 and 5.1.
- **Empirical finite diagnostic:** the all-endpoint gap table aside from the
  exact inequality (14).  It can falsify proposed universal inequalities but
  cannot prove asymptotics.
- **Inherited proved:** aligned adjacent two-micro heat baths are original
  `H_4` updates; the coefficient comparison from aligned `H_4` to `K`; and
  qualitative arbitrary-endpoint connectivity.  Only the first two enter
  (23); no quantitative gap is imported.
- **Conditional/open:** any inverse-polynomial lower bound for `gap(T_l)` or
  the block correlation estimate following (29).

## 5. First unproved standalone proposition

> **BRAIDED COORDINATE-CORRELATION BOUND.**  There are universal constants
> `A<infinity` and `l_0<infinity` such that for every `N>=3`, every
> `l>=l_0`, and every feasible endpoint `h in A_N`, the operator (26) obeys
> `mu_l(h)<=A/l`.  Equivalently, after removing constants and product-fiber
> zero modes, every scalar matrix (32), for every nonconstant eigenvalue of
> the exact group correlation operator `K_(N,l,h)` from (30), has norm at
> most `A/l`.

Together with inverse-polynomial complete-chain gaps at the finitely many
lengths below `l_0`, (27)--(28) would give only polynomial loss in `l`; then
(22)--(23) would transfer it to `K`.  No theorem audited here proves this
proposition for nonexchangeable fixed noncommutative endpoints.

## 6. Strongest self-attack

1. The raw conditional (1) is only one of several product-preserving braided
   kernels.  It is nevertheless the unique one relevant to Caputo because it
   is actual conditional expectation given the raw complement.  The report
   explicitly rejects the opposite orientation rather than conflating them.
2. Equation (9) lower-bounds a commutator; it does not prove the norm decays
   as `N^-4`.  Only the displayed embedded coefficient is known to dilute.
3. The exact `N=6` threshold failure refutes the Caputo route, not polynomial
   mixing and not Terminal B.  Its gap is still positive.
4. Comparison (22) is useful only after `T_l` has a polynomial gap.  It does
   not estimate that gap.
5. The CGL recursion can be exponentially lossy.  A bound
   `1-mu_l>=poly(N,l)^(-1)` is not sufficient; one needs a summable/O(`1/l`)
   control of `mu_l` or a different multiscale use.
6. The block-Gram proposition may fail for sparse or nearly minimal endpoint
   bridges; it requires a direct asymptotic proof or a cut with mass and flow.

## 7. Calibration results

- Odd original `m`: the transposition identity bridge is empty; grouping is
  not invoked.
- `m=0`: singleton.  `N=2`, even `m`: singleton.  These create no centered
  spectral subspace.
- `m=2` (`l=1`): there is no adjacent pair update; this is the excluded
  disconnected regime.
- `m=4` (`l=2`): `T_2=P_12` and `B_2=P_12` are the whole-word `H_4` heat
  bath.  Formula (22) is valid (loose), and (23) uses the actual `1/4`
  coefficient rather than discarding the global update.
- The grouped micro bijection retains the exact `S_3,m=4` count 27,
  `S_4,m=4` count 120, and `S_4,m=6` count 3,936.  The harness checks the
  `N=4,l=3` quotient with lift multiplicities, rather than counting its 144
  group words uniformly.
- The crossing obstruction first appears at `N=4`; `A_3` is abelian, so no
  false universal conclusion is drawn from `N=3`.
- Arbitrary sparse endpoints and near-minimal bridges are included in (1),
  (22), and (27); no full-support or surplus assumption is used.
- The known failure of arbitrary length-two local simulation is not
  contradicted.  The auxiliary nonadjacent move is simulated by a directed
  sequence of adjacent Hurwitz outcomes and one adjacent heat bath, with an
  explicit Dirichlet loss; it is not asserted to be a single `L=2` update.
- No edge-multiplicity parity, canonical normal-form hub, or stationary-mass
  bottleneck argument is used.

## 8. Artifacts, reproduction, and citations

Artifacts:

- `plan.md`
- `checkpoint.md`
- `braided_collision_audit.py`
- `results.json`
- `three_gap_scaling.py`
- `three_gap_results.json`
- `three_gap_all_endpoints_results.json`
- `exact_three_gap_witness.py`
- `exact_three_gap_witness.json`
- `coordinate_gram_audit.py`
- `coordinate_gram_results.json`
- `exact_coordinate_eigenvalue.py`
- `exact_coordinate_eigenvalue.json`
- `report.md`

Reproduction from repository root:

```bash
python3 -m compileall \
  experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/braided_collision_audit.py \
  experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/three_gap_scaling.py \
  experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/exact_three_gap_witness.py \
  experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/coordinate_gram_audit.py \
  experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/exact_coordinate_eigenvalue.py

python3 experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/braided_collision_audit.py \
  --N 4 --length 4 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/results.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/three_gap_scaling.py \
  --max-N 7 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/three_gap_results.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/three_gap_scaling.py \
  --max-N 6 --all-endpoint-types \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/three_gap_all_endpoints_results.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/exact_three_gap_witness.py \
  --N 6 --endpoint-type 2,2,1,1 --round-scale 1000000 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/exact_three_gap_witness.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/coordinate_gram_audit.py \
  --N 6 --endpoint-type 2,2,1,1 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/coordinate_gram_results.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M16-braided-collision/exact_coordinate_eigenvalue.py
```

Environment: Python 3.12.3, NumPy 1.26.4, SciPy 1.11.4.  All runs are exact
enumerations or deterministic eigensolver diagnostics; there is no random
seed.  The exact certificate is reevaluated with Python integers and
`fractions.Fraction` after the numerical vector is rounded.

Primary citations are linked in Section 2.7.  The exact source obligations
used are Caputo Theorem 2.1/equation (1.11), Sasada Lemmas 1.1--1.2/Theorem
2.1, and CGL Lemma 3.1/equations (3.4)--(3.8)/Lemma 5.1.

## 9. Verdict

**REFUTED.**  The natural raw complete-pair bridge projections do not satisfy
the Caputo disjoint-pair algebra, and the uniform three-site `>1/3` threshold
is exactly false.  The scoped direct braid-Caputo transfer is therefore
refuted.  The polynomial complete-to-adjacent comparison and CGL
leave-one-out recursion survive, but both leave the standalone
**BRAIDED COORDINATE-CORRELATION BOUND** (and a base complete-chain gap) open.
This is a proof-route refutation only, not Terminal B.
