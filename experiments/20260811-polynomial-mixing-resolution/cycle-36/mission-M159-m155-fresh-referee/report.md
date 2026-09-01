# M159 fresh referee report on frozen M155

Date: 2026-08-13. Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision and exact scope

```text
ACCEPT M155'S STRICT BOUNDARY-CONDENSATE REDUCTION.
MATERIAL NUMBERED OBJECTIONS: ZERO.
```

For `n=3k`, odd `k>=3`, this accepts the exact separated-color
disintegration of the complete signed two-step score, its product-critical-
Borel boundary limit, the `(2/pi)log D+O(1)` truncated minimum moment, and
the conditional `(BLM)` and `(UBL)` consequences.  It also accepts
`(BCL-sharp)` as an exact positive reformulation and `(BCL-log)` as the
weaker balanced-family target.

The accepted target is only the uniform minimal length-`n-1`
factorization law of the odd long cycle and M73's nonlazy cyclic rank-two
quotient kernel.  This is not the identity-word law or the lazy `{3,4,5}`
heat-bath chain.  The audit accepts no score lower bound, direct L1 theorem,
general strict-edge estimate, H0 theorem, bridge or identity-chain gap, or
Terminal conclusion.

## 2. Frozen provenance

All assigned SHA-256 values independently match:

| M155 artifact | observed SHA-256 |
|---|---|
| `report.md` | `1d8d6061aff3c9dc3f7811dbe15be4deb9c17c0e29ada6fb27fa6e9125ee8d2f` |
| `boundary_condensate_reduction.md` | `ee0092cbf553a4ed317d409f7c99fbd8850a23ebcc12bd3f836aec4a0821850a` |
| `boundary_condensate_check.py` | `99262179be2586618165cfcf1ca605d8d18eb6387b728609d5299b4b8fcaadcf` |
| `boundary_condensate_results.json` | `65104f7890dd6c9f37f73cff256a84d7491b820c1799817084c0f86d5e0d1438` |
| `freeze_manifest.md` | `3861fb6894e48b7c3481a38164e7d939434ef706469267230e847e7ce5a87e24` |
| `SHA256SUMS` | `d85240d4a643ae217386403f737eee62f85fe313c97b511da79f6e4993b56383` |

No frozen or predecessor artifact was modified.

## 3. Orbit and colored-encoding audit

Permutations compose as `(pq)(x)=p(q(x))`, and tuple factors multiply
left-to-right.  For odd `n`, every supported double transposition has a
free orbit under conjugation by the long cycle.  Indeed, a rotational
stabilizer has odd order and hence cannot interchange the two edges; if it
fixes each edge setwise, its odd-order action cannot interchange either
edge's endpoints, forcing a nonidentity rotation to fix a vertex.  This is
impossible.

At its four cyclic support anchors, each double orbit has four colored
positive-composition encodings: two separated and two nested.  For a
separated encoding `(x,y,z,w;S)`, the residual cycle sizes are
`(x,z,y+w)` and the orbit mass is

```text
2n(n-3)! tau(x)tau(z)tau(y+w)/n^(n-2).
```

Giving an encoding one quarter of that mass and fixing
`x=a,z=b,c=y+w` gives a `y`-independent value.  Summing
`1<=y<=c-1` yields exactly

```text
W_n(a,b)=(c-1) Gamma_n b_a b_b b_c/2.
```

For any nonnegative orbit function `f`, the separated encoding sum counts
each orbit twice at quarter mass, so it is exactly
`(1/2) E[f 1_D]`.  Taking `f=k^2|z_k|` proves the factor two in

```text
k^2 E[|z_k|1_D]=2 sum_(a,b) W_n(a,b)A_k(a,b).
```

This argument also explains why duplicated colored appearances are required
rather than a stabilizer error.

The independent standard-library checker imports no M155 or predecessor
code.  It enumerates the raw products, cyclic orbits, and all four encodings
at `n=9,15`.  Exact `Fraction` results are:

| `n` | raw doubles | quotient orbits | S encodings | N encodings | double mass | separated quarter-mass |
|---:|---:|---:|---:|---:|---:|---:|
| 9 | 252 | 28 | 56 | 56 | `2/3` | `1/3` |
| 15 | 2730 | 182 | 364 | 364 | `4/5` | `2/5` |

Every orbit has size `n`; every positive four-composition occurs once in
each color; every individual `W_n(a,b)` agrees exactly; and a separate
nonconstant orbit function verifies the factor-two identity exactly.

## 4. Product-Borel condensation

With `b_r=e^-r r^(r-1)/r!`, the tree-function identity at `e^-1` gives
`sum_r b_r=1`.  Stirling gives

```text
Gamma_n~sqrt(2 pi n),
b_(n-a-b)~(2 pi)^(-1/2)(n-a-b)^(-3/2).
```

Thus for each fixed `a,b`, `(c-1)Gamma_n b_c/2 ->1/2`, proving
`W_n(a,b)->b_a b_b/2`.  The exact colored count gives total mass
`sum W_n=(n-3)/(2n)->1/2`.  Pointwise convergence of nonnegative masses
plus convergence of their totals is precisely the countable Scheffe
argument, so the normalized laws converge in total variation to two
independent critical-Borel variables.  No unproved uniform bound on
`W_n/(b_ab_b)` is used.

## 5. Logarithmic threshold

Layer cake gives exactly

```text
H_D=sum_(r=1)^D (sum_(j=r)^D b_j)^2.
```

The uniform truncated-tail expansion is

```text
sum_(j=r)^D b_j
 =sqrt(2/pi)(r^(-1/2)-D^(-1/2))
  +O(r^(-3/2)+D^(-3/2)).
```

After squaring and summing, the first square contributes
`(2/pi)sum_(r<=D)1/r`.  The mixed
`D^-1/2 sum r^-1/2` term and the `D^-1 sum 1` term are both bounded;
all remainder cross-products are summable uniformly.  Therefore

```text
H_D=(2/pi)log D+O(1).
```

The coefficient and the handling of the truncated upper tail in M155 are
correct.

## 6. Conditional quantifiers and finite-truncation logic

`(BLM)` requires one common `lambda>0` and a liminf statement for every
fixed pair.  M155 correctly fixes a finite `D` first.  Nonnegativity,
pointwise convergence of `W_(3k)`, and the finite-sum liminf inequality give

```text
liminf 2k^2 TV >=lambda H_D.
```

Only afterward is `D` sent to infinity.  This is valid finite-truncation
logic and does not exchange a liminf with an infinite sum.  It proves
`liminf k^2 TV=infinity` conditionally on `(BLM)`.

Under `(UBL)`, the quantifiers are stronger: one common `lambda`, one fixed
`0<theta<1`, all sufficiently large odd `k`, and all
`a,b<=floor(k^theta)`.  Since `a+b=o(n)` uniformly there,
`W_(3k)(a,b)>=c b_a b_b` for an absolute positive `c`; the same truncation
with `H_floor(k^theta)` proves `TV=Omega(log k/k^2)`.  Neither premise is
asserted proved.

## 7. BCL equivalences and downstream scope

The triangle and double terms in M155 equation `(2.6)` are nonnegative.
Consequently direct balanced `TV=O(k^-2)` is equivalent to the two uniform
bounds called `(BCL-sharp)`.  Likewise `(BCL-log)` is exactly the balanced
upper bound `TV=O(log k/k^2)`, up to an immaterial constant factor.

Only a uniform all-strict-edge analogue of `(BCL-log)`, not the balanced
statement, can be combined with M80's diameter-at-most-four graph.  That
would give `delta(bar K^2)=O(log n/n^2)` and, by self-adjointness,
`|kappa|=O(sqrt(log n)/n)`.  M155 correctly labels this conditional and does
not promote it to H0, a bridge gap, or a Terminal.

Finally, M94's `z_k` is the complete signed posterior convolution over all
supported intermediate triangle and double states.  M155 takes the absolute
value only after that sum, and averages over `y` afterward.  Hence the
small-component and lower-support strata flagged by M102/M105 are retained.
M155 does not claim that triangles form a complete matching counterterm, so
it respects M105's required topology correction.

## 8. Status ledger, objections, and hygiene

```text
colored disintegration, W formula, and factor two       proved
product-Borel TV condensation                            proved
H_D=(2/pi)log D+O(1)                                    proved
(BLM) and (UBL) implications                            proved conditional implications
(BLM), (UBL), BCL-sharp, BCL-log score bounds           unresolved
direct L1, all-edge estimate, H0 and all gaps            unresolved
identity-chain mixing and both Terminals                 unresolved
```

Material numbered objections: **none**.  The strongest controlling caveat
is exactly M155's own: product-Borel condensation supplies no lower or upper
bound on the fully signed fixed-cell score `A_k(a,b)`.

M159 changed only its owned directory, used no network or nonstandard
package, and made no commit or push.  The exact checker is deterministic
with `seed=null` under Python `3.12.3`.

**Final verdict: ACCEPT M155'S STRICT BOUNDARY-CONDENSATE REDUCTION, WITH
ZERO MATERIAL OBJECTIONS; DIRECT L1 AND EVERY GAP/TERMINAL CONSEQUENCE REMAIN
UNRESOLVED.**
