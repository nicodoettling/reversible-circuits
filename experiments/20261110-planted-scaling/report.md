# Growing plants: the quadratic host leaks, the linear host remains open

Date: 2026-11-10. **Verdict: reject the proposed quadratic-host assumption
with negligible-in-N security for the all-transpositions game; retain the
linear-host version as unresolved.** This responds to growing plants, not
the previous k=m-2 control. The user confirmed considering both an N-gate
plant in an N^2-gate host and a poly(log N)-gate plant in an N-gate host.

Status: self-contained attack arguments plus a checked classical spectral
input and exact finite verification; no independent proof review. This is a
scoped obstruction, not a claim that every planted-circuit model is easy.

## Precise game and security convention

N is permutation degree. Let U_m be global uniform on ordered labeled
length-m transposition identity words. The planted law chooses a fresh uniform
hidden k-subset I and draws U_m conditioned on its ordered subsequence having
identity product. Both full words compute identity, the plant positions are
hidden, and there is one noiseless word with no oracle. Products act rightmost
first. Even m,k are required. The question is whether all poly(N,m)-time
adversaries have negligible distinguishing advantage in N.

| Host m | Plant k | Finding at this security convention |
| --- | --- | --- |
| N^2 | even-rounded (log N)^c, fixed c>0 | **Refuted:** random shared-label test has advantage Omega(k/N^4) |
| N^2 | N, even N | **Refuted:** random equal-gate test has advantage Omega(N^(-5)) |
| N | even-rounded (log N)^c | **Unresolved:** the long-completion argument does not apply |

The bounds are deliberately conservative. They prove inverse-polynomial
leakage, not constant distinguishing advantage. A weaker requirement that no
single-sample adversary attain constant advantage is not refuted by these
bounds alone.

## Why hidden positions do not eliminate this signal

For the first test, select two positions uniformly, select one endpoint of
the first transposition uniformly, and test whether it also occurs in the
second gate. In an iid word the acceptance probability is 2/N. Inside an
identity word each used label must occur at least twice, forcing extra shared
labels when the plant is short compared with N. The chance of selecting two
plant positions is small but still inverse-polynomial for the requested
polynomial-size host.

The second test simply asks whether two random gates are equal. A moment-ratio
argument proves an excess equality probability even when the planted identity
has N gates. It does not enumerate its exponentially many possible locations.

The host is conditioned on identity, so iid heuristics alone would be invalid.
The proof bounds the exact joint marginal on the plant positions and the two
inspected positions. For m=N^2 and k<=N, the remaining completion is long enough
that its relative density error is exponentially small in N. Multiplicative
accuracy survives conditioning on the rare plant event without dividing the
error by that event's probability. The checked input is the classical random
transposition Fourier estimate with its nonlazy parity translation, detailed
in [source-audit.md](source-audit.md).

Let q=binom(N,2), Z_j=|Omega(N,j)|, and delta the parity-correct relative
pointwise error after m-k-2 transpositions. The equal-gate attack has the
explicit finite lower bound

    binom(k,2)/binom(m,2) * (q Z_(k-2)/Z_k - 1/q)
       - 8 delta/(1-delta)^2,      provided delta<1.

All pieces of this bound are evaluated exactly in the checker. The
[proof](proof.md) separately establishes its asymptotic positivity, including
the k=N moment bound. Neither a finite trend nor failed obstruction search is
used to claim the asymptotic result.

## Exact numerical certificates

These are lower bounds for the specific one-random-pair equality test, not
estimates of optimal advantage:

| N | m | k | Certified distinguishing advantage, at least |
| --- | --- | --- | ---: |
| 8 | 64 | 8 | 0.0009336575 |
| 16 | 256 | 16 | 0.0001119291 |
| 32 | 1024 | 26 | 0.0000126199 |
| 32 | 1024 | 32 | 0.0000124700 |

The last two cases directly compare an even-rounded log-squared plant and
a linear-size plant at the same host size. The gaps are small, but an
inverse-polynomial lower bound contradicts negligible-in-N security.
Expected null witness counts are also recorded; their size alone does not
give witness-existence probabilities or prove statistical indistinguishability.

For the finite sweep, L=ceil(log2(N)) and the schedules are k=N,
k=2 ceil(L/2), and k=2 ceil(L^2/2). At nonpowers of two the latter may differ
from rounding (log2(N))^2 directly; it has the same asymptotic scale.
There are 42 scheduled rows: 21 positive quadratic-host certificates
(19 distinct parameter triples), 8 feasible linear-host cases where this
smoothing bound is unavailable, 9 trivial k=m cases, and 4 infeasible k>m
small-parameter cases. Trivial/infeasible controls are not counted as evidence
against a valid nontrivial schedule.

## The remaining candidate assumption

One precise version matching the other requested alternative is:

    N even and sufficiently large; m=N;
    k=2 ceil((log_2 N)^2/2).

**Candidate linear-host planted-identity assumption (unresolved):** for every
probabilistic polynomial-time adversary A, given the explicit N,m,k and one
word, the difference between its acceptance probabilities under U_m and the
fresh-hidden-subset conditional planting law is negligible in N.

This is a definition of what we would like to assume, not an endorsement.
The first missing check is the actual joint bridge/plant low-order law at
m=N, where endpoint conditioning is strong and the dense-host surrogate is
not justified. Failure of the present smoothing bound proves nothing about
security. Actual efficient null/host generation also remains a separate
obligation; efficient short-plant generation does not solve host sampling.

If N^2 host length is essential, raising the plant length to order
N(log N)^2 would make this particular fixed-coordinate signal negligible
by the same completion estimate applied inside the plant. That is a new
candidate schedule, not a hardness result: its full statistical distance and
other attacks have not been analyzed here.

## Security-parameter caveat

If instead the security parameter is n=log_2 N, then N^(-5)=2^(-5n) is
negligible in n, so this argument does not refute that different guarantee.
However, the N^2-gate output is then exponential in n, and poly(N,m) time is
not polynomial in n. A succinct or oracle-access formulation must declare
that different representation and adversary interface explicitly. The report
uses the repository's explicit-degree model throughout.

## Reproduction, dependencies and ledger

Run:

```sh
python3 -B experiments/20261110-planted-scaling/check.py
```

Python 3.12.3, standard library only, deterministic exact arithmetic and no
random seed. The final run took about 2.6 seconds. [results.json](results.json)
records the command, commit, script and prior-reference hashes, all parameters,
rational bounds, return counts, and expected witness counts. The checker
computes spectra from partition content sums and tableau-corner recursion.
Independent cycle-type cut/join counts agree for N2..8 through length 2N,
including S3m4=27, S4m4=120 and S4m6=3936. Row-bound algebra is checked for
r1..500. Eleven comparisons with the prior complete literal-word laws pass,
including S3 zero-error cases. No Monte Carlo estimate supports a conclusion.

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
| --- | --- | --- | --- | --- | --- |
| Conditional low-order law admits multiplicative comparison | proved | delta_(m-k-2)<1; global all-transposition law | proof.md sections 1–2 | Eleven prior exact word-law comparisons | Keep finite certificate formula |
| Polylog plant in N^2 host leaks shared labels | proved; negligible-in-N candidate refuted | Fixed log power; even lengths; checked spectral bound | proof.md sections 3,5 | Exact return/smoothing checks; asymptotics from proof | Reject this scoped assumption |
| N-gate plant in N^2 host leaks gate equality | proved; negligible-in-N candidate refuted | Even N; moment bound; same spectral input | proof.md sections 4–5 | Cut/join count comparison; radial algebra checks; finite certificates | Reject this scoped assumption |
| Linear-host polylog plant is hard | unresolved | Strong endpoint-conditioning law and generation remain to check | Candidate statement above | Eight finite smoothing failures are inconclusive | Retain as a candidate, not accepted hardness |
| These results break every planted circuit model | not claimed | Other libraries/interfaces/security parameters differ | Scope and caveats above | None | Do not generalize |

The original experiment, proof and raw outputs remain unchanged. New map
navigation records this follow-up without upgrading existing mathematical
records, changing the manuscript, or launching a campaign.
