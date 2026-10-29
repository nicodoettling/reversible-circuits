# relaxed-heatbath-comparison

- Created UTC: 2026-10-27T10:47:14.777050+00:00
- Objective: Resolve all-length connectivity and compare relaxed legal-gate heat bath to exact adjacent pair heat bath; test Hamming contraction
- Target distribution: Uniform even-length transposition words with endpoint defect at most two; distinct lifted exact bridge law declared separately
- Main target: uniform A(N,m,2), N>=3 and even m>=2; products rightmost first. H=I/2+(1/(2m)) sum_i conditional legal-gate refresh. Each selected coordinate is uniform, including coordinates whose legal set is small. No rejection or wraparound window.
- Separate comparison target: uniform exact identity words of length L=m+2. Q is half-lazy adjacent pair heat bath, S half-lazy pair heat bath between a uniform position i<L and the final position, and T half-lazy refresh of {i,L-1,L} with i uniform among the first m positions. These are distinct kernels.
- Named obligations: all-length boundary access via two correction gates; polynomial spectral-gap comparison between H and Q; exact failure or success of one-step Hamming contraction.
- Parameters: exact identity routing on S3,m4,m6; S4,m4,m6; S5,m4,m6. Relaxed conditional checks on S3,m4; S4,m4,m6; S5,m4. Local three-factor hub fibers for every endpoint through S5. Explicit Hamming witnesses at N5/6/8/12 and lengths 4/6/8/16.
- Commands: python3 -B experiments/20261027-104714-relaxed-heatbath-comparison/check.py
- Raw data: results.jsonl, including script/import hashes, commit, Python version and parameters.
- No stochastic conclusions: all checks use exhaustive integer/rational arithmetic. No random seeds are needed. No new numerical spectral extrapolation.
- Expected failure modes: a hidden correction-word multiplicity bias; non-Markovian projection; confusing the old middle-conjugating nonlocal kernel with a pair update that leaves the middle untouched; missing normalization/congestion factors; Hamming contraction failure mistaken for torpid mixing.
- Decision: keep only proved scoped implications. General polynomial mixing remains open unless an actual inverse-polynomial gap is established.
