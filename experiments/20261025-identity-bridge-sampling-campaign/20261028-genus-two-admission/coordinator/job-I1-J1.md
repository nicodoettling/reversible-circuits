# I1-J1 reservation and finite model

Reserved by coordinator, attempt000002, 2026-10-28. Only one computational job authorized at a time. Test CUT2 universal coverage and exact labeled macro multiplicity, not an asymptotic theorem or sampler certificate.

Parameters: genus2 connected identity at (N,m)=(2,6),(3,8); legacy identity totals (3,4),(4,4),(4,6), plus boundaries N2,m0,2 and odd m. Largest exhaustive case has6^6=46656 literal words; S3m8 has6561. At most2184 genus2 words and at most7 cuts each; a small dictionary of macro counts. Estimated memory<256MiB, requested bound1GiB and wall90s. Standard Python3.12.3 only, deterministic seed=null. Base commit d8893491e04aff74ff3185f7054470ffa24a44a4.

Independent reference computes rightmost-first products, literal support components, per-component endpoint cycles/genus and uses the subtractive genus1 formula, different from the proposed positive decoration grammar. Every cut satisfying prefix genus1 is keyed by literal prefix permutation, both labeled support partitions and their genus decorations. Direct word-incidence counts must equal j!(m-j)! times the product of normalized fixed-endpoint connected counts. This checks normalizers and labels, not the unimplemented grammar/parser.

Mandatory retained failures: (ab)^3 has no adjacent square; S3 transposition endpoint length5 total81 vs connected80; unweighted triangle support mass1/4 vs3/4 for connected genus1 S3; CP1 exact joint21/2000>1/100 and residual21/221<1/10. No independence shortcut is used.

Command (from repo root): /usr/bin/python3 -B /home/nico/projects/harnesses/codex-research-harness-releases/v0.3.2/src/research_harness/bounded.py --run-file /home/nico/projects/research_projects/reversible_circuits/.campaigns/identity-bridge-sampling-20261025/attempts/000002/run.json --timeout 90 --memory-gib 1 -- /usr/bin/python3 -B experiments/20261025-identity-bridge-sampling-campaign/20261028-genus-two-admission/coordinator/cut-reference-v1.py

Detailed output: cut-reference-results-v1.json, published atomically only after completion. Output prints a compact summary.
