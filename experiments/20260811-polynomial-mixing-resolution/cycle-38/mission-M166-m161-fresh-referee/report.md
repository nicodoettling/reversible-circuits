# M166 fresh immutable referee report on frozen M161

Date: 2026-08-13.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict and exact scope

```text
ACCEPT M161'S EXACT FIXED-BOUNDARY-CELL CONVOLUTION REDUCTION.
MATERIAL NUMBERED OBJECTIONS: ZERO.
NONMATERIAL NUMBERED OBJECTIONS: ONE (FINITE-DIAGNOSTIC LABEL ONLY).
```

The accepted target is only the uniform minimal length-`n-1`
factorization law of the odd long cycle and M73's nonlazy cyclic rank-two
quotient kernel, with `n=3k`, odd `k>=3`, at M161's balanced separated cell
`(1,y,1,n-2-y;S)`.  This is not the identity-word law or the lazy
`{3,4,5}` heat-bath chain.  The audit accepts no asymptotic `(FCL1)` bound,
fixed-cell limit, direct L1 theorem, all-edge estimate, H0 theorem, gap, or
Terminal conclusion.

## 2. Frozen provenance

All assigned M161 hashes independently match:

| M161 artifact | observed SHA-256 |
|---|---|
| `report.md` | `d7a4270525b307f86940cc07c0707a56c1086d489d45edfd96f1474a55dfe71e` |
| `fixed_cell_convolution.md` | `f7d5369f58cf1e0f2aa34caf237fdc907a4012f15b49d5cff1ea9d3465517d09` |
| `fixed_cell_exact.py` | `76dc00d59326f0a1aecad0f3aff16d4b421a95acd88553a5b92b02a620c5331d` |
| `fixed_cell_results.json` | `7295dcbf6cec4a6b1a0a8d67f09add532bbcf66f13e717f441899110df271e19` |
| `freeze_manifest.md` | `b6b366bab63493245abbf47c89cb6cfb14d40af56e9812a3227a6086f3af926d` |
| `SHA256SUMS` | `17bd62a9b121a10058f87c576275411186e1c3c5039fa07a9cf29c9bea7358d8` |

No M161 or predecessor artifact was modified.

## 3. Constant mass and intentional duplicate audit

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
For

```text
t_y=(0,1)(y+1,y+2),                 1<=y<=n-3,
```

the exact reconstruction finds residual cycle sizes `(1,1,n-2)` for every
`y`.  Therefore its raw marginal completion count, literal double lift
factor two, and free cyclic orbit size `n` give

```text
bar pi(O_y)=2n(n-3)! tau(n-2)/n^(n-2)
            =2n c_n b_1^2 b_(n-2),
```

independent of `y`.  The target orbit is free at both checked ranks.
Moreover, literal orbit enumeration proves

```text
O_y=O_(n-2-y).
```

Every physical orbit occurs exactly twice in the full colored `y` list:
three physical orbits among six appearances at `k=3`, and six among twelve
at `k=5`.  Thus M161's duplication is the required pair of separated
colored appearances, not a stabilizer or normalization error.

## 4. Independent literal phase-correlation reconstruction

The clean-room checker imports no predecessor code and builds no quotient
matrix.  It generates every admissible raw rank-two intermediate from all
literal ordered pairs of distinct transpositions.  Exact enumeration gives

| `k` | triangles, lift 3 | doubles, lift 2 | target phase checks |
|---:|---:|---:|---:|
| 3 | 84 | 252 | 18,144 |
| 5 | 455 | 2,730 | 573,300 |

For each intermediate residual `q=s^-1h`, each `y`, and every cyclic phase,
the checker compares the literal completion-count response

```text
2 F_(n-5)(t_y q)/F_(n-3)(q)
```

with an independently calculated response:

- if the two boundary edges lie in different residual cycles, the `X`
  value is `2r_i r_j/R_n` times the two exact one-chord Cayley weights;
- if they lie in one residual cycle, the `IS` or `IN` value is
  `r_i(r_i-1)/R_n` times the exact two-chord Cayley weight, including its
  literal factor two;
- inadmissible or crossing configurations have value zero.

All 591,444 rational equalities hold.  The final signed sum retains exactly
the six nonempty categories

```text
T_IS, T_IN, T_X, D_IS, D_IN, D_X.
```

Thus both intermediate kinds, all three second-row topologies, collisions,
and lower-support cases are combined before the absolute value.  This
independently validates M161 equations `(2.3)--(2.6)` as literal phase
correlations/lag slices and respects the M102/M105 topology warning.

## 5. Reflection, scaling, and finite checks

Exact target-orbit equality gives the mirror symmetry

```text
z_k(y)=z_k(n-2-y).
```

The independent complete signed score vectors agree entry-by-entry with
M161 at `k=3,5`.  In particular,

| `k` | exact `A_k(1,1)` | decimal |
|---:|---|---:|
| 3 | `22035419749493793/14123762450000000` | 1.560166409446641 |
| 5 | `365389626737269866778895542335238781797128038414977990550255/360536623837056962824358313261027674643802004279764627488768` | 1.013460499098716 |

Writing `Z_k(y)=kz_k(y)`, the exact normalization is

```text
A_k(1,1)=k/(n-3) sum_(y=1)^(n-3)|Z_k(y)|.
```

Since `n=3k`, the prefactor `k/(n-3)` lies between `1/3` and `1/2` for
odd `k>=3`.  Consequently `(FCL1)`, namely
`sum_y |Z_k(y)|=O(1)`, is exactly equivalent to uniform boundedness of
`A_k(1,1)`.  This is an equivalence of unresolved statements, not a proof of
either.  The two finite values cannot establish boundedness or a limit.

## 6. Numbered objections

1. **Nonmaterial: mislabeled finite diagnostic.**  M161 report Section 7
   labels its final table column `Var(k z_k)`.  The frozen implementation and
   JSON instead compute

   ```text
   k sum_y |z_k(y+1)-z_k(y)|,
   ```

   called `k_times_score_sequence_TV_float`; the displayed values
   `.7072389201`, `.4421812930`, and `.2480906028` are this sequence total
   variation, not a statistical variance.  The quantity is used nowhere in
   M161's proof, so this is a label correction only and changes no accepted
   identity, finite `A` value, or scope.

Material objections: **none**.

## 7. Status and hygiene

```text
constant fixed-cell mass and colored duplicate accounting       proved
literal IS/IN/X correlation and lag formulas                    proved
complete signed topology retention                              proved
mirror symmetry and A/FCL1 equivalence                           proved
finite k=3,5 calibrations                                        exact finite facts
(FCL1), boundedness/limit, direct L1, all-edge estimate          unresolved
H0, every gap, identity-chain mixing, and both Terminals         unresolved
```

M166 changed only its owned directory, used no network or nonstandard
package, and made no commit or push.  Its exact checker is deterministic
with `seed=null` under Python `3.12.3`.

**Final verdict: ACCEPT M161'S EXACT FIXED-BOUNDARY-CELL CONVOLUTION
REDUCTION WITH ZERO MATERIAL OBJECTIONS AND ONE NONMATERIAL DIAGNOSTIC-LABEL
CORRECTION; ALL ASYMPTOTIC L1, GAP, AND TERMINAL CLAIMS REMAIN OPEN.**
