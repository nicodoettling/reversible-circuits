# M305 fresh-audit request

Date: 2026-08-14 UTC.

Please audit this package without importing its verdict.

1. Reproduce every top digest and every payload row listed in
   `source_lock.md`, especially M91, M297, and M302.
2. Check the correlation-variation inequality and constants in
   `profile_implication.md`, including the distinction between a zero
   response profile and a possibly nonzero coefficient atom at that
   profile.
3. Verify Lemma 1 and Lemma 2 in `analytic_reduction.md` at the endpoints
   `k=3`, `s=h`, `s=h+1`, and `s=k-1`.
4. Check that the two-point marked-kernel construction refutes only the
   generic scalar-BV multiplier shortcut and is not presented as an actual
   model counterexample.
5. Verify the exact marked pushforward/Abel identity `(4.2)`, including
   `D_(k-1)=0`, both live channels, raw lifts, exact triangle `1/3` and
   side/negative `1/4` representation factors, actual owner incidences,
   phases, and seams.
6. Re-run only the already-declared `k=11` command if a finite check is
   needed; compare the exact JSON and the embedded M297 SHA gates.
7. Confirm the controlling stop: CMPAD/CBPV and SOCL are unresolved, and
   no BODT/DOR/PBV/FD/FCL1/gap/mixing/Terminal inference is licensed.

Suggested ledger entry:

```text
claim | status | assumptions | evidence | independent check | action
CBPV=>SOCL | proved conditional implication | M297/M302 interfaces | profile_implication.md | pending | audit
scalar split BV | proved all-rank | frozen Borel laws/ratios | analytic_reduction.md | pending | audit
generic multiplier shortcut | refuted abstractly | bounded arbitrary mark kernels | analytic_reduction.md | pending | retain negative
CMPAD/CBPV/SOCL | unresolved | full combined marked-profile cancellation | analytic_reduction.md | pending | next frontier
```
