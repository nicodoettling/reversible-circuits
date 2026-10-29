# parallel-hurwitz-layers

- Created UTC: 2026-10-15T13:41:44.842744+00:00
- Objective: Analyze uniform ternary Hurwitz updates on two alternating matchings, correct the endpoint seam, and prove layer-gap comparisons
- Target distribution: Uniform on a fixed Hurwitz orbit; separately a declared heat-bath extension for global fixed-product uniformity
- Parameters: even m>=2; each matching chosen with probability 1/2; each coordinate of v independent uniform on {-1,0,1}. No added global laziness. Products act rightmost first. At g=id the cyclic boundary is literal; general g uses the explicitly derived endpoint-preserving boundary conjugation.
- Tested claims: endpoint preservation and failure of the naive seam; matching commutation, inverse layers and uniform-orbit reversibility; local spectra {1,0,-1/3}; constant-factor projection comparison; layer gap of order min(m*sequential_cyclic_gap,1), hence no exponential improvement in asymptotic polynomial status.
- Positive benchmark: minimal factorizations of a product of m disjoint transpositions, N>=2m, even m>=4. Exact cyclic sequential gap via the checked interchange theorem gives parallel gap Theta(m^-2).
- Separately declared extension: retain independent local square heat baths with L_i=I/2+H_i/4+R_i/4. This is not the user's pure ternary kernel; compare it only with its own sequential walk and previous S3 bound.
- Commands: `python3 -B experiments/20261015-134144-parallel-hurwitz-layers/check.py`.
- Raw data: results.jsonl; exact deterministic tests, no seeds or floating-point spectral claims.
- Validation: identity S3,m4 and S4,m4,m6; nonidentity full cycles S3,m4 and S5,m4,m6; m2 boundaries; commuting benchmark. Enumerate all layer vectors, verify product and inverse maps, compare layer components with ordinary Hurwitz components, and verify local projection inequalities by complete finite spectral types.
- Literature obligations: inspect Anshu-Arad-Vidick arXiv:1602.01210v3 Lemma 2 and Corollary 3 (arbitrary projectors with bounded noncommutation), and Caputo-Liggett-Richthammer arXiv:0906.1238 Theorem 1.1 and generator normalization. No direct global Hurwitz mixing theorem is imported.
- Expected failures: naive cyclic seam changes nonidentity endpoint; pure moves cannot leave a Hurwitz orbit; rare prescribed-vector probability is confused with a gap estimate; layer time is confused with elementary update work; odd m is silently admitted.
- Interpretation: promote only precise comparison and benchmark claims pending independent review; growing-N full-cycle polynomial gap remains unresolved.
