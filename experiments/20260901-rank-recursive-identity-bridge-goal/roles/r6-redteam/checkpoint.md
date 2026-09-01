# R6 substantive checkpoint

Date: 2026-09-01

## Named exact checks

The red-team implementation is independent: it imports no R1/R3 code and
uses direct labeled endpoint walks, full word enumeration, a separately coded
stable-sort/inverse, and a separate positive coefficient evaluator.

So far it has found no counterexample to the accepted R1 or R3 claims:

```text
R1: 57,087 full words round-tripped for 2<=N<=4, 0<=L<=6;
    224 every-endpoint coefficient identities checked.
R3: 1,064 every-endpoint star counts checked for 2<=N<=5, 0<=k<=6;
    912 exact last-factor recurrences checked.
```

All arithmetic is exact.  The full identity fiber sizes reproduced are
`|Omega(3,4;e)|=27`, `|Omega(4,4;e)|=120`, and
`|Omega(4,6;e)|=3936`.  Detailed exact `(k,h)` records, including old and
star fiber sizes and rational branch probabilities, are in
`branch_laws.jsonl`.

## Precisely specified pair architecture

For `N>=3` and even `L>=4`, define `Pair(N,L)` as follows:

1. draw `u` uniformly from `Omega(N-1,L-2;e)` and embed it as fixing `N`;
2. draw `i` uniformly from `[N-1]`;
3. draw uniformly one of the `L-1` gaps of `u` and insert the adjacent block
   `(i N),(i N)` there.

Define `SymPair(N,L)` by additionally choosing uniform `sigma in S_N` and
simultaneously conjugating every factor.  Define the lazy symmetric Hurwitz
kernel `K_H` by holding with probability `1/2`; otherwise choose one of the
`L-1` adjacent positions and one of the right/inverse Hurwitz rewrites
uniformly.  Thus each directed rewrite has probability `1/[4(L-1)]`.

These definitions include all source multiplicities; their pushforward laws
are not assumed uniform on their supports.

## Named obstruction beyond the sorted `h=e` fact

The weighted support-component signature is the sorted multiset

```text
(number of vertices in a support component,
 number of word factors belonging to that component),
```

including isolated vertices with weight zero.  It is invariant under global
conjugation up to label erasure and under every Hurwitz rewrite.

**Proved architecture-specific obstruction.**  Under `SymPair(N,L) K_H^t`,
for every `t>=0`, the event that all `L` factors are one repeated
transposition has probability zero: the lower identity word is nonempty and
uses an old edge, while the inserted star edge is distinct.  If these two
edges meet, their weighted component has at least three vertices; if not,
there are at least two nontrivial components.  Neither signature can become
the one-edge signature under Hurwitz moves.  Under the uniform target,

```text
Pr_U[one repeated edge] = binom(N,2)/|Omega(N,L;e)| > 0.
```

This refutes exact equality for this fully symmetrized, arbitrarily
post-Hurwitz one-pair architecture.  It does not by itself rule out
negligible error in the dense schedule, because the displayed lower bound may
be tiny there.

The exact finite cases give much stronger invariant observables:

| case | Hurwitz-invariant support event `A` | `Pr_SymPair(A)` | `Pr_U(A)` | persistent TV lower bound |
|---|---|---:|---:|---:|
| `N=3,L=4` | connected signature `[(3,4)]` | `1` | `8/9` | `1/9` |
| `N=4,L=4` | two signatures `[(2,2),(2,2)]` | `1/3` | `3/20` | `11/60` |
| `N=4,L=6` | `[(2,2),(2,4)]` or `[(4,6)]` | `25/27` | `495/656` | `3035/17712` |

Because `A` is invariant, these probabilities hold after every finite number
of lazy symmetric Hurwitz steps.  They also survive ideal uniformization
inside every occupied Hurwitz component.  Exact component enumeration found
4, 13, and 17 components in the three cases and gave ideal within-orbit TVs
`1/9`, `11/60`, and `3035/17712`, respectively.

This is a genuine obstruction to the named architecture, not a hardness
claim for all recursive samplers.  The exact R1 disintegration with the R3
prescribed-star sampler remains the first surviving alternative.

## Fresh R2 candidate audit

The R2 lane's two-sided parity-flattened branch sampler became visible after
the first checkpoint.  I independently reconstructed its integer weights,
without importing its implementation:

```text
N binom(L,k) d^(L-k) S_k(g^(-1)(N)),   L-k>=k,
  binom(L,k) d^(L-k) (N-1)^k,          k>L-k.
```

The coset condition `q(g^(-1)(N))=N`, recovery `h=gq^(-1)`, common `N!/2`
scaling, and token recurrence all checked.  Exact identity-branch TVs were

```text
N=3,L=4: 56/783
N=4,L=4: 9/136
N=4,L=6: 29/287.
```

For every feasible endpoint at `N=4,L=128` and `N=5,L=250`, the independent
calculation reproduced the R2 lane's exact maximizing endpoint, exact rational
maximum TV, and `Delta/(1-Delta)` pointwise-normalization bound.  The spectral
prefactors are consistent with projecting out trivial/sign modes; the star
bound uses the fact that no other Young-tableau content has absolute value
`N-1`.

No mismatch was found.  This audit does not close R4/R5: recursive calls can
have short internal lengths, and a fixed long length cannot deliver a user
error smaller than its explicit bound without another mechanism.

## Current status

The pair-architecture claim is **proved**.  The finite computations are exact
facts that could have falsified R1/R3 universal identities; their agreement
does not prove those theorems.  Remaining work is to audit any R2/R4 report
that becomes visible, finish the branch tables and candidate summary, and
write the final calibrated report.
