# M219 final report: fresh immutable referee of M216

Date: 2026-08-13 UTC.

## Field 1 — verdict

```text
FINAL VERDICT: ACCEPT.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL OBJECTIONS: NONE.
```

M216's rational row exactly refutes the declared degree-cap diagonal
Bernstein PSD-envelope ansatz. The row has positive actual contraction slack,
so it does not refute contraction or a broader full-kernel majorant.

## Field 2 — target and strict scope

The project target remains uniform fixed-length identity transposition words,
with `(pq)(x)=p(q(x))` and displayed factors read left-to-right. This audit is
only about the auxiliary fresh first-Jacobi kernel at the named row and the
cone `B_6^diag`. It establishes no all-degree, arbitrary nondiagonal,
Jacobi/Green, contraction, total-AMV, gap, mixing, or Terminal conclusion.

## Field 3 — immutable source lock

The M216 directory has exactly its nine declared payloads plus the checksum
ledger. Every payload passes, and the independently computed ledger digest is

```text
2c25bb31839bf8ff64181b9e4437fe70f5530bf5e7d0aa4eca8de4c21388d414.
```

M216 remained immutable. Its frozen checker also replayed exactly into
`/tmp` after the clean-room result was produced.

## Field 4 — Bernstein closure and envelope

Exact multiplication sends `b_(d,a)b_(ell,j)` to a positive scalar multiple
of `b_(d+ell,a+j)`. A saturated `d+ell=L` atom is diagonal at cap `L`.
An unsaturated atom degree-elevates to a positive vector `e` and has raw
coefficient matrix `ee^T`, generally nondiagonal. The named envelope is exact:

```text
(sum e)diag(e)-ee^T
=sum_(i<j)e_i e_j(unit_i-unit_j)(unit_i-unit_j)^T >=_PSD 0.
```

The independent checker verifies 182 products, 77 saturated closures, all 28
elevations through cap six, and 105 unsaturated nondiagonal cases.

## Field 5 — exact recursion reconstruction

The clean-room checker reads no predecessor artifact or data. It uses literal
ordered compositions, independently reconstructs reset basin currents, and
uses the retained lift

```text
(eta/pi_a)L_a(u)L_a(v)K_child(u,v),  a=0,...,d-1.
```

Every beta-binomial attachment law sums to one and `a=d` is omitted exactly.
Across 32 reachable states it records 51 live literal root rows, 108 retained
observations, and 51 killed observations. It independently reproduces the
frozen kernel and Bernstein-coefficient digests:

```text
d2ee4261fd89e712d0649d9cea3c30952256bff82c99134a59fce7b151505152
d1dd37fe74b894523b4b049099d194ed34fb64fb36d144b48ff3746a34e1ccae
```

## Field 6 — necessary PSD inequality

The degree-six Bernstein evaluation matrix is invertible (the checker finds
determinant `3125/17006112` at `0,1/6,...,1`). Therefore
`b(u)^T M b(v)` is a PSD kernel iff `M>=_PSD0`. If
`K=b^T A b` and `J_c=b^T diag(c)b` satisfies `J_c>=_PSD K`, then necessarily

```text
diag(c)-A>=_PSD0.
```

For `w_j=Q[b_j tensor b_j]`, every dual `X>=0` with `diag(X)=w` consequently
gives `Q[J_c]>=Tr(A X)`.

## Field 7 — exact certificate and positive actual slack

At `(B,L,kappa,D)=(1,6,2,1)`, the clean-room exact arithmetic reproduces

```text
q=117649/262144,
Tr(A X)-(1-q)
=1000948704365931347999936328408157889213
 /48209994003606915089647408250880000000000 > 0.
```

The dual matrix is `X=vv^T+diag(w-r^2)` and all seven displayed remainders are
strictly positive. Hence no degree-six diagonal Bernstein majorant fits the
fresh budget. At the same time,

```text
(1-q)-T_1
=152250599938846145694280798538691179
 /459142800034351572282356269056000000 > 0,
```

so the actual row contracts with positive slack.

## Field 8 — numbered objections and reproducibility

1. **Material objections:** none.
2. **Algebra/normalization objections:** none.
3. **Certificate objections:** none.
4. **Scope objections:** none.

Reproduce the independent row with

```text
python3 -B independent_reconstruction.py --output results.json
```

The checker uses Python 3.12.3 standard-library exact `Fraction` arithmetic,
`seed=null`, one named top row, literal ordered compositions, and exact
Gaussian basis inversion. It imports no project or M216 code and reads no
M216 data.

## Field 9 — disposition

Accept M216 as a strict-scope exact ansatz obstruction. The surviving proof
obligation is the one M216 states: a likelihood-compatible nondiagonal
structured full-kernel majorant, or another method preserving the needed
off-diagonal cancellation, within the fresh first-Jacobi budget. This audit
does not advance that remaining lemma.

