# M311 Precomputation Candidate Freeze

Date: 2026-08-14 UTC
Status: frozen before any finite execution

## Candidate `QBP_1`

Use the notation and maximal Abel sign blocks `mathcal B_q` of
`staircase_identity.md`.  The single predeclared compensation candidate is:

```text
(QBP_1)  For every odd k>=3, every 1<=u<k/2, every
         2<=ell<=3k-2, and every maximal sign block q,

         C_q(k,u,ell)
          =sum_((c,d) in mathcal B_q)
             pi_cd(k)[Xbar_c(k,u,ell)-Ybar_d(k,u,ell)]
          >=0.                                             (QBP_1)
```

This is a genuine multi-cell condition: individual summands may have either
sign, but compensation must occur before the Abel sign changes.  All middle
phases and all supported cells are retained.

## Sufficiency

The exact block decomposition `(QBD_1)` gives

```text
QBP_1  =>  P_(k,ell)(u)=sum_q C_q(k,u,ell)>=0.
```

Thus an all-rank proof of QBP_1 would prove MCLP_1.  No converse is claimed;
different blocks may cancel in the full aggregate, so QBP_1 is strictly a
sufficient strengthening whenever more than one block occurs.

## Falsification protocol fixed now

Analytic proof is attempted first.  If it does not close, one and only one
new exact rank is allowed:

```text
k=11, n=33,
u=1,2,3,4,5,
ell=2,...,31,
all 11 middle phases,
every supported quantile cell,
every maximal sign block.
```

The first counterexample is ordered lexicographically by
`(u,ell,block_index)`, with block indices ordered by increasing rung.  The
checker must also verify QTI_1, QBD_1, row/column marginals, complete cell
coverage, exact reflection, and the full MCLP aggregate.  It may not search a
replacement grouping or another rank after seeing the result.

No finite positivity will be promoted to MCLP_1, and failure of QBP_1 will
not refute MCLP_1 unless the complete aggregate itself is negative.
