# Conductance audit claim ledger

Date: 2026-11-24. Status `proved` means the displayed mathematical argument
survived this single-session audit, with the listed proof expansions. It does
not mean formal verification or independent human refereeing. Exact checks
are falsification attempts, not proofs of asymptotic assertions.

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
| --- | --- | --- | --- | --- | --- |
| Connected count (CB.1) | proved | Ordered labeled transpositions, rightmost-first product, connected used support | Manuscript Lemma `connected-map-bound`; source p.2 | Reconstructed tree/cotree encoding; checked Hurwitz-map correspondence in CLW Definition 1.3/equation (10); finite face/genus checks | promote |
| Conditional switching (CB.2)-(CB.3) | proved | Even m <= c0 N; 2 <= k <= K <= m/2 | Manuscript Lemma `component-switching` | Weighted double counting handles variable available alphabet; exact component assembly and 30 conditional-moment comparisons | promote |
| Balanced cap exists | proved | Each sufficiently large even m; existential N in stated interval | Theorem `balanced-bottleneck` proof | Recomputed entropy comparison and adjacent-N jump; no monotonicity assumed | promote |
| Pair flow exponentially small | proved | Exact pair kernel; same balanced cap | (CB.5) | Classified nonidentity pair fibers and square boundary; exact small cut flows | promote |
| Bounded-slot extension, including project kernel | proved | Uniform stationarity; at most b changed positions, fixed b; growing b only in stated little-o regime | (CB.6) and TV argument | Contracted old components; stationary reverse flow; averaged exit probability plus Markov inequality | promote |
| Universal polynomial mixing for project kernel | refuted | Quantification over all N>=3 and even m>=4 | Above theorem with b=5 | N is polynomially bounded in m, while mixing lower bound exceeds every such polynomial | retire universal positive target |
| Parity smoothing (CB.7) | proved | v>=2, integer r>=1, parity-compatible x | Long-profile theorem proof | Recomputed conjugate-character pairing, row-size ratio and tableau sum; v=2 exact | promote |
| Long-length profile conductance Theta(N^-3) | proved | Pair heat bath; even m >= C N log N, large N | Theorem `long-profile-conductance` | Checked dense merger stays dense, reverse disconnection estimate, and unused-label upper cut | promote only at stated kernel/scope |
| Full conductance >=delta phi/(delta+phi+2) | proved | Restricted-profile conductance delta, singleton convention as stated | Same theorem | Checked rounding even when rounded mass exceeds 1/2 | promote; delta remains unbounded below |
| All-endpoint pair connectivity | proved | Same feasible endpoint and length, N>=2 | Lemma `all-endpoint-pair-connectivity` | Reconstructed vertex sweep and unchanged square transport; exhaustive endpoint fibers through S4,m6 | promote; no normal-form congestion inference |
| All-length pair conductance bound (CB.8) | proved | N>=3, even m>=2 | Proposition `coarse-pair-conductance` | Checked connector parity, ordered-pair reconstruction and cut counting without path-length factor | promote |
| Polynomial full mixing at m=N^2 | unresolved | Pair/project kernels, growing N | No inverse-polynomial restricted-fiber bound supplied | Long-profile theorem only controls profile unions | retain as separate research question |
| Impossibility of efficient direct sampling | unresolved; not implied | Arbitrary sampling algorithm | Local-walk obstruction has restricted algorithmic scope | Existing dense direct sampler is compatible | do not claim |

No subagents or additional independent reviewers participated. The independent
checks above are rederivations and exact calculations distinct from the supplied
draft's prose, performed in this audit session.
