# Frozen theorem C2.v1 — input suitable for theorem-only review

For every integer N>=2 and b>=1, there exists one randomized algorithm that outputs an ordered list of exactly2N+2 transpositions of[N], whose rightmost-first product is identity and whose support graph is connected on all[N]. Its law is exactly uniform on that finite target set, so its total-variation error is0<=2^(-b). Under independent fair bits and exact binary arithmetic it has expected bit time polynomial in N,b and polynomial space. A proposed conservative bound is O(N^20 log^4(N+1)), independent of b. Permutations and explicit words use canonical labels; N is degree, not log N wires.

Allowed input dependency: the exact S-G01 theorem supplies connected transposition factorizations of any fixed permutation sigma on a fixed v-set, for genus h=0 or1 and length v+c(sigma)-2+2h, with exact uniform law in expected polynomial bit time. It supplies the exact fixed-endpoint counts C_h(alpha)=r_h! product_i(a_i^(a_i+1)/a_i!) H_h(alpha), with

H_0(alpha)=v^(k-3),

H_1(alpha)=(1/24)[v^(k-2) sum_i a_i(a_i-1) + sum_(j=2)^k (j-1)! v^(k-1-j) sum_(|J|=j) (product_(i in J) a_i)(sum_(i in J) a_i)].

The singleton genus-zero fiber contains the empty word; singleton positive-genus fibers are empty. Reject zero-count component branches. The exact inherited source and its explicit normalization/dependencies are experiments/20260907-genus-one-sampler/proof.md, together with its recorded recursive and candidate audits. Those inherited artifacts are permitted primary project inputs; the original Vakil source cited there is permitted if source rechecking is needed.

This statement asserts no arbitrary-endpoint genus-two sampler, no all-length global sampler, no Hurwitz transitivity or mixing theorem, and no polynomial complexity in log N. Boundary cases to classify include N=2, singleton component fibers, zero local mass and minimum connected component lengths. General odd identity lengths are infeasible; the theorem's own output length is always even.

Review request: prove, refute or isolate a precise first gap under these definitions and explicit dependencies. No candidate construction or its evidence is included in this theorem-only input.
