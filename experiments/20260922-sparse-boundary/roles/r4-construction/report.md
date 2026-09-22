# R4 construction and algorithm audit report

Frozen candidate: H2-QC.v1. Verdict: **keep the exact quotient decoder as
an author-proved, finitely validated primitive; reject H2 and its genus0/1
union as a T0 mechanism.** The optional decoder has not received a
nonauthor correctness audit and is not needed by either main theorem.
The unchanged H0/H1 algorithm dependency audit is accepted separately.

All words use distinguished labels and positions, rightmost-first
composition. No Markov kernel, local mixing, or wire-efficient complexity
claim occurs here. Time and storage variables are N and m.

## Results and dispositions

| Claim | Status | Scope / evidence |
|---|---|---|
| QC.v1 support-history quotient is sufficient for exact literal decoding | proved by author; nonauthor audit pending | proof-v1.md; <=3^(v-1) states; positive conditional edge weights |
| H2-QC.v1 exactly samples every-genus components v<=L, L=max{v:3^v<=P^4} | proved by author; nonauthor audit pending | fixed top-level L; global law Unif(D); expected O(P24) bit time/O(P12) storage |
| Required finite laws and transition/count checks | exact finite facts | results.json; all tests pass,2.26s |
| H2 achieves benchmark T0 | refuted | R2-O2.v1 plus h2-obstruction-audit.md: TV>=1-2^(-1-jm/2), N2^(8j),m2^(6j),j>=64 |
| Adding all g0/1 components rescues this cutoff | refuted | same generalized-cutoff numerator bound |
| Old H0/H1 exact law and O(P20)/O(P10) depend on old m^3<=N² regime | refuted as an algorithmic limitation | algorithm-audit.md: exact law and resources hold for every even length |
| Root SB-T1.v1 algorithm integration | accepted | exact root proof hash 3a54f12e4d172cfdfc5ef6f8e7b84c067e86eba8d10a2f387496ff7bd435d611; ALG-INT.v2 |
| Full existence T0 | unresolved | neither the restricted decoder nor its obstruction addresses all algorithms |

## Concrete sampler modification

The old small-support decoder stores a literal permutation and exposed
support partition, giving v!Bell(v) states. QC stores their complete orbit
under simultaneous vertex relabeling: a multiset of integer partitions,
one partition listing the permutation-cycle lengths inside each support
block. This retains support history. At most3^(v-1) marked compositions
encode these states, allowing a larger Theta(logP) support cutoff with a
fixed polynomial budget.

The quotient recurrence counts each successor with its exact number of
literal transpositions. During generation, the actual labeled prefix and
support partition remain present; each actual edge receives the quotient
count of its own child as conditional weight. Thus every connected word
has probability1/C(v,ell). Counts are accompanied by positive decoding,
not assumed to imply it. Least-label assembly then gives1/Z_D globally
and exact omitted mass1-Z_D/Z. H0/H1 definitions were never changed.

The new conditional sampler includes arbitrary-genus components beyond
old K. Nevertheless R2's generalized-cutoff obstruction applies to L too.
The failure is omitted global mass, not a decoder bias or resource defect.
The construction is therefore a primitive improvement without a new
asymptotic T0 regime.

## Exact validation

Command, from repository root:

    timeout 90s python3 -B experiments/20260922-sparse-boundary/roles/r4-construction/validate.py --output experiments/20260922-sparse-boundary/roles/r4-construction/results.json

One root-allocated expensive slot was used and explicitly released after
2.25895seconds; no computation remains running. Python3.12.3, standard
library only, commit20e86f665f69053031fe7eec0c3388458affb1fc. Imported
executable bytes were hashed before execution. No old file was modified.
The new sampler source hash used in this run is
7cfd9bcaed9cc08d57d2e50564b829d8a54cbc40e89aa5fe445a2a5c2149ee7c.

- Every quotient state through v7: explicit representative edge counts
  agree with the indexed-cycle multiplicity formula. There are220 tested
  quotient states and3576 actual edge transitions.
-189 connected count cells v1..9,ell0..20 agree with the independent,
  hash-frozen positive DYZ count implementation.
- Actual forward sampler choices are exhaustively replayed at S3m4,
  S4m4,S4m6,S3m8. The output laws have respectively27,120,3936,2187
  words, each exactly reciprocal-total probability. These complete laws
  imply equality for every diagnostic pushforward on these finite sets,
  including support, edge counts, prefix types and adjacent repeats.
- Endpoint-only support-history regression: the same identity endpoint
  has terminal connected completion count1 or0 according to its support.
- Arbitrary length v2,ell1400 runs with explicit stacks and1401 memo entries.
- Fixed cutoff regression: top(N,m)=(100,38) has L17; residual(17,38)
  would recompute L14. The actual prepared branch table retains the
  size17,length38 branch using original L17. This is a branch-table check,
  not exhaustive execution of that large connected branch.
- m0,m2,N0/1 empty words,N2 positive even lengths pass; odd/empty positive
  fibers reject. Seeds1729,2718,31415 each add20 validity draws per small
  law. The seeds do not establish the exact-law result.

## Algorithm dependency audit for the positive extension

ALG.v1 rereads unchanged sampler-v4.py, proof-v3.md and the imported g0/1
source/proof. It verifies that all-even-length polynomial bounds retain
the (m+1) state factor, original K, exact support-history boundary, positive
count/assembly tables, and fixed-size g0/1 internal lengths. No decoder or
resource statement is restricted to m³<=N². Hence the smaller new
m<=N^(2/3)lnN/4 theorem can use them unchanged. ALG-INT.v2 confirms the
exact canonical root Section6 and corresponding Section3 imports. R5 caught an ambiguity in the earlier dispatcher wording; the final text explicitly routes every H0 genus0/1 component through g01 even when small, and this role freshly checked that exact predicate against source.

This review inherits the recorded primary-source normalization checks for
DYZ and Vakil and does not claim a new source-theorem verification. H1
requires DYZ counting but not the nontrivial g0/1 primitive. The analytic
length/error theorem has separate reviewers; this algorithm audit alone
does not certify its tail inequality.

## Remaining primitive and retained findings

reduction.md isolates connected inputs v>L,g>=2,ell<=m. A single literal
connected sampler with exact identity/length, TV2^-b and expected
poly(N,m,b) cost on those inputs would suffice for global negligible error
by exact macro assembly, a conditional coupling union bound, and
b=ceil(log2(N+2))². The scalar connected counts are already available;
this primitive remains unproved. It is sufficient, not a necessity or a
hardness statement.

Preserved negatives: the new logarithmic cutoff fails at T0; old endpoint
cycle type alone loses support history; top cutoff must never be recomputed;
large integer CLI output needs the old hex repair; arbitrary genus is not
silently dropped. Existing m0,m2,N2 and near-minimal exceptions remain.
HANDOFF/GOAL_SPEC still concern local mixing; the current frozen run
explicitly supersedes that objective, and neither file was edited.

All attributable files are under this role directory and listed in
changed_files.txt. No worker delegation, goal creation, install, service,
configuration change, commit or push occurred. The default python command
was unavailable during setup, so all successful commands used python3 -B.
Model/effort requested gpt-6-astra/ultra; no separate backend setting
introspection is exposed. Shared-clock deadlines were read and never reset.
