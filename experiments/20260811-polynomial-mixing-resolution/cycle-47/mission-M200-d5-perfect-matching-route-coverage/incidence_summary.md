# M200 compact incidence summary

Date: 2026-08-13 UTC.

Let `q_0=16` be M181's `W_0=V` quotient point and `q_1=0` its
`W_(e_1)=U` quotient point. For each edit, the entries below give the matched
target `Q_5` ID at roots `0,1,2,3,4`, respectively.

| DPS edit | targets over `q_0=16` | targets over `q_1=0` |
|---:|---|---|
| 1 | `16,16,740,4526,3397` | `0,0,724,3312,3379` |
| 2 | `2460,725,726,725,2460` | `2444,741,758,2444,2444` |
| 3 | `16,740,16,791,102` | `0,724,0,58,132` |
| 4 | `155,155,155,155,155` | `107,107,217,433,107` |
| 5 | `4526,16,4526,16,4529` | `0,3312,58,0,4` |
| 6 | `15,15,15,15,15` | `6,6,6,11,44` |
| 7 | `16,3397,102,3397,16` | `0,3379,132,4,0` |

Thus the target pair for edit `i` and roots `(r_0,r_1)` is exactly

```text
(A_i[r_0], B_i[r_1]),
```

where `A_i,B_i` are the corresponding two table entries. The complete
175-row map from `(i,r_0,r_1)` to the deduplicated M196 target ID and its
quotient route certificate is in `incidence_table.json`.

M135 did not freeze a numerical `d=5` edge coloring. For any actual coloring,
each color selects one root above `q_0` and one root above `q_1`; hence its
paired target is one of these 175 rows. Labeling colors by their root over
`q_0`, the roots over `q_1` form a permutation `sigma_i`. The JSON records all
five possible `sigma_i(c)` values for all 35 normalized `(edit,color)` rows.
Every possibility is covered, so no arbitrary color choice is hidden.
