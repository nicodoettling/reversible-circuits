# Identity-Bridge Sampling Programme

Version 1.1, operational clarification 2026-10-28 (Europe/Berlin). Scientific
cards P0.v1-P5.v1 and their scopes are unchanged. Planning state: active
authorized attempt; I1 active after P0 admission (D-20261028-04). Campaign ID: `identity-bridge-sampling-20261025`.

## Objective and Evidence

Develop a sampler for the uniform law on ordered transposition identity words
in S_N, with exact length and endpoint, total-variation error at most 2^(-b),
and expected bit time bounded by one polynomial in N,m,b. Inputs are N>=2,
even m>=0 and b>=1; output length is explicit. Independent fair bits and
rightmost-first composition are the mathematical conventions. Degree N,
output length m and precision b are distinct resources.

The current evidence hub is the [research map](../../PROJECT_MAP.md). On the
campaign branch its generated entry point is `notes/project-map/FRONTIER.md`.
Exact statements and reviews linked from the catalogue govern mathematical
status. This programme governs allocation of work, rather than acceptance.

The [connected-component reduction](../../experiments/20260922-sparse-boundary/roles/r4-construction/reduction.md)
removes scalar counting, component selection, labels and interleavings from one
sufficient route. Its remaining primitive concerns larger support and genus
g>=2. For a connected identity word on v vertices, length=2v-2+2g.
The [existing recursive construction](../../experiments/20260907-genus-one-sampler/proof.md)
and [marked-cut construction](../../experiments/20260907-genus-one-sampler/roles/r2-structural/report.md)
are predecessors, with their recorded review limits.

## Portfolio

| ID/version | Planning state | Question | Map predecessors | Entry condition |
| --- | --- | --- | --- | --- |
| P0.v1 | achieved for I1 | Which existing result or new test makes the next allocation worthwhile? | T-CONNECTED, T-MASS, T-AUDIT | Read exact claims, relevant old failures and current recovery state |
| P1.v1 | active in I1 | Can final-letter recursion sample connected genus-two words efficiently? | S-G01, R-CONNECTED, O-COUNTS | P0 finds an uncovered statement and a concrete allocation identity/test |
| P2.v1 | active in I1 | Can the marked-cut construction extend beyond genus one? | S-CUT, O-COUNTS | P0 identifies a new cut/grammar with specified multiplicities |
| P3.v1 | active in I1 | Which component types carry enough bridge probability to extend the global regime? | S-COUNTS, S-SPARSE, O-H0, O-H2 | A specified event/policy and exact count computation or asymptotic lemma |
| P4.v1 | reserve | Can the rank lift improve accuracy at fixed length? | S-DENSE, S-STAR, O-TABLE | A new positive connection law, avoiding rejected endpoint inventories |
| P5.v1 | audit/delivery | Does the exact current result survive full review and change the global frontier? | T-AUDIT and the selected result | Frozen statement, proof/code, complete reports and executable regressions |

Planning states: planned, active, achieved, falsified, inconclusive, blocked,
retired. They apply to the card's deliverable. HOLD allocates no repeat until
a named entry artifact exists. Card changes need a new version if their target,
assumptions or success criteria change; preserve old cards in decision receipts.

## P0.v1: Admission and Allocation

Allocate at most 30 minutes of the first research wave to focused admission.
Read the map's exact source/version and strongest predecessor before declaring
a claim new. Search relevant old role directories and primary literature only
for a named counting/decoding/transfer question. Reconcile the stronger blind
all-N sparse obstruction before proposing it as a new result.

Deliver a frozen investigation brief specifying its distribution, all quantifiers,
first discriminating test, resource regime, relevant regressions, review plan,
maximum allocation and what each outcome changes. Rank by scope gained, a new
ingredient, cheap falsification and value of a negative answer. Recency and an
unproved technical sufficient condition alone do not determine priority.

Positive admission enables only that in-scope card. Overlap retires that version
and preserves the old result. An empty regime or missing comparison produces a
receipt and HOLD, not an automatic waiver. If all cards are ineligible, request
operator review with the missing entry artifacts; do not circulate between them.

## P1.v1: Recursive Genus Two

First target: sample connected identity words on v>=2 fixed labels at length
2v+2, error <=2^(-b), expected poly(v,b) bit time. Prefer the closed recursive
interface with arbitrary specified endpoint sigma and length
v+c(sigma)+2. Reject infeasible/zero-count inputs. Exact sampling is welcome.
This case alone is not the unrestricted global sampler.

Prerequisites: the exact S-G01 final-letter law and its scoped reviews;
arbitrary-endpoint genus-two counts/conditional weights are obligations, not
consequences of identity scalar counts. First derive all final-edge branches,
including two genus-one children. Test whether partially forced assignments of
individual labeled endpoint cycles admit positive polynomial-size aggregation.
Do not enumerate all subsets and call the result polynomial.

A positive result must produce actual words with a proved per-word law and
bit bound, and record the dependence on genus. It opens P3/P5 and a separately
admitted higher-genus extension. A counterexample retires the failed compression
or law, preserving S-G01; it opens P2 only if P2's own entry condition holds.
An inconclusive result isolates the first missing formula/oracle as a lemma.
HOLD the unchanged version until a new identity, witness or compression appears.

## P2.v1: Beyond the Genus-One Cut Grammar

Target the same connected 2v+2 law through a structural decomposition. State
the proposal on marked objects, an actual parser, label/interleaving weights,
number of representations of each literal word, and the correction for
forgetting marks. Supply the rejection/variance and bit-cost bounds needed for
polynomial sampling. An incidence count by itself is insufficient.

First test: does the proposed cut exist for every target word, or does a declared
restricted family omit mass? Check the smallest cases and the old zero-square
fibers before constructing a large grammar. Preserve parallel-core and repeated
substructure multiplicities from C1's regression/audit records.

Positive construction opens P3/P5. A missing cut or biased forgetting step
falsifies that construction version, not the existence of a sampler. Keep any
valid auxiliary bijection/count even if its proposed sampler application fails.
Inconclusive or non-polynomial descriptions require a new cut or bound before
another allocation. Genus-dependent exponents must remain explicit.

## P3.v1: Component Mass and Global Usefulness

Use the exact bridge-conditioned C(v,ell) counts and least-label assembly to
identify support/genus events in the gap between the proved sparse range and
m=N^(3/4). Freeze the policy and cutoff at the original input. First calculate
exact selected probabilities at a small declared grid and falsify a specific
universal inequality. Ordinary unconditioned random-graph behavior is not a
substitute for bridge normalization.

Deliver either a new policy with a proved useful omitted-mass bound, a reviewed
obstruction to a proposed policy, or a precise asymptotic lemma still needed.
Tie every proposed decoder extension to its global mass consequence. P1/P2 may
be achieved while a global application remains open or fails.

Do not rerun the H0/H1 benchmark refuted by O-H0, the logarithmic-cutoff-only
repair refuted by O-H2, or the genus<=1-only global claim refuted at m=2N.
Finite plots alone cannot establish a sharp transition. If the diagnostic has
no new algorithmic or obstruction consequence, place that version on HOLD.

## P4.v1: Conditional Reserve

At fixed feasible N,m, seek an old/star connection law whose accuracy improves
with b in poly(N,m,b). S-STAR supplies one primitive, not the joint branch law.
Admission requires an explicit new positive conditional identity or falsifiable
proposal avoiding full labeled endpoint/type inventories. Do not allocate this
reserve simply because P1 and P2 are blocked. Success, rejection and HOLD use
the same exact-word and resource criteria as P1.

## P5.v1: Review and Integration

Use the mathematical-proof-audit protocol. Freeze the full theorem and its
dependencies; obtain a fresh blind report with only the theorem, definitions,
assumptions and permitted sources, then a separate exact-version adversarial
review. Recycle the three worker slots without exceeding four total agents.
Keep raw prompts and complete reports. Same-model reviews remain correlated.
Repairs reopen all affected claims and require fresh checks.

Test boundaries m odd, m=0, m=2, N=2, minimum connected length and zero-mass
branches as relevant. Validate changed sampler logic against exact S_3,m=4 and
S_4,m=4 references, with S_4,m=6 when feasible, and appropriate new-target cases.
Check full finite laws where feasible, not just validity or marginal histograms.
Preserve (ab)^3 insertion failures, support-conditioned 81-versus-80 counts,
graph-weight bias, and the conditional-probability regressions in source audits.

Acceptance needs a closed current dependency graph, explicit fair-bit and
bit-complexity model, complete reviews, regression results and a clean-state
reproduction. A failed application preserves an accepted auxiliary result.
An interrupted review remains integration pending; it does not certify a theorem.

## Allocation, Routing and Stopping

One coordinator and three workers, all Astra Ultra/default tier, within the
prepared manifest. Initial proposed roles: recursive construction, structural
construction, and component mass/falsification. The coordinator may change roles
or use fewer slots when the admitted question warrants it. Fresh review slots
follow frozen reports. Workers own distinct directories and never edit the map,
programme, manuscript, shared instructions or another worker's files.

Each research allocation normally lasts 2-4 hours including at least 40 minutes
for review/integration; it must fit the current attempt deadline. The harness's
six-hour attempt envelope is a recovery boundary, not the overall research
deadline. This preparation authorizes no inference and sets no total runtime
or spending promise. Later operator launch starts the frozen mission, with
recovery and quota resume as explicitly selected by the user.

After each allocation append an outcome receipt, reconcile map dependencies and
cards, and choose the next eligible investigation within this same mission.
The coordinator can propose a new in-scope card, with the same admission and
review requirements, instead of following a fixed proof ladder. A new generator
model, cryptographic objective or unrelated campaign requires operator direction.

No unchanged card receives repeated inconclusive allocations without a named
new ingredient. After two inconclusive allocations to an essentially unchanged
mechanism, HOLD it and state what would reopen it. If every branch is held,
publish an unresolved structured NEEDS_ATTENTION.json request after freezing
the safe handoff/checkpoint, using the six-field protocol in the current mission.
A prose-only exit or COMPLETION.json is not the blocked-state signal. Do not wait in
an inference loop or invent an automatic escalation ladder.

Terminal positive outcome: the frozen global sampler theorem has a closed proof
and complete review. Terminal refutation requires a checked impossibility result
under its exact declared computational model/assumptions; failure of a method
does not qualify. An exhausted frontier can end execution for operator review
with the mathematics explicitly unresolved, using operator attention rather
than theorem completion. A partial result triggers the next
eligible allocation rather than a false declaration of overall completion.

## Durable Decisions

Append outcomes to [PROGRAMME_DECISIONS.md](PROGRAMME_DECISIONS.md) before updating
cards; preserve old versions under the campaign's immutable investigation files.
Receipts name exact proofs/reviews/hashes, mathematical and planning status,
scope gained, failed routes, affected dependencies, enabled/disabled actions,
actual resources where observed, and unchanged priorities with reasons.
Update catalogue target priorities and launch-brief dispositions with the same
reviewed delta. Use [UPDATE_PROTOCOL.md](UPDATE_PROTOCOL.md) for discovery,
evidence and generated views. In the campaign catalogue, FRONTIER.md is the
front page; primary PROJECT_MAP.md remains the pre-campaign snapshot.

This programme is inert in ordinary sessions. Its research/review/checkpoint
obligations apply only inside the explicitly started campaign's sealed attempt.
Preparation, normal edits, status checks and Git requests do not activate them.
