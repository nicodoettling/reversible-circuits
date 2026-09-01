# M35 final report: general parking-multiset flow

Date: 2026-08-11.  Frozen bundle version 1.  Permutations compose as
`(pq)(x)=p(q(x))`; factor tuples multiply left-to-right.

## 1. Exact claim, quantifiers, and convention

Let `r>=1`, let

```text
J_r={m in N^r: sum_i m_i=r and sum_(i=0)^k m_i>=k+1 for 0<=k<r},
pi_r(m) proportional to 1/product_i m_i!,
```

and let `bar P_r` be the stationary-flow projection of the **nonlazy**
uniform scan of the `r-1` adjacent exact rank-two heat baths on minimal
transposition factorizations of `(0 1 ... r)`.

The full requested comparison remains open.  The following scoped claims
are proved.

1. The M36 Lorentzian down-up chain `D_r` on `J_r` has the audited gap
   `gap(D_r)>=1/r`, stationary law `pi_r`, and every positive off-diagonal
   transition is at least `r^-2`.
2. If `A_r` retains only adjacent-value (`|i-j|=1`) off-diagonal moves of
   `D_r`, rejecting the other exits, then

   ```text
   gap(A_r)>=r^-7.                                      (1.1)
   ```

3. Universal two-hop polynomial-capacity comparison of `D_r` with
   `bar P_r` is false.  The family `0^a 1 2^b -> 0^a 2^(b+1)` has an
   exponential two-hop congestion lower bound when `a,b` are balanced.
4. The exact aggregate actual departure from a duplicated value is

   ```text
   sum_(j>h) bar P_r(m,m-e_h+e_j)
      =2m_h(m_h-1)/[3r(r-1)].                          (1.2)
   ```

5. Append `m_r=0` and view `m` as the preorder degree vector of its unique
   plane tree.  If `j` is a nonlast leaf child of `i`, then the leaf
   rotation `m^rot=m-e_i+e_j` is an actual projected edge and

   ```text
   bar P_r(m,m^rot)=2m_i/[3r(r-1)].                    (1.3)
   ```

   Its stationary capacity is `pi_r(m)` times (1.3).  This claim is
   universal in `r`; its proof is combinatorial, not an extrapolation from
   finite enumeration.
6. The law `pi_r` is the pushforward of the uniform rooted Cayley-tree law
   under numeric-child sorting followed by preorder degree projection.
   Leaf rotation lifts injectively to a labeled subtree slide, with exact
   per-lifted-edge conductance

   ```text
   2m_i/[3r(r-1)(r+1)^(r-1)].                          (1.4)
   ```

The singleton `r=1` convention is `gap=1`.  The original identity bridge,
its laziness, and its `{3,4,5}` scan are outside this scoped minimal-sector
projection theorem; no Terminal-A or Terminal-B conclusion is claimed.

## 2. Full proof or construction

### 2.1 Ideal and adjacent-value chains

The M36 support `J_r` satisfies symmetric exchange: for a coordinate with
`x_i>y_i`, a nearest deficit to its right can be paid from a unit of
`x`-prefix slack; if none exists, the last crossing to the left has the
corresponding `y`-slack.  Branden--Huh Theorem 3.10 applied to the
normalized homogeneous M-convex enumerator, followed by polarization,
gives a clone down-up chain with gap at least `1/r`.  A clone subset of
occupancy `m` has aggregate mass `1/m!`; after deletion, clone
multiplicities cancel, so the destination type is uniform among feasible
types and every positive rate is at least `r^-2`.  This independently
audits M36.

For a `D_r` edge `x -> x-e_i+e_j`, move the unit through consecutive values.
If `i<j`, all intermediate vectors `x-e_i+e_k` are feasible because the
endpoint feasibility supplies one unit of prefix slack on `[i,j)`.  If
`j<i`, all changed prefixes only increase.  The path has length at most
`r`.  Along it, `pi(x)/pi(z)<=r`.  A used directed adjacent edge together
with metadata `(i,j)` recovers the unique source; there are at most `r^2`
metadata values.  Since an `A_r` edge has capacity at least `pi(z)/r^2`,
the standard path load is at most `r^6` times its capacity.  Hence
`E_D<=r^6 E_A`, proving (1.1).  The fully expanded calculation is in
`adjacent_reduction.md`.

### 2.2 Exact failure of two-hop routing

For `r=a+b+1`, `a>=2,b>=1`, put

```text
x=0^a 1 2^b,  y=0^a 2^(b+1),
delta=0^(a+1)2^b,  zeta=0^(a-1)1 2^(b+1).
```

Root decomposition shows every nontrivial actual two-hop path from `x` to
`y` uses `delta` or `zeta`.  Goulden--Yong compatible-edge orders give
exact favorable outcome counts `2(b+1)` on `delta-y` and `2(a-1)` on
`x-zeta`.  With `T=(r+1)^(r-1)`, the corresponding capacities are those
counts divided by `3(r-1)T`.  Since

```text
|O_x|=r!/(a!b!)=r binom(r-1,a),   D_r(x,y)>=r^-2,
```

every length-two fractional routing has congestion at least
`3(r-1)|O_x|/(2r^3)`, exponential for balanced `a,b`.  See
`halfway_checkpoint.md` for the complete path classification and order
count.

### 2.3 Aggregate flow and leaf rotations

Conditional on macro `m`, Biane's lower-sequence bijection makes the raw
factorization uniform over the `r!/product m_h!` permutations of its
parking multiset.  At a fixed scan position, equal lower labels `h,h`
occur with probability `(m_h)_2/(r)_2`; two of the three decompositions of
the resulting 3-cycle replace one `h` by a larger label.  This proves
(1.2), including the scan and three-state-fibre normalization.

For the sharper leaf edge, `leaf_rotation_count.md` proves a deterministic
interval-component lemma for every noncrossing factor tree.  It identifies
the canonical plane-tree child intervals from the forward-degree vector.
Thus the designated leaf chord `(i,j)` and the attachment `(i,k)` of its
next sibling component occur in every source tree and are consecutive in
the incident-edge order.  Deleting the leaf factor from a *word-consecutive*
marked pair and closing vertex/factor labels is bijective with the smaller
orbit; conversely insert `(i,j)` immediately after `(i,k)`.  The
Goulden--Yong clockwise-decreasing inequalities are preserved.  Therefore

```text
#marked=(r-1)!/[(m_i-1)! product_(h!=i,j)m_h!]
       =m_i|O_m|/r.
```

Each mark has two favorable states among its three decompositions.  The
uniform `r-1` scan gives (1.3), with denominator `3r(r-1)` exactly.

Finally, sorting the children of a rooted Cayley tree numerically imposes
disjoint sibling chains of lengths `m_i` on its `r` nonroot labels.  Their
linear-extension count is `r!/product m_i!`, proving the pushforward.
Sliding the next sibling-subtree root below the leaf preserves preorder
labels and injects the source fiber into the target fiber.  Dividing (1.3)
over the source Cayley fiber proves (1.4).

### 2.4 New weighted-growth resource audit

Fleurat, arXiv:2411.03065v3, Theorem 4 applies exactly to `w_k=1/k!`:
`SG^w_(r+1)=pi_r`, and the hypotheses `w_0w_1>0`, no internal zeros, and
log-concavity all hold.  Reversing its right-leaning-leaf growth kernel
gives deletion kernels `D_r^del` satisfying

```text
sum_s D_r^del(t,s)=1,
sum_t pi_r(t)D_r^del(t,s)=pi_(r-1)(s).                (2.1)
```

This is exactly the weighted deletion-balance identity analogous to
Caraceni--Stauffer Proposition 5.1.  It is useful for a fractional path
construction because weighted column sums can telescope.  It does not yet
give the desired comparison: for infinite-support weights Fleurat's proof
passes through truncation and compactness, and supplies no polynomial
pointwise transition bound; more importantly, the uniform
Caraceni--Stauffer pivot/load count is not automatically valid under
`1/product m_i!`.  The precise audit is in `fleurat_audit.md`.

## 3. Probability, runtime, path, and congestion accounting

- `D_r` positive off-diagonal rate: at least `r^-2`; `gap(D_r)>=r^-1`.
- Canonical `D_r`-to-`A_r` path length: at most `r-1`; stationary-density
  ratio along a path: at most `r`; source recovery metadata: at most `r^2`;
  comparison congestion: at most `r^6`; hence `gap(A_r)>=r^-7`.
- Actual rank-two scan: `r-1` scan sites and a three-state nontrivial
  conditional fibre.  All favorable counts convert to capacities by
  division by `3(r-1)T`, `T=(r+1)^(r-1)`.
- Leaf-rotation transition and capacity are exactly (1.3); no `O(1)`
  normalization is suppressed.
- The exact falsification scripts enumerate all minimal long-cycle
  factorizations, so their runtime and output are exponential in `r`; they
  are bounded falsifiers only.  The universal leaf theorem and adjacent
  reduction are proof-based and have polynomial constructive operations.
- No polynomial congestion has been proved from `A_r` to `bar P_r`.

## 4. Dependencies, labeled

- **Proved here:** adjacent-value reduction and `r^-7` gap; two-hop
  obstruction; aggregate departure identity; interval-component lemma;
  leaf contraction/insertion bijection; exact leaf-rotation count; Cayley
  pushforward and lifted conductance.
- **Cited and convention-checked:** Goulden--Yong, JCTA 98 (2002),
  Theorem 2.2(f1)--(f3), Proposition 2.4, Lemma 2.5; Stanley, EJC 4(2)
  (1997), Theorem 3.1 and Proposition 4.1; Biane, EJC 9 (2002), Theorem
  3.1.  The one-based/right-action to zero-based/left-to-right translation
  is the one independently accepted for M27 and is restated in
  `leaf_rotation_count.md`.
- **Cited, independently audited:** Branden--Huh, Theorem 3.10 and the
  polarization/down-up consequence used in M36.
- **Cited, applicable but quantitatively incomplete:** Fleurat,
  arXiv:2411.03065v3, Theorems 1 and 4; Caraceni--Stauffer, Proposition
  5.1 and their uniform-plane-tree leaf-translation comparison.
- **Template only, not transferred:** Anand--Feng--Freifeld--Guo--Jerrum--
  Wang, arXiv:2409.07892 / SoCG 2025, Lemmas 15--18.  Their uniform NCST
  law and flip moves do not preserve the present compatible-order weights.
- **Empirical exact only:** enumerations through the sizes listed in field
  7.  They falsify stronger statements but prove no asymptotic theorem.

## 5. First unproved standalone proposition

> **ADJACENT-VALUE PARKING FLOW.**  There is a universal constant `C` such
> that for every `r>=2` and every directed off-diagonal edge `(x,y)` of
> `A_r`, one can assign a probability distribution on `bar P_r` paths
> from `x` to `y`, each of length at most `r^C`, for which every directed
> actual edge `e` satisfies
>
> ```text
> sum_(x,y) pi_r(x)A_r(x,y)
>   E[ |gamma_xy| 1{e in gamma_xy} ]
>     <= r^C pi_r(e^-)bar P_r(e^-,e^+).
> ```

By (1.1), this proposition would give an inverse-polynomial gap for the
parking macro projection.  A sufficient replacement is an
inverse-polynomial gap for the exact leaf-rotation chain together with a
polynomial comparison from `A_r` to leaf rotations.  Fleurat (2.1) is a
candidate aggregate-flow input, not a proof of this proposition.

## 6. Strongest self-attack

The exact leaf-rotation formula controls only rotations at nonlast leaf
children.  It does not show that the resulting weighted graph has a
polynomial gap, nor that arbitrary adjacent-value ideal demand can be
spread among such edges without concentrating on a small-capacity arch.
The balanced binary example already shows that a seemingly natural short
route can have exponentially weak relative capacity.  Likewise, the
uniform Cayley lift is only a stationary-measure representation: a
polynomial gap for an unrestricted Prüfer-coordinate or edge-slide chain
does not transfer until each move is routed through the restricted,
preorder-compatible slides with recoverable polynomial load.  Finally,
Fleurat's existence kernel can contain extremely small entries; only its
aggregate balance may safely be used without a new quantitative proof.

## 7. Calibration results

- `r=1`: singleton macro, gap convention one.
- Exact raw counts, endpoint products, Stanley--Biane labels, rank-two
  fibres, and detailed balance pass through `n=r+1<=8` in the corrected
  harnesses.
- The leaf count, contraction map, and insertion inverse pass exhaustively
  through `n<=7`; these checks are falsifiers, while the theorem is proved
  for all `r`.
- The stronger fixed-prefix/suffix witness claim fails at `n=5`; the claim
  that the predecessor is always `(i,j+1)` also fails at `n=5`.
- For `r=7`, `0^4 1^3 -> 0^3 1^4` has exact actual capacity `1/(9T)` and
  ideal lower-bound capacity `35/(49T)`, ratio `7/45`; this checks the
  corrected `3(r-1)` normalization and prevents misuse of aggregate (1.2).
- The two-hop obstruction handles rare labels and balanced multiplicities.
  General M36 edges require actual graph distance 3 by `n=6` and 4 by
  `n=8` (coordinator M39), so no distance-two extrapolation is made.
- Original-chain calibrations (`S_3,m=4`, `S_4,m=4`, `S_4,m=6`, whole-word
  `H_4`, odd/empty and `m=2` exclusions) are not contradicted: this report
  concerns only the minimal long-cycle projection and makes no full-`K`
  claim.

## 8. Artifacts and reproduction commands

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-08/
  mission-M35-general-parking-flow/
```

Core proof notes are `adjacent_reduction.md`, `halfway_checkpoint.md`,
`aggregate_departure.md`, `leaf_rotation_count.md`, and
`fleurat_audit.md`.  Exact falsifier commands (Python standard library)
are:

```text
python3 adjacent_bypass_probe.py --n-max 6 --output adjacent_bypass_n6.json
python3 adjacent_bypass_probe.py --n-max 8 --dump-edges --output adjacent_bypass_edges_n8.json
python3 borrow_move_probe.py --input adjacent_bypass_edges_n8.json --output borrow_move_n8.json
python3 boundary_block_probe.py --n 7 --output boundary_block_n7.json
python3 leaf_rotation_probe.py --n 5 --output leaf_rotation_n5.json
python3 leaf_contraction_audit.py --n 7 --output leaf_contraction_n7.json
python3 leaf_insertion_probe.py --n 7 --output leaf_insertion_n7.json
```

All computations are exhaustive and deterministic, so no random seed is
used.  The scripts record their parameters and machine-readable results;
finite success is not used as universal proof.

## 9. Verdict

**OPEN AT A NAMED STEP: ADJACENT-VALUE PARKING FLOW.**

