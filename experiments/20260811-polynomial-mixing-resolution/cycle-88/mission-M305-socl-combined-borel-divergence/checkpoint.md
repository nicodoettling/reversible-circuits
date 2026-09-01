# M305 initial checkpoint

Date: 2026-08-14 UTC.

- Read the project skill and the complete frozen M297 proof/addendum/report.
- Read M302's clean-room acceptance and both notation guards.
- Reproduced both immediate top digests and every manifest row.
- Fixed CBPV in `plan.md` before any new computation.
- Locked the exact size conventions: formal `u_1=0`; every row with index
  one vanishes; only `Delta A_2` and `Delta A_3` vanish among the remaining
  small-size rows.
- Next: source-lock every imported predecessor, prove the deterministic
  profile-TV implication, and derive or refute the first complete Borel
  complementary-gap coefficient identity.

## Final checkpoint

- Every cited inventory, now including M91, passes byte-for-byte.
- Proved exact `CBPV => SOCL`, with the zero-profile atom distinction.
- Proved the all-rank Borel ratio envelope and
  `sum_s |Delta(p_s-q_s)|=O(1/k)`.
- Refuted the generic scalar-BV multiplier shortcut; this is not a
  counterexample to CBPV.
- The sole predeclared `k=11` guard survives with maximum normalized CBPV
  values `2.3543`, `0.8659`, and `4.9294` for H, A, and C.
- Frozen `(CMPAD)` as the first standalone unresolved lemma.  SOCL and all
  downstream claims remain unresolved pending fresh audit.
