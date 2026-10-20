# A meaningful static assumption for generalizing local mixing

Verdict: **keep** the proposed conditional-decorrelation research target and
the proved implication, provisionally pending independent review. The
uniform hypothesis and general local mixing remain **unresolved**.

## Recommendation

Assume that, under the uniform word law conditioned on ANY total product,
the first and last thirds have maximal correlation at most 1-delta for a
universal delta>0. This means every pair of nonconstant observables of
the two separated pieces has correlation bounded away from one. It is
a stationary-law statement, rather than an assumption that some other
walk mixes rapidly. The hypothesis can be checked or falsified directly
from the completion-count matrix

    J(u,v)=Z_a(u)Z_b(u^-1 g v^-1)Z_a(v),  a=floor(m/3), b=m-2a.

The original endpoint-blind marginal condition does not supply this
conditional correlation estimate. The stronger condition precisely
controls the interaction between blocks that the user's proposal needs.

## Conditional theorem obtained

For K_A=I/2+H/4+R/4, define Lambda_N(m) as the worst-endpoint gap
multiplied by m-1. The two overlapping intervals AB and BC yield

    Lambda_N(m)>=delta/2 * Lambda_N(m-floor(m/3)).

Only a constant loss is paid when length shrinks by a fixed fraction.
Iteration to a cutoff k therefore transfers any polynomial base gap to
polynomial mixing at every larger length and every endpoint. A theorem
for all endpoint complexities <=k supplies the base because every word
of length <=k has such an endpoint.

The prior length-three theorem already gives beta_N(3)>=1/12. Under
the proposed decorrelation assumption, it follows that

    gap(K_A)>=delta/[24(m-1)(m-2)^alpha],
    alpha=log(2/delta)/log(3/2),  m>=4.

This is a conditional bound for the original small-move walk, from all
starting states. It is not a claim that the static assumption is proved.
The fixed mixture (K_A+Q345)/2 inherits half the gap. Polynomial means
polynomial in N,m,log(1/epsilon), not necessarily in log N wires.

## Weaker hypotheses and the N/2 proposal

Uniform decorrelation can be weakened to a polynomial bound on the product
of inverse correlation deficits along the shrinking-length sequence. A
bounded number of inverse-polynomial bad scales is allowed; an unspecified
polynomial loss at EVERY scale can instead lead to quasipolynomial time.

Using the archived sharp O(N log N) parity smoothing, the N/2 proposal has
a useful more permissive corollary. Assume the low-complexity mixing theorem
through k=floor(N/2), N>=6. Only for intermediate lengths k<m<C N log N,
assume 1-rho>=c/(log(N+2))^B. There are O(log log N) such scales, so
their combined cost is exp(O((log log N)^2)), bounded by a polynomial
in N. Longer scales already have constant decorrelation by smoothing.
Thus these two hypotheses imply global polynomial mixing. For a log N
cutoff the same inverse-polylog deficit is not enough for a polynomial
bound by this proof; a constant deficit or the displayed scale-product
bound suffices.

The sharp smoothing import is traced to archived M10 and its referee,
and to Diaconis--Shahshahani Lemma 14, equation (3.1), and the end of
Section 3. The primary source's Plancherel estimate and the archive's
nonlazy parity translation were checked. It is not inferred from total
variation mixing alone. The main constant-delta implication does not use
this external input.

## Falsification results

| N | Tested lengths | Feasible endpoint-type cases | Largest numerical estimate |
|---|---|---|---|
| 3 | 4--12 | 14 | 0, also proved exactly at all lengths |
| 4 | 4--12 | 23 | about 0.200000 |
| 5 | 4--12 | 32 | about 0.539081 |
| 6 | 4--8 | 28 | about 0.573758 |

These are 97 finite cases, not an asymptotic proof. Power iteration gives
numerical lower approximations to the largest centered singular value.
Seeds 20261020 and 20261021 agree within 5.2e-9 on the final run, but
four cases hit the 1000-iteration cap. Neither convergence flags nor seed
agreement certify an upper bound. Separate exact rational PSD calculations
prove rho<99/100 in all 37 tested S3/S4 cases.

The tempting stronger constant rho<=1/2 is refuted exactly. For S5,m4
and g=(12)(34), label 0 fixed, use tail observable 0 on the endpoint's
two transpositions, 9 on cross-pair transpositions within {1,2,3,4},
and -16 on transpositions involving 0. Its correlation between the two
tails is exactly 917/1800>1/2. This is retained as a negative result;
it does not refute existence of some other uniform constant below one.

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
|---|---|---|---|---|---|
| Conditional decorrelation criterion for original K_A | Uniform fixed-length prescribed-product words | original product-preserving kernel unchanged | inherited square-refresh capability; no new sampler implemented | exact count formula, finite rational correlation certificates, recursion normalization | keep conditional theorem; global hypothesis unresolved |

## Reproduction and boundaries

Command:

    python3 -B experiments/20261020-073334-bridge-decorrelation-bootstrap/check.py

Final run commit 99bc9e206a980bc2a57c6f418cd53e0486f5b9fc, Python 3.12.3,
standard library only. Manifest hashes both this script and the imported
previous permutation/count helper. Required identity S3,m4 and S4,m4,m6
are enumerated to validate the joint count matrix, with 27,120,3936 words.
The script checks 499,497 adjacent-slot decompositions and exact recursion
rounding. No sampler logic changed, and no MCMC convergence experiment is
used to infer a gap.

Empty and singleton fibers, m0,1,2, N2, endpoint parity and feasible odd
lengths are explicitly treated in the proof. Near-minimal endpoint types
are included within the finite search range. Growing-N near-minimal
families remain a useful place to try to falsify the hypothesis.

## Workspace changes

New files: this experiment's plan.md, proof.md, check.py, results.jsonl,
claim_ledger.md and report.md; plus
notes/project-map/integration-2026-10-20-bridge-decorrelation-bootstrap.md.

Further updates to map files: notes/project-map/COVERAGE.md, notes/project-map/RESULTS.md,
notes/project-map/catalogue.json and notes/project-map/inventory.json.
Rendering leaves PROJECT_MAP.md unchanged.

All October 14, October 15 and October 19 research directories and their
existing integration receipts are preserved. No HANDOFF, GOAL_SPEC,
AGENTS, manuscript or skill changes; no installations, agents, commits,
pushes or external messages. Map registration is provisional, not
independent mathematical certification.

During this turn HEAD advanced externally to
99bc9e206a980bc2a57c6f418cd53e0486f5b9fc, which tracks the prior research.
This agent made no commit and preserved those contents. The run manifest
retains the commit observed when the final numerical run started. Temporary
bytecode from an exploratory import was removed before the final status check.
