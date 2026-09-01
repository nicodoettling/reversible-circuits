# M30 final report: the second full-support shell leaks inverse-polynomially

## 1. Exact claim, quantifiers, convention, and kernel

Use `(pq)(x)=p(q(x))`; words evaluate as `t_1...t_m`.  For every `N>=5`,
put

```text
M=binom(N,2),                   m=4N^3+4,
V^(0)={w in Omega(N,m):c(w)>=2},
V^(a+1)=V^(a) union {y:K(x,y)>0 for some x in V^(a)},  (1.1)
```

where `c` counts all support components, including isolates.  The original
chain is

```text
K=(1/2)I
 +(1/6) sum_{r=3}^5 [1/(m-r+1)] sum_i H_{i,r}.         (1.2)
```

**Theorem (proved).**  The actual second shell `V^(2)` admits the rigorous
intrinsic sandwich defined in Section 2.1.  It is proper, has exact global
orientation

```text
pi_{N,m}(V^(2))<=exp(-5N^2)<1/2,                       (1.3)
```

and satisfies the full-chain conductance bound

```text
Phi_pm^K(V^(2))
 >=1/[96N m^2(m-4)M^14]
 >=N^(-38).                                             (1.4)
```

Thus the literal radius-two halo of all disconnected words is not a
superpolynomial bottleneck on this infinite sequence.  This is a scoped
anti-bottleneck theorem, not Terminal A and not a refutation of unrelated
Terminal-B cuts.

## 2. Full argument and construction

### 2.1 A rigorous intrinsic sandwich

For a nontrivial vertex bipartition `P`, let `H_P` be its direct-product
subgroup and call a factor *crossing* if its endpoints lie on opposite sides.
Define three intrinsic sets:

- `C_2`: some cut has all crossing occurrences coverable by two intervals,
  each of length at most five;
- `O_2`: some cut has all crossing occurrences in one interval of length at
  most nine;
- `D_2`: some cut has all crossing occurrences in two disjoint length-five
  intervals `I,J`, and both ordered block products `h_I,h_J` lie in `H_P`.

Then

```text
D_2 subset V^(2) subset O_2 union D_2 subset C_2.       (2.1)
```

For `D_2 subset V^(2)`, a length-five block whose product lies in `H_P` has
an internal same-product factorization of length five: take a minimal internal
transposition factorization and pad by adjacent internal squares.  Replace
one of `I,J`; the resulting word has all crossings in the other five-window
and hence lies in the exact first shell from M28.  Replacing that window
reaches `V^(0)`.

For the middle inclusion, take `y in V^(2)`, a predecessor `x in V^(1)`, a
witness cut/window `I` for `x`, and the update window `J` producing `y`.  M28
proved that `I` can be chosen of length at most five.  Every crossing factor
of `y` lies in `I union J`.

If its hull has length at most nine, `y in O_2`.  Otherwise `I,J` are
separated and can be extended to disjoint length-five intervals: a hull of
length at least ten has enough intervening positions to supply their combined
length deficit.  In `x`, every factor outside `I` is internal, so `h_I in
H_P`; every factor in the disjoint `J` is internal, and the update preserves
its ordered product, so the `J` product in `y` also lies in `H_P`.  Added
extension factors are internal.  Hence `y in D_2`.  Words already in `V^(1)`
fall in `O_2`.  The last inclusion in (2.1) is immediate.

This is a sandwich, not an unsupported assertion that every coarse
two-interval cover has distance two.

### 2.2 Factorially normalized mass of the full second shell

Set

```text
k=m-10=4N^3-6,                  E=binom(N-1,2).         (2.2)
```

An `O_2` witness extends to one length-ten interval.  A `D_2` witness already
has two disjoint five-windows.  In either case exactly `k` outside factors are
internal to the witness cut, and `k` is even.

For a cut `P`, let `T_P` be the central sum of its `e_P` internal
transpositions and let `h_P=|H_P|`.  For `O_2`, the ten-block product lies in
`H_P`, because the outside factors are internal and the whole product is
identity.  For `D_2`, each five-block product lies in `H_P` by definition.
Centrality therefore combines every outside segment.  At even time,
Cauchy--Schwarz and the frozen M12 direct-product trace estimate give

```text
[g]T_P^k<=[e]T_P^k<=4e_P^k/h_P.                        (2.3)
```

The density hypothesis holds uniformly because `k/e_P>=k/M>=4log(2N)`.

Sum over labeled bipartitions by their smaller side.  Relative to an isolate
cut, whose internal alphabet is `E`, the exact factorial sum is

```text
sum_P e_P^k/h_P
 <=[E^k/(N-1)!]
   sum_{s=1}^{floor(N/2)}
    [binom(N,s)^2/N]
    exp{-k(s-1)(N-s-1)/E}.                             (2.4)
```

The `s=1` contribution is `N`.  For `s>=2`, use

```text
k/E>=8N,       N-s-1>=N/4,
binom(N,s)<=N^s,       log N<=N/2.
```

Each remaining summand is at most `exp[-N^2(s-1)]`, so

```text
sum_P e_P^k/h_P<=2N E^k/(N-1)!.                       (2.5)
```

There are at most `m` ten-windows for `O_2`, at most `m^2` ordered disjoint
five-window pairs for `D_2`, and at most `M^10` block tuples in either case.
Equations (2.1), (2.3), and (2.5) yield

```text
|V^(2)|
 <=|O_2 union D_2|
 <=16N m^2 M^10 E^k/(N-1)!.                           (2.6)
```

For the even global bridge,

```text
|Omega(N,m)|>=2M^m/N!                                 (2.7)
```

by Cauchy--Schwarz on the `m/2`-step parity-coset law.  Since
`E/M=(N-2)/N`,

```text
pi(V^(2))
 <=8N^2m^2(1-2/N)^k
 <=8N^2m^2 exp(-2k/N)
 <=exp(-5N^2)<1/2.                                    (2.8)
```

Here `log(8N^2m^2)<=2N^2` and `2k/N=8N^2-12/N` for `N>=5`.  This proves the
global smaller-side orientation for the actual shell, not merely for `D_2`.

### 2.3 Many tails robust against two deleted windows

Now work on `d=N-1` labels with transposition alphabet size
`E=binom(d,2)`.  At even length `k`, the exact identity-return lower bound is

```text
#{u in T_d^k:product(u)=e}>=2E^k/d!.                   (2.9)
```

Call an identity tail *two-window robust* when deleting the union of any two
intervals, each of length at most five, leaves connected support on `[d]`.

If a tail is not robust, a bipartition of the disconnected remainder has all
crossing occurrences in the two deleted intervals.  If their union has
`u<=10` positions, then for a fixed cut/window pair a deliberately crude
count is

```text
E^u e_P^(k-u)
 <=E^10 [E(1-2/d)]^(k-10).                             (2.10)
```

This discards the endpoint condition and therefore does not require commuting
an arbitrary block through a cut subgroup.  Summing at most `k^2` window
pairs and `2^d` cuts, and dividing by (2.9), bounds the bad fraction by

```text
(1/2)k^2 2^d d! exp[-2(k-10)/d].                       (2.11)
```

Its logarithm is at most `4N^2-7N^2=-3N^2`, so it is less than one half.
Consequently the number `R` of robust identity tails obeys

```text
R>=E^k/(N-1)!.                                         (2.12)
```

In particular, the construction below is nonempty for every `N>=5`.

### 2.4 Explicit second-shell boundary sources

Let

```text
z=N,                 s=(z,1),                 q=(2,3),
B=(s,q,q,q,s).                                          (2.13)
```

Since `s,q` are disjoint, `product(B)=q`.  For every robust identity tail
`u=(b_1,...,b_k)` counted by (2.12), form

```text
y=(B,B,b_1,...,b_k).                                    (2.14)
```

The two prefix products multiply to `q^2=e`, and the tail product is identity,
so `y in Omega(N,m)`.  Across the cut `{z}|[N-1]`, the crossing positions are

```text
1,5,6,10.                                               (2.15)
```

The two disjoint five-block products both equal `q in H_P`; hence
`y in D_2 subset V^(2)`.  Concretely, replacing the second `B` by any internal
length-five factorization of `q` reaches `V^(1)`, and replacing the first
reaches a word with isolated `z` in `V^(0)`.

Apply `H_5` at positions ten through fourteen.  Four right Hurwitz identities

```text
(a,b)->(b,b^{-1}ab)
```

push the last `s` through `b_1,...,b_4`.  The target has its `z`-incident
factors at

```text
1,5,6,14.                                               (2.16)
```

No two intervals of length at most five cover these four positions: one is
needed for position one, one for position fourteen, and neither can also
cover both positions five and six.  More explicitly, an interval covering
`1,5` cannot cover `6`, while an interval covering `5,6` cannot cover `1`;
position `14` is distance at least eight from `6`.

Deleting any two five-windows therefore leaves at least one `z`-edge.  In the
target, the tail factors retain their order with the conjugated `z`-edge
inserted after `b_4`; each global deleted interval removes at most one
contiguous tail interval of length five.  Two-window robustness keeps
`[N-1]` connected, and the surviving `z`-edge attaches `z`.  Thus every
two-window deletion leaves connected full support.  The target is outside
`C_2`, hence outside `V^(2)` by (2.1).

A fixed length-five product fiber has size at most `M^4`.  Including laziness,
block-size choice, scan probability, and exact uniform conditional sampling,
the specified target probability is at least

```text
p=1/[6(m-4)M^4].                                       (2.17)
```

### 2.5 Conductance and complete kernel normalization

For `r=3,4,5`, define

```text
Q_r(V^(2),(V^(2))^c)
 =pi(V^(2))/[6(m-r+1)]
   E_{w|V^(2)}[sum_i H_{i,r}(w,(V^(2))^c)].            (2.18)
```

The lazy identity contributes no boundary flow and

```text
Q_K=Q_3+Q_4+Q_5.                                       (2.19)
```

Retaining only the `R` sources (2.14) and their one specified `H_5` targets,
then dividing by the exact smaller side using (2.6), (2.8), (2.12), and
(2.17), gives

```text
Phi_pm^K(V^(2))
 >=[R/|V^(2)|]p
 >=1/[96N m^2(m-4)M^14].                               (2.20)
```

Finally, `m<=5N^3`, `m-4=4N^3`, and
`M^14<=N^28/2^14`, so the denominator in (2.20) is at most `N^38`.  This
proves (1.4).  All uncharged `Q_3,Q_4,Q_5` transitions are nonnegative.

## 3. Worst probability, runtime, path, and congestion accounting

- Actual-shell mass: at most `exp(-5N^2)`.
- Robust boundary-source count: at least
  `binom(N-1,2)^(m-10)/(N-1)!`.
- Specified original-chain transition: `1/[6(m-4)M^4]`.
- Exact conductance lower bound: first expression in (1.4), hence `N^-38`.
- Every charged transition is one actual `H_5` outcome.  The four displayed
  Hurwitz identities specify that target and do not introduce a four-edge
  comparison path or congestion factor.
- Given a cut and two intervals, the sandwich predicates are checked in
  `O(m)`.  A tail can be checked naively for two-window robustness in
  `O(m^3+Nm^2)`.  No efficient recognition algorithm for the union over all
  cuts is asserted or needed.
- The inherited exact `r<=5` block sampler has polynomial per-step cost.

## 4. Dependencies and statuses

1. **Proved here:** sandwich (2.1), mass bound, robust-tail count, explicit
   boundary surgery, properness, and conductance (1.4).
2. **Proved in M28:** exact first-shell characterization by one localized cut
   interval.
3. **Proved and frozen in Cycle-02 M12:** parity-aware direct-product central
   trace upper bound with the hypotheses checked in (2.3).
4. **Inherited proved:** exact same-product heat-bath reversibility,
   stationarity, and polynomial exact block sampling.
5. **Not used:** conductance monotonicity, macro reachability as probability,
   restriction gaps, finite representatives, canonical paths, length-two
   simulation, or graph-only dynamics.
6. **Empirical dependencies:** none.

## 5. First unproved standalone proposition

> **THIRD FULL-SUPPORT SHELL.**  With (1.1), characterize or sharply sandwich
> `V^(3)`, determine whether it is proper, orient its exact global stationary
> mass, and prove inverse-polynomial conductance or a literal
> superpolynomial-gap obstruction with all `Q_3+Q_4+Q_5` flow included.

No conductance monotonicity from `V^(2)` to `V^(3)` is assumed.

## 6. Strongest self-attack

The theorem uses a sandwich rather than an equality for `V^(2)`.  This is
safe in both directions actually used: the upper sandwich controls the full
shell mass, the boundary sources are explicitly in `D_2 subset V^(2)`, and
their targets lie outside the larger `C_2`.  It does not identify every
distance-two word.

The exponent 38 is crude, and the dense length `4N^3+4` is essential to the
robust-tail count.  More importantly, conductance can decrease after another
shell is added.  The theorem says nothing about `V^(3)`, arbitrary internal
full-support cuts, or the global spectral gap.

## 7. Calibration

- Odd `m`: the bridge is empty; no shell theorem is asserted.
- `m=0` and even `N=2`: singleton regimes.
- `m=2,N>=3`: excluded disconnected chain.
- `S_3,m=4`: 27 words and four macro/Hurwitz classes.  The whole-word `H_4`
  makes the analogous first shell all of `Omega`; no five-window statement is
  extrapolated.
- `S_4,m=4`: 120 words and 13 macro/Hurwitz classes; full support is
  infeasible and the whole-word `H_4` remains present.
- `S_4,m=6`: 3936 words and 17 macro/Hurwitz classes; finite shell behavior is
  not used as asymptotic evidence.
- Near-minimal connected doubled trees need not be robust against two window
  deletions; the theorem counts dense tails only.
- Ordered window locations and subgroup products are essential.  Unordered
  support graphs alone do not define `D_2`.
- No edge/degree parity criterion characterizes identity; parity is used only
  in exact even return counts.
- The boundary transition is an actual `H_5`, not the false `L=2` local
  simulation.
- Global mass orientation precedes conductance division, and the full
  `Q_3+Q_4+Q_5` normalization is explicit.

## 8. Artifacts and reproduction

Owned artifacts:

- `plan.md`
- `checkpoint.md`
- `report.md`

No computation was used.  Reproduce by checking the overlap/separation
sandwich (2.1), factorial cut sum (2.4)--(2.6), crude robust-tail union bound
(2.9)--(2.12), and ordered-product `H_5` surgery (2.13)--(2.20).

Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED

The verdict concerns inverse-polynomial conductance of the literal second
shell, not either global terminal outcome.
