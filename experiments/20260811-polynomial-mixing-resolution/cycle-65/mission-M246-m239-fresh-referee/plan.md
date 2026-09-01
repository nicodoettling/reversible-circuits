# M246 plan: fresh immutable referee of M239 YCM

## Scope

Freshly audit the frozen M239 YCM sufficiency package only.  Do not promote or
infer TCM, WBE, DE, DV, J2, or any downstream result.

## Inputs to freeze and verify

- M239 frozen directory and advertised top digest
  `66c78dd3aab40acc6166857f96f3afd90bba64184d7f139783d395667d21f542`.
- The exact M226/M229 coefficient reduction used by M239.
- The accepted M241/M243 ratio/strip lemma package, as recorded in the ledger.

## Independent audit obligations

1. Reconstruct the YCM statement, domains, and probability notation.
2. Re-derive GG1 survivor, short-shift, and long-shift estimates and every
   cancellation used in their aggregation.
3. Re-derive the small-`y` B estimate and the repaired A estimate, explicitly
   checking that the `QP` triangle is bounded by safe constants `72/80` and
   never by the stale constant `40`.
4. Check the middle range, all below/at/above-seam domains, and the final
   prefix constant `<=7000`.
5. Check exceptional odd cases `k=3,5,7` exactly.
6. Write an independent exact-rational or certified-interval checker that
   imports no M239 code and covers all finite/small boundary cases.
7. Issue an explicit `ACCEPT` or `REJECT`, with numbered objections if any,
   then freeze this referee directory with SHA-256 hashes.

## Standards

- All claims are limited to YCM.
- Any dependency is quoted with exact statement and domain; no silently
  strengthened lemma is allowed.
- M239 remains immutable throughout the audit.
- Final artifacts: `checkpoint.md`, independent checker, machine-readable
  results, `report.md`, `freeze_manifest.md`, and `SHA256SUMS`.
