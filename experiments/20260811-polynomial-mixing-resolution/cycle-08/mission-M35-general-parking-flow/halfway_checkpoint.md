# M35 halfway checkpoint

Date: 2026-08-11.  Convention: `(pq)(x)=p(q(x))`; factor tuples
multiply left-to-right.

## 1. Ideal-chain audit: ACCEPT

The frozen M36 theorem survives independent audit.

- Its tight-prefix proof verifies the symmetric exchange axiom for
  `J_r`: a deficit to the left is paid for by one unit of `y`-slack and a
  deficit to the right by one unit of `x`-slack.
- Branden--Huh Theorem 3.10 and Proposition 3.1 apply to the homogeneous
  normalized M-convex enumerator and its polarization.
- A clone subset of occupancy `m` has weight
  `product_i (r-m_i)!/r!`; summing over its
  `product_i binom(r,m_i)` clone fiber gives exactly `1/m!`.
- After deletion to `eta`, the aggregate add weight of type `j` is
  `(r-eta_j)(r-eta_j-1)!` times the common remaining factors, hence is
  independent of `j`.  The projected destination is uniform over feasible
  types, every positive off-diagonal rate is at least `r^-2`, and the
  quotient gap is at least `1/r`.

No objection was found.  This does not compare the ideal chain to the
actual parking projection.

## 2. A rigorous length-two capacity obstruction

Put `r=a+b+1`, with `a>=2,b>=1`, and define

```text
x     = 0^a 1 2^b,
y     = 0^a 2^(b+1),
delta = 0^(a+1) 2^b,
zeta  = 0^(a-1) 1 2^(b+1).
```

The ideal M36 chain has the positive edge `x->y`.  The actual adjacent
rank-two projection has no direct `x-y` edge.  Moreover, every nontrivial
actual path of length two from `x` to `y` has middle macro exactly `delta`
or `zeta`.

The two unavoidable rare edges have exact favorable raw-outcome counts

```text
R(delta,y)=2(b+1),       R(x,zeta)=2(a-1).             (2.1)
```

Here a favorable raw outcome includes the selected adjacent scan position
and one of the two nonspecial outcomes in its three-state interval.  If
`T=(r+1)^(r-1)` is the Dénes count, their stationary capacities are

```text
Q(delta,y)=2(b+1)/[3(r-1)T],
Q(x,zeta)=2(a-1)/[3(r-1)T].                            (2.2)
```

The source orbit has size

```text
|O_x|=r!/(a!b!)=r binom(r-1,a).
```

Since `D_r(x,y)>=r^-2`, every fractional routing of the ideal demand
`pi(x)D_r(x,y)` by actual paths of length at most two has congestion at
least

```text
  3(r-1)|O_x|/[2r^3].                                  (2.3)
```

For balanced `a,b`, (2.3) is exponential.  Thus universal two-hop
inverse-polynomial-capacity simulation is rigorously refuted.  This does
not refute polynomial paths of length `O(r)`.

### Proof of the path classification

Every macro-changing rank-two edge joins a special macro containing two
copies of a lower label `i` to the macro obtained by replacing one `i` by
some `j>i`.  Decomposing the root `e_2-e_1` into two unit-exchange roots
shows that an intermediate between `x` and `y` must be either
`x-e_1+e_k` or `x-e_k+e_2`.  For `k>=3`, the first kind would require
`x_1>=2`, but `x_1=1`; its only nontrivial feasible case is `k=0`, namely
`delta`.  The second kind uses a type present in `x`; apart from endpoints,
only `k=0` gives `zeta`.

### Proof of the rare counts

A move replacing a zero label by a two label must start with the special
pair `(0,k),(0,2)`, `k>2`.  For `delta`, containing `(0,2)` forces the
unique noncrossing threshold tree

```text
(0,1),(0,2),
(2,j), 3<=j<=b+2,
(0,j), b+3<=j<=r.
```

The Goulden--Yong incident-edge order puts the large zero edges in
decreasing order before `(0,2)`, the two edges in decreasing order after
it, and leaves `(0,1)` free to occupy one of `b+1` slots after `(0,2)`.
The pair `(0,b+3),(0,2)` is adjacent in every such extension.  Both
nonspecial interval states have macro `y`, giving `2(b+1)`.

For `x`, containing `(0,2)` forces `(1,2)` and excludes `(0,1)`:
if `(0,1)` were present, the unique one-edge either closes a triangle or
crosses `(0,2)`; an edge `(1,k)` with `k>2` also crosses `(0,2)`.  The
unique threshold tree is therefore

```text
(1,2),(0,2),
(2,j), 3<=j<=b+2,
(0,j), b+3<=j<=r.
```

The singleton `(1,2)` can occupy `a` slots among the `a-1` large zero
edges before `(0,2)`.  Exactly the final slot separates
`(0,b+3)` from `(0,2)`, leaving `a-1` favorable extensions.  Again both
nonspecial outcomes have macro `zeta`, giving `2(a-1)`.  These local-order
claims use Goulden--Yong, JCTA 98 (2002), Theorem 2.2, Proposition 2.4,
and Lemma 2.5 in the convention already checked in M27.

## 3. Computation and broader correction

The corrected Stanley inverse and exact rank-two fibers pass through
`n=8`: Dénes counts, endpoint products, labels, and detailed balance all
agree.  The adjacent-value ideal subgraph happens to have actual distance
at most two through this range, but this must not be extrapolated.
Coordinator artifact M39 finds arbitrary M36 ideal edges of distance three
already at `n=6` and distance four at `n=8`.

The Anand--Feng--Freifeld--Guo--Jerrum--Wang SoCG 2025 comparison remains
a template, not a transfer.  Their states are uniformly weighted
noncrossing spanning trees and their elementary flips need not be triangle
slides between consecutive Goulden--Yong factor edges.  Here the raw-tree
marginal is weighted by compatible edge orders, and the exact macro states
are ordinary parking multiplicities rather than their 2-Dyck state space.

## 4. Exact frontier

The smallest surviving proposition is:

> **GENERAL PARKING-MULTISET FLOW.**  Route every positive M36 ideal edge
> through the actual parking projection with path length `r^O(1)` and
> total stationary-flow congestion `r^O(1)`, using longer buffer paths and
> a recoverable fractional encoding.

Finite widest paths through `n=8` are consistent with this proposition but
cannot prove it.  The length-two obstruction proves that any successful
argument must genuinely use growing paths or an aggregate functional
inequality.
