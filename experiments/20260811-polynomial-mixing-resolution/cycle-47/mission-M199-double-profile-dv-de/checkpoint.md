# M199 Checkpoint

## Start checkpoint

- The owned directory and plan were initialized before substantive work.
- M192/M195 and the accepted predecessor chain are immutable.
- The target is only `(DV)` and `(DE)` for the conditional `J=2`
  disjoint profiles, with every kind/color/collision retained.
- No analytic conclusion or finite diagnostic has yet been adopted.
- `(DV)`, `(DE)`, the conditional `J=2` prefix estimate,
  `(PCR)/(WPCR)`, `(SCBR)`, and all downstream claims are open at start.

## Immutable-gate checkpoint

- Every entry in the frozen M174, M178, M180, M182, M186, M189, M192, and
  M195 checksum manifests passed. No predecessor was edited.
- Checksum-file digests, in order, are
  `fea1f624...51ba`, `6ca82e9f...1fba`, `b362d629...76d6`,
  `4b5f96b5...c9ad`, `9d5aa5ff...d7bd`, `893275dc...ce66`,
  `4c6cd295...36c60`, and `1f0c398b...3f0a`.
- The accepted starting interface is therefore the literal disjoint ordered-
  double law `Phi_s^D,Psi_s^D`, not a kindwise or collision-deleted
  approximation.

## Halfway substantive checkpoint

- Put `D=2k-1`, `R=D-2`, and `K_R(r,d)=b_d b_(r-d)/(R b_r)`.
  Conditional on a B first split `s`, the disjoint second edge lies inside
  one marked piece `r in {s,D-s}`. A source cut of size `d` has
  `r-d-1` nonincident placements and exact per-placement mass `K_R(r,d)`.
  Dividing the resulting literal ambient-face sum by `1-gamma_L(s)` gives
  `Phi_s^D` exactly.
- On the A side the same marked-piece sum has `r in {s,k-s}` and
  denominator `R=2k-3`, plus a disjoint edge in the untouched `k`-cycle
  with total mass `(k-1)/(2k-3)`. Division by `1-gamma_F(s)` gives
  `Psi_s^D` exactly.
- The one-run B faces are evaluated by the two-seam exterior word
  `v=(1,...,k-1,2k,...,3k-1)`. The two-run face is its complement after
  the two one-run faces are removed. This is a literal deletion/merge map:
  same/cross placements, both double colors, unit gaps, shared-endpoint
  deletion, and repeated component sizes are all still present.
- Independent exact reconstruction verifies these closed one-run and two-run
  formulas for every prefix at odd `k=3,5,7,9`.
- No finite counterexample appears. At `k=9`, the `(DV)` ratios are
  `1.3330557` for `Y_l` and `1.2427734` for `X_l`. A stronger pointwise
  comparison has `max k|Phi_s^D-Psi_s^D|/sqrt(l)=1.0050587`, which would
  imply `(DE)` after averaging, but these finite constants prove nothing.
- The remaining analytic certificate is now sharply isolated: bound the
  change in the marked interval kernel under `s -> s+1` by the incidence of
  the added/deleted boundary point plus the derivative of
  `1/(1-gamma_L(s))`, and bound the two-seam B/A embedding defect. Until
  those estimates are proved, both `(DV)` and `(DE)` remain open.
