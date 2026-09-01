# M56 checkpoint: marked root-history flow

Date: 2026-08-11.  Convention: `(pq)(x)=p(q(x))`; factors multiply
left-to-right.  Scope: the minimal long-cycle parking projection `Pbar_r`,
not the original identity chain `K`.

## 1. Exact claim and current verdict

The proposed **exact** stationary normalization of canonical or uniformly
randomized root-boundary coalescence is **REFUTED** at `r=3`.  The full
ROOT-MEAN LIFT and polynomial gap remain open at the named step
`MARKED-HISTORY L2 CONTROL` in `marked_history_recurrence.md`.

## 2. Full argument and construction

M50 gives exact stochastic merge kernels between root-degree layers.  By
reversibility, their endpoint density is the reverse valid-cut-history
partition function (2.2)--(2.3) of `marked_history_recurrence.md`.  A
root-composition `(1,2)` source at `r=3` maps with probability one to macro
`(0,1,2)`, while the unary-root stationary conditional law gives masses
`1/3,2/3` to `(0,1,1),(0,1,2)`.  Thus a valid cut mark is indispensable and
does not normalize away after forgetting it.

The zero-length histories imply endpoint density at least
`(r/(r+1))^(r-1)>=e^-1` pointwise.  Exact endpoint chi-square remains below
`.023` for canonical and `.030` for uniform-boundary coalescence through
`r=7`; this is finite evidence only.  The exact recurrence is now the
analytic target, not a product of one-step density maxima.

The rigid alternative in which every rotation moves the same distinguished
leaf is also refuted at `r=3`: a first-child marked leaf followed by another
child is neither movable down nor liftable.  Full unmarked routes may swap
the mark or move auxiliary subtrees.  Exhaustive unmarked geometry through
`r=7` finds every distinct leaf-replanting neighbor connected in full
`Pbar_r`, with maximum shortest distances `1,2,3,4,5,6` for `r=2,...,7`.

## 3. Probability, runtime, path, and congestion

- One canonical boundary has total rate `alpha k`; all `k-1` boundaries
  have total rate `alpha k(k-1)`, `alpha=2/[3r(r-1)]`.
- Canonical coalescence path length is at most `r-1`.
- The endpoint lower density is at least `e^-1`; no universal upper/L2
  theorem is proved.
- The M41 root quotient gap `2/[9e r(r-1)]` is retained.
- Exact scripts enumerate Catalan macros through `n<=8`; runtime and memory
  are exponential and prove no asymptotic congestion statement.

## 4. Dependencies

- **Proved M50/M41:** boundary rate/support, root quotient and its `r^-2`
  gap, product restrictions, stationary parking law.
- **Proved here:** density recurrence, zero-history lower bound, smallest
  normalization counterexample, rigid distinguished-leaf obstruction.
- **Fresh-refereed here:** M53 report hash
  `eb5f5241616853115afcef669daddf4ff9a689a86869ab9cea6b902fd46e47a9`
  is ACCEPTED with no objection.
- **Empirical exact:** all `n<=8` density and distance calculations.

## 5. First unproved standalone proposition

`MARKED-HISTORY L2 CONTROL` as stated in
`marked_history_recurrence.md`, including prefix edge-load control.

## 6. Self-attack

Small endpoint chi-square does not control path-edge occupation by itself,
and a constant density loss per recursive level is fatal.  Cyclic
conjugation is an automorphism only at micro level; its parking macro after
rerooting depends on hidden incidence to the wrap label, so macro
exchangeability cannot be assumed.  The unmarked distance data have no
stationary-flow or source-recovery bound.

## 7. Calibrations

- `r=1` singleton; `r=2` exact normalization holds trivially.
- Smallest failure is `r=3`, consistent with the M50 nonlumpability witness.
- Stars/path-like shapes are included; endpoint pointwise extremes are
  recorded rather than discarded as rare.
- Full unmarked replant distances are exact through `r=7`, but only
  falsifiers.
- The M48 leaf-rotation separator is not lifted to full `Pbar_r`.

## 8. Artifacts and reproduction

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/marked_history_audit.py --n-max 8 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/marked_history_n8.json
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/replant_full_distance.py --n-max 8 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/replant_full_distance_n8.json
```

Python 3.12.3, no random seed, standard library, commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

**OPEN AT A NAMED STEP: MARKED-HISTORY L2 CONTROL.**
