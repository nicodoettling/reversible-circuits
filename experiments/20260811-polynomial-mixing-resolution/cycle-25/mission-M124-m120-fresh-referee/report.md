# M124 fresh referee report on frozen M120

Date: 2026-08-12 UTC.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — decision, scope, and numbered objections

```text
ACCEPT M120's universal singleton-split/reverse theorem and its two
directional cycle-defect rate bounds.
Material numbered objections: none.
```

The exact formulas, universal inequalities, existence arguments, defect
range, and `d=2` exception are correct.  M120 also correctly makes no
unconditional spectral-gap or mixing-time claim.  This referee acceptance
does not prove the defect no-valley lemma, a fixed-defect restricted gap,
`gap(A_d)>=d^{-O(1)}`, a polynomial value of `beta(d)`, or a polynomial gap
for the lazy `{3,4,5}` same-product heat-bath chain.

## Field 2 — frozen provenance, target, convention, and kernel

All five assigned M120 hashes independently match:

| frozen artifact | required and observed SHA-256 |
|---|---|
| `report.md` | `9f1cdd5f137b32b3ded80d951b6067565edac2ade9032d18cb0251e7c92803db` |
| `incidence_gap_audit.py` | `2649acb303c910f1d526f446572eb6fd674aa17c26c78bc175843fc76b94f368` |
| `results.json` | `9285dc8958a59cd62fccd2cd8cdc95053dd1ecb033c6a3562925962bc1af28f9` |
| `checkpoint.md` | `a5bff43d77a568255537b4db4f2faf33c6ee6ed538cf65f647398e59671d8580` |
| `freeze_manifest.md` | `9e70cb1f3db32ae602f99c7ff78e5800e66069ce893b546e7c3f46212a8f515b` |

The audited target is the auxiliary law

```text
rho(kappa)=|C_kappa|/Z_inc
```

on realizable keys `kappa=(j,p,Q_L,Q_R)`, not the original uniform identity-
word law or the lifted projection law `bar_pi`.  The two partitions coarsen
the cycles of `p`; their bipartite cycle-incidence multigraph is connected
and unicyclic; and `j=d+|Q_R|-|Q_L|`.  Permutations compose as
`(p q)(x)=p(q(x))`, and word factors multiply left-to-right.

For compatible adjacent keys the exact stationary flow is

```text
Q_A(kappa,lambda)=|C_kappa intersect C_lambda|/(2Z_inc),
```

with unused row mass held.  The factor `1/2` is the left/right direction
coin.  M118 independently accepted the M113 cell formula and Cartesian
overlap on which this definition rests.

## Field 3 — nonidentity singleton-split formula and bounds

Let `p!=id`, let `A` be a `p`-cycle of length `a>=2`, choose `x in A`, and
set `t=(x,p^{-1}(x))`.  Then right multiplication `p'=pt` splits `A` into
`{x}` and an `(a-1)`-cycle.  If the `Q_R` block `B` containing `A` has `b`
labels and contains `s` cycle-atoms, splitting `B` into `{x}` and
`B\{x}` produces a valid rightward adjacent key.

Put `k=2d-j` and `h(a)=a^a/(a-1)!`.  Dividing the Cartesian overlap by twice
the source cell count leaves the target suffix count divided by the source
suffix count.  The factorial contribution is `1/k`; the atom contribution is

```text
h(a-1)/h(a)=((a-1)/a)^a;
```

and the only changed block contribution is

```text
(b-1)^((s+1)-3) / b^(s-3)
 = ((b-1)/b)^(s-3).
```

Consequently M120's exact formula is correct:

```text
A_d(kappa,lambda)
 = 1/(2k) * ((a-1)/a)^a * ((b-1)/b)^(s-3).            (3.1)
```

Here `b>=a>=2`, so every expression is defined.  Also `k<=2d` and
`((a-1)/a)^a>=1/4`: the sequence has value `1/4` at `a=2` and is increasing.
If `s<=3`, the block factor is at least one.  If `s>=4`, then `s<=b`, so
`s-3<=b`; because the base is in `(0,1)`,

```text
((b-1)/b)^(s-3) >= ((b-1)/b)^b >= 1/4.
```

Thus every nonidentity source has this one downward edge with

```text
A_d(kappa,lambda) >= 1/(64d).                          (3.2)
```

The bound is intentionally on a constructed singleton split, not on every
valid adjacent edge; M113's balanced family already refutes the latter.

## Field 4 — identity reverse existence and exact rate

Now let `p=id` and `d>=3`.  The incidence multigraph has `d` vertices and
`d` label-edges.  There is an incidence vertex with two incident edges going
to distinct opposite vertices.  Indeed, if every pair at every vertex had
the same opposite endpoint, the underlying connected simple graph would
have maximum degree at most one, hence at most two vertices, contrary to
`d>=3`.

Join the two corresponding singleton cycles.  If their common incidence
block is on the left, shift the cut left and merge the two right blocks; if
it is on the right, shift the cut right and merge the two left blocks.  The
distinct opposite endpoints are exactly what makes the appropriate two
blocks distinct, so the adjacent-key condition is satisfied.  This move is
the reverse of a singleton split.

If the common block contains `b` labels, the general join ratio with
`a=b_cycle=1` has `h(2)/(h(1)h(1))=4`; after the direction coin its exact
source probability is

```text
2/(j b)  or  2/((2d-j)b).                              (4.1)
```

Since `j,2d-j<=2d` and `b<=d`, either rate is at least `1/d^2`.  Combining
(3.2) and (4.1), every source for `d>=3` has total singleton-split-or-reverse
probability at least

```text
min{1/(64d),1/d^2} >= 1/(64d^2).                      (4.2)
```

This proves precisely M113's requested aggregate precursor.

## Field 5 — defect range, directions, and binomial-pmf inequality

Define `R(kappa)=d-c(p)`.  A realizable connected-unicyclic incidence graph
has `c(p)=|Q_L|+|Q_R|>=2`, while `c(p)<=d`, so

```text
0 <= R <= d-2.
```

Every level occurs.  For any `c=d-r` with `2<=c<=d`, choose a permutation
with `c` cycles, take one left block containing all cycle-atoms, and on the
right take one block containing two atoms and all remaining atoms as
singletons.  The resulting bipartite incidence multigraph is connected,
has `c` vertices and `c` edges, and is therefore a unicycle.  The stated
formula gives a legal cut `j=d+(c-1)-1=d+c-2`.

A transposition either joins two cycles or cuts one cycle, so every `A_d`
edge changes `R` by exactly one.  Equation (3.2) is a statewise downward
rate at every `R>=1`; after stationary-flow projection it yields

```text
q_r >= 1/(64d),                  1<=r<=d-2.             (5.1)
```

For `R<=d-3`, there are at least three cycle-atoms and hence at least three
incidence vertices.  The same simple-graph argument supplies an incidence
vertex containing two atom-edges with distinct opposite endpoints.  Joining
atoms of lengths `a,b`, in a common label block of size `B`, along a side of
length `k`, is a valid edge increasing `R`.  Independent side-count division
gives exactly

```text
h(a+b)/(2kB h(a)h(b)).                                (5.2)
```

For `n=a+b`, direct factorial cancellation gives

```text
h(n)/(h(a)h(b))
 = n/(ab) /
   [binom(n,a)(a/n)^a(b/n)^b].                         (5.3)
```

The bracket is exactly `Pr[Bin(n,a/n)=a]`, hence at most one.  Therefore

```text
h(n)/(h(a)h(b)) >= n/(ab) >= 4/n >= 4/d.
```

The middle inequality is equivalent to `(a-b)^2>=0`, and `n<=d` because the
two cycles are disjoint subsets of `[d]`.  Since `k<=2d` and `B<=d`, (5.2)
is at least `1/d^3`.  Thus the statewise and projected upward rates obey

```text
p_r >= 1/d^3,                     0<=r<=d-3.            (5.4)
```

No averaging reversal occurs: statewise bounds imply their conditional
stationary averages.  Reversibility supplies the usual birth-death detailed
balance between consecutive levels.

## Field 6 — `d=2` exception and exponential-valley self-attack

At `d=2`, realizability leaves exactly

```text
(j,p,Q_L,Q_R)=(2,id,{{0,1}},{{0,1}}).
```

There is no off-diagonal adjacent transition and only defect level zero.
The gap is one by the one-state convention, but (4.2) is false and is
correctly not asserted.

M120's warning that (5.1)--(5.4) do not prove a gap is also correct.  On
`{0,...,2L}`, fix `0<delta<1/2`.  For edges strictly left of the center take
right/left rates `(delta,1/2)`; for edges at and right of the center take
`(1/2,delta)`, with remaining mass held.  Detailed balance gives, up to
normalization,

```text
pi_i=(2delta)^min(i,2L-i).
```

Every nonzero direction rate is at least `delta`, but the flow across the
middle cut is proportional to `(2delta)^L`, while either side has mass
bounded below by an endpoint mass.  Hence conductance is exponentially small
in `L`.  The exact checker instantiates `delta=1/8` for `1<=L<=10`; all
detailed-balance, rate-floor, holding, and geometric-shape checks pass, and
the conductance divided by `(2delta)^L` stays between `0.375` and `0.5`.

Accordingly, M120 correctly labels the defect no-valley lemma as unresolved
and its projected-gap bound `1/(64d^5)` as conditional.  It also correctly
uses a lazy two-step restriction for fixed defect, since the one-step
restriction has no off-diagonal edges.

## Field 7 — independent exact reconstruction

`fresh_audit.py` was written without importing any M120, M118, M113, or
other mission code.  It enumerates permutations and coarsenings, applies the
connected-unicycle criterion, evaluates independent one-sided genus-zero
counts, generates compatible adjacent cuts, and keeps all probabilities as
`Fraction` values.  It does not enumerate transposition words.

| `d` | keys | edges | components | formula/bound failures |
|---:|---:|---:|---:|---:|
| 2 | 1 | 0 | 1 | 0 |
| 3 | 9 | 12 | 1 | 0 |
| 4 | 101 | 324 | 1 | 0 |
| 5 | 1420 | 7520 | 1 | 0 |

For every finite source it tests every possible chosen `x` in every
nontrivial cycle for (3.1), every admissible identity reverse for (4.1), and
every admissible distinct-neighbor join for (5.2).  There are zero missing
constructed neighbors, ratio mismatches, row failures, defect-direction
failures, statewise-bound failures, projected-bound failures, missing levels,
or detailed-balance failures.  The exact key/edge counts match M120, and the
singleton skeleton is connected through `d=5`.

Finite defect masses are unimodal and log-concave through `d=5`.  This is a
finite diagnostic only.  It is not used to promote the universal no-valley
lemma, and no real-rootedness claim is made.

Reproduction from the repository root:

```text
python3 -B \
  experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M124-m120-fresh-referee/fresh_audit.py \
  --d 2 3 4 5 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M124-m120-fresh-referee/results.json
```

The run is deterministic (`seed=null`) under Python `3.12.3` and took less
than one second of checker time on the recorded machine.  Raw exact output is
in `results.json`.

## Field 8 — dependencies, claim audit, and hygiene

- Read before judgment: `HANDOFF.md`, `GOAL_SPEC.md`, the full project skill,
  its sampling and experiment references, relevant manuscript status/graph
  sections, frozen M113 sources, fresh M118 sources, and all frozen M120
  payloads.
- M120 keeps `rho`, `bar_pi`, and the original identity-word target distinct.
- The direction coin, cut boundary, factorial ratio, atom ratio, and changed
  block ratio are all retained.
- The identity existence proof genuinely needs `d>=3`; `d=2` is separated.
- The join proof covers all nontop defect states and both cut directions.
- The binomial bracket in (5.3) is a probability at the integer outcome `a`,
  so the inequality direction is correct.
- Polynomial local escape, finite connectivity, and finite spectra are not
  promoted to expansion.  The explicit valley attack blocks that inference.
- M120 calls the projected-gap claim conditional and leaves the fixed-defect
  two-step gap and the comparison back to the squared chain open.
- No continuation mission is proposed.  No predecessor, shared durable,
  manuscript, skill, or coordinator file was edited.

## Field 9 — final verdict and open obligations

**ACCEPT, with zero material numbered objections.**

M120 validly promotes exactly these proved statements for `d>=3`:

```text
every state has singleton-split-or-reverse probability >= 1/(64d^2);
every nonbottom defect state has downward probability >= 1/(64d);
every nontop defect state has upward probability >= 1/d^3.
```

It validly excludes `d=2` from the off-diagonal theorem and explicitly
demonstrates why the directional rates alone give no spectral-gap theorem.
The first unresolved statements remain M120's `DEFECT NO-VALLEY` lemma and
`FIXED-DEFECT TWO-STEP GAP`; neither is promoted here.  There is no
continuation recommendation from M124.
