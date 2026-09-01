# M120 halfway checkpoint: uniform two-direction defect drift

Date: 2026-08-12 UTC.

## 1. Scope and exact chain

This checkpoint works only with M113/M118's exact chain `A_d`, for `d>=2`.
Its states are realizable keys

```text
kappa=(j,p,Q_L,Q_R),
```

where the two partitions coarsen the cycles of `p`, their bipartite
cycle-incidence multigraph is connected unicyclic, and
`j=d+|Q_R|-|Q_L|`.  Its stationary law is

```text
rho(kappa)=|C_kappa|/Z_inc,
```

and a compatible adjacent pair has stationary flow

```text
Q_A(kappa,lambda)=|C_kappa intersect C_lambda|/(2 Z_inc).
```

The factor `1/2` is the left/right direction coin; all unused row mass is
held.  Permutations compose as `(p q)(x)=p(q(x))`, with factors multiplying
left-to-right.  The results below do not prove a gap for `A_d` or for the
original heat-bath chain.

## 2. Proved universal singleton-split/reverse rate

Write

```text
h(a)=a^a/(a-1)!.
```

### Nonidentity seam

Suppose `p` is not the identity.  Choose a `p`-cycle `A` of length `a>=2`,
choose `x in A`, and put `t=(x,p^{-1}(x))`.  Then `p'=pt` splits `A` into
the singleton `{x}` and a cycle of length `a-1`.  If the `Q_R` block `B`
containing `A` has `b` labels and contains `s` cycles of `p`, split `B` into
`{x}` and `B\{x}`.  This is M113's valid rightward singleton-split edge.

Put `k=2d-j`.  The exact side-count ratio gives its source transition
probability

```text
A_d(kappa,lambda)
 = 1/(2k) * ((a-1)/a)^a * ((b-1)/b)^(s-3).            (2.1)
```

Indeed the factorial ratio is `1/k`, the atom ratio is
`h(a-1)/h(a)=((a-1)/a)^a`, and only the block `B` changes.  Now `k<=2d`,
`((a-1)/a)^a>=1/4`, and the last factor is at least `1/4`: it is at least
one if `s<=3`, while for `s>=4` one has `s-3<=b` and
`((b-1)/b)^b>=1/4`.  Therefore

```text
A_d(kappa,lambda) >= 1/(64d).                          (2.2)
```

### Identity seam

Now let `p=id` and `d>=3`.  Its incidence multigraph has `d` vertices and
`d` edges.  Some incidence vertex has two incident cycle-edges with distinct
opposite endpoints: otherwise the connected underlying simple graph would
have maximum degree one and hence only two vertices.  Let its label block
have size `b`, and join two corresponding singleton cycles by a
transposition.  According to the color of the block this is a leftward or
rightward valid join, and it is the reverse of a singleton split.  Its exact
source probability is respectively

```text
2/(j b)  or  2/((2d-j)b),                              (2.3)
```

because `h(2)=4`.  Since `j,2d-j<=2d` and `b<=d`, (2.3) is at least
`1/d^2`.

### Uniform conclusion

Thus, for every key of `A_d` and every `d>=3`, the total probability of all
singleton-cycle splits and their reverses is at least

```text
min{1/(64d),1/d^2} >= 1/(64d^2).                      (2.4)
```

This proves M113's explicitly requested weaker precursor.  At `d=2` the
chain has one state and no off-diagonal move, so (2.4) is intentionally not
asserted.

## 3. Proved bidirectional rates for a defect projection

Define the transposition defect

```text
R(kappa)=d-c(p) in {0,...,d-2}.                        (3.1)
```

Every `A_d` edge changes `R` by exactly one.  The split in (2.1) decreases
`R`; hence every state with `R>=1` has downward probability at least
`1/(64d)`.

There is also a polynomial upward move from every state with `R<=d-3`.
Here `c(p)>=3`, so the connected incidence graph has at least three vertices.
As above, one incidence vertex contains two cycle-atoms of lengths `a,b`
having distinct opposite endpoints.  Joining those atoms in the appropriate
cut direction is valid and increases `R`.  If that incidence block has `B`
labels and the relevant side has length `k`, its exact probability is

```text
  h(a+b) / (2 k B h(a)h(b)).                           (3.2)
```

For `n=a+b`,

```text
h(n)/(h(a)h(b))
 = [n/(ab)] / [binom(n,a)(a/n)^a(b/n)^b]
 >= n/(ab) >= 4/n >= 4/d,                             (3.3)
```

because the bracketed denominator in (3.3) is a binomial point probability
and is at most one.  Since `k<=2d` and `B<=d`, (3.2) is at least `1/d^3`.

Consequently the stationary-flow projection `\bar A_d` onto `R` is an exact
birth-death chain satisfying

```text
q_r >= 1/(64d),     1<=r<=d-2,
p_r >= 1/d^3,       0<=r<=d-3.                        (3.4)
```

All levels occur: for each `c=d-r` take a permutation with `c` cycles and a
one-left-vertex incidence unicycle with one doubled right neighbor.

## 4. Why (2.4) and (3.4) are not yet a gap

Uniform local escape is not a Poincare inequality.  Even a birth-death chain
with both directions at least a fixed `delta` can have an exponentially deep
stationary valley.  For example, on `{0,...,2L}`, take right/left rates
`(delta,1/2)` on the left half and `(1/2,delta)` on the right half.  The
stationary masses fall by a factor `2delta` for `L` edges and then rise by
its reciprocal.  Both directional rates are at least `delta`, while the
middle conductance is of order `(2delta)^L`.

For the exact defect masses

```text
mu_r=sum_{R(kappa)=r}rho(kappa),                       (4.1)
```

the exact checks through `d=5` find a unimodal and log-concave sequence, but
this is a finite fact only.  A useful standalone missing statement is:

> **DEFECT NO-VALLEY LEMMA.**  The sequence `(mu_0,...,mu_(d-2))` is
> unimodal for every `d>=3`.

This weak shape assertion is already enough.  If `mu` is unimodal and
`epsilon=min{1/(64d),1/d^3}`, then the path canonical-path bound and (3.4)
give

```text
gap(\bar A_d) >= epsilon/d^2 >= 1/(64d^5).             (4.2)
```

Indeed, at an edge before the mode its lower-prefix mass is at most `d` times
the left endpoint mass; after the mode its upper-tail mass is at most `d`
times the right endpoint mass.  The edge flow is at least `epsilon` times
both endpoint masses, and all path lengths are at most `d`.

Thus (4.2) is CONDITIONAL on the named no-valley lemma, not a proved
projection gap.

## 5. Exact restricted same-level chain

The ordinary restriction of `A_d` to one defect level has no off-diagonal
edges, because every transposition joins or cuts a cycle.  The correct fiber
object is therefore two-step.  Let `P=(I+A_d)/2`, let `Omega_r={R=r}`, and
hold every `P^2` exit from `Omega_r`.  Equivalently, for distinct
`kappa,lambda in Omega_r`, define

```text
Q_(B_r)(kappa,lambda)
 = rho(Omega_r)^(-1)
   sum_eta rho(kappa) P(kappa,eta)P(eta,lambda),        (5.1)
```

with the unused conditional row mass held.  This is reversible for
`rho(.|Omega_r)`.  Its nontrivial edges are the exact down-up and up-down
coagulation/fragmentation moves through an adjacent defect level.

The remaining restricted obligation is:

> **FIXED-DEFECT TWO-STEP GAP.**  Prove
> `min_r gap(B_r)>=d^{-O(1)}`.

One must then apply a precise decomposition/comparison to the lazy squared
chain.  This is a non-hub fiber target; routing all levels through `p=id` or
one extreme incidence key is not used.

## 6. Exact finite audit and current verdict

`incidence_gap_audit.py` independently reconstructs all combinatorial keys,
cell weights, compatible overlaps, stationary flows, canonical formulas,
and sparse spectra.  At `d=2,3,4,5` it finds respectively
`1,9,101,1420` keys and numerical finite gaps
`1,0.1414353635,0.1254163084,0.1121580619`.  It finds zero failures of
(2.1), (2.3), or (3.2); every exact finite rate satisfies the proved coarse
bounds.  The singleton-only skeleton is connected at all four sizes, with
finite numerical gaps `1,0.1414353635,0.1254163084,0.1059080005`.
Balanced, hub-degree, cycle-count, leaf-count, block-size, and cut-level
threshold scans through `d=5` show no finite small-conductance candidate.
These spectra and scans are finite diagnostics, not asymptotic evidence.

Current verdict: **PROMOTE** the universal aggregate singleton/reverse theorem
and bidirectional defect rates; **KEEP OPEN** the defect no-valley lemma and
fixed-defect two-step gap.  No spectral-gap theorem for `A_d`, `beta(d)`, or
the original heat-bath chain is claimed.
