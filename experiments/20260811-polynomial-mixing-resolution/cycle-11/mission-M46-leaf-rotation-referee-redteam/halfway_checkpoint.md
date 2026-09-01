# M46 halfway checkpoint

Date: 2026-08-11.  Convention: `(pq)(x)=p(q(x))`; tuple products are
written left-to-right.  This checkpoint does not claim a result for the full
identity-word chain `K`.

## Frozen M35 referee verdict

**ACCEPT, with no substantive objection.**  I verified the frozen hashes

```text
report.md              1ca18204936040277da472579d0f2070234d94f721d80cdac79e49e078872f65
leaf_rotation_count.md e4e8da1e66caa28f90155cf750aed4e18c6243fdbb39428dff35920a82b46c7d
```

and independently audited the exact theorem.  For every `r>=2`, every
`d in J_r`, and every nonlast leaf child `j` of `i` in the preorder plane
tree of `(d,0)`, put `d'=d-e_i+e_j`.  The nonlazy adjacent-rank-two
heat-bath projection has

```text
Pbar_r(d,d')=2d_i/[3r(r-1)],
Pbar_r(d',d)=2/[3r(r-1)].
```

The audit points are as follows.

1. Deleting the least vertex from a noncrossing tree yields interval
   components.  On any such component `I=[a,b]`, every proper initial
   subinterval `J` has `sum_(h in J)d_h>=|J|`, while
   `sum_(h in I)d_h=|I|-1`.  Thus `b` is the unique first return of the
   Łukasiewicz sum.  The one external attachment in the recursive step has
   lower endpoint outside `I` and does not enter its forward degrees.  This
   closes the induction in M35 Lemma 2.1.
2. Hence every compatible factor tree contains the designated leaf chord
   `(i,j)` and the unique attachment `(i,k)`, `k>j`, of the next child
   interval.  They are consecutive in the incident-edge order.
3. Inserting `(i,j)` immediately after factor `(i,k)` in word order, shifting
   later factor numbers, preserves noncrossing and every
   clockwise-decreasing incident order.  Deletion is its inverse.  The
   number of source-word/scan-position marks is therefore
   `|O_(d^-)|=d_i|O_d|/r`.
4. For `i<j<k`, the same-product fibre of `(i,k)(i,j)` is exactly
   `(i,k)(i,j),(i,j)(j,k),(j,k)(i,k)`.  The last two and only the last two
   change the lower-label multiset by `-e_i+e_j`.  This also proves that all
   favourable scans, not merely a subset, are counted by the marks.
5. Dividing by `|O_d|`, the `r-1` scan sites, and the three fibre outcomes
   gives the forward rate.  Since `pi(d')/pi(d)=d_i` and the projection is
   reversible, the reverse rate is exactly the displayed value.
6. At `r=2`, the star-to-path and reverse rates are respectively `2/3` and
   `1/3`, so the smallest nontrivial boundary is covered.  A last leaf has
   no next child interval and is correctly excluded.

For an independent bounded falsifier, `interval_lemma_audit.py` enumerated
every noncrossing spanning tree through seven vertices and checked every
vertex component decomposition plus 1,628 nonlast-leaf consequences.  It
found no failure.  This finite check supports but does not prove the
universal argument above.

## Weighted leaf-chain red team

Let `L_r` retain all accepted undirected leaf-rotation edges and place unused
probability on the diagonal.  Writing

```text
c_r=2/[3r(r-1)],   w(d)=r!/product_i d_i!,
```

an oriented canonical rotation has forward rate `c_r d_i`, reverse rate
`c_r`, and common unnormalized capacity `c_r w(d)d_i=c_r w(d')`.

Exact graph enumeration through `r=9` found the Catalan state counts and the
edge counts `1,4,15,56,210,792,3003,11440`; every graph was connected.  The
minimum bridge conductance from `r=5` through `r=9` is exactly

```text
4/[57r(r-1)],
```

so bridge cuts do not supply a superpolynomial obstruction.  Cuts by root
first-subtree size and leaf number also had only polynomial-looking finite
flow.  These are falsifiers only.

A sparse symmetric eigensolve through `r=9` used the exact transition
normalization.  The gaps for `r=5,...,9` were approximately

```text
1.018e-3, 2.208e-4, 6.555e-5, 2.242e-5, 8.363e-6.
```

They are numerically close to `380 r^-8`.  This rejects neither polynomial
mixing nor a superpolynomial bottleneck and is not an asymptotic theorem.

## Resource/comparison audit

Fleurat, arXiv:2411.03065v3, Theorems 1 and 4, applies to
`w_k=1/k!` and therefore supplies a size-increasing coupling of the exact
conditioned-Poisson plane-tree laws.  Time reversal supplies the aggregate
deletion balance identity.  Its proof for infinite-support weights uses
truncation/compactness and recursive quantile couplings; it gives no
polynomial pointwise lower bound or congestion estimate.

There is also a move mismatch with Caraceni--Stauffer.  In Dyck notation,
their right leaf translation swaps the local steps `UDU -> UUD`.  The exact
M35 rotation across a next sibling excursion `P` is `UD P -> U P D`.
These agree only when `P=UD`.  Thus neither the uniform-plane-tree gap nor
its canonical paths transfer by a stationary reweighting.

## Current first unproved step

> **QUANTITATIVE WEIGHTED ROTATION COMPARISON.**  There are universal
> constants `c,C>0` such that for every `r>=2`, the reversible chain `L_r`
> above has `gap(L_r)>=c r^-C`; equivalently, it suffices to route every
> adjacent-value ideal edge through leaf rotations with polynomial path
> length and total stationary-flow congestion, using no fixed exponentially
> rare hub.

This result would still be an auxiliary minimal-sector projection theorem,
not Terminal A.  Conversely, a superpolynomial cut for `L_r` would not by
itself imply Terminal B for the original chain `K`.

## Reproduction

```text
python3 interval_lemma_audit.py --n-max 7 --output interval_lemma_n7.json
python3 leaf_chain_bridge_probe.py --r-min 2 --r-max 9 --output bridge_results_r9.json
python3 leaf_chain_spectral_probe.py --r-min 2 --r-max 9 --output spectral_results_r9.json
```

