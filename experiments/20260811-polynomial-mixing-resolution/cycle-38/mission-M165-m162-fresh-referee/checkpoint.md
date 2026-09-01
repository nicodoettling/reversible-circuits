# M165 checkpoint

Date: 2026-08-13 UTC.

- Read the project skill, source-of-truth goal/sampling documents, experiment
  standard, and accepted M157/M160 scope.
- Recorded a documentation-path mismatch: `AGENTS.md` names
  `references/experiments.md`, while the existing file is
  `.codex/skills/reversible-circuit-sampler/references/experiments.md`.
- All five coordinator-supplied M162 hashes match exactly, and every entry in
  M162's complete `SHA256SUMS` verifies from its frozen directory.
- Algebraic audit so far supports the single-`pi_a` feature scaling and the
  normalized coefficient `m_s(d,t)q_child/q_parent`.
- Implemented a no-import weighted-feature reconstruction, distinct from
  M162's bivariate-kernel implementation.  It compresses identical
  univariate feature coordinates while preserving their exact positive
  weights.
- The compact run checks 42 shared-observation monomial pairs in three
  asymmetric beta cases and exactly the four decisive right-heavy repair
  states.  It reports zero failures.
- Every row matches the frozen exact `H/q`, trace, degree-one energy, `T_1`,
  and budget; scalar normalization, diagonal recursion, modal Parseval, and
  the first-mode recursion also agree exactly.
- Provisional disposition: `ACCEPT`, with no material objections and one
  harmless clarification that `T_1` at `L=0` needs the natural zero-extension
  of the absent degree-one mode.
