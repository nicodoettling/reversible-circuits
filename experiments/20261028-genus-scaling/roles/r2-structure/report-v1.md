# R2 structural report v1 — uniform topology and rejection, local coefficient gap retained

Frozen2026-10-28 15:04UTC. Verdict **keep/promote the scoped structural partial for fresh review**, not a T0/T1 theorem. New claims S1–S4 are author-proved **PROVISIONAL**; no independent current-version acceptance is implied. The strongest result is that every connected identity word of genus g>=2 has a penultimate-genus marked cut whose incidence graph is a tree or unicycle, and reciprocal-cut rejection needs at most2N−2 proposals in expectation, independently of g. This removes growing graph cores and rejection cost as necessary obstacles to this particular structural route.

The exact frozen statements are theorem-v1.md and the complete argument is proof-v1.md. The target is uniform on literal ordered transposition words on exact labels[N], length2N−2+2g, connected support, rightmost-first product identity, fair-bit computation. N is permutation degree. No Markov-chain, all-length global, or log-N-wire complexity claim follows.

## What is proved in the candidate argument

For G(u)=(|u|−N−c(u)+2q(u))/2, every appended letter increases G by0 or1. For a genus-g target word, cuts with G_left=g−1 form a nonempty interval. At every such cut g=G_left+G_right+beta, with beta the connected incidence graph's cycle rank. Therefore G_right+beta=1, giving exactly the tree/right-genus1 and unicycle/right-genus0 alternatives.

The potential P=N+c−2q lies in[1,2N−2] at these nonempty positive-genus prefixes. Since j=2(g−1)+P, there are at most2N−2 admissible cuts. This is a universal pointwise inequality, stronger than the old length-based proposal bound. N2 attains it for every g>=2: the cuts are2g−1 and2g.

The exact weight is N!j!(m−j)! product_e[a_e^(2a_e+1)/(a_e!)²] product_v H_(h_v)(a(v)), using every individual incidence size and actual connected endpoint counts. Here j=N+(#right−#left)+beta+2g−3. Tree codes root a left genus-h vertex with weight h/(g−1), then divide by every child-order factorial. Summing these root masses gives1 even with several positive-genus vertices. Unicycle codes retain the2s core-start/direction divisor, including two parallel edges. Equal numerical child shapes remain distinct after cycle labels. These factors give the full marked literal-word law; accepting with1/|J(w)| corrects nonconstant cut multiplicities exactly.

## The algorithmic gap is explicit

A uniform-topology symbolic grammar needs only mass, imbalance, left genus<=g−1 and right genus<=1, with O(N²g) scalar indices and at most two external ports before parsing. It avoids the N^(O(g)) port assignments arising from a naively enumerated higher-excess kernel. Its fixed-port forest contraction, PORT-CONTRACT.v1 in proof Section5, must sum H_h(P,a_1,...,a_k) against an arbitrary supplied ordered branch table, conditioned on mass/genus indices and all already chosen sizes. The required bound is f(g) times an absolute polynomial in N,g and input bit length. Scalar H_h evaluation alone does not establish this bound.

Literal local connected endpoint decoders beyond the accepted genus range are also required. This role does not infer them from scalar counts or from identity-only recursion. Conditionally on PORT-CONTRACT and such decoders, both with the requested uniform resource bounds, the structural overhead has an absolute polynomial exponent and only O(N) outer rejection. Thus the first unproved structural coefficient step is precise, but this report alone does **not** claim that T0 has been reduced to only one complete primitive, nor that a genus ladder proves FPT. The initial balanced-cut core route and its N^(O(g)) implementation risk are retained in proof Section7 as a negative finding, not a lower bound.

## Exact finite falsification

Coordinator reservation J2 ran check_cuts_v1.py through the current v0.4.2 bounded helper and sealed attempt000001 run. Timeout180s, address ceiling1GiB, estimated memory<128MiB. Exit0; tool time0.055965423s and child time0.039585739s. Actual RSS was not measured. Python3.12.3; standard library only; deterministic exact computation with seednull. Exact argv and resource provenance are job-J2-plan.json; raw output is cut-results-v1.json. No worker-side mathematical execution occurred.

The script uses a weighted-support/permutation dynamic program and a separately implemented partition-lattice inversion of ordinary subgroup walk counts. It checks189 connected reference cells. It then checks every marked macro and the complete plateau-size distribution at genera2/3. No literal word enumeration is used; in particular N4,g3 is handled with at most63 weighted-support states per layer and240 plateau-augmented states.

|N|g|connected words|marked pairs|acceptance|
|---|---:|---:|---:|---:|
|2|2|1|2|1/2|
|2|3|1|2|1/2|
|3|2|2184|4656|91/194|
|3|3|19680|39648|205/413|
|4|2|4959360|11952000|861/2075|
|4|3|180686880|394778880|125477/274152|

All12 N2/3/4,g0..3 connected counts were retained. Every g2/g3 macro passed the independent local-count/interleaving factorization, genus identity, root weights summing1, and parallel-core multiplicity checks. The full cut histogram certifies finite coverage and the2N−2 maximum in these cases. This is finite evidence for the universal proof, not its substitute; it is not a production high-genus sampler check.

|candidate|claimed target|identity valid|crosses Hurwitz components|exact diagnostics|verdict|
|---|---|---|---|---|---|
|penultimate-genus marked-cut representation|connected identity F(N,g), conditional on exact marked sampling|candidate universal proof and exact finite macro laws|not a walk; complete marked representation of its fixed target|N2/3/4,g0..3 counts; all g2/g3 cut macros and histograms|keep scoped structural partial; T0/T1 remain open|

## Retained regressions and dependencies

The job reproduces S3m4=27,S4m4=120,S4m6=3936; ordinary endpoint81 versus connected80; graph triangle3/4 versus unweighted1/4; the zero-adjacent-square identity(ab)^3; and CP1's21/2000>1/100 with later residual21/221. Equal-child and parallel-cut factors are proved directly and tested at complete macro level. Odd length,m0,m2,N2 and singleton local fibers are classified in the proof. M-GROW remains the accepted source-scoped obstruction to low-genus/small-support policies; it is neither refuted nor retested as a new asymptotic statement here.

S1–S4 require no literature classification or Hurwitz transitivity. H_h is defined from actual connected counts. Efficient low-genus count/decoder interfaces remain only at their prior scoped acceptances; no all-genus evaluator is silently imported. The conditional grammar depends on PORT-CONTRACT and actual local endpoint decoders. This separates mathematical structure from computational availability and preserves the scalar-count-versus-literal-sampler distinction.

|claim|status|assumptions|evidence/artifact|independent check|action|
|---|---|---|---|---|---|
|S1 interval and2N−2 pointwise cut bound|proved by author; provisional certification|N>=2,g>=2, connected identity words|proof Section2|exact DP finite histograms; no nonauthor proof yet|review exact frozen version|
|S2 tree/unicycle topology at every penultimate cut|proved by author; provisional certification|same|proof Section2|all finite macros N<=4,g<=3|review|
|S3 full weights, h-root quotient, parallel/equal-child corrections|proved by author; provisional certification|actual connected local counts/words|proof Sections3–4|independent local-count factorization, finite macros|review|
|S4 exact rejection law and expected<=2N−2 proposals|proved by author; provisional certification|exact uniform marked sampler and fresh fair bits|proof Section6|complete finite cut distributions|review conditioning|
|uniform structural FPT overhead|conditional|PORT-CONTRACT and uniform endpoint decoders|proof Section5|no production high-genus grammar claimed|retain dependencies|
|PORT-CONTRACT complexity|unresolved|none assumed true|standalone primitive Section5|not established by finite success|next coefficient obligation|
|balanced-core f(g) shapes imply FPT automatically|rejected inference|numeric port domain[N]|proof Section7|analytic operation count|retain negative finding|
|T0/T1 or complete single-primitive T2|unresolved|higher-genus computation/decoding remain|full proof/report|not claimed|no upgrade|

## Provenance, review boundary and files

Base commit b178daf320833e859dcdee0ce56eb16c6d2130b7. Owned role only. Inherited gpt-6-astra/ultra/default tier; no separate server tier attestation. No descendants, research CLI sessions, installs, configuration changes, staging or commits. Required skills and prior reviewed structural material were read. The historical heat-bath objective and older PROJECT_MAP snapshot differ from the campaign/FRONTIER state; this report follows the explicit frozen campaign T0 and does not rewrite those sources.

This author partial was completed before reading any current peer or coordinator mathematical draft. Any subsequent coordinator-requested review is explicitly nonblind, with separate versioned input and report artifacts. Same-model reviews are correlated. The parent owns synthesis and acceptance.

Owned files at freeze: input-v1.md (coordinator-authored input, unchanged), plan.md, checkpoint-early-v1.md, checkpoint-halfway-v1.md, theorem-v1.md, proof-v1.md, check_cuts_v1.py, cut-results-v1.json (coordinator-executed output), job-J2-plan.json, report-v1.md, SHA256SUMS-v1 and freeze-manifest-v1.json. No shared file was edited by this worker. Repository-wide status also shows coordinator-managed changes under research-campaigns/genus-scaling-20261028/ and other files within the untracked experiments/20261028-genus-scaling/ tree; those are not this worker's edits.
