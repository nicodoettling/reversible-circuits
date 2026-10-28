# Frozen theorem-only package: ES.v1 and ES-LOG.v1

For N>=2 let T_N be the full set of transpositions of the canonically labeled set [N]. Let Omega(N,m) be the ordered m-tuples of transpositions whose product is the identity; permutation maps compose rightmost first. Output words explicitly list all m factors. Randomness is a sequence of independent fair bits; arithmetic and storage are measured in bits.

Assess the following two claims for one common randomized algorithm. The algorithm is defined for every even m>=0 and returns an exactly uniform member of Omega(N,m). Odd m is rejected. There exist absolute constants A,d<infinity, independent of N,m and every accuracy request, such that its expected bit time is at most A(N+m+2)^d on each stated range:

* ES.v1: all N>=2 and even m>=0 satisfying m^3<=N^2.
* ES-LOG.v1: all N>=2 and even m>=0 satisfying m<=N^(2/3)ln(N)/4.

The algorithm need not test membership in these analytic runtime ranges. The two finite-N ranges are kept separate; their union may be taken only if both claims hold. Exactness is equivalent to TV error0 for every b>=1. No polynomial worst-case time or worst-case space bound is claimed. Efficiency is in N and m, not logN wires.

Boundaries include m0, odd m, m2, N2, the isolated component (v,ell)=(1,0), zero-mass branches, and connected minimum length2v-2. Every feasible component genus must be eligible.

Allowed pre-existing mathematical sources: experiments/20260922-sparse-global-sampler/proof.md and its source_checks.md/closed claim_ledger.md; experiments/20260922-sparse-boundary/proof.md and its source_checks.md/closed claim_ledger.md; experiments/20260922-sparse-boundary/roles/r4-construction/proof-v1.md and ../../construction_audit.md relative to that directory; DYZ Classical Hurwitz numbers and related combinatorics, Proposition1 Eq13, Section1.2 Eqs19–20 and genus-zero value after Eq28, https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf. These prior sources may be scrutinized; their old scope is not automatically the claimed new scope.

Prove, refute, or identify the first missing precise hypothesis. Do not infer a computational bound from scalar counts or a state count alone. Preserve the full report and identify inherited context.
