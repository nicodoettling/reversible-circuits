# R1 plan — final-transposition recursion, T0

Frozen target: exact uniform sampling of ordered connected transposition words of length 2N with product identity on all N labels, N>=2. This would imply the requested TV guarantee for every b>=1. Rightmost factor acts first. The recursive internal target is connected words of length r=v+c(sigma)-2+2g, for a specified labeled endpoint sigma and g in {0,1}; this is not arbitrary prefix-conditioned bridge sampling.

1. Verify the genus-zero/one connected endpoint count formulas directly in Vakil's primary source, including factorial and symmetry normalization.
2. Derive deletion of the final transposition as a disjoint word-level decomposition. Connected predecessor branches join endpoint cycles or split a cycle and lower genus; disconnected predecessor branches have exactly two components and genus sums to g.
3. Try to sum and sample labeled cycle assignments in the disconnected branch by a positive polynomial dynamic program. Explicitly charge every state and arithmetic bit length; do not enumerate cycle subsets.
4. Implement minimal exact validation and compare every small word's probability/reconstruction multiplicity, along with boundary and historical regressions.
5. Write a complete proof or a precise first missing lemma, keeping all rejected constructions and sending substantive milestones to the coordinator.

All artifacts remain in this role directory. No delegation, installation, infrastructure changes, or detached work. Each computational invocation receives an explicit timeout. Checkpoint interval <=15 minutes. Initial result target 23:07 UTC; final report by 00:37 UTC.

Initial repository HEAD: 20e86f665f69053031fe7eec0c3388458affb1fc. Python command unavailable; python3 is 3.12.3. Initial dirty state consists of untracked current-run directory and five run-related notes/log files; no tracked changes. Standard library preferred.
