# M41 halfway checkpoint

Date: 2026-08-11. Convention: `(pq)(x)=p(q(x))`, with factor
products read left to right.

## 1. The ideal-to-adjacent reduction is accepted

I independently rederived M35's comparison. Moving the same deleted unit
one label at a time keeps every intermediate parking vector feasible:
rightward feasibility is exactly the endpoint prefix slack, and leftward
moves only increase affected prefixes. Along a route,
`pi(x)/pi(x^(k))<=r`. A directed adjacent edge plus metadata `(i,j)`
recovers the source; there are at most `r^2` metadata choices, length at
most `r`, and adjacent ideal capacity at least `pi(z)/r^2`. Thus

    E_D<=r^6 E_A,
    gap(A_r)>=r^-7.

The remaining theorem is only the comparison of `A_r` with the actual
parking projection.

## 2. Exact simultaneous-load audit

The exact harness reconstructs every Stanley noncrossing chain, every
rank-two fiber, and both projected stationary flows through `n=8`. It
checks Dénes counts, orbit sizes, endpoints, labels, feasibility, and exact
detailed balance.

Choosing one deterministic capacity-maximizing path independently for every
adjacent-value ideal commodity gives:

| `r` | maximum path length | minimum individual capacity ratio | total comparison congestion |
|---:|---:|---:|---:|
| 2 | 1 | `4/3` | `3/4` |
| 3 | 2 | `1/2` | `3` |
| 4 | 7 | `1/3` | `243/8` |
| 5 | 11 | `1/4` | `452/5` |
| 6 | 18 | `1/5` | `5125/24` |
| 7 | 27 | `1/6` | `13913/14` |

The individual ratio `1/(r-1)` pattern and the finite congestion values
are nonproof.

## 3. Two explicit buffer templates

For the M35 warning family

    x=0^a 1 2^b,  y=0^a 2^(b+1),

the following fan route is positive in every exact case:

1. replace `b-1` copies of 2 successively by `3,...,b+1`;
2. perform `1->0` and then `0->2`;
3. collapse `3,...,b+1` back to 2.

Its length is `2b`. At `r=7`, the minimum capacity/ideal-flow ratios for
`(a,b)=(2,4),(3,3),(4,2),(5,1)` are respectively
`7/9,7/9,28/45,7/27`. A universal count proof is still missing.

A shorter borrow--move--return template treats a right adjacent move
`i->i+1`. Prefix slack guarantees some duplicated `h<=i`. For each
candidate `h`, try

    x -> x-e_h+e_i
      -> x-e_h+e_(i+1)
      -> x-e_i+e_(i+1),

with the obvious direct simplification when `h=i`, and reverse the path
for a left move. At least one candidate is a positive actual path for every
exact commodity through `r=7`. Selecting the best candidate gives:

| `r` | missing commodities | maximum length | minimum capacity ratio | total congestion |
|---:|---:|---:|---:|---:|
| 2 | 0 | 1 | `4/3` | `3/4` |
| 3 | 0 | 3 | `1/2` | 5 |
| 4 | 0 | 3 | `8/27` | `81/8` |
| 5 | 0 | 3 | `5/36` | `108/5` |
| 6 | 0 | 3 | `2/25` | `75/2` |
| 7 | 0 | 3 | `7/180` | `405/7` |

The minimum-ratio pattern is deceptive. At `r=7` the worst commodity is

    0^4 1^3 -> 0^3 1^4.

This is M32's balanced binary direct edge. Its actual capacity divided by
ideal flow is asymptotically exponential, even though the finite values look
small-polynomial. M32 supplies a high-label two-hop bypass for precisely
this family. Therefore the duplicate-buffer template alone is refuted as a
polynomial-capacity comparison.

## 4. Exact frontier

The surviving standalone proposition is:

> **HIGH-BUFFER ADJACENT PARKING FLOW.** For every positive adjacent-value
> ideal commodity, choose or fractionally spread over duplicate-buffer,
> high-label, and fan routes so that path length and total stationary-flow
> congestion are bounded by `r^O(1)`.

A useful sufficient lemma would assign each commodity a compatible high
buffer whenever every duplicate-buffer candidate is capacity-poor, while
making the source recoverable from a used edge and only polynomial metadata.
Finite widest paths do not prove this lemma.

## 5. Artifacts and reproduction

- Plan: `plan.md`
- Exact harness: `exact_widest_congestion.py`
- Machine-readable result: `results.json`
- Commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python 3.12.3, standard library only, no randomness.

Run:

    python3 experiments/20260811-polynomial-mixing-resolution/cycle-09/mission-M41-adjacent-parking-flow/exact_widest_congestion.py --n-max 8 --output experiments/20260811-polynomial-mixing-resolution/cycle-09/mission-M41-adjacent-parking-flow/results.json

Verdict: **OPEN AT A NAMED STEP: HIGH-BUFFER ADJACENT PARKING FLOW.**

## 6. Exact Cayley lift and a rejected literature transfer

Append a terminal zero to a parking multiplicity vector

    d=(d_0,...,d_(r-1),0),

so that `sum_i d_i=r` and the parking prefix inequalities are exactly the
Lukasiewicz conditions.  There is a unique rooted plane tree on `r+1`
preorder positions having outdegree sequence `d`.  Its parking-macro mass is

    pi(d)=r!/[ (r+1)^(r-1) product_i d_i! ].           (6.1)

This law has the following exact Cayley representation.  Take a uniform
tree on the labelled vertex set `{0,...,r}`, root it at `0`, order the
children of every vertex by increasing numerical label, and then forget the
labels after recording the preorder outdegrees.  The resulting degree
sequence has law (6.1).

Indeed, fix the plane shape with preorder degrees `d` and keep label `0` at
the root.  Assigning labels `1,...,r` to the remaining preorder positions
recovers this shape after child-sorting exactly when labels increase inside
each sibling group.  The sibling groups partition the nonroot positions, so
exactly

    r!/product_i d_i!

assignments work.  Summing over all `d` gives Cayley's
`(r+1)^(r-1)` rooted-at-zero trees and proves (6.1) without an enumerative
parking-function input.

This also shows why Caraceni--Stauffer, *Probab. Theory Relat. Fields* 176
(2020), Theorems 3--4, do not directly prove the parking projection gap.
Their leaf-replanting and leaf-translation chains are reversible for the
uniform law on plane trees.  Our law is the simply-generated/conditioned
Poisson(1) law proportional to `product_i 1/d_i!`; for the star and path
shapes its weight ratio is `r!`.  Thus there is no polynomial pointwise
density comparison, and their local move is not the same as the
sibling-subtree rotation seen in the exact parking projection.  The Cayley
lift remains a useful prospective randomized comparison, but a
stationary-flow-preserving simulation is still required.

For a sibling-subtree rotation that changes
`d -> d-e_p+e_j` with `d_j=0`, the exact weight ratio is

    pi(d-e_p+e_j)/pi(d)=d_p.                           (6.2)

Consequently the empirically identified forward/reverse projected rates
`2d_p/[3r(r-1)]` and `2/[3r(r-1)]` have exactly the required detailed-balance
ratio.  Equation (6.2) proves only the normalization check, not the universal
transition-count formula or a gap bound.

## 7. Polynomial gap for a weighted leaf-replanting chain

The aggregate deletion balance from Fleurat is sufficient for a weighted
version of the Caraceni--Stauffer randomized-path argument; no pointwise
lower bound on the deletion kernel is needed. This closes the weighted
pivot/load issue, though not the comparison to the exact parking rotations.

Let `T_r` be the rooted plane trees with `r` edges, with the root vertex
fixed throughout, and put

```text
omega(t)=product_v 1/d_v(t)!,
Z_r=(r+1)^(r-1)/r!,
pi_r(t)=omega(t)/Z_r.
```

Fleurat, arXiv:2411.03065v3, Theorem 4, applied to `w_k=1/k!`, gives growth
kernels supported on adding a right-leaning leaf. Time reversal gives
deletion kernels `f_r:T_r x T_(r-1)->[0,1]` supported on deleting a leaf and
satisfying

```text
sum_s f_r(t,s)=1,
sum_t pi_r(t) f_r(t,s)=pi_(r-1)(s).                  (7.1)
```

Define `Y_r` as follows. Two different rooted plane trees are replanting
neighbors if one is obtained from the other by deleting a nonroot leaf and
reinserting it in an arbitrary ordered child slot, without changing the root.
For every such unordered pair set

```text
Y_r(t,t')=(4r^2)^(-1) min(1,pi_r(t')/pi_r(t)),       (7.2)
```

and put the remaining mass on the diagonal. There are at most
`r(2r-1)<2r^2` replanting proposals, so (7.2) defines a lazy reversible
chain with stationary law `pi_r` and polynomial per-step implementation.

**Theorem 7.1.** For every `r>=1`, with the singleton convention at `r=1`,

```text
gap(Y_r) >= 1/[16(r+1)^8].                           (7.3)
```

**Proof.** Write `N=r+1`; the comparison source is the one-step global
`pi_r` heat bath, whose gap is one. For each ordered pair `x,y in T_r`,
independently sample a pivot `z~pi_(r-1)`. Starting from `x`, use a deletion
trajectory with kernels (7.1). In reverse, use an independent deletion trajectory from
`z` to reinsert those leaves into the first-child subtree of the root. This
gives `r` leaf-replanting moves from `x` to the unique tree whose first-child
subtree is `z` and whose remaining root tree is a singleton. Concatenate
the time reversal of an independent construction from `y`. The two deletion
histories conditioned on `z` are independent but share that same pivot, so
the two halves meet. Null replant steps are suppressed. Every resulting path
has length at most `2r`.

At a first-half time `i`, `1<=i<=r`, let `L(t)` be the first-child subtree of
the current tree and let `R(t)` be the rooted tree left after deleting that
subtree and its root edge. Then `|L(t)|=i-1` and `|R(t)|=r-i`. Summing the
path demand `pi_r(x)pi_r(y)` over the endpoints, pivot, and unused deletion
trajectory, (7.1) gives the exact marginal load

```text
pi_(i-1)(L(t)) pi_(r-i)(R(t)).                       (7.4)
```

The second half is identical, and the endpoint load is simply `pi_r(t)`.
If the root degree of `t` is `k`, product weights factor as

```text
omega(t)=omega(L(t))omega(R(t))/k.
```

Put `a=i`, `b=N-i`. Therefore the ratio of (7.4) to `pi_r(t)` is

```text
k Z_r/[Z_(a-1)Z_(b-1)]
 = k ab/[N p_(N,a)],                                 (7.5)
```

where

```text
p_(N,a)=binom(N,a)(a/N)^a(b/N)^b
```

is the probability that a `Bin(N,a/N)` variable equals its mean. Standard
Stirling bounds give `p_(N,a)>=1/(3 sqrt(N))`, uniformly for
`1<=a<=N-1`. Since `k<=N` and `ab<=N^2/4`, (7.5) is at most
`(3/4)N^(5/2)<=N^3`. Thus, at every one of the at most `2N` path times, the
total endpoint-weighted probability of occupying `t` is at most
`N^3 pi_r(t)`.

A root-preserving leaf replant from a parent of degree `u>=1` to a different
parent of degree `v` changes the weight by the exact ratio `u/(v+1)`; a
same-parent reorder has ratio one. Consequently every replanting neighbor
satisfies

```text
N^(-1) <= pi_r(t')/pi_r(t) <= N,
Q_Y(t,t') >= pi_r(t)/(4N^3).                         (7.6)
```

For a fixed directed edge, summing over all path times and then multiplying
by the path length bounds its canonical demand by

```text
(2N)(2N)N^3 pi_r(t)=4N^5 pi_r(t).
```

Dividing by (7.6) gives congestion at most `16N^8`, proving (7.3). The
argument uses only the aggregate identity (7.1), so compactness-small
individual entries in Fleurat's kernel cause no loss.

The new standalone frontier is therefore:

> **WEIGHTED REPLANTING-TO-ROTATION FLOW.** Route every edge of `Y_r`
> through the exact leaf rotations of (1.3), with path length and total
> stationary-flow congestion bounded by `r^O(1)`.

This proposition would prove a polynomial gap for the leaf-rotation chain.
It is not automatic: a Caraceni--Stauffer leaf translation is a different
Dyck move when the following sibling subtree is nontrivial, and the balanced
binary examples already rule out uniform short-route capacity.

## 8. Exact mass of the maximum-degree separator

The new comb--path energy-barrier candidate has an exact stationary-mass
reduction.  If `D>=1`, then

```text
pi_r(max_i d_i>=D)<=(r+1)(e/D)^D.                    (8.1)
```

Indeed, append `d_r=0` and put `a_i=d_i-1`.  The cycle lemma gives a unique
cyclic shift with all proper partial sums nonnegative for every weak
composition of `r` into `r+1` parts.  Since the total increment is `-1`,
no such composition is periodic under a nontrivial shift.  The law `pi_r`
is therefore the Vervaat/cycle-lemma image of the multinomial occupancy law
of `r` independent balls in `r+1` boxes.  Maximum occupancy is invariant
under cyclic shift.  This representation already includes the fixed-root
size bias visible in the Cayley model: the root marginal is
`1+Bin(r-1,1/(r+1))`, but the rotation-invariant maximum has exactly the
`r`-ball occupancy law above.  A union bound and the standard binomial upper
tail give

```text
Pr(max_i d_i>=D)
 <=(r+1)Pr(Bin(r,1/(r+1))>=D)
 <=(r+1)(e/D)^D,
```

proving (8.1).  In particular, for

```text
D_r=2+ceil(log_2(r-1)),
```

the right side is superpolynomially small: for every fixed `C`, it is
`o(r^-C)`.

This turns the proposed reversible-pebbling invariant into a precise cut
criterion.  Let `R_D={d:max_i d_i>=D}`.  If a union `A` of connected
components of the induced leaf-rotation graph on `R_D^c` has both
`pi_r(A)>=r^-C_0` and `pi_r(A^c)>=r^-C_0`, then every `L_r` edge leaving
`A` enters `R_D`, so reversibility gives

```text
Q_L(A,A^c)<=pi_r(R_D),
gap(L_r)<=pi_r(R_D)/[pi_r(A)pi_r(A^c)].               (8.2)
```

At `D=D_r`, (8.1)--(8.2) would make `gap(L_r)` superpolynomially small and
would refute every polynomial-congestion comparison from the accepted
replanting chain.  What remains unproved is the two-part separator theorem:
the comb and path must lie in distinct components of `R_(D_r)^c` for all
`r`, and two unions of those components must have inverse-polynomial mass.
Even that auxiliary slowdown would not be Terminal B unless the separator
survives all other actual parking-projection moves and then the full
`H_3,H_4,H_5` identity chain.

## 9. Reconciliation and an exact root-degree projection gap

M48 has now completed the separator proposed in Section 8.  Ordered root
branch prefix sums project every low-degree leaf rotation to the persistent
reversible-pebble game on a path.  The empty configuration and the sink
singleton need `ceil(log_2(r-1))+1` pebbles, whereas maximum degree
`D_r=2+ceil(log_2(r-1))` permits only `D_r-2`.  Root-unary trees and
root composition `(r-1,1)` give the two constant-mass sides.  Consequently
the exact leaf-rotation chain `L_r` has superpolynomially small gap, and
the weighted replanting-to-`L_r` comparison proposed in Section 7 is
refuted.

This separator does not lift to the full projection.  On the low-degree
`(r-1,1)` reservoir, `d_0=2`, and the aggregate identity (1.2) gives

```text
sum_(j>0) Pbar_r(d,d-e_0+e_j)=4/[3r(r-1)].
```

Every target is root-unary and stays below the degree barrier.  Thus the
full projected heat bath crosses the separator with inverse-polynomial
stationary flow.

The same calculation proves a reusable positive theorem.  Let `K=d_0` be
the root outdegree.  Under `pi_r`,

```text
K-1 has law Bin(r-1,1/(r+1)).                         (9.1)
```

Indeed M35 identifies `pi_r` as the child-sorted pushforward of a uniform
rooted Cayley tree on `r+1` vertices, and the Prufer code contains the
fixed root a `Bin(r-1,1/(r+1))` number of times.

For every real `f` and `F(d)=f(d_0)`, the full projected Dirichlet form
contains all root-lowering aggregate transitions.  Reversibility lets one
sum each such undirected edge in its lowering orientation, giving

```text
E_Pbar(F,F)
 >=sum_(k=2)^r Pr(K=k)
      [2k(k-1)/(3r(r-1))] [f(k)-f(k-1)]^2.           (9.2)
```

Put `n=r-1`, `p=1/(r+1)`, and compare (9.2) to the random-scan heat
bath on `n` independent Bernoulli-`p` variables, projected onto their
sum `B=K-1`.  Its downward rate from `b` is
`b(1-p)/n`, and its exact gap is `1/n`.  For every `b>=1`,

```text
[2(b+1)b/(3r(r-1))]/[b(1-p)/n]
 =2(b+1)(r+1)/(3r^2)
 >=4(r+1)/(3r^2).                                    (9.3)
```

Therefore

```text
Var_pi(f(d_0))
 <=[3r^2(r-1)/(4(r+1))] E_Pbar(f(d_0),f(d_0)).       (9.4)
```

Equivalently, the exact stationary-flow projection of `Pbar_r` onto root
degree has gap at least

```text
4(r+1)/[3r^2(r-1)].                                  (9.5)
```

At `r=2`, (9.5) equals one and matches the exact two-state root-degree
chain.  The result controls only root-degree observables.  The new standalone
gap is a recursive restriction theorem for fixed root degree and ordered
branch data; without it, (9.5) is not a gap bound for the full parking
projection.

## 10. A polynomial-gap Cayley basis-exchange source chain

Section 6 gives an exact lift of `pi_r` to the uniform law on labelled trees
on `{0,...,r}`, rooted at `0`: order every vertex's children by label, take
preorder outdegrees, and then forget the labels.  This lift supplies a sharper
ideal comparison chain than the parking-multiset down-up walk.

Let `U_r` be the uniform spanning-tree down-up chain on the complete graph
`K_(r+1)`.  From a tree `T`, delete one of its `r` edges uniformly.  If the
two resulting vertex sets have sizes `a` and `r+1-a`, add uniformly one of
the `a(r+1-a)` complete-graph edges crossing the cut, including the deleted
edge.  Thus `U_r` is reversible for the uniform Cayley-tree law and is
implementable in time polynomial in `r`.

The spanning trees are the bases of the rank-`r` graphic matroid of
`K_(r+1)`.  Its multiaffine basis generating polynomial is strongly log
concave.  Applying the same checked normalization of
Anari--Liu--Oveis Gharan--Vinzant, *Log-Concave Polynomials II*, Theorem 1.1,
used in M36 gives

```text
gap(U_r) >= 1/r.                                    (10.1)
```

Let `C_r` be the exact stationary-flow projection of `U_r` under the
child-sort/preorder-degree map from Section 6.  Its stationary law is exactly
`pi_r`.  For every function `f` on parking degree sequences, the lift of `f`
to labelled trees has the same variance, and its `U_r` Dirichlet form equals
the `C_r` Dirichlet form by the definition of stationary-flow projection.
Consequently

```text
gap(C_r) >= gap(U_r) >= 1/r.                        (10.2)
```

This theorem is unconditional and has polynomial per-step cost.  It is not
yet a gap theorem for the actual projected rank-two heat bath `Pbar_r`.
Deleting and replacing one labelled Cayley-tree edge can reorder a
macroscopic collection of child-sorted preorder positions, so neither a
bounded-length local simulation nor a pointwise transition domination is
being asserted.  The precise remaining implication is:

> **CAYLEY-EXCHANGE-TO-PARKING FLOW.** Construct a stationary fractional
> comparison from `C_r` to `Pbar_r` with congestion polynomial in `r`, or
> refute this comparison by an explicit stationary-flow obstruction.

Together with the exact full-branch root-composition quotient now under M50
audit, (10.2) identifies a natural randomized source whose stationary law is
already correct and avoids routing through a rare plane-tree hub.

## 11. Stationary path lengths sharpen the root-composition gap

M50 proves the following exact root-composition quotient of `Pbar_r`.  To
avoid collision with the Cayley projection `C_r` in Section 10, call it
`G_r` here.  Its states are ordered compositions
`a=(a_1,...,a_k)` of `r`, with

```text
rho_r(a)=Z_r^(-1)(k!)^(-1) product_i w_(a_i),
w_A=A^(A-1)/A!,
alpha_r=2/[3r(r-1)].                                (11.1)
```

Merging either fixed adjacent pair has rate `alpha_r k`; the reverse rate
is fixed by detailed balance.  M50's left-merge canonical path to the
one-part state gave a gap of order `r^-3` after charging every path its worst
possible length.  The exact stationary root-degree law removes that loss.

**Theorem 11.1.**  Subject only to the exact quotient formulas (11.1), which
M50 proves combinatorially and which are under independent audit,

```text
gap(G_r) >= alpha_r/(3e)
         =2/[9e r(r-1)],   r>=2.                    (11.2)
```

**Proof.**  From a composition `x`, repeatedly merge the first two parts to
the hub `(r)`.  Route every ordered pair through the two corresponding hub
paths, retaining repeated undirected edges if the two halves overlap.  Put
`h(x)=number_of_parts(x)-1`.  Under `rho_r`,

```text
E h=(r-1)/(r+1)<1,                                  (11.3)
```

because root degree minus one has law
`Bin(r-1,1/(r+1))`.

Fix a directed merge edge with refined endpoint

```text
s=(A,c_2,...,c_k),   k>=2.
```

Its source basin consists exactly of
`(b_1,...,b_p,c_2,...,c_k)`, where the first `p` parts sum to `A`.  With

```text
C_(A,p)=sum_(b_1+...+b_p=A) product_i w_(b_i),
```

Lagrange inversion and the root decomposition give

```text
sum_p C_(A,p)/p!=Z_A,
Z_A/w_A=(1+1/A)^(A-1)<=e.                            (11.4)
```

M50's basin calculation gives `rho(B_s)<=e rho(s)`.  The corresponding
first moment of the hub-path length is exactly

```text
M_s:=sum_(x in B_s) rho(x)h(x)
 =rho(s) [k!/w_A]
    sum_p [(p+k-2)C_(A,p)/(p+k-1)!].                (11.5)
```

For every `p>=1,k>=2`,

```text
k!(p+k-2)/(p+k-1)! <= k/p!,                         (11.6)
```

since (11.6) is equivalent to
`p+k-2<=binom(p+k-1,p)`.  Equations (11.4)--(11.6) imply

```text
M_s<=e k rho(s).                                    (11.7)
```

For the one-step global `rho_r` heat bath, an ordered pair `(x,y)` carries
demand `rho(x)rho(y)` and path length `h(x)+h(y)`.  The edge occurs in the
first half precisely when `x in B_s` and in the second half precisely when
`y in B_s`.  Counting both occurrences, its total length-weighted load is

```text
2[M_s+rho(B_s) E h]
 <=2e(k+1)rho(s)
 <=3e k rho(s).                                     (11.8)
```

The exact stationary capacity of this merge edge is
`rho(s)alpha_r k`.  Therefore every edge has congestion at most
`3e/alpha_r`, and comparison with the gap-one global heat bath proves
(11.2).  At `r=2`, the exact two-state quotient has rates `2/3,1/3`, so the
bound is valid with slack.  QED

The gain is structural: the one-part hub has constant mass and the number
of root branches has bounded stationary mean, so no rare canonical plane
tree is being used.  This still does not prove the full `Pbar_r` gap.  The
remaining `BALANCED ROOT MEAN-LIFT` must transfer fiber means to the actual
crossing Dirichlet form without multiplying a polynomial density loss at
every recursive depth.

## 12. Bounded right-spine split falsifier

The obstruction in the root mean lift is the law inside a reverse merge.
For a source plane tree whose root has one child, a reverse root split into
ordered branch sizes `(A,B)` is not stationary inside the target root-
composition fiber.  A bounded exact probe tests a sharper geometric support
statement:

> **RIGHT-SPINE SPLIT SUPPORT.**  For every unary-root plane tree of size
> `r+1`, the actual parking projection has a positive reverse root split
> with ordered sizes `(r-B,B)` if and only if `B` is the size of a proper
> suffix subtree rooted on the rightmost child spine below the unique root
> child.

This proposition is **unresolved** universally.  The exact enumerator agrees
with it for every unary-root macro through `r=7`: the numbers of macros for
`n=r+1=3,...,8` are respectively

```text
1, 2, 5, 14, 42, 132,
```

and every recorded positive split has the asserted suffix size while every
such suffix appears.  There are no support failures in the bounded range.
This is a falsification check only; finite agreement is not a proof.

The transition weights also show why support alone is insufficient.  In the
four-edge path macro `[0,1,2,3]`, the three split rates divided by
`alpha_r=2/[3r(r-1)]` are `1/3,1/2,1`, whereas other macros with the same
possible sizes have different weights (for example `[0,1,1,3]` gives
`2/3,1`).  A usable theorem therefore needs the exact marked right-spine
multiplicity or a weighted Poincare inequality on the span of these suffix-
cut indicators, not just a support characterization.

Artifacts:

```text
spine_split_probe.py
spine_split_results.json
```

Reproduction command from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-09/mission-M41-adjacent-parking-flow/spine_split_probe.py \
  --n-max 8 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-09/mission-M41-adjacent-parking-flow/spine_split_results.json
```

The script records commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`,
Python `3.12.3`, exact rational rates, the project multiplication convention,
and the finite-scope warning.  Its universal named gap is **RIGHT-SPINE SPLIT
FORMULA**: prove the support statement above together with a polynomially
controlled exact multiplicity formula strong enough to make reverse-split
bias costs add across recursive levels.

### 12.1 Correction: the support statement is universal

The preceding finite status is superseded for support, but not for rates.
The independently accepted M50 child-boundary lemma proves the universal
RIGHT-SPINE SPLIT SUPPORT statement directly.

Indeed, suppose a unary-root macro `y` has a positive split to a two-branch
macro `x` with ordered sizes `(r-B,B)`.  By reversibility, the reverse
transition `x -> y` is positive.  M50 Lemma 2.1 classifies every upward
transition: it merges the unique root-child boundary by attaching the second
branch at a vertex on the right spine of the first branch.  In `y`, the root
edge of the former second branch is therefore a last-child edge on that
spine, and its descendant subtree has size `B`.

Conversely, let a unary-root tree contain such a right-spine last-child edge
whose descendant subtree has size `B`.  Cut that edge and attach its
descendant subtree to the root immediately after the residual branch.  This
produces a valid two-branch plane tree `x`.  Reattaching the second branch at
the cut vertex is one of the positive child-boundary outcomes in M50 Lemma
2.1, so `x -> y` and hence `y -> x` are positive.  Subtree sizes strictly
decrease down a spine, so a specified `B` determines at most one such edge
and one macro target.

The exact bounded table independently calibrates this proof and already
refutes a size-only rate formula: unary macros `[0,1,1,1]` and
`[0,1,1,3]` both have a `(3,1)` split at `r=4`, but their reverse split
rates are respectively `alpha_r` and `(2/3)alpha_r`.  Thus the remaining
standalone proposition is not support.  It is **SPINE-BIAS H-INVERSE
BOUND**: represent the shape-dependent right-spine split density as a
polynomial-energy divergence (or prove an equivalent weighted Poincare
bound) so that its correction cost is additive across the recursive root
decomposition.  Individual split probabilities need not have a polynomial
lower bound.

## 13. Exact prefix-product fibers are uniformly leaky

This section records a separate original-chain anti-bottleneck theorem. Put

```text
M=binom(N,2),   B=|R_m|,
Z_(N,j)(g)=#{(s_1,...,s_j) in T_N^j:s_1...s_j=g}.
```

For `1<=k<=m-1` and `h in S_N`, define

```text
A_(k,h)={w in Omega(N,m):t_1...t_k=h}.
```

**Theorem 13.1.** For every `N>=3`, even `m>=4`, and every nonempty
`A_(k,h)`, the exact lazy `{3,4,5}` heat-bath chain satisfies

```text
K(w,A_(k,h)^c) >= 1/[2B(m-2)M^3]       for every w in A_(k,h),

Q(A_(k,h),A_(k,h)^c)/pi(A_(k,h))
    >= 1/[2B(m-2)M^3],

Phi_pm(A_(k,h)) >= 1/[2B(m-2)M^3].      (13.1)
```

Here `Phi_pm(A)=Q(A,A^c)/min(pi(A),pi(A^c))`. In particular, no fixed
prefix endpoint sector is a global bottleneck, irrespective of its mass or
of the mixing behavior conditional on that endpoint.

**Proof.** Write the factors in the selected three-window as transpositions
`a,b,c`. If `k=1`, use the window starting at position one. When `a!=b`, the
same-product replacement

```text
(a,b,c) -> (b,bab,c)
```

changes the first factor, because `bab` is a transposition and
`b(bab)c=abc`. When `a=b`, choose any transposition `d!=a` and use

```text
(a,a,c) -> (d,d,c).
```

This again has the same ordered product and changes the first factor.

If `k>=2`, use the window at positions `k-1,k,k+1`. When `b!=c`, use

```text
(a,b,c) -> (a,c,cbc).
```

Its product is `ac(cbc)=abc`, while the old and new length-`k` prefixes are
respectively `Pab` and `Pac`, where `P=t_1...t_(k-2)`; equality would force
`b=c`. When `b=c`, choose a transposition `d!=b` and use

```text
(a,b,b) -> (a,d,d).
```

The triple product remains `a`, and the length-`k` prefix changes from
`Pab` to `Pad`. These windows exist also at `k=m-1`. The assumption `N>=3`
gives at least three transpositions, so the required `d` always exists.

Thus every `w in A_(k,h)` has a specified state outside the fiber among the
outcomes of one legal `H_(i,3)` update. The chain chooses that window with
coefficient `1/[2B(m-2)]`. Its exact same-product length-three fiber has at
most `M^3` words, so the specified outcome has conditional probability at
least `M^-3`. This proves the pointwise bound in (13.1). Summing against
`pi` proves the stationary-flow bound. Since
`min(pi(A),pi(A^c))<=pi(A)`, it also proves the two-sided conductance bound;
the constructed exit shows that every nonempty fiber is proper. The `H_4`,
`H_5`, and holding contributions are retained as nonnegative terms. QED

For completeness, the exact stationary mass is

```text
pi(A_(k,h))
 = Z_(N,k)(h) Z_(N,m-k)(h^(-1)) / Z_(N,m)(id).       (13.2)
```

No orientation or asymptotic estimate for (13.2) is used. The witness is a
single actual transition, has path length one and no congestion, and can be
constructed with polynomial group-operation cost. Boundary cases `k=1`,
`k=m-1`, `m=4`, and `N=3` are included; the whole-word `H_4` term at `m=4`
is not discarded from the chain.

The theorem rejects a direct embedding of a slow arbitrary-endpoint bridge
as a global prefix-fiber cut. A prefix-based obstruction would have to
absorb a growing collection of endpoint values while simultaneously
controlling both its stationary mass and all crossing `H_3` flow.

## 14. Exact refutation of contextual quotient absorption

M65 proves the closed contextual conditional-mean formula in
`cycle-14/mission-M65-contextual-quotient-absorption/closed_mean_formula.md`.
That formula turns the scalar absorption conjecture from Section 5 of M56
into an explicit weighted-composition inequality.  The inequality is false
on an infinite family.

Fix local rank `s=2`, contextual suffix size `B=1`, outer root degree
`K>=1`, and put every other outer branch to the right of the split branch,
so `R=K-1`.  The two inner root compositions, their stationary masses, and
the normalized root-composition transition rates are

```text
C              rho(C)       (-G/alpha) off-diagonal rate
(2)              2/3                     1
(1,1)            1/3                     2.
```

Thus the unique nonconstant eigenvalue of `-G/alpha` is `3`.  M65's exact
formula gives the normalized conditional mean

```text
q(2)=K/(K+1),             q(1,1)=2/(K+1),
E q=2/3.                                                   (14.1)
```

Consequently

```text
||q-Eq||_(-1,-G/alpha)^2
 =Var_rho(q)/3
 =2(K-2)^2/[27(K+1)^2],                                  (14.2)

E[q 1_(last part=B)]=2/[3(K+1)].                          (14.3)
```

The ratio of (14.2) to (14.3) is

```text
(K-2)^2/[9(K+1)],                                         (14.4)
```

which exceeds one exactly for every integer `K>=14`.  Restoring the common
factor `alpha_s` on both sides proves an exact counterexample to
CONTEXTUAL QUOTIENT ABSORPTION as stated in M56.  This is a scoped
refutation inside the auxiliary parking projection, not a slow mode or a
Terminal-B result for the identity chain.

The marked recurrence coefficient itself is

```text
delta=K/(K+1),
a=(K-2)^2/[9(K+1)^2],
delta+a -> 10/9.                                          (14.5)
```

Here the only deep local state recurses from rank two to the singleton rank
one chain, so (14.5) does not by itself make the recursive energy grow.  A
correct replacement must absorb terminal low-rank costs separately and
control products only along genuinely continuing ranks.  It cannot use the
pointwise inequality `a<=1-delta`.

The deterministic formula-based falsifier
`contextual_absorption_formula_probe.py` independently constructs the exact
root-composition generator and solves its symmetrized `H^{-1}` problem.
It finds the first failure at `(s,B,K,R)=(2,1,14,13)` and, assuming M65's
now-proved formula, no numerical inconsistency in the generator symmetry.
The exhaustive output through local rank nine and `K<=100`, plus a targeted
rightmost-suffix output through rank thirteen at `K=100000`, are:

```text
contextual-absorption-formula-r9-k16.json
contextual-absorption-formula-r9-k100.json
contextual-absorption-rightmost-r13-k100000.json
```

Those larger-rank values are finite diagnostics only.  The exact theorem is
the symbolic two-state calculation (14.1)--(14.5).  The next standalone
proposition is **TERMINAL-AWARE CONTEXTUAL RECURRENCE**: reorganize M56's
marked network so that a coefficient larger than one is paid only when the
active contextual rank strictly continues, with a summable total excess,
then prove actual-edge marked source recovery.

### 14.1 Correction: deep recursion is not the ordinary `R=0` family

The geometric last-branch statement does not identify the recursively
inherited observable with the unweighted contextual statistic having
parameters `(K',R')=(k,0)`.  M65's exact `context_map_audit.py` refutes that
shape-level scalar map first at ambient rank four.  For the parent context
`K=1,R=0`, coarse split `(4)->(3,1)`, inner composition `(3)`, and `B=1`,
the two last-branch local macros have parent values `1/3,1/3`.  The natural
ordinary child context `(3)->(2,1)` has values `1,1/2`; multiplying by the
closed-mean factor `D=1/2` predicts `1/2,1/4`, not the parent values.

Thus only the **conditional mean** collapses to the closed formula.  The
recursive fine observable retains a positional/history mark.  The exact
absorption refutation (14.1)--(14.5) is unchanged, but the proposed repair
by proving ordinary `R=0` absorption is insufficient.  The corrected next
step is **MARKED CONTEXT INHERITANCE**: identify the minimal positional mark,
derive its closed transition under last-branch recursion, and prove a
terminal-aware energy bound on that marked family before source recovery.
The `R=0` numerical file remains a diagnostic for only the unmarked
subfamily and is not evidence for the corrected recursion.
