# M251 report: adjacent-split DV restart

Date: 2026-08-14 UTC.

## Verdict

```text
PROVED: exact paired short/long difference identity.
PROVED: Y-profile DV with constant 18400.
UNRESOLVED: X-profile DV, reduced solely to literal two-run TAV.
NO DE/J2/PCR/GAP/MIXING/TERMINAL INFERENCE.
```

The target is the unweighted adjacent-split profile variation from accepted
M192/M195.  The setting and composition convention are exactly those of
M199/M207: odd `k>=3`, `D=2k-1`, `R=2k-3`, and the normalized literal
B-side ordered-disjoint-double law.  This is not a new Markov kernel or a
global identity-bridge theorem.

## Exact paired identity

`paired_difference_identity.md` puts `s` and `s+1` on one common triangular
tuple domain.  The expanding short and shrinking long pieces are paired
before absolute values.  The identity isolates survivor/cutoff, common
smooth kernel, common seam, boundary strip, and normalization blocks.  The
leading `1/R` normalization derivatives cancel exactly, and the paired
boundary formula cancels its common `b_d/R` coefficient.

## Proved Y theorem

For the one-run profile, the common seam edit vanishes.  The exact scalar
operator annihilates constants.  Finite Abel expansion therefore reduces
the explicit three-atom seam incidence profile to head cutoffs.

The decisive proved Borel estimate is

```text
|Delta W_r(t)|<=3/R,

|Delta W_r(t)-B_t/R|<=120sqrt(t)/(Rr),  r>=2t+2.
```

The first inequality follows from the exact Borel convolution after a
signed likelihood-ratio increment is bounded in absolute value; no false
monotonicity claim is used.  In the far regime, log-ratio derivatives give
the second inequality.  Pairing short and long parents cancels `B_t/R`.
After survivor and normalization terms, the head response has weighted
variation at most `2300sqrt(t)`.  The explicit seam profile has weighted
cutoff variation at most `8sqrt(l)`.  Hence

```text
sum_s sqrt(s)|Phi_(s+1)^D(Y_l)-Phi_s^D(Y_l)|
 <=18400sqrt(l).
```

This is a universal analytic theorem, not a finite-data inference.

## First remaining lemma

Let `Theta_s(l)=Phi_s^D(X_l)-Phi_s^D(Y_l)`, the literal expected indicator
of the complementary two-run face.  The sole remaining X obligation is

```text
sum_s sqrt(s)|Theta_(s+1)(l)-Theta_s(l)|<=Csqrt(l).
```

Its full tuple formula is (5.1) of `y_dv_theorem.md`.  It retains both seams,
all ordered kinds, and collision multiplicities.  This mission does not
weaken it to an unpaired total-variation estimate.

## Diagnostic and self-attack

Only after the exact paired identity was fixed, the deterministic
formula-only Y diagnostic tested selected `k<=201`.  Its largest recorded
Y-DV ratio was approximately `1.690528` at `(k,l)=(201,2)`; unweighted
profile variation stayed below `1.988`.  This is finite falsification only.

A tempting proof that every individual Borel coefficient increment is
nonnegative is false near the long boundary.  The theorem instead bounds
the absolute signed increment through the full convolution; this correction
is material to the proof route and is recorded explicitly.

## Scope and action

M245 was treated only as interrupted read-only reconstruction.  No M245 file
was accepted or edited.  No `q` or `qhat` weight entered DV.  No claim about
DE, conditional J2, PCR/WPCR, a spectral gap, mixing, or a Terminal follows.

Action: freeze the exact identity and proved Y theorem; keep `(TAV)` and the
X clause of DV open; request a fresh immutable audit.

## Reproducibility metadata

- Repository commit at start/freeze: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Runtime: Python `3.12.3`; standard library only; no nonstandard
  dependencies; deterministic computation with `seed=null`.
- Exact retained command:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-67/mission-M251-dv-restart/formula_diagnostic.py --output experiments/20260811-polynomial-mixing-resolution/cycle-67/mission-M251-dv-restart/formula_diagnostic_results.json
```

- Parameters are the finite selected rows recorded literally in
  `formula_diagnostic_results.json`, capped at `k=201`.
- Validation: both JSON files parse, the retained command replays, and scoped
  `git diff --check` passes.
