# Coordinator Report: Bridge-Length Sampling Complexity

Status: final synthesis, 2026-09-05 UTC. All three research reports are final;
the strongest new theorem received a fresh nonauthor audit, and the short
exact theorem received a reciprocal fresh audit. Both audits accepted.

```text
classification=quantified-phase-diagram
```

The run proves multiple polynomial sampling regimes and leaves an explicit
uncovered length/accuracy band. It also removes all scalar counting and
component-assembly obligations from the intermediate problem. It does not
establish an all-length polynomial sampler or a computational hardness
result. No local Hurwitz or block heat-bath mixing work was resumed.

## Strongest audited new theorem

For every N≥5, every feasible endpoint g, and every input length m, set

```
q=floor(m/[2N(N−1)]).
```

If `q≥4ceil(log2 N)`, the positive retained-rank algorithm always returns
exactly m transpositions with displayed product g, and its output law Q
satisfies

```
d_TV(Q,U_(N,m;g)) ≤ min(1,3N² exp(−q/144)).              (A)
```

It takes polynomial expected Turing time in N,m, conservatively
`O(N⁴m³)` exact arithmetic operations on polynomial-bit operands. Thus for
every `0<epsilon<1`, every feasible length satisfying

```
m ≥ D_eps(N):=2N(N−1) ceil(144 ln(3N²/epsilon))         (B)
```

has an endpoint-exact epsilon-close sampler in expected time polynomial in
N,m,log(1/epsilon). Ranks at most four use a fixed finite-state exact DP.
This replaces the hard-coded m=2N³ schedule by a length/accuracy theorem.
At fixed N,m, additional runtime alone is not proved to lower this
algorithm's error below (A). Its exact random integer draws explain the
expected-time qualification.

The new proof step is short. On every discarded old-long branch, the old
completion is already pointwise smoothed at length at least L/2. Summing
its exact star endpoint weights through the token projection before
conditioning gives

```
Pr_bridge(discarded) ≤2r(1+Delta) Pr_binomial(old count<child floor)
                    ≤3r exp(−q/144).
```

The historical estimate paid r! at this step. The old-side normalization
cancels all but r. Rational floors
`c_r=1+sum_(j=6)^r 1/[j ceil(sqrt j)]`,
`B_r=ceil(qr(r−1)c_r)`, `B4=0`, retain each recursive child. Their ceiling
slack is at least `q sqrt(r)/4`, pointwise error is at most `exp(−qr/4)`,
and the uniform rank telescope proves (A).

Evidence: [R2 Theorem D and Lemma S](roles/r2-dense-threshold/report.md),
[fresh nonauthor dense audit](roles/r1-short-exact/fresh_dense_audit.md).
The coordinator independently checked the primary spectral/star sources,
read every new inequality, and reran the decisive exact harness.

## Other audited positive results

The positive defect-type sampler is exact for every feasible endpoint in
expected bit time

```
exp(O(sqrt(min(m,N)))) poly(N,m).
```

For each fixed A it is polynomial on `m≤A(log N)²`; the polynomial degree
may depend on A. It retains only defect partitions in the exact endpoint
cone and lifts by individual labeled transpositions. Exactness is proved
per word, not inferred from cycle-type marginals. The slower first-appearance
sampler also proves FPT sampling; its correct embedding weight is
`(N)_k/2^b`, where b counts simultaneous introductions of two new labels.
A capped-randomness version gives bounded-time approximate sampling with
exact endpoint and polynomial logarithmic precision overhead. See
[R1](roles/r1-short-exact/report.md) and its
[fresh nonauthor audit](roles/r2-dense-threshold/fresh_short_audit.md).

Let Q0 be uniform on the subset whose every component has zero surplus.
It has a polynomial exact conditional sampler using DPS and positive
component assembly. Its global TV error is exactly `1−Z0/Z`, computable
as a rational number in polynomial time. A new incidence bound proves

```
d_TV(Q0,U_(N,m)) ≤ min(1,m⁴/[48(N−m+1)²]),
                    even 0≤m≤N.                       (C)
```

This gives the further sufficient regime
`m⁴≤48epsilon(N−m+1)²`, reaching order
`epsilon^(1/4)sqrt(N)` for a sufficiently small absolute constant.
The coordinator proposed the proof; R3 supplied a fresh independent
[matching-incidence audit](roles/r3-intermediate-hybrid/sparse_bound_audit.md).
The exact mass test often improves the conservative closed bound.

## Complete sparse-to-dense phase diagram

Here `b=ceil(log2(1/epsilon))`, q and D_eps are as above, and
`R(N,m)=m⁴/[48(N−m+1)²]` on even 2≤m≤N. All runtime claims name the
permutation degree N and output word length m; they do not imply
polynomial time in log2 N wires.


| regime | sampler | exact/approximate | runtime | TV error | status | missing primitive |
|---|---|---|---|---|---|---|
| m=0 | Empty word | exact | O(1) output | 0 | proved | none |
| Odd m | Identity fiber empty | no sampler requested | parity check | n/a | proved | none |
| m=2,N≥2 | Uniform edge repeated twice | exact | poly(log N) expected bit time | 0 | proved | none |
| N=2, even m | Unique edge repeated m times | exact | O(m) output | 0 | proved | none |
| N=1 | Only m=0 feasible | exact/empty | constant | 0 on singleton | proved | none |
| All feasible lengths, parameterized by min{m,N} | Positive defect-type DP and labeled lift | exact | exp(O(sqrt(min{m,N}))) poly(N,m) | 0 | proved; fresh audit accepted | remove partition-state factor for general inputs |
| m≤A(log N)² for fixed A; also min{m,N}=O(log²(N+m)) | Same defect-type DP | exact | poly(N,m), degree depends on fixed regime constant | 0 | proved; fresh audit accepted | none in stated regime |
| Fixed N, every even m | Full type DP / finite-state bridge DP | exact | poly(m), constant depends on N | 0 | proved | no uniform poly(N,m) bound from fixed-N enumeration |
| even 2≤m≤N with R(N,m)≤epsilon | Minimal-component assembly and DPS | approximate global; exact within declared subset | O(N²m²) polynomial-bit integer arithmetic plus polynomial DPS reconstruction | ≤R(N,m) | proved; independently audited incidence bound | none in stated accuracy regime |
| Any (N,m) with Z0>0 and 1−Z0/Z≤epsilon | Same minimal-component sampler, exact mass certificate | approximate | poly(N,m); exact certificate arithmetic | exactly 1−Z0/Z | proved | none for inputs passing certificate |
| N≥5, feasible even m, q≥4ceil(log2 N) | Density-parameterized retained-rank recursion | approximate | O(N⁴m³) exact arithmetic on polynomial-bit operands | ≤min(1,3N² exp(−q/144)) | proved; fresh audit accepted | smaller requested error at fixed (N,m) |
| N≥5, feasible even m≥D_eps(N) | Same dense sampler | epsilon-close | poly(N,m,b) expected bit time | ≤epsilon | proved; fresh audit accepted | none in stated regime |
| Restricted hybrid assembly with certified omitted macro mass≤epsilon/2 | Exact macro counts, exact short/minimal connected words, dense connected rejection where certified | epsilon-close | poly(N,m,b) with fixed explicit exact-state cap | ≤omitted mass+epsilon/2 | proved reduction and certificate | connected generation for excluded components |
| Remaining feasible length/accuracy pairs | No audited general polynomial sampler supplied here | unresolved | no established bound | no established guarantee | uncovered | connected positive-surplus sampling; exact counting already solved |

Here Z counts all identity bridges, Z0 counts those whose every nontrivial
component is minimal, and both are exactly computable in polynomial time.
At fixed epsilon, the explicit sparse theorem reaches order sqrt(N); the
dense theorem starts at order N² log N. Exact short sampling can dominate
the sparse approximation when epsilon is very small. These are sufficient
regimes with different precision dependence, not a single threshold.


### Conditional internal primitives and limitations


| regime | sampler | exact/approximate | runtime | TV error | status | missing primitive |
|---|---|---|---|---|---|---|
| Connected v-label identity words, length 2v−2 (g=0) | DPS rooted Cayley/permutation product, forget uniform root | exact | polynomial bit time; published RAM algorithm linear | 0 | proved; source and root quotient checked | none for this conditional target |
| Arbitrary endpoint g at minimal length N−cycles(g) | Positive cycle-splitting recurrence and interleaving | exact | polynomial in N | 0 | proved; R1 | none; public identity gives m=0 only |
| Prescribed endpoint star words | Féray coefficient and backward sampler | exact | polynomial in degree and length | 0 | proved imported primitive | does not itself sample general transposition bridges |
| Connected components with v^(2v)≤(Nm+2)^c for a fixed constant c | DP on (prefix permutation, exposed support partition) | exact | O(ell v³ v!Bell(v)) polynomial-bit work; polynomial under the cap | 0 | proved | no unrestricted R1-to-connected substitution |
| High-surplus connected words with C(v,ell)/Z(v,ell)≥1/2 and dense error δ | Reject disconnected dense outputs | approximate connected | expected polynomial for δ≤1/4 | ≤4δ | proved conditional transfer | sufficient dense length/accuracy condition |
| Connected words of length 2v (g=1), v unbounded | Counts solved by positive DYZ recurrence | sampling unresolved | count poly(v); no proved general sampling bound here | unresolved | uncovered primitive | exact or tunable uniform connected sampler |
| Positive-surplus intermediate components in general | Exact positive component/surplus reduction | unresolved generation | all weights poly(N,m) | no error claim without primitive | strict reduction | connected sampler with poly(v,ell,b) runtime |
| Full defect-type inventory, m≤N and m=omega(log²N) | Literal type enumeration | named-method obstruction | ≥exp(Omega(sqrt(m))) states | n/a | proved | compression or another method |
| Minimal-component-only output at m=Theta(N^alpha), fixed 2/3<alpha≤1 | Always condition total surplus to zero | named-method obstruction | sampler is polynomial but target approximation fails | TV→1 (or subset empty) | proved; independent R3 audit | allow positive surplus; no hardness consequence |


## Explicit uncovered set and final classification

Fix an implementation work cap, or a fixed constant A for the short
regime. The uncovered set consists of feasible length/accuracy inputs
outside the short/fixed-degree polynomial regime, failing both the sparse
bound and the exact minimal/hybrid mass certificates, and below the dense
sufficient threshold (B). For fixed accuracy and growing degree, the
closed guarantees leave general lengths between order sqrt(N) and order
N²log N unresolved, with any passing per-instance certificates removed.
General m=Theta(N) is a concrete intermediate family for which this run
provides no sampler covering all inputs. The interval is a statement about
available guarantees, not an impossibility interval or a universal threshold.

The precision axis matters. Short exact sampling has zero distributional error.
The sparse theorem may become weaker than the short exact regime for tiny
epsilon. Dense admissible length grows with log(1/epsilon); holding length
fixed leaves the theorem's stated error bound. No matching lower bound on
the actual output-law error is claimed. Exact enumeration can also
be polynomial in the enlarged input variables N,m,b when
`min(m,N)=O(log²(N+m+b))`.

The classification is quantified-phase-diagram because the proved short,
sparse, and dense regimes have explicit runtimes and errors, and the
remaining band is stated. The connected reduction is an additional result,
not a second outcome classification.

## Exact intermediate reduction and first open lemma

Let C(v,ell) count connected identity words on a fixed v-set, with
`C(1,0)=1` for an isolate and no other singleton lengths. For v≥2,
`ell=2(v−1)+2g`, g≥0, is precisely its feasible regime. For labeled
components `(B,ell_B)`, their exact global weight is

```
W(alpha)=m! product_B C(|B|,ell_B)/ell_B!.
```

All label choices, equal-component multiplicities, component surpluses,
internal words, and color interleavings are retained. Distinguishing the
least remaining label gives the positive polynomial assembly recurrence

```
Z(n,k)=sum_(v,ell) binom(n−1,v−1) binom(k,ell)
                    C(v,ell) Z(n−v,k−ell),
Z(0,0)=1.
```

The DYZ formula supplies every C through a positive integer recurrence:

```
d²(d−1)C(d,k)
 =2 sum_(a+b=d) binom(d,a)
      sum_(k1+k2+r=k, even r≥2)
       multinomial(k;k1,k2,r) a^(r+1)b² C(a,k1)C(b,k2).
```

Two binomial convolutions per degree split compute the full table in
`O(N²(m+1)²)` integer operations on `O((m+1)log(N+1))`-bit numbers.
Thus exact connected scalar counts, global counts, component sets,
lengths/surpluses, and interleavings are solved in polynomial time.
Sampling formal terms of this recurrence does not supply a word decoder.

The precise remaining primitive is:

> **CONNECTED-IDENTITY-WORD-SAMPLE.** Given v≥3, g≥1 and integer accuracy
> b≥1, put ell=2v−2+2g. Output a length-ell word with exactly connected
> support [v], exact identity endpoint, and TV error at most 2^(−b) from
> the uniform connected law, in expected time polynomial in v,ell,b,
> for the inputs outside the proved component predicates.

The first concrete unsolved subfamily is g=1, ell=2v, with v unbounded.
Its scalar counts are already polynomial-time computable. Solving that
subfamily would be progress but would not by itself solve every genus.
Solving the full displayed primitive would finish the global sampler by
the positive assembly recurrence. The first unproved count-to-sample step
is a constructive lifting with correct word multiplicities, or an
endpoint-and-connectivity-marked completion oracle; C(v,ell) alone is
not that oracle.

The hybrid is precise even without this primitive. Exact support-marked
DP is allowed under a fixed polynomial cap on `v!Bell(v)≤v^(2v)`;
minimal components use DPS. An unrestricted exact short sampler can be
conditioned only when its exact connected acceptance probability is
certified large. Dense component proposals have the same requirement:
if `C(v,ell)/Z(v,ell)≥1/2` and their global TV is δ≤1/4, connected
rejection costs at most four calls in expectation and has connected TV≤4δ.
Allocate error epsilon/(2N) to each of at most N components. Restricting
the exact assembly table to these allowed components yields

```
TV(Q_hybrid,U)≤1−Z_allowed/Z+epsilon/2.
```

The dense eligibility test can use only integers: with
`b=ceil(log2(1/epsilon))` and v≥5 require

```
q_v=floor(ell/[2v(v−1)])
 ≥max(4ceil(log2 v),144[b+ceil(log2(24Nv²))]),
2C(v,ell)≥Z(v,ell).
```

Since exp(−x)≤2^(−x) for x≥0, this guarantees proposal error at most
epsilon/(8N). The exact work cap can use R1's explicit state/arithmetic
bound and a fixed polynomial budget. No real-valued transcendental
comparison is needed to select allowed components. Both restricted and
unrestricted counts are exact, so omitted mass≤epsilon/2 is a
polynomial-time checkable sufficient condition. All these claims are proved in
[R3 equations (1)–(14)](roles/r3-intermediate-hybrid/report.md). No general
overlap closing the uncovered band was proved.

## Negative results and the distinction from hardness

The first-appearance weight `(N)_k` without the introduction symmetry
factor is refuted already at m=2. The full midpoint type inventory has
at least `exp(Omega(sqrt(m)))` states for even m≤N and is superpolynomial
when m=omega(log²N). Both are limitations of named implementations.

There is also a stronger obstruction to using only minimal components.
Their normalized counts equal a weighted forest sum, hence
`Z0(N,2k)/(2k)!≤binom(binom(N,2),k)`. For any 2≤r≤N and even m>0,
midpoint Cauchy–Schwarz on a parity class gives
`Z(N,m)≥2binom(r,2)^m/r!`. Choosing r=floor(m/log m) shows

```
log(Z0/Z)≤m[log N−(3/2)log m+2loglog m+O(1)].
```

Therefore minimal-only TV tends to one at
`m=Theta(N^alpha)` for every fixed `2/3<alpha≤1`, when the subset is
nonempty; above 2N−2 it is empty. The finite upper bounds were vacuous
on the recorded exploratory cases and are retained as negative findings.
The asymptotic conclusion comes from the proof, not numerical trends.
It excludes this sampler family, not positive-surplus sampling in general.

No computational hardness reduction was produced. Neither an uncovered
band, a failed recurrence decoder, nor a large natural state table implies
that the underlying sampling problem is hard. A fixed-positive-genus
coherent-mobile construction is plausible, with its positive sampling step
still unproved.

## Conventions, exceptional cases, and source reconciliation

Permutations are maps with `(alpha beta)(x)=alpha(beta(x))`; the rightmost
displayed factor acts first. The public target is uniform on all identity
bridges; internal endpoints are always declared. All algorithms preserve
requested endpoint and length on every output.

For N≥2, feasibility is parity plus m≥N−cycles(g). At N=1 only m=0 is
feasible, because there is no pair available for padding. This is an
explicit domain qualification to the unqualified fiber formula appearing
in the source documents. m=0 is the empty word; odd identity lengths are
empty; m=2 repeats a uniform transposition; N=2 has a unique feasible word.
Minimal endpoint length is handled by a separate positive cycle-splitting
sampler. Pair padding establishes feasibility or a valid fallback; it is
not used to infer uniformity.


- Féray, *Partial Jucys–Murphy elements and star factorizations*,
  [Proposition 1.1, Theorem 1.2, Lemma 3.1](https://arxiv.org/html/0904.4854v2).
  Theorem 1.2 gives the transitive star coefficient at a fixed endpoint
  cycle type. Its excess index is factor length minus n+number-of-cycles−2,
  not the genus. Summing over exactly used lower fixed labels gives the
  positive general star count. Permutation maps and composition agree;
  backward self-reduction appends tau and updates q to q tau.
- Caputo–Liggett–Richthammer,
  [*Proof of Aldous’ spectral gap conjecture*, Theorem 1.1](https://arxiv.org/pdf/0906.1238).
  With unit graph-edge rates, the interchange gap equals the one-particle
  gap. Dividing by edge count converts continuous time to the normalized
  nonlazy step used for endpoint smoothing. Sign twisting pairs the
  spectrum, so after excluding constant/sign vectors the absolute radii
  are 1−2/(r−2) for the old S_(r−1) walk and 1−1/(r−1) for the star.
  This is used only for the endpoint walks, not as a word-chain mixing
  theorem.
- Duchi–Poulalhon–Schaeffer,
  [*Uniform random sampling of simple branched coverings of the sphere by itself*](https://www.irif.fr/~poulalho/Articles/DuPoSc13.pdf),
  Proposition 1, Proposition 3, Theorems 4–5 and Corollary 2. The connected
  minimal sampler follows a bijection from rooted Hurwitz trees, whose
  independent coordinates are a Cayley tree and a permutation of 2v−2
  labels; forgetting the white root is exactly v-to-one. Their displayed
  product is reversed; inversion or reversal preserves the identity fiber
  and connected support. Count: C_0(v)=(2v−2)!v^(v−3), including v=2.
- Dubrovin–Yang–Zagier,
  [*Classical Hurwitz numbers and related combinatorics*, Proposition 1, equation (13)](https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf).
  Section 1.2, equations (19)–(20), identifies the weighted cover count
  with labeled transposition words divided by degree factorial and separates
  connected components exponentially. Thus C(d,k)=d!k!h_(g,d),
  k=2g+2d−2, h_(0,1)=1 and h_(g>0,1)=0. This supplies a positive count
  recurrence; it does not supply a bijection that samples words.

No Hurwitz transitivity dependency is used. Literature searches were
restricted to these named technical obligations; no novelty claim is made.


### Focused checks of adjacent literature


Féray–Louf–Thévenin, [Corollary 1](https://doi.org/10.1007/s00440-022-01170-9),
gives asymptotically uniform fixed-genus factorizations of a long cycle.
The endpoint and length n−1+2g differ from the present connected identity
primitive at 2n−2+2g, and the statement is not a tunable accuracy guarantee.

DPS, [*Bijections for simple and double Hurwitz numbers*, Theorems 1 and 4](https://arxiv.org/pdf/1410.6521),
extends the correspondence to coherent higher-genus Hurwitz mobiles.
The inspected theorem does not provide the required polynomial sampler for
those coherent objects. This is a possible research route, not a discharged
sampling dependency.

The focused search also inspected Chapuy–Louf–Walsh,
[*Random Partitions Under the Plancherel–Hurwitz Measure, High Genus Hurwitz Numbers and Maps*](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.AofA.2022.6),
Theorem 5, because it counts exactly the identity words at linear length.
No claim here depends on its asymptotics; the elementary bound above is
sufficient for the minimal-only obstruction. These source checks do not
establish novelty or prove that no other sampler exists.

## Audit record and reproducibility

All three roles wrote plan.md, substantive checkpoint.md, and final
report.md in their own directories. Every checkpoint arrived inside the
75-minute requirement. Reports were frozen before cross-audit. R1 audited
R2, and R2 audited R1; neither edited the author's files. R3 independently
audited the coordinator's sparse proof and forest argument. The coordinator
resolved the conditioning and connected-target distinctions, checked primary
source formulas, audited R3's positive recurrences, and reran exact checks.

- Short fresh audit: 90,743 cone-layer checks, 3,547 endpoint counts,
  all required per-word probabilities and canonical embeddings, minimal
  counts, and 336 finite random-tape laws.
- Dense fresh audit: 25,228 rational floor cases; 720 feasible endpoints
  across rank-six lengths 380 and 381; 173,520 rank-five joint branches
  with exact support, normalization, likelihood ratios and TV checks.
- Component work: all required cases, 114 exact mass-certificate rows,
  exact connected support-DP probabilities, and all 11,520 rooted DPS
  inputs at v=4, with the correct four-to-one quotient.
- Coordinator: independently matched original rational DYZ with connected
  counts extracted from labeled permutation DP in 78 cells N≤6,m≤12;
  reran the full short, dense, and component deterministic harnesses. Required totals
  were 27,120,3936; minimal-only TVs were exactly 1/9,1/20,11/41.

These finite computations can falsify claims and validate conventions;
universal conclusions use the complete proofs and named external inputs.
The final [cross-document consistency audit](roles/r3-intermediate-hybrid/synthesis_audit.md)
accepted the phase diagram, ledger, and report at 15:56 UTC, after resolving
all three observations about precision wording, final status, and integer
hybrid eligibility.
There are no failed decisive checks or unresolved substantive audit objections.
The dense deliverable is an audited constructive algorithm and pseudocode
with exact finite harnesses; it is not a new production implementation of
the full large-input recursive sampler. Short and component samplers are
implemented for research reproduction.

Commands, Python/dependency versions, timestamps, commit, final status,
artifact hashes and the complete changed-file inventory are in
[run_manifest.md](run_manifest.md). The claim-by-claim dispositions are in
[claim_ledger.md](claim_ledger.md), and the standalone diagram is
[phase_diagram.md](phase_diagram.md).

## Proposed durable patches and next human review

No protected project file was edited. Proposed follow-up changes, after
human review, are:

1. Add the exact defect-type sampler and its explicit growing-length regime
   to HANDOFF and the direct-sampling manuscript section.
2. Replace the dense section's hard-coded schedule by Theorem D, its rational
   floors and the O(r) bridge-conditioning lemma, retaining the stated
   expected time and fixed-length accuracy qualification.
3. Add the polynomial DYZ/component assembly theorem, the sparse approximation
   and its method obstruction, and the standalone connected-sampling lemma.
4. Keep the local-chain objective separate and avoid any hardness claim.

The single most valuable human-review target is **R2 Lemma S and its use
in the retained-rank telescope**, alongside the fresh dense audit and the
Féray star-coefficient normalization. This is the step that broadens the
dense schedule to the requested length/accuracy theorem.

The next constructive research task is connected genus-one identity sampling
at length 2v, or a correctly weighted decoder for the positive connected
recurrence. Resume from the final reports and claim ledger; no unfinished
worker, local-chain run, or historical resolution ledger needs to be resumed.
