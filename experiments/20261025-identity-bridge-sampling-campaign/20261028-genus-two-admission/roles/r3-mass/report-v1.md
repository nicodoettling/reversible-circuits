# R3 mass/falsification — immutable report v1

Frozen 2026-10-28, I1.v1, campaign attempt000002. **Verdict: keep the complete obstruction candidate for fresh blind and exact-version nonauthor review.** Author mathematical disposition: proved from the explicit inherited DYZ source identity; campaign disposition: provisional. Main sampler mission remains OPEN. This report does not certify its own proof.

## Result and global consequence

The new enlarged-event argument shows the following candidate statement. For every integer j>=64, let N=2^(8j), m=2^(6j), and L=max{1<=v<=N:3^v<=(N+m+2)^4}, fixed at the original input. For every integer0<=G<=2^j, define E_(G,L) by permitting all support components with genus g<=G OR support size v<=L. Then

    U_(N,m)(E_(G,L)) <= 2^(-1-jm/2).

Every probability law supported on this event consequently has TV error at least1-2^(-1-jm/2). This includes the assigned M2 policy G=2. For fixed G, the explicit threshold is j>=max{64,ceil(log_2(max{1,G}))}. The separately admitted growing-genus scope permits G up to N^(1/8) on the same sequence; no efficient decoder for those genera is assumed or supplied.

If accepted, this rejects the claim that the declared genus-two/small-support policy is a global sampler throughout the benchmark m=N^(3/4). It leaves a genus-two connected primitive valuable but insufficient by itself. A sampler for the entire mission must cover mass outside this enlarged event or use a different mechanism. This is not a hardness theorem, not an impossibility result for all samplers, and not a local heat-bath spectral-gap conclusion. No all-N strengthening of the older provisional blind report is asserted.

## Precise new ingredient

The historical accepted H0/H2 numerator only included unrestricted genus0/1 plus arbitrary genus on small supports. Failure of that smaller event does not imply failure after enlarging it. The new proof instead bounds every added genus term. Write k=m/2, x=k/N^2, q=3Nx. The inherited checked majorant

    A_g(v)=C(v,2v-2+2g)/(2v-2+2g)! <=v^(v-3)((v^3-v)/36)^g/g!

and a geometric moment estimate give

    S_g(x)<=9k*x^g*c_g,
    c_g=(3g-2)!2^(3g-1)/(36^g g!) <=(6g^3)^g.

Thus the exact enlarged component assembly is dominated by S<=147k/20<8k whenever q<=1/2,b_L*x<=1,6G^3*x<=1/16. These explicit conditions hold throughout the stated sequence and G range. The existing elementary embedded-subgroup lower bound then yields the displayed probability bound. All component labeling/interleaving factors and the genuine bridge normalizer are retained. No sequential marginal bounds are multiplied.

Full statement, dependency graph, reconstructed source majorant, finite estimate, sequence constants, denominator proof, boundaries and remaining certification obligations: [proof-v1.md](proof-v1.md). Original fixed-G scope: [plan-v1.md](plan-v1.md). Separately admitted uniform scope: [scope-growing-v1.md](scope-growing-v1.md). The source recurrence is inherited from the exact September22 source audit and nonauthor reconstruction, not a fresh external source check by this worker.

## Finite falsification and exact reference checks

One coordinator-reserved job I1-J3 ran through current v0.3.2 bounded.py and attempts/000002/run.json. Exit0; all checks PASS. Deterministic standard-library Python3.12.3, seed0 recorded but unused. Authorized90s/1GiB; observed tool wall0.055754336s, script0.0308246871s, largest literal DP57 states. Peak RSS was not measured. Raw output93010bytes; console one short line. Exact command and environmental metadata: [bounded-job-I1-J3-receipt-v1.json](bounded-job-I1-J3-receipt-v1.json).

-63 connected-count/majorant cells from the positive DYZ recurrence, v2..8,g0..8.
-33 independent permutation/product/support/length DP reference cells, N2..4,m0..10, including odd lengths.
-162 exact comparisons of allowed-event counts from component assembly against independent DP, G0..2 and each fixed cutoff1..N.
-64 rational geometric-moment checks through g16 and q in{1/64,1/8,3/8,1/2}; exact c_g envelope checks.
-15 exact subgroup-denominator checks and9 selected sequence-condition checks through j128, with the j>=64 final constant inequality tested by squaring positive sides.
-CP-1 retains rejection of the historical0.0105<=0.01 marginal-product claim. The analytic argument does not use it.

Selected literal reference counts:

| N | m | All identity words | Connected identity words on all N labels |
| --- | --- | --- | --- |
| 3 | 4 | 27 | 24 |
| 3 | 8 | 2187 | 2184 |
| 4 | 4 | 120 | 0 |
| 4 | 6 | 3936 | 2880 |
| 4 | 10 | 5039616 | 4959360 |

Source/normalization diagnostics validate the new target cases S3,m8 and S4,m10 and preserve required S3,m4,S4,m4,S4,m6 checks. They can expose false finite formulas; they do not prove an asymptotic theorem. Full raw exact rationals and integer counts are in [finite-results-v1.json](finite-results-v1.json); reproducible implementation is [finite_checks_v1.py](finite_checks_v1.py).

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
| --- | --- | --- | --- | --- | --- |
| E_(G,L) support-policy obstruction | Global fixed-length uniform bridge reference | Product DP checks exact identity counts | Not a transition sampler; no such claim | Counts, component eligibility, lengths, parity and assembly matched | Keep provisional obstruction; M2 policy fails if proof accepted |

No sampler logic was changed. Edge-frequency/prefix histogram tests therefore do not certify or test a new sampler here.

## Claim ledger and unresolved work

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
| --- | --- | --- | --- | --- | --- |
| Uniform factorial genus majorant | inherited proved input; reconstructed | Exact DYZ identity/count normalization and genus-zero value | proof-v1 sections1; pinned historical source checks | Historical separate source reconstruction;63 finite cells | Preserve explicit source dependency |
| New finite enlarged-event bound | author proved; provisional | q<=1/2,b_J*x<=1,6G^3*x<=1/16, exact assembly | proof-v1 section2 | Finite exact moment/assembly checks only | Fresh exact-version audit |
| M-GROW.v1 | author proved; provisional | Explicit sequence,0<=G<=2^j, same top-level L | proof-v1 sections3–4 | Sequence finite checks; no fresh proof referee yet | Blind theorem-only review and argument audit |
| FG.v1 and M2 obstruction | author proved corollaries; provisional | Fixed G / G2 specialization | proof-v1 statements | Depend on M-GROW scope review | Reject only declared global support policy if accepted |
| Older H0/H2 obstruction | accepted-inherited at original scope | Original source versions | Pinned old obstruction/corollary | No status upgrade from this role | Preserve |
| Older all-N blind claim | provisional | Its original exact statement | Pinned old blind_report | No scope-matched acceptance supplied here | Preserve as provisional; not used |
| Global polynomial sampler mission | unresolved | Frozen independent-bit model and all feasible N,m,b | No all-length algorithm in this role | None claimed | Continue research |

The author finds no missing internal mathematical inequality beyond the explicit literature input. The next required obligation is certification of this exact version: fresh blind theorem-only report, separate nonauthor argument audit, coordinator decisive reproduction and dependency closure. [blind-statement-v1.md](blind-statement-v1.md) contains only the theorem/definitions/allowed primary source/boundary obligations. It contains no candidate proof, verdict or confidence. Worker reviews use the same model and are correlated; this role is not itself blind.

## Preserved negative findings and boundaries

The historic H0/H1 benchmark and enlarged-cutoff failure remain at their exact scopes. The stronger all-N blind report is not treated as accepted or novel. Zero-square insertion,(ab)^3, support-conditioned81-versus80, unweighted graph bias, marked-cut multiplicities and adaptive-normalizer failures remain valid counterexamples to their original claims; this count argument neither reuses nor repairs those mechanisms.

Odd m has empty target; m0 has the unique empty word; m2 is a repeated transposition; N2 has one word at each even length and L2. None contradicts the displayed asymptotic sequence. Singleton positive genus and negative genus are infeasible and never normalized. All minimal components remain allowed. The source and proof conventions distinguish degree N from log_2(N) wires.

## Artifacts and operational limits

All new/changed role files are confined to this directory:

- input-v1.md: full received worker task and inherited-context disclosure.
- plan-v1.md: original fixed-G quantified target and resource/test plan.
- checkpoint-early-v1.md and checkpoint-halfway-v1.md: durable progress.
- scope-growing-v1.md: separately authorized uniform-G target.
- proof-v1.md: full immutable proof candidate.
- blind-statement-v1.md: theorem-only review packet.
- finite_checks_v1.py and finite-results-v1.json: code and full exact raw output.
- bounded-job-I1-J3-receipt-v1.json: command, reservation, exit and resource evidence.
- freeze-manifest-v1.json: exact source/own-artifact hashes before this final report.
- report-v1.md: this immutable report.

No central/protected file, other worker directory, supervisor metadata or historical report was edited. No worker descendants, separate research CLI sessions, installations, Git staging or commits were used. Astra/ultra/default is inherited requested configuration; server-returned worker tier is not observable through the role interface. Attempt deadline was read; report completes well before13:00UTC and the hard cap16:45:16UTC. Git status was inspected; coordinator owns the full shared-worktree reconciliation and checkpoint.
