# Frozen game M0, version 1

N>=2, L>=0 even, 0<=k<=L; q=N(N-1)/2; T_N all transpositions; mu uniform. Products act rightmost first, (p q)(x)=p(q(x)); words are ordered lists of unordered label pairs. U(N,L) is uniform over ALL labeled ordered transposition words with product identity. No connected conditioning, quotient, or Hurwitz orbit is substituted. Odd L is infeasible; L=0 allows only k=0; N=2 has one word for every even L.

A candidate supplies Setup(1^lambda), exposed A and any hidden K, exact sampler D_(A,K) with fresh independent uniform tapes, precise representation and polynomial costs in declared N,L,lambda. State whether sampling uses a secret and whether per-word secrets are fresh. Reused setup retains the same (A,K) while all word/noise tapes are fresh. Public A is identical in both worlds and reference U is independent of setup. One-sample and every-polynomial-number-of-requests claims are distinct, as are every-key and average-setup claims. No decoder oracle exists.

Q_k chooses a uniform k-subset I of [L], independently of the word, setup and all other tapes, replaces each selected coordinate with independent mu, and hides I and its draws; replacement may equal old value. Compare complete observed words Q_k(D) and Q_k(U), exposing A. Fixed positions and Bernoulli replacement are not M0. Advantage is |Pr[test=1 in structured world]-Pr[test=1 in reference world]|; success with equal priors is (1+advantage)/2.

Semantic correctness means disagreement of the computed permutation with identity on uniform x in [N]. The elementary support bound is <=min(1,4k/N); it is an upper bound only and does not establish negligible error for nonzero polynomially related k,N. Hiding noise and any later transmission noise are separate. No PRC detection or false-positive notion is imported.

For every asymptotic statement supply an explicit lambda schedule or declare a finite parameter theorem. Time polynomial in N,L is not automatically polynomial in log2(N) wires. Statistical claims need proof; computational claims remain conjectured absent a checked reduction to an established assumption. Passing tests certifies neither.

Mandatory source regressions: stable-sort Hurwitz subsequence law under global U; conjugated replacement telescoping and non-iid old B tuple; parity-aware p_(2k) endpoint behavior; pair-equality attenuation; repeated-single-transposition endpoint counterexample; doubled/mirrored syntax controls; common sign/distance/support endpoint restrictions are not attacks. The frozen foreground report is evidence, not independent certification.

Source disagreement: historical AGENTS/HANDOFF describe irreducibility as conditional while PROJECT_MAP records inherited acceptance; this mission does not use that input. GOAL_SPEC historically excludes hardness, explicitly overridden by the authorized frozen M0 mission. The operator snapshot map is later than the tracked map; neither authorizes sampler/mixing work here.
