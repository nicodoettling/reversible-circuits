# LC1 — finite local-observable survival theorem (statement only)

Frozen 2026-10-29. No acceptance is asserted.

Let an alphabet of size q>=1 have uniform law mu; let P,R be any laws on length-L words. For a deterministic fixed ordered set I of s positions, 1<=s<=L, let f:alphabet^s->[0,1] be a rational-valued test. Let Q_k replace a uniform k-subset of all L positions with independent mu values, for 0<=k<=L-s; the subset and values are independent of the source. Write alpha_j=binom(L-j,k)/binom(L,k), 0<=j<=s. There is an explicit rational-valued randomized test h:alphabet^s->[0,1], depending only on f,L,k,q, such that

 Pr[h((Q_k P)_I)=1]-Pr[h((Q_k R)_I)=1]
 = alpha_s/(2*3^s) * (E_P[f(W_I)]-E_R[f(W_I)]).

Here randomized test h accepts with its indicated value; this is equality of acceptance differences, not a claim of pointwise source reconstruction. One can compute its acceptance probability with at most O(4^s q^s) evaluations of f and polynomial bit overhead in the input lengths and rational representation. Exact rational Bernoulli sampling uses unbiased bits with finite expected polynomial work (worst-case finite random-tape bounds require a separately charged negligible approximation). The case s=0 has no nonzero bias; for q=1 every source has the same word law. The theorem makes no claim for k>L-s.

In M0 q=N(N-1)/2, for fixed s and polynomially bounded N,L and inverse-polynomial original bias, any schedule with alpha_s inverse polynomial gives an efficient inverse-polynomial noisy advantage. In particular k/L<=1-c for fixed c>0 and L sufficiently large has this property. An explicit security schedule and f are still required for any concrete family; this is a transfer lemma, not an attack on every identity sampler.

Reference law may be global U(N,L); no independence within P or R, word invariance, endpoint mixing or setup hypothesis is needed. The claim can be applied conditional on each public setup A when I,f are fixed functions of A and all source/noise laws obey the stated independence. It does not choose a hidden-key-dependent observable for an adversary. A one-sample attack already applies to reused-setup games by ignoring other replies. General amplification requires a key-wise gap assumption and is not asserted here.
