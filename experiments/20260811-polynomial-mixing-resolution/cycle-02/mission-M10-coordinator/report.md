# Report: two-type synchronous path coupling is not contractive

This report rigorously refutes one direct-coupling criterion for the auxiliary
pair chain `J`.  It does **not** exhibit slow mixing: the exact witness is at
`N=4,m=4`, where the target chain `K` has gap at least `1/4` from its
whole-word heat bath.

## 1. Exact claim and conventions

Use `(pq)(x)=p(q(x))`.  In prefix coordinates, an identity word gives a path
`X_0=id,X_j=t_1...t_j,X_m=id`; an adjacent-pair heat bath updates one interior
prefix vertex.  Write

    J = (1/2)I + (1/2)G,
    G = [1/(m-1)] sum_{j=1}^{m-1} H_{j,2}.

For two transpositions `a,b`, give an unequal discrepancy cost `1` if they
overlap and `lambda>0` if they are disjoint.  The named coupling under audit
uses the corresponding two-type additive discrepancy potential and couples
the laziness and scan site synchronously, using an optimal transport coupling
of the two conditional midpoint laws.

**Proposition.** For every `lambda>0`, this coupling is not one-step
contractive uniformly in `N,m`.  Already at `N=4,m=4`, an overlapping
single-site discrepancy has expected potential at least `19/18` after one
lazy `J` step, from initial potential one.

This proposition refutes the two-weight synchronous additive criterion.  It
does not refute all metrics, nonsynchronous couplings, block couplings,
path coupling with a larger state-dependent type space, or a Poincare bound.

## 2. Exact construction and proof

On labels `{0,1,2,3}`, set

    p=(1,3),    t=(0,1),    t'=(0,2).

The two identity words

    x=(p,t,t,p),       y=(p,t',t',p)

differ at only the middle prefix `X_2`; their quotient type is overlapping,
so its normalized potential is one.  The prefix vertices `X_1` and `X_3`
coincide for the two paths.

Updating `X_2` gives identical conditional laws because the two fixed
neighbors coincide, so the discrepancy can be coupled to zero.  Consider
instead updating `X_1`.  The two endpoint products are `pt` and `pt'`.
Their exact first-transposition midpoint fibers are

    L={(0,1),(0,3),(1,3)},
    R={(0,2),(1,3)}.

Both conditional laws are uniform.  Put `c=(1,3)` and `d=(0,2)`.  Every
transport from either of the two labels in `L\{c}` to either target in `R`
has overlapping cost one.  The transport `c -> c` has cost zero and
`c -> d` has disjoint cost `lambda`.

If `z` is the transported mass from `c` to `c`, then `0<=z<=1/3` and every
coupling has cost

    2/3 + lambda(1/3-z) >= 2/3.

Equality is feasible by taking `z=1/3` and splitting the remaining mass to
meet the two target demands.  Thus the exact optimal cost is `2/3`,
independently of `lambda`.  Updating `X_3` gives inverse endpoint products
`tp,t'p` and the same two fibers and cost.

For the active random scan `G`, the minimum synchronous-site expected
additive potential is therefore

    [0 + (1+2/3) + (1+2/3)]/3 = 10/9.

The explicit half-laziness of `J` gives

    (1/2)*1 + (1/2)*(10/9) = 19/18 > 1.

This is an exact algebraic obstruction, not a numerical extrapolation.
Embedding the same four labels proves failure for every `N>=4` at the local
criterion level, although the single `N=4,m=4` witness already refutes a
universal contraction claim.

## 3. Probability, runtime, path, and congestion accounting

- `J` holds with probability `1/2`; conditional on the active half, each of
  the three interior prefix vertices at `m=4` is scanned with probability
  `1/3`.  Equivalently, each heat bath has total coefficient `1/6` in `J`.
- The midpoint fibers have exact sizes three and two.  The lower bound uses
  the entire transportation polytope, not a particular failed coupling.
- The deterministic harness quotients all triples `(p,t,t')` by simultaneous
  label relabeling and solves the residual finite transport problems for
  `N=3,...,9` and fifteen positive weight ratios.  A timed fresh run took
  1.28 seconds and was byte-identical.
- No Markov-chain comparison path or congestion bound is claimed.

## 4. Dependencies

1. **Proved:** the prefix-path representation of `J`, exact two-step fibers,
   the displayed transportation calculation, and the `19/18` drift.
2. **Empirical finite cross-check:** SciPy linear programs reproduce the exact
   witness and scan the other finite orbit types.  The proposition itself does
   not depend on floating-point optimization.
3. **Inherited proved:** `E_K>=E_J/(3 binom(N,2)^2)` and irreducibility of
   `J`.  The comparison is one-way and is not used to infer slowness.
4. **Unresolved:** any contractive multitype/block metric or direct Poincare
   inequality for `J`.

## 5. First unproved standalone proposition

**Bridge Poincare proposition.** There exist universal `c>0,C<infinity`
such that for every `N>=3` and even `m>=4`,

    gap(J_{N,m}) >= c(Nm)^(-C).

The present result only removes the two-type synchronous additive path-
coupling proof of this proposition.

## 6. Strongest self-attack

Failure of one-step contraction is common even for rapidly mixing chains.
The witness lies in the easiest whole-word regime for `K`, and `19/18` is an
expansion of a chosen potential, not an eigenvalue or conductance estimate.
A metric that remembers the full local factorization type, a two-step or
block coupling, or a functional inequality can still prove the bridge
Poincare proposition.  No conclusion about TERMINAL B is available.

## 7. Calibration

- Odd `m` and the `m=0,N=2,m=2` boundary regimes are not used.
- At `N=3` no disjoint discrepancy type exists; the exact harness records
  this rather than inventing it.
- At `N=4,m=4`, both displayed words evaluate to identity.  The `r=4`
  whole-word heat bath in `K` remains present and proves fast mixing of `K`;
  it is not dropped from any normalization.
- The construction uses full transposition products, not edge- or
  degree-parity summaries.
- The known failure of length-two internal simulation is not invoked.

## 8. Artifacts and reproduction

Owned directory:

    experiments/20260811-polynomial-mixing-resolution/
      cycle-02/mission-M10-coordinator/

Files: `plan.md`, `two_type_coupling.py`, `results.json`, and this report.

Reproduce with:

    python3 two_type_coupling.py --output results.json --n-min 3 --n-max 9

Recorded environment: Python 3.12.3, SciPy 1.14.1, NumPy 1.26.4, seed zero
(the calculation is deterministic).  Final hashes:

    two_type_coupling.py
      64e6246b0c20a998ab94558951a63a76c384229a334a2b1eceed8dd1082c7a27
    results.json
      2dc46816888062baf6f989f2a113d34864b8d78327cc0b84dbf62feedeb7979a

## 9. Verdict

REFUTED, scoped exactly to universal one-step contraction of the two-type
synchronous additive path coupling.  The bridge gap and global goal remain
open.
