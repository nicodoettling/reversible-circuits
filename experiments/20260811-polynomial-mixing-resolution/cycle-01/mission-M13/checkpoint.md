# M13 Halfway Checkpoint

## Status at halfway

No literal TERMINAL B construction has survived. In particular, the
all-label connected-support fiber is not split by any of the candidate
statistics below: padded Hurwitz moves stay in the fiber, Classification H
makes their graph connected, and every specified padded Hurwitz move has only
inverse-polynomially small one-step probability under the exact `r=3` heat
bath.

The strongest exact reduction so far is the following. Let `F` be any fixed
labeled weighted-component fiber and let `K^F` be the restriction of the exact
kernel (exits are converted to holding). Let `P_H` be the lazy symmetric
random-scan Hurwitz walk: with probability `1/2` hold, and otherwise choose
one of the `2(m-1)` right/inverse generators uniformly. Writing
`M=binom(N,2)` and `B=|R_m|`, direct allocation of each adjacent Hurwitz move
to a containing length-three window gives

\[
  \mathcal E_{K^F}(f,f)
  \ge {m-1\over 2B(m-2)M^2}\,
      \mathcal E_{P_H}(f,f).
\]

The factor `M^2` is the elementary bound `F_3(h) <= M^2`: the first two
factors determine the third. The displayed constant includes the outer
laziness, block-size probability, random-window probability, and a safe
multiplicity factor of four when the two boundary adjacent pairs are assigned
to the same length-three window. A cleaner allocation may improve the
constant, but this one is sufficient and polynomial. The argument will be
written fully in the final report.

Consequences:

- a superpolynomially small restricted-fiber gap for `K^F` would force a
  superpolynomially small gap for this precise Hurwitz Schreier walk;
- no literal edge-multiplicity, degree-parity, doubled-tree, or midpoint-cycle
  invariant survives;
- the quantitative issue is collective expansion of a connected Hurwitz
  orbit, not a hidden component or an exponentially tiny individual move.

## Exact locality lemma

For the prefix endpoint `X_k=t_1...t_k`, only windows satisfying
`i <= k < i+r-1` can alter `X_k`. Hence the exact probability of even selecting
an eligible window is

\[
  a_{m,k}={1\over 2B}\sum_{r\in R_m}
       {c_{m,k,r}\over m-r+1},
\quad
 c_{m,k,r}=\max\{0,\min(k,m-r+1)-\max(1,k-r+2)+1\}.
\]

This is `O(1/m)` for an interior cut. For the first-factor event
`A_s={t_1=s}` in the all-label full-support fiber, conjugation symmetry gives
`pi_F(A_s)=1/M`, while only the unique window starting at position one can
change membership. Therefore the indicator Rayleigh quotient gives the
rigorous upper bound

\[
 \operatorname{gap}(K^F)
 \le {1\over 1-1/M}\,{1\over 2B}
       \sum_{r\in R_m}{1\over m-r+1}.
\]

This refutes any uniform constant-gap conjecture, but it is only polynomial
slowness and is not TERMINAL B.

## Scoped exact falsification

`exact_cut_audit.py` enumerated only the mandated smoke cases and computed
exact normalized flow for named cuts. It used no nonstandard dependencies and
no randomness (recorded seed `130013`). Assertions checked total/full-support
counts and reversibility of directed cut flow.

- `S_3,m=4`: 27 identity words, 24 all-label full-support words.
- `S_4,m=4`: 120 identity words, but the all-four-label connected fiber is
  empty, as required by `m < 2(N-1)`. The whole-word `r=4` update is included
  in the other `m=4` calculation.
- `S_4,m=6`: 3936 identity words, 2880 full-support words.
- Across 4,923,552 enumerated block outcomes for `S_4,m=6`, there were zero
  violations of prefix locality.
- At `S_4,m=6`, exact smaller-side conductance was approximately `0.15645`
  for the midpoint-distance/mountain cut, `0.24719` or larger for all
  distinct-edge thresholds, and `0.27601` for the aligned doubled-tree family.
  These reject those finite candidate cuts only; they are not asymptotic
  evidence.
- Explicit positive-probability one-step witnesses change midpoint distance,
  distinct-edge count, edge-multiplicity parity, vertex-degree parity, and
  leave the aligned doubled-tree family while remaining full support.

Artifacts:

- `exact_cut_audit.py`
- `results.json`

Exact command:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M13/exact_cut_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M13/results.json --seed 130013 --commit 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
```

## Current smallest open proposition

**Uniform connected Hurwitz-orbit gap.** There is a polynomial `q(N,m)` such
that, for every `N>=3`, every even `m>=4`, and every feasible labeled weighted
support-component fiber, the lazy symmetric random-scan right/inverse Hurwitz
walk defined above has spectral gap at least `1/q(N,m)`.

For this M13 lane the sharp adversarial version is: construct an explicit
full-support family violating this proposition, with a cut of exactly
controlled conditional mass and flow. The second half of the mission attacks
that proposition through prefix geometry and minimal-factorization families,
and separately checks whether the proposed mean-lift inequality is even the
right formulation.
