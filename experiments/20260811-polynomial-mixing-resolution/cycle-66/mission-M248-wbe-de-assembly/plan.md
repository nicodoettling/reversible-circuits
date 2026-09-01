# Mission M248 plan: WBE and signed averaged DE assembly

## Objective

Assemble a standalone exact theorem, using only frozen accepted inputs, that proves the weighted boundary estimate (WBE) for the exact observables `X_ell` and `Y_ell` and then the signed averaged defect estimate (DE).

## Scope and labels

- Target: the exact combinatorial observables in the accepted M217/M222, M226/M229, M235/M238, and M239/M246 artifacts.
- Parameter regime: odd `k >= 3` and `2 <= ell <= (3k-1)/2`.
- Intended conclusion: **proved**, conditional only on the cited frozen inputs retaining their accepted status.
- Required constants: `7000` for `Y_ell`-WBE and at most `7160` for `X_ell`-WBE; propagate the accepted normalizer remainder into DE.
- Forbidden inference: no DV, conditional J2, PCR/WPCR/SCBR, gap, mixing-time, or Terminal conclusion.

## Dependency audit

Read every relevant frozen artifact in:

1. M217/M222: exact `DE = S + K + N` reduction and normalizer remainder.
2. M226/M229: exact Y/T coefficient identities and the conditional implication.
3. M235/M238: accepted TCM with constant `160`.
4. M239/M246: accepted YCM with constant `7000`.

Check exact domains, normalization, kind/seam/collision conventions, signs, and theorem status. Any disagreement is an obstruction, not something to repair silently.

## Proof route

1. Recover the exact definitions of YCM, TCM, WBE, and DE from the frozen sources.
2. Apply accepted YCM directly to `Y_ell`.
3. Use the exact coefficient identity for `X_ell - Y_ell` plus TCM and the triangle inequality to obtain `7160` for `X_ell`.
4. Insert WBE into the accepted M217/M222 identity and bound the normalizer remainder with its accepted estimate.
5. Perform only compact, no-import arithmetic/domain checks.
6. Freeze theorem, report, command/output record, manifest, and hashes; then request an immutable fresh referee.

## Expected failure modes

- A source is not actually frozen or accepted.
- M226/M229's TCM-to-`X-Y` identity uses a different normalization or domain.
- M217/M222's `N` estimate is only qualitative or has a hidden restriction that prevents a universal explicit DE constant.
- Endpoint, seam, or collision terms were removed in an earlier informal summary but remain in the exact formulas.

