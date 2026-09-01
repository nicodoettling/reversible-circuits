# M79 plan: M76 fresh referee and reset-resolvent attack

Date: 2026-08-12. Base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and scope

Freshly referee the frozen M76 report with report SHA256
`376c27b991073c97899071e8c2f31ea5806179f0c15289a485d4e91faabec7ae`
and manifest SHA256
`be966da6865c2015dee7f585a9fa68a84582f084553643420dcfe5e427f5a2e1`.
The mathematical target is only the auxiliary nonlazy stationary-flow
parking projection `Pbar_r` in the minimal long-cycle sector. It is not the
uniform identity-word target and not the original lazy `{3,4,5}` heat-bath
kernel `K`.

## Referee checks

1. Independently verify strict descent of `P=s+K-R` and the reachable mark
   closure.
2. Verify the infinite right-heavy counterfamily against every fixed-power
   one-step potential claimed in M76.
3. Re-derive and exactly check the seed-kernel coefficients `A`, `C`,
   `M_B(t)`, and the scaled/unscaled normalization.
4. Check that inverse-split-mass superharmonicity for
   `K_reset=(I-D)^(-1)J_can` implies the stated polynomial occupation and
   inverse-`q` bound, including nilpotence and the number of reset epochs.
5. Independently compare the raw `(D+J)` row with the pure-deep-eliminated
   row on the smallest decisive cases.

## Post-referee attack

Attempt the standalone inequality

```text
sum_y [(I-D)^(-1)J_can](x,y)/q_y <= 1/q_x
```

for every right-heavy context. Search first for an exact finite
counterexample. If none appears, transform by `h=1/q` and seek an explicit
supersolution of the `D` resolvent using exact child `q` ratios. Keep any
finite scan labeled as a falsifier/calibration only.

## Reproduction and expected failure modes

All scripts will be deterministic Python 3 programs using exact rational
arithmetic on the smallest ranks and documented floating arithmetic only for
larger bounded scans. Raw output will be JSON. Expected failures include a
missing factor of the root degree in canonical capacity, confusing raw with
eliminated rows, treating a finite margin as an asymptotic theorem, or
silently extending an auxiliary `Pbar_r` statement to the original chain.

Verdict will be `ACCEPT` or `REJECT` with numbered objections, followed by a
separate status for the new inequality attack.
