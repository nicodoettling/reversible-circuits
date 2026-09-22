# Beyond the sparse sampling boundary — coordinator report

The unchanged component samplers extend beyond the old range, but fail the full proposed benchmark. The new smaller theorem is negligible-error global sampling for every even

    m <= (1/4) N^(2/3) ln N.

The obstruction proves that H0's error tends to one at an explicit sequence on m^4=N^3, even though H0 includes arbitrary genus on small supports. H1 fails there as well. Existence of another polynomial-time sampler for the full benchmark, T0, remains **unresolved**. This is an internally audited result, not external human certification or a novelty-priority claim.

## Exact outcomes and parameter map

Labels and positions are distinguished; products satisfy(ab)(x)=a(b(x)). The target is global U_(N,m), uniform on all length-m transposition identity words. N>=2, m even, P=N+m+2, K=max{v<=N:v^(2v)<=P^4}, fixed at top-level. H0 allows every component with g<=1 OR v<=K; H1 allows every component with v<=K. Small supports include ALL genera. No local-chain kernel or mixing result is used.

| Claim | Parameter range | Final mathematical outcome |
|---|---|---|
| Prior internally audited theorem | m^3<=N^2 | Retained as imported prior result |
| Old finite-tail corollary | m<=c N^(2/3)(ln N)^(1/3), fixed c<24^(1/3), eventually | Algebraic consequence of old bound; not a new mechanism |
| SB-T1.v1 | every even m<=N^(2/3)ln N/4 | Proved smaller extension for unchanged H0 and H1 |
| P0 / unchanged H0 at full benchmark | every even m^4<=N^3 | Refuted by SB-O1.v1 |
| P1 / unchanged H1 at full benchmark | same benchmark | Refuted, since B subset A |
| T0 / any algorithm at full benchmark | same benchmark | Unresolved; no sampling-hardness conclusion |

SB-T1.v1 uses one explicit error function:

    eta(N)=1                                      for2<=N<2^2048,
    eta(N)=exp[-(ln N)^2/(48 ln ln N)]             forN>=2^2048.

For each fixed a>0, eta(N)<=N^(-a) whenever ln N>=max(2048ln2,(48a)^2). The algorithm, fixed cutoff and polynomial exponent do not depend on a. Expected bit time remains O(P^20), storage O(P^10). These are bounds in N and m, not in log2(N) wires. The large finite threshold is a conservative theorem constant, not a practical onset claim.

SB-O1.v1 takes every integer j>=64 and sets N=2^(8j), m=2^(6j). Then m=m_*(N) exactly and m^4=N^3. It proves

    |A|/|Omega| <=2^(-1-jm/2),
    TV(H0,U) >=1-2^(-1-jm/2),
    TV(H1,U) >=1-2^(-1-jm/2).

The first threshold is N=2^512 on this sequence. This lower bound tends to one and directly refutes the uniform negligible-error assertions for both policies. It is stronger than a non-negligible-error obstruction, but it concerns these policies, not all algorithms.

## Why the two results hold

The positive proof retains information discarded by the old estimate. A component of size v and genus g uses cost q=v-1+g, with g<=k-v+1 when m=2k. The exact bridge-normalization incidence bound has a falling factorial(k)_q. Keeping it makes the finite genus sum a binomial rather than an infinite exponential. The resulting component tail supports the additional ln N factor. This changes the analysis, not the sampler.

The negative proof bounds the count of every allowed H0 profile, including arbitrary-genus small components, by a convergent positive component series. Its numerator is at mostm!(N^2/k)^k exp(8k) under explicit finite conditions. The total identity-word count is bounded below by words confined to a larger fixed subgroup, using exact midpoint Cauchy–Schwarz. At the boundary sequence the denominator dominates by the stated exponential factor. No independence model for support graphs or finite-data extrapolation enters either proof.

The exact samplers have conditional laws Unif(A) and Unif(B); their global errors are exactly1-|A|/|Omega| and1-|B|/|Omega|. H0 sends every g0/1 component to the unchanged genus-zero/one decoder, including small components, and uses support-marked decoding for allowed higher genus. H1 uses support-marked decoding throughout. The original cutoff is retained in every residual instance.

## Candidates, exact tests and secondary result

| Candidate | Exact output target | Identity / length | Global support coverage | Asymptotic verdict |
|---|---|---|---|---|
| Unchanged H0 | Unif(A) | valid by literal decoder proof and regressions | allg<=1 plus allgenusv<=K | promote SB-T1; reject P0 |
| Unchanged H1 | Unif(B) | valid; exact small forward laws checked | allgenusv<=K | promote SB-T1; reject P1 |
| New H2-QC.v1 | uniform on componentsv<=L, L=max{v:3^v<=P^4} | new literal quotient decoder audited | allgenusv<=L | keep exact primitive; reject as T0 rescue |

R4's targeted modification quotients prefix states by simultaneous label relabeling while retaining each exposed support block's cycle partition. At most3^(v-1) quotient states allow a larger cutoff L=Theta(logP), with conservative expected O(P^24) bit time/O(P^12) storage. Root reviewed and reran its actual forward choices. A separately versioned corollary shows that H2, and its union with allg0/1 components, still fail on the same boundary sequence. This negative finding is retained alongside the valid decoder.

The sufficient remaining connected primitive is stated in roles/r4-construction/reduction.md: uniformly accurate literal connected sampling for v>L,g>=2 with polynomial bit cost. Exact macro selection plus component errors2^(-b) gives global error at mostN2^(-b), with b=ceil(log2(N+2))^2. That primitive remains unresolved; this reduction is sufficient, not a claim that every T0 solution must use it.

Finite evidence includes all required S3,m4; S4,m4; S4,m6 counts/laws, boundary and zero-count handling, arbitrary-genus small supports, fixed top-level cutoff, actual forward laws, length1400 stacks, huge-integer serialization and distinct policy labels. New QC actual laws also include all2187 S3,m8 words. R3 tested53,300 exact component bounds and7,300 binomial sums/identities; corrected relaxed-exponent diagnostics cover150 eligible instances. Root independently reran55 majorant cells,80 profile-coefficient comparisons,390 subgroup lower bounds,197 binomial bounds and512 integer-sequence checks. Root's full QC rerun took about2.25seconds. All assertions passed; analytic proofs, not these finite grids, establish asymptotics.

One finite example illustrates why policy distinction matters: atN28,m12,K4, H0 error is18339750000/714036684356251 (about2.57e-5), while H1 error is190337199624000/714036684356251 (about0.2666). Neither number alone refutes an asymptotic negligible bound.

## Audit, provenance and reproduction

All five fresh requested gpt-6-astra/ultra worker contexts actually started. Backend model identity is not independently exposed; no substitution was requested. R5 froze its blind report at09:34:39 UTC before candidate disclosure, independently finding an all-m_star obstruction by a different low-genus bound. Its stronger claim remains preserved in the blind artifact; the canonical accepted theorem uses the separately audited explicit sequence. Same-model agreement is correlated.

R1 and R2 cross-audited the obstruction and positive bound. R3 provided exact diagnostics and a nonauthor obstruction audit. R4 audited unchanged all-length algorithmic dependencies. R5 checked source normalization, both candidate proofs and exact canonical integration. Root checked the primary DYZ source, all load-bearing proof steps, decisive tests and the new QC decoder. The final exact-version disposition and hashes are in claim_ledger.md and the referee reports.

Two presentation/test issues were preserved and repaired: the initial exponent diagnostic testedbinom(N,v) instead of the proof's relaxedN^v/v!;v2 tests both. The first canonical algorithm summary ambiguously described H0's small low-genus dispatch; the corrected version states the actual branch predicate and received fresh review. Neither changed the mathematical theorem or unchanged sampler code. All historical negative regressions remain in regression_registry.md.

Repository commit20e86f665f69053031fe7eec0c3388458affb1fc; Python3.12.3; standard library only. Stochastic validity checks use1729,2718,31415; exact proofs/tests use no seed. Runs were supervised, initially timeout90s, with at most two expensive checks. Commands and detailed domains/timings are recorded in raw JSON.

From the repository root:

```sh
timeout 90s python3 -B experiments/20260922-sparse-boundary/coordinator_checks.py --output /tmp/sparse-boundary-root-checks.json
timeout 90s python3 -B experiments/20260922-sparse-boundary/roles/r4-construction/validate.py --output /tmp/sparse-boundary-qc-checks.json
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 4 --m 6 --seed 1729
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 28 --m 12 --certificate-only
```

All research changes are under experiments/20260922-sparse-boundary and individually inventoried in changed_files.txt. Initial/pre-existing untracked work and launcher-owned artifacts are listed separately. Old source hashes are checked unchanged; no HANDOFF, manuscript, AGENTS, GOAL_SPEC, skill, configuration, commit or push changes occurred. The older local-mixing objective was explicitly superseded by the user's global sampling task.

The cap began09:25:28.937730 UTC, with wrap-up10:15:28.937730, graceful shutdown10:24:23.937730 and hard deadline10:25:28.937730. No cap reset, new run, detached job or automatic restart occurred. Native goal completion and usage are recorded only from the actual tool return in completion_record.json once delivery verification closes. T0 remains unresolved even when this disjunctive research goal completes via the audited obstruction and smaller extension.

Final delivery verified and native goal marked complete at2026-09-22 09:49:17 UTC, well before wrap-up. The actual tool returned810,751 tokens and1,411seconds (23minutes31seconds) of native goal usage, with no token budget. Completion rests on the closed mathematical/audit graph and saved artifacts, not on worker report completion or time expiry. All five worker turns are finished; no computation or automatic continuation remains. Final file/source inventories were refreshed after saving this accounting record.
