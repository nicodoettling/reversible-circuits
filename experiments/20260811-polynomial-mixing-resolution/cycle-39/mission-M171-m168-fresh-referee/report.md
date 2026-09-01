# M171 fresh immutable referee report on frozen M168

Date: 2026-08-13. Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
ACCEPT M168'S STRICT EXACT FIXED-CELL PHASE-COLLAPSE/SCALAR REDUCTION.
MATERIAL NUMBERED OBJECTIONS: ZERO.
NONMATERIAL NUMBERED OBJECTIONS: ONE.
FCL1: UNRESOLVED.
```

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
The accepted target is only M73's nonlazy cyclic rank-two quotient under the
uniform minimal long-cycle factorization law, for `n=3k`, odd `k>=3`, at
M168's balanced sources and first separated physical cell.  No broader
kernel conclusion is audited or inferred.

## 2. Frozen provenance

The four supplied hashes independently match:

| M168 artifact | observed SHA-256 |
|---|---|
| `report.md` | `97357d9a31d5ebb13e41a790c0ff3cf8a82720a7f6e7e57b5a2ec44d3dedf83a` |
| `phase_collapse_reduction.md` | `ea6667b8c679ce6fa342c43abbd6dc633cc586b4d972ff5333c28f212c489714` |
| `freeze_manifest.md` | `32e62aba79103a298eb19050f916dc1a359c671cdeaa1c1744c156dcec7b92f0` |
| `SHA256SUMS` | `3f86fc364d1809752d06085eddad8b2e75132ea03c1d27d5a87e9ec3b1cb84bd` |

Moreover, `sha256sum -c SHA256SUMS` passes all eight M168 payload entries.
M168 and all predecessor directories remained immutable during this audit.

## 3. Generic-edge iff, component counts, and `(PC)`

For `q=s^{-1}h` and `E_r=(r,r+1)`, one has identically

```text
s(r+1)=r+1  iff  q(r)=r+1.
```

For each supported intermediate, the explicit residual cycles complete the
iff: in an oriented triangle, the three support-head boundary edges connect
the three cyclic-gap cycles pairwise; in either noncrossing double color,
each of the four support-head edges connects its single-gap cycle to the
combined-gap cycle.  Every other boundary edge is the displayed directed
edge of one residual cycle.  Thus a boundary edge is internal, and can split
`q`, exactly when it is generic.

The lags `2,...,n-2` enumerate every ordered pair of disjoint polygon edges
once.  Within component `i`, the `g_i(g_i-1)` ordered distinct generic pairs
lose exactly two orientations for each of the `a_i` adjacent unordered
pairs, giving

```text
g_i(g_i-1)-2a_i.
```

Across components `i<j`, either component can supply the first edge, giving
`2g_i g_j`.  Two disjoint directed cycle edges isolate their two tails.
Consequently the remaining cycle sizes are exactly

```text
(1,1,d_i-2)                         within one component,
(1,d_i-1,1,d_j-1)                  across two components,
```

with untouched components retained.  Nonzero same-component terms partition
into `IS/IN`, and cross-component terms are `X`.  The outer sum still ranges
over every triangle/double intermediate with lift multiplicity `3/2` and
keeps the two source contributions signed until after summation.  This proves
M168's `(PC)` as stated.

## 4. `(PCS)`, orbit normalization, and physical factor `1/2`

The raw first row contributes

```text
a(s)[C_B(s)/A_B-C_A(s)/A_A].
```

For the second row, every boundary-double target has raw lift two, hence its
phase sum contributes `2S(s)/A_s`.  Its constant quotient mass is

```text
pi_y=2nF_T/n^(n-2).
```

Dividing by `pi_y` cancels only the target lift two and leaves
`n^(n-2)/(nF_T)`, exactly the prefactor in `(PCS)`; the intermediate lift
`a(s)` remains.  This independently confirms the full normalization.

The involution `y -> n-2-y` has no fixed point because `n` is odd, and it
identifies precisely the two edge orderings of each physical orbit.  Thus
every physical orbit occurs twice in the colored list and

```text
Delta_k(C_k)=(pi_y/2) sum_y z_k(y).
```

The factor `1/2` is necessary and correct.

## 5. `(TV-close)`, `(NEG-id)`, `(SC)`, and quantifiers

For every real sequence of length `N`, its mean lies in its range and the
range is at most its path variation `V`; therefore

```text
sum_i |x_i| <= |sum_i x_i| + N V(x).
```

With `x_y=Z_k(y)=kz_k(y)` and `N=3k-3`, this becomes

```text
sum_y |Z_k(y)|
 <= k|sum_y z_k(y)|+(3k-3)k sum_y|z_k(y+1)-z_k(y)|.
```

Hence the two uniform estimates in `(SC)` are sufficient, with the required
factor `k^2` in the finite-difference estimate.  Both estimates remain open
uniformly over odd `k>=3`.

For `P_k=sum_y(z_k(y))_+` and `N_k=sum_y(-z_k(y))_+`, direct algebra gives,
for every such `k`,

```text
sum_y|Z_k(y)|
 =k|sum_y z_k(y)|+2k min(P_k,N_k).
```

Thus the signed-sum bound plus a uniform minority-mass bound is sufficient;
one sign within each `k` is stronger.  Neither condition is proved.

## 6. Independent exact reconstruction, capped at `k=3,5`

The clean-room checker imports no M168 code.  It reconstructs rank-two
products and their lift multiplicities from literal ordered pairs of distinct
transpositions, evaluates the raw two-step convolution, and consults frozen
M168 output only after obtaining its results.

| check | `k=3` | `k=5` |
|---|---:|---:|
| supported states | 336 | 3,185 |
| generic-edge iff checks | 3,024 | 47,775 |
| ordered disjoint-pair/support checks | 18,144 | 573,300 |
| nonzero completion-size checks | 5,670 | 308,880 |
| distinct physical cell orbits | 3 | 6 |

All component-count, completion-size, `IS/IN/X`, `(PC)`, `(PCS)`, and
physical-factor assertions pass exactly.  The reconstructed signed sums are

```text
k=3: 7345139916497931/7061881225000000

k=5: 73077925347453973355779108467047756359425607682995598110051
     /150223593265440401176815963858761531101584168449901928120320
```

They match frozen M168 exactly.  This is exact finite calibration only; the
audit intentionally stopped at `k=5`.

## 7. Numbered objections and status ledger

1. **Nonmaterial: unretained `k=9` exact-sign provenance.**  M168 reports a
   separate exact `k=9` positivity check, but its frozen bundle retains only
   the floating `k=9` phase-sum row and does not identify a machine-readable
   exact `k=9` output or its exact command.  M171 therefore does not audit
   that exact-sign diagnostic.  It remains finite-only and is used in no
   accepted proof or asymptotic inference.

Material objections: **none**.

```text
generic-edge iff and ordered component counts              proved
completion-size phase collapse and full topology retention proved
(PCS) normalization and physical factor 1/2                proved
(TV-close), (NEG-id), and sufficiency of (SC)               proved
clean-room k=3,5 phase sums                                 exact finite facts
k=9 positivity report                                      finite only; unaudited provenance
(PCS-bound), (FD-bound), and FCL1                           unresolved
```

## 8. Artifacts, command, reproducibility, hashes, and hygiene

The stable retained command is

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-39/mission-M171-m168-fresh-referee/run_cleanroom_audit.py \
  --frozen-m168 experiments/20260811-polynomial-mixing-resolution/cycle-38/mission-M168-fixed-cell-fcl1/signed_cell_sum_results.json
```

Python `3.12.3`; standard library only; deterministic; `seed=null`; exact
scope `k=3,5`.  The immutable predecessor hash gate was run both before the
audit and immediately before freeze.  M171 changed only files under its owned
directory.  Final payload hashes are recorded in `SHA256SUMS` and
`freeze_manifest.md`.

## 9. Final action

**ACCEPT AND FREEZE M168'S STRICT EXACT PHASE-COLLAPSE/SCALAR REDUCTION WITH
ZERO MATERIAL OBJECTIONS AND ONE NONMATERIAL FINITE-PROVENANCE OBJECTION.
KEEP BOTH UNIFORM SCALAR BOUNDS AND FCL1 OPEN.**

