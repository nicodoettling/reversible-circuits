# R1 final-transposition sampler report

Version: R1-T1.1, 2026-09-07 21:29 UTC. Author result is complete; certification status **PROVISIONAL**, awaiting nonauthor audit. Verdict: **keep pending audit**. The mathematical argument has no identified missing completion oracle for genus zero or one. This report does not promote its own theorem automatically. Version 1.1 only weakens the conservative displayed bit exponent to avoid depending on a sharp gcd bound; tested algorithm R1-T1 is unchanged.

## Frozen theorem and outcome

Let X_N consist of all ordered length-2N transposition words in S_N with identity product and connected support on **all N labeled vertices**. Products act rightmost first. For every N>=2, the supplied algorithm samples exactly uniformly from X_N in expected bit time polynomial in N. Consequently its TV error is zero, satisfying the requested 2^-b guarantee for every integer b>=1. X_2 is a singleton; X_1 is empty.

The stronger internal theorem covers any specified labeled permutation sigma on v vertices and either g=0 or g=1, at connected-factorization length r=v+c(sigma)-2+2g, whenever that fiber is nonempty. The singleton genus-zero empty word is the recursive base; singleton genus one has zero count and is never sampled. Complexity is measured in permutation degree, not its logarithm. This is a direct sampler with no Markov chain or mixing dependency.

Complete proof and pseudocode: [proof.md](proof.md). Executable implementation: [sampler.py](sampler.py). Exact audit: [audit.py](audit.py). Machine-readable results: [results.json](results.json).

## Construction and substantive new step

Remove the final transposition tau from a connected word with endpoint sigma. The predecessor endpoint is sigma tau. If the predecessor support remains connected, its genus is g or g-1 according to the elementary cycle cut/join rule. If it disconnects, exactly two support components remain. The two cycles produced by cutting one sigma-cycle belong to opposite components; every other **individual labeled cycle** is allocated to one of them. Their genera sum to g.

For a fixed allocation, the exact branch weight is

    binom(r-1,r_A) C_{g_A}(alpha_A) C_{g_B}(alpha_B).

The two sides are oriented by the smaller endpoint of tau, so no symmetry division is present. Each parent word recovers its final edge, component allocation, two child words, and interleaving uniquely. This discharges the word-level lifting issue rather than assuming that counts already supply a sampler.

The main algorithmic step sums the apparently exponential allocation list by a **positive** dynamic program. After canceling child factorials against the interleaving binomial, genus-zero weights depend only on each component's vertex count and cycle count. In genus one, the positive form of the Hurwitz formula additionally involves Q=sum a_i(a_i-1) and marked-cycle statistics S_j=sum_{|J|=j}(product_J a_i)(sum_J a_i). These statistics have nonnegative updates on states indexed only by vertex count, cycle count, and marked-cycle count. Thus O(v^4) arithmetic work suffices for a branch aggregate. Forced partial allocations use the same DP; evaluating the two next choices produces the exact sequential conditional distribution. Fixed genus is not used to claim that all endpoint partitions form a polynomial inventory.

Given a branch and allocation, recursively sample its connected child words, sample a uniform binary interleaving, and append tau. For each fixed word the probability is exactly

    (D/C_parent)(W/D)(1/C_A)(1/C_B)/binom(r-1,r_A)
      = 1/C_parent.

The connected case telescopes directly. Every factor is a conditional probability under the actual exposed branch. No unconditioned marginal bounds are multiplied.

## Source and dependency audit

Primary input checked directly: Ravi Vakil, *Genus 0 and 1 Hurwitz numbers: recursions, formulas, and graph-theoretic interpretations*, https://math.stanford.edu/~vakil/files/g01hurwitz.pdf, Section 1.2, Corollary 1.5, Proposition 3.2 and its positive graph expansion, and Section 4.1. The paper defines c_g for a fixed permutation and relates its cover count by G_g=c_g/product a_i. Thus our C_g=c_g already counts ordered labeled words. We introduce no extra conjugacy, cycle-order, r!, or v! quotient. The factorials in the formula are part of its stated count and cancel only when combined with the genuine word interleaving count.

The source verifies scalar arbitrary-endpoint counts; the final-letter word bijection and polynomial allocation DP are established separately in proof.md. DYZ scalar identity counts, DPS maps, Hurwitz transitivity, and local mixing are not dependencies of this route.

| ID/version | claim | mathematical evidence | audit status | first remaining gate |
|---|---|---|---|---|
| R1-C1 | positive normalized endpoint counts for g=0,1 | named primary source; positive/signed formulas and independent support DP agree | source checked by author and coordinator | nonauthor full review |
| R1-C2 | connected length has nonnegative integral genus | prefix joins/splits and support-component joins | author proof complete | nonauthor review |
| R1-C3 | final-letter branches are disjoint and reconstruct uniquely | elementary edge deletion; full small-case inverse reconstruction | author proof complete | nonauthor review |
| R1-C4 | allocation sums and conditional allocation sampling are polynomial and exact | nonnegative DP recurrence; 112,698 forced-query comparisons | author proof complete | nonauthor review |
| R1-C5 | full sampler gives probability 1/C for every word | induction and exact conditional telescoping; all required words checked | author proof complete | nonauthor review |
| R1-C6 | expected bit time polynomial in N | length potential, bit-size proof, bounded caches, explicit stack | author proof complete | nonauthor complexity review |
| R1-T1 | exact uniform connected endpoint sampling, g<=1 | R1-C1 through R1-C6 | PROVISIONAL | fresh nonauthor reconciliation |

The first unproved step in the **certification process** is fresh nonauthor audit, not a missing mathematical lemma currently hidden in the construction. If any listed proof is rejected, the theorem reopens through its dependency graph.

## Resource accounting

Each DP has O(N^3) scalar entries per layer and O(N) layers. A sampler node scans O(N^2) candidate final edges, costing O(N^6) arithmetic operations; sampling the chosen allocation costs O(N^5), already dominated. The sum of child lengths is the parent length minus one. Hence the recursion has exactly 2N positive-length nodes for X_N and at most N empty singleton leaves. Total arithmetic work is O(N^7).

All DP entries and final integer counts have O(N log(N+1)) bits. Reduced rational summands have denominators dividing 24(N!)^5: the product of cycle factorial denominators divides N!, and the only negative component-size exponents are at least -2 on either side. Numerators and sums are also exp(O(N log(N+1))) because all terms are nonnegative. Standard integer and reduced-rational arithmetic therefore yields polynomial bit complexity; proof.md records a conservative O(N^10 log^3(N+1)) bound allowing O(B^3) operations for a B-bit reduced-rational operation. Random integer rejection needs fewer than two attempts in expectation and O(N log(N+1)) bits per attempt.

The implementation has explicit continuation frames, so it does not rely on changing Python's recursion limit. Caches have fixed bounded capacities. The exhaustive subset/word inventories occur only in audit.py at named finite cutoffs, not in sampler.py.

## Exact validation

All tests passed on the current explicit-stack implementation. The complete run took approximately 14.15 seconds.

| finite case | all identity words | connected words | checked full word probability |
|---|---:|---:|---|
| S_2, m=4 | 1 | 1 | 1 |
| S_3, m=4 | 27 | 24 | 1/24 for all 24 |
| S_3, m=6 | 243 | 240 | 1/240 for all 240 |
| S_4, m=4 | 120 | 0 | connected fiber empty |
| S_4, m=6 | 3936 | 2880 | 1/2880 for all 2880 |
| S_4, m=8 | 140160 | 131040 | 1/131040 for all 131040 |

Further exact checks:

- 478 oriented cut-cycle inventories of total size at most 10, 4,621 full assignments, and **112,698 partially forced assignment queries**, including non-prefix constraints and zero branches. Every positive-DP count equals a direct subset sum computed with a separately coded subtractive Corollary 1.5 formula.
- 1,745 arbitrary labeled endpoint/count comparisons through degree six and lengths at most twice the degree, against a separate positive DP on permutation and actual support partition.
- Complete inverse reconstruction and exact rational probability multiplication for every tested connected word, including its recursive descendants. The digest for X_4 is `b8ca6359bda6e14f7edc5684871948e647da99898dc556f03e9895abf84a1f87`.
- All subset-unranking choices through n=8; empty, odd-length, m=2, N=1, and N=2 boundaries.
- The square-free identity ((01)(12))^3 receives exactly 1/240; its connected fourth-vertex square extension receives exactly 1/131040. These preserve the historical failure of adjacent-square-only generation.
- The cached-prefix regression reproduces 21/2000>1/100 and rejects the old marginal product bound. The new argument uses exact positive conditional masses under every partial assignment.
- Two seeded validity runs (1729,2718), three draws each at N=2,3,4,6,8,12, check exact product, length and connectivity. These are validity smoke checks, not empirical evidence of uniformity.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| final-transposition recursive sampler | uniform connected X_N; internal specified connected g<=1 endpoint law | yes, proof and tests | not a chain; component crossing is not the objective | complete small-word law and reconstruction; forced-oracle and endpoint checks | keep pending audit |

## Reproduction and retained negative findings

Run from this role directory:

    timeout 300s python3 -B audit.py --forced-max 10 --endpoint-max 6 --word-max 4 --output results.json

Python 3.12.3, standard library only. Repository commit `20e86f665f69053031fe7eec0c3388458affb1fc`. The exact command and contemporaneous dirty state are embedded in results.json. Before the final run, the smaller command with `--forced-max 8 --endpoint-max 5` passed; its purpose was to validate the first implementation, whose only subsequent repair was replacement of Python recursion by an explicit stack. No installs, configuration changes, commits, pushes, remote work, or subagents were used.

Rejected historical implications remain rejected: identity scalar counts alone give no exposed-prefix connectivity oracle; adjacent-square insertion does not cover the target; a fixed surplus does not make literal cycle-partition enumeration polynomial. This algorithm instead recurses on genuinely connected endpoint fibers and sums cycle allocations by a polynomial table. It claims no higher-genus, all-length global, or local-chain mixing theorem.

All author changes are within this role directory: assignment.md, plan.md, checkpoint.md, proof.md, sampler.py, audit.py, results.json, and report.md. The coordinator owns shared ledgers, final acceptance, and any durable synthesis. Awaiting audit assignment.
