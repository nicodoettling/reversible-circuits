# Halfway checkpoint — 2026-09-07 21:14 UTC

Blindness remains intact: only the brief, operational metadata, permitted standards, and four permitted primary PDFs have been opened. No coordinator mathematical argument or role artifact has been read.

Provisional constructive route: sample connected factorizations of any endpoint at genus 0 or 1 by deleting the last transposition. Its deletion leaves either one connected component, or exactly two. In the second case, the two cycles created by splitting the endpoint cycle anchor the two components; all other endpoint cycles must be allocated to one side. A naive allocation sum is exponential.

Potential polynomial repair: Vakil Corollary 1.5 gives c_g(alpha)=r! Q(alpha) F_g(alpha), with Q=product a^a/(a-1)!, F_0=d^(k-3), and F_1=[d^k-d^(k-1)-sum_{j>=2}(j-2)! e_j(alpha)d^(k-j)]/24. In the two-component branch the binomial interleaving coefficient cancels both factorial denominators, Q is independent of cycle allocation, and at most one component has genus one. Thus a DP over allocated total size, cycle count, and elementary-symmetric-polynomial degree can aggregate every allocation in polynomial time. Sequential constrained versions of the same DP give the exact conditional allocation law.

This is PROVISIONAL, not yet a certified theorem. Next checks: formula normalization for fixed endpoints; all last-edge branch multiplicities; forced-allocation DP identity; singleton genus-one zero case; exact finite transition laws; rational bit-length bounds. Negative route preserved: a total Hurwitz count alone does not implement a sampler, and unconstrained endpoint bridges omit connectivity.

No computation has yet been promoted. Python 3.12.3 is available as python3; python and pdftotext are unavailable. No dependency installation is attempted.
