# R2 structural final report — C2.v1

Frozen2026-10-28. Verdict: **promote for fresh blind and exact-version audit**. Status: complete author proof and prototype, **PROVISIONAL**, not coordinator acceptance. Main mission remains OPEN.

C2.v1 is an exact expected-polynomial-bit sampler for connected identity transposition words on[N] of length2N+2, for everyN>=2. This is the requested identity genus-two primitive. It does not supply arbitrary-endpoint genus-two sampling or an unrestricted global sampler. The only imported mathematical interface is accepted S-G01: exact connected genus-zero/one fixed-endpoint counts and actual samplers. Products act rightmost first, words are ordered and labeled, and the probability theorem uses independent fair bits. DegreeN is the resource parameter. The full statement is theorem-v1.md, argument proof-v1.md, implementation cut_genus_two.py.

## New construction and exact law

The elementary identity g=G_L+G_R+beta_1 holds at every cut of a connected identity word. Prefix genus rises by unit increments. In a genus-two word, every cut after the first genus increment and before the second has G_L=1, so G_R<=1. The incidence graph is a tree when G_R=1, a unicycle when G_R=0. Coverage is proved for every word, including N=2 and zero-length singleton factors.

Every such graph has one genus-one left vertex. The tree case has one genus-one right vertex and is rooted intrinsically at its unique genus-one left vertex, leaving only child-order factorials to correct. The unicycle case has no right genus-one vertex and uses the previously audited2s core-root/direction quotient, including parallel cores. Local normalized counts H_0,H_1 retain all individual incident cycle sizes. Cycle-labeling rotations and local word/interleaving factorials give the exact macro weight N!j!(2N+2-j)! product_e A(a_e) product_v H_{h_v}(a(v)).

The positive grammar tracks total edge-size mass, color imbalance and two binary genus totals. It augments the earlier forest table by Q,E_j,W_j moments. The actual parser chooses every successive child using the exact residual moment mass with the parent/core ports **and all earlier chosen child sizes fixed**. This is a concrete polynomial conditional decoder; it never enumerates all subsets or treats scalar counts as word-completion counts. It samples uniform marked cut pairs. Accepting a pair with probability1/|J(w)| gives every literal word equal accepted mass. Fresh proposals have expected at most2N+1 trials.

The proposed conservative bound is O(N^20 log^4(N+1)) expected bit operations and polynomial space; it is deliberately loose. The full proof gives explicit table indices, a common polynomial-bit denominator for all partial and conditional masses, exact fair-bit categorical draws, and stack-based parsing. The first unproved mathematical step claimed by the author is **none under S-G01**. Certification remains outstanding and must examine this exact proof and code; the indicated bound is not a practical large-N benchmark.

## Exact finite evidence

Job I1-J2 ran once through the current v0.3.2 bounded helper and attempt000002 sealed run, with coordinator reservation,180s wall limit and1GiB address-space cap. It completed exit0 in observed0.71835s, below the estimated256MiB memory budget (actual peak memory was not measured). Python3.12.3; standard library only. Full command, parameters, estimates and outcome are in job-I1-J2-plan.json and job-I1-J2-outcome.json.

The audit intercepts the production numeric parser's categorical choices to exhaust every positive execution branch with exact rational probability. It compares that law to an independent finite plane-tree/unicycle inventory using the **subtractive**, independently coded H_1 expression. It then exhausts all label shuffles and compares the complete macro projection to the coordinator's literal word enumeration where available.

| N | numeric codes | labeled macros | cut incidences | exact-law check |
| --- | ---: | ---: | ---: | --- |
|2|2|2|2|actual parser and full literal-reference macro law|
|3|10|23|4656|actual parser and full literal-reference macro law|
|4|47|303|11952000|actual parser versus independent numeric inventory; full label projection|

The coordinator's independent reference finds2184 connected genus-two words at N=3, with2712 unicycle and1944 tree cut incidences. These references are `../../coordinator/cut-reference-results-v1.json`; they are retained as parent-owned evidence, not reproduced or modified here. N=4 was not compared to full literal word enumeration in this role. The audit contains every macro probability and every parser-execution summary in grammar-results-v1.json.

Five accepted samples for each of seeds1729,2718 and each N=2,3,4 passed exact length, product, support, genus and cut checks. Those PRNG samples are reproducible validity diagnostics only; they do not support the universal uniformity or runtime claims. The exact parser tests use seednull.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
| --- | --- | --- | --- | --- | --- |
|C2.v1 positive genus-one-decorated cut grammar|exact uniform connected identity genus2, length2N+2|proved in candidate; all samples valid|not a walk; universal cut coverage of its fixed target|actual numeric parser N<=4, complete label macro law N<=3 against literal reference|promote for fresh audit|

## Dependencies, retained failures and review gates

All new claims are provisional author proofs: C2.1 coverage; C2.2 weights; C2.3 code multiplicities; C2.4 finite grammar; C2.5 actual parser; C2.6 target law and bit complexity. Their complete dependency graph is in proof-v1.md. S-G01 is accepted-inherited, with its original exact-source normalization and audits preserved. No old source status changed merely because of this attempt.

Every prior failure remains recorded: zero-square insertion `(ab)^3` and its extensions; ordinary endpoint81 versus connected80; unweighted triangle mass1/4 versus required3/4; unequal-cut forgetting; parallel-core and equal-child order multiplicities; CP1's21/2000>1/100. The parent reference reran the global27/120/3936 totals, boundaries and probability regressions. C2 uses full connected local counts and exact posterior normalization, avoiding the failed implications rather than asserting that they were repaired. No failure of a sufficient mechanism is a refutation of the global mission.

Required next gates: a fresh theorem-only referee using theorem-v1.md; separate exact-version nonauthor review of proof/code/raw evidence; coordinator decisive reproduction and claim reconciliation. Reviews from the same model are correlated. The main points needing adversarial scrutiny are the conditional moment oracle with previously fixed sizes, unique-root/parallel-core multiplicities, and polynomial-bit accounting. Any repair must create a new version and reopen its dependency cone; this frozen version must not be silently edited.

## Provenance and owned files

Base commit d8893491e04aff74ff3185f7054470ffa24a44a4. Parent brief I1.v1 fixes all deadlines; construction froze before the13:00 report deadline. Model/effort/tier requested and inherited gpt-6-astra/ultra/default. The worker interface exposes no independent server-returned service-tier attestation. No overrides, descendants, separate research CLI sessions, installation, Git stage/commit or protected-file writes were performed.

Owned artifacts: input-v1.md; plan.md; checkpoint-early-v1.md; checkpoint-halfway-v1.md; theorem-v1.md; proof-v1.md; cut_genus_two.py; audit_grammar.py; grammar-results-v1.json; job-I1-J2-plan.json; job-I1-J2-outcome.json; report-v1.md; freeze-manifest-v1.json; SHA256SUMS-v1. The manifest freezes exact payload hashes and external dependency/reference hashes. Only this role directory was edited. No manuscript-ready claim is promoted into the manuscript by this report.
