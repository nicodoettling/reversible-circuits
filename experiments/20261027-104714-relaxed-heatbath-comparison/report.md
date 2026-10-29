# Legal-gate heat bath: full connectivity and polynomial gap equivalence

Verdict: **keep** the proved comparison and fixed-degree positive result,
provisionally pending independent review. **Growing-N polynomial mixing
remains unresolved.** This investigation resolves the qualitative boundary
gap left on October 26 and identifies a precise limitation of the proposed
relaxation. It does not establish torpid mixing or sampling hardness.

## Main answer

Let H be half-lazy uniform-coordinate heat bath on the uniform relaxed
space of length-m transposition words correctable with at most two
transpositions. Let Q be half-lazy adjacent pair heat bath on EXACT identity
words of length L=m+2, and put M=binom(N,2). The proved comparison is

    gap(Q)/(9 M^7 L) <= gap(H)
        <= 4 M^13 (L-1) L^3 gap(Q).

Thus the two-error legal-gate process forgets its initial state in
polynomial time in N,m if and only if this exact adjacent-pair process
does. The exponents are deliberately loose. This is a reduction between
two precisely specified kernels, not a proof of a growing-N gap, and no
unproved comparison to the original {3,4,5} kernel is silently included.

There is a positive all-length corollary at fixed degree four. The relaxed
S4 target is an unconstrained product law, so gap(H)=1/(2m). Consequently,
for every even L>=4,

    gap(Q on S4) >= 1/(8 * 6^13 * L^5),

giving worst-case mixing O(L^6+L^5 log(1/epsilon)). This supplies a rigorous
polynomial result in L with N fixed at four. It does not extrapolate to
growing N, and the large constants are not an implementation recommendation.

## Why the comparison works

Append two correction gates to an approximate word. On the exact extended
word, use the last correction position as a helper. Every adjacent Hurwitz
or square-refresh move can be carried out by three conditional pair moves
that each change the helper and one other position, leaving all middle
gates untouched. Projecting these moves to the original positions proves
FULL connectivity at every length, not just the earlier m<=6 result.
Correction padding extends qualitative connectivity to all nontrivial
budgets: even m,k>=2, or odd m,k>=1, with the usual singleton/empty cases.

Uniform exact extensions do not have uniform relaxed prefixes: the number
of two-gate corrections is M,3,2 according to the endpoint type. The proof
keeps this multiplicity. Refreshing one original gate AND both correction
gates gives a Markovian projection with the correct weighted marginal;
conditional-variance comparison costs at most M. Local three-factor
Poincare bounds and recoverable comparison paths supply the remaining
polynomial factors. No global paths are routed through a single normal
form for the quantitative argument.

## The direct contraction route fails

For neighboring words, the optimal one-step Hamming transport cost equals

    1 - 1/(2m) + (1/(2m)) sum_{j != changed position}
        TV(uniform legal sets at coordinate j).

Explicit neighboring words in S5,m4 give cost 41/40, and in S6,m4 cost
43/40, starting at distance one. These are lower bounds for EVERY coupling,
attained by a synchronous maximal coupling, not just failures of a chosen
implementation. Fixed positive coordinate weights cannot give a universal
one-step contraction either. This rejects that proof method, not
polynomial mixing. Multi-step couplings, metrics depending on the state,
and other Poincare arguments remain possible.

The general first unproved obligation is now an inverse-polynomial gap;
the earlier missing connectivity lemma has been discharged. The comparison
is specific to a two-transposition budget. It does not settle whether a
growing O(log N) budget yields an easier chain.

## Validation and reproducibility

Command:

    python3 -B experiments/20261027-104714-relaxed-heatbath-comparison/check.py

Commit: 7640534e21b0cdf3cdf25d93201b74caa063cecb. Python 3.12.3,
standard library only. All checks are deterministic and use integer or
rational arithmetic; no random seeds or numerical eigenvalue estimates.
The manifest pins both the current checker and the imported prior helper.

- 714,000 routed channels, in both directions, on six exact identity
  fibers: S3,L4,L6; S4,L4,L6; S5,L4,L6. Every intermediate endpoint,
  touched position, prefix error bound and final destination is checked.
- 51,628 legal-coordinate fibers on relaxed S3,m4; S4,m4,m6; S5,m4.
  Stationarity, legal set sizes, per-position frequencies and completion
  multiplicities are checked. Extended identity counts include 140,160
  S4,L8 words and 20,860 S5,L6 words. The state space and uniform target
  are identical to the prior experiment, whose complete prefix, window,
  repeat, edge-multiplicity and weighted-support marginals remain valid.
- All 75 feasible three-factor endpoint fibers through S5 are checked
  for helper-pair connectivity. Direct selected-triple enumeration verifies
  972 projected rows in S3/S4 independently of completion-count formulas.
- Five exact Hamming-expansion witnesses, through N12,m16, include full
  rational transition rows and marginal transport lower bounds.

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
|---|---|---|---|---|---|
| Half-lazy legal-gate H | Uniform relaxed A(N,m,2) | bounded correction, intentional nonidentity | full connectivity proved for all lengths | exact conditionals, routing, lift counts, coupling witnesses | keep; growing-N gap equivalent to exact pair problem |
| Exact adjacent-pair Q at N4 | Uniform exact identity words | yes | inherited constructive pair connectivity | symbolic comparison plus exact short-fiber routes | keep fixed-degree polynomial theorem, provisional |

The earlier nonlocal proof's fixed-endpoint vertex sweep was read and
reproduced in the argument. Its middle-conjugating K_G is NOT the helper
pair kernel here. No external literature dependency, install, subagent,
commit, push or external message was used. New proofs remain author work
pending independent review; no manuscript or HANDOFF theorem is changed.

## Workspace changes

New files in experiments/20261027-104714-relaxed-heatbath-comparison/:
plan.md, proof.md, check.py, results.jsonl, claim_ledger.md, report.md.

Updated: .codex/skills/reversible-circuit-sampler/references/experiments.md;
notes/project-map/catalogue.json, inventory.json, RESULTS.md, COVERAGE.md.

New integration receipt:
notes/project-map/integration-2026-10-27-relaxed-heatbath-comparison.md.

The prior experiment and its raw outputs remain frozen. Its map record is
versioned to mark boundary access superseded by this provisional proof;
the original quantitative mixing gap is retained. PROJECT_MAP.md and
other rendered views remain unchanged. The receipt records final checks.
