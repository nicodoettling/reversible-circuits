# M157 plan: two-beta signed-current transfer

Date: 2026-08-13 UTC.

## Objective and declared target

The project target remains the uniform law on fixed-length identity
transposition words.  This mission concerns only the normalized full
unweighted reset excursion `F=H/q` of the auxiliary nonlazy
minimal-long-cycle parking projection.  It is not a sampler, a gap theorem,
or an original-chain claim.

The candidate is an exact two-copy beta representation which keeps the
signed cross-beta reset products discarded by M152's endpointwise Jensen
step.

## Tested claims

1. Derive the exact shared-observation posterior transfer for
   `V_K(kappa,D)=integral integral K dBeta dBeta`, including the killed
   `X=d` atom.
2. Express the exact reset energy as a signed two-copy beta integral.
3. Determine whether these formulas give a finite exact recursion and/or a
   nonnegative supersolution useful for the right-heavy budget.
4. Test the exact M152 witness and capped fresh states.  If a named
   positive-part or absolute-value repair fails, record the first exact
   counterexample and its mechanism.

## Parameters and caps

- `1 <= B <= 3`, `0 <= L <= 6`, `2 <= kappa <= 16` for broad diagnostics.
- Exact M152 witness `(B,L,kappa,D)=(3,6,2,1)`.
- Standard-library Python, exact `fractions.Fraction`, deterministic
  `seed=null`.
- No `L=7` support enumeration and no use of the rejected canonical-basin
  Bessel/frame inequality.

## Expected failure modes

- The shared-posterior RN kernel depends on `(kappa,D)`, so it may not close
  as one state-independent latent polynomial.
- The exact reset kernel is pointwise signed even though its beta-square
  integral is nonnegative.
- Taking a pointwise positive part or absolute value may recreate a Jensen-
  like loss and violate the right-heavy budget.
- A finite exact signed equality may be algebraically correct but offer no
  new scalar inequality beyond the original nilpotent recurrence.

## Planned artifacts and commands

- `two_beta_theorem.md`: derivation, scope, and first open inequality.
- `two_beta_exact.py`: standalone exact checker.
- `two_beta_exact.json`: machine-readable exact results.
- `checkpoint.md`, `report.md`, `freeze_manifest.md`, `SHA256SUMS`.

Planned command:

```text
python3 -B two_beta_exact.py --output two_beta_exact.json \
  --max-B 3 --max-excess 6 --max-kappa 16
```

