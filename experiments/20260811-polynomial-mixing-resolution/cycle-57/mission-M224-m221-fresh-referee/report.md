# M224 final report: fresh immutable referee of M221

Date: 2026-08-13 UTC.

## Field 1 — verdict

```text
FINAL VERDICT: ACCEPT.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL OBJECTIONS: NONE.
```

M221's exact one-row theorem and negative raw lift-closure statement both
reproduce independently.

## Field 2 — target and scope

The project target remains uniform fixed-length identity transposition words,
with `(pq)(x)=p(q(x))` and displayed factors read left-to-right. This report
audits only degree-six Bernstein coefficient bandwidth at
`(B,L,kappa,D)=(1,6,2,1)` and the raw lift algebra. It accepts no recursive
envelope, contraction, total AMV, gap, mixing, or Terminal claim.

## Field 3 — immutable source gate

M221 contains exactly its eight declared payloads plus `SHA256SUMS`. Every
payload passes, and the independently computed ledger digest is

```text
ff5315e5930f3d8dc3c959acbb4413e32df4cf1f9870338e94ec892c18ec1983.
```

M221 remained immutable.

## Field 4 — clean-room reconstruction

The referee checker imports no M221 or project code and reads no M221 data.
Using literal ordered compositions and exact Gaussian Bernstein inversion, it
reproduces the actual-kernel, coefficient, and cost-matrix digests:

```text
d2ee4261fd89e712d0649d9cea3c30952256bff82c99134a59fce7b151505152
d1dd37fe74b894523b4b049099d194ed34fb64fb36d144b48ff3746a34e1ccae
9bd460a8da3fbf2a7f3dd8698eae88116bb1608dc2b1db9746ddfd9b1b2f5c0c
```

Reset, exterior `eta`, the single `1/pi_a`, and killed `a=d` are retained
exactly.

## Field 5 — conic pair and width zero

The full symmetric Frobenius pairing gives M221's exact dual:

```text
min <G,C>: C-A>=0, C off-band zero;
max <A,X>: X>=0, X on-band equals G.
```

No off-diagonal factor is missing. The width-zero matrix
`X_0=vv^T+diag(G_jj-r_j^2)` is PSD with the required diagonal, and the
independent exact objective excess is

```text
1000948704365931347999936328408157889213
/48209994003606915089647408250880000000000 > 0.
```

Therefore width zero is budget-infeasible.

## Field 6 — width-one certificate

The declared tridiagonal `C_1` reproduces exactly. Its seven strict
signed-diagonal-dominance margins are

```text
(253/150,193/300,16/75,143/300,19/25,1/200,113/40).
```

The independently formed `C_1-A` reproduces its frozen digest and all seven
strict margins; the minimum is

```text
22066085580152050340437577895121
/9632366434287095922007474176000000 > 0.
```

Thus both matrices are positive definite. Exact contraction gives

```text
<G,C_1>=4937603/9172800,
(1-q)-<G,C_1>=485323987/37571788800 > 0.
```

Width zero is impossible and width one is feasible, so the least feasible
integer bandwidth is exactly one for this row only.

## Field 7 — lift audit

Saturated multiplication shifts both Bernstein indices equally and preserves
bandwidth. Unsaturated degree elevation spreads each index over an interval of
length `L-n`, giving the exact upper bound

```text
min(L,w+(L-n)).
```

The retained `d=1,a=0` lift of the degree-one rank-one vector `(1,1)` elevates
to

```text
(1,5/6,2/3,1/2,1/3,1/6,0),
```

whose outer product has bandwidth five. Raw width one is therefore not
closed. A cost-controlled width-one envelope remains unresolved.

## Field 8 — numbered objections and reproducibility

1. **Material objections:** none.
2. **Nonmaterial objections:** none.
3. **Scope objection:** none; M221 explicitly forbids recursive or contraction
   promotion.

Run:

```text
python3 -B independent_referee.py --output results.json
```

Python 3.12.3, standard-library `Fraction`, `seed=null`, one exact row, no
M221 imports/data.

## Field 9 — disposition

Accept M221 as an exact finite-row minimal-bandwidth theorem plus an exact raw
closure obstruction. The surviving standalone obligation remains a
cost-controlled likelihood-compatible envelope or broader analytically closed
structured cone. No additional inference is accepted.

