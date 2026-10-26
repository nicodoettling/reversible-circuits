# Two-transposition endpoint relaxation

Verdict: **keep** the candidate and the scoped results. The relaxation
passes the completed connectivity tests and removes the confinement of
exact single-gate updates, but **general polynomial mixing is unresolved**.
No independent referee was used. This is partial proof progress, not a
new all-length sampler theorem. Project decision: **no-decision** about
the original exact {3,4,5} heat-bath chain.

## What was established

The target is uniform on all ordered length-m transposition words whose
endpoint is at most k transpositions from identity. A half-lazy random
single-gate replacement is accepted exactly when it stays in this set.
The main tests use k=2, which is a stricter allowance than a growing
logarithmic budget. Bounds are in explicit N and m, not log N wires.

1. All exact identity circuits communicate through two-error states for
   every N and even m. Every adjacent Hurwitz or square-refresh move can
   be implemented with two single-gate edits. A constructive normal form
   proves connectivity of this exact core, not polynomial congestion.
2. The WHOLE relaxed space is connected for every N at even lengths
   m<=6. This is a computer-assisted fixed-length result with a complete
   support-size argument, not an extrapolation from small N. The largest
   represented case has 46,854,304 words. General boundary-shell access
   at larger lengths remains unproved.
3. A repeated-pair cut gives a genuine slowdown: at m4,k2,N>=14,
   gap<=5/binom(N,2) and mixing time >=floor(binom(N,2)/10). Thus the
   unrestricted coupon-collector rate does not survive unchanged. This
   is a polynomial obstruction and does not refute rapid mixing.
4. A k2 rapid-mixing theorem would yield a near-uniform sampler with
   EXACT identity functionality, unchanged length, and O(N^4) expected
   rejection overhead. The endpoint-identity mass is at least
   1/[1+2C(N,3)+3C(N,4)] by Cauchy--Schwarz on word counts. This avoids
   the bias of appending a deterministic correction. The mixing premise
   is unproved; finite-time MCMC does not give exact distributional uniformity.

## Falsification and finite evidence

| N | m | k | Allowed words | Exact identity words | Full connectivity |
|---|---|---|---:|---:|---|
| 3 | 4 | 2 | 81 | 27 | yes; unrestricted case |
| 4 | 4 | 2 | 1,296 | 120 | yes; unrestricted case |
| 4 | 6 | 2 | 46,656 | 3,936 | yes; unrestricted case |
| 5 | 4 | 2 | 7,000 | 340 | yes; labeled graph |
| 6 | 4 | 2 | 24,705 | 765 | yes; labeled graph |
| 5 | 6 | 2 | 625,000 | 20,860 | yes; exact relabeling quotient |
| 6 | 6 | 2 | 3,701,025 | 72,315 | yes; exact relabeling quotient |
| 7 | 6 | 2 | 14,824,341 | 197,421 | yes; exact relabeling quotient |
| 8 | 6 | 2 | 46,854,304 | 460,768 | yes; exact relabeling quotient |

The quotient preserves the entire ordered word up to simultaneous vertex
relabeling. It is not the previously refuted unordered-support projection.
Five overlapping cases match the full labeled graph exactly, including
distances to the identity subset; a separate labeled-permutation DP
checks all nine quotient cardinalities. Support rank proves at most m+k
used labels, so S6/m4 and S8/m6 cover all larger N at those fixed lengths.

The proposed greedy proof is refuted. The word
((12),(13),(24),(34)) has defect two and no single-gate move reducing
the defect. It does admit a path of defects 2,2,0. Every checked allowed
word is within two edits of an exact word, but this is not proved at
arbitrary length. An attempted length-eight orbit generation was stopped
before a result and is not included as evidence.

The two-seed power probes give gap Rayleigh estimates around 0.06464
for S5,m4 and 0.04469--0.04471 for S6,m4. Residuals reach about 6.8e-4;
these are uncertified UPPER estimates of the gap, not proved positive
lower bounds. Both seeds and residuals remain in spectral.jsonl. No
stochastic convergence conclusion or asymptotic gap is claimed.

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
|---|---|---|---|---|---|
| Half-lazy single-gate refresh with endpoint budget 2 | Uniform relaxed fixed-length law A(N,m,2) | Intentional nonidentity states; correction bound checked | All exact identity states communicate through relaxed states, proved for all N,m | Integer symmetry, connectivity, endpoint/prefix/window types, per-position edges, multiplicities, adjacent repeats, weighted support; full counts cross-checked | keep; rapid mixing unresolved |

## Next obligation

First prove boundary access for arbitrary even length: every defect-two
word reaches an exact word without exceeding defect two. Strict descent
cannot prove it. Then establish a quantitative Poincare/congestion bound
that does not route all flow through one normal form. A logarithmic budget
is another possible target, but enlarging the state space does not make
the gap monotone. Neither candidate presently has a growing-N,m bound.

## Reproduction and validation

Starting commit: 543c5f5d9791e96baee02248536ddc96935f83bb.
Python 3.12.3, standard library only. Exact commands are in plan.md and
the raw manifests, which record script hashes and parameters. Only the
numerical spectral probes use randomness: seeds 20261026 and 20261027.
The graph/count/connectivity assertions are deterministic.

The audit checks 62,571 adjacent Hurwitz/square channels on the required
identity fibers S3,m4 and S4,m4,m6, and 231,160 endpoint-count inequalities
through S8 and even length eight. Empty odd-identity fibers, m0,m2,N2,
budgets 0/1, and minimal-length unrestricted regimes are checked explicitly.
The repeated-pair cut is evaluated exactly at eight degrees up to N100.

The experiment guide gains one procedural note about parity, vacuous
small cases, and correction bias; the skill-creator validator passes.
Map integration is provisional and does not upgrade the original mixing
frontier. No manuscript or HANDOFF theorem is changed, and no package
installation, subagent, commit, push or external message was used.

## Workspace changes

New files under experiments/20261026-141337-relaxed-endpoint-refresh/:

- plan.md
- check.py
- results.jsonl
- spectral.jsonl
- quotient.py
- quotient.jsonl
- audit.py
- audit.jsonl
- proof.md
- claim_ledger.md
- report.md

Updated procedural reference:

- .codex/skills/reversible-circuit-sampler/references/experiments.md

Map integration files:

- notes/project-map/integration-2026-10-26-relaxed-endpoint-refresh.md
- notes/project-map/catalogue.json
- notes/project-map/inventory.json
- notes/project-map/RESULTS.md
- notes/project-map/COVERAGE.md

PROJECT_MAP.md and the other rendered views remain unchanged. The final
integration receipt records map validation and inventory scope. Temporary
bytecode from the stopped exploratory command was removed.
