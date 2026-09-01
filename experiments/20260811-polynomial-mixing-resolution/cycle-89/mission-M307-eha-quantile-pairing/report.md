# M307 report: canonical quantile cells do not sign MCLP

Date: 2026-08-14 UTC.

## Verdict

```text
KEEP THE EXACT MIXED-SIGN QUANTILE TRANSPORT IDENTITY QTI_1.
REJECT THE PREDECLARED CELLWISE QUANTILE PAIRING QCP_1.

MCLP_1 AND GOCI_1 REMAIN UNRESOLVED.
GOCI_2, OCI/CP, OS+, MS, FCL1, GAP, MIXING, AND TERMINALS
REMAIN UNRESOLVED.
```

This mission concerns only channel one in the first separated fixed cell of
the auxiliary minimal long-cycle factorization law.  It is not a theorem
about the global uniform identity-word target or the lazy exact same-product
`{3,4,5}` heat-bath chain.

## 1. Exact analytic result

For the accepted all-middle exterior cut masses, define the canonical
increasing quantile coupling

```text
pi_cd=|(sum_(i<c)x_i,sum_(i<=c)x_i]
        intersect
       (sum_(j<d)y_j,sum_(j<=d)y_j]|.
```

Equal positive and negative Hahn mass makes its row sums `x_c` and column
sums `y_d`.  Therefore exactly

```text
P_(k,ell)(u)=sum_(c,d)pi_cd(Xbar_c-Ybar_d).          (QTI_1)
```

The accepted `R_c` equals the difference of the two cumulative cut masses.
Negative `R_c` forces transport cells below one side of the cut diagonal;
positive `R_c` forces cells on the other side.  Hence QTI_1 preserves the
mixed Abel signs instead of assuming a common monotone direction.

The frozen sufficient candidate was

```text
QCP_1: Xbar_c>=Ybar_d on every cell with pi_cd>0.
```

It acts only after all middle phases have been summed and is distinct from
the already-refuted fixed-middle, MON/FOSD, raw-atom, and signed-PSD routes.

## 2. Exact obstruction at the sole new rank

The exact standard-library `k=9`, `n=27` guard finds the first supported
failure at

```text
(u,ell,c,d)=(1,2,2,2),
pi_22>0,
Xbar_2-Ybar_2 approximately -2.871982675510025.
```

The full rational witness is equation `(5.1)` of `proof.md` and is recorded
machine-readably in `qcp_k9.json`.  This exactly refutes universal QCP_1.

The failure is pervasive: 778 of 1,440 supported cells are negative, and
all 96 middle-class/lag rows contain a negative cell.  The counts by middle
class are `204,188,192,194`.  The rank's cumulative signs are

```text
R_1,...,R_4<0;  R_5,...,R_7>0;  R_8=0,
```

so the test retains the intended mixed-sign geometry.

## 3. What survives

Every one of the 96 complete MCLP aggregates at `k=9` is strictly positive.
The minimum is at `u=2`, reflected lags `ell=8,19`, approximately
`0.0997997722412562`.  Thus negative quantile cells are compensated by
other cells in every tested row.

This finite survival is not an all-rank MCLP theorem.  The exact conclusion
is only:

```text
cellwise canonical quantile ordering is false;
any QTI_1 proof must retain multi-cell cancellation.
```

Per the mission cap, no weaker row/block pairing was searched.

## 4. Claim ledger

| claim | status | evidence | action |
|---|---|---|---|
| M300/M303 source locks | verified | top and per-file hashes | retain; note nonmaterial 15/14 count typo |
| quantile marginals and QTI_1 | proved | interval-partition argument | keep for fresh audit |
| mixed-`R_c` support interpretation | proved | cumulative mass intervals | retain |
| universal QCP_1 | refuted | exact `(1,2,2,2)` witness | do not reuse |
| 778/1440 negative QCP cells | exact finite only | `qcp_k9.json` | cancellation warning |
| 96/96 positive MCLP cells | exact finite only | same artifact | do not extrapolate |
| MCLP_1 / GOCI_1 | unresolved | QCP false; finite aggregate positive | remain open |
| GOCI_2 / OCI/CP / OS+ / MS / FCL1 | unresolved | out of proved scope | no inference |
| gap / mixing / Terminals | unresolved | out of scope | no inference |

## 5. Final action

**Freeze QTI_1 and the exact QCP_1 obstruction for fresh immutable audit.**
Do not replace QCP by an untested weaker grouping in this mission.
