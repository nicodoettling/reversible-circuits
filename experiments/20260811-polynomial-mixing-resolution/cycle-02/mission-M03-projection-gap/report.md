# M03 final report: projection-gap audit

Date: 2026-08-11  
Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## 1. Exact claim with all quantifiers and conventions

Permutations compose by `(pq)(x)=p(q(x))`; a word is evaluated in displayed
order.  Put `M=binom(N,2)` and

```text
K=(1/2)I+(1/(2|R_m|)) sum_{r in R_m}(1/(m-r+1))sum_i H_{i,r},
R_m={r in {3,4,5}:r<=m}.
```

The following claims are **proved**.

1. For every `N>=3` and even `m>=4`, the frozen M02 macro weights, full
   `r=3,4,5` stationary-flow projection, fixed-slot square chain `S`, formula
   `D_N=(3N^2+N-12)/2`, comparison
   `E_barK>=c_sq E_S` with
   `c_sq>=1/[24(m-2)]`, and qualitative `S`/aligned-`B` connectivity formulas
   are correct, with the classification dependency exactly as stated in M02.

2. For every `N>=3` and even `m` satisfying
   `m-2>=4M log(2N)`, the exact-support-partition projection `Pi` of `S`
   satisfies

   ```text
   Phi(Pi)>=3/(16M^2),
   gap(Pi)>=9/(512M^4).
   ```

   This is an arbitrary-cut theorem.

3. For every exact support partition `P`, the rejected-exit restriction of
   `S` is exactly the allocation chain (3.3) in `proof.md`.  For every
   nonsingleton restriction with `q` nontrivial blocks,

   ```text
   gap(S_P)>=q gap(Z_P)/[M m(m-1)],
   ```

   where `Z_P` is a uniform-destination complete-graph zero-range process
   with the same conditional product stationary law.

The global square gap is not proved.  A sufficient remaining proposition is
HURWITZ-RATE-CURVATURE in field 5.

## 2. Full argument or construction

The complete derivation is in `proof.md`.  Its logical chain is:

1. Count each macro fiber by independent connected component words and their
   color interleavings.  Aggregate the exact heat baths to obtain the full
   macro transition formula.  Project the fixed-first-pair square refresh to
   the common-core formula.  Enumerate the length-three fiber by its third
   transposition, giving `D_N`, and compare each specified square output to
   its exact `H_3` output.

2. In the dense regime, use M12's target-wise parent-map estimate
   `sum_{C:F(C)=P}nu(C)<=q_N nu(P)`, `q_N<=1/4`.  The full-support root has
   mass at least `3/4`; every descendant subtree has mass at most `4/3` times
   its top mass.  A fixed-slot internal-square injection and refresh to a
   chosen crossing edge gives every parent edge probability at least
   `1/(4M^2)`.  Decompose an arbitrary set of mass at most `1/2` into its
   rooted-tree components and sum their distinct top boundary edges.  This
   yields conductance `3/(16M^2)` and Cheeger gives the gap.

3. Within fixed `P`, write every component length as
   `2(v_i-1)+2g_i`.  The common-core formula shows that a distinct
   within-`P` square move transfers exactly one surplus unit.  Its exact rate
   is

   ```text
   binom(v_i,2)binom(v_j,2) rho_{v_i}(g_i)/[M m(m-1)].
   ```

   Comparing edge by edge to a uniform-destination zero-range chain loses
   only `M m(m-1)/q`.  Boudou et al. then converts a uniform lower bound on
   `rho_v(g+1)-rho_v(g)` into a gap.  M12/DYZ already proves
   `rho_v(g)>=12/v^3`, so a vanishing action rate is not the remaining issue.

4. `S` and its projections/restrictions are positive semidefinite.  JSTV
   therefore gives, in the dense regime,

   ```text
   gap(S)>=9 lambda_alloc/(2048M^4),
   gap(barK)>=9 lambda_alloc/[49152(m-2)M^4].
   ```

No inference from finite spectra is used.

## 3. Worst-case probability, runtime, path length, and congestion accounting

Exact one-step quantities:

- a specified local square output through `H_{1,3}` has probability
  `1/[2|R_m|(m-2)D_N]`;
- the `K`-to-`S` action factor is exactly
  `M/[2|R_m|(m-2)D_N]`;
- a dense parent-partition edge under `S` has probability at least
  `1/(4M^2)`;
- a fixed-partition surplus transfer has exact probability (3.3) of
  `proof.md`;
- the direct zero-range Dirichlet comparison loses at most
  `M m(m-1)/q`;
- JSTV loses a factor at most four for this decomposition.

The dense proof uses one-step edges only.  There are no comparison paths,
path lengths, vertex loads, or edge-congestion factors, and no canonical hub.

The exact M02 harness is intentionally exponential and is not a proposed
sampler: its crude state enumeration is bounded by `M^m`, and the largest
case has 3936 identity words.  On Python 3.12.3 it took 31.33 seconds wall
time for all three cases.  The rate harness uses dynamic programming on at
most `v! 2^M` permutation/support-mask states per length, with at most `M`
extensions per state; its declared run through `v=5,g=6` took about eight
seconds.  Both are deterministic, so no seed is applicable.

## 4. Dependencies

- **Proved in this bundle:** exact fixed-partition formula; direct uniform
  zero-range comparison; dense arbitrary-cut parent-tree conductance; PSD and
  JSTV `/4` bookkeeping; exact small-case falsification results.
- **Proved, inherited and audited:** macro-fiber factorization; connected
  component feasibility; exact heat-bath reversibility; Ben-Itzhak--Teicher
  classification translation used only for qualitative aligned-`B`
  connectivity.
- **Proved in frozen M12 artifacts:** dense trace bounds, target-wise child
  mass `q_N<=1/4`, root mass `>=3/4`, and the DYZ ratio deduction
  `rho_v(g)>=12/v^3`.
- **Cited with checked hypotheses:** JSTV Theorem 1; Boudou et al. Theorem
  4.2, generator (4.2), condition (4.11); Hermon--Salez Theorem 2 and its
  doubly-stochastic corollary; Gaudilliere--Reygner Theorems 1--2; Anari et
  al. Theorem 1.1; Alev--Lau Theorem 1.5.
- **Conditional:** HURWITZ-RATE-CURVATURE.
- **Empirical only:** positive `rho` increments through `v<=5,g<=5`.
- **Refuted:** ultra-log-concavity of all `a_v`; the exact counterexample is
  `v=4,g=1`.  Also refuted is strong log-concavity of the natural bilinear
  common-core incidence polynomial in all three calibration cases.

## 5. First unproved standalone proposition

**HURWITZ-RATE-CURVATURE.**  There exist universal constants `c_0>0` and
`A<infinity` such that, for every integer `v>=2` and `g>=0`, if

```text
a_v(g)=C(v,2(v-1)+2g)/[2(v-1)+2g]!,
rho_v(0)=0,
rho_v(g)=a_v(g-1)/a_v(g)  (g>=1),
```

then

```text
rho_v(g+1)-rho_v(g)>=c_0(v+g+1)^(-A).
```

M12 proves this at `g=0` up to the stronger bound `12/v^3`; the proposition
is open for `g>=1`.  A direct inverse-polynomial Poincare theorem for the
exact allocation chain would also suffice and could remain true if this
particular curvature proposition fails.

## 6. Strongest self-attack

The finite increase of `rho_v` may be misleading.  Ultra-log-concavity, the
most convenient all-genus shape theorem, already fails at `v=4`; nothing in
the positive DYZ recurrence currently prevents a later very small or
negative increment.  The unconditional lower bound on `rho_v(g)` controls
action frequency but does not rule out a multimodal conditional product
measure or a low-conductance allocation cut.  Therefore (3.10) alone cannot
be promoted to a gap theorem.

The dense parent-tree theorem critically uses M12's **target-wise** child
mass bound, not merely a layer ratio.  I checked that its parent map includes
isolates and has a unique full-support root.  If only the summed layer bound
were available, the arbitrary-cut proof would fail.

Even a proof of HURWITZ-RATE-CURVATURE would settle only the dense square
macro chain.  Sparse/intermediate `m` and word-level restrictions within
weighted macro fibers remain separate nonterminal obligations.  Hence this
report is not TERMINAL A.

## 7. Calibration results

- odd `m`: empty; no claim made;
- `m=0` and `N=2` with even `m`: singleton calibrations;
- `m=2,N>=3`: excluded and disconnected;
- exact `(words,macros)` are `(27,4)`, `(120,13)`, `(3936,17)` in the three
  required cases;
- for `m=4`, aligned `B` is the whole-word `r=4` heat bath; independently,
  its occurrence in `K` gives `gap(K_{N,4})>=1/4`;
- doubled-tree/minimal connected words have `G=0`, hence singleton
  allocation restrictions;
- disjoint-component color interleavings are included in `W_m`;
- no edge-multiplicity or degree-parity characterization is assumed;
- the known `L=2` simulation failure is not used;
- the repeated-edge macro is used only to falsify a component-count
  restriction decomposition, never as a hub;
- all asymptotic cut statements include exact stationary mass and boundary
  flow.

The exact harness additionally found:

| case | `D_N` | `c_sq` | `S` connected | `B` connected |
|---|---:|---:|---|---|
| `S_3,m=4` | 9 | `1/24` | yes | yes |
| `S_4,m=4` | 20 | `3/80` | yes | yes |
| `S_4,m=6` | 20 | `1/80` | yes | yes |

All row, detailed-balance, macro-weight, common-core, and comparison error
lists are empty in `results.json`.

## 8. Artifacts, reproduction commands, and exact citations

Artifacts in this directory:

- `plan.md`
- `checkpoint.md`
- `proof.md`
- `audit_m02.py`
- `results.json`
- `hurwitz_rate_audit.py`
- `hurwitz_rate_results.json`
- `report.md`

Reproduce from the repository root:

```bash
cd experiments/20260811-polynomial-mixing-resolution/cycle-02/mission-M03-projection-gap
python3 audit_m02.py --output results.json
python3 hurwitz_rate_audit.py --max-v 5 --max-g 6 --output hurwitz_rate_results.json
python3 -m compileall audit_m02.py hurwitz_rate_audit.py
```

No nonstandard Python packages and no randomness are used.

Primary citations:

- M. Jerrum, J.-B. Son, P. Tetali, E. Vigoda, *Elementary bounds on
  Poincare and log-Sobolev constants for decomposable Markov chains*,
  Theorem 1, equations (3)--(5),
  [arXiv:math/0503537](https://arxiv.org/abs/math/0503537),
  [DOI 10.1214/105051604000000639](https://doi.org/10.1214/105051604000000639).
- A.-S. Boudou, P. Caputo, P. Dai Pra, G. Posta, *Spectral gap estimates for
  interacting particle systems via a Bochner-type identity*, Theorem 4.2,
  generator (4.2), condition (4.11),
  [arXiv:math/0505533](https://arxiv.org/abs/math/0505533),
  [DOI 10.1016/j.jfa.2005.07.012](https://doi.org/10.1016/j.jfa.2005.07.012).
- J. Hermon, J. Salez, *A version of Aldous' spectral-gap conjecture for the
  zero range process*, Theorem 2 and Corollaries 3--4,
  [arXiv:1808.00325](https://arxiv.org/abs/1808.00325),
  [DOI 10.1214/18-AAP1449](https://doi.org/10.1214/18-AAP1449).
- A. Gaudilliere, J. Reygner, *Sampling the Fermi statistics and other
  conditional product measures*, Theorems 1--2,
  [arXiv:0911.4565](https://arxiv.org/abs/0911.4565),
  [DOI 10.1214/10-AIHP385](https://doi.org/10.1214/10-AIHP385).
- B. Dubrovin, D. Yang, D. Zagier, *Classical Hurwitz numbers and related
  combinatorics*, Proposition 1, equation (13),
  [primary PDF](https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf).
- N. Anari, K. Liu, S. Oveis Gharan, C. Vinzant, *Log-concave polynomials II*,
  Theorem 1.1, [arXiv:1811.01816](https://arxiv.org/abs/1811.01816).
- V. L. Alev, L. C. Lau, *Improved Analysis of Higher Order Random Walks and
  Applications*, Theorem 1.5,
  [arXiv:2001.02827](https://arxiv.org/abs/2001.02827),
  [DOI 10.1145/3357713.3384317](https://doi.org/10.1145/3357713.3384317).
- P. Diaconis, E. Mayer-Wolf, O. Zeitouni, M. Zerner, *The Poisson--Dirichlet
  law is the unique invariant distribution for uniform split--merge
  transformations*, [arXiv:math/0305313](https://arxiv.org/abs/math/0305313),
  [DOI 10.1214/aop/1079021468](https://doi.org/10.1214/aop/1079021468).

## 9. Verdict

OPEN AT A NAMED STEP: HURWITZ-RATE-CURVATURE
