# Logarithmic correction budget claim ledger

All author proofs remain provisional pending independent review. The
checks below are independent arithmetic formulations by the same author,
not independent referee certification.

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
|---|---|---|---|---|---|
| H_k is uniform relaxed-word heat bath; boundary fibers have k+1 to binom(k+2,2) gates | proved | even m,k; all transpositions; rightmost-first product | proof.md §1 | representative legal sets evaluated directly | retain exact kernel |
| Uniform one-step Hamming contraction at logarithmic k | refuted | N>=2(k+2), even m>2k+1 | proof.md §2, both-boundary witness | six exact witnesses, 21 representative coordinate classes | reject this coupling criterion only |
| Minimum k-correction count is k! | proved | N>=2k; parity-compatible endpoint ball | proof.md §3, fresh-label injection | permutation-state DP for N<=6, k<=8, with guard enforced | retain self-contained counting lemma |
| Worst-case correction multiplicity has polynomial ratio | refuted | even k=Theta(log N), m>=k | proof.md §3, ratio >=M^(k/2)/k! | identity pair lower bound and matching counts checked exactly | reject direct bounded-density extension |
| k iid transpositions nearly sample uniform correction-ball permutations | proved | N>=2k; endpoint law only | proof.md §4, TV<=Delta=O(k^2/N) | small group DP plus integer coefficient DP to N=4096 | retain positive endpoint result |
| Uniform exact extensions yield nearly uniform relaxed prefixes | refuted | m=k=Theta(log N), k even | proof.md §5, TV lower bound tends to one | nine small prefix/extension comparisons; explicit bound evaluation | reject unweighted correction-lift sampler |
| Flat endpoint word counts transfer endpoint closeness to word laws | conditional | explicit uniform count hypothesis (FC) | proof.md §5, TV<=Delta+2epsilon | four exact conditional-transfer cases | retain with (FC) adjacent; no all-length use |
| General polynomial mixing of H_k at logarithmic k | unresolved | growing N and even m>k | proof.md §6, Poincare target (P) | no numerical extrapolation attempted | keep open; no original-chain theorem |
| m<=k relaxed chain mixes quickly | proved | non-singleton product space | proof.md §6, gap=1/(2m) | m0,m2,N2 handled separately | distinguish easy dynamics from failed lift |
