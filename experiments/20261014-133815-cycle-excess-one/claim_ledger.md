# Claim ledger: full-cycle excess-one proof attempt

All positive mathematical statuses are author proof claims. Independent
review is pending; map registration is provisional. Finite checks are
independent constructions within this same session, not a nonauthor audit.

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
| --- | --- | --- | --- | --- | --- |
| Original pair hybrid P mixes in poly(N) at m=N+1 | unresolved | none asserted | proof.md Sections 1,6 | no finite test proves it | retain as main open target |
| S_3, all feasible endpoints and m>=2: gap K_A>=1/[4(m-1)], gap P>=1/[8(m-1)] | proved | explicitly declared kernel and prefix coordinates | proof.md Section 2 | exact enumeration m=2,...,7; results.json | keep; fixed N scope |
| S_3 local K_A mixes within 12(m-1) log((m-1)/epsilon), rounded up | proved | same kernel | proof.md Section 2 | exhaustive neighboring-pair coupling checks d<=5 | keep |
| At m=N+1, Y<=3, E Y=6/N and fixed-pair equality is 12/[N^2(N+1)] | proved | checked full-cycle count normalization | proof.md Section 3 | every pair and every word for N<=5 | keep |
| Balanced available-pair refresh is uniform-reversible, accepts >=1/3, speeds its branch by factors between binom(N+1,2)/3 and binom(N+1,2) | proved | full-cycle excess one; channelwise MH rule | proof.md Section 4 | exact rational transitions N<=4, plus identity regressions for general reversibility | keep; not a full-gap acceleration claim |
| Every exact support-multigraph restriction has a positive gap | refuted | rejected-exit restriction of the declared pair kernels | proof.md Section 5, two frozen star words | all channels N=3,...,12 | reject this decomposition step; preserve witnesses |
| Tree-plus-2h-extra-edges proposal has tau(w) preimages | proved | rooted time-edge codec; occurrence-distinguished spanning trees | tree_jump_proof.md Section 2 | 922830 proposal tuples, independently enumerated target fibers | keep |
| Correcting by 1/tau gives Q_h=(1-p_h)I+p_h Pi_h | proved | preceding preimage lemma | tree_jump_proof.md Sections 2-3 | exact equal per-output accepted weights | keep as a different global macro |
| At m=N+1, hybrid (L+Q_1)/2 has gap>=1/[6(N-1)] and TV mixing <=ceil(6(N-1)log(1/epsilon)) | proved | L reversible for gap, stationary for TV; checked count formula | tree_jump_proof.md Section 3 | p_1=1/[3(N-1)] at N=2,...,5 | keep; original slide-only kernel unresolved |
| At m=N+3, p_2=(5N-7)/[15(N-1)^3], giving O(N^2 log(1/epsilon)) macro mixing | proved | GJV Proposition 1.1 and Theorem 3.1 normalization | tree_jump_proof.md Sections 3,5 | p_2=1/15,13/405 for N=3,4 | keep |
| At m=N-1+2h, fixed h gives O_h(N^h log(1/epsilon)) macro mixing | proved | same count input; coefficient positivity | tree_jump_proof.md Section 3 | lower bound and h=1,2 exact checks | keep; no jointly fixed-degree polynomial for variable h |
| Polynomial-length implementations of Q imply polynomial mixing of P | unresolved; inference not justified | missing polynomial stationary-flow congestion | both proof files | normal-form route warning retained | do not promote original conjecture |

No claim about uniformity over unlabeled or labeled support graphs follows:
the target throughout is uniform over ordered circuits, inducing graph
weights equal to their compatible-circuit multiplicities.
