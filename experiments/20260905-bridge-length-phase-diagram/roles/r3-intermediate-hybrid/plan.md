# Component/surplus law and hybrid reduction

Role: `r3-intermediate-hybrid`. Started 2026-09-05 15:12 UTC; coordinator
deadline 18:09:34 UTC. No subagents. Own this directory only.

Target: the uniform law on all length-`m` transposition identity words on
`[N]`; connected conditional laws are separate internal primitives.
Convention: `(alpha beta)(x)=alpha(beta(x))`. All samplers must produce an
exact identity endpoint. No Markov-chain mixing claim is in scope.

1. Prove the labeled component, length, surplus, and interleaving
   disintegration, retaining every multiplicity.
2. Give a positive assembly dynamic program with explicit integer and bit
   complexity; determine whether the cited DYZ positive recurrence computes
   its connected counts in polynomial time.
3. Audit the already accepted DPS minimal connected sampler input. Test
   whether the count recurrence itself yields connected sample generation,
   and whether short/minimal/dense conditional primitives make a complete
   hybrid. State exactly the first remaining primitive if they do not.
4. Independently enumerate `S_3,m=4`, `S_4,m=4`, `S_4,m=6` and boundaries;
   test exact counts, normalization, per-word assembly probabilities,
   endpoint validity, and the danger of conditioning every component minimal.

Named sources: M02 `proof.md` (only its component formula), M12 `report.md`
(only connected count recurrence/ratios), M112 `report.md` and M119
`report.md` (only rooted minimal product encoding). M12's report does not
display the full DYZ recurrence, so its cited `checkpoint.md` is read solely
to recover that formula; it still omits the genus-independent coefficient.
Coordinator is reconciling the primary DYZ source. M112's cited
`dps_local_audit.py` is read solely for the explicit closure map and runtime.

Repository commit: `9cc740b29eda6dd38adfde5f0aadc4a9c4eeb6fc`.
Python: 3.12.3. Dependencies: standard library only. Exact checks use no
random seed; any random sampler smoke checks will record fixed seeds.

Expected failure modes: missing factorial/root quotient; treating count-only
recurrences as sample bijections; replacing global uniform by a minimal-only
conditional law; using an unconditioned dense bridge as a connected sampler
without bounding the conditioning probability. Finite checks may falsify
claims but cannot certify asymptotics.
