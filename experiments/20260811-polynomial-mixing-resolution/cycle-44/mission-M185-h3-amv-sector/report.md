# M185 final report: fresh actual-history `h=3` AMV sector

Date: 2026-08-13 UTC.

## 1. Verdict

```text
FINAL VERDICT: PROMOTE STRICT STANDALONE REDUCTION WITH FRESH REFEREE.
PROVED: exact 3x3 branch and universal branch charge <=(3/4) child trace.
REFUTED: the proposed 2/3 matrix factor and the Sbar<=1 envelope route.
OPEN: coupled observation-dependent suffix-two trace aggregation.
```

## 2. Target, law, and convention

The project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors
left-to-right.  This mission concerns only the normalized full unweighted
reset excursion `F=H/q` in the auxiliary nonlazy minimal-long-cycle parking
projection, and only fresh retained descendants of last-root height `h=3`.

## 3. Precise proved statement

At a fresh parent `xi=(B+L,2,1,B)`, a retained height-three observation
`0<=a<d` has child

```text
(B+2,d+2,a+1,B),       Beta(a+1,d-a+1).
```

Its complete feature has three Jacobi modes.  If `A_i` are their
Hilbert-valued coefficients and `S_a=sum_i||A_i||^2`, the exact branch is

```text
B_(d,a)=sum_(i,j=0)^2
 [E_child(L_a e_i e_j)-12 pi_a z_i z_j]<A_i,A_j>,
z=(p-1/2,sqrt(v),0),       pi_a=1/(d+1).
```

Every likelihood-weighted cross term is present, and the killed `a=d` is
absent.  Universally,

```text
B_(d,a)<=(3/4)S_a.
```

The proof uses Vandermonde Loewner domination followed by exact Sylvester
minors: a positive first minor, a concave quadratic with positive endpoints,
and a cubic with four coefficient-positive Bernstein coefficients on
`0<=t^2<=d^2`.

## 4. Exact objections and falsification attempts

1. **Rejected constant `2/3`.** At `(d,a)=(20,0)`,
   `det((2/3)I-G)=-1731224299/244943654967<0`.  This is an exact universal
   counterexample to that Loewner factor.
2. **Rejected trace-envelope cap one.** The direct actual-history suffix-two
   trace envelope is
   `Sbar=R_2+D_0+(2/3)W_1`.  At `(B,d,a)=(3,20,19)`, it equals
   `10249528643/7684875000>1`.  This refutes the proposed proof route, not an
   unknown sharper inequality for the exact child trace.
3. **No diagonal shortcut.** The branch matrix keeps all three off-diagonal
   entries; its covariance subtraction keeps the constant/linear cross term.
4. **No scalar substitution.** M117's envelope controls scalar `F=H/q`, not
   the full trace used in the matrix comparison, and was not substituted for
   it.

## 5. Actual-history trace reduction

Direct history support accounting reconstructs the reset coordinates of
`(1,1,B)`, `(2,B)`, and `(1,B+1)`, both retained height-one observations,
and the likelihood-weighted unary height-two child.  With the notation in
`h3_reduction.md`,

```text
S_a <= R_2+D_0+(2/3)W_1.
```

This is an actual-history-only envelope, not a generic operator, Jensen,
finite-summary, diagonal, or scalar-`T_1` bound.  Its observation dependence
must remain coupled to the branch matrix in the next mission.

## 6. Exterior and boundary audit

For `n=L-3`, `r=d-1`,

```text
eta^(3)_(n,r)=(3/2)c(n,r)/[(r+1)!w_(n+4)].
```

The separate `n=0` boundary has only `r=0,d=1` and `eta=9/16`.  For
`n>=1`, the sum includes `r=n` and satisfies

```text
sum_r(r+1)eta
=(3/2)(n+1)^n(n+2)(n+3)/(n+4)^(n+2).
```

At `B=1`, inactive rank-one targets are removed from the exact history; the
displayed trace formula only retains extra nonnegative nominal terms and is
therefore still an envelope.  No complete aggregate sector constant is
claimed.

## 7. Dependencies and status labels

- **Proved here:** exact Bayes-normalized 3x3 formula, `2/3` counterexample,
  universal `3/4` Loewner bound, trace-envelope obstruction, exterior.
- **Accepted dependencies:** M109/M114, M115/M116, M117/M121, M147/M151,
  M157/M160, M162/M165, M173/M177, and M179/M184.
- **Unresolved:** the coupled observation/degree trace aggregate and hence a
  complete `h=3` sector budget.
- **Out of scope:** reset, `h>=4`, all suffixes, ROOT-MEAN, any gap,
  original-chain mixing, Terminal A, and Terminal B.

## 8. Exact diagnostics and reproducibility

```text
command      | python3 -B h3_exact.py --output h3_exact.json
arithmetic   | Python standard-library Fraction
parameters   | named matrix rows (20,0),(50,0),(1,0);
             | named trace rows (3,20,19),(2,1,0),(1,1,0)
random seed  | null
imports      | no predecessor imports; standard library only
```

Finite rows audit formulas and exact obstructions.  The analytic minor
certificate in `h3_reduction.md` proves the universal `3/4` theorem.

## 9. Handoff, scope table, and fresh audit request

```text
candidate                  | fresh actual-history h=3 retained sector
claimed target             | exact branch reduction, not total AMV budget
identity ok                | not a sampler-generation claim
crosses Hurwitz components | not applicable to this quotient operator
exact diagnostics          | rational branch determinants and trace rows
verdict                    | strict reduction; coupled trace lemma remains
```

First open lemma: for each `d`, aggregate `G_(d,a)` against the actual
suffix-two history constraints over exactly `a<d`, then sum the resulting
degree-dependent charge against the exact exterior, with `n=0` separate.

Request an immutable fresh referee to rederive the degree-two collapse,
Bayes normalization, all 3x3 cross terms, killed observation, `2/3`
counterexample, `3/4` Sylvester certificate, trace reconstruction and its
`>1` row, plus `B=1`, `n=0`, and `r=n` boundaries.  The referee must make no
inference about reset, `h>=4`, all `L`, a gap, or either terminal.
