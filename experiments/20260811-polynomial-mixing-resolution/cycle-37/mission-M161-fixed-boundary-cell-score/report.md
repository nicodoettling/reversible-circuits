# M161 final report: exact first boundary-cell convolution

Date: 2026-08-13. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
VERDICT: EXACT FIXED-CELL CONVOLUTION REDUCTION.
BOUNDEDNESS/LIMIT OF A_k(1,1): UNRESOLVED.
```

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
For odd `k>=3`, `n=3k`, this report concerns only M73's nonlazy cyclic
rank-two quotient kernel under the uniform minimal factorization law of the
long cycle, at `A_k=(0,k,2k)` and `B_k=(0,1)(k,2k)`.  It proves no all-edge,
H0, bridge-gap, identity-heat-bath, or Terminal claim.

## 2. Exact proved reduction

For `1<=y<=n-3`, let

```text
t_y=(0,1)(1+y,2+y),
z_k(y)=[bar K^2(O_B,O_y)-bar K^2(O_A,O_y)]/bar pi(O_y).
```

The target complement has sizes `(1,1,n-2)`, so

```text
bar pi(O_y)=2n c_n b_1^2 b_(n-2)
```

is independent of `y`; also `O_y=O_(n-2-y)`.  For an intermediate `s`,
write the cycles of `s^-1h` as `C_i`, with ranks `r_i`, and let `E_r` be the
boundary edge `(r,r+1)`.  M73's exact four-schema formula specializes to

```text
bar K(O_s,O_y)=P_y^IS(s)+P_y^IN(s)+P_y^X(s),

P_y^X(s)=sum_(i!=j) 2r_i r_j/R_n
                    sum_(r mod n)N_i(r)N_j(r+y+1),

P_y^c(s)=sum_i r_i(r_i-1)/R_n
                    sum_(r mod n)M_i^c(r,y+1), c=IS,IN.
```

Here `N_i` is the exact conditioned-Borel first-boundary-edge weight in
`C_i`, and `M_i^c` is the exact same-cycle two-edge Cayley weight, including
literal double lift multiplicity and color.  Thus the cross term is a
circular correlation and the same-cycle terms are exact lag slices.

Substitution into M91's measure-valued Abel identity gives the complete
two-channel scalar convolution displayed as equation (3.3) in
`fixed_cell_convolution.md`.  Both channels, all triangle/double
intermediates, collisions, and lower-support strata are summed before
absolute value.  It proves exact reflection `z_k(y)=z_k(n-2-y)` and

```text
A_k(1,1)=1/(n-3) sum_y k^2|z_k(y)|.
```

## 3. Probability, multiplicity, and cancellation accounting

- The cyclic target orbit has literal size `n`; its two colored appearances
  at `y` and `n-2-y` are intentional.
- Triangle and double intermediate lift counts are respectively `3` and `2`.
- `IS`, `IN`, and `X` responses retain exact component-interleaving factors.
- The source contrast is the complete M91 `alpha_1,alpha_2` signed sum.
- No schemawise absolute value, bulk continuum limit, quotient-matrix build,
  or claim that triangles are a complete collision counterterm is used.

## 4. Dependencies and status labels

- **Accepted proved:** M73 exact quotient kernel/four schemas; M91 posterior
  and two-channel Abel identity; M94/M100 orbit-aware score; M102/M105
  collision warning; M155/M159 boundary-cell disintegration.
- **Proved here:** constant cell mass; exact circular-correlation formulas;
  exact reflection; exact scalar `(FCL1)` reduction.
- **Exact finite only:** `k=3,5,7` scores and schema decompositions.
- **Unresolved:** `(FCL1)`, boundedness/limit of `A_k(1,1)`, every further
  weighted cell, direct L1, all-edge/H0/gap/Terminal consequences.

## 5. First unproved standalone statement

> **FIXED-CELL L1 CORRELATION `(FCL1)`.**  With `Z_k(y)=kz_k(y)`, prove
> uniformly over odd `k>=3` that
>
> ```text
> sum_(y=1)^(3k-3)|Z_k(y)|=O(1).
> ```

By the exact identity above, `(FCL1)` is equivalent to boundedness of
`A_k(1,1)`.  If it holds, the next cells required by M155's weighted
product-Borel criterion are `(1,b)` for fixed `b>=2`, followed by a summable
joint envelope in `(a,b)` and finite-`n` tail control.  One bounded cell alone
does not prove direct L1.

## 6. Strongest self-attack

The circular-correlation formula is an identity, not a norm bound.  Its
`IS`, `IN`, and `X` pieces are individually much larger than the complete
score and cancel.  Exact positivity through `k=7` may fail later, and the
three decreasing values cannot establish a limit.  Consequently no
schemawise variation estimate or finite trend is promoted.

## 7. Exact falsification checks

`fixed_cell_exact.py` evaluates the raw M94 convolution directly, without a
quotient matrix, using `Fraction`.  It verifies zero inadmissible/crossing
nonzero terms, exact reflection, and full category reconstruction.  Results:

| `k` | `A_k(1,1)` | `Var(k z_k)` |
|---:|---:|---:|
| 3 | 1.5601664094 | .7072389201 |
| 5 | 1.0134604991 | .4421812930 |
| 7 | .8476179288 | .2480906028 |

All displayed `A` values are stored as exact rational numbers.  The table is
exact finite calibration only.

## 8. Artifacts, command, runtime, and hygiene

The deterministic standard-library command was

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-37/mission-M161-fixed-boundary-cell-score/fixed_cell_exact.py --k 3 5 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-37/mission-M161-fixed-boundary-cell-score/fixed_cell_results.json
```

Python `3.12.3`, `seed=null`, no nonstandard dependency.  The three ranks
took under twelve seconds total.  No package, network, commit, push,
predecessor, coordinator, manuscript, goal, or skill file was changed.

## 9. Final action

**KEEP THE EXACT REDUCTION; PRIORITIZE `(FCL1)`, THEN FIXED CELLS `(1,b)`.**
Fresh independent audit is required before promotion.
