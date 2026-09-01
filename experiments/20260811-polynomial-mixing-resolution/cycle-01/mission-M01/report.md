# M01 Final Report

## 1. Exact claim with quantifiers and conventions

**Claim.** For every `N>=3` and every even `m>=4`, the exact lazy random-scan
same-product heat-bath chain `K_{N,m}` with block sizes `{3,4,5}` (restricted
to sizes at most `m`) is irreducible on `Omega(N,m)`.

Permutations are maps on `[N]`; `pq` is `p` after `q`; words evaluate as
`t_1...t_m`. The exact kernel normalization is the one in the run manifest.

## 2. Full argument

The complete argument is in `proof.md`. Length-three heat baths realize every
project Hurwitz and inverse-Hurwitz move, including boundary pairs. By
Ben-Itzhak--Teicher Theorem 3.4, each word is Hurwitz-equivalent to an explicit
representative made entirely of adjacent equal pairs, with the same labeled
weighted support components. Length-four heat baths can replace any such pair
`(t,t)` by `(s,s)`, including at a boundary and when `m=4`. Refreshing all
pairs to `(1,2),(1,2)` connects every state to one universal word.

## 3. Probability, runtime, path length, and congestion accounting

A chosen padded Hurwitz transition has probability at least

    [2|R_m|(m-2)F_3(h)]^{-1}>0,

and a chosen square refresh has probability at least

    [2|R_m|(m-3)F_4(h)]^{-1}>0.

There are exactly `m/2` square refreshes after reaching the paired
representative. The cited classification guarantees a finite Hurwitz path but
this report proves no polynomial upper bound on its length, no runtime bound
for finding that path, and no congestion bound. Routing through the universal
word is explicitly rejected as a mixing comparison because its stationary
mass can be exponentially small.

## 4. Dependencies

- **cited and checked:** Ben-Itzhak--Teicher, arXiv:math/0110110v1, Theorem
  3.4, including hypotheses and inverse-generator convention translation;
- **proved:** padded-Hurwitz realization by `H_3`;
- **proved:** explicit adjacent-pair representative with matching macro data;
- **proved:** arbitrary adjacent-square refresh by `H_4`;
- **proved inherited:** feasible component criterion, although only its
  necessity is used to confirm the construction length;
- **not used:** any finite spectral evidence, missing fresh-square result, or
  quantitative Hurwitz-mixing conjecture.

## 5. First unproved step

**Proposition M01-GAP (open).** There exist universal `c>0` and finite `C`
such that for all `N>=3` and even `m>=4`,
`gap(K_{N,m})>=c(Nm)^{-C}`.

M01 removes qualitative irreducibility as a dependency but supplies no
quantitative inequality toward this proposition.

## 6. Strongest self-attack

The universal-hub construction is maximally atypical and would create
exponential comparison congestion. The proof must not be repurposed as a
canonical-path mixing proof. Its only quantitative statements are positivity
of individual transitions and the `m/2` square-refresh count after an
unquantified Hurwitz path.

## 7. Calibration

- odd `m`: state space empty by sign;
- `m=0`: singleton;
- `N=2`, even `m`: singleton;
- `m=2,N>=3`: multiple `(t,t)` states and no allowed update; excluded;
- `S_3,m=4`, `S_4,m=4`, `S_4,m=6`: consistent with the recorded one-component
  exact heat-bath graphs despite multiple pure-Hurwitz components;
- `m=4`: the proof explicitly uses whole-word `H_{1,4}` square refresh;
- near-minimal components: paired tree word has exactly `2(v-1)` factors;
- disjoint components: factors commute, but the proof uses Hurwitz moves to
  sort/interleave them and does not discard ordering;
- edge/degree parity: not used as a characterization;
- `L=2`: no simulation claim is made;
- canonical hub: used only for reachability, never for congestion.

## 8. Artifacts and reproduction commands

- `plan.md`
- `checkpoint.md`
- `proof.md`
- `report.md`

No computation was used.

## 9. Verdict

PROVED
