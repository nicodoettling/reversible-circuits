# M03 proof bundle: macro audit and dense square-projection reduction

Date: 2026-08-11  
Repository commit audited: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

Throughout, `(pq)(x)=p(q(x))` and a displayed word is evaluated as
`t_1...t_m`.  Put `M=binom(N,2)`.  Gaps are Poincare constants.  The exact
chain under review is

```text
K = (1/2)I
    + (1/(2|R_m|)) sum_{r in R_m} (1/(m-r+1)) sum_i H_{i,r},
R_m={r in {3,4,5}: r<=m}.
```

This bundle proves three things: the frozen M02 formulas are correct; the
exact-support-partition projection of the square chain has a polynomial gap
in the dense regime; and every restriction to one exact support partition is
an explicit zero-range allocation process.  The last process is reduced to
one enumerative rate-curvature proposition, which is not proved here.

## 1. Audit of the frozen M02 bundle

Let `alpha={(B,k_B)}` be labeled weighted support-component data, with
isolated labels implicit, and let `C(v,k)` be the number of connected
length-`k` identity transposition words on a fixed labeled `v`-set.  Direct
color-interleaving counting gives

```text
W_m(alpha)=m! product_{(B,k_B) in alpha} C(|B|,k_B)/k_B!.       (1.1)
```

Thus the macro stationary law is `mu(alpha)=W_m(alpha)/Z_m`.  If
`h_{i,r}(w)` is the ordered product of the selected window,
`F_r(h)` its same-product fiber size, and `N_{i,r}(w,beta)` the number of
outputs having macro datum `beta`, the exact stationary-flow projection is

```text
barK(alpha,beta)
 = (1/2)1{alpha=beta}
   + (1/(2|R_m|)) sum_r (1/(m-r+1)) sum_i
       (1/W_m(alpha)) sum_{w:A(w)=alpha}
         N_{i,r}(w,beta)/F_r(h_{i,r}(w)).                       (1.2)
```

This includes every `r=3,4,5` transition and all holding mass.  Reversibility
follows by summing the symmetric word-level stationary flow.

For a feasible length-`m-2` macro datum `gamma`, let `A_t gamma` be the datum
obtained by inserting `(t,t)`, and put

```text
d_gamma(alpha)=#{t in T_N: A_t gamma=alpha}.                    (1.3)
```

The word chain `R` inspects positions 1,2, holds if they differ, and if they
are `(t,t)` replaces them by `(s,s)` for uniform `s in T_N`.  Its macro
projection `S` satisfies, for distinct `alpha,beta`,

```text
S(alpha,beta)
 = [1/(M W_m(alpha))] sum_gamma W_{m-2}(gamma)
       d_gamma(alpha)d_gamma(beta),                             (1.4)
```

with the remaining row mass on the diagonal.  Formula (1.4), including its
diagonal completion, is exact.

For a transposition `c`, the length-three same-product fiber has size

```text
D_N=F_3(c)
   =M+3[2(N-2)]+2 binom(N-2,2)
   =(3N^2+N-12)/2 <=4M.                                        (1.5)
```

Indeed, condition on the third factor: it is `c`, shares one endpoint with
`c`, or is disjoint, leaving respectively `M`, `3`, or `2` two-factor
solutions.  A specified square replacement through `H_{1,3}` has probability

```text
1/[2|R_m|(m-2)D_N].                                           (1.6)
```

Consequently, pointwise off the diagonal and hence in Dirichlet form,

```text
barK >= c_sq S,
c_sq=M/[2|R_m|(m-2)D_N] >=1/[24(m-2)].                        (1.7)
```

The M02 connectivity proof is also sound.  Square-paired representatives can
refresh any pair edge, so `S` is connected.  The aligned `r=4` chain uses
starts `1,3,...,m-3`, which contain every adjacent letter pair, emulates each
Hurwitz move and each square refresh, and is connected conditional on the
audited Ben-Itzhak--Teicher classification.  A specified aligned output has
probability at least `1/[(m/2-1)M^3]`; for `m=4`, the unique aligned window is
the whole word.

The deterministic exact audit found no error in (1.1)--(1.7), row sums,
detailed balance, or connectivity in `(N,m)=(3,4),(4,4),(4,6)`.  Section 6
records the exact outputs and command.

## 2. Dense exact-support-partition projection

Let `P` range over exact labeled support partitions of `[N]`, including
isolated singleton blocks, that contain at least one nontrivial block.  Let
`E_P(k)` count exact-support-`P` identity words of length `k`, and define

```text
nu(P)=E_P(m)/Z_m.                                             (2.1)
```

Let `Pi` be the stationary-flow projection of `S` under the map that forgets
component weights and retains `P`.

**Theorem 2.1 (dense arbitrary-cut projection gap).**  If `N>=3`, `m` is
even, and

```text
m-2 >= 4M log(2N),                                           (2.2)
```

then

```text
Phi(Pi) >= 3/(16M^2),
gap(Pi) >= 9/(512M^4).                                      (2.3)
```

Here `Phi(Pi)=min_{0<nu(A)<=1/2}Q_Pi(A,A^c)/nu(A)`.  Thus (2.3)
controls every cut of the partition state space, not merely a nested
component-count threshold.

**Proof.**  For a partition `P`, order its blocks by their least labels and,
if `P` is not the one-block partition, let `F(P)` merge the first two blocks.
This makes all partitions a rooted tree with the full-support partition as
root.

The frozen M12 dense trace theorem proves the following target-wise estimate,
not only its layer-summed corollary:

```text
sum_{C:F(C)=P} nu(C) <= q_N nu(P),
q_N=4/N^4 <=1/4.                                             (2.4)
```

It also gives `nu(root)>=3/4`.  Iterating (2.4), the total mass of the
descendant subtree rooted at any `C` is at most

```text
nu(C)/(1-q_N) <= (4/3)nu(C).                                 (2.5)
```

It remains to lower-bound each parent edge.  Suppose the first two blocks of
`P` have sizes `a,b`, and put

```text
e(P)=sum_{B in P} binom(|B|,2).
```

Insert `(t,t)` in positions 1,2 of an exact-`P` word of length `m-2`, with
`t` any of the `e(P)` internal edges.  Deletion is injective jointly in the
core and `t`.  The dense trace estimates at lengths `m-2` and `m` give

```text
e(P) E_P(m-2)/E_P(m) >=1/[4e(P)].                            (2.6)
```

Under `R`, refresh this square to one of the `ab` edges between the first two
blocks.  Every such refresh has probability `1/M` and produces exactly
`F(P)`.  Therefore

```text
Pi(P,F(P)) >= ab/[4e(P)M] >=1/(4M^2).                        (2.7)
```

Now fix `A` with `0<nu(A)<=1/2`.  Since the root has mass at least `3/4`, it
is outside `A`.  Split the induced forest on `A` into connected components.
Each component has a unique top vertex `C` whose parent is outside `A`; the
component is contained in the descendant subtree of `C`.  Equations
(2.5)--(2.7) imply

```text
Q_Pi(A,A^c)
 >= sum_{top C} nu(C)/(4M^2)
 >= [3/(16M^2)] nu(A).                                      (2.8)
```

This proves the conductance claim.  The standard reversible-chain Cheeger
inequality `gap>=Phi^2/2` gives the second inequality in (2.3).  QED.

For comparison, the same estimates applied to all crossing edges, rather
than only the chosen parent, give the stronger bound

```text
Phi_pm^S({number of components <=c_0})
 >=3(N-1)/(16M^2)                                           (2.9)
```

for every nontrivial threshold under (2.2).  But (2.9) alone would not imply
any gap: the conductance minimum ranges over arbitrary subsets, which may
split a component-count layer or be a nonmonotone union.  No rearrangement
principle reduces such a cut to one of the `N-2` threshold cuts.  The rooted
tree argument (2.8) is the missing arbitrary-cut step.

## 3. Exact fixed-partition restrictions are zero-range chains

Fix `P`, with nontrivial blocks `B_1,...,B_q`.  Put

```text
v_i=|B_i|,       E_i=binom(v_i,2),       e=sum_i E_i,
G=m/2-N+|P|.
```

Every weighted macro datum above `P` is uniquely an allocation
`g=(g_1,...,g_q)` with `g_i>=0`, `sum_i g_i=G`, and block lengths

```text
k_i=2(v_i-1)+2g_i.
```

Define

```text
a_v(g)=C(v,2(v-1)+2g)/[2(v-1)+2g]!.                         (3.1)
```

By (1.1), the stationary law conditional on `P` is exactly

```text
nu_P(g)=(1/Z_P) product_i a_{v_i}(g_i).                     (3.2)
```

Let `S_P` be the rejected-exit restriction of `S` to this partition fiber.
For `g_i>=1` and `i!=j`, its exact off-diagonal transition is

```text
S_P(g,g-e_i_unit+e_j_unit)
 = [E_i E_j/(M m(m-1))] rho_{v_i}(g_i),                     (3.3)

rho_v(g)=a_v(g-1)/a_v(g)
        =k(k-1) C(v,k-2)/C(v,k),
k=2(v-1)+2g.                                               (3.4)
```

To prove (3.3), the unique distinct common-core macro datum has the same
partition and removes two letters from donor block `i`; its two incidence
multiplicities in (1.4) are `E_i` and `E_j`.  The ratio of its weight to the
source weight is

```text
W_{m-2}(gamma)/W_m(g)=rho_{v_i}(g_i)/[m(m-1)].              (3.5)
```

A finer common-core partition can reconnect to `P` in two ways only with the
same resulting block weights, so it contributes only to the diagonal, not to
(3.3).  Equations (3.3)--(3.5) are therefore exact, including the square
action rate.  Rejected exits are added to the diagonal and do not alter the
Dirichlet form.

The restriction is qualitatively irreducible: whenever `g_i>0`, the inherited
connected-factorization feasibility theorem makes `a_{v_i}(g_i-1)>0`, so one
unit can move from `i` to any `j`.  The allocation simplex is connected.  If
`q=1` or `G=0`, the restriction is a singleton.

### 3.1 Direct comparison to a uniform-destination zero-range process

For `q>=2`, define the continuous-time complete-graph zero-range generator

```text
(L_Z f)(g)
 = (1/q) sum_{i,j} rho_{v_i}(g_i)
       [f(g-e_i_unit+e_j_unit)-f(g)],                       (3.6)
```

with `rho_v(0)=0`.  It is reversible for the same law (3.2), because
`a_v(g)rho_v(g)=a_v(g-1)`.  Pointwise comparison of every off-diagonal edge
in (3.3) and (3.6) yields

```text
E_{S_P}(f,f)
 >= [q/(M m(m-1))] E_Z(f,f),
gap(S_P) >= [q/(M m(m-1))] gap(Z_P),                        (3.7)
```

since `E_iE_j>=1`.  This direct comparison removes the apparent obstruction
that the original factorization of (3.3) has destination law `E_j/e`, which
is not uniform.  There is no path or congestion term.

Boudou--Caputo--Dai Pra--Posta, Theorem 4.2, generator (4.2), and condition
(4.11), applies literally to (3.6): if

```text
delta_P=min_i inf_{g>=0}[rho_{v_i}(g+1)-rho_{v_i}(g)]>0,     (3.8)
```

then `gap(Z_P)>=delta_P`.  Consequently,

```text
gap(S_P) >= q delta_P/[M m(m-1)].                            (3.9)
```

The source's lower bound `g_x(k)>=1` is only a time-normalization; rescaling
handles any common positive lower bound.  Here positivity is unconditional:
the M12 deduction from Dubrovin--Yang--Zagier Proposition 1, equation (13),
proves

```text
a_v(g)/a_v(g-1) <=v^3/12,
rho_v(g)>=12/v^3                    (v>=2,g>=1).             (3.10)
```

Thus the first increment `rho_v(1)-rho_v(0)` and every source action rate are
already inverse polynomial.  What (3.10) does not control is cancellation in
`rho_v(g+1)-rho_v(g)` for `g>=1`.

## 4. Conditional dense gap reduction and the exact frontier

The word chain `R` is an orthogonal conditional-expectation projection: an
unequal initial pair is a singleton class, while each class `(t,t,u)` is
averaged uniformly over `t`.  Hence `R` is positive semidefinite.  Its macro
projection `S` is a compression and is positive semidefinite.  Each
rejected-exit restriction is a principal positive-semidefinite block plus a
nonnegative exit diagonal, so it is also positive semidefinite.

Apply Jerrum--Son--Tetali--Vigoda Theorem 1 to the exact-support-partition
decomposition of `S`.  Give a singleton restriction gap one, and put
`lambda_alloc=min_P gap(S_P)`.  With `gamma<=1` and all gaps at most one by
positive semidefiniteness, their exact bound implies

```text
gap(S) >= gap(Pi) lambda_alloc/4.                            (4.1)
```

Combining (2.3) and (4.1), under (2.2),

```text
gap(S) >=9 lambda_alloc/(2048M^4).                           (4.2)
```

Together with (1.7),

```text
gap(barK) >=9 lambda_alloc/[49152 (m-2)M^4].                 (4.3)
```

The smallest explicit sufficient proposition left by this route is:

> **HURWITZ-RATE-CURVATURE.**  There are universal `c_0>0` and
> `A<infinity` such that, for every `v>=2` and every `g>=0`, with
> `rho_v(0)=0`,
> `rho_v(g+1)-rho_v(g) >= c_0(v+g+1)^(-A)`.

If this proposition holds, (3.9) gives an inverse-polynomial
`lambda_alloc`, and (4.2)--(4.3) give an inverse-polynomial dense-regime gap
for `S` and the M02 macro projection.  Explicitly, because `q>=2` for every
nonsingleton restriction and `g<=m/2`,

```text
lambda_alloc
 >=2c_0/[M m(m-1)(N+m+1)^A].                               (4.4)
```

This is not yet TERMINAL A: HURWITZ-RATE-CURVATURE is open; (2.2) leaves the
sparse/intermediate regime; and a full-chain theorem also needs polynomial
gaps for the word restrictions inside each weighted macro fiber.

## 5. Literature applicability audit

1. **Boudou--Caputo--Dai Pra--Posta.**  Theorem 4.2 studies the generator
   `(1/n)sum_{x,z}g_x(eta_x)[f(eta^{xz})-f(eta)]`; with zero perturbing
   energy, condition (4.11) gives gap at least
   `inf_{x,k}[g_x(k+1)-g_x(k)]`.  After (3.7), this applies exactly if
   HURWITZ-RATE-CURVATURE is proved.  It does not itself prove that
   enumerative hypothesis.

2. **Hermon--Salez.**  Their Theorem 2 says that Dirichlet-form comparison
   between two zero-range processes with the same kinetics and invariant
   site law is exactly comparison of the single-particle jump matrices.
   Their uniformly-increasing-rate corollary is stated for doubly stochastic
   geometry.  The natural geometry of (3.3), with rows `E_j/e`, has invariant
   law `E_j/e` and is not doubly stochastic unless all block edge-counts
   agree.  Thus that corollary does not literally apply to the natural
   representation.  The elementary same-stationary-law comparison (3.7),
   not a misuse of their theorem, is what reaches the uniform complete graph.

3. **Gaudilliere--Reygner.**  Their Theorem 1 gives
   `t_mix(epsilon)<=km log(k/epsilon)` for their specifically defined chain
   on a conditional product of ultra-log-concave marginals.  For our
   `a_v`, ultra-log-concavity is equivalent to
   `g rho_v(g+1)>=(g+1)rho_v(g)`.  This shortcut is rigorously false:
   for `v=4,g=1`, exact counts give `rho_4(1)=16/13`,
   `rho_4(2)=195/82`, and the left-minus-right margin is `-89/1066`.
   Their Theorem 2 allows a quantified strict-log-concavity parameter but
   analyzes another Metropolis-like chain, so it still requires a new
   enumerative estimate and a Dirichlet comparison.

4. **High-dimensional walks.**  Anari--Liu--Oveis Gharan--Vinzant Theorem
   1.1 requires a homogeneous multiaffine strongly-log-concave generating
   polynomial and a uniform deletion down-up walk.  Alev--Lau Theorem 1.5
   requires a pure weighted simplicial complex and link-walk eigenvalue
   bounds.  Our top states are weighted partitions with repeated square
   choices; the deletion probability in (1.4) is state dependent and may
   hold, and no pure face/link structure has been identified.  Moreover the
   natural common-core incidence polynomial is not log-concave: its incidence
   matrices have rational ranks `3,6,13` in the three calibration cases.
   The Hessian has block form `[0 I; I^T 0]` and hence at least two positive
   eigenvalues; the rank-one correction in a log Hessian cannot remove them
   all.  This refutes this natural lift, not every possible lift.

5. **Classical split-merge chains.**  Random-transposition split-merge
   chains have Ewens/Poisson--Dirichlet stationary laws on integer block
   sizes.  Here the law is on labeled exact partitions with weight
   `E_P(m)`, and the microstate retains component weights and color
   interleavings.  No stationary-measure-preserving bounded simulation was
   found.  Mere similarity of merge/split moves gives no comparison.

Primary sources are listed with direct links in `report.md`.

## 6. Exact falsification and calibration

The deterministic script `audit_m02.py` uses exact permutation arithmetic
and `fractions.Fraction`.  It found:

| case | words | macros | `D_N` | `c_sq` | incidence rank | `S`,`B` |
|---|---:|---:|---:|---:|---:|---|
| `S_3,m=4` | 27 | 4 | 9 | `1/24` | 3 | connected |
| `S_4,m=4` | 120 | 13 | 20 | `3/80` | 6 | connected |
| `S_4,m=6` | 3936 | 17 | 20 | `1/80` | 13 | connected |

There were no macro-weight, row-sum, detailed-balance, common-core, or
`barK>=c_sq S` errors.  The same-component-count restrictions had component
sizes

```text
S3,m4: c=1 [1], c=2 [1,1,1]
S4,m4: c=2 [7], c=3 [1,1,1,1,1,1]
S4,m6: c=1 [1], c=2 [10], c=3 [1,1,1,1,1,1].
```

This exactly shows why decomposing only by component count fails: the top
`c=N-1` restriction consists of singleton repeated-edge macros.  It is a
restriction obstruction, not a bottleneck for `S` itself.

The independent exact rate audit found `rho_v(g+1)>rho_v(g)` for
`2<=v<=5,1<=g<=5`, but this is finite evidence only.  It also produced the
exact ultra-log-concavity counterexamples above and verified the proved floor
(3.10) in every tested case.

Calibration:

- odd `m` is empty; `m=0` and `N=2` even are singleton calibrations;
- `m=2,N>=3` is excluded and not repaired by these arguments;
- the dense theorem does not cover `m=4`, but `H_{1,4}` is a whole-word heat
  bath and separately gives `gap(K_{N,4})>=1/4`;
- doubled-tree minimal words correspond to `G=0`, so their allocation
  restrictions are singletons rather than hidden slow chains;
- color interleavings are included in the factorial weight (1.1);
- no edge- or vertex-parity surrogate is used;
- no length-two simulation is used;
- the repeated-edge macro appears only as a diagnostic counterexample to a
  bad decomposition, never as a routing hub;
- every dense-cut claim above includes both exact stationary mass and
  one-step boundary flow.
