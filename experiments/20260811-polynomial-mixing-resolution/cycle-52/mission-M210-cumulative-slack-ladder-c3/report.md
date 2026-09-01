# M210 final report: cumulative C3 slack and full-kernel order

Date: 2026-08-13 UTC.

## Field 1 — verdict

```text
FINAL VERDICT: FREEZE EXACT REFORMULATION AND STRICT STATE-VARIABLE REDUCTION.
UNRESOLVED: universal C3>=X3, equivalently fresh T1<=1-q.
PROVED: exact full-child-Gram residual recursion and PSD monotonicity.
PROVED: the smallest direct functional-order inequality is a restatement.
PROVED: listed scalar summaries do not close the likelihood lift.
```

## Field 2 — target, object, and convention

The project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, displayed factors left-to-right.
This mission concerns only fresh right-heavy parents in the normalized full
unweighted auxiliary reset excursion.

## Field 3 — exact cumulative accounting

For `S_h=U_h-T_h`,
`X_3=T_reset+sum_(h>=4)T_h-[1-q-U_1-U_2-U_3]`, and
`C_3=sum_(h=1)^3 S_h`, exact orthogonal-sector additivity gives

```text
C_3-X_3=(1-q)-T_1.
```

Thus the universal cumulative inequality is not a new consequence of the
accepted three sector bounds. It is the original fresh first-Jacobi boundary.

## Field 4 — full-kernel residual recursion

For a state `zeta`, define the positive linear first-Jacobi functional
`Q_zeta` on Gram kernels and the retained lift

```text
Lift_(d,a)[K](u,v)=L_(d,a)(u)L_(d,a)(v)K(u,v)/pi_a.
```

Then, with killed `a=d` absent,

```text
K_zeta=R_zeta+sum_(d,t,a<d)eta_(d,t)Lift[K_child],

1-q_zeta-T_1(zeta)
=1-q_zeta-Q_zeta[R_zeta]
 -sum_(d,t,a<d)eta_(d,t)Q_zeta[Lift[K_child]].
```

This preserves every likelihood-weighted Hilbert/Jacobi cross term and the
exact parent covariance subtraction.

## Field 5 — monotonicity and smallest kernel inequality

`Lift` preserves PSD kernels and `Q_zeta` is positive on them. Therefore
`K<=_PSD Khat` implies

```text
Q_zeta[Lift[K]]<=Q_zeta[Lift[Khat]].
```

A sufficient proof would build explicit nonconstant PSD majorants for every
child and verify the aggregated parent budget. The smallest direct preorder
statement using the actual child kernels is exactly

```text
K_parent<=_(parent,1)(1-q_parent)J,
```

which is merely `T_1<=1-q`. M210 states this restatement explicitly rather
than presenting it as theorem progress. PSD domination by the constant kernel
is impossible for a nonconstant feature.

## Field 6 — exact scalar nonclosure

The accepted `Beta(1,2)` residuals `P_2,P_3`, after normalization, have the
same

```text
(M,C,||Z||^2,T_1)=(0,0,1,1)
```

but parent likelihood-lift charges

```text
18/35 != 32/63.
```

Hence none of child scalar `T_1`, fresh scalar `C_3`, or
`(M,C,||Z||^2)` determines the exact lifted charge. A scalar-only proof would
need an additional uniform operator envelope not supplied by the recursion.

## Field 7 — numbered self-objections and scope

1. **Is `C_3` a new amortized theorem target?** No; it equals the full fresh
   deficit exactly.
2. **Does kernel monotonicity prove the inequality?** No; an explicit PSD
   majorant satisfying the budget is still missing.
3. **Can `(1-q)J` be that majorant?** No; a constant rank-one kernel cannot
   PSD-dominate a nonconstant Gram feature.
4. **Does nonclosure rule out every scalar upper bound?** No. It rules out
   exact closure on the listed summaries; a genuinely new, possibly looser
   uniform operator theorem could still exist.
5. **Did finite rows prove all `L`?** No. Completed exploratory passes are
   nonpromoted and unused.

## Field 8 — dependencies and exact reproducibility

Accepted immutable inputs are M173/M177, M179/M184, M193/M197,
M201/M204, and M206/M209; every ledger passed. Run

```text
python3 -B kernel_order_exact.py --output kernel_order_results.json
```

using Python 3.12.3 standard-library `Fraction`, `seed=null`, and no
predecessor imports. It checks exact accounting, the two nonclosure charges,
zero parent first-mode subtractions, and the constant-kernel Loewner
obstruction. It performs no parameter scan.

## Field 9 — handoff and fresh-audit request

The next standalone lemma is the **full-child-Gram majorant lemma**: construct
explicit nonconstant PSD majorants for all reachable child kernels such that
the exact lifted aggregate fits the fresh budget. Equivalently retain all
observation-weighted residual-polynomial moments.

Request a fresh immutable referee to verify all hashes; rederive the exact
functional and lift normalizations, PSD monotonicity, restatement equivalence,
constant-majorant obstruction, and `P_2/P_3` nonclosure; and confirm that no
universal `C_3`, total-AMV, gap, mixing, or Terminal theorem is claimed.
