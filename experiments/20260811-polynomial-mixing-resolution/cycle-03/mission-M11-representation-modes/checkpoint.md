# Halfway checkpoint: exact one-gate representation modes

## 1. Model and bridge transfer operator

Use `(pq)(x)=p(q(x))`, and let `X_j=t_1...t_j`.  Write

```text
q_l(g)=#{(s_1,...,s_l) in T_N^l:s_1...s_l=g},
Z_m=q_m(id)=|Omega(N,m)|.
```

The prefix bridge marginal is exactly

```text
Pr(X_j=g)=q_j(g)q_{m-j}(g^{-1})/Z_m.                    (1.1)
```

Let `rho_lambda` be an irreducible representation.  If a length-`r` window
starts after prefix `A=X_{i-1}`, has product `H=A^{-1}X_{i+r-1}`, and the
observed prefix lies `s` steps into the window, then its heat-bath conditional
expectation is

```text
E[rho_lambda(X_{i+s-1}) | outside]
 =rho_lambda(A) B_{lambda;s,r}(H),                       (1.2)

B_{lambda;s,r}(H)
 =[1/q_r(H)] sum_U q_s(U)q_{r-s}(U^{-1}H)rho_lambda(U).
```

This is the exact matrix-valued bridge transfer operator for `K`, not the
ordinary random-transposition convolution operator.  It obeys only the
equivariance

```text
B(kHk^{-1})=rho(k)B(H)rho(k)^{-1};                       (1.3)
```

it need not be scalar.  Therefore scalar character modes can couple to
matrix multiplicities and local word geometry.

For reference, if `c_mu` is the transposition-class-sum content eigenvalue
in irreducible `mu`, Fourier inversion and the Kronecker coefficient
`g(mu,nu,lambda)` give the exact bridge expectation

```text
E[chi_lambda(X_j)]
 = [sum_{mu,nu} d_mu d_nu c_mu^j c_nu^(m-j)
                    g(mu,nu,lambda)]
   /[sum_mu d_mu^2 c_mu^m].                              (1.4)
```

Thus even a one-prefix character involves tensor-product multiplicities,
not one ordinary-walk character ratio.  The sign character is deterministic,
`sgn(X_j)=(-1)^j`; sign-twisting any prefix character only multiplies it by
that deterministic sign.

## 2. A proved Poincare inequality for every one-gate mode

Let `M=binom(N,2)`.  For a position `j`, let `F(w)=f(t_j)`, where
`f:T_N -> R` has uniform mean zero.  Since simultaneous conjugation and
cyclic rotation act transitively, `t_j` is exactly uniform on `T_N`, so
`Var_pi(F)=Var_unif(f)`.

**Theorem 2.1.**  For every `N>=3` and even `m>=4`,

```text
Var_pi(f(t_j)) <= 4 E_K(F,F)                             (m=4),

Var_pi(f(t_j)) <= 7 M(m-2) E_K(F,F)                     (m>=6).  (2.1)
```

This controls the entire permutation representation on transpositions,

```text
R[T_N] = [N] direct-sum [N-1,1] direct-sum [N-2,2]
```

for `N>=4` (with the last summand absent at `N=3`).  In particular, no slow
mode depending on one gate alone can have a superpolynomial Rayleigh
quotient.

### Proof

First suppose the chosen gate is the first factor in an actual length-three
window.  Conditional on block product `c in T_N`, the first factor `a` has
law

```text
P(c,a)=
  M/D_N  if a=c,
  3/D_N  if a,c share exactly one endpoint,
  2/D_N  if a,c are disjoint,

D_N=M+6(N-2)+2binom(N-2,2)=(3N^2+N-12)/2.               (2.2)
```

Indeed, after fixing `a`, the last two factors must multiply to `ac`, whose
two-transposition fiber has size `M`, `3`, or `2` in the three cases.

This symmetric Markov kernel belongs to the Johnson association scheme on
two-subsets.  If `A_1` is adjacency by one-point intersection and `A_2` by
disjointness, then

```text
P=(M I+3A_1+2A_2)/D_N.                                  (2.3)
```

The eigenvalues of `(A_1,A_2)` on the constant, standard, and `[N-2,2]`
summands are

```text
(2(N-2), binom(N-2,2)),
(N-4,   -(N-3)),
(-2,     1).
```

These follow directly from the vertex-edge incidence matrix of `K_N` and
`A_2=J-I-A_1`.  Hence the nonconstant eigenvalues of `P` are

```text
theta_1=(M+N-6)/D_N,
theta_2=(M-4)/D_N,                                      (2.4)
```

with only `theta_1=0` at `N=3`.  For `N>=4`, both are nonnegative,
`theta_1>=theta_2`, and `theta_1<=3/8`.  Therefore

```text
(1/M)sum_c Var_{a~P(c,.)} f(a)
 =Var_unif(f)-||Pf||_2^2
 >=(55/64)Var_unif(f).                                  (2.5)
```

The explicit `55/64` is used below.

For a fixed length-three window, the event that its product is a
transposition contains the event that the other two factors form an adjacent
square.  Insertion/deletion at those designated positions gives exactly

```text
Pr(the designated other pair is equal)=M Z_{m-2}/Z_m.    (2.6)
```

The central trace formula

```text
Z_k=(1/N!)sum_mu d_mu^2 c_mu^k
```

and `|c_mu|<=M` imply, for even `m>=4`,

```text
Z_m<=M^2 Z_{m-2}.                                       (2.7)
```

Thus the event in (2.6), and hence the transposition-product event, has
probability at least `1/M`.  Conditional on a transposition product, that
product is uniform over `T_N` by simultaneous conjugation, and the heat bath
uses (2.2).  Equations (2.5)--(2.7) give

```text
E_pi Var(F | outside of the selected H_3 window)
 >=55/(64M) Var_pi(F).                                  (2.8)
```

For any `j<=m-2`, use the window beginning at `j`; for either of the last two
positions, use a window ending at `j` and reverse the same calculation.
The exact `r=3` contribution to `E_K` is

```text
1/[2|R_m|(m-2)] times the conditional variance.          (2.9)
```

When `m>=6`, `|R_m|=3`, so (2.8)--(2.9) actually prove the slightly stronger

```text
E_K(F,F)>=55/[384 M(m-2)] Var_pi(F),                     (2.10)
```

which implies the rounder second bound in (2.1), since
`384/55 < 7`.  When `m=4`, the whole-word `H_{1,4}` has coefficient
`1/4` in `I-K` and is projection onto constants, proving the first bound.

Every block-size, window, laziness, fiber, and stationary-mass factor is
visible above.

## 3. Prefix-character scalar closure is false

The tempting scalar reduction

```text
span{1, chi_std(X_1),...,chi_std(X_{m-1})}
```

is not invariant under full `K`.  The exact smallest decisive witness found
is `S_4,m=6`, where all `r=3,4,5` terms are present.  Let `e=(0,1)` and
`s=(0,2)`, and take

```text
w_1=(e,e,e,e,e,e),
w_2=(e,e,e,e,s,s).
```

Both have product identity and the identical standard-character prefix
vector

```text
(chi(X_1),...,chi(X_5))=(1,3,1,3,1).
```

Exact conditional-fiber averaging gives

```text
(K chi_std(X_2))(w_1)=9349/4428,
(K chi_std(X_2))(w_2)=84305/39852,
```

whose difference is `41/9963`.  Therefore `K chi_std(X_2)` is not even a
function of the complete displayed prefix-character vector, proving
nonclosure.  Exact matrix ranks are `4` before and `5` after adjoining this
image.  The same failure occurs for `X_3` and `X_4`.

This finite computation refutes the universal scalar-closure lemma; it is
not evidence of slow mixing.  It precisely exhibits the matrix/multiplicity
information hidden by cycle-type characters.

## 4. Exact frontier

The one-gate theorem closes all standard and `[N-2,2]` increment modes with
an `O(N^2m)` Poincare constant.  The first unproved representation statement
is:

> **MULTIPLICITY-AWARE PREFIX POINCARE.**  There is a universal polynomial
> `p(N,m)` such that every mean-zero function in the linear span of all
> matrix coefficients of `rho_lambda(X_j)`, over irreducibles `lambda` and
> positions `j`, satisfies `Var_pi(F)<=p(N,m)E_K(F,F)` after enlarging the
> span as necessary to make the exact transfer operators (1.2) closed.

The phrase “after enlarging” is substantive: the scalar character span is
already refuted, and unrestricted closure may generate the full word
algebra.  A useful theorem needs a polynomial-dimensional or otherwise
quantitatively controlled multiplicity space.
