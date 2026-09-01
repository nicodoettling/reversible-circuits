# M42 halfway checkpoint: prefix occupation reaches `N^2 log log N`

## Frozen scoped theorem candidate

Use the project multiplication convention, `m=4N^3+4`, and the literal
original lazy heat bath.  Put

```text
L_N=log log N,                 a_dagger=floor(N^2 L_N/100).
```

For `N>=10^6`, the proof below, combined with the already audited M37/M40
coefficient bookkeeping, gives simultaneously for every
`0<=a<=a_dagger`,

```text
pi(V^(a))<=exp(-4N^2),
Phi_pm^K(V^(a))>=N^(-25).                              (C.1)
```

This is genuinely beyond every constant multiple of `N^2`.  It remains an
anti-bottleneck theorem for one shell family, not Terminal A.

## 1. Prefix-hull lower bound

For a nontrivial cut side `S subset [N]`, let `H_S` be its setwise
stabilizer.  For `w=(t_1,...,t_m)`, put

```text
A_S(w)=#{j in [m]:t_1...t_j notin H_S}.               (C.2)
```

If `w` is reached in `u` updates from a word whose every factor lies in
`H_S`, take the overlap-connected components of all update windows.  Outside
their hulls the target factors equal the internal starting factors.  Each
hull has product in `H_S`, so by induction every prefix at a hull boundary
lies in `H_S`.  A component of `u_i` windows has span at most `4u_i+1`.
Thus

```text
A_S(w)<=sum_i(4u_i+1)<=5u.                             (C.3)
```

In particular, `A_S(w)>5a` rules out every path of at most `a` updates from
the `S`-internal macro.  This is order-sensitive and is strictly stronger for
the present purpose than counting cut-edge occurrences.

## 2. Kicked subset-walk contraction

Fix the source isolate `z=N`, put `d=N-1`, `E=binom(d,2)`, and delete the
primitive source blocks and four reserved factors.  Their completed products
are fixed permutations of `[d]`, hence deterministic *kicks* between the
remaining internal core segments.

For a nonempty proper `S subset [d]` of size `s<=d/2`, the uniform internal
transposition walk induces the lazy Johnson/Bernoulli--Laplace walk `P_s` on
the `s`-subsets.  Its eigenvalues are

```text
lambda_j=1-j(d-j+1)/E,              0<=j<=s.           (C.4)
```

This follows from the Johnson adjacency eigenvalues
`(s-j)(d-s-j)-j`.  All eigenvalues are nonnegative for `d>=5`, and the
mean-zero norm is

```text
rho=1-2/(d-1).                                          (C.5)
```

Every kick acts unitarily on the subset orbit and commutes with `P_s`, since
the transposition sum is central.  Set

```text
r=ceil(d log(4d)).                                      (C.6)
```

Between two core checkpoints separated by `r` core letters, with any number
of intervening kicks, the transition is `P_s^r U` and its mean-zero norm is

```text
eta<=rho^r<=(4d)^(-2)=1/(16d^2).                       (C.7)
```

## 3. Elementary confinement estimate, uniform in all kicks

Let `K=binom(d,s)` and let `D` project onto one fixed orbit state `S` in
`L^2` of the uniform law.  Any checkpoint transition `Q` in (C.7) has
`Q=Pi+R`, `||R||<=eta`, whence

```text
||D Q D||<=1/K+eta<=2/d.                               (C.8)
```

The same holds between nonconsecutive checkpoints.  Starting from an
arbitrary orbit state, the probability of visiting `S` at any prescribed
`k` checkpoint indices is therefore at most

```text
sqrt(K)(2/d)^(k-1).                                    (C.9)
```

Let the core length be `t>=m-5a>=3.99N^3`.  If at most `5a` core prefix
times are away from `S`, one of the `r` residue classes contains
`B>=t/(4d log(4d))` checkpoints with away fraction at most

```text
epsilon=10a/t<=0.026 L_N/N<1/100.                     (C.10)
```

For that residue, sum (C.9) over at most `epsilon B` missed visits.  Since
`K<=2^d` and binary entropy `H(epsilon)<=0.06`, its logarithm is at most

```text
(d/2)log 2+B H(epsilon)
 -(1-epsilon)B log(d/2)+log(d/2)
 <=(d/2)log 2-0.8B log(4d)
 <=-0.79N^2+O(N).                                      (C.11)
```

Union-bounding the `r` residues and fewer than `2^d` cuts still gives
`exp(-0.78N^2)` under the unconditioned core law.  The compatible-endpoint
lower bound is `E^t/d!`; paying the full `d!` once leaves bad fraction at
most

```text
d! r 2^d exp(-0.78N^2)<=exp(-0.75N^2)<1/2.            (C.12)
```

Thus for every fixed block/layout choice, every compatible endpoint retains
at least `(1/2)E^t/d!` cores satisfying `A_S>5a` simultaneously for every
nontrivial `S subset [d]`.  This estimate is uniform in the number, positions,
and values of all deterministic kicks.

## 4. Target exclusion

For the isolate cut `{z}|[d]`, the primitive-source rigidity from M37 and the
four-position final `H_5` push increase the exact required update count from
`a` to `a+1`.

Every other cut has `z` together with a nonempty proper `S subset[d]` on one
side, after complementing if necessary.  At core positions all completed
block products fix `z`, so its full prefix stabilizes that cut exactly when
the kicked subset process is at `S`.  Equations (C.3) and (C.12) rule out a
path of at most `a` updates.  Therefore every specified `H_5` target is
outside the literal `V^(a)`.

## 5. Polynomial entropy audit in the enlarged range

The primitive middle-word and layout losses are no longer constant, but they
remain polynomial:

```text
[M/(M-1)]^(4a)<=exp(0.081L_N),
C=ceil(20sqrt(a))<=2N sqrt(L_N)+1,
(m/(m-8a))^C<=exp(0.081L_N^(3/2)).                     (C.13)
```

For `N>=10^6`, the product in (C.13) is at most `N^2`.  Repeating the exact
M40 coefficient/tail comparison therefore gives

```text
|V^(a) charged to isolate cuts|<=N^7 B_a.              (C.14)
```

For non-isolate cuts the previous uniform `M/e<=5/2` is too crude.  With
smaller side `s`, use `e=M-s(N-s)` exactly.  For `s<=N/4`,

```text
log(M/e)<=5s/N,
E-e=(s-1)(N-s-1)>=0.7(s-1)N.                          (C.15)
```

Thus the positive active-block term is at most `20as/N`, whereas the trace
suppression is at least `5.6(s-1)N^2`; cut entropy and the Bessel term are
lower order.  For `s>=N/4`, trace suppression is `Omega(N^3)` while every
positive term is `O(N^2 L_N+N log N+N^(3/2)sqrt(L_N))`.  Hence all
non-isolate cuts together contribute below `B_a`, and

```text
|V^(a)|<=N^8 B_a.                                      (C.16)
```

The direct orientation count remains `exp(-4N^2)`: its isolate positive
terms are only `O(N sqrt(L_N)+N L_N)`, and (C.15) controls all other cuts.
The genuine same-product `H_5` exit still has probability
`1/[6(m-4)M^4]`.  Equations (C.14)--(C.16) therefore yield (C.1).

## 6. Current first gap

> **ENTROPY-MATCHED SUPERLOGARITHMIC SHELL ACTION.**  Replace the primitive
> source restriction by an exact first-return/segmentation boundary layer so
> that the source/outer ratio stays polynomial when
> `a/(N^2 log log N)->infinity`, ideally through `a=N^(2+delta)` or a fixed
> fraction of `m`.

The prefix-occupation repair itself already works at a small fixed fraction
of `m`.  The remaining restriction is enumerative: the present primitive
middle loss is `exp(Theta(a/N^2))` and becomes superpolynomial beyond
`a=O(N^2 log N)`.  A reversal of that exact boundary-layer entropy remains a
live Terminal-B alternative, but no conductance upper bound follows merely
from failure of this source family.
