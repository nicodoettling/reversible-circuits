# M75 plan: one-radius partial-macro coarea

## Objective and target

Work at

```text
N>=5,  m=2N-2,  M=binom(N,2),
Omega=Omega(N,m),  pi=Unif(Omega),
K=(1/2)I+(1/6) sum_(r=3)^5
       (1/(m-r+1)) sum_i H_(i,r).
```

Permutations compose as `(pq)(x)=p(q(x))`; words evaluate as
`t_1...t_m`.  The assigned target is the accepted M68/M74
**ONE-RADIUS PARTIAL-MACRO MARKED-COVER / COAREA** obligation for the
M64 exterior balls `E_k` and cuts `C_k=A union E_k`.

The primary positive target is a polynomial first-boundary flow for every
partial exterior macrofiber.  The negative target is a rigorous refutation
of the strongest natural state-independent/randomized short-cover
construction, with an exact replacement lemma.  No auxiliary-chain cut is a
Terminal-B claim unless its stationary mass and complete literal
`H3/H4/H5` boundary are proved.

## Inherited frozen inputs

1. M68, corrected and independently accepted by M74: whole-macro marked
   probability at least `3/[Nm(m-1)]`, downward action `theta_N`, dense
   macro action, the conditional fixed-word cover theorem, and the exact
   obstructions to direct two-deletion, one-level four-null, pointwise exit,
   colors-only handles, full arcs, and global terminal coalescence.
2. M64/M66: the exact exterior boundary identity, polynomial exterior
   diameter, and first-exterior-boundary stopping framework.
3. Quantitative Classification H: each weighted component macro has Hurwitz
   diameter at most `50Nm^3`; every Hurwitz generator is a positive padded
   literal `H3` edge.

Frozen predecessor directories will not be modified.

## Work lanes

1. **Randomized marked-cover lemma.**  Replace a finite deterministic
   translate cover by a state-independent law on Hurwitz words.  Derive the
   exact first-crossing boundary bound from a uniform hitting probability
   and expected/maximal word length, with source recovery performed
   path-by-path.
2. **Component-local cover candidate.**  Test fixed/random adjacent-generator
   schedules that expose a connected-deletable square in a selected
   positive-genus component.  Separate genuine algebraic handle preservation
   from mere collision of two colored positions.
3. **Coarea/averaging.**  Determine whether transitivity plus polynomial
   diameter and the whole-macro marked density can yield a polynomial
   randomized translate cover without exponential support or mixing.  If
   false, give an explicit vertex-transitive counterexample and identify the
   extra geometric hypothesis needed.
4. **Finite falsification.**  Calibrate the strongest surviving candidate at
   `N=3,4,5` where relevant.  Exact finite success is never promoted to an
   asymptotic theorem.
5. **Additive mergers.**  Audit whether the local cover composes across
   component mergers while stopping at first exterior boundary, without a
   multiplicative `theta_N` loss or a minimal-macro hub.

## Expected failure modes

- a state-independent distribution that hits marks from every source exists
  only with exponentially long/support-heavy words;
- transitivity and polynomial diameter alone do not imply expansion or a
  polynomial hitting law;
- algebraic deletability requires braid-history data with unbounded
  monodromy;
- component-local normalizations still collide through an atypical paired
  word;
- a multiradius volume-growth statement fails to control the one particular
  shell `L_k -> L_(k+1)`.

## Deliverables

Produce `checkpoint.md`, any exact scripts and machine-readable output,
and a nine-field `report.md`: exact claim/convention; full argument;
probability/runtime/path/congestion accounting; dependencies; first unproved
step; strongest self-attack; calibrations; artifacts/reproduction; and one
verdict `PROVED`, `REFUTED`, or `OPEN AT A NAMED STEP`.
