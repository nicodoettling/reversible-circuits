# Hidden planted identity subsequences: first viability test

Date: 2026-11-10, Europe/Berlin. Starting commit:
`c4331bada5575f58ad463e62479ff20015305759`.

User authorization: try a new experiment to determine whether the planted
assumption in Q4 of `notes/research-questions-2026-11-06.md` is meaningful.
This is a bounded foreground investigation, not a continuation of an archived
campaign. That explicit request selects the cryptographic alternative over
the historical mixing-only GOAL_SPEC. No agents or external jobs are needed.

## Frozen model and target

All transpositions of S_N, explicit labeled ordered words, products acting
rightmost first. N>=2; even m and even 0<=k<=m. Null D0 is global uniform
Omega(N,m). D1 chooses a fresh uniform k-subset I of positions and then draws
D0 conditioned on the selected ordered subsequence having identity product.
The adversary receives N,m,k and one entire word, without I. No noise, key
reuse, oracle or connected-support restriction. All k-subsets are allowed.
Complexity is measured in explicit N,m, not log(N) wires. No Markov kernel is
proposed; exact finite enumeration and independent bridge draws are used.

## Named obligations

1. Verify the stable-sort bijection from the earlier projection report and
   derive an exact planted sampler from two independent uniform bridges.
2. Derive the likelihood ratio using the number X_k of identity subsequences.
   Test whether cheap observable statistics capture its finite distinguishing
   advantage, and whether witnesses are already abundant under the null.
3. State the actual conditional search consequence and its missing parameter
   premises, without inferring cryptographic hardness from small tests.

## Planned checks and parameters

- Mandatory complete cases S3,m4; S4,m4; S4,m6. Also N2 boundaries, m0,m2,
  odd m and odd k; near-minimal cases among the sweep.
- Finite exact sweep: N3,m6,8,10; N4,m8; N5,m6,8; N6,m6,8. All nontrivial
  even k in each case. Reduce a large case only if an explicit runtime or
  memory obstruction is recorded. Use conjugation orbits with exact weights;
  independently verify the tiny cases by literal-word enumeration.
- Measure exact full-law TV, witness absence and fluctuations, gate
  multiplicities, adjacent repeats, support/components, prefix/window cycle
  types, fixed points/standard character, and combined cheap features.
- Validate the inverse stable-sort sampler exhaustively on mandatory cases,
  then smoke-test draws with seeds 17,29,43. These random draws validate code;
  conclusions about distribution distances use exact counts, not a seed.
- Check meet-in-the-middle witness counts against full subset enumeration.

Follow-up inside this experiment: after the initial sweep passed, add N3,m12
and N8,m8. The latter exhausts every possible support size for length eight,
allowing exact binomial-polynomial evaluation at larger N (not Monte Carlo
extrapolation). Check the complement/transport involution and the resulting
efficient k=m-2 statistic. Compress complete feature histograms so the
reproducibility artifacts remain compact.

Application check: formulate balanced recursive planting as a conditional
computational identity sampler. Explicitly distinguish the original uniform
single-sample assumption from the stronger nonuniform security needed to
hardwire an unavailable exact sibling bridge in the hybrid proof. Compare
the complete finite recursive laws with exact base lengths two and four at
N3/N4 and m4/6/8. This tests bias accumulation, not a security hypothesis.

Use Python 3.12.3 standard library only. Store exact integer histograms and
rational probabilities in results.json; record exact command, repository and
script hashes, parameter values, seeds and runtime. Keep temporary logs in
/tmp if needed. No installation or sampler MCMC convergence claims.

## Failure modes and decision rule

Wrong planting weights, arbitrary shuffling instead of inverse Hurwitz moves,
and conflating connected and global bridges invalidate the experiment.
Conjugation compression must preserve multiplicities and every statistic used.
Finite optimum tests are descriptive, not an asymptotic efficient adversary.

Reject a tested finite case as a promising hardness benchmark when a cheap
statistic exposes most of its TV, or the laws coincide. Keep the formulation
only if it yields exact generation/analysis and a sharply stated next
obligation. Absence of a tested attack is inconclusive about hardness. Write
report.md, proof.md and a claim ledger, with negative findings retained.
