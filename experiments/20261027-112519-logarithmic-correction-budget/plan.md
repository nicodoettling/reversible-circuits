# logarithmic-correction-budget

- Created UTC: 2026-10-27T11:25:19.902360+00:00
- Objective: Analyze logarithmic correction budgets symbolically: contraction, correction multiplicity and endpoint-law balance
- Target distribution: Uniform length-m transposition words with endpoint defect at most an even k=Theta(log N); auxiliary endpoint laws explicitly separate
- Model: all M=binom(N,2) transpositions, products rightmost first;
  even m and even k. H_k holds with probability 1/2, otherwise chooses
  one of m coordinates uniformly and replaces it by a uniform legal gate.
  The other coordinates remain fixed; no wraparound or window choice.
- Regime: k=Theta(log N), with k=2ceil(log2 N) for numerical examples.
  Auxiliary permutation counting claims allow either parity of k.
- Tested claims: logarithmic budget might restore Hamming contraction or
  polynomial bounded-density comparison; correction multiplicity might be
  almost balanced in total variation even when its worst-case ratio is large.
- Expected failure modes: confusing endpoint permutations with words;
  treating failed coupling/comparison as a slow-mixing theorem; extrapolating
  small exact computations to all N; ignoring parity or N>=2k guards.
- Parameters: exact permutation-state count DP for N=2,...,6, lengths 0,...,8;
  representative conditional fibers at (N,k)=(16,4),(32,10),(64,12);
  integer coefficient DP at N=32,64,128,256,1024,4096; formula evaluations
  at N=2^20 and 2^40. No MCMC, full circuit enumeration, or spectral computation.
- Command: python3 -B experiments/20261027-112519-logarithmic-correction-budget/check.py
- Raw data: results.jsonl, including commit, Python version, script hash and
  deterministic parameter records. Seeds: not applicable; no randomness.
- Interpretation: proved statements require the separate symbolic arguments
  in proof.md; small checks only falsify errors. General rapid mixing unresolved.
- Next changes: preserve previous research artifacts; add a provisional map
  entry and procedural target-law warning. No HANDOFF/manuscript promotion.
