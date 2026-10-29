# Actual adjacent-chain gap attempt

Verdict: **keep** the short-block theorem, exact comparison and explicit
local obstruction. **Inconclusive** for the requested inverse-polynomial
gap of K_A on full-cycle length N+1 circuits. All new results are
same-author work pending independent review.

## What was proved

For the exact adjacent chain K_A=I/2+H/4+R/4, products rightmost first,
uniform fixed-endpoint target, linear windows and no wraparound:

1. Half-lazy two-factor heat bath Q_2 satisfies
   (1/2) E_Q2<=E_KA<=E_Q2 for every feasible N,m,g.
2. At m=3, every nontrivial endpoint fiber has gap(K_A)>=1/24 uniformly
   in N. The proof classifies all four endpoint types, treats the
   transposition type by an all-N arrowhead-matrix calculation, and
   certifies the other three types by exact rational matrices. Thus the
   finite calculations are backed by a completeness argument.
3. At every m>=3, half-lazy exact three-factor heat bath Q_3 satisfies
   E_Q3<=24 E_KA and E_KA<=2 E_Q3. This is a constant-factor spectral
   reduction, not a mixing theorem for Q_3.
4. For a full N-cycle at m=N+1, N>=3, a conservative actual-chain bound is
   gap(K_A)>=3/[N^(N+3)(N-1)^2(N+1)^3]. This is exponential in N and
   does not establish fast mixing. The proof retains the S=|Omega|
   congestion factor rather than suppressing it.

## Failed proof step

The three-gate generator (I-E1)+(I-E2) has exact gap 1/3 on a
transposition endpoint for every N>=4; its outer-gate correlation is 2/3.
This entire conditional fiber occurs inside full-cycle m=N+1 circuits
by fixing an appropriate reduced tail. Therefore the endpoint constraint
cannot remove the obstruction to the simplest local-contraction route.
The direct open-chain inequality needs local gap above 1/2 to produce
a positive bulk bound. With 1/3 it gives no such bound. No general
failure of local-to-global methods or polynomial mixing is claimed.

The remaining obligation is genuinely quantitative: control the growing
chain's Poincare constant, or route comparison flow without an exponential
state-count factor. Neither the short-block gap nor short normal-form
paths supply that missing estimate.

## Reproduction

Baseline commit: `4699f218df63bc2ff5c91e645e4bf08300490bfd`.
Client date: 2026-10-15, Europe/Berlin. Started 2026-10-14 UTC.
Python 3.12.3; standard library only; deterministic exact arithmetic,
so no random seeds. NumPy was unavailable and was not installed; no
result depends on numerical eigensolvers. The initial script locator in
the skill was relative to its own directory and was resolved there.

```sh
python3 -B experiments/20261015-adjacent-gap-proof/check.py
```

Raw output: results.json, recording command, commit, Python version and
both imported-code hashes. Checks include exact length-two formulas for
N=2,...,8; the three minimal triple incidence matrices and positive LDL
pivots; transposition triple matrices for N=2,...,12; the explicit
eigenfunction and full-cycle conditional embedding; all two-factor
transition ratios on 20375 words and 229196 directed channels; and the
tighter genus-one normalization length on the tested full-cycle fibers.

Full-cycle cases: N=3,m=4 (27 states), N=4,m=5 (640), N=5,m=6 (15625).
Identity regressions: S3,m4 (27), S4,m4 (120), S4,m6 (3936).
All exact assertions passed. Boundary, odd-length and singleton cases are
handled in proof.md Section 6. The endpoint, transition probabilities,
conditional fibers and exact count ratios are the relevant diagnostics;
no time-series mixing claim is made.

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
| --- | --- | --- | --- | --- | --- |
| Actual adjacent K_A | uniform fixed-length fixed-endpoint words | all identity regressions pass | square refresh allows crossings; prior constructive connectivity retained | exact K_A/Q ratios, triple certificates, primitive normalization bound | keep partial theorems; N+1 polynomial gap inconclusive |

## Sources and status

Relevant prior internal proofs: the all-endpoint vertex sweep in the
nonlocal-graph-lift experiment, the full-cycle count normalization in the
excess-one experiment, and the stronger S3 all-length theorem. None was
changed or silently upgraded.

The targeted literature check concerned whether a three-site finite-size
criterion could close the gap. Gosset-Mozgunov arXiv:1512.00088v1,
Corollary 2/Theorem 3, concerns periodic chains and is cited only for
context; the open-chain inequality used here is derived directly.
Lemm arXiv:1709.02756 is marked superseded by arXiv:1801.08915 on its
primary page and was not used as a theorem dependency. No claim that
the literature contains no polynomial-gap theorem is made.

The map registers the new result provisionally. The substantive outcome
is proof progress on local conditional control, not a completed proof
of the user's conjecture or a manuscript-level certification.

## Files changed this turn

Added:

- `experiments/20261015-adjacent-gap-proof/plan.md`
- `experiments/20261015-adjacent-gap-proof/check.py`
- `experiments/20261015-adjacent-gap-proof/results.json`
- `experiments/20261015-adjacent-gap-proof/proof.md`
- `experiments/20261015-adjacent-gap-proof/claim_ledger.md`
- `experiments/20261015-adjacent-gap-proof/report.md`
- `notes/project-map/integration-2026-10-15-adjacent-gap-proof.md`

Updated navigation files that were already dirty on entry:

- `notes/project-map/catalogue.json`
- `notes/project-map/inventory.json`
- `PROJECT_MAP.md`
- `notes/project-map/RESULTS.md`
- `notes/project-map/COVERAGE.md`

Preserved all nine files under the earlier
`experiments/20261014-133815-cycle-excess-one/` and its
`notes/project-map/integration-2026-10-14-cycle-excess-one.md` receipt.
Their complete pre-existing file list is in that experiment's report.md.
No existing proof, HANDOFF, GOAL_SPEC, manuscript, skill, or user artifact
was edited. No commit or push. The distinction between finite certificates
with a completeness argument and asymptotic spectral extrapolation is
already in the research rules; no workflow/skill change is needed.
