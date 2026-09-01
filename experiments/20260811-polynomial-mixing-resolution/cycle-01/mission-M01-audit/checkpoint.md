# Halfway checkpoint

The convention and endpoint audits find no defect in the frozen
irreducibility proof. Ben-Itzhak--Teicher Theorem 3.4 applies to identity
factorizations of equal length into transpositions, includes the fixed labeled
vertex set (hence isolated vertices), and uses

```text
(a,b) -> (aba^{-1},a),
```

which is the inverse of the project's
`(a,b)->(b,b^{-1}ab)`. Thus both generate the same equivalence relation.

The main apparent risk in the pair-chain comparison is also resolved. If an
`H_{j,2}` update sends `x` to a distinct `y`, equality of the old and new pair
products implies that neither coordinate of the pair can remain fixed.
Consequently the discrepancy set is exactly `{j,j+1}`. No different pair scan
can generate the same off-diagonal transition, so the displayed formula for
the full point probability `J(x,y)` is valid.

Exact enumeration of `S_3,m=4`, `S_4,m=4`, and `S_4,m=6` found respectively
27, 120, and 3936 states; one `K` component in each case; 4, 13, and 17 pure
Hurwitz components; normalized `K` and `J` rows; off-diagonal `J` scan
multiplicity one; no violation of the claimed `1/(3M^2)` pointwise floor; and
the exact adjacent-square insertion/deletion count at every position.

The remaining audit work is to freeze the symbolic argument, distinguish the
pair-padding comparison from the known *internal* `L=2` large-block warning,
and state the new smallest open implication without converting stationary
average square frequency into a worst-state estimate.
