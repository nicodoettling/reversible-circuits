# M32 report: direct parking-macro edges can be exponentially rare but have a polynomial bypass

## 1. Exact claim, convention, target, and kernel

Permutations compose as `(pq)(x)=p(q(x))`, and factor tuples multiply from
left to right.  Fix `n>=3`, put `r=n-1`, and let the endpoint be the long
cycle `c=(0 1 ... n-1)`.  The target law is uniform on the reduced
transposition factorizations

```text
Omega_red(c,r)={t in T_n^r:t_1...t_r=c}.
```

The nonlazy test chain `L_n` chooses one of the `r-1` adjacent raw-factor
pairs uniformly and resamples it uniformly conditional on its ordered
product.  Stanley's noncrossing-cover labels agree with the raw lower
endpoints in this convention; the script computes both and asserts equality.
Project `L_n` by the sorted multiset of its parking labels.

The following claims are proved or exactly refuted.

1. **REFUTED:** every adjacent Dyck lowering
   `c_x,c_(x+1)->c_x+1,c_(x+1)-1` is one projected edge.  The first missing
   edge is

   ```text
   (0,0,2) -> (0,0,1)                                 (1.1)
   ```

   at `n=4`.
2. **EXACT FINITE:** for `3<=n<=6`, every such lowering has a directed
   projected route of length at most two.  This is falsification evidence,
   not a universal theorem.
3. **PROVED INFINITE FAMILY:** for `a,b>=1`, `r=a+b`,

   ```text
   alpha=0^a1^b,              beta=0^(a+1)1^(b-1),
   ```

   the exact projected rate is

   ```text
   bar L_n(alpha,beta)=2/[3(r-1)binom(r,a)].           (1.2)
   ```

   This is exponentially small for balanced `a,b`, so even positive direct
   Dyck edges need not have polynomial rate.
4. **PROVED BYPASS:** if `b>=2` and

   ```text
   gamma=sort(0^a1^(b-1)b),
   ```

   then

   ```text
   bar L_n(alpha,gamma)=2b/[3r(r-1)],                 (1.3)
   bar L_n(gamma,beta)
     =2[1-1/binom(r-1,a)]/[3r(r-1)]
     >=1/[3r(r-1)].                                   (1.4)
   ```

   Thus the exponentially rare direct binary edge has a two-step path on
   which both rates are inverse polynomial.  For `b=1`, (1.2) itself is
   inverse polynomial.

These are theorems for the minimal long-cycle bridge sector.  They are not a
gap theorem for every parking multiset, every endpoint, the identity bridge,
or the original chain `K`.

## 2. Exact calculation

The harness enumerates every transposition word of length `r`, retains the
long-cycle endpoint, and independently checks:

- the Dénes counts `3,16,125,1296`;
- parking-label injectivity and the parking inequalities;
- Stanley cover labels against raw lower endpoints;
- every adjacent-pair product fiber and its exact `Fraction` weight;
- stationary-flow aggregation and detailed balance;
- every adjacent Dyck lowering, the fraction of source microstates that can
  realize it, and shortest directed projected routes; and
- the shared-vertex pair in every sorted representative containing
  consecutive parking values.

The exact summary is:

| `n` | parking macros | missing direct lowerings | maximum route | minimum positive projected edge |
|---:|---:|---:|---:|---:|
| 3 | 2 | 0 | 1 | `1/3` |
| 4 | 5 | 1 | 2 | `1/18` |
| 5 | 14 | 6 | 2 | `1/54` |
| 6 | 42 | 28 | 2 | `1/180` |

There are no detailed-balance failures or disconnected tested Dyck routes.
The first missing edge (1.1) routes exactly as

```text
(0,0,2) -> (0,1,2) -> (0,0,1)
```

with rates `2/9` and `1/18`.

The per-microstate statistics expose the quantitative trap.  For example,
only two of the ten words in each of the `n=6` macros `0^2 1^3` and
`0^3 1^2` realize the direct binary lowering, each through one selected
three-state rank interval.  This matches (1.2), giving rate `1/60` in both
cases.  Finite positivity was therefore not promoted to a uniform-rate
claim.

## 3. Universal binary proof

For a parking multiset `0^A1^B`, its raw factor graph is a noncrossing tree
whose edges have smaller endpoint zero or one.  Connectivity and acyclicity
leave two types.  The edge type `T_E` contains `(0,1)`; noncrossing forces
vertices `2,...,B+1` to attach to `1` and the remaining vertices to `0`.
The vertex type `T_V` has a unique common neighbor `B+1`, with lower vertices
attached to `1` and higher vertices attached to `0`.

The checked Goulden--Yong cyclic-neighbor ordering makes `T_E` a single
edge chain with unique label word `0^A1^B`.  In `T_V`, the zero and one
edges form chains

```text
z_1<...<z_A,             o_1<...<o_B,
```

with only the cross relation `o_1<z_A`.  Hence its linear extensions are all
binary label words except the sorted one.

The macro change `alpha->beta` uses the triangle on vertices `0,1,b+1`.
It occurs once in the unique `T_E` word and once in the unique `T_V` word
`0^(a-1)10 1^(b-1)`.  Each has one scan site and one of three heat-bath
outputs in `beta`, proving (1.2).

For the first bypass edge, contract the first two one-chain edges.  The two
tree types give `binom(r-1,a)` favorable source words, and both nonspecial
outputs of the three-state fiber lie in `gamma`.  Division by
`binom(r,a)` proves (1.3).  For the reverse of the second edge, contract the
last two zero-chain edges in the `T_V` tree for `beta`; this gives
`binom(r-1,a)-1` favorable words.  Stationary projected masses are orbit
sizes, with `|gamma|=(a+1)|beta|`; detailed balance then gives (1.4).

The full combinatorial proof and its tree-poset convention are frozen in
`cycle-06/mission-M27-base-exceptional-modes/binary_macro_formula.md`.

## 4. Probability, runtime, path, and congestion accounting

- Every direct test step has scan probability `1/(r-1)` and exact fiber
  probability `1/2` or `1/3`; formulas (1.2)--(1.4) retain these factors.
- The binary bypass has path length exactly two and minimum path-edge rate
  at least `1/[3r(r-1)]`.
- No general multicommodity congestion bound is claimed.  In particular,
  many ideal refresh transitions could still load the same bypass edges.
- The deterministic `n<=6` run completed in under seven seconds in the
  recorded coordinator run with Python 3.12.3.  It uses exact rational
  arithmetic and no nonstandard dependency.
- Enumerating the finite kernel is exponential in `n`; it is a falsifier,
  not a proposed sampler.  The proved formulas are evaluated in polynomial
  time.

## 5. Dependencies and statuses

1. **PROVED in the M27 binary artifact and restated here:** the two-tree
   classification, linear-extension counts, (1.2)--(1.4), and their exact
   normalization.
2. **CITED and convention-checked in M27:** Stanley's maximal-chain parking
   bijection and the Goulden--Yong cyclic-neighbor order for a fixed raw
   noncrossing tree.
3. **EXACT FINITE here:** all `n<=6` counts, rates, microstate fractions,
   shortest routes, and detailed balance.
4. **INHERITED PROVED:** the restricted fixed-parking-multiset chain has an
   inverse-polynomial gap through adjacent label swaps.  Combining it with a
   projection gap would be legitimate through the accepted JSTV theorem.
5. **Not proved:** a uniform gap or polynomial-congestion comparison for the
   full parking-multiset projection.

## 6. First unproved standalone proposition

> **GENERAL PARKING-MULTISET FLOW.**  There are universal `c>0,C<infinity`
> such that the stationary-flow projection of the half-lazy adjacent
> rank-two heat bath on every minimal long-cycle factorization space has
> gap at least `c n^(-C)`.  Equivalently, construct a polynomial-congestion
> fractional simulation of the Pollak quotient-coordinate refresh chain,
> accounting for exponentially diluted direct edges such as (1.2).

The finite distance-two observation and the binary bypass suggest a
tree-contraction flow, but neither controls all parking multisets or global
edge congestion.

## 7. Strongest self-attack and calibration

The binary bypass is a single structured family.  It does not imply that
every exponentially rare projected edge has a polynomial bypass, that a
chosen family of bypasses has polynomial congestion, or that an arbitrary
surplus/endpoint bridge reduces to the minimal long-cycle case.  Even a
proof of the named proposition would close only one stratum of the
`O(N log N)` base-scale bridge theorem.

The endpoint is nonidentity and the raw length is minimal, so odd identity
words, `m=0`, `m=2`, `N=2`, and the 27/120/3936 identity calibrations are not
instances of this test.  This separation is deliberate.  Near-minimal
factorizations are exactly the stress case.  No global uniformity is claimed
for pure Hurwitz moves, no `L=2` simulation of the original chain is used,
and no canonical tree or parking word carries comparison flow.  The finite
calculation is used only to refute universal support/rate claims and to
calibrate the universal binary formulas.

## 8. Artifacts and exact reproduction

Owned files:

- `plan.md`;
- `exact_projection.py`;
- `results.json`; and
- this report.

Exact command:

```bash
python3 experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M32-parking-projection/exact_projection.py \
  --n-max 6 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M32-parking-projection/results.json
```

The seed is `null`, Python is 3.12.3, and the repository base commit is
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

REFUTED

This verdict is scoped to direct one-step support/rate domination of the
parking-multiset projection.  The exact binary rare edge is real, but its
proved polynomial two-hop bypass refutes it as a bottleneck candidate.  The
global goal remains open at GENERAL PARKING-MULTISET FLOW and the broader
base-scale fixed-endpoint gap.
