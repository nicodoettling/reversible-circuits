# M03 plan: projection-gap audit and square down-up frontier

Date: 2026-08-11  
Repository commit at start: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## Objective

Freshly referee the frozen M02 coordinator bundle:

- exact macro-fiber weights;
- the full `r=3,4,5` stationary-flow projection formula;
- the fixed-first-slot square down-up kernel `S`;
- `D_N`, every action-rate normalization, and `bar K >= c_sq S`;
- irreducibility of `S` and the aligned nonlazy `r=4` chain `B`, including
  `m=4` and endpoint windows.

Only if those claims survive, seek an inverse-polynomial Poincare bound for
`S` by comparison with a partition/merge-split/down-up chain or an
authoritative high-dimensional-walk result.  Incorporate the M12 dense
threshold theorem once its final statement is available.  Do not use the
repeated-edge macro as a comparison hub.

## Target and conventions

The target is the global uniform law on

```text
Omega(N,m)={transposition words (t_1,...,t_m): t_1...t_m=e}.
```

Composition is `(pq)(x)=p(q(x))`.  The original kernel is

```text
K=(1/2)I+(1/(2|R_m|)) sum_{r in R_m}(1/(m-r+1))sum_i H_{i,r},
R_m={r in {3,4,5}:r<=m}.
```

`S` inspects positions 1 and 2, holds if they differ, and otherwise replaces
`(t,t)` by uniform `(s,s)`.  `B` is the nonlazy average of aligned length-four
heat baths.

## Exact falsification claims

For `(N,m)=(3,4),(4,4),(4,6)`, a deterministic exact harness will test:

1. identity-word counts `27,120,3936` and macro counts `4,13,17`;
2. observed macro-fiber sizes against
   `m! product_B C(|B|,k_B)/k_B!`;
3. row stochasticity and stationary detailed balance of the directly
   aggregated `bar K` for all `r=3,4,5` available;
4. direct projection of the word chain `R` against the common-core formula
   for `S`, including its diagonal and square-exposure probability;
5. the enumerated triple-fiber size against
   `D_N=(3N^2+N-12)/2`;
6. every off-diagonal inequality `bar K(alpha,beta)>=c_sq S(alpha,beta)`;
7. connectivity of `S` and `B`.

Any discrepancy falsifies the corresponding universal M02 formula.  Passing
these finite cases is calibration only and cannot prove the universal claims.

## Expected failure modes

- loss of a multinomial or label automorphism factor in `W_m`;
- double counting the deleted square core in `(3.2)`;
- treating off-fiber square-refresh mass as renormalized action rather than
  holding;
- omitting `|R_m|`, laziness, the `m-2` window count, or `D_N`;
- failing to cover an adjacent pair at the first or final aligned window;
- using polynomial diameter through a macro of exponentially small mass as
  a gap proof;
- confusing threshold-set conductance with arbitrary-cut conductance.

## Reproducibility

The harness will use Python 3.12, exact `fractions.Fraction` arithmetic, no
nonstandard packages, and no randomness.  No seed is needed.

