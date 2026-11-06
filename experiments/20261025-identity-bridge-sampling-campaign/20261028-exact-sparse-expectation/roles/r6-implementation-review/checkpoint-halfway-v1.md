# I2 implementation review halfway checkpoint

Status: ACTIVE; nonauthor, NONBLIND, correlated same-model review. Exact timestamp follows. Frozen author and both inherited implementation hashes read; no author bytes changed. The v0.4.0/attempt000003 cap and exact operator disposition have been read. No mathematical experiment has yet run in this role.

Analytic findings so far:

1. Least-label macro recursion uses unrestricted C/Z with all positive branches. Uniform choices of labels and positions cancel their two binomial factors. The full specified macro mass is product C/Z; each actual connected suffix decoder then contributes1/C. Public labels are1..N and positions retain increasing order. No quotient is constructed during C/Z preparation or sample_macro.
2. The inherited q retains the multiset of permutation cycle lengths separately in each exposed support block. Its indexed-cycle transitions count literal edges, including repeated cycles/blocks. Actual p and support pi survive throughout literal edge selection. The quotient law therefore preserves the80-versus81 distinction and samples literal words, not unweighted support graphs.
3. For a selected degreev, at mostS=3^(v-1) quotient states andQ=(ell+1)S count keys occur. Strict decreasing remaining length and depth-first task order imply a key cannot be simultaneously expanded as its own ancestor; first processing finishes before a pending duplicate is popped. Thus at mostO(Qv²) accesses, each scanning at mostQ keys. Exponential-map scans costO(P^6 9^v) before the stated slack, withinO(P^12 9^v).
4. Polynomial temporary Counter/set/dict structures admit pessimistic collision-scan charges; none has exponential cardinality except the explicit LinearMemo arrays. Counts/keys/addresses have polynomial bit length. Scalar C/Z intermediates remain polynomial-size positive integers. The P12 envelope appears conservative and sufficient.
5. Fair-bit work must use an ideal independent getrandbits interface. The public optional exact_index hook is audit-only and can allocate a tuple of length bound; it is rightly excluded from the production runtime theorem. SystemRandom is the concrete platform source, not a proof of physical bit independence. Rejection loops have unbounded deterministic running time; the theorem claims expectation.
6. Decoding conditional on the full macro uses the fresh fair-bit tail. The proof only conditions the decoding cost; macro-selection cost is bounded unconditionally and then added. No product of marginal event bounds is used. No polynomial worst-case memory is asserted.

Coordinator I2-J3 raw and receipt were read completely. Full laws pass: S3m4=27,S4m4=120,S4m6=3936,S3m8=2187, each literal word gets reciprocal total count. The rare v6,g2 component at N82,m14 has positive macro mass and builds only its selected counter (276keys), then releases it. These tests exercise actual production sample apart from categorical primitives; they do not themselves validate arbitrary fair-bit rejection sequences or the asymptotic cost proof.

New discriminating script targeted-check-v1.py is written but awaits coordinator reservation. It checks production getrandbits rejection and zero-weight categorical tickets, memo replacement, unmodified DFS expansion via tracing, and two selected components with counter disposal before the next creation. Request:60s/1GiB, expected<10s/<128MiB, detailed atomic JSON. No duplicate full-law enumeration is planned.

No material implementation/proof objection found at this stage. Final recommendation waits for the targeted check outcome and source re-verification. Separate moment/referee integration and the main all-length theorem remain outside this role's acceptance scope.

Updated 2026-10-28T12:52:02.649469+00:00
