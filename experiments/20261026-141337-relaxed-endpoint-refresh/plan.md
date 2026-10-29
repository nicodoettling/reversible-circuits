# relaxed-endpoint-refresh

- Created UTC: 2026-10-26T14:13:37.426948+00:00
- Objective: Test connectivity and quantitative obstructions for single-gate refresh with a bounded transposition correction budget
- Target distribution: Uniform on length-m transposition words with endpoint correction distance at most k from identity
- Scope: investigate the user's proposed relaxation, not launch a broad mixing run.
- Model: all transpositions of N labeled points; ordered products act rightmost first. Target is uniform on A(N,m,k)={w: ell(eval(w))<=k}, ell(g)=N-c(g). No support-connectivity condition. The main regime has even m and k>=2.
- Kernel: half hold; otherwise uniformly choose one of m positions and one of M=binom(N,2) replacement gates; accept exactly when the proposed endpoint has ell<=k. Boundaries reject. Length remains m. For m=0 the only word is held. Complexity variables are explicit N,m, not log N wires.
- Named claims: stationarity; connectivity at logarithmic/constant defect; whether local near-identity rejection introduces an identifiable slow mode; relation of relaxed sampling to exact sampling.
- Exact cases: S3,m4; S4,m4,m6; first genuinely restricted cases S5,m4,k2 and S6,m4,k2. Include m=0, odd m, m=2, N=2, and k=0,1. More cases only if a named concern justifies them.
- Expected failure modes: disconnected or frozen boundary states; poor conductance; confusing unrestricted tiny cases with meaningful relaxation; interpreting numerical eigenvalues as all-size gap bounds; bias from deterministic correction.
- Commands: python3 -B experiments/20261026-141337-relaxed-endpoint-refresh/check.py (additional arguments documented if used).
- Raw data: results.jsonl, with environment/commit/script hashes; no large transition matrices retained.
- Environment: Python standard library. System python has no NumPy; no package installation is needed. Numerical probes use fixed seeds 20261026 and 20261027 and are labeled uncertified. Exact graph/count checks are deterministic.
- Deliverables: proof.md, check.py, results.jsonl, claim_ledger.md, report.md. Integrate only stable scoped findings into the project map, with provisional author status where appropriate.

## Adaptive checks and exact commands

The first constrained labeled graphs were connected. To test the outer-shell
repair obstruction at length six without materializing tens of millions of
words, add a complete ordered-word quotient under simultaneous relabeling.
Audit its counts against a separate labeled-permutation DP. This is not a
projection onto unordered support graphs. Test the proposed greedy-descent
proof and a repeated-pair conductance cut explicitly.

```sh
python3 -B experiments/20261026-141337-relaxed-endpoint-refresh/check.py
python3 -B experiments/20261026-141337-relaxed-endpoint-refresh/check.py --case 5,4,2 --case 6,4,2 --iterations 300 --output experiments/20261026-141337-relaxed-endpoint-refresh/spectral.jsonl
python3 -B experiments/20261026-141337-relaxed-endpoint-refresh/quotient.py --case 3,4,2 --case 4,4,2 --case 5,4,2 --case 6,4,2 --case 4,6,2 --case 5,6,2 --case 6,6,2 --case 7,6,2 --case 8,6,2
python3 -B experiments/20261026-141337-relaxed-endpoint-refresh/audit.py
```

An exploratory call to `quotient.states(10,8,2)` was interrupted before a
result, because generation was substantially larger than the useful length-six
check. It supplies no evidence, and no length-eight connectivity claim is
made. Its temporary bytecode was removed. No packages were installed.
