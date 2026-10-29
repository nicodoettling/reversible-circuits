# Blind supplement BS2: statement T0

Frozen 2026-10-29 after BS1. Additional input is only `r1-theory/statement-T0.md`; no r1 proof/status or adjacent files have been read. The full prior input list is preserved in B1 and BS1. No new mathematical computation executed. This is a provisional independent blind derivation; same-model review is correlated.

## General local bound: reconstruction

Let even r>=2 and even L>=2r. Conditional on exactly s of a chosen r-window's coordinates being replaced, B1's exact formula gives its identity probability as

    sum_h p_s(h^{-1}) p_(r-s)(h) p_(L-r+s)(h^{-1}) / p_L(id).

Put a=L-r, which is even. Symmetry and Cauchy-Schwarz give p_a(g)<=p_a(id) for every g: write p_a=p_(a/2)*p_(a/2), and compare the inner product of p_(a/2) with its translated copy. Since convolution with a probability measure cannot increase the supremum, p_(a+s)(g)<=p_a(id). The sum is therefore at most

    p_(L-r)(id)/p_L(id) * sum_h p_s(h^{-1})p_(r-s)(h)
      = p_r(id) p_(L-r)(id)/p_L(id).

This holds for every s and hence under the hypergeometric mixture, including k=L. It requires no untouched-window event or false product of survival marginals.

To bound the return ratio, use the finite self-adjoint transition matrix P of the symmetric transposition walk. The sequence a_n=p_(2n)(id) is a positive weighted moment sequence of the squared real eigenvalues: a_n=sum_j c_j x_j^n with c_j>=0 and 0<=x_j<=1. Cauchy-Schwarz makes a_n log-convex, so a_(n-d)/a_n is nonincreasing in n for any fixed positive integer d. With d=r/2 and n=L/2>=2d,

    p_(L-r)(id)/p_L(id) <= p_r(id)/p_(2r)(id).

Thus T0's general local bound follows. All denominators are positive: a fixed repeated transposition is an identity word at every even positive length, and p_0(id)=1. The spectral representation is a finite elementary matrix fact, not an asymptotic mixing assumption.

## Six-window threshold and candidate class

A cyclic rotation of M disjoint length-six identity blocks leaves at least M-1 complete nonwrapping identity windows. Simultaneous conjugation preserves their products. Each subsequent adjacent Hurwitz move changes only two consecutive positions and can affect at most two of these fixed disjoint witness windows; at most 2B witnesses are lost. Q_k then affects at most k of the surviving disjoint windows. Thus the final count over all nonwrapping six-windows is at least H=M-1-2B-k pointwise, regardless of setup-dependent/adaptive choices of the construction or move locations. There is no claim that the adversary knows which windows witnessed the bound.

The reference has L-5 windows. Each has probability <=beta_N=p_6(id)^2/p_12(id), and Markov gives false acceptance <=min(1,(L-5)beta_N/H). If H>=M/2 and beta_N<1/40, then this is <12/40=3/10, proving advantage >=7/10. The sparse literal permutation calculation touches at most twelve labels per window, so its stated polynomial and linear-in-L word-RAM cost is reasonable.

## Reconstructing the numerical bound without long-walk mixing

Let F_j(N)=|Omega(N,j)|. Then beta_N=F_6(N)^2/F_12(N): q factors cancel. The exact six-step count is

    F_6(N)=binom(N,2)+240 binom(N,3)+2970 binom(N,4)
               +3600 binom(N,5)+1350 binom(N,6).

Derivation/dependencies: each connected active component on v labels consumes at least 2(v-1) gates. At total length six, the possibilities are one component (v=2,3,4), two components with lengths 2+4 (support sizes 2+2 or 2+3), and three length-two components. The exact connected counts at length six are 1 on two labels, 240 on three labels, and 2880 on four labels. The three-label count is 3^5-3=240; the four-label count follows from the permitted complete global enumeration count F_6(4)=3936 after subtracting 6+4*240+90=1056 disconnected words. This finite count is an explicit verification dependency, not an unproved universal connected-count formula. Two disjoint edges with lengths 2+4 contribute 3 pairings *2 choices *15 interleavings=90 per four-set, making 2970. A three-label length-four component (24 words) plus an edge contributes 10*24*15=3600 per five-set. Three doubled disjoint edges contribute 15 pairings *90 interleavings=1350 per six-set. Length-four connected count 24 on three labels follows from F_4(3)=27 minus three single-edge words. All decompositions are exhaustive by the component length bound.

For F_12, count only six pairwise vertex-disjoint edges each used twice. There are

    F_12(N) >= (10395/64)*(N)_12.

Indeed choose twelve labels, a perfect matching, and an interleaving of the doubled edges. Their products are identity because disjoint edges commute. This is a lower bound, with no claim that these exhaust length-twelve bridges.

Using binom(N,j)<=N^j/j!,

    F_6(N) <= (15/8)N^6*(1+16/N+66/N^2+22/N^3+1/N^4).

For N>=1000, the parenthesis is <1017/1000. Also (N)_12/N^12=product_(j=0)^11(1-j/N)>=1-66/N>=934/1000. Consequently

    beta_N < (5/231)*(1017/1000)^2/(934/1000) < 1/40.

The last comparison is the integer inequality 200*1017^2 < 231*934*1000 (206857800 <215754000). No asymptotic approximation enters. Certification still requires the promised independent exact small-bridge count regression; it is already part of the coordinator's planned mandatory source checks.

## Schedule, amplification, boundaries

For lambda>=32, N=lambda^2>=1024. H=N-1-2 floor(N/8)-lambda >=3N/4-lambda-1>=N/2 because lambda^2/4-lambda-1>0. Thus the explicit schedule is covered. C1-v1's own published schedule differs (L=6lambda^6 and B moves=floor(lambda^6/10)); it too satisfies the finite hypotheses with M=lambda^6 and H=M-1-2floor(M/10)-lambda, so the theorem need not silently overwrite C1's schedule.

Because the acceptance bound is every-key and the structured acceptance is pointwise one, repeated fresh reference replies conditional on public setup allow multiplying the <=3/10 reference factors. This is a legitimate conditional product: the reference replies are independent under their actual joint game, and the deterministic test is fixed. No hidden-key-dependent threshold or test is introduced.

- N=2: p_r(id)=p_(2r)(id)=1, hence beta=1; the numerical small-beta claim is excluded and the general upper bound is vacuous.
- L=0,2,6: excluded from the length-six theorem (M>=2); no extrapolation of beta_N to a full length-six window is allowed. At L=r the noiseless identity-window probability is one, which refutes such an extrapolation.
- k=L: H<=0, so the attack clause is inactive; the complete noisy laws coincide as required. The general local upper bound still holds.
- k=0 or 1: included with their exact source-independent channel laws; no conditioning on a hidden replacement event is needed.
- Odd L: global identity target empty/infeasible.
- H<=0: no positive-threshold attack conclusion. M,B,k must retain their stated integer/nonnegative domains.

Verdict: **T0 has a complete provisional blind proof reconstruction**, with the explicit finite-count regression dependency described above. The statement appears to remove the long-completion mixing dependency of BS1. It does not classify constructions outside the bounded local-relator class, prove a generic impossibility, or certify any security assumption.
