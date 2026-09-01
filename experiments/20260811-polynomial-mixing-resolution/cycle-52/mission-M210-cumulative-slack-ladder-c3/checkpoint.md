# M210 checkpoint

Date: 2026-08-13 UTC.
Status: substantive work complete; freezing exact kernel-order reduction.

## Immutable and source gates

- Full project source lock refreshed.
- Complete ledgers pass for M173/M177, M179/M184, M193/M197,
  M201/M204, and M206/M209.
- No predecessor was edited; ownership remained M210 only.

## Main conclusion

With the accepted definitions,

```text
C_3-X_3=(1-q)-T_1
```

identically. Therefore universal cumulative three-rung slack is exactly the
already-open fresh all-suffix first-Jacobi boundary, not a weaker theorem.
M210 neither proves nor refutes it.

## Exact full-kernel reduction

For child Gram kernel `K`, the retained likelihood lift is

```text
Lift_(d,a)[K]=L_(d,a)(u)L_(d,a)(v)K(u,v)/pi_a,
a=0,...,d-1,
```

with killed `a=d` absent. The parent first-Jacobi functional `Q_parent` is
positive and linear on PSD Gram kernels, while `Lift` preserves PSD. Hence
the exact residual recursion is monotone under full-child PSD domination.

The smallest direct functional-order inequality is precisely
`K_parent<=_(parent,1)(1-q)J`; this is algebraically the original boundary.
Actual progress requires explicit nonconstant PSD child majorants. A constant
rank-one majorant cannot dominate a nonconstant Gram kernel.

## Nonclosure and surviving lemma

The accepted unrestricted `P_2/P_3` witness has identical
`(M,C,||Z||^2,T_1)` but distinct exact likelihood-lift charges `18/35` and
`32/63`. Thus those scalar summaries do not close the exact monotone
recursion. The surviving standalone obligation is a full-child-Gram majorant
lemma, or equivalently control of all observation-weighted residual moments.

Diagnostics were stopped by the coordinator. Previously completed bounded
fresh rows found no counterexample but are not promoted or used. No universal
claim, total AMV, gap, mixing, or Terminal inference is made.
