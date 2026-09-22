# Coordinator report — connected genus-one uniform sampling

Mathematical synthesis accepted: `classification=sampler-theorem`.
The exact connected sampler, its implementation and the global consequence
have passed complete current-version nonauthor audits. Final delivery
consistency is the only pending check at this synthesis snapshot; the native
goal remains active until that check and the handoff are complete. This is a
new capped run, and no old local-chain goal was resumed.

## Main accepted mathematical result

For every N>=2 and every b>=1, the algorithm returns an ordered
length-2N transposition identity word with connected support on all [N],
exactly uniformly. The stronger internal theorem samples connected
factorizations of any specified endpoint sigma at length
N+cycles(sigma)-2+2g for g in {0,1}. Its conservative expected bit bound is
O(N^10 log^3(N+1)) in the exact binary-arithmetic/fair-bit model. Thus the
TV error is zero, and the precision parameter b is unnecessary. N=1 is
infeasible for T0; N=2 is the unique fourfold repeated transposition.
The complexity parameter is permutation degree N, not log_2 N wires.

The new constructive step is the polynomial allocation oracle. Deleting
the final transposition leaves one connected predecessor or exactly two
connected predecessors whose genera sum to at most one. The specified
endpoint cycles stay intact inside these two support components, with two
daughter cycles anchoring their orientation. Interleaving cancels the child
length factorials. Vakil's positive genus-one formula then makes every
remaining allocation mass a function of total vertex size, cycle count,
and elementary/marked symmetric coefficients. A positive DP on these
polynomially many indices computes the mass after every actual partial
assignment. Exact weighted choices and uniquely recoverable reconstruction
give the uniform word law. This supplies a word decoder missing from scalar
identity counts alone.

The canonical proof is `proof.md`; implementation is
`roles/r1-recursive/sampler.py`, with explicit work stacks. The experiment
entry point is `sample.py`. It separately labels connected and restricted
global output laws. Examples from the repository root:

    python3 -B experiments/20260907-genus-one-sampler/sample.py --n 8
    python3 -B experiments/20260907-genus-one-sampler/sample.py --n 4 --m 8 --target restricted

Python APIs use labels 0,...,N-1; the CLI reports labels 1,...,N. Omit --seed
for SystemRandom; fixed seeds are reproducible implementation diagnostics.
The mathematical theorem uses independent fair bits.

## Consequence for global component assembly

The exact global target is Unif(Omega(N,m)), allowing unrestricted support.
Adding accepted genus-one connected generation to the existing positive
component selector gives an exact sampler conditional on every nontrivial
component having genus at most one. The selector uses the exact weights
m! product_B C(|B|,ell_B)/ell_B!, chooses labeled components, and interleaves
their positions uniformly. Its exact global TV is

    1-Z_(g<=1)(N,m)/Z(N,m),

whenever the restricted count is positive. Both counts are polynomial-time
computable integers. If component samplers are approximate, allocate at most
epsilon/(2N) conditionally to each component and add epsilon/2 to the omitted
mass, via a conditional coupling and union bound. Exact components avoid
this extra error entirely.

The independent global audit has accepted the count normalization, assembly
law as a conditional theorem, and the following obstruction. At m=2N,
the restricted set necessarily uses every label and has genus exactly one
in every component. Its mass satisfies

    log(Z_(g<=1)/Z) <= -N log N+4N loglog N+O(N) -> -infinity.

Therefore genus<=1-only assembly has global TV tending to one at length 2N.
This is a limitation of that declared restriction. It does not constrain a
hybrid that includes higher-genus components and proves no sampling hardness.
Any existing eligible higher-genus or size-two primitive can still be added
to the larger hybrid; the literal requested g<=1 certificate intentionally
does not include those extra types.

The exact finite certificate table has 369 rows through N=64,m=128. At
m=2N the covered masses are 1 at N=2, 80/81 at N=3, 4375/4672 at N=4,
approximately .4749276 at N=8, .0268221 at N=16, and 3.9064e-6 at N=32.
The asymptotic conclusion follows from the proved factorial upper bound and
subgroup-return lower bound, not an extrapolation from these numbers.
Details and exact fractions are in `global_consequence.md` and
`global_mass_results.json`.

## Independent work and audit trail

All four contexts use gpt-6-astra with ultra effort. Workers did not spawn
agents. Their independent roles finished and complete reports were frozen
before the slots were reused for nonauthor review. Same-model agreement is
correlated and is not statistical independence.

| role | independent result | current audit disposition |
|---|---|---|
| r1_recursive | positive-moment final-transposition sampler, R1-T1.1 | accepted by R2 and R3; coordinator reconciled and reran |
| r2_structural | unicyclic cut sampler with reciprocal mark rejection, C1 | accepted by R1; coordinator read full audit/code and reran parser checks |
| r3_referee | blind independent signed-coefficient final-edge derivation, B1-B7 | frozen and preserved; subsequent complete R1/global audits accepted |
| coordinator | canonical integration, independent C/Z checks, exact global certificates, asymptotic restricted-method obstruction | all mathematical claims accepted; final delivery check pending |

The blind referee received only the separate brief and operational/safety
instructions in fork_turns=none. It saved blind_report.md at
2026-09-07T21:26:04.326022+00:00 before receiving any candidate. Its complete
input and report remain frozen. It independently chose the same deletion
structure as R1 but used a different DP based on the signed closed formula;
its later audit must still check R1's positive moments and actual code.

The structural route supplies a separately audited sampler using only genus-zero
endpoint generation and the elementary M97 cut theorem. It samples ordered
unicyclic incidence codes, pays the core and child-order multiplicities,
and rejects a uniform cut pair (w,j) with acceptance 1/|J(w)|. The overall
acceptance is at least 1/(2N-1). It is retained in full. Its parser passed a new exact forward-execution audit,
including all 336 cut pairs and all 240 accepted words at N=3, as well as
all 1420 labeled macros at N=5. Its acceptance is based on the complete
grammar proof and parser law, not matching decorated totals alone.

## Evidence and limitations

- R1's frozen full audit checks every one of the 131040 X4 words with exact
  probability 1/131040, as well as all X3/X2 words and all connected minimal
  identity words in the required cases. It checks 112698 forced-allocation
  queries, including arbitrary non-prefix constraints through degree10,
  against explicit subset sums with a separately computed count formula.
  An independent endpoint/support DP verifies 1745 endpoint counts through
  degree6. Coordinator reran the frozen snapshot in a fresh process; all
  exact result digests match. These tests can refute the formulas or code;
  the universal sampler theorem rests on the complete proof.
- The global count code matched 91 independent small count cells and every
  allowed word's macro law in the required cases. R3 then reproduced every
  one of the 369 certificate rows by a different DYZ total-count recurrence
  and its independently written fixed-endpoint count formula. Its global
  audit also checks the exact conditional coupling law on finite supports.
- R2's independent macro audit matches all cut incidences at N=2,3,4,
  with counts 1,336,234720. R1's new structural review verifies all 58
  numerical codes at N=5 (78 across N=2,...,5), full cut-output laws through N=3, and 4431
  partial coefficient support/denominator checks. Coordinator reran it.
- R2's fresh R1 audit checks 97232 raw allocation moments and exact forward
  production-stack laws for 5068 words at arbitrary endpoints, plus complete
  global integration laws at (3,4),(4,4),(5,4). Coordinator reran it. R3's
  distinct check compares 7754 entire moment tables, 11631 forced masses and
  3192 count formulas, then replays 1488 prescribed tapes through the actual
  repaired implementation. Its 1200-step stack fixture uses explicit stub
  counting oracles and is not a degree-600 sampler benchmark.
- Seeded draws check endpoint, length, support and integration validity;
  they are never evidence of empirical convergence or proof of uniformity.
  All experiments use Python3.12.3 and the standard library, bounded local
  subprocesses, exact integer/rational tests and recorded seeds/commands.

## Rejected arguments, repairs, and disagreements

The literal adjacent-square insertion method still has zero fibers on
((12)(23))^3. Appending doubled tree edges preserves the connected-deletion
failure. Both current candidates cover these words; neither relies on
square insertion for coverage. M97's handle-coordinate strong-lumping failure
is retained as a regression, but no current sampler makes a chain claim.

The blind referee also gives two concrete failures: an S3 transposition has
81 unconstrained length-five factorizations but only 80 connected ones; and
uniformly choosing a connected simple support graph at N=3 gives the triangle
probability 1/4 instead of its correct word-law probability 3/4. These do not
refute correctly weighted endpoint recursion or graph representations.

Coordinator found that the first recursive Python implementation could hit
the interpreter depth cap. R1 replaced it with explicit continuation tasks
and values, without changing machine settings. Both nonauthors freshly
tested the repaired implementation, including complete forward output laws
and a deep continuation fixture. No mathematical counterexample to the
final-edge decomposition was found; no mathematical repair was needed. The
arithmetic bound was conservatively relaxed from N^9 log^2 to N^10 log^3
to avoid relying on an optimized rational-reduction cost.

The global reviewer requested clearer wording for size-two one-word fibers
versus singleton vertex components, and a separate N=0 bit-cost base. Both
editorial changes appear in G1.v1.1, with the reviewed version preserved.
There is no global mathematical disagreement currently unresolved.

HANDOFF.md describes an older dense-only candidate at length 2N^3; the
September 5 phase diagram and reports are newer and contain additional
short/sparse/count/assembly results while leaving genus-one sampling open.
This chronological conflict is recorded. No protected document was silently
changed, and old agent acceptance was not used as external certification.
The local heat-bath objective in GOAL_SPEC/AGENTS is superseded by user T0
for this run; no mixing diagnostics or dense-sampler proof were resumed.

## Remaining obligations and stopping

The proof, probability, implementation and bit-complexity dependencies are
closed in their accepted versions. Only the final artifact consistency review
and handoff bookkeeping remain at this synthesis snapshot. No mathematical
lemma remains for T0 under the checked published genus-zero/one count theorem.
Arbitrary higher-genus connected generation, and hence the all-length global
sampler, are outside the proved result. No general global closure or
computational hardness claim is made.

Cap activation: 2026-09-07T21:07:10.321763Z. Stop new construction at
2026-09-08T00:37:10.321763Z; hard deadline 01:07:10.321763Z. Current native
session: 01a07db2-4703-7312-ae54-75fcdc0bdc13. No process/service/tmux restart
or cap alteration was made. The objective may finish early under the user contract because the sampler
theorem and its global consequence are actually achieved. The native goal
will be completed only after final delivery review and the saved handoff.
Exact file changes are listed in changed_files.txt; operational inputs and
externally maintained cap/log files are excluded from research attribution.
