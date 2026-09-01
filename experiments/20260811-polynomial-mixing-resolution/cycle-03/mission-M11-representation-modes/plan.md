# Cycle 03 M11 plan: representation modes of the exact bridge heat bath

## Exact target and conventions

The target is the uniform law on

```text
Omega(N,m)={t in T_N^m: t_1...t_m=id},
```

for `N>=3` and even `m>=4`.  Permutations are maps on `[N]`, `pq` means
`p` after `q`, and `X_j=t_1...t_j`.  The reviewed chain is

```text
K=(1/2)I+(1/(2|R_m|)) sum_{r in R_m} 1/(m-r+1) sum_i H_{i,r},
R_m={r in {3,4,5}:r<=m}.
```

Every formal Dirichlet calculation will retain the lazy factor, block-size
choice, window scan, and exact conditional-fiber law.  The ordinary random-
transposition convolution operator, the adjacent-pair bridge chain `J`, and
Hurwitz restrictions will never be identified with `K` without a proved
comparison in the correct direction.

## Program

1. Derive the exact bridge transfer formula for joint prefix observables
   `rho(X_j)` in an arbitrary irreducible `S_N` representation.  Express the
   action of a window heat bath through matrix-valued bridge kernels rather
   than only conjugacy-class marginals.
2. Audit the lowest modes: sign (expected to be deterministic by parity),
   standard and sign-twisted standard, character ratios, and spatial Fourier
   combinations over prefix location.  Remove constants and modes already
   explained by `O(1/m)` prefix locality.
3. Seek a closed invariant subspace or an exact Rayleigh-quotient identity
   for full `K`.  If closure fails, identify the representation multiplicity
   or conditional-fiber dependence responsible for failure.
4. Red-team a candidate slow mode only after accounting for every `r=3,4,5`
   window.  A slow mode of `J` or ordinary convolution is nonresponsive.
5. Use exact finite arithmetic only to falsify a named closure/eigenfunction
   lemma in the smallest decisive cases.  No spectrum grid.

## Candidate exact statements

- **Prefix-character closure:** determine whether the span of
  `chi_lambda(X_j)` over `j` is invariant under `K`, and if not give an exact
  counterexample.
- **Standard-mode Poincare:** bound the variance of linear standard-
  representation prefix observables by their full-`K` Dirichlet form with a
  universal polynomial constant.
- **Transfer multiplicity obstruction:** determine whether bridge endpoint
  conditioning couples matrix coefficients through Kronecker multiplicities
  in a way that rules out scalar Fourier diagonalization.

## Calibration and success boundary

Check the empty/singleton/excluded cases, the three exact smoke cases, the
whole-word `H_4` at `m=4`, sparse doubled-tree words, disjoint-component word
ordering, and all conditional-fiber normalizations.  Prefix locality alone
only gives a polynomial upper bound and is not a result of this mission.

A Terminal-B claim requires an explicit infinite family with
superpolynomially small full-`K` gap and complete stationary-mass/Dirichlet
accounting.  Otherwise the deliverable is the strongest rigorously closed
mode inequality or the exact first representation-theoretic obstruction.

## Deliverables

- `checkpoint.md`: a genuine exact operator lemma or decisive closure
  obstruction.
- any deterministic falsification script plus compact machine-readable
  output and commit/environment metadata.
- `report.md`: the required nine-field schema and exact verdict.
