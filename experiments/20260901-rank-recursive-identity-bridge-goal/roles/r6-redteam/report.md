# R6 final report: exact branch and paired-lift red team

Date: 2026-09-01 UTC
Role target: exact finite falsification of R1--R5 candidates and quantified
paired-lift bias
Primary outcome: **R1 and R3 independently survive; the final fixed-error
dense closure survives a fresh constant audit; one precisely specified
symmetrized/post-Hurwitz pair architecture is rigorously refuted as exact**

## 1. Convention, targets, and calibration

Permutations are maps and

```text
(p q)(x)=p(q(x)).
```

A displayed word `t_1...t_L` therefore acts rightmost-first.  The canonical
comparison law is exact uniform

```text
U(N,L;g)=Uniform Omega(N,L;g).
```

All reported probabilities and total-variation distances were computed as
exact rational numbers.  Full enumeration can refute a universal identity,
inverse, recurrence, or exact-sampler claim.  Agreement in finitely many
cases does not prove an asymptotic theorem, a complexity bound, or a mixing
claim.

The red-team script is implementation-independent: it imports no code from
R1, R2, R3, or R4.  It separately implements permutation arithmetic,
stable sorting and its inverse, endpoint dynamic programs, the positive star
coefficient extraction, pair pushforwards, and Hurwitz components.

## 2. Independent R1 audit

For each word, the script repeatedly rewrites an adjacent star-old inversion

```text
(i N) a  ->  a (a^{-1}(i) N),
```

then independently reconstructs the original binary pattern with the inverse
rewrite.  It checks the displayed product, exact inversion count, and literal
word round trip.

For every word with `2<=N<=4` and `0<=L<=6`, all checks passed:

```text
57,087 full-word inverse round trips
199,613 local rewrites checked
224 every-endpoint coefficient identities
0 failures.
```

The coefficient check independently compared the full transposition endpoint
DP with

```text
sum_k binom(L,k) sum_h
  OldCount(N-1,L-k,h) StarCount(N,k,h^{-1}g).
```

This could have falsified product orientation, the binary multiplicity, or
the fixed-pattern inverse.  It found no counterexample to R1.

## 3. Independent R3 audit and boundaries

A direct labeled star-walk DP was compared with a separately implemented
exact-support/Féray coefficient evaluator for every endpoint with
`2<=N<=5`, `0<=k<=6`.  The last-factor identity was checked independently.

```text
1,064 every-endpoint count equalities
912 last-factor recurrence equalities
0 failures.
```

`star_fibers.jsonl` contains every labeled endpoint record.  Representative
boundary facts are:

| case | exact counts |
|---|---|
| `N=2,q=e` | one word at even `k=0,2,4,6`; zero at odd `k` |
| `N=2,q=(1 2)` | one word at odd `k=1,3,5`; zero at even `k` |
| `N=3,q=(1 2)` with pivot fixed | minimum `3`; counts `2` at `k=3`, `10` at `k=5` |
| `N=3,q=(1 3)` incident to pivot | minimum `1`; counts `1,3,11` at `k=1,3,5` |
| `N=3,q=(1 2 3)` | minimum `2`; counts `1,5,21` at `k=2,4,6` |

The full identity fibers at `N=2` contain the empty word at `L=0`, one word
at every positive even length, and no word at odd length.  Direct checks at
`N=3` likewise found empty identity fibers at `L=1,3,5`.  Thus the audit
covers `N=2`, `L=0`, odd length, minimal star length, and pair padding.

These checks support R3 but do not replace its proof or primary-source input.

## 4. Exact `(k,h)` branch laws

Each identity word was independently stable-sorted.  The direct branch count
was compared with

```text
binom(L,k) OldCount(N-1,L-k,h) StarCount(N,k,h^{-1}).         (1)
```

Every row below gives the count for each indicated labeled `h`; multiply by
the `h`-multiplicity for the row's total contribution.  Divide by the stated
identity-fiber size for its exact probability.

| `N,L` | `k` | `h` family | labeled `h` count | old fiber | star fiber | patterns | count per `h` |
|---|---:|---|---:|---:|---:|---:|---:|
| `3,4` | 0 | `e` | 1 | 1 | 1 | 1 | 1 |
| | 2 | `e` | 1 | 1 | 2 | 6 | 12 |
| | 3 | lower transposition | 1 | 1 | 2 | 4 | 8 |
| | 4 | `e` | 1 | 1 | 6 | 1 | 6 |
| `4,4` | 0 | `e` | 1 | 27 | 1 | 1 | 27 |
| | 2 | `e` | 1 | 3 | 3 | 6 | 54 |
| | 3 | lower transposition | 3 | 1 | 2 | 4 | 8 |
| | 4 | `e` | 1 | 1 | 15 | 1 | 15 |
| `4,6` | 0 | `e` | 1 | 243 | 1 | 1 | 243 |
| | 2 | `e` | 1 | 27 | 3 | 15 | 1215 |
| | 3 | lower transposition | 3 | 9 | 2 | 20 | 360 |
| | 4 | `e` | 1 | 3 | 15 | 15 | 675 |
| | 4 | lower 3-cycle | 2 | 3 | 3 | 15 | 135 |
| | 5 | lower transposition | 3 | 1 | 20 | 6 | 120 |
| | 6 | `e` | 1 | 1 | 93 | 1 | 93 |

The exact `k` marginals are:

```text
N=3,L=4, |Omega|=27:   {0:1, 2:12, 3:8, 4:6}
N=4,L=4, |Omega|=120:  {0:27, 2:54, 3:24, 4:15}
N=4,L=6, |Omega|=3936: {0:243, 2:1215, 3:1080,
                         4:945, 5:360, 6:93}.
```

The nonidentity `h` mass is substantial in these cases, but that is only a
diagnostic: the fact that adjacent pair insertion starts in the `h=e` sorted
branch was already known.

## 5. Precisely specified pair and Hurwitz architectures

For `N>=3` and even `L>=4`, define `Pair(N,L)`:

1. sample `u` uniformly from `Omega(N-1,L-2;e)` and embed it as fixing `N`;
2. sample `i` uniformly from `[N-1]`;
3. sample one of the `L-1` gaps of `u` uniformly and insert the adjacent block
   `(i N),(i N)`.

Repeated outputs are aggregated with their exact source multiplicity.  Define
`SymPair(N,L)` by then choosing uniform `sigma in S_N` and simultaneously
conjugating every factor.

The postprocessing kernel `K_H` is the following lazy symmetric Hurwitz walk:

- hold with probability `1/2`;
- otherwise choose one of `L-1` adjacent positions and one of the right or
  inverse Hurwitz rewrites uniformly.

Each directed rewrite consequently has probability `1/[4(L-1)]`.  Define
`OrbitUniformize` as the favorable idealization that replaces the current law
inside each Hurwitz component by the uniform law there while retaining its
component mass.  This is the limit of the finite lazy symmetric walk in these
enumerated components, not a claimed finite mixing-time bound.

## 6. Rigorous obstruction beyond `h=e`

For a word, define its unlabeled weighted support signature as the sorted
multiset

```text
(number of vertices in a support component,
 number of factors whose edge belongs to that component),                  (2)
```

including isolated vertices with weight zero.  A Hurwitz move either swaps
disjoint edges or replaces two incident edges by two edges spanning the same
three vertices.  It therefore preserves the connected-component partition
and each component's factor count.  Global conjugation only relabels the
signature.

### General one-pair obstruction

**Proved.**  For every `N>=3`, even `L>=4`, and every `t>=0`, under

```text
SymPair(N,L) K_H^t,                                          (3)
```

the event `E_1` that all `L` factors are one repeated edge has probability
zero.  The lower identity word is nonempty and contains an old edge distinct
from the inserted star edge.  If the two supports meet, the relevant
component has at least three vertices; if they do not, there are at least two
nontrivial components.  Neither signature can reach the single-edge
signature under Hurwitz moves.

Under the uniform target there is exactly one word `tau^L` for each
transposition `tau`, hence

```text
Pr_U(E_1)=binom(N,2)/|Omega(N,L;e)| > 0,
d_TV(SymPair K_H^t,U) >= binom(N,2)/|Omega(N,L;e)|.           (4)
```

This refutes exact equality for the fully symmetrized, arbitrarily
post-Hurwitz architecture (3).  It does not refute negligible error in the
dense schedule: the lower bound in (4) may itself be negligible.

### Strong exact finite observables

The enumerated cases give larger invariant events.  Signatures below omit no
isolates unless they are displayed.

| case | invariant event `A` | `Pr_SymPair(A)` | `Pr_U(A)` | TV lower bound for every `t` |
|---|---|---:|---:|---:|
| `N=3,L=4` | `[(3,4)]` | `1` | `8/9` | `1/9` |
| `N=4,L=4` | `[(2,2),(2,2)]` | `1/3` | `3/20` | `11/60` |
| `N=4,L=6` | `[(2,2),(2,4)]` or `[(4,6)]` | `25/27` | `495/656` | `3035/17712` |

The gaps persist for every number of Hurwitz steps.  Exact Hurwitz component
enumeration found respectively 4, 13, and 17 components.  Even ideal
within-orbit uniformization has TV exactly

```text
1/9, 11/60, 3035/17712,                                    (5)
```

so qualitative orbit connectivity or perfect mixing inside each initially
weighted orbit cannot fix the component-mass bias.

This is an architecture-specific theorem, not an unconditional hardness
result.  It does not cover multi-pair dense lifts, an orbit-breaking
postprocessor, or the exact R1/R3 rank disintegration.

## 7. Exact paired-lift statistics

| case | adjacent-pair TV | conjugation-symmetrized TV | TV after `K_H^1` | after `K_H^2` | after `K_H^4` | ideal orbit TV |
|---|---:|---:|---:|---:|---:|---:|
| `N=3,L=4` | `7/9` | `5/9` | `1/3` | `7/27` | `653/3888` | `1/9` |
| `N=4,L=4` | `31/40` | `1/2` | `191/540` | `493/1620` | `7099/29160` | `11/60` |
| `N=4,L=6` | `1177/1312` | `435/656` | `79507/147600` | `205417/442800` | `20827133/55350000` | `3035/17712` |

The symmetrized laws occupy 1 of 4, 7 of 13, and 11 of 17 exact Hurwitz
components in the three cases.  Finite Hurwitz support expansion is visible,
but its TV floor is fixed by the invariant macro law.

## 8. Fresh audit of the R2 two-sided dense branch sampler

After the R2 checkpoint became visible, this lane independently reconstructed
its two complementary parity-flattened weights.  With
`d=binom(N-1,2)`, `s=L-k`, `b=N-1`, and
`S_k(g^{-1}(N))` the exact projected star-word count, the common-scaled
`k` weights are

```text
N binom(L,k)d^s S_k(g^{-1}(N)),  s>=k,
  binom(L,k)d^s b^k,             k>s.                        (6)
```

The audit confirmed the orientation
`q(g^{-1}(N))=N`, recovery `h=gq^{-1}`, token recurrence, common `N!/2`
scaling, and positive labeled support.  Exact identity-branch TVs are

```text
N=3,L=4: 56/783,
N=4,L=4: 9/136,
N=4,L=6: 29/287.                                            (7)
```

For every feasible external endpoint at `(N,L)=(4,128)` and `(5,250)`, the
independent DP reproduced the R2 lane's exact maximizing endpoint, exact
rational maximum TV, and pointwise-normalization bound.  The maximum TVs were
approximately `6.862e-13` and `1.004e-19`; the proved bounds audited were
approximately `3.940e-11` and `1.068e-14`.

The spectral prefactors are consistent with removing the trivial and sign
modes: projecting both point masses contributes `(G!-2)/2` to the relative
entry bound, and the nontrivial star-walk content eigenvalues have absolute
value at most `N-2`.  No mismatch was found.

This audit supports the one-rank dense R2 theorem.  It does not prove full
recursive closure: lower-rank calls may receive short retained lengths, and a
fixed-length bound cannot meet an arbitrarily smaller requested `epsilon`
without a tunable mechanism or exact fallback.

## 9. R4/R5 projected closure audit

The final R4/R5 construction uses

```text
q^{-1}(r)=g^{-1}(r), equivalently q(g^{-1}(r))=r,
h=gq^{-1}.                                                   (8)
```

This orientation, its two-state projected count, and its common flat old
factor agree with the independent branch/token calculations.  The
pointwise old-endpoint estimate is sufficient for a one-rank positive
bridge-weight comparison when the retained old length is long.

The final proof was audited line by line after it became available.  For the
global top rank `N`, it defines rational rank increments `w_r`, cumulative
floors

```text
B_r=ceil(N r(r-1)c_r),
```

and discards only an old-long branch whose old length is below `B_(r-1)`.
The following checks passed independently.

- The ceiling loss in the cutoff gap is exactly at most one.  With `W_N<=3`,
  the two rank-increment terms give

  ```text
  E[A]-B_(r-1)
   >= N sqrt(r)/16 + (25/2)z_N r - 1
   >= N sqrt(r)/32 + 6z_Nr=:t_0.
  ```

- Under `12z_N<=N` and `r>=6`,
  `t_0/(Nr)<=1/(32sqrt(6))+1/2<33/64`.  The star-count binomial has mean at
  most `5Nr`, so Bernstein's denominator is below `12Nr`.  Squaring the two
  positive pieces of `t_0` gives separately `N/12288` and at least
  `3r log N` in the exponent.
- The full transposition walk's nontrivial periodic remainder is at most
  `(1-2/(r-1))^L`.  At `L>=B_r` this yields the uniform feasible-endpoint
  lower bound `|Omega(r,L;g)|>=binom(r,2)^L/r!`, so multiplying the
  unconditioned binomial tail by `r!` is a valid bridge-conditioning step.
- For the untruncated proposal, the normalized pointwise likelihood-ratio
  interval gives `Q(discarded)<=3U(discarded)` when `Delta<=1/2`.  The actual
  implementation instead zeros the corresponding `k` weights.  Comparing
  first with `U` conditioned on the retained event costs its exact discarded
  mass, and the retained likelihood-ratio comparison costs
  `Delta/(1-Delta)`; no unproved independence under the bridge is used.
- Every surviving old-long child has length at least its next-rank floor;
  star-long branches terminate.  Markov-kernel contraction therefore gives
  the claimed rank telescope.

No counterexample or missing inequality was found.  Subject to the imported
proved R1--R3 results, this audit accepts the R4/R5 theorem

```text
d_TV(output,U_(N,2N^3;g)) <= 3N exp(-N/12288)
```

for all sufficiently large `N`, uniformly over feasible `g`, with the stated
polynomial expected runtime.  This is a fixed negligible-error theorem, not
an arbitrary-accuracy theorem: at the scheduled length it does not meet a
requested `epsilon` below the displayed floor.

## 10. Candidate ledger

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| exact R1 branch + exact R3 star conditional | exact `U(N,L;g)` given exact branch/lower sampler | yes | direct construction is not confined to one orbit | R1/R3 independent checks pass | promote as reduction, not full sampler |
| R2 two-sided dense branch flattening | negligible-error dense branch law | yes after exact conditionals | full branch support when `Delta<1` | small and dense exact audits pass | promote one-rank theorem; fixed-error closure supplied and audited in R4/R5 |
| `Pair(N,L)` | exact `U(N,L;e)` | yes | samples several starting components only | large exact TV | reject |
| `SymPair(N,L)` | exact `U(N,L;e)` | yes | global conjugation crosses some labeled components, not macro signatures | exact invariant gap | reject |
| `SymPair K_H^t` | exact/global uniform after Hurwitz scrambling | yes | no crossing after initialization | persistent event (2) gap | reject as exact for every `t` |
| `OrbitUniformize(SymPair)` | ideal within-orbit uniform | yes | no | exact component-mass TVs (5) | reject as global uniform |
| R4/R5 retained two-sided recursion | fixed negligible-error dense recursive sampler | yes | direct construction is not confined to one orbit | orientation, cutoff constants, bridge denominator, conditioning, and telescope pass a fresh audit | promote at its fixed error; not tunable in `epsilon` |

## 11. Artifacts and reproduction

Files in this role directory:

- `plan.md`, `checkpoint.md`, `report.md`;
- `exact_redteam.py`, the self-contained deterministic harness;
- `results.json`, summary plus exact branch/pair/R2 records;
- `branch_laws.jsonl`, every nonzero exact branch in the three required cases;
- `star_fibers.jsonl`, every endpoint through `N=5,k=6`.

Reproduction command:

```bash
python3 experiments/20260901-rank-recursive-identity-bridge-goal/roles/r6-redteam/exact_redteam.py \
  --output-dir experiments/20260901-rank-recursive-identity-bridge-goal/roles/r6-redteam
```

The recorded run used repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, CPython 3.12.3, no
nonstandard dependencies, no randomness, and about eight seconds wall time.

The harness uses full enumeration only through `S_4,L=6`; its cost is
exponential in `L` and is not an implementation of the proposed large-rank
sampler.  Endpoint DPs and rational calculations are exact finite audit
tools.

## 12. Accepted scope and first open step

Accepted as proved:

- the exact finite branch, star, pair-pushforward, finite-Hurwitz, and
  orbit-uniformization calculations;
- the general invariant obstruction (4) to the specified one-pair
  symmetrized/post-Hurwitz architecture;
- independent finite survival of R1 and R3.

Accepted as a successfully audited candidate, with its proof owned by R2:
the one-rank two-sided dense branch approximation.

Accepted after a fresh proof audit, with its proof owned by R4/R5: the
retained two-sided recursion with total error at most
`3N exp(-N/12288)` at the scheduled dense length.

Not proved here or in that closure theorem: a tunable polynomial sampler at
fixed `N,L`.  The first surviving standalone obligation is the tunable
positive connection lemma: sample the exact R1 labeled branch law to any
requested `epsilon` in time polynomial in `r,L,log(1/epsilon)`, or supply an
exact polynomial sampler.  The current dense recursion cannot be driven
below its explicit error floor merely by increasing runtime.

role: r6-redteam
claim: Independent exact enumeration validates R1 and R3 in all stated small cases and proves that the specified adjacent one-pair lift remains nonuniform after uniform conjugation and any number of Hurwitz steps, with explicit persistent support-signature probability gaps.
status: proved
assumptions: Permutations use map composition (p q)(x)=p(q(x)); pair, conjugation, and lazy symmetric Hurwitz kernels are exactly those defined in Sections 5-6; R2 spectral theorem remains owned by its proof report.
evidence: exact_redteam.py; results.json; branch_laws.jsonl; star_fibers.jsonl; 57,087 R1 round trips, 1,064 R3 endpoint checks, exact branch laws, exact Hurwitz components, and rational TV tables.
independent_checks: Self-contained implementation imports no other role code; direct word enumeration, endpoint DPs, support-formula counts, stable-sort branches, and component BFS cross-check one another; R2 dense maxima were independently reproduced for every feasible endpoint at N=4,5; the final R4/R5 cutoff, Bernstein, bridge-denominator, conditioning, recursion-boundary, and telescope calculations were checked line by line with no mismatch.
complexity: The audit uses O(binomial(N,2)^L) full enumeration in its largest word-level cases, polynomial endpoint DP for fixed N, and O(|Omega| L) finite Hurwitz graph exploration; these are finite falsification costs, not sampler-runtime claims.
first_unproved_step: Prove the tunable positive connection lemma: sample the exact labeled R1 branch law to every requested epsilon in time polynomial in r,L,log(1/epsilon), or give an exact polynomial sampler; the accepted dense recursion has a fixed length-determined error floor.
verdict: promote
