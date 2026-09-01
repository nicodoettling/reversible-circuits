# M39 report: exact parking-flow two-hop falsifier

## 1. Exact claim and convention

Let `n>=3`, `r=n-1`, and let the raw state space be the minimal
transposition factorizations of a fixed `n`-cycle. Via Stanley's labeling,
these are the zero-based parking functions of length `r`. The project
composition convention is

    (pq)(x)=p(q(x)),

with tuple products read from left to right. Let `P_r` be the nonlazy
uniform scan of the `r-1` exact adjacent rank-two heat baths, and let
`bar P_r` be its stationary-flow projection to sorted parking multisets.
Let `D_r` be the Lorentzian ideal chain that deletes one uniformly chosen
coordinate and reinserts it uniformly among the feasible values.

The tested universal claim was:

> For every `r` and every positive directed edge of `D_r`, the endpoints
> can be connected in `bar P_r` by a path of length at most two, with each
> used stationary edge capacity at least an inverse polynomial times the
> ideal stationary flow.

This claim is **refuted** already at `n=6`, `r=5`.

## 2. Exact construction and argument

The harness enumerates every parking function, applies the corrected inverse
of Stanley's labeling to recover its maximal noncrossing-partition chain,
and enumerates every legal middle element of every rank-two interval. A
rank-two interval has exactly two or three elements. The common integer flow
scale is `6(r-1)`: an interval of size two contributes weight three and one
of size three contributes weight two. Aggregating these weights by sorted
parking multiset gives the exact stationary flow of `bar P_r`.

For `n=6`, there are exactly `6^4=1296` raw states and 42 parking
multisets. The ideal edge

    (0,0,1,1,2) -> (0,0,1,1,4)

has rate `1/25` in `D_5`, but its endpoints have exact graph distance
three in `bar P_5`. Hence there is no direct or two-hop route, independent
of any capacity exponent. One exact three-edge route is

    (0,0,1,1,2)
      -> (0,1,1,2,4)
      -> (0,0,1,2,4)
      -> (0,0,1,1,4).

The minimum capacity along this particular widest route is `10/9` times
the ideal stationary flow. Thus this witness refutes bounded length two, not
polynomial capacity at unrestricted length.

The obstruction grows in the tested range. At `n=8`, the ideal edge

    (0,0,1,1,2,2,3) -> (0,0,1,1,2,2,6)

has exact projected graph distance four. The complete summary is:

| `n` | raw states | macros | directed ideal edges | missing two-hop edges | maximum shortest distance | minimum widest-capacity ratio | maximum chosen widest-path length |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 3 | 2 | 2 | 0 | 1 | `4/3` | 1 |
| 4 | 16 | 5 | 14 | 0 | 2 | `1/2` | 2 |
| 5 | 125 | 14 | 76 | 0 | 2 | `1/3` | 8 |
| 6 | 1,296 | 42 | 374 | 4 | 3 | `1/4` | 11 |
| 7 | 16,807 | 132 | 1,748 | 54 | 3 | `1/5` | 24 |
| 8 | 262,144 | 429 | 7,916 | 454 | 4 | `1/6` | 28 |

For every tested ideal edge, unrestricted widest-path capacity is at least
`1/(n-2)` times its ideal stationary flow. This exact finite pattern is
evidence for longer buffered routes only; it is not a universal theorem.

## 3. Probability, runtime, path length, and congestion accounting

All transition probabilities are exact rational numbers. The raw scan
factor is `1/(r-1)` and the conditional heat-bath factor is `1/2` or
`1/3`. The projected stationary flow is accumulated before division by
the common raw-state count, and the same omitted stationary normalization
appears in the ideal flow, so every reported ratio is exact.

The exhaustive algorithm visits all `n^(n-2)` parking functions, all
`r-1` rank-two intervals of each function, and then all positive ideal
macro edges. It is exponential in `n` and is a falsification harness, not
a sampler. The largest run has 262,144 raw states, 429 macros, and 7,916
directed ideal edges. The maximum shortest distance of an ideal edge is
four; the maximum length among capacity-maximizing paths selected by the
widest-path algorithm is 28.

No total congestion claim is made. Widest paths are optimized separately,
and many ideal commodities may reuse the same actual edge. Bounding that
aggregate load is exactly the surviving proof obligation.

## 4. Dependencies

- **Proved/cited:** Stanley's parking-function labeling of maximal
  noncrossing-partition chains, in the convention audited in M27.
- **Proved in the harness:** the corrected inverse labeling reproduces every
  input label; every generated partition is explicitly tested for the
  noncrossing condition.
- **Proved in the harness:** Dénes counts, rank-two interval sizes, exact row
  sums, projected detailed balance, ideal detailed balance, and support
  agreement all pass throughout `3<=n<=8`.
- **Inherited/proved:** M36's Lorentzian ideal chain has the parking-macro
  stationary law and gap at least `1/r`.
- **Empirical only outside the exhaustive range:** the apparent
  `1/(n-2)` unrestricted widest-capacity pattern.

## 5. First unproved step

**POLYNOMIAL-LENGTH FRACTIONAL PARKING FLOW.** For every `r`, route all
stationary flows of `D_r` simultaneously through positive edges of
`bar P_r`, with path length and total edge congestion bounded by a
polynomial in `r`.

## 6. Self-attack

The strongest failure mode for the proposed longer-route program is
collective load, not reachability or individual capacity. A large family of
ideal exchanges could be forced through the same small set of buffer macros;
the widest-path calculation would not detect this. The exact range is also
far too small to exclude rapidly growing shortest paths or an asymptotic
capacity collapse. Finally, this projection concerns only minimal
long-cycle endpoint sectors, so even a successful flow would not by itself
prove the full base-scale fixed-endpoint theorem.

## 7. Calibration

- Exact raw counts are `n^(n-2)` for every `3<=n<=8`.
- The corrected Stanley inverse has zero label failures.
- All rank-two intervals have size two or three after explicitly rejecting
  crossing intermediates.
- Both the actual projected chain and `D_r` satisfy exact detailed balance.
- The result is compatible with M32's balanced-binary two-hop bypass: that
  family is not a universal description of all ideal edges.
- Odd identity-word lengths, `m=0`, `m=2`, `N=2`, and the global
  `S_3,m=4`, `S_4,m=4`, `S_4,m=6` suite are not claims of this
  fixed-endpoint long-cycle experiment. Its applicable smallest sectors
  `n=3,4,5` are exhaustively included.

## 8. Artifacts and reproduction

- Plan: `plan.md`
- Exact harness: `exact_two_hop.py`
- Machine-readable result: `results.json`
- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python: 3.12.3; standard library only; no random seed.

Reproduce from the repository root with:

    python3 experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M39-parking-two-hop-falsifier/exact_two_hop.py --n-max 8 --quiet --output experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M39-parking-two-hop-falsifier/results.json

## 9. Verdict

**REFUTED** — the universal length-at-most-two parking-flow claim is false.
This is not a refutation of polynomial total congestion and is not Terminal B.
