# R3 H0 implementation plan v1

Target: exact Unif(A(N,m)), with A fixed by top-level K. The desired global law remains Unif(Omega(N,m)); exact TV=1-Z_A/Z is a per-instance certificate, not an asymptotic bound. Products act rightmost first.

1. Hash and inspect September 7 genus-zero/one decoder and September 5 scalar count source, preserving dependencies read-only.
2. Implement exact integer cutoff, iterative support-marked completion DP, fixed-predicate assembly and CLI/API.
3. Verify complete word laws and counts on (3,4),(4,4),(4,6),(3,6),(4,8), high-genus (3,8), forced K=2 exclusion, top-level cutoff stability, and empty/odd/singleton boundaries. Include length above the interpreter recursion limit with v=2.
4. Give polynomial bit/storage bounds retaining the m layer factor, record primitive dependencies and first open global-tail lemma.
5. Hand current versions to nonauthor audit and preserve repairs/negative findings.

Commands use python3 -B with timeout<=120s. One heavy compute slot held; R4 owns disjoint certificate grids. Seeds1729,2718,31415 for validity only. First checkpoint before06:03:44Z; thereafter<=15m; no new construction09:13:44Z; reports09:38:44Z; hard cap09:43:44Z.
