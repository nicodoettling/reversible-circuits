# Independent referee report: M05 shuttle comparison

Date: 2026-08-11  
Frozen bundle: `cycle-03/mission-M05-shuttle-comparison/{plan,checkpoint,report}.md`

## 1. Frozen claim

Use `(pq)(x)=p(q(x))`, evaluate words as `t_1...t_m`, and let

```text
P_H^alpha=I/2+[1/(4(m-1))]sum_i(R_i+R_i^-1),
delta=min(1,min_a gap(P_a)),
M=binom(N,2), B=|R_m|.
```

The frozen claim is that for every `N>=3`, even `m>=4`, and feasible macro
datum `alpha`,

```text
gap(P_H^alpha)>=delta/m^10,                              (1.1)
gap(K^alpha)>=(m-1)delta/[2B(m-2)M^2m^10].              (1.2)
```

I independently **ACCEPT** both inequalities.

## 2. Full audit

The uniform macro law is exactly the product of the uniform color-word law
and uniform connected-factorization coordinate laws.  For

```text
P_*=(Q_col+sum_a P_a)/(q+1),
```

the coordinate Poincare decomposition gives

```text
gap(P_*)>=min(gamma_col,min_a gamma_a)/(q+1).
```

Here the audited half-lazy adjacent-multiset gap is
`gamma_col=[1-cos(pi/m)]/(m-1)>=2/m^3`.  Since `q+1<=m`, this proves
`gap(P_*)>=2delta/m^4` with the stated singleton conventions.

For consecutive internal `a`-factors at original physical positions `u<v`,
both orientations of

```text
R_u,...,R_(v-2), R_(v-1)^epsilon, R_(v-2),...,R_u
```

are correct.  Outer moves swap disjoint-support factors; the middle move is
the requested internal generator; the return restores the original color
word.  The path length is `2(v-u-1)+1<=2m-3`.

The recovery argument is genuinely injective.  With fixed metadata
`mu=(a,u,v,epsilon,s)`, the pre-edge prefix is a fixed composition `F_mu` of
bijections.  If the directed used edge has tail `w`, its source must be
`F_mu^-1(w)`.  Therefore two different sources cannot share both the same
directed edge and metadata.  The internal index is recovered as the rank of
`u` among the source's `a`-positions.

Repeated colors, duplicate right/inverse outputs, and a physical edge used
at multiple phases do not invalidate this: they change or duplicate metadata
values and are charged separately.  A central generator self-loop has zero
Dirichlet energy and needs no path.  Outer shuttle steps cannot be self-loops,
because their transpositions lie in disjoint positive components and are
distinct.

The direct color load is also correct.  Two different unequal adjacent swaps
from one color word cannot have the same target (compare the first changed
position).  The ideal probability after mixing is
`1/[2(q+1)(m-1)]`, while the two physical Hurwitz orientations aggregate to
`1/[2(m-1)]`; the direct load is at most `1/(q+1)`.

Finally, I re-read the original padded-H3 comparison.  The factor four is the
maximum number of assigned oriented adjacent generators in one boundary-safe
length-three window.  The relevant Dirichlet coefficients are

```text
1/[16B(m-2)M^2]    for K^alpha,
1/[8(m-1)]         for P_H^alpha,
```

so their ratio is exactly `(m-1)/[2B(m-2)M^2]`.  Rejected exits are held and
do not remove any assigned within-macro output.

## 3. Probability, paths, congestion, and runtime

- Product internal labeled flow:
  `pi_alpha/[4(q+1)(k_a-1)]<=pi_alpha/8`.
- Physical oriented-generator capacity:
  at least `pi_alpha/[4(m-1)]` for every used directed edge.
- Metadata count:
  `q binom(m,2)2(2m-3)<m^4`.
- Shuttle length: at most `2m-3`.
- Internal congestion: below `m^6`.
- Direct color congestion: at most `1/(q+1)`.
- Total comparison congestion: at most `2m^6`.
- Hence `gap(P_H^alpha)>=2delta/m^4/(2m^6)=delta/m^10`.
- The exact H3 transfer factor is
  `(m-1)/[2B(m-2)M^2]`, yielding (1.2).
- Constructing a path takes `O(m)` Hurwitz operations.  Exact block sampling
  remains polynomial; the crude fixed-`r` enumeration is at most `M^4`.

The deterministic falsifier ran the four cases `(3,4),(4,4),(4,6),(5,6)`
in 9.1 seconds under CPython 3.12.3.  It checked 190,620 off-diagonal shuttle
paths and 203,580 used-edge occurrences, with zero recovery collisions and
zero path failures.  The computation is finite calibration, not the proof.

## 4. Dependencies

- **Proved in the frozen bundle and independently accepted here:** product
  comparison, both shuttle orientations, recovery injection, congestion,
  direct color load, and final arithmetic.
- **Previously proved, independently re-audited here:** the exact
  K-to-full-Hurwitz H3 comparison and its rejected-exit convention.
- **Previously proved/cited:** the exact macro product law; adjacent-color
  gap; Ben-Itzhak--Teicher identity-factorization transitivity for each
  connected coordinate.
- **Conditional:** the numerical value of `delta` remains uncontrolled
  uniformly because the connected-Hurwitz gap theorem is open.
- **Empirical:** only the finite exact falsifier; no empirical input enters
  the accepted proof.

## 5. First open standalone step

Prove universal `c>0,C<infinity` such that, for every `v>=2` and every even
`k>=2(v-1)`, the half-lazy random-scan right/inverse Hurwitz chain on
connected-support identity transposition factorizations satisfies

```text
gap(P_H^{v,k})>=c(vk)^(-C).
```

The accepted shuttle theorem then supplies the fixed-macro-fiber comparison;
it does not close the global projection/decomposition obligations.

## 6. Strongest self-attack

The recovery proof would fail if its prefix depended on unrecorded state
data, but it does not: positions, orientation, and stage fix the entire map
sequence.  The most dangerous real issue was aggregation—several labeled
commodities can use the same physical state-pair edge.  The exact harness
observed this (up to four metadata occurrences on one edge), and the proof's
`m^4` metadata sum explicitly pays for it.  Thus the proof never assumes
unique generator output or unique edge usage.

This remains a one-way comparison.  If a connected Hurwitz coordinate is
slow, the exact heat bath may still mix quickly through `H_4,H_5`; the
accepted result cannot be reversed.

## 7. Calibration

- Odd `m` is empty; `m=0`, `N=2`, and singleton macro spaces use the stated
  gap convention; `m=2` is excluded from the H3 transfer.
- The harness reproduced `27`, `120`, and `3936` identity words for
  `S_3,m=4`, `S_4,m=4`, and `S_4,m=6`.
- At `m=4`, `B=2` and the transfer coefficient is `3/(8M^2)`; the whole-word
  `H_4` update remains in `K` and is merely unused.
- `k_a=2` and all other singleton internal coordinates are harmless;
  one-color macros have shuttle distance zero.
- Rare colors and endpoints create no missing generator indices.
- Near-minimal doubled-tree words require no square or surplus; all their
  difficulty is retained in `delta`.
- For `(ABBBBB)^4`, consecutive `A` positions are six apart and the proof
  uses the advertised eleven-edge shuttle, regardless of the repeated `B`
  colors.
- No length-two heat-bath simulation or canonical hub is used.  The known
  exact-color restriction obstruction is bypassed because the shuttle leaves
  and restores that color word.

## 8. Artifacts and reproduction

Owned referee artifacts:

```text
cycle-03/mission-M05-referee/plan.md
cycle-03/mission-M05-referee/checkpoint.md
cycle-03/mission-M05-referee/report.md
cycle-03/mission-M05-referee/shuttle_recovery_audit.py
cycle-03/mission-M05-referee/results.json
```

Reproduce with:

```bash
cd experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M05-referee
python3 shuttle_recovery_audit.py --output results.json
```

The run is deterministic and has no seed or nonstandard dependency.

## 9. Verdict and objections

**ACCEPT**

Numbered objections: none.

This accepts only the frozen partial comparison theorem, not the global
polynomial-mixing goal.

