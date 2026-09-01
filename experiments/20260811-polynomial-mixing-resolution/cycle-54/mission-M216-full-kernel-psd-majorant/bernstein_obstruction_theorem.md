# M216 diagonal Bernstein-envelope obstruction

Date: 2026-08-13 UTC.

## 1. Scope and status

This note concerns only the fresh first-Jacobi full-kernel recursion for the
normalized auxiliary reset excursion. It proves an exact obstruction to one
named nonconstant finite-dimensional PSD-majorant ansatz. It neither refutes
fresh contraction nor constructs an arbitrary full-kernel majorant.

## 2. Exact recursion retained

For a state `zeta`, retained observation `a<d`, likelihood
`L_(d,a)=b_(d,a)`, and `pi_a=E_mu L_(d,a)`, the actual feature lift is

```text
Phi_child -> sqrt(eta/pi_a) L_(d,a) Phi_child.
```

Hence, with killed `a=d` absent,

```text
K_zeta=R_zeta
 +sum_(live d,t)sum_(a=0)^(d-1)
   eta_(d,t) L_a(u)L_a(v)K_child(u,v)/pi_a.       (2.1)
```

The first-Jacobi charge `Q_zeta` is positive linear on PSD kernels, while
`1-q_zeta-Q_zeta[K_zeta]` is affine antitone in every child kernel.

## 3. Named degree-cap Bernstein envelope

Let

```text
b_(n,j)(u)=binom(n,j)u^j(1-u)^(n-j).
```

At degree cap `L`, the ansatz cone is

```text
B_L^diag={sum_(j=0)^L c_j b_(L,j)(u)b_(L,j)(v): c_j>=0}.  (3.1)
```

It is PSD and nonconstant. Bernstein likelihood multiplication is exact:

```text
b_(d,a)b_(ell,j)
 =[binom(d,a)binom(ell,j)/binom(d+ell,a+j)]
   b_(d+ell,a+j).                                  (3.2)
```

When `d+ell=L`, (3.2) preserves the diagonal cone exactly. If
`n=d+ell<L`, degree elevation gives

```text
b_(n,k)=sum_(j=k)^(k+L-n)
 [binom(n,k)binom(L-n,j-k)/binom(L,j)] b_(L,j)
        =sum_j e_j b_(L,j),                        (3.3)
```

with `e_j>=0`. Its exact outer product is generally nondiagonal. The named
envelope uses the positive-linear PSD bound

```text
e e^T <=_PSD (sum_j e_j)diag(e),                  (3.4)
```

because for every vector `x`,
`(sum e_j x_j)^2 <= (sum e_j)(sum e_j x_j^2)`.
Applying (3.4) atomwise after (3.2), and enveloping the exact reset kernel in
the same degree-cap cone, defines a recursive positive-linear supersolution
ansatz. The exact `eta/pi_a` factor is kept and `a=d` is deleted before
the envelope.

This repair is deliberately explicit: raw unsaturated lifts are not claimed
to remain diagonal.

## 4. A necessary dual inequality for every envelope

At a fresh degree-`L` state, express the exact actual kernel in the
degree-`L` Bernstein basis:

```text
K(u,v)=b(u)^T A b(v).                              (4.1)
```

The Bernstein evaluation vectors at `L+1` distinct points form an invertible
matrix. Therefore

```text
J_c-K is a PSD kernel  iff  diag(c)-A >=_PSD 0.    (4.2)
```

Put

```text
w_j=Q[b_(L,j)(u)b_(L,j)(v)].
```

Then `Q[J_c]=sum_j w_j c_j`. For any rational matrix `X>=_PSD0` with
`X_jj=w_j`, (4.2) implies

```text
0<=Tr(X[diag(c)-A])
  =Q[J_c]-Tr(A X).                                (4.3)
```

Thus `Tr(A X)` is an exact lower bound applying to **every** feasible
coefficient vector, independently of the chosen reset or lift envelope.

## 5. Exact fresh obstruction at B=1, L=6

Take `(B,L,kappa,D)=(1,6,2,1)`; then

```text
q=(7/8)^6=117649/262144,
1-q=144495/262144.                                (5.1)
```

Exact uniform-beta first-Jacobi weights are

```text
w=(433/10192, 747/28028, 3491/112112, 100/3003,
   3491/112112, 747/28028, 433/10192).             (5.2)
```

Let

```text
s=(-1,-1,-1,+1,+1,+1,+1),
r=(1/5,4/25,17/100,9/50,17/100,4/25,1/5),
v_j=s_j r_j,
X=vv^T+diag(w_j-r_j^2).                           (5.3)
```

The diagonal remainders are

```text
(633/254800, 18427/17517500, 39213/17517500,
 6757/7507500, 39213/17517500, 18427/17517500,
 633/254800),
```

so `X` is rational PSD and `diag(X)=w`. Reconstructing `A` from the
exact reset/history recursion (2.1) gives

```text
Tr(A X)
=27574523089250503170656957870808157889213
 /48209994003606915089647408250880000000000,

Tr(A X)-(1-q)
=1000948704365931347999936328408157889213
 /48209994003606915089647408250880000000000
>0.                                                (5.4)
```

Equations (4.3)--(5.4) prove:

> **Theorem (exact ansatz obstruction).** At the fresh state
> `(B,L,kappa,D)=(1,6,2,1)`, no kernel in `B_6^diag` can both
> PSD-dominate the exact actual kernel and have first-Jacobi charge at most
> `1-q`. Hence no recursive reset/lift envelope constrained to the
> degree-cap diagonal Bernstein cone can prove the fresh boundary.

This is one decisive row in the declared cap. No claim of global or analytic
minimality among `B<=3,L<=6` is made.

## 6. Not a contraction counterexample

At the same row, the exact actual charge is

```text
T_1
=100831060869578347854833692341308821
 /459142800034351572282356269056000000,

(1-q)-T_1
=152250599938846145694280798538691179
 /459142800034351572282356269056000000
>0.
```

Thus the true contraction budget has large positive slack. The positive dual
excess measures the cost of forcing the full kernel into the diagonal
degree-cap cone.

## 7. Exact limitation and next lemma

The obstruction does not apply to:

- arbitrary nondiagonal Bernstein coefficient matrices;
- the larger cone generated simultaneously by diagonal Bernstein atoms of all
  degrees `0,...,L`;
- weighted Jacobi/Green kernels outside (3.1); or
- the actual kernel itself.

The surviving lemma is therefore a **nondiagonal structured full-kernel
majorant**: find a likelihood-compatible PSD coefficient cone retaining
off-diagonal Bernstein/Jacobi cancellation and construct a recursive
supersolution within the fresh budget.

## 8. Reproducibility

```text
python3 -B bernstein_obstruction_exact.py \
  --output bernstein_obstruction_results.json
```

The checker is standalone, standard-library `Fraction` only, reconstructs
the single exact kernel from (2.1), converts it to the degree-six Bernstein
basis, and verifies every rational in (5.1)--(5.4). It performs no scan.
