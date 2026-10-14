# Labeled-tree slides: report

## Scope and verdict

**Keep: proved auxiliary mixing theorem**, using a checked standard
spanning-tree down-up gap. Author proof and deterministic checks are
complete; independent review remains pending. Polynomial mixing of the
ordered adjacent Hurwitz circuit walk is still **unresolved**.

For N>=3, the half-lazy walk on all vertex-labeled trees choosing an
incident edge pair and one of its two slides has stationary distribution
proportional to W(T)=sum_v binom(deg(v),2), and

    gap >= 2/[(N-1)^2(N-2)^2],
    t_mix(epsilon) = O(N^4 [N log N + log(1/epsilon)]).

The same bound holds for the Metropolis correction to uniform trees, and
for the uniform-tree variant that proposes any edge pair and holds if it
is disjoint. N=1,2 are singleton cases. Bounds are in explicitly labeled
vertex count N, not log N wires. The exponent is not claimed optimal.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| incident-pair P | W-weighted labeled trees | not an identity-word model | not applicable | exact stationarity, connectivity, all comparison paths and loads through N=6 | keep |
| Metropolis M | uniform labeled trees | not an identity-word model | not applicable | exact stationarity and domination of U | keep |
| all-edge-pair U | uniform labeled trees | not an identity-word model | not applicable | exact stationarity and congestion comparison | keep |
| transfer by forgetting circuit order | purported projection of ordered Hurwitz | endpoint is a full cycle | no transfer theorem | N=4 identical-support words have different projected rows | reject this identification |

## Analytic evidence

See proof.md Sections 3--5. The reference B deletes a uniform tree edge
and reconnects its two components by a uniform cross edge. Theorems 1.1
and 5.2 of Anari--Liu--Oveis Gharan--Vinzant, arXiv:1811.01816v3, imply
gap(B)>=1/(N-1). Its exact normalization and graphic-matroid hypotheses
were checked against the primary text.

To simulate an exchange, preserve the two-component forest and slide the
joining edge's endpoints, in a fixed component order. There are at most
N-2 slides. A physical slide identifies the original forest uniquely.
Counting source/target bridges bounds the length-weighted directed flow
by (N-2)/4 before multiplying by the uniform state mass. This proves
comparison congestion at most binom(N-1,2)(N-2). The nonuniform-target
variance comparison cancels its change of edge capacities, so it needs
no extra factor N. No canonical-tree hub or diameter-to-mixing inference
is used.

## Exact validation

Command: `python3 -B experiments/20261014-tree-slides/check.py`.
Commit: `9a7ca2119172f87b15e9f85e28cee6dc91af188f`.
Python 3.12.3; standard library only. Seed 0 recorded, zero random draws.
Source fingerprint and complete compact output are in results.json.

| N | trees | directed slides | nontrivial B transitions | maximum routed length | exact maximum comparison congestion | universal comparison bound |
|---|---:|---:|---:|---:|---:|---:|
| 3 | 3 | 6 | 6 | 1 | 1 | 1 |
| 4 | 16 | 72 | 108 | 2 | 4 | 6 |
| 5 | 125 | 900 | 1860 | 3 | 12 | 18 |
| 6 | 1296 | 12960 | 34920 | 4 | 24 | 40 |

Also checked N=1,2 singletons. Pruefer enumeration was checked independently
against all (N-1)-edge subsets of K_N through N=6. Every state passed
tree preservation, proposal uniqueness, reverse-slide existence, all
three exact stationary column sums, half-laziness, and connectivity.
Every reference transition passed path legality, endpoint recovery,
fixed-forest reconstruction and the exact unweighted congestion-count
formula. Length-weighted loads use rational arithmetic.

The N=3 row is analytically diagonal 1/2 and off-diagonal 1/4, with gap
3/4; the theorem only claims 1/2. At N=4, four stars have W=3 and twelve
paths have W=2, explicitly falsifying a uniform target for P. The two
same-support full-cycle words in proof.md were checked to have different
projected Hurwitz rows, so ordinary forgetting is not even a strongly
lumpable projection of that word walk.

These are exact finite facts, not asymptotic spectral estimates. The
asymptotic result rests on the analytic comparison and cited theorem.
No circuit sampler implementation changed; identity regression cases
are therefore inapplicable to this auxiliary graph kernel.

## Remaining obligation

A circuit result needs a separate target-preserving lift and a polynomial
congestion bound for legal adjacent-word moves, including control of
discarded order information. A tree/factorization counting bijection is
insufficient. The graph theorem resolves the user's explicitly relaxed
model, not this remaining circuit problem. The project map registers
the result provisionally and preserves the previous endpoint frontier.
