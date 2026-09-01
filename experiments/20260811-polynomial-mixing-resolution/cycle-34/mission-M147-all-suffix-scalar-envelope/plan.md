# M147 plan: all-suffix scalar envelope

Date: 2026-08-13 UTC.

## Objective and scope

Derive, from the accepted all-attachment-rank nilpotent recurrence and the
corrected one-power exceptional subtraction, an abstract suffix-level
envelope for the complete unweighted reset excursion.  The primary target is
either a uniform-in-`L` contraction theorem or a rigorous obstruction showing
why a state consisting only of `L`, `q`, `C_s` (even augmented by finitely
many consecutive Cayley ratios) cannot close.

This mission concerns only the auxiliary full nonlazy stationary-flow
parking-degree projection in the minimal-long-cycle sector.  The project
target remains uniform on fixed-length identity transposition words, with
`(pq)(x)=p(q(x))` and displayed factors left-to-right.  No auxiliary gap,
ROOT-MEAN LIFT, original-chain gap, polynomial mixing, Terminal A, or
Terminal B is in scope.

## Accepted inputs

- M109/M114: exact all-`j` finite-DAG recurrence, strict suffix descent,
  canonical basin estimate, all-deficit `L=0`, and right-heavy `L<=2`.
- M115/M116: arbitrary-deficit `L=1` envelope and right-heavy `L=3`.
- M117/M121: arbitrary-deficit `L=2` envelope and right-heavy `L=4`.
- M140/M144: `C_s<3/4` for `s>=100`, corrected one-power exceptional
  subtraction, arbitrary-deficit descendants through `L=3`, and accepted
  right-heavy `L=5`.

The rejected M131 two-power subtraction is not used.  M145 owns explicit
`L=6` enumeration; M147 will not duplicate it.

## Method

1. Re-express the root support, corrected reset, and all positive attachment
   ranks as a functional operator on suffix data and the exact attachment
   state `(a,D,z)`.
2. Seek an analytic renewal inequality using `C_s<3/4`, retaining the
   exceptional-current subtraction rather than dropping it.
3. If scalar closure fails, construct two exact reachable/abstract suffix
   instances with identical proposed scalar summaries but different next-step
   requirements, or an infinite family defeating every fixed-window summary.
   Identify the first additional statistic needed for a valid Bellman state.
4. Use only capped, deterministic exact rational checks on minimal boundaries
   and extreme `K`; computation will audit identities, not substitute for a
   universal argument.
5. Self-attack all normalizations, rank-one killing, coincident children,
   attachment-deficit propagation, and any claim of sufficiency/minimality.

## Expected failure modes

- Treating the right-heavy child theorem as valid for non-right-heavy
  descendants.
- Replacing the one-power subtraction `a_E lambda_E` by the rejected
  two-power expression.
- Compressing the child attachment law to `q` although it depends on
  `(a,D,z)`.
- Calling a finite counterexample to one chosen envelope an obstruction to
  every scalar envelope without a completeness argument.
- Repeating M145's exponential support/basin enumeration at `L=6`.

## Deliverables

- `checkpoint.md` with the exact functional recurrence and decisive route.
- A proof or obstruction note.
- A standalone deterministic exact checker and machine-readable results if
  needed.
- A nine-field `report.md`, `freeze_manifest.md`, and `SHA256SUMS`.

