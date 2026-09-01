# M222 plan: fresh immutable referee of M217

## Objective

Independently audit the frozen M217 signed averaged boundary-edit reduction, without modifying M217 or attempting the unresolved weighted boundary-edit estimate (WBE).

## Source lock

- `HANDOFF.md`
- `GOAL_SPEC.md`
- `.codex/skills/reversible-circuit-sampler/SKILL.md`
- `.codex/skills/reversible-circuit-sampler/references/sampling-problem.md`
- `references/experiments.md`
- the relevant frozen M217 artifacts and only directly cited local proof context

## Exact audit obligations

1. Verify the complete M217 `SHA256SUMS` inventory and claimed digest `7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557`.
2. Re-derive the unnormalised tilt `qhat_s=q_s a_F(s)`, including cancellation of the `A`-conditional normalizer.
3. Check all signs and definitions in `DE_Z=S_Z+K_Z+N_Z`, retaining both observables, both boundary kinds, seams, and collisions.
4. Check the exact formula for `a_F/a_L-1` and the uniform estimate `N_Z=O(k^-2)`.
5. Audit the Stirling route to `qhat_s <= C s^-3/2` and the tail `sum_{s>=m} qhat_s <= C/sqrt(m)`.
6. Explain why that tail control closes the reduction only when `ell` is comparable to `k`, not for fixed `ell`.
7. Verify that WBE, `|S_Z+K_Z| <= C sqrt(ell)/k`, implies the claimed DE bound.
8. Run a compact, no-import, exact rational formula check for `k=3,5`.

## Exclusions

Do not attempt WBE; do not audit DV, J2, PCR, any downstream spectral-gap claim, or either Terminal. Do not broaden finite scans.

## Deliverables

`checkpoint.md`, `proof_audit.md`, `checker.py`, `results.json`, `report.md`, `manifest.md`, and `SHA256SUMS`, followed by an explicit `ACCEPT` or `REJECT` verdict with numbered objections.

