# M227 checkpoint

Date: 2026-08-13 UTC.
Status: exact certificate search complete; freeze in progress.

The required source lock is complete: all six immutable predecessor ledgers
have the expected digests and every payload passes. The exact explicit atom,
first-Jacobi compression cost, and primal/dual programs are fixed in `plan.md`
before numerical or exact certificate search begins.

The standalone clean-room checker now reconstructs the degree-six charge
matrix and atom without importing predecessor code or data. Exact rational
primal and dual matrices, certified positive definite by complete Fraction
`LDL^T` pivot lists, prove

```text
60650731/180180000 <= p_1 <= 1136822741/3363360000,
167478197/630630000 <= p_2 <= 894863807/3363360000.
```

Consequently `p_1>p_2>1/4`, with exact positive separations. Here `1/4` is
the raw atom charge. Numerical SDP was used only to locate rational matrices;
no numerical value or unproved algebraic optimum is promoted. The exact
optima and any degree-uniform cost factor remain unresolved. No further
search will be undertaken in this mission.
