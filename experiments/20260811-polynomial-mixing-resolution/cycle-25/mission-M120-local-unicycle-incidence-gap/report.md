# M120 final report: uniform incidence drift, gap still open

Date: 2026-08-12 UTC.

## Field 1 — decision and claim status

Verdict: **PROMOTE** the universal singleton-cycle split/reverse rate and the
two directional rates for the cycle-defect projection.  **KEEP OPEN** every
spectral-gap claim.

PROVED for every `d>=3` and every state of the exact M113/M118 chain `A_d`:

```text
Pr[singleton-cycle split or its reverse] >= 1/(64d^2).
```

More strongly, every nonidentity seam has one singleton split of probability
at least `1/(64d)`, and every identity seam has one reverse of probability at
least `1/d^2`.  For the defect `R=d-c(p)`, every nonbottom state has total
downward probability at least `1/(64d)`, while every nontop state has total
upward probability at least `1/d^3`.

UNRESOLVED: unimodality/no-valley behavior of the stationary defect masses;
the defect-projection gap; fixed-defect two-step restricted gaps;
`gap(A_d)`; `beta(d)`; and the lazy `{3,4,5}` same-product heat-bath gap.
Neither project terminal criterion is reached.

## Field 2 — target, convention, and exact kernel

The auxiliary target is

```text
rho(kappa)=|C_kappa|/Z_inc
```

on realizable keys `kappa=(j,p,Q_L,Q_R)`, where `Q_L,Q_R` coarsen the cycle
partition of `p`, the bipartite cycle-incidence multigraph is connected
unicyclic, and `j=d+|Q_R|-|Q_L|`.  Permutations compose as
`(p q)(x)=p(q(x))`; factors multiply left-to-right.

For a compatible adjacent pair, M113/M118's exact stationary flow is

```text
Q_A(kappa,lambda)=|C_kappa intersect C_lambda|/(2Z_inc),
```

with unused row mass held.  Equivalently, sample a word uniformly from the
raw cell and choose a left/right adjacent cut shift with probability `1/2`.
The accepted exact cell count is

```text
|C_kappa|=j!(2d-j)!
 product_(B in Q_L union Q_R)|B|^(c_B-3)
 product_(p-cycle a)[a^a/(a-1)!]^2.
```

## Field 3 — nonidentity singleton-split theorem

Let `p!=id`.  Choose a `p`-cycle `A` of length `a>=2`, a point `x in A`,
and `t=(x,p^(-1)(x))`.  Then `p'=pt` splits off `{x}`.  If the `Q_R` block
`B` containing `A` has `b` labels and contains `s` cycles, split it into
`{x}` and `B\{x}`.  This is a valid rightward adjacent key.

Write `h(a)=a^a/(a-1)!` and `k=2d-j`.  The exact Cartesian overlap and side
counts give

```text
A_d(kappa,lambda)
 = 1/(2k) * ((a-1)/a)^a * ((b-1)/b)^(s-3).            (3.1)
```

The factors are respectively the direction coin and factorial ratio, the
atom ratio `h(a-1)/h(a)`, and the sole changed block ratio.  Since `k<=2d`,

```text
((a-1)/a)^a >= 1/4.
```

The last factor is at least one for `s<=3`.  For `s>=4`, use `s-3<=b` and
`((b-1)/b)^b>=1/4`.  Hence the single edge (3.1) satisfies

```text
A_d(kappa,lambda) >= 1/(64d).                          (3.2)
```

This move decreases `R=d-c(p)` by one.

## Field 4 — identity reverse theorem and aggregate conclusion

Let `p=id` and `d>=3`.  The incidence multigraph has `d` vertices and `d`
edges.  Some incidence vertex has two incident label-edges with distinct
opposite endpoints: otherwise the underlying connected simple graph would
have maximum degree one and at most two vertices.  Join the two corresponding
singleton cycles.  Depending on the vertex color, this is a valid leftward
or rightward move and the reverse of a singleton split.

If its incidence block has `b` labels, its exact source probability is

```text
2/(j b)  or  2/((2d-j)b),                              (4.1)
```

where the numerator `2` comes from `h(2)=4` and the direction coin.  As
`j,2d-j<=2d` and `b<=d`, one such move has probability at least `1/d^2`.
Combining (3.2) and (4.1), every state for `d>=3` satisfies

```text
Pr[singleton split or reverse]
 >= min{1/(64d),1/d^2} >= 1/(64d^2).                  (4.2)
```

This discharges exactly M113's weaker aggregate-drift precursor.  At `d=2`,
there is one key and no off-diagonal transition; (4.2) is not asserted, and
the gap convention is one.

## Field 5 — exact defect birth-death projection

Define

```text
R(kappa)=d-c(p) in {0,...,d-2}.
```

Every transposition joins or splits two permutation cycles, so every `A_d`
edge changes `R` by exactly one.  Equation (3.2) gives, statewise and hence
after stationary-flow projection,

```text
q_r=Pr[R -> r-1 | R=r] >= 1/(64d),   1<=r<=d-2.       (5.1)
```

For `r<=d-3`, the incidence graph has at least three vertices and contains
two atom-edges at one vertex with distinct opposite endpoints.  If their
cycle lengths are `a,b`, their common incidence block has `B` labels, and
the relevant side has length `k`, joining them is a valid edge increasing
`R`, with exact probability

```text
h(a+b)/(2kB h(a)h(b)).                                (5.2)
```

For `n=a+b`,

```text
h(n)/(h(a)h(b))
 = [n/(ab)]/[binom(n,a)(a/n)^a(b/n)^b]
 >= n/(ab) >= 4/n >= 4/d,                             (5.3)
```

because the denominator in square brackets is a binomial point probability.
Using `k<=2d` and `B<=d` in (5.2) proves

```text
p_r=Pr[R -> r+1 | R=r] >= 1/d^3,     0<=r<=d-3.       (5.4)
```

Every level occurs.  For any `c=d-r>=2`, choose a permutation with `c`
cycles and partitions giving a connected unicycle, for example one left
block and a right partition with one two-cycle-atom block and all other
atoms singleton.  Thus the exact stationary-flow projection onto `R` is a
birth-death chain on the full displayed interval with (5.1)--(5.4).

## Field 6 — exponential-valley self-attack and exact remaining reduction

The directional bounds do not prove a spectral gap.  A reversible
birth-death chain can have both directions at least `delta` while its
stationary law has an exponential central valley: on `{0,...,2L}`, take
right/left rates `(delta,1/2)` on the left half and `(1/2,delta)` on the
right half.  Detailed balance makes masses fall geometrically by `2delta`
to the middle and rise symmetrically.  The middle conductance is
exponentially small in `L`, despite the local rate lower bound.

For the exact defect masses

```text
mu_r=sum_(R(kappa)=r)rho(kappa),                       (6.1)
```

the next standalone statement is:

> **DEFECT NO-VALLEY LEMMA.**  `(mu_0,...,mu_(d-2))` is unimodal for every
> `d>=3`.

Conditional on that lemma, a path comparison gives

```text
gap(projected defect chain) >= 1/(64d^5).              (6.2)
```

At an edge before a mode, the lower-prefix mass is at most `d` times the
left endpoint mass; after a mode, the upper-tail mass is at most `d` times
the right endpoint mass.  The edge flow is at least
`min{1/(64d),1/d^3}` times both endpoint masses, and paths have length at
most `d`.  Statement (6.2) is CONDITIONAL, not promoted.

The ordinary restriction to one `R` level has no off-diagonal edges.  Let
`P=(I+A_d)/2`.  The correct restricted object `B_(d,r)` holds every exit of
`P^2` from `Omega_r={R=r}` and, for distinct states in `Omega_r`, has flow

```text
Q_B(kappa,lambda)
 = rho(Omega_r)^(-1)
   sum_eta rho(kappa)P(kappa,eta)P(eta,lambda).         (6.3)
```

It is reversible for `rho(.|Omega_r)` and consists of exact down-up/up-down
coagulation-fragmentation moves.  The remaining fiber lemma is

```text
min_r gap(B_(d,r)) >= d^(-O(1)).                       (6.4)
```

A precise decomposition/comparison for `P^2` is still required after
(6.2) and (6.4).  This is a non-hub reduction: it routes through neither a
fixed `p=id` state nor an extreme incidence normal form.

## Field 7 — exact finite diagnostics

`incidence_gap_audit.py` independently constructs all keys from the
connected-unicycle criterion, evaluates exact side counts, builds all exact
overlaps and flows, checks (3.1), (4.1), and (5.2), and diagonalizes a sparse
reversible symmetrization numerically.

| d | keys | edges | components | finite numeric gap(A_d) |
|---:|---:|---:|---:|---:|
| 2 | 1 | 0 | 1 | 1 |
| 3 | 9 | 12 | 1 | 0.1414353635 |
| 4 | 101 | 324 | 1 | 0.1254163084 |
| 5 | 1420 | 7520 | 1 | 0.1121580619 |

The independently reconstructed `d<=4` values match M113/M118.  There are
zero exact row, canonical split, or canonical join formula failures.  The
stationary eigenvector residual is at most `5.7e-13`.  The finite defect
mass sequence is unimodal and log-concave for `d=2,3,4,5`; this is a finite
fact only.  The singleton-only skeleton is connected in these cases and has
finite numerical gaps `1,0.1414353635,0.1254163084,0.1059080005`.

Named threshold scans by defect/cycle count, cut level, incidence maximum
degree, incidence leaves/core, maximum label-block size, and left/right
block count find no small-conductance cut through `d=5`.  The smallest at
`d=5` among these named scans is `19353/116192 ~=0.16656`, for the one-left-
block and color-reversed one-right-block thresholds.  These are exact finite
flows and masses, not asymptotic gap evidence.

Reproduction command from the repository root:

```text
python3 -B \
  experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M120-local-unicycle-incidence-gap/incidence_gap_audit.py \
  --d 2 3 4 5 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M120-local-unicycle-incidence-gap/results.json
```

Environment: repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python `3.12.3`, NumPy
`1.26.4`, SciPy `1.11.4`, seed `null` (deterministic).

## Field 8 — dependencies, boundaries, and self-audit

- Required sources read: `HANDOFF.md`, `GOAL_SPEC.md`, the project skill,
  its sampling and experiment references, the relevant manuscript sections,
  frozen M113, and fresh M118.
- The auxiliary target `rho` is distinct from both the original uniform word
  law and M113's lifted projection law `bar_pi`; only the accepted M113/M118
  comparison can transfer a future `A_d` gap.
- Exact constants retain the direction coin and holding convention.
- `d=2` is separated explicitly; there is no aggregate off-diagonal drift.
- The theorem chooses one edge per source, so it survives exponentially tiny
  balanced individual edges elsewhere; it does not assert all edges are large.
- Aggregate escape, polynomial diameter, finite connectivity, finite spectra,
  and finite cut scans are not promoted to an asymptotic gap.
- The explicit exponential-valley construction refutes the inference from
  two directional polynomial rates alone to a birth-death gap.
- Unimodality and fixed-defect down-up expansion are kept beside every result
  that depends on them.
- No Lorentzian claim is made; M113's refuted natural polynomial is not used.
- No file outside the owned M120 directory was edited; no package was
  installed; generated bytecode cache was removed.

## Field 9 — first open lemmas and recommended next attack

First projection obligation:

```text
DEFECT NO-VALLEY:
mu_r=sum_(R(kappa)=r)rho(kappa) is unimodal for 0<=r<=d-2.
```

First restricted-fiber obligation:

```text
FIXED-DEFECT TWO-STEP GAP:
min_(0<=r<=d-2) gap(B_(d,r)) >= d^(-O(1)),
```

with `B_(d,r)` defined exactly by (6.3).  The recommended next attack is an
exact generating-function or injection proof of DEFECT NO-VALLEY, in
parallel with a non-hub exchange/decomposition for `B_(d,r)`.  A future
theorem must then state and prove the comparison from the defect projection
and these restrictions back to the lazy squared chain.  Until all three
steps close, `gap(A_d)>=d^(-O(1))` remains unresolved.
