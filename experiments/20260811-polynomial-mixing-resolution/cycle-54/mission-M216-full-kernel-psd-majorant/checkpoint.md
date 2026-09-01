# M216 checkpoint

Date: 2026-08-13 UTC.
Status: substantive halfway obstruction proved; exact artifact/freeze pending.

## Source lock and immutable gate

- Ownership remains restricted to M216; no predecessor was edited.
- The project skill, `HANDOFF.md`, `GOAL_SPEC.md`, sampling/experiment
  references, and relevant manuscript status sections were refreshed.
- Every frozen ledger in the relevant M157/M160, M162/M165, M173/M177,
  M179/M184, M185/M190, M193/M197, M201/M204, M206/M209, and M210/M213
  chain passes exactly.

## Named analytic ansatz

Before diagnostics I fixed the diagonal Bernstein PSD family

```text
J_zeta(u,v)=sum_(j=0)^ell c_j b_(ell,j)(u)b_(ell,j)(v), c_j>=0.
```

Bernstein multiplication is exact. Saturated branches remain diagonal;
unsaturated branches require degree elevation, which produces a nondiagonal
rank-one coefficient matrix. The named ansatz applies the positive-linear PSD
envelope `ee^T <= (sum e)diag(e)` after elevation. A recursive
supersolution would include an envelope of the exact reset kernel, the single
`1/pi_a`, all exterior `eta`, and deletion of killed `a=d`. Residual
antitonicity would then reduce the fresh proof to `Q[J_fresh]<=1-q`.

## Exact decisive obstruction

At the fresh state `(B,L,kappa,D)=(1,6,2,1)`, let `A` be the coefficient
matrix of the exact actual kernel `K` in the degree-six Bernstein basis and
let

```text
w_j=Q[b_(6,j) tensor b_(6,j)].
```

Any diagonal-Bernstein `J>=_PSD K` must have `diag(c)-A>=0`. Hence for every
dual feasible `X>=0` with `diag(X)=w`,

```text
Q[J]=sum_j w_j c_j >= Tr(A X).
```

Choose

```text
sign=(-1,-1,-1,+1,+1,+1,+1),
r=(1/5,4/25,17/100,9/50,17/100,4/25,1/5),
v_j=sign_j r_j,
X=vv^T+diag(w_j-r_j^2).
```

All `w_j-r_j^2` are exact nonnegative rationals, so `X` is PSD with the
required diagonal. Exact recursion and basis conversion give

```text
q=(7/8)^6=117649/262144,
Tr(A X)-(1-q)
=1000948704365931347999936328408157889213
 /48209994003606915089647408250880000000000 > 0.
```

Therefore no coefficient choice in the degree-cap diagonal-Bernstein envelope
family can both PSD-dominate the actual kernel and fit the fresh first-Jacobi
budget. This refutes every positive-linear lift/reset envelope that insists on
returning to that cone. It does not refute contraction, a nondiagonal
full-kernel majorant, or the larger all-degree Bernstein dictionary cone.

## Next

Freeze the exact dual proof with a compact standalone `Fraction` checker,
nine-field report, manifest/hashes, and request for a fresh immutable audit.
No further family or row will be explored in this mission.
