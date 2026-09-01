# Mission M167 plan: all-suffix first-Jacobi boundary

Date: 2026-08-13 (UTC)

## Single target

Prove or refute the following falsifiable statement, in exactly the notation
and actual-history recursion frozen by M162:

```text
For every admissible B, L, and kappa,
T_1(B,L,kappa,1) <= 1 - q_(B,L).
```

This is the right-heavy, all-suffix, first-Jacobi (`t=1`) boundary only.
The mission will label the result `proved`, `refuted`, or `unresolved`.

## Source lock

Before theorem work, read the repository core sources required by `AGENTS.md`,
then the frozen M147/M151, M157/M160, M162, and accepted M165 artifacts.
Verify the freeze manifests and record any disagreement rather than choosing a
convenient convention.

## Method

1. Reconstruct M162's exact actual-history state, feature vector, first-mode
   recursion, common-attachment coupling, and killed `a=d` branch.
2. Algebraically isolate `T_1-(1-q_(B,L))`, with special attention to the
   high-mode tail and killed-atom contribution.
3. Seek a structural inequality valid for every admissible state. If it
   fails, give an exact counterexample and lift it to an infinite counterfamily
   when possible.
4. Use exact arithmetic only for identity checks or a compact witness. Do not
   enumerate `L=7` and do not broaden finite scans.
5. Falsify the proposed proof/counterfamily on boundary cases (`L=0`, empty
   modes, killed branches, and minimal admissible parameters as applicable).

## Forbidden closures and inferences

- Do not discard shared attachment observations.
- Do not drop the killed `a=d` branch.
- Do not reuse pointwise Jensen, diagonal-trace, generic-frame, or scalar
  deficit-blind closures already refuted by predecessor missions.
- Do not infer a spectral gap, Terminal, or polynomial mixing result.

## Deliverables

- `checkpoint.md`, initialized now and replaced/extended at halfway.
- A theorem note with statement, status, conventions, dependency ledger,
  complete proof or exact obstruction, first unresolved step if any, and
  boundary falsification.
- Compact exact machine-readable artifacts only if they materially audit the
  algebra.
- A nine-field `report.md`, freeze manifest, and SHA-256 ledger.

