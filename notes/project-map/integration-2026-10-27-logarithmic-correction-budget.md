# Logarithmic correction-budget integration, 2026-10-27

Prior commit: `7640534e21b0cdf3cdf25d93201b74caa063cecb`.
User authorization: investigate the log(N) transposition correction budget,
without heavy simulation. This was a symbolic proof and small exact-check
pass, with no agents, installs, external messages, commit or push.

## Scope, evidence and status

Add ALT-LOG-CORRECTION v1, provisional. The six new artifacts contain a
minimum-correction-count injection, endpoint TV upper bound, prefix-lift
TV lower bound tending to one, two exact Hamming expansion families,
and an explicitly conditional static word-law transfer. Polynomial mixing
of the relaxed chain at general m>k remains unresolved. No original-chain
gap, mixing lower bound or asymptotic inference from small cases is claimed.

The author inspected all six artifacts and executed the self-contained
73-record harness. Permutation-state counts, actual legal gate sets and
coefficient counts provide separate arithmetic checks of the formulas.
The longest permutation table has 720 states; no circuit graph or Markov
trajectory was generated. The concrete N=2^20 and N=2^40 examples evaluate
proved bounds; they are not empirical data from those groups. Review is
by the author, not an independent referee. Negative findings are retained
in the ledger alongside the positive endpoint result.

The relation to ALT-RELAXED-HEATBATH is analogous-to, not supersession:
the old fixed-k2 spectral comparison and general-budget connectivity
remain unchanged. The new result only rules out a polynomial extension
using the actual worst-case completion-weight ratio. A does-not-imply edge
to G-HEATBATH preserves the unresolved exact local mixing frontier. No
accepted descendant, ranked target or main overview is upgraded.

The experiment reference gains a procedural warning to distinguish endpoint
permutation laws from word laws and to test extension multiplicities and
event masses before asserting prefix uniformity. This changes no mathematical
evidence source. Skill validation passes. HANDOFF and the manuscript remain
unchanged, pending independent review.

## Discovery review and preserved work

The working tree already contained the previous correction-gate comparison
experiment and its map/skill updates. Its six artifacts and receipt are
preserved unchanged. The baseline catalogue validated at 52 records and
134 sources, generated views matched, and all 19 map tests passed.

The reviewed candidate inventory at
`/tmp/reversible-log-correction-candidate.json` adds exactly the six new
experiment files and changes only the procedural experiment reference.
It removes no file and reveals no unrelated research drift. The map tree
is excluded under the existing self-reference policy; no policy changes
or new mission branches were introduced. The full 19-file dirty/untracked
inventory, including preserved previous work, is in the new report.

The new catalogue validates at 53 records and 140 pinned sources. No old
source fingerprint was refreshed. This receipt accepts discovery only,
not an independent theorem certification.

## Reviewed fingerprints

- `experiments/20261027-112519-logarithmic-correction-budget/check.py`: `e35e05a1ff4870eb9e31baaba8a09e2c3319941fe5c90c9e867dbfe0394795c2`.
- `experiments/20261027-112519-logarithmic-correction-budget/claim_ledger.md`: `2339654cc0c5743034cd7b033a1f65554752354dc7bc97e43e6ae7a04c032468`.
- `experiments/20261027-112519-logarithmic-correction-budget/plan.md`: `d848da9d2c70531022fd0863e9c2c86d2719298a2d92aaa38e7c168af7933f40`.
- `experiments/20261027-112519-logarithmic-correction-budget/proof.md`: `41278d134bce8b2d48cac6ca18c9a4eaadaf711db065b2909be115305146f168`.
- `experiments/20261027-112519-logarithmic-correction-budget/report.md`: `5596b2d30713266e6ab781a7fa0cd498675da950b16e98d50fbdf642ea590510`.
- `experiments/20261027-112519-logarithmic-correction-budget/results.jsonl`: `45b50e7a4f7a7fb28f656c060c199073f3b1cd6a38d7ad85f0b9810ca0d45b5c`.
- `.codex/skills/reversible-circuit-sampler/references/experiments.md`: `6171494207db081d522b88d432d9e31904cf48b7136a322d11e04b28b17a6d8f`.

## Verification

Accepted-inventory freshness, catalogue validation (53 records, 140 pinned
sources), deterministic rendering and all 19 map tests pass. Skill validation
and the exact experiment checks pass. Final whitespace and retrieval checks
are recorded with the finishing workspace inspection. These checks establish
repository consistency, not mathematical certification.
