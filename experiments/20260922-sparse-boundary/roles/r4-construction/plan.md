# R4 construction plan

Target: uniform literal length-m transposition identity words on distinguished labels and positions; rightmost-first composition. Investigate a separately versioned extension of connected component decoding beyond genus one, initially fixed genus two, while preserving top-level K. First inspect the positive count recurrence and decoder dependencies to find the first obstruction. If efficient genus-two decoding cannot be closed, give an exact conditional suffix-count primitive and a proved global assembly reduction. No claim that counts alone provide sampling.

Read-only evidence: old sparse-global result and September 7 genus-one recursion. Shared HANDOFF/GOAL_SPEC still target local mixing; this run explicitly supersedes that objective. Keep all research writes here.

Status: intake. Save early proof notes and checkpoint each major finding or 10 minutes. Bound computations with timeout 90s and preserve before-import hashes.

## Versioned direction change, 09:33 UTC

The single candidate is now H2-QC.v1: arbitrary genus up to a larger fixed
support cutoff L=max{v<=N:3^v<=P^4}. This replaces the initial speculative
genus-two route before construction. A complete simultaneous-conjugacy
invariant gives <=3^(v-1) support-history states and exact literal decoding.
See proof-v1.md. No H0/H1 definition changes and no T0 claim.
