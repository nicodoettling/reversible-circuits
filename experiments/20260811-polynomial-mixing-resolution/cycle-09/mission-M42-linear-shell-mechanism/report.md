# M42 final report: prefix occupation gives superquadratic shell leakage

## 1. Exact claim, quantifiers, convention, and kernel

Use `(pq)(x)=p(q(x))`; words evaluate as `t_1...t_m`.  Let

```text
N>=10^6,                         M=binom(N,2),
d=N-1,                           E=binom(d,2),
m=4N^3+4,                        L_N=log log N,
a_dagger=floor(N^2 L_N/100),
U={w in Omega(N,m):c(w)>=2},
V^(0)=U,
V^(a+1)=V^(a) union {y:K(x,y)>0 for some x in V^(a)}.  (1.1)
```

The target is the global uniform identity bridge and the literal chain is

```text
K=(1/2)I
 +(1/6) sum_{r=3}^5 [1/(m-r+1)]
       sum_{i=1}^{m-r+1}H_{i,r}.                      (1.2)
```

Every `H_{i,r}` is the exact uniform same-ordered-product heat bath.

**Theorem (proved).**  Simultaneously for every integer
`0<=a<=a_dagger`,

```text
pi_{N,m}(V^(a))<=exp(-4N^2)<1/2,                      (1.3)
Phi_pm^K(V^(a))>=N^(-25).                             (1.4)
```

Since `a_dagger/N^2 -> infinity`, this is a genuinely superquadratic shell
range.  It is a scoped anti-bottleneck theorem, not a global spectral-gap
bound.

## 2. Full proof

### 2.1 Prefix occupation is a deterministic distance witness

For a nontrivial cut side `S subset [N]`, let `H_S` be its setwise
stabilizer.  For `w=(t_1,...,t_m)` define

```text
A_S(w)=#{j in [m]:t_1...t_j notin H_S}.               (2.1)
```

**Lemma 2.1 (prefix-hull lower bound).**  If `w` is reached in `u` local
updates from a word all of whose factors lie in `H_S`, then

```text
A_S(w)<=5u.                                            (2.2)
```

*Proof.*  Take the union of every update interval in the path and decompose
it into overlap-connected components.  Outside their hulls, the target
factors equal the `H_S`-internal starting factors.  Every update preserves
the product of its interval, so the target product on each component hull
equals the starting product there and belongs to `H_S`.  Scanning from left
to right, every prefix before and after a hull therefore lies in `H_S`; only
prefixes inside hulls can contribute to (2.1).

A component containing `u_i` windows has span at most
`5+4(u_i-1)=4u_i+1`.  If there are `b` nonempty components, `b<=u`, hence

```text
A_S(w)<=sum_i(4u_i+1)=4u+b<=5u.                       (2.3)
```

This proves the lemma. `□`

Thus `A_S(w)>5a` rules out every path of at most `a` updates from the macro
whose factors are internal to `S|S^c`.

### 2.2 Source framework and deterministic kicks

Fix `z=N` and `H=Stab(z)=S_d`.  Retain the audited M37/M40 source family:

- primitive `z`-excursion blocks, whose inverse prefix state leaves `z`, has
  no intermediate return, and returns at the last factor;
- for a block of length `l`, budget `q=ceil((l-1)/4)` and
  `l in {4q-2,4q-1,4q,4q+1}`;
- budgets sum exactly to `a`, with at least three internal gap positions and
  four reserved internal factors after the rightmost block;
- exact primitive count `d(M-1)^(l-2)`;
- the five-factor zipper removes all blocks in exactly `a` genuine `H_5`
  updates.

Delete the primitive block positions and the four reserved factors.  The
remaining internal factors, concatenated in word order, form a core of length

```text
t=m-L-4>=m-5a>=3.99N^3.                               (2.4)
```

Every completed primitive block and the reserved product is an element of
`H`.  In the prefix process on `[d]`, these fixed products are deterministic
permutation kicks between the random internal core segments.

### 2.3 Exact subset spectrum under the project normalization

Fix a nonempty proper `S subset[d]`, with `s=|S|<=d/2` after complementing.
Uniform internal transpositions induce a walk `P_s` on the `s`-subsets.  It
has `e_s=E-s(d-s)` holding transpositions and one transition along each edge
of the Johnson graph.  Since the Johnson adjacency eigenvalues are

```text
(s-j)(d-s-j)-j,                 0<=j<=s,
```

the eigenvalues under the present all-transposition normalization are

```text
lambda_j=1-j(d-j+1)/E.                                (2.5)
```

For `d>=5` they are nonnegative, and the exact mean-zero operator norm is

```text
rho=lambda_1=1-d/E=1-2/(d-1).                         (2.6)
```

This checks rather than imports the normalization of the classical
Bernoulli--Laplace spectrum.

Every kick acts unitarily on the subset orbit.  It commutes with `P_s`
because the uniform transposition sum is central.  Set

```text
r_0=ceil(d log(4d)).                                   (2.7)
```

Between two checkpoints separated by `r_0` core factors, with any number and
placement of intervening kicks, the transition is `P_s^(r_0)U` for a
permutation operator `U`.  Its mean-zero norm is at most

```text
eta<=rho^(r_0)<=exp[-2r_0/(d-1)]
 <=(4d)^(-2)=1/(16d^2).                               (2.8)
```

### 2.4 A changing-expander confinement bound

Let `K_s=binom(d,s)`, let `Pi` project onto constants in uniform
`L^2`, and let `D` project onto the single orbit state `S`.  Any transition
`Q` between checkpoint times satisfies `Q=Pi+R`, `||R||<=eta`; therefore

```text
||D Q D||<=||D Pi D||+eta
 =1/K_s+eta<=2/d.                                     (2.9)
```

The same estimate holds between nonconsecutive checkpoints because there are
at least `r_0` random core factors between them.  Starting from an arbitrary
orbit state costs `sqrt(K_s)` in uniform `L^2`.  Hence the probability of
visiting `S` at any prescribed `k` checkpoint indices is at most

```text
sqrt(K_s)(2/d)^(k-1).                                 (2.10)
```

This proof is uniform in the number, values, and positions of all kicks.

Suppose at most `5a` of the `t` core-prefix times are away from `S`.
Partition the core indices into their `r_0` residue classes.  Some residue
has

```text
B>=t/[4d log(4d)]                                      (2.11)
```

checkpoints and away fraction at most

```text
epsilon=10a/t<=0.026L_N/N<1/100.                      (2.12)
```

For that residue, sum (2.10) over the choices of at most `epsilon B` missed
visits.  Since `K_s<=2^d` and binary entropy satisfies
`H(epsilon)<=0.06`, the logarithm of this probability is at most

```text
(d/2)log 2+B H(epsilon)
 -(1-epsilon)B log(d/2)+log(d/2)
 <=(d/2)log 2-0.8B log(4d)
 <=-0.79N^2+O(N).                                     (2.13)
```

Union-bound the `r_0` residues and fewer than `2^d` nontrivial subsets.  The
unconditioned fraction of internal cores failing for at least one `S` is at
most `exp(-0.78N^2)`.  The inherited arbitrary-endpoint Fourier/content
bound gives at least `E^t/d!` core words for every parity-compatible endpoint.
Paying the full endpoint factor once gives lost fraction

```text
d! r_0 2^d exp(-0.78N^2)
 <=exp(-0.75N^2)<1/2.                                 (2.14)
```

Therefore, for every fixed primitive-block/layout/reserved-factor choice and
every requested compatible endpoint, at least

```text
(1/2)E^t/d!                                            (2.15)
```

cores satisfy `A_S>5a` simultaneously for all nontrivial `S subset[d]`.
There is no endpoint-dependent or kick-dependent exceptional class.

### 2.5 Source count and exact target exclusion

Summing the four reserved factors restores the outside count
`(1/2)E^(m-L)/d!`.  Define

```text
A=(M-1)/E,                   D_A=1+A+A^2+A^3,
beta_-=(m-8a)d/E^2,          theta_-=beta_-D_A/A^4,
C=ceil(20sqrt(a)),

S_a=sum_{b=1}^{min(a,C)}
 binom(a-1,b-1)theta_-^b/b!.
```

Exactly as in M40, the injective robust-source count is

```text
B_a>=(1/2)E^m/d! A^(4a)S_a.                           (2.16)
```

Every source belongs to the literal `V^(a)` by the exact zipper path.

Push the final return crossing through the four reserved factors:

```text
(t,b_1,b_2,b_3,b_4)
 ->(b_1,b_2,b_3,b_4,h^(-1)th),       h=b_1...b_4.     (2.17)
```

The rightmost primitive excursion grows by four.  For the isolate cut
`{z}|[d]`, primitive grouping and the hull-span bound increase the minimum
required update count from `a` to `a+1`.

Now consider any other cut of `[N]`.  Complement it so that its side is
`{z} union S`, where `S` is a nonempty proper subset of `[d]`.  At every core
position the completed block products fix `z`; the full prefix stabilizes
this cut exactly when the kicked subset process is at `S`.  Equation (2.15)
gives more than `5a` core prefixes outside the stabilizer.  Lemma 2.1 rules
out every path of at most `a` updates from that cut macro.  Thus the target in
(2.17) lies outside the entire literal `V^(a)`, not merely outside an isolate
restriction.

A fixed length-five fiber contains at most `M^4` words, so the specified
original-chain exit probability is

```text
p_exit>=1/[6(m-4)M^4].                                (2.18)
```

### 2.6 Entropy comparison remains polynomial

The exact outer encoding from M40 gives, for each cut `P`,

```text
O_P(a)<=4e^m/|H_P| [1+
 sum_{Q=1}^a sum_{b=1}^Q
 binom(Q-1,b-1)R_P^(4Q)theta_P^b/b!],                (2.19)
```

where `e` is the number of internal transpositions,
`R_P=M/e`, `beta_P=m(M-e)/e^2`,
`D_P=1+R_P+R_P^2+R_P^3`, and
`theta_P=beta_PD_P/R_P^4`.

For isolate cuts, write `R=M/E`, `theta=mdD_R/(E^2R^4)`.  The two losses
which were constant in M40 are now

```text
[M/(M-1)]^(4a)<=exp(0.081L_N),
C<=2N sqrt(L_N)+1,
(m/(m-8a))^C<=exp(0.081L_N^(3/2)).                    (2.20)
```

For `N>=10^6`, their product is at most `N^2`: putting `x=log N`, the left
logarithm is at most `0.081[log x+(log x)^(3/2)]<2x`, and the inequality is
preserved as `x` grows.  The exact coefficient comparison and geometric
large-`b` tail from M40 therefore give

```text
|V^(a) charged to isolate cuts|
 <=56NaN^2 B_a<=N^7B_a.                              (2.21)
```

For a non-isolate cut with smaller side `2<=s<=N/2`, put
`e=M-s(N-s)`.  Compare with the isolate base `E` and set
`D=E-e=(s-1)(N-s-1)`.  If `s<=N/4`,

```text
log(M/e)<=5s/N,                 D>=0.7(s-1)N.         (2.22)
```

The logarithm of the total size-`s` contribution relative to `E^m/d!` is
therefore at most

```text
2s log N-5.6(s-1)N^2+20as/N
 +2sqrt(800sa)+log 8+(1/2)log(800sa)<-2N^2.          (2.23)
```

Indeed `20as/N<=0.2sNL_N`, while every other positive term is also lower
order than `(s-1)N^2`.  If `s>=N/4`, then `D>=0.1N^2`, so trace suppression
is at least `0.8N^3`; the active-block, cut-entropy, and Bessel terms are only

```text
O(N^2L_N)+O(N log N)+O(N^(3/2)sqrt(L_N)).             (2.24)
```

Summing all non-isolate sizes leaves less than `B_a`.  Hence

```text
|V^(a)|<=N^8B_a.                                      (2.25)
```

The direct outer count also supplies the global orientation.  For isolate
cuts, division by `|Omega(N,m)|>=2M^m/N!` has the dominant term
`m log(E/M)<=-8N^2`, while every positive term is
`O(Nsqrt(L_N)+NL_N+log N)`.  Equations (2.22)--(2.24) make non-isolate cuts
smaller.  Thus

```text
pi(V^(a))<=exp(-4N^2)<1/2.                            (2.26)
```

### 2.7 Complete full-kernel flow

For `r=3,4,5`, write

```text
Q_r(B,B^c)=1/[6(m-r+1)|Omega|]
 sum_{w in B}sum_iH_{i,r}(w,B^c),
Q_K=Q_3+Q_4+Q_5.                                     (2.27)
```

Retain only the `B_a` sources and their positive specified `Q_5` exits;
every omitted `Q_3,Q_4,Q_5` summand is nonnegative.  From (2.18), (2.25),
and (2.26),

```text
Phi_pm^K(V^(a))
 >=N^(-8)/[6(m-4)M^4]
 >=N^(-25).                                           (2.28)
```

This proves (1.3)--(1.4) for `1<=a<=a_dagger`.  At `a=0`, use
`U subset V^(1)` for mass and the inherited M25 bound
`Phi_pm^K(U)>=1/(32N^3)`.

## 3. Probability, runtime, path length, and congestion

- Kicked-core failure before endpoint conditioning is at most
  `exp(-0.78N^2)`; after all cuts and the single `d!` endpoint loss it is at
  most `exp(-0.75N^2)`.
- The bound is uniform in every fixed block product, layout, kick placement,
  subset size, and compatible endpoint.
- Every source has an exact length-`a` path of genuine `H_5` zipper updates
  to `U`.
- Every specified exit is one actual `H_5` outcome with probability at least
  `1/[6(m-4)M^4]`.
- The source/whole-shell ratio is at least `N^-8`; there is no path-history or
  canonical-hub congestion.
- The zipper runs in `O(aN)` maintained-product time.  Prefix robustness is
  an enumerative certificate and is not required by the sampler.
- Exact local block sampling remains polynomial in `N,m`.

## 4. Dependencies and statuses

1. **Proved here:** prefix-hull distance witness; kicked Johnson-walk
   contraction; changing-walk confinement; endpoint-uniform robust core;
   alternative-cut exclusion; superquadratic entropy and cut stratification.
2. **Proved in M37/M40 and restated where used:** outer cluster encoding,
   five-factor zipper, primitive enumeration/rigidity, injective source
   count, and the genuine final `H_5` surgery.
3. **Proved/frozen in M12/M31:** dense direct-product trace upper bound,
   global parity-coset return lower bound, and arbitrary-compatible-endpoint
   Fourier/content lower bound.
4. **Inherited proved:** stationarity, reversibility, irreducibility, exact
   polynomial local sampling, and M25's radius-zero leakage theorem.
5. **Cited/checked:** Diaconis--Shahshahani's Bernoulli--Laplace spectral
   analysis.  The exact lazy normalization is rederived in (2.5).
6. **Cited but not used:** Gillman's homogeneous expander-walk Chernoff
   theorem; deterministic kicks violate its literal setup, so (2.9)--(2.14)
   replace it.
7. **Empirical dependencies:** none.

## 5. First unproved standalone proposition

> **ENTROPY-MATCHED SUPERLOGARITHMIC SHELL ACTION.**  Construct an exact
> first-return/segmentation boundary source whose ratio to the cumulative
> isolate outer encoding is polynomial whenever
> `a/(N^2 log log N)->infinity`, prioritizing `a=N^(2+delta)` and then a fixed
> fraction of `m`; or prove a literal full-`K` bottleneck when that exact
> boundary-layer entropy reverses.

The prefix-occupation mechanism itself works for a small fixed fraction of
`m`.  The current restriction is the primitive-source middle factor

```text
[M/(M-1)]^(4a)=exp(Theta(a/N^2)),                     (2.29)
```

which becomes superpolynomial beyond `a=O(N^2 log N)`.  Failure of this
particular source comparison is not a conductance upper bound.

## 6. Strongest self-attack

Conductance is not monotone.  Although the theorem moves beyond every
constant times `N^2`, it controls only radii up to `N^2 log log N/100` and
only this disconnected-neighborhood shell family.

At `a=N^(2+delta)` the primitive no-intermediate-return restriction loses
`exp(Theta(N^delta))` relative entropy, and the present boundary sources are
too rare for an inverse-polynomial flow lower bound.  Canonical splitting at
intermediate prefix returns changes the exact minimal window-cover cost and
requires a new hard-rod/segmentation layer theorem.  It could restore the
action bound, or its failure could signal a real shell transition.  Neither
conclusion is proved here, and no auxiliary slow mode is promoted to
Terminal B.

## 7. Calibration

- Odd `m`: empty state space; no claim.
- `m=0` and even `N=2`: singleton regimes.
- `m=2,N>=3`: excluded disconnected chain.
- `S_3,m=4`: 27 words/four Hurwitz classes; whole-word `H_4` makes the
  analogous shell global.
- `S_4,m=4`: 120 words/13 Hurwitz classes; whole-word `H_4` is retained.
- `S_4,m=6`: 3936 words/17 Hurwitz classes; no finite extrapolation is used.
- Near-minimal doubled-tree words need not have a dense prefix core; the
  theorem explicitly fixes `m=4N^3+4`.
- The proof uses ordered prefix products and ordered windows, not graph-only
  support, degree parity, edge multiplicity parity, or color counts.
- Three crossings may have subgroup product; isolate exclusion uses primitive
  return times, while alternative cuts use full prefix-set occupation.
- The zipper uses actual `H_5` moves and does not assert a general `L=2`
  simulation.
- Global smaller-side orientation and all `Q_3+Q_4+Q_5` normalizations are
  explicit.

## 8. Artifacts, reproduction, and primary citations

Owned artifacts:

- `plan.md`
- `checkpoint.md`
- `resource_audit.md`
- `report.md`

No computation was used.  Reproduce by checking Lemma 2.1, the spectrum
(2.5)--(2.8), the projection-product confinement (2.9)--(2.14), source and
target exclusion (2.15)--(2.18), polynomial coefficient/cut comparison
(2.19)--(2.26), and exact full-kernel flow (2.27)--(2.28).

Primary sources audited:

- Persi Diaconis and Mehrdad Shahshahani, *Time to Reach Stationarity in the
  Bernoulli--Laplace Diffusion Model*, SIAM J. Math. Anal. 18 (1987),
  208--218, DOI 10.1137/0518016:
  <https://epubs.siam.org/doi/10.1137/0518016>.
- David Gillman, *A Chernoff Bound for Random Walks on Expander Graphs*, SIAM
  J. Comput. 27 (1998), 1203--1220, DOI
  10.1137/S0097539794268765:
  <https://epubs.siam.org/doi/10.1137/S0097539794268765>.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED

The verdict is the assigned superquadratic shell-leakage theorem.  It is not
Terminal A or Terminal B.
