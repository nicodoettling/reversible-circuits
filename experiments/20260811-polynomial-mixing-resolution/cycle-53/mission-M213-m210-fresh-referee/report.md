# M213 final report: fresh immutable referee of M210

Date: 2026-08-13 UTC.

## Field 1 — verdict

```text
FINAL VERDICT: ACCEPT.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL CLARIFICATION: child charges are positive-linear; the residual is
affine antitone in each child kernel.
```

M210 correctly freezes an exact reformulation and state-variable obstruction.
It does not prove the universal cumulative inequality.

## Field 2 — target, convention, and scope

The project target remains uniform fixed-length identity transposition words,
with `(pq)(x)=p(q(x))` and displayed factors left-to-right. This report
audits only the fresh-parent first-Jacobi/full-child-kernel formulation. It
makes no total-AMV, all-`L`, gap, mixing, or Terminal inference.

## Field 3 — immutable hash gate

Before reading M210 conclusions, I verified its exact nine-file inventory:
`SHA256SUMS` plus all eight listed payloads. Every payload passed. The
independently computed digest of M210's ledger is
`fe96d736dd4b0bd330d98975a47ad8e4e42a949d34ec27f5087daadd48120c7b`.
All cited accepted ledgers M162/M165, M173/M177, M179/M184, M193/M197,
M201/M204, and M206/M209 also passed. M210 remained immutable.

## Field 4 — cumulative identity

Direct substitution independently gives

```text
C_3-X_3
=1-q-[T_reset+sum_(h>=1)T_h]
=(1-q)-T_1.
```

Thus `C_3>=X_3` is exactly the already-open fresh boundary
`T_1<=1-q`. M210 correctly calls it a restatement, not theorem progress.

## Field 5 — kernel recursion and monotonicity

The retained feature block `sqrt(eta/pi_a)L_a Phi_a` gives
`eta L_a(u)L_a(v)K_a(u,v)/pi_a`; killed `a=d` is absent. Orthogonal
history coordinates therefore give M210's exact full-kernel recursion.

For PSD `K=<Phi,Phi>`, the first-Jacobi functional is positive by
Hilbert-valued Bessel/Cauchy--Schwarz. Likelihood lifting preserves PSD order,
so `K<=_PSD H` implies `Q[Lift K]<=Q[Lift H]`. All covariance and
likelihood-weighted cross terms remain encoded in the full kernel.

## Field 6 — direct majorant obstruction

Testing `K<=_PSD cJ` on two points with coefficients `(1,-1)` gives zero
from `cJ` and `||Phi(u)-Phi(v)||^2` from `K`. Hence such domination
forces `Phi` constant. The weaker direct `Q`-preorder against
`(1-q)J` is exactly `T_1<=1-q`, so it only restates the target.

## Field 7 — scalar nonclosure and state requirement

The clean-room exact calculation reproduces normalized child summaries
`(M,C,||Z||^2,T_1)=(0,0,1,1)` for both `P_2` and `P_3`, but parent
charges `18/35` and `32/63`, with zero parent first-mode subtraction.
Therefore the listed summaries do not close the exact likelihood lift.

This proves only that exact recursion needs information distinguishing these
weighted shapes; the full Gram kernel or equivalent queried moments suffices.
It does not prove the full kernel uniquely minimal, rule out every scalar
upper envelope, or supply an actual-history contraction counterexample.

## Field 8 — numbered objections and reproducibility

1. **Material objections:** none.
2. **Nonmaterial wording:** M210 Section 1 says the residual is positive
   linear in child kernels. Precisely, each child charge is positive linear
   and order-preserving, while the residual is affine and antitone. M210's
   equations and deductions already use the correct sign.
3. **Scope objection:** none. M210 explicitly leaves the universal boundary
   and majorant lemma unresolved and limits the `P_2/P_3` inference.

Run:

```text
python3 -B kernel_referee_exact.py --output kernel_referee_results.json
```

The checker uses only Python 3.12.3 standard-library `Fraction`, imports no
predecessor, and performs no parameter scan.

## Field 9 — disposition

Accept M210 as an exact strict-scope reformulation. The surviving proof
obligation is still a genuinely checkable nonconstant full-child-kernel
majorant (or equivalent all-observation moment inequality) meeting the fresh
budget. No universal `C_3`, contraction theorem, total AMV, gap, mixing, or
Terminal result has been established.
