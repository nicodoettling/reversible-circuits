# M31 final report: logarithmically growing full-support shells have polynomial leakage

## 1. Exact claim, quantifiers, convention, and kernel

Use `(pq)(x)=p(q(x))`; an ordered word evaluates as `t_1...t_m`.  For every
`N>=5`, set

```text
M=binom(N,2),             E=binom(N-1,2),
m=4N^3+4,                 a_*(N)=max(3,floor(log N)),
U={w in Omega(N,m):c(w)>=2},
V^(0)=U,
V^(a+1)=V^(a) union {y:K(x,y)>0 for some x in V^(a)}.  (1.1)
```

Here `c` counts support components including isolates, logarithms are natural,
and the original chain is

```text
K=(1/2)I
 +(1/6) sum_{r=3}^5 [1/(m-r+1)] sum_{i=1}^{m-r+1}H_{i,r}.  (1.2)
```

Each `H_{i,r}` is the exactly uniform length-`r` transposition word with the
same ordered product.

**Theorem (proved).**  With the explicit universal constant
`C_0=5,000,000`, for every `N>=5` and every integer
`1<=a<=a_*(N)`, the actual graph shell has

```text
pi_{N,m}(V^(a)) <= exp(-4N^2)<1/2,                     (1.3)

Phi_pm^K(V^(a))
 >=1/[288 N C_0^a (m-4)M^4E^5]
 >=N^(-60).                                            (1.4)
```

In particular, `V^(a)` is proper throughout a radius range tending to
infinity, and these shells do not furnish Terminal B.  This is a theorem
about logarithmic radii only; it neither proves the global gap lower bound nor
rules out a bottleneck at a larger radius or elsewhere in the state space.

## 2. Full argument

### 2.1 The product-cluster sandwich

For a nontrivial vertex bipartition `P`, write `H_P` for the direct-product
subgroup preserving both sides, `e=e(P)` for the number of transpositions
internal to its sides, and `x=M-e` for the crossing transpositions.

Define the outer set `C_a` as follows.  A word `y` belongs to `C_a` if there
are a cut `P`, pairwise disjoint intervals `J_1,...,J_c`, and positive
integers `q_1,...,q_c` such that

```text
sum_j q_j<=a,                  |J_j|<=4q_j+1,
product(y|J_j) in H_P,
every P-crossing factor of y lies in union_j J_j.       (2.1)
```

Define the inner set `D_a` by requiring instead at most `a` disjoint
intervals of lengths in `{3,4,5}` which cover all crossings and whose ordered
products each admit an internal factorization of the same displayed length.
Then

```text
D_a subset V^(a) subset C_a.                           (2.2)
```

The first inclusion follows by resampling the displayed blocks one at a time;
afterwards every factor is internal to `P`.  For the second, take a path of at
most `a` positive local updates from a disconnected word `x_0` to `y`, and
choose `P` between support components of `x_0`.  Decompose the update windows
into connected components under positional overlap.  A component containing
`q` windows has a contiguous hull of length at most

```text
5+4(q-1)=4q+1.                                         (2.3)
```

All changes made by this component occur in its hull, and every update
preserves the ordered product of its interval.  Hence the final hull product
equals the initial hull product and lies in `H_P`.  A component with no final
crossing factor can be discarded: its final factors are all internal and may
be counted with the outside word.  The remaining hulls are disjoint and
satisfy (2.1).  This proves (2.2).

The ordered-product condition in (2.1) is essential.  This is not the false
claim that a support-only cover determines graph distance.

### 2.2 Counting an active cluster

Let `A_l(P)` be the number of length-`l` transposition blocks whose ordered
product belongs to `H_P` and which contain a crossing factor.  Then

```text
A_l(P)<=l^2 x M^(l-2).                                 (2.4)
```

To prove this, mark the first and last crossing positions `p<q`.  There must
be two distinct positions: a word with exactly one crossing factor has the
form `h_0 t h_1`, with `h_0,h_1 in H_P` and `t notin H_P`, and therefore
cannot have product in `H_P`.  Choose `p,q`, the first crossing factor, and
all factors except the last crossing factor.  The suffix after `q` is
internal.  If `L t R in H_P`, with `R in H_P`, then on either cut side `S`
we must have

```text
t(S)=L^(-1)(S).                                        (2.5)
```

A crossing transposition changes `S` by deleting one vertex and inserting
one vertex.  The target set in (2.5), if attainable this way, uniquely fixes
that pair and hence fixes `t`.  It may also be unattainable.  Thus the last
crossing factor has at most one choice, proving (2.4).  Allowing the
intermediate choices to violate the marked first/last conditions only
overcounts.

### 2.3 Outside coefficients, including odd lengths

Let `T_P` be the sum in the group algebra of all `e` internal
transpositions.  It is central in `H_P`.  After active hull words and their
products `h_j in H_P` are fixed, all internal outside segments combine to one
coefficient of `T_P^t`, where `t=m-sum_j|J_j|`.

For `p=floor(t/2)` and `q=ceil(t/2)`, convolution and Cauchy--Schwarz give

```text
[g]T_P^t <=sqrt([id]T_P^(2p) [id]T_P^(2q)).            (2.6)
```

The frozen dense direct-product trace estimate applies to both even lengths:
`t>=m-5a_*`, and hence `(t-1)/e>=4log(2N)`.  Consequently

```text
[g]T_P^t<=4e^t/|H_P|.                                  (2.7)
```

This handles both parities of the outside length; no odd-block commutation is
used.

### 2.4 Constant-per-update counting and stationary orientation

Let the smaller side of `P` have size `s`.  For `N>=5`, elementary algebra
gives

```text
mx/M^2<=26s,                    M/e<=5/2.               (2.8)
```

For a hull charged with `q` updates, (2.4), its at most `m` placements, and
the outside normalization in (2.7) give the relative cost

```text
F_q(P)
 :=sum_{l=2}^{4q+1} m l^2 x M^(l-2)/e^l
 <=6500s q^3(625/16)^q
 <=s(2,100,000)^q.                                    (2.9)
```

The first inequality uses at most `4q` lengths,
`4q+1<=5q`, and (2.8); the second uses `q^3<=8^q`.
For a total of `Q` active updates, summing over all ordered compositions of
`Q` gives

```text
sum_{c=1}^Q sum_{q_1+...+q_c=Q} product_j F_{q_j}(P)
 <=(2s*2,100,000)^Q.                                  (2.10)
```

Summing `0<=Q<=a` and rounding upward to `C_0=5,000,000`, the number of
identity words charged to a fixed cut is therefore at most

```text
12(C_0s)^a e^m/|H_P|.                                 (2.11)
```

The `Q=0` term includes the initially disconnected words.  All inactive
updates were safely absorbed among the arbitrary internal outside factors.

Put

```text
e_s=binom(s,2)+binom(N-s,2),
E=binom(N-1,2).
```

Summing labeled cuts of smaller side `s` and comparing to an isolate cut
gives the exact factorial ratio

```text
sum_P (C_0s(P))^a e(P)^m/|H_P|
 <=[E^m/(N-1)!]
   sum_{s=1}^{floor(N/2)}
    [binom(N,s)^2/N](C_0s)^a(e_s/E)^m.                (2.12)
```

At `s=1` the summand is `NC_0^a`.  For `s>=2`,

```text
E-e_s=(s-1)(N-s-1),                    m/E>=8N,        (2.13)
```

so the logarithm of the corresponding summand is at most

```text
2s log N+a log(C_0s)-8N(s-1)(N-s-1).                  (2.14)
```

This is nonpositive throughout the stated range.  Indeed, for `5<=N<=54`,
`a<=3`, and the positive part is bounded by
`N log N+3log(C_0N)`; for `N>=55`, it is bounded by
`N log N+log N log(C_0N)`.  The negative part is at least `8N(N-3)`.
The first inequality is already strict at `N=5`, and the margin increases
thereafter.  There are fewer than `N` non-isolate sizes.  Equations
(2.11)--(2.14) now imply

```text
|V^(a)|<=24N C_0^a E^m/(N-1)!.                        (2.15)
```

For even `m`, parity-coset Cauchy--Schwarz gives the global identity-return
lower bound

```text
|Omega(N,m)|>=2M^m/N!.                                (2.16)
```

Since `E/M=(N-2)/N`, division yields

```text
pi(V^(a))
 <=12N^2C_0^a(1-2/N)^m
 <=exp{log 12+2log N+a log C_0-2m/N}
 <=exp(-4N^2)<1/2.                                    (2.17)
```

For the last inequality, `a<=3` through `N=54`, while above that point
`a<=log N`; the positive logarithms are at most `4N^2`, beginning already at
`N=5`.  Thus (2.17) proves both properness and the exact global smaller-side
orientation needed below.

### 2.5 Uniform arbitrary-endpoint robust tails

Write `d=N-1` and view `E=binom(d,2)` as the transposition alphabet on
`[d]`.  Set

```text
L=4a-4,                         n=m-(4a+1).             (2.18)
```

A length-`n` tail is called *`a`-window robust* if deleting the union of any
at most `a` intervals of length at most five leaves connected support on
`[d]`.

First, every parity-compatible endpoint `h in S_d` has at least

```text
E^n/d!                                                   (2.19)
```

length-`n` transposition factorizations.  For completeness, Fourier inversion
for the random-transposition walk has trivial and sign contributions equal to
two on the compatible parity class.  The content calculation in the frozen
M12 trace lemma says that, outside those representations, the absolute
normalized transposition character ratio is at most
`rho=1-2/(d-1)`: the content sum is at least `d` below the extremal value
`E=binom(d,2)`, and conjugate partitions give the negative extreme.  Thus the
remaining character sum has magnitude at most
`d!rho^n<1`, since `d>=4` and `n>=m-4a_*-1`.  This proves (2.19).

If a tail is not robust, choose a cut of `[d]` disconnected after deleting
the witness windows.  Extending shorter windows to length five, there are at
most `n^a` ordered window choices and at most `2^d` cuts.  The cut has at most

```text
E-(d-1)=E(1-2/d)                                       (2.20)
```

internal transpositions.  Ignoring the endpoint condition, the number of bad
tails is at most

```text
n^a 2^d E^(5a)[E(1-2/d)]^(n-5a).                      (2.21)
```

Relative to (2.19), its logarithm is at most

```text
a log n+d log 2+log(d!)-2(n-5a)/d <=-N^2<log(1/2).    (2.22)
```

The inequality follows from `n=4N^3+3-4a`, `a<=a_*`, and `d=N-1`; its
negative term is order `8N^2`, whereas the positive terms are at most
`O(N log N+(log N)^2)`, with the displayed bound already valid at `N=5`.
Consequently, for every compatible endpoint, at least

```text
(1/2)E^n/(N-1)!                                       (2.23)
```

tails are `a`-window robust.  This is a uniform endpoint statement, not an
identity-tail specialization.

### 2.6 Explicit sources in the actual `a`-shell

Let

```text
z=N,                 s=(z,1),                 q=(2,3).
```

The transpositions `s` and `q` are disjoint.  Choose arbitrary internal
transpositions `c_1,...,c_L` on `[d]`, put `g=c_1...c_L`, and choose an
`a`-window robust tail `u=(b_1,...,b_n)` of product `(qg)^(-1)`.
The parity is compatible because `L` is even and `n` is odd.

Start from the disconnected identity word

```text
x_0=(q,q,q,q,q,c_1,...,c_L,u).                         (2.24)
```

Its first five factors have product `q`, so its total product is identity and
`z` is isolated.  One actual `H_5` update replaces `q^5` by

```text
B=(s,q,q,q,s),                 product(B)=q.           (2.25)
```

Repeated right-Hurwitz identities

```text
(r,t) -> (t,t^(-1)rt)                                  (2.26)
```

implemented four at a time as positive `H_5` outcomes push the last `s`
through `c_1,...,c_L` in `a-1` more updates.  The resulting source is

```text
y=(s,q,q,q,c_1,...,c_L,g^(-1)sg,u).                   (2.27)
```

It lies in the actual `V^(a)`, not merely in the outer envelope.  Its only
`{z}|[d]` crossing factors occur at positions `1` and `4a+1`.

Different choices of the visible `c`-sequence and tail give different
sources.  Equations (2.18) and (2.23) therefore give

```text
R_a>=E^L (1/2)E^n/(N-1)!
   =(1/2)E^(m-5)/(N-1)!.                              (2.28)
```

The loss is the fixed power `E^5`, independent of `a`.

### 2.7 One genuine `H_5` move exits `V^(a)`

Apply `H_5` to the block consisting of the last crossing factor in (2.27)
and `b_1,...,b_4`.  Four identities (2.26) move that crossing factor to the
right.  The target `y'` has exactly two `{z}|[d]` crossings, at positions

```text
1 and 4a+5.                                             (2.29)
```

Suppose for contradiction that `y' in V^(a)`.  Choose a path of at most `a`
updates from a disconnected word and a cut `P` between initial components.
Delete the union of its update windows from `y'`.  Erasing the one inserted
`z`-crossing coordinate maps the intersection of each global window with the
ordered `b`-tail to one interval of at most five consecutive `b`'s.  Tail
robustness therefore leaves the support on `[d]` connected.  Every undeleted
factor is internal to `P`, so all vertices of `[d]` must lie on one side of
`P`; nontriviality forces `P={z}|[d]`.

Now use the product-cluster decomposition from Section 2.1.  An active
cluster has product in `H_P` and hence cannot contain exactly one crossing
factor.  Since (2.29) lists the only two crossings, they must belong to the
same overlap-connected cluster.  A cluster of at most `a` windows has span at
most `4a+1`, whereas the two positions in (2.29) have hull length `4a+5`.
This contradiction proves

```text
y' notin V^(a).                                         (2.30)
```

A length-five fixed-product fiber has at most `M^4` words, because its first
four factors determine the fifth.  Including the original laziness,
block-size choice, scan position, and exact heat bath, the specified exit has
probability at least

```text
p_5=1/[6(m-4)M^4].                                     (2.31)
```

### 2.8 Full `Q_3+Q_4+Q_5` flow and conductance

For `r=3,4,5`, define

```text
Q_r(A,A^c)
 =1/[6(m-r+1)|Omega|]
   sum_{w in A} sum_i H_{i,r}(w,A^c).                  (2.32)
```

The lazy identity contributes no boundary flow and

```text
Q_K(A,A^c)=Q_3(A,A^c)+Q_4(A,A^c)+Q_5(A,A^c).          (2.33)
```

Retain only the `R_a` sources in (2.28) and their specified `H_5` outcomes.
All uncharged terms in (2.33) are nonnegative.  Since (2.17) proves that
`V^(a)` is the smaller side, (2.15), (2.28), and (2.31) yield

```text
Phi_pm^K(V^(a))
 >=(R_a/|V^(a)|)p_5
 >=1/[288N C_0^a(m-4)M^4E^5].                         (2.34)
```

Finally, throughout the stated range

```text
C_0^a<=N^29.                                           (2.35)
```

For `N<=54`, this follows from `a<=3` and
`C_0^3<=5^29`; for `N>=55`, it follows from
`a<=log N` and `log C_0<29`.  Since `m-4=4N^3`,
`M,E<=N^2`, and `1152<=N^5` for `N>=5`, (2.34) is at
least `N^-56`, and hence at least the advertised `N^-60`.  This completes
the proof of (1.3)--(1.4).

## 3. Probability, runtime, path length, and congestion accounting

- Exact shell mass upper bound: (2.17), at most `exp(-4N^2)`.
- Robust source count: (2.28), at least
  `(1/2)binom(N-1,2)^(m-5)/(N-1)!`.
- Source construction: exactly `a` positive `H_5` transitions from a
  disconnected identity word.
- Boundary transition: one actual `H_5` outcome of the original chain, with
  probability at least `1/[6(m-4)M^4]`.
- Full conductance: the exact first expression in (1.4), hence `N^-60`
  uniformly over all `a<=a_*(N)`.
- No comparison paths, canonical hubs, or congestion bound are used.  The
  Hurwitz identities merely name one output in a single exact heat-bath
  fiber.
- A certificate for membership in the outer envelope consists of a cut,
  at most `a` window clusters, and their products, and is checked in
  `O(N+m+a)` group/scan operations.  Naive robustness checking costs
  `O(n^(a+1)+Nn^a)` and is not claimed efficient when `a` grows.  The theorem
  is enumerative and does not require recognition or generation of the
  robust source set.
- The inherited exact `r<=5` conditional sampler has polynomial per-step
  cost in `N,m`.

## 4. Dependencies and statuses

1. **Proved here:** the product-cluster sandwich, active-block bound,
   constant-per-update shell count, global orientation, robust-tail count,
   explicit boundary family, target exclusion, and full conductance bound.
2. **Proved/frozen in Cycle-02 M12:** the dense direct-product return
   estimate used in (2.7), with its density hypothesis checked here.
3. **Proved/frozen in the same Cycle-02 M12 trace lemma and rederived in
   Section 2.5:** the content-sum character-ratio bound
   `max |r_lambda|=1-2/(d-1)` outside trivial/sign.  Fourier inversion then
   gives the elementary uniform endpoint lower bound (2.19); no external
   pointwise-mixing theorem is imported.
4. **Inherited proved:** exact same-product heat-bath reversibility,
   stationarity, and polynomial exact block sampling.
5. **Not used:** conductance monotonicity under shell enlargement, a
   support-only distance characterization, parity/degree characterization of
   identity words, canonical normal forms, restriction gaps, the false
   length-two simulation, or finite spectral evidence.
6. **Empirical dependencies:** none.

## 5. First unproved standalone proposition

> **MESOSCOPIC SHELL ACTION.**  There are universal `c,C>0` such that, for
> `m=4N^3+4` and every integer
> `1<=a<=cN^2/log(N+1)`, the actual shell in (1.1) satisfies
> `Phi_pm^K(V^(a))>=N^-C` whenever it is a proper set.

The present proof loses `C_0^-a`; this remains polynomial only for
`a=O(log N)`.  Either a source family with entropy matching the outer shell at
mesoscopic radii or a different layer-flow argument is needed.

## 6. Strongest self-attack

The shell count is deliberately an outer-envelope overcount and the source
family deliberately sparse.  Their ratio is only `C_0^-a`.  At
`a/log N -> infinity`, this very proof becomes superpolynomially weak and says
nothing: it neither proves a bottleneck nor excludes one.  Conductance is not
monotone in `a`, and irreducibility implies sufficiently large shells
eventually fill the state space.  Thus (1.4) cannot be extrapolated to a
mesoscopic radius, to an arbitrary internal full-support cut, or to the
global spectral gap.

The argument also relies essentially on dense tails of length `Theta(N^3)`.
It is not a theorem for near-minimal connected words or for another scaling
of `m`.

## 7. Calibration

- Odd `m`: `Omega(N,m)` is empty; no shell theorem is asserted.
- `m=0` and even `N=2`: singleton regimes.
- `m=2,N>=3`: excluded disconnected chain.
- `S_3,m=4`: 27 identity words and four pure-Hurwitz components.  The
  whole-word `H_4` makes the analogous first neighborhood global; the
  asymptotic theorem starts at `N=5`.
- `S_4,m=4`: 120 words and 13 pure-Hurwitz components; again the whole-word
  `H_4` cannot be omitted.
- `S_4,m=6`: 3936 words and 17 pure-Hurwitz components.  These counts are not
  used as asymptotic evidence.
- Near-minimal connected doubled-tree words need not possess robust tails;
  the dense `m=4N^3+4` hypothesis is explicit.
- Ordered interval overlap and ordered subgroup products are essential.
  Disjoint-support color interleavings are not collapsed to unordered graphs.
- Neither edge-multiplicity parity nor degree parity is used to characterize
  an identity word.
- Every exit charged in (2.34) is a genuine `H_5` update.  No `L=2` local
  simulation is invoked.
- The exact global mass orientation is proved before division, and all
  `Q_3+Q_4+Q_5` normalizations appear in (2.32)--(2.34).

## 8. Artifacts and reproduction

Owned artifacts:

- `plan.md`
- `checkpoint.md`
- `report.md`

No computation was used.  Reproduce the theorem by checking, in order:

1. overlap-cluster invariance (2.1)--(2.3);
2. the forced-last-crossing count (2.4)--(2.5);
3. the odd/even outside coefficient and cut sum (2.6)--(2.17);
4. the uniform endpoint and robustness bounds (2.18)--(2.23);
5. the ordered-product `H_5` construction and exclusion
   (2.24)--(2.31); and
6. the exact full-kernel flow calculation (2.32)--(2.35).

Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED

This verdict concerns the uniform inverse-polynomial leakage theorem for the
growing logarithmic-radius shell family.  It is not either global terminal
outcome.
