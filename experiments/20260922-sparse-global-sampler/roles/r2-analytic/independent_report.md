# Independent analytic report R2-A.v1

Frozen before cross-review, 2026-09-22 05:54 UTC.

**Result:** provisional complete analytic proof of T0's omitted-mass obligation, with the stronger regime m^3<=N^2 (version T1). Full independent derivation: proof_v1.md. No R1 proof or candidate artifact was read before this report. Parent messages disclosed that the coordinator and R1 found related factorial-majorant arguments only after this worker had independently communicated its own argument.

**Status:** proved candidate, not yet nonauthor accepted. The proof uses the DYZ positive recurrence, with normalization checked directly against the primary source, and elementary weighted counting. It does not use any random-graph independence, Markov-chain result, asymptotic Hurwitz estimate, or numerical extrapolation.

**Main estimate:** for k=m/2, d=N-2k+1, a=k(k+1)^2/(9d^2), and q=4exp(1+a)Nk/d^2<1, the global uniform probability of ANY support component larger than K is at most min(1,Nexp(1+a)q^K/(1-q)). This stronger event contains the H0 omitted event. In T0 and N>=2^145, the bound is exp(-log(N)^2/[12loglog(N)]); in T1 m^3<=N^2 it is exp(-log(N)^2/[16loglog(N)]). Use one below-threshold bound of 1. These are uniform negligible errors with fixed algorithms/constants.

**New count bound:** A_g(v)<=A_0(v) B_v^g/g!, B_v=sum_(j=1)^(v-1)j^2/12. It follows by a coefficientwise exponential majorant of the normalized degree-split recurrence, whose weights sum to one. The factorial in g is essential; the inherited geometric genus bound need not suffice near the target range.

**Simpler consequence:** restriction to ALL components of size <=K already suffices, so a versioned small-support-only sampler removes the genus-zero/one generator dependencies from the global existence proof. H0 remains valid and is a larger subset.

**Exact tests:** verify.py (standard library Python 3.12.3, no imported old code) writes results.json. It checks 156 rational majorant cells through v=12,g=12; all incidence-ratio cells through N=12; all raw words in (3,4),(4,4),(4,6),(3,6) and boundary cases; exact marked-component label/position factors; coefficient and B inequalities. Eleven test groups passed in under one second. These checks can refute algebra errors but do not replace the asymptotic proof.

**Scope:** mathematical novelty is the derived factorial majorant plus marked-component incidence/tail combination; the connected recurrence and minimal counts are imported results. This worker implemented independent verification only, not a sampler. The global theorem still requires exact DP/assembly implementation and polynomial bit/runtime audit, plus a nonauthor review of this precise proof. No named-method obstruction was found; no hardness conclusion is drawn.

**Verdict:** promote to adversarial nonauthor audit. First remaining gate: independent review of proof_v1.md and its exact DYZ normalization, followed by sampler/complexity integration.
