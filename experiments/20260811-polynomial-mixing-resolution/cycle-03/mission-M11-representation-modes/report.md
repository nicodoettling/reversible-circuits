# Cycle 03 M11 report: exact one-gate modes and prefix-transfer obstruction

## 1. Exact claims, quantifiers, and conventions

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and a word evaluates as
`t_1...t_m`.  Put `X_j=t_1...t_j`, `M=binom(N,2)`, and

```text
K=(1/2)I+(1/(2|R_m|)) sum_{r in R_m} 1/(m-r+1) sum_i H_{i,r},
R_m={r in {3,4,5}:r<=m}.
```

All variances and Dirichlet forms below are under the uniform law on
`Omega(N,m)`.

**Claim A (proved: exact bridge transfer).**  For every `N`, every feasible
prefix/window configuration, and every irreducible representation `rho` of
`S_N`, the conditional action of an exact heat bath is the matrix-valued
operator in (2.2) below.  It is conjugation equivariant but need not be a
scalar character-ratio operator.

**Claim B (proved: a nontrivial inverse-polynomial mode bound).**  For every
`N>=3`, every even `m>=4`, every `1<=j<=m`, and every real function
`f:T_N -> R` of uniform mean zero, let `F(t_1,...,t_m)=f(t_j)`.  Then

```text
Var_pi(F) <= 4 E_K(F,F)                         if m=4,
Var_pi(F) <= (384/55) M(m-2) E_K(F,F)           if m>=6.       (1.1)
```

In particular the second constant is less than `7M(m-2)`.  This controls
every nonconstant mode in the conjugation permutation representation

```text
R[T_N]=[N] direct-sum [N-1,1] direct-sum [N-2,2]
```

for `N>=4`, with `[N-2,2]` absent at `N=3`.  Thus a mode depending on one
gate alone cannot witness superpolynomially small gap.

**Claim C (refuted universal auxiliary lemma).**  It is false that, for all
`N,m`, the span of `1` and the scalar standard characters
`chi_std(X_j)`, `1<=j<m`, is invariant under the full exact `K`.  An exact
counterexample occurs at `N=4,m=6` and includes all `r=3,4,5` updates.

Claims A--C do not prove a gap bound for all functions and do not establish
Terminal A or Terminal B.

## 2. Full argument

### 2.1 Exact transfer operator

Define

```text
q_l(g)=#{(s_1,...,s_l) in T_N^l:s_1...s_l=g},
Z_m=q_m(id)=|Omega(N,m)|.
```

Splitting an identity word at `j` gives the exact prefix bridge marginal

```text
Pr(X_j=g)=q_j(g)q_{m-j}(g^{-1})/Z_m.                    (2.1)
```

Suppose a length-`r` window begins after `A=X_{i-1}`, its fixed ordered
product is `H=A^{-1}X_{i+r-1}`, and the observed prefix is `s` factors into
the window.  Exact uniform conditional resampling gives

```text
E[rho(X_{i+s-1}) | outside]
 =rho(A) B_{rho;s,r}(H),

B_{rho;s,r}(H)
 =[1/q_r(H)] sum_U q_s(U)q_{r-s}(U^{-1}H)rho(U).        (2.2)
```

The formula follows by fixing the product `U` of the first `s` new factors;
there are `q_s(U)q_{r-s}(U^{-1}H)` completions.  Since every `q_l` is a
class function,

```text
B(kHk^{-1})=rho(k)B(H)rho(k)^{-1}.                     (2.3)
```

Equivariance does not make `B(H)` scalar when `H` is not central.  To display
the resulting multiplicities already at the level of expectations, let
`c_mu` be the scalar by which the transposition class sum acts in irreducible
`mu`, let `d_mu` be its dimension, and let `g(mu,nu,lambda)` be the
Kronecker coefficient.  Fourier inversion and the fact that all symmetric-
group characters are real yield

```text
E chi_lambda(X_j)
 = [sum_{mu,nu} d_mu d_nu c_mu^j c_nu^(m-j)
                    g(mu,nu,lambda)]
   /[sum_mu d_mu^2 c_mu^m].                            (2.4)
```

This is not an ordinary random-transposition eigenvalue formula.  Also,
`sgn(X_j)=(-1)^j` deterministically, so the sign and sign-twisted scalar
observables provide no new stochastic scalar mode.

### 2.2 One-gate Poincare inequality

Simultaneous conjugation preserves `Omega(N,m)` and acts transitively on
`T_N`, so every `t_j` is exactly uniform.  Hence
`Var_pi(f(t_j))=Var_unif(f)`.

First put the chosen gate in the first position of a length-three window and
condition on the window product being a transposition `c`.  If its first
factor is `a`, the remaining two factors must multiply to `ac`.  The exact
number of two-transposition factorizations is `M`, `3`, or `2` according as
`a=c`, `a,c` meet in one vertex, or `a,c` are disjoint.  Therefore the first
factor has the symmetric Markov kernel

```text
P(c,a)=M/D_N  if a=c,
       =3/D_N  if |a intersect c|=1,
       =2/D_N  if a intersect c is empty,

D_N=M+6(N-2)+2binom(N-2,2)=(3N^2+N-12)/2.             (2.5)
```

Write `A_1` for one-point-intersection adjacency and `A_2` for disjointness
on the two-subsets of `[N]`.  Then

```text
P=(M I+3A_1+2A_2)/D_N.                                (2.6)
```

The vertex-edge incidence matrix of `K_N`, together with
`A_2=J-I-A_1`, gives the following eigenvalue pairs for `(A_1,A_2)`:

```text
constant:  (2(N-2), binom(N-2,2)),
standard:  (N-4, -(N-3)),
[N-2,2]:   (-2, 1).
```

Thus the two possible nonconstant eigenvalues of `P` are

```text
theta_1=(M+N-6)/D_N,       theta_2=(M-4)/D_N.           (2.7)
```

At `N=3` only the standard summand occurs and `theta_1=0`.  For every
`N>=4`, `0<=theta_2<=theta_1<=3/8`; the last inequality is equivalent to
`N^2-5N+60>=0`.  As `P` is symmetric and stochastic, for every mean-zero
`f`,

```text
(1/M) sum_c Var_{a~P(c,.)} f(a)
 =Var_unif(f)-||Pf||_2^2
 >=(55/64)Var_unif(f).                                 (2.8)
```

It remains to lower-bound how often a stationary length-three window has a
transposition product.  In a chosen orientation, require the two factors
other than the observed gate to be equal.  Deleting that fixed adjacent
square is a bijection between such words and a choice of one of `M`
transpositions together with an arbitrary word in `Omega(N,m-2)`.  Hence

```text
Pr(the designated other pair is equal)=M Z_{m-2}/Z_m.  (2.9)
```

For completeness, Fourier inversion at the identity gives

```text
Z_k=(1/N!) sum_mu d_mu^2 c_mu^k.                       (2.10)
```

Each `c_mu` is real and `|c_mu|<=M`, since it is an eigenvalue of a sum of
`M` unitary transpositions.  Because `m` and `m-2` are even, every summand
in (2.10) is nonnegative and

```text
Z_m<=M^2 Z_{m-2}.                                      (2.11)
```

Consequently (2.9) is at least `1/M`.  The square event implies that the
three-factor product equals the observed transposition.  Conditional on the
larger event that this product is a transposition, its value is uniform on
`T_N` by simultaneous conjugation.  The heat-bath conditional variance
depends only on this product, so (2.8)--(2.11) imply

```text
E_pi Var(F | outside the selected H_3 window)
 >=55/(64M) Var_pi(F).                                 (2.12)
```

For `j<=m-2`, choose the window beginning at `j`.  For the final two
positions choose a window ending at `j`; reversing the preceding
first/last-factor count gives the same kernel.  In the exact lazy `K`, a
specified `H_3` window has Dirichlet coefficient

```text
1/[2|R_m|(m-2)].                                       (2.13)
```

When even `m>=6`, `|R_m|=3`; multiplying (2.12) by (2.13) gives

```text
E_K(F,F)>=55/[384M(m-2)] Var_pi(F).                    (2.14)
```

All `r=4,5` Dirichlet contributions are nonnegative and remain in the full
form; they have not been identified with, or removed from, the chain.
When `m=4`, `R_m={3,4}` and the whole-word heat bath `H_{1,4}` occurs in
`I-K` with coefficient `1/4`.  It is projection onto constants under the
uniform bridge law, so `E_K(F,F)>=Var_pi(F)/4`.  This proves Claim B.

### 2.3 Exact failure of scalar prefix closure

At `N=4,m=6`, let `e=(0,1)` and `s=(0,2)`, and define

```text
w_1=(e,e,e,e,e,e),
w_2=(e,e,e,e,s,s).
```

Both words evaluate to the identity.  For the standard character
`chi_std(g)=#{fixed points of g}-1`, both have the complete prefix vector

```text
(chi_std(X_1),...,chi_std(X_5))=(1,3,1,3,1).           (2.15)
```

Exact rational averaging over every same-product fiber, every window, all
three block sizes, and the lazy half gives

```text
(K chi_std(X_2))(w_1)=9349/4428,
(K chi_std(X_2))(w_2)=84305/39852,
difference=41/9963.                                    (2.16)
```

Thus the image is not even a function of the complete scalar vector (2.15),
so it cannot lie in its linear span.  The feature matrix has rank `4` and
rank `5` after adjoining this image.  The same exact test fails for `X_3`
and `X_4`.  This refutes the universal closure lemma, not polynomial mixing.

## 3. Probability, runtime, path length, and congestion accounting

- The exact stationary event used in Claim B has probability
  `MZ_{m-2}/Z_m>=1/M`; this is not a reachability estimate.
- A specified active `H_3` window has full-chain Dirichlet weight
  `1/[2|R_m|(m-2)]`, which is `1/[6(m-2)]` for even `m>=6`.
- The conditional spectral loss is exactly bounded by `55/64`; multiplying
  the three factors gives `55/[384M(m-2)]`.
- At `m=4`, the whole-word term has exact weight `1/4`, including laziness
  and the two-way block-size choice.
- No comparison paths or multicommodity flow are used, so path length and
  congestion are not applicable.
- The falsification harness is deterministic and enumerates at most `M^m`
  words, then exact block fibers.  It is deliberately a bounded
  falsification tool, not a polynomial-in-`N,m` algorithm or an asymptotic
  mixing argument.  No random seed is used.  The output records Python
  `3.12.3`, SymPy `1.12`, the repository commit, all fiber sizes, ranks, and
  exact rational witnesses.

## 4. Dependencies

- **Proved here:** the transfer formula (2.2), the three-factor marginal
  count (2.5), the Johnson-scheme eigenvalues (via incidence), the fixed-slot
  square insertion/deletion bijection, the trace ratio (2.10)--(2.11), and
  the full-`K` inequality (1.1).
- **Proved inherited:** uniform bridge stationarity/reversibility of exact
  heat baths.  Only uniform counting is needed for Claim B.
- **Exact finite proof:** Claim C.  Exact exhaustive arithmetic refutes the
  universal scalar-closure statement; it is not empirical convergence
  evidence.
- **Cited standard algebra:** finite-group Fourier inversion and the
  decomposition of the two-subset permutation representation.  Their needed
  special cases are also derived in the argument above.
- **Conditional dependencies:** none for Claims A--C.
- **Empirical dependencies:** none.

## 5. First unproved step

> **STANDARD-MATRIX PREFIX POINCARE.**  There are universal constants
> `c>0,C<infinity` such that for every `N>=3`, every even `m>=4`, and every
> mean-zero real function `F` in the span of the real and imaginary matrix
> coefficients of `rho_std(X_j)`, `1<=j<m`, one has
> `E_K(F,F)>=c(Nm)^(-C) Var_pi(F)`.

This proposition is well-defined without assuming that the span is
`K`-invariant.  Formula (2.2) suggests a multiplicity-aware route, while
(2.16) proves that scalar characters alone do not close it.

## 6. Strongest self-attack

Claim B controls `F=f(t_j)` for one fixed `j`; it does **not** control the
linear span of such functions over multiple positions.  Dirichlet changes
can cancel in sums, and a prefix observable contains strongly correlated
products of many gates.  The controlled space is therefore nontrivial but
small relative to `L^2(Omega(N,m))`.  Moreover, iterating (2.2) may generate
a multiplicity space as large as the full word algebra.  The exact closure
counterexample is an obstruction to a simple proof route, not a slow mode.
No arbitrary-cut conductance, global fiber gap, or Terminal-B family follows.

## 7. Calibration results

- Odd `m`: `Omega(N,m)` is empty; all claims explicitly assume even `m`.
- `m=0`: the state space is a singleton and lies outside the theorem.
- `N=2`, even `m`: singleton; the nonconstant mode statement starts at
  `N=3`.
- `m=2,N>=3`: excluded, and no `H_3` window exists.
- `S_3,m=4`: the harness finds exactly `27` words and no scalar-closure
  failure.  The theorem uses the whole-word `H_4`, not pure Hurwitz motion;
  the four Hurwitz components therefore cause no mismatch.
- `S_4,m=4`: the harness finds exactly `120` words and no scalar-closure
  failure.  Again the exact `H_4` coefficient `1/4` is essential; the
  thirteen Hurwitz components are irrelevant to that global heat bath.
- `S_4,m=6`: the harness finds exactly `3936` words and the decisive full-K
  closure witness (2.16).  All `r=3,4,5` fibers and all windows are used;
  the seventeen pure-Hurwitz components are not substituted for K.
- Connected near-minimal doubled-tree words and disconnected component
  interleavings are covered uniformly by the one-gate counting argument,
  but no claim is made about their global mixing or cuts.
- Sign parity is deterministic; edge-multiplicity parity and vertex-degree
  parity are not used as identity criteria.
- No length-two local simulation, fixed canonical hub, or graph-only
  projection is used.  No asymptotic cut is proposed, so no stationary-mass
  side has been suppressed.
- The bound is polynomial in `N,m`, as required by the present parameter
  model; it is not claimed polynomial in `log N`.

## 8. Artifacts and reproduction commands

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-03/mission-M11-representation-modes/
```

Files:

```text
plan.md
checkpoint.md
prefix_mode_closure.py
prefix_closure_N3_m4.json
prefix_closure_N4_m4.json
prefix_closure_N3_m6.json
prefix_closure_N4_m6.json
report.md
```

From the repository root, reproduce with:

```text
python3 -m compileall experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M11-representation-modes/prefix_mode_closure.py
python3 experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M11-representation-modes/prefix_mode_closure.py --N 3 --m 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M11-representation-modes/prefix_closure_N3_m4.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M11-representation-modes/prefix_mode_closure.py --N 4 --m 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M11-representation-modes/prefix_closure_N4_m4.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M11-representation-modes/prefix_mode_closure.py --N 3 --m 6 --output experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M11-representation-modes/prefix_closure_N3_m6.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M11-representation-modes/prefix_mode_closure.py --N 4 --m 6 --output experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M11-representation-modes/prefix_closure_N4_m6.json
```

The finite calculation could falsify only the named universal scalar-closure
lemma; it cannot prove an asymptotic gap.  The decisive failure is already
the smallest tested full-`r=3,4,5` calibration case `S_4,m=6`.

## 9. Verdict

**PROVED**

This verdict refers to the assigned alternative of proving a rigorous
inverse-polynomial full-`K` Poincare bound for a nontrivial representation
mode family, namely (1.1), together with the exact transfer analysis.  It is
not a global-goal verdict and is neither Terminal A nor Terminal B.
