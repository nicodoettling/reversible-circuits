# Live viability report — provisional checkpoint

Two explicit construction families now have complete provisional attack arguments beyond the known pair controls. Both attacks compare complete noisy words with the SAME Q_k applied to global U(N,L); no security candidate has survived. This is not a refutation of noise hiding for arbitrary structured sources. Exact-version reviews and candidate-specific implementation checks remain in progress.

candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict
---|---|---|---|---|---
C1 six-distinct-edge relator blocks + bounded scrambling | specified structured law versus global U | analytical proof; code gate pending | scrambling alone preserves orbit | inherited global baseline passed; candidate checks pending | provisional reject
C2 one path/star relation on a planted support + L^3 scrambling | specified structured law versus global U | analytical proof; code gate pending | scrambling preserves planted support | exact sparse reference count bound; code gate pending | provisional reject

attack | one sample / reused setup | effect size | sample/time cost | status
---|---|---|---|---
C1 aligned identity-window threshold | one query also breaks reused public setup | >=1-N! binom(B,ceil(B/2)) q^(-ceil(B/2)); concrete deficit exp(-Omega(lambda^6 log lambda)) | one sample; O(L) label operations | provisional full proof, coordinator analytical review
T0 unaligned six-window theorem | every key, one query; all-reply amplification stated separately | >=.7 for N>=1000 and surviving-window threshold>=M/2 | O(L); no mixing dependency | blind reconstruction and authored proof under review
C2 support threshold | one query also breaks reused public setup | >=1-min(1,binom(N,h)binom(h,2)^(2m)/D(N,m)); deficit exp(-Omega(lambda log lambda)) | one sample; O(L) expected dictionary operations | provisional full proof, author-distinct review requested
LC1 fixed local-observable transfer | generic one-sample transfer; setup must not reveal hidden-key test choices | alpha_s times original signed bias divided by 2*3^s | O(4^s q^s) test evaluations; polynomial for fixed s | 108 exact finite channel cases passed; blind proof reconstruction received

Full immutable proofs live in role directories and coordinator/local-channel-proof-v1.md. C1 general finite-family random-bit complexity has a preserved erratum (log L term); concrete law and schedule unchanged. Same-model reviews are correlated. Source disagreements and mission exclusions are in model-v1.md.

Bounded smoke passed. J001 exact regression suite passed: global counts 27/120/3936; empty/N2/odd cases; exact projection and endpoint tests; pair attenuation smoke; CP1 rejects the invalid marginal-product rule; local-channel finite basis checks. No experiment is currently active. See coordinator/job-registry.json and regressions-report-v1.md.

Recommendation remains provisional: redesign constructions to match global support statistics and remove bounded local relations before asking whether noise supplies further hiding. No third candidate or all-length sampler/mixing programme is authorized by this checkpoint. Highest-value remaining obligation is complete exact-version audit of the two finite attacks and literal-word code checks.
