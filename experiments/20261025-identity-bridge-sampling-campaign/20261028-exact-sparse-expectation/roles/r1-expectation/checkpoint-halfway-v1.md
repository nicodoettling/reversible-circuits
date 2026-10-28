# I2 R1 substantive halfway checkpoint — 2026-10-28 12:06 UTC

Status PROVISIONAL, not accepted. Both separately frozen targets ES.v1 and ES-LOG.v1 have candidate analytic closures, conditional on the exact R2 decoder bit-cost lemma and fresh review. No computation has run.

For any integer a>=2, under the exact uniform identity bridge and canonical E X_v<=N c rho^(v-1)/v^3,

E sum_nontrivial a^v <= N c a^2 rho/[8(1-a rho)]

whenever a rho<1. If a rho<=1/2 this is <=a N c/8. The random variable is a sum over actual components of the one full macro drawn first, not a product of stagewise marginal events.

ES: for N>=64 and m^3<=N^2, D>=3N/4, z<=5/162<1/16, c<3 and rho<(32/3)N^(-1/3). With a9 and N>=(32a)^3, a rho<1/3 and E sum_nontrivial a^v<3aN/16. Smaller degrees use the same algorithm and the deterministic inequality sum a^v<=N a^N. No lookup or precomputation over these degrees is proposed.

ES-LOG: for N>=2^2048, inherited Section3 gives c_new<=eN^(1/4),rho_new<=N^(-1/24), so 9rho_new<1/2 and the expectation is <=27N^(5/4)/8<4N². For N<2^2048 the deterministic bound is <=N9^(2^2048). Thus a single explicit proof-only constant K=1+9^(2^2048) gives E sum_nontrivial 9^v<=K N² throughout the union of the two separately frozen ranges.

R2's actual proposed algorithm samples the entire exact unrestricted macro before building any quotient decoder and discards tables after each component. Its deterministic linear-scan memo envelope has base9; the polynomial bit exponent remains to be pinned. Given conditional expected cost <=A P^d(1+sum9^v) for every full macro, the law of total expectation gives <=A(1+K)P^(d+2), with no independence assumption. Detailed full proof and dependency hashes next; fresh blind/nonauthor and finite regressions still required.
