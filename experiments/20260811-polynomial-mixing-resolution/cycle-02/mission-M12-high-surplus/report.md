# M12 Cycle 02 Report: High-Surplus and Dense Thresholds

## 1. Exact claim with all quantifiers and conventions

Permutations are maps on `[N]`; `pq` means `p` after `q`, and words evaluate
as `t_1...t_m`.  Put `M=binom(N,2)`.  The target is the uniform law `pi` on
`Omega(N,m)`, and the chain is exactly

```text
K = (1/2)I
    + (1/(2|R_m|)) sum_{r in R_m} (1/(m-r+1)) sum_i H_{i,r},
R_m={r in {3,4,5}:r<=m}.
```

Every logarithm below is natural.  Let `c(w)` count all components of the
support graph, including isolated labels, and let

```text
Phi_pm(A)=Q_K(A,A^c)/min{pi(A),pi(A^c)}.
```

The following restricted theorem is proved.

> **Uniform dense-threshold theorem.**  For every `N>=3`, every even `m`
> satisfying
>
> ```text
> m-2 >= 4 binom(N,2) log(2N),
> ```
>
> and every `1<=c_0<=N-2`, both sides of
> `A(c_0)={w:c(w)<=c_0}` are nonempty and
>
> ```text
> Phi_pm(A(c_0)) >= (N-1)/[128 binom(N,2)^2].
> ```

For every word,

```text
G(w)=sum_C [k_C-2(|C|-1)]/2=m/2-N+c(w).
```

Therefore the theorem applies to every nontrivial total-surplus threshold
`A_{<=g}` in this dense regime, with exponent independent of `g`.

The report also rigorously refutes one auxiliary all-genus estimate.  If
`C_g(d)` counts connected identity words on a fixed `d`-set of length
`2g+2d-2`, then the fixed-position pendant-square subclass has proportion

```text
R_g(d)=d(d-1)C_g(d-1)/C_g(d),
```

and, for every fixed `d>=3`,

```text
R_g(d)
 ~ [4d^2/((d-1)(d-2)^2)]
      ((d-2)/d)^(2g+2d-2)                  (g -> infinity).
```

It is exponentially small in `g`.  Thus a uniform inverse-polynomial lower
bound for this pendant subclass is false.  This does not refute polynomial
mixing or the square down-up chain: pendant bridge squares are only a subset
of adjacent squares, and the orientation-free cut denominator switches to
the rare disconnected side at high density.

No reducibility example and no total-threshold sequence with
superpolynomially small two-sided conductance was found.  Hence this is not
TERMINAL B.

## 2. Full argument or construction

The complete argument is in [`proof_final.md`](./proof_final.md).  The main
steps, including every multiplicity, are as follows.

For a labeled support partition `P`, put

```text
e(P)=sum_{B in P} binom(|B|,2),
H_P=product_{B in P}S_B,
h(P)=|H_P|.
```

Let `Z_P(k)` count identity words confined to its internal transpositions and
let `E_P(k)` count words with exact support partition `P`.  The central
Cayley operator has regular trace

```text
Z_P(k)=h(P)^(-1) sum_rho dim(rho)^2 nu_rho^k.             (2.1)
```

For each active `S_n` block, `nu_lambda` is the Young-diagram content sum.
The trivial and sign representations give the two parity extrema
`+binom(n,2)` and `-binom(n,2)`.  Every nontrivial representation has top
deficit at least `n`; this includes `n=2`.  Factoring the trace over blocks
and pairing a representation tuple with its conjugate proves, uniformly for
every partition and every even `k/e(P)>=4log(2N)`,

```text
2e(P)^k/h(P) <= Z_P(k) <= 4e(P)^k/h(P).                   (2.2)
```

This factorization retains all mixed component-parity modes; it does not
apply a false `N!`-multiplicity bound to the slowest size-two mode.

If a confined word does not have exact partition `P`, some nominal block of
size `n` admits a cut of sizes `a,n-a` with no used crossing edge.  Refining
along that cut loses `a(n-a)` generators and changes the subgroup order by
`binom(n,a)`.  Using (2.2) and summing over every cut gives total relative
error at most

```text
sum_blocks 2*4^n exp[-4log(2N)(n-1)] <= 1/N^3 < 1/2.
```

Thus, simultaneously at lengths `m-2` and `m`,

```text
e(P)^k/h(P) <= E_P(k) <= 4e(P)^k/h(P).                    (2.3)
```

No Möbius cancellation is assumed: this is the first, safe
inclusion--exclusion/union-bound direction.

Let `W_c(m)` be the exact number of words with `c` components.  Order a
partition's blocks by smallest label and merge its first two.  Given the
merged partition, every preimage comes from splitting the block containing
label `1`.  Summing the exact count ratio (2.3) over all such splits yields

```text
W_{c+1}(m) <= q_N W_c(m),       q_N=4/N^4<=1/4.           (2.4)
```

This includes the inverse multiplicity of the merge map.  Consequently an
upper component tail is at most `4/3` times its first layer, and the upper
tail is the smaller side of every nontrivial lower threshold.

For full boundary flow, fix an exact disconnected partition `P` and write
`e=e(P)`, `x=M-e`.  Inserting an internal square at a designated adjacent
slot is injective because deletion recovers both the shorter word and the
edge.  Equation (2.3) gives designated-square probability at least `1/(4e)`.
Deleting that square preserves exact partition `P`; refreshing it to any of
the `x` crossing squares merges exactly two components.

Pad the square by one unchanged neighbor and use an actual `r=3` update.  If
the padding transposition is `a`, the exact fiber size is

```text
D_N=F_3(a)
   =M+3[2(N-2)]+2binom(N-2,2)
   =(3N^2+N-12)/2 <=4M.                                  (2.5)
```

The three terms are respectively third factor equal to `a`, sharing one
endpoint, or disjoint; the corresponding two-factor fibers have sizes
`M,3,2`.  A specified refresh at a specified square slot has exact kernel
contribution

```text
1/[2|R_m|(m-2)D_N].                                      (2.6)
```

Because a crossing replacement changes exactly the two square positions,
targets arising from different scan positions are disjoint.  Summing all
`m-1` slots and all `x` crossing choices gives average exit from every exact
partition at least

```text
x/(24eD_N) >= (N-1)/(96M^2)=alpha_N.                     (2.7)
```

Here `x>=N-1` for every disconnected partition.  Retaining only the first
layer of the smaller upper tail gives

```text
Q_K(A,A^c) >= alpha_N W_{c_0+1}/|Omega(N,m)|,
pi(A^c)    <= (4/3)W_{c_0+1}/|Omega(N,m)|.
```

Their ratio is the claimed `(N-1)/(128M^2)`.  This is a complete word-chain
stationary-flow bound, not merely a component-count transition or a
reachability statement.

For the recurrence audit, Dubrovin--Yang--Zagier's P1, with the
cover-to-word normalization checked in Cycle 01, gives
`C_g(d)~(2/d!)binom(d,2)^(2g+2d-2)` only for fixed `d`.  Applying it at fixed
degrees `d,d-1` proves the displayed exponential decay of `R_g(d)`.
Their degree-six finite-exponential formula has coefficients of both signs,
so termwise positivity is unavailable; their fixed-degree and fixed-genus
asymptotics provide no joint error bound.  Do--He--Robertson likewise fix the
ramification profile in their large-genus theorem.  These asymptotics are
used only to refute the pendant-ratio lemma, not in the dense-threshold
theorem.

## 3. Worst-case probability, runtime, path length, and congestion accounting

- Exact-support count error: at most `1/N^3`, uniformly over all labeled
  partitions and both lengths `m-2,m`.
- Component-layer ratio: `q_N=4/N^4`; hence the boundary layer is at least
  `3/4` of the smaller tail mass.
- Fixed-position deletable internal square: probability at least `1/(4e)`.
- Crossing choices: exactly `x=M-e`, with worst case `x>=N-1`.
- Laziness: exact factor `1/2` appears in (2.6).
- Block-size choice: exact factor `1/|R_m|`, bounded using `|R_m|<=3`.
- Window choice: exact factor `1/(m-2)` for `r=3`; summing the `m-1`
  disjoint-target square positions contributes `(m-1)/(m-2)>=1`.
- Conditional heat bath: exact factor `1/D_N`, with `D_N<=4M`.
- Each favorable move is one actual `K` transition.  Path length is one and
  there is no canonical-path, vertex, or edge-congestion term.
- The inherited exact block samplers for `r=3,4,5` have polynomial cost in
  `N,m`; this proof introduces no modified chain.  Identifying a support
  partition, an internal square, or a crossing edge is polynomial-time.
- No computation or random sampling was used, so there is no seed or finite-
  data runtime to report.

## 4. Dependencies

- **Proved here:** `G=m/2-N+c`; the block-factorized central trace inequality
  including parity and size-two cases; the exact-support union bound; the
  deterministic partition-merge multiplicity; geometric layer tails and
  smaller-side orientation; the fixed-position square injection; the exact
  `D_N` enumeration; full one-step boundary flow; the uniform dense-threshold
  theorem; exponential decay of the fixed-degree pendant-square subclass
  given the cited asymptotic.
- **Proved, inherited:** exact heat-bath reversibility and uniform
  stationarity; the exact kernel definition; polynomial exact block samplers;
  L-0020's more general adjacent-pair comparison.  The proof uses the sharper
  special `D_N` comparison directly.  L-0022's corrected JSTV theorem is not
  needed because no projection/restriction gap is inferred.
- **Cited:** [Dubrovin--Yang--Zagier, *Classical Hurwitz numbers and related
  combinatorics*](https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf),
  P1 and equations (1), (3), (13), (19)--(21), for the precise fixed-degree
  large-genus hypothesis and Frobenius context; [Do--He--Robertson, *The
  structure of Hurwitz numbers with fixed ramification profile and varying
  genus*](https://arxiv.org/abs/2409.06655), Theorems 1.5--1.6, for the scope
  of the generalized fixed-profile result.  Neither source is needed for the
  dense-threshold theorem.
- **Empirical/calibration only:** the exact `S_3,m=4`, `S_4,m=4`, and
  `S_4,m=6` state and Hurwitz-component counts.
- **Conditional/unneeded:** no global Hurwitz mixing, JSTV mean-lift, or
  large-block comparison claim is assumed.

## 5. First unproved step

> **Intermediate-density total-surplus threshold proposition.**  There are
> universal constants `c>0,C<infinity` such that, for every `N>=3`, every even
> `m` with
>
> ```text
> 2(N-1)<m<2+4binom(N,2)log(2N),
> ```
>
> and every integer `g` for which `A_{<=g}` and its complement are nonempty,
>
> ```text
> Phi_pm(A_{<=g}) >= c(Nm)^(-C).
> ```

The present trace/inclusion argument loses uniformity below its support-
partition mixing scale.  Proving the proposition would eliminate every
dense total-surplus threshold.  Refuting it requires an explicit sequence
with the exact smaller-side mass and full `r=3,4,5` boundary flow, not merely
an exponentially small pendant-square statistic.

## 6. Strongest self-attack and failure mode

The theorem leaves the entire intermediate window from just above connected
minimal length through order `N^2 log N`.  At those lengths, a support
partition may contain a dense giant block and a rarely selected size-two
block; the uniform trace factorization no longer makes all parity and
connectivity errors small.  This is a limitation of the proof, not evidence
for a bottleneck.

The result addresses only total-surplus/component-count cuts.  A bottleneck
may lie strictly inside one exact support partition or connected fiber, in an
ordering or representation statistic invisible to `c(w)`.  M13's finding
that doubled-tree/mountain cuts have polynomial escape rules out two examples
but not all such cuts.

Equation (6.3) in `proof_final.md` concerns pendant squares whose deletion
removes one label and leaves a connected word on the remaining labels.  It
must not be promoted to a claim about all adjacent squares, all splitting
moves, or the square down-up chain.  Indeed the full dense cut has polynomial
conductance because its smaller side exits by merges.

Finally, a polynomial conductance lower bound for one family of cuts is not a
global spectral-gap lower bound.  Conversely, failure of this red-team lane
to find a cut is not a refutation of TERMINAL B.

## 7. Calibration results

- Odd `m`: `Omega(N,m)` is empty; no cut is asserted.
- `m=0`: singleton; no cut is asserted.
- `N=2`, even `m`: singleton; excluded from the theorem.  The trace proof's
  active `S_2` calculation is exact (`e=1`, eigenvalues `+1,-1`).
- `m=2,N>=3`: the allowed chain has no block and is disconnected; this
  excluded case is not used to claim TERMINAL B.
- `S_3,m=4`: the 27 words split by support components as `W_1=24,W_2=3`;
  there are four pure-Hurwitz components.  The `r=4` update is a whole-word
  heat bath with exact kernel coefficient `1/4`, and it is not dropped.  The
  theorem's density hypothesis is not asserted.  More generally for fixed
  `N=3`, the disconnected side consists of the three constant-edge words;
  for even `m>=6`, its `r=4` exit probability is at least
  `(1/6)(24/27)=4/27`, illustrating why an exponentially rare reverse
  pendant split is not a bottleneck.
- `S_4,m=4`: the 120 words have `W_2=114,W_3=6`; there are 13 pure-Hurwitz
  components.  This checks disconnected zero-surplus words and the fact that
  full support is infeasible at this length.  The whole-word `r=4` update is
  retained.
- `S_4,m=6`: the 3936 words have `W_1=2880,W_2=1050,W_3=6`; there are 17
  pure-Hurwitz components.  This agrees with `G=c-1` and the Cycle-01
  zero/one-surplus counts.  The present high-density theorem is not
  extrapolated to this finite case.
- Connected near-minimal doubled-tree examples lie outside the new density
  regime and are covered only by the prior restricted anti-bottleneck
  arguments.  No route uses a canonical doubled-tree hub.
- Disjoint components commute but retain a nontrivial color interleaving.
  `E_P(k)` counts the original ordered words, so all interleavings are
  included automatically.
- Edge-multiplicity parity and vertex-degree parity are never used as
  identity criteria; parity in Lemma 2.1 is the exact group-character parity.
- The known failure of internal length-two local simulation is irrelevant:
  every boundary move is an actual globally padded `H_3` update of `K`.
- No finite spectrum, slow trace, graph-only experiment, or small-mass set is
  used to infer an asymptotic conclusion.

## 8. Artifacts and reproduction commands

Owned artifacts:

- `plan.md`
- `checkpoint.md`
- `proof.md` (valid but weaker preliminary density bound)
- `proof_final.md` (superseding proof)
- `report.md`

No executable computation, randomness, third-party package, or generated
raw data was used.  The universal claim that a finite computation would need
to falsify was instead settled analytically.  Read the final artifacts with:

```bash
sed -n '1,999p' \
  experiments/20260811-polynomial-mixing-resolution/cycle-02/mission-M12-high-surplus/proof_final.md
sed -n '1,999p' \
  experiments/20260811-polynomial-mixing-resolution/cycle-02/mission-M12-high-surplus/report.md
```

Repository baseline inherited from Cycle 01: commit `502a6f0` on `main`.

## 9. Verdict

OPEN AT A NAMED STEP: Intermediate-density total-surplus threshold proposition.

