# First planted-subsequence experiment

Date: 2026-11-10. **Verdict: keep the exact formulation and analysis; no
supported cryptographic hardness regime yet.** There is a concrete conditional
application: recursive computational sampling from exact short bridges, under
an explicitly stronger nonuniform planting assumption at every internal
length. Small middle-length plants
usually expose most of their signal through repeated gates. In a separate
fixed-length large-N regime, the laws converge statistically. Neither result
rules out a different schedule with growing plant and complement lengths.

This is one bounded foreground investigation authorized by the user's request
to try the planted idea. It does not resume an archived campaign. Proofs and
checks are by one agent, with a separately written audit implementation;
there is no independent proof review or manuscript promotion.

## What was actually tested

The model is exactly Q4 with every k-subset allowed: D0 is uniform over all
ordered labeled transposition identity words of length m in S_N. D1 chooses
a fresh uniform hidden k-subset I, then samples D0 conditioned on its ordered
subsequence having product identity. The adversary sees one full word and
N,m,k, without I. There is no noise, reused key, oracle or connected-support
conditioning. Products act rightmost first; complexity is in explicit N,m.
There is no MCMC kernel, burn-in or convergence estimate.

The study exhausts 34 (N,m,k) cases at N=3,4,5,6,8 and m=4,6,8,10,12 as
listed in [plan.md](plan.md) and [results.json](results.json). It also checks
N2, empty/short lengths, odd m/k and trivial k0/km controls. Exact conjugation
orbit weights account for every literal word, including disconnected words.

## Concrete finite attack

Count equal-gate pairs: R(W)=sum_t binom(multiplicity(t),2). This uses a
dictionary over the visible gates, without searching hidden index sets. The
following thresholds are optimized from exact finite laws; these are not
claims about a threshold that works at arbitrary growing parameters.

| N,m,k | Test accepts planted when | Null acceptance | Planted acceptance | Advantage | Best possible advantage (TV) |
| --- | --- | ---: | ---: | ---: | ---: |
| 4,8,4 | R>6 | 21.9521% | 41.7619% | 19.8098% | 24.2832% |
| 5,8,4 | R>3 | 35.7223% | 61.7044% | 25.9821% | 28.7316% |
| 6,8,4 | R>3 | 27.1716% | 51.2627% | 24.0911% | 25.6009% |
| 8,8,4 | R>2 | 60.9906% | 81.2225% | 20.2319% | 21.6620% |

For example, at N6,m8,k4 the cheap test recovers about 94.1% of the available
TV signal. Equal-prior classification accuracy is 62.0455%, compared with the
optimal 62.8005%. Advantage here means the difference of acceptance
probabilities, not accuracy above 50%.

Gate multiplicities, support and weighted support components, middle-prefix
cycle types/fixed points/standard character, and window cycle histograms were
also checked. Their complete exact marginal histograms are stored in
[feature-histograms.json.gz](feature-histograms.json.gz); results.json stores
their TV values. A joint feature histogram often captures nearly all TV, but
its finite lookup rule is **not** claimed to be a uniform efficient algorithm
at growing parameters. Both full endpoints are always identity, and every
single gate coordinate is exactly uniform by relabeling symmetry, so those
controls cannot distinguish the worlds.

Retained minority finding: at N3,m12,k6 the full TV is only 0.016486, and the
repeat-pair marginal TV is 0.002845 (best threshold: 0.001470). Repetition is
not universally the best statistic. This small-N case also supplies no
cryptographic hardness evidence: exact group-state dynamic programming is
efficient when N is fixed.

## Useful analytic outputs

The accompanying [proof.md](proof.md) gives elementary proofs, with all
efficiency premises explicit:

1. **Exact planted generation.** Draw independent uniform identity words of
   lengths k and m-k, then undo selected-left stable sorting using inverse
   Hurwitz moves for a uniform hidden I. This samples exactly D1. It avoids
   rejection on a rare event, conditional on having the two bridge samplers.
   The finite implementation uses factorial-size group tables, so it is not
   a new all-length polynomial sampler.
2. **Exact likelihood.** If X_k counts length-k identity subsequences and
   Z_r counts length-r identity words, then
   D1(W)/D0(W)=X_k(W)/E_D0 X_k, with
   E_D0 X_k=binom(m,k) Z_k Z_(m-k)/Z_m. Planting weights words by their number
   of witnesses. This supplies the exact optimum and the correct null model.
3. **Additional easy boundary.** k=2 has the repeat-pair score. For k=m-2,
   conjugate each gate by its preceding prefix and count equal transformed
   gates. This also computes the entire likelihood statistic efficiently.
   A complement involution makes the full TV equal at k and m-k. General
   meet-in-the-middle counting takes O(2^ceil(m/2) poly(N,m)), and was checked
   against complete subset enumeration.

These are useful reductions and tests, not evidence that the central
distinguishing problem is hard. Constant k or constant m-k are poor targets
for a computational gap: their witness scores have polynomial enumeration
cost, with the decision threshold still requiring normalization or calibration.

## Statistical closeness in the fixed-length sparse limit

Every length-m identity word uses at most m labels. Enumerating N=m therefore
captures every support pattern. Counts for any N are exactly a sum of
binom(N,v) times counts on a fixed v-label support. This completeness argument
allows the N8,m8 enumeration to be evaluated at much larger N without drawing
any samples or fitting a curve.

| N, with m=8,k=4 fixed | Exact TV, shown in decimal |
| --- | ---: |
| 8 | 0.21662009 |
| 20 | 0.14297585 |
| 100 | 0.04683347 |
| 1,000 | 0.00526444 |
| 1,000,000 | 0.000005333264 |

The proof separately establishes TV=O_(m,k)(1/N) for fixed even m,k. The
leading words consist of m/2 disjoint transpositions, each repeated twice;
every such word has exactly binom(m/2,k/2) witnesses. Choosing the appropriate
number of complete edge pairs finds a witness easily. Thus the observed
agreement is statistical and comes with abundant, easy relations. Constants
are not uniform in growing m,k; inverse-polynomial error is not negligible
when N itself is the security parameter.

## Does the assumption imply anything useful?

**Yes, conditionally: it can support a recursive identity-word sampler.**
Use an exact sampler up to a cutoff B. For a longer even length ell, recursively
sample two nearly equal even-length identity words and combine them by exact
inverse-Hurwitz planting. Every output computes identity, and the total
combination work is O(m^2) local conjugations. An exact short-bridge primitive
is still a separate efficiency premise.

If the planting assumption holds against **nonuniform polynomial-size
circuits at every internal length**, a hybrid proof shows that the resulting
word is computationally indistinguishable from a global uniform identity word.
This would give a useful computational alternative to an unavailable exact
all-length sampler. It does not require rarity of null witnesses.

This is a **stronger assumption** than the original single-sample PPT
template. The hybrid may need an exact sibling bridge that a uniform
reduction cannot efficiently generate; nonuniform advice can hardwire it.
[Proof section 6](proof.md#6-a-conditional-recursive-identity-word-sampler)
states that extra premise explicitly. A reduction from the original
uniform-only assumption has not been established.

All internal scales matter. Exact finite recursion checks show that easily
distinguished short levels can worsen the final law:

| N,m | TV with exact bridges only through length 2 | TV with exact bridges through length 4 |
| --- | ---: | ---: |
| 3,8 | 0.223476 | 0.067411 |
| 4,8 | 0.361238 | 0.242832 |

These figures enumerate the entire recursive law, including the biased
children; a recursive plant is not automatically the one-level D1. There is
no secure instantiation here yet. The conditional construction identifies
what an eventual hardness assumption would buy and which premise must be
tested, instead of treating the assumption as an end in itself.

**A separate conditional consequence is average-case witness-finding hardness,
but only
with an additional null rarity premise.** Run a proposed search algorithm
and verify its output. If it succeeds on planted samples with probability s,
its distinguishing advantage is at least s-Pr_D0[X_k>0]. Consequently
computational indistinguishability plus negligible null witness existence
would force negligible planted search success.

That simple consequence does not help in these test cases. At N6,m8,k4,
93.8580% of null words already have a witness; at N5,m8,k4 the figure is
94.2675%. Merely finding one is a weak distinguishing signal. Recovering the
particular hidden I, reusing it, or adding an oracle would be different games
and has not been silently assumed. No encryption, one-way function, or
obfuscation construction follows from this experiment.

The first unresolved task is to exhibit **growing plant and complement
lengths, efficient samplers, a nonnegligible statistical gap, and resistance
to the concrete easy tests**. A useful search application additionally needs
a suitable rarity or recovery condition. The 34 finite cases do not establish
such a schedule, and failure of the tested cases does not refute every one.

## Validation and reproducibility

Starting commit: `c4331bada5575f58ad463e62479ff20015305759`.
Python 3.12.3; standard library only. Commands:

```sh
python3 -B experiments/20261110-planted-subsequence/check.py
python3 -B experiments/20261110-planted-subsequence/audit.py
python3 -B experiments/20261110-planted-subsequence/recursive_check.py
```

The final main check took about 29.3 seconds and the independent literal audit
about 1.3 seconds on this host. Exact commands, script hashes, commit, seeds,
parameters, counts and rational probabilities are stored in machine-readable
outputs. Seeds 17,29,43 each generated 200 samples per world in two sampler
smoke cases (2,400 total words); no statistical conclusion relies on them.
The earlier 11-case pilot motivated the extra complement and support checks;
the final scripts/results supersede its generated output, with no failed
scientific claim or discarded negative result.

Mandatory literal cases reproduce S3,m4=27, S4,m4=120, S4,m6=3936.
All fixed-I sampler fibers are checked exhaustively on those cases. Every
mask count in every orbit enumeration equals Z_k Z_(m-k). The independent
audit imports no main-check code and reconstructs the entire N4,m8,k4
witness histogram and attack probabilities. It also verifies the universal
support polynomial's leading coefficient. See [audit-results.json](audit-results.json).
The separate [recursive-results.json](recursive-results.json) records 12 exact
recursive laws, their complete generation-weight histograms, and checks that
every one-level case agrees with the main planted-law calculation. Its code
reuses the tested group/planting implementation and is not an independent audit.

Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict
--- | --- | --- | --- | --- | ---
Completion-table bridge decoder | D0, global uniform | Yes | Independent global draws, not a walk | Literal counts and completion identity | Keep finite reference; factorial cost |
Inverse stable-sort planting | Exact D1 of Q4 | Yes | Two global input bridges; no orbit-convergence claim | Every mandatory fixed-I fiber, seeded smoke | Keep exact reduction conditional on bridge decoders |
Recursive planting | Its exact recursive law R, compared with U | Yes | Independent recursive construction, not a walk | 12 complete finite laws; one-level checks | Keep conditional nonuniform-security construction; no secure schedule |
Hidden-subsequence hardness template | Computational indistinguishability along an unspecified schedule | Both endpoints id | Not a walk | 34 exact cases and fixed-m limit | Inconclusive overall; tested easy/statistical regimes do not justify hardness |

The [claim ledger](claim-ledger.md) retains both positive reductions and
negative/limiting findings. Project-map changes record this investigation as
a diagnostic, with existing mathematical records and priorities preserved.
