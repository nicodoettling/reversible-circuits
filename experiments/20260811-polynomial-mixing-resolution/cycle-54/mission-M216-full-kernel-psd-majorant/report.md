# M216 final report: full-kernel PSD-majorant ansatz

Date: 2026-08-13 UTC.

## Field 1 — verdict

```text
FINAL VERDICT: REFUTE THE DEGREE-CAP DIAGONAL BERNSTEIN ENVELOPE ANSATZ.
UNRESOLVED: arbitrary nonconstant full-kernel PSD majorants and fresh
first-Jacobi contraction.
```

An exact rational dual certificate proves that no degree-six diagonal
Bernstein kernel can both dominate the actual fresh kernel and fit its budget.

## Field 2 — target and strict scope

The project target remains uniform fixed-length identity transposition words,
with `(pq)(x)=p(q(x))` and displayed factors left-to-right. This is only an
auxiliary fresh first-Jacobi ansatz obstruction. No all-state, total-AMV,
gap, mixing, or Terminal result follows.

## Field 3 — immutable inputs

All frozen ledgers in the M157/M160 through M210/M213 AMV chain passed before
substantive use. Those directories were read-only. The accepted exact
full-kernel recursion, positive child-charge functional, and affine-antitone
residual are retained.

## Field 4 — named nonconstant ansatz

At degree cap `L`, the cone is

```text
J=sum_(j=0)^L c_j b_(L,j) tensor b_(L,j), c_j>=0.
```

Bernstein likelihoods multiply exactly. Saturated lifts remain diagonal.
Unsaturated lifts degree-elevate to a positive feature vector `e`, and the
named positive-linear envelope uses
`ee^T<=_PSD(sum e)diag(e)`. The recursive ansatz also envelopes the exact
reset kernel, keeps `eta/pi_a`, and deletes killed `a=d`.

Raw unsaturated lifts are not claimed to remain diagonal.

## Field 5 — universal dual lower bound within the ansatz

If the exact degree-`L` Bernstein coefficient matrix is `A`, every
feasible ansatz kernel satisfies `diag(c)-A>=0`. With
`w_j=Q[b_(L,j) tensor b_(L,j)]`, any `X>=0` having `diag(X)=w` gives

```text
Q[J]=sum_j w_j c_j >= Tr(A X).
```

This bound applies to every coefficient vector and every lift/reset envelope
returning to the named cone.

## Field 6 — exact B=1, L=6 certificate

At `(B,L,kappa,D)=(1,6,2,1)`, use signs
`(-,-,-,+,+,+,+)`, radii
`(1/5,4/25,17/100,9/50,17/100,4/25,1/5)`, and
`X=vv^T+diag(w-r^2)`. Every remainder is nonnegative. Exact arithmetic gives

```text
q=117649/262144,
Tr(A X)-(1-q)
=1000948704365931347999936328408157889213
 /48209994003606915089647408250880000000000 > 0.
```

Therefore no degree-six diagonal Bernstein majorant fits the fresh budget.
This is a decisive row in the declared cap; analytic minimality is not claimed.

## Field 7 — self-attack and boundaries

The actual kernel at the same row has

```text
(1-q)-T_1
=152250599938846145694280798538691179
 /459142800034351572282356269056000000 > 0.
```

So this is not a contraction counterexample. It does not refute arbitrary
nondiagonal kernels, the larger all-degree Bernstein dictionary cone, or a
Jacobi/Green majorant. The exact recursion includes reset coordinates,
`eta/pi_a`, and all retained observations; `a=d` is absent exactly.

## Field 8 — exact reproducibility

Run:

```text
python3 -B bernstein_obstruction_exact.py \
  --output bernstein_obstruction_results.json
```

The standalone Python 3.12.3 checker uses standard-library `Fraction`,
`seed=null`, imports no predecessor, reconstructs exactly one row, and
performs no parameter scan.

## Field 9 — next lemma and audit request

The surviving standalone obligation is a **nondiagonal structured
full-kernel majorant** retaining off-diagonal Bernstein/Jacobi cancellation
under likelihood lifts. A fresh immutable referee should verify the M216
hashes, exact recursion normalization, Bernstein multiplication/elevation,
PSD dual argument, rational B=1,L=6 certificate, positive actual slack, and
strict ansatz-only scope.
