# M167 first-Jacobi operator obstruction theorem

Date: 2026-08-13 UTC.

## 1. Scope and disposition

This note concerns only the normalized full unweighted reset excursion
`F=H/q` of the auxiliary nonlazy minimal-long-cycle parking projection. The
project target remains uniform fixed-length identity transposition words,
with `(pq)(x)=p(q(x))` and displayed factors left-to-right.

The requested universal boundary

```text
T_1(B,L,kappa,1) <= 1-q_(B,L)
```

remains **unresolved**. Two exact infinite operator counterfamilies prove a
strict obstruction reduction: scalar `T_1` induction cannot close, and no
degree-uniform branch-local charge of high modes to the killed atom can hold.
The latter obstruction is factorially summable after the exact terminal
Cayley exterior weights, so it is not an actual-history counterexample.

No auxiliary gap, `ROOT-MEAN LIFT`, original-chain gap, polynomial mixing
result, Terminal A, or Terminal B is inferred.

## 2. Accepted actual-history functional

For `b>=1`, let `mu_b=Beta(1,b)`, with

```text
p_b=1/(b+1),
sigma_b^2=b/[(b+1)^2(b+2)].
```

For a scalar or Hilbert-valued polynomial `f`, define

```text
Q_b(f)=E_mu ||f(U)||^2
       -||E_mu[(U-p_b)f(U)]||^2/sigma_b^2.          (2.1)
```

M162/M165's orthogonal actual-history coordinates `phi_gamma` give exactly

```text
T_1=sum_gamma Q_b(phi_gamma).                       (2.2)
```

For a shared degree-`d` observation `a`, the exact coordinate lift is

```text
sqrt(eta/pi_a) L_(d,a)(u) Phi_child(u),             (2.3)
```

where `pi_a=E_mu L_(d,a)` and `eta` is the exterior root/Cayley coefficient.
Every `a=0,...,d-1` is retained. The value `a=d`, equivalently attachment
rank `j=0`, is killed exactly; there is no conditioning on survival.

## 3. Exact child-first-mode leakage

> **Theorem 3.1 (proved).** For every integer `b>=1`, a retained degree-one
> shared-observation lift sends a child pure first Jacobi mode, whose child
> `T_1` is zero, to a parent with strictly positive degree-two tail. Before
> exterior multiplication the leaked fraction of a unit child first mode is
> exactly
>
> ```text
> 4/[(b+3)(b+4)].                                  (3.1)
> ```

**Proof.** Take degree `d=1` and retained `a=0`. Then

```text
L_(1,0)(u)=1-u,
pi_0=b/(b+1),
mu_child=Beta(1,b+1).
```

The other observation `a=1=d` is the killed atom. Put

```text
f(u)=u-1/(b+2),
g(u)=(1-u)f(u)/sqrt(pi_0).                         (3.2)
```

The child function `f` is its monic first Jacobi polynomial, so
`Q_(b+1)(f)=0`. Bayes gives

```text
E_mu_b[(1-U)f(U)]=pi_0 E_mu_(b+1)[f(U)]=0.
```

Thus `g` has no parent constant mode, but it is quadratic. Direct beta-moment
evaluation in (2.1) gives

```text
Q_b(g)=4(b+1)/[(b+2)^2(b+3)^2(b+4)] > 0.          (3.3)
```

The child squared norm is

```text
||f||^2=(b+1)/[(b+2)^2(b+3)].                     (3.4)
```

Dividing (3.3) by (3.4) proves (3.1). QED.

Consequently, no Bellman recursion whose child state records only scalar
`T_1` can dominate every exact shared-observation lift: the omitted child
first-mode energy can reappear in the parent's high tail.

## 4. Exact branch-local killed-atom obstruction

Take the fresh law `mu_1=Beta(1,1)`. For degree `d>=1`, write

```text
L_a(u)=binom(d,a)u^a(1-u)^(d-a),
pi_a=integral_0^1 L_a(u)du=1/(d+1),
e_a=L_a/sqrt(pi_a),       a=0,...,d-1.             (4.1)
```

Again `a=d` is killed exactly and has mass `pi_d=1/(d+1)`.

> **Theorem 4.1 (proved).** Each retained coordinate obeys
>
> ```text
> Q_1(e_a)
>  =(d+1)/(2d+1) * binom(d,a)^2/binom(2d,2a)
>    -3(2a-d)^2/[(d+1)(d+2)^2].                   (4.2)
> ```
>
> Hence its retained total is
>
> ```text
> R_d=sum_(a=0)^(d-1) Q_1(e_a)
>    =(d+1)/(2d+1)
>       [4^d/binom(2d,d)-1]
>      -d/(d+2)+3d^2/[(d+1)(d+2)^2],              (4.3)
> ```
>
> and
>
> ```text
> R_d=sqrt(pi*d)/2-3/2+o(1).                       (4.4)
> ```

**Proof.** Beta integration gives

```text
E[e_a^2]
 =(d+1)/(2d+1) * binom(d,a)^2/binom(2d,2a),
E[(U-1/2)e_a]
 =(2a-d)/[2 sqrt(d+1)(d+2)].
```

Since `Var(U)=1/12`, subtraction gives (4.2). Summing the squared centered
terms over `a<d` gives

```text
d/(d+2)-3d^2/[(d+1)(d+2)^2].
```

For the trace terms, the exact convolution identity

```text
sum_(a=0)^d binom(d,a)^2/binom(2d,2a)
 =4^d/binom(2d,d)                                 (4.5)
```

follows after rewriting each summand as
`binom(2a,a)binom(2d-2a,d-a)/binom(2d,d)` and taking the degree-`d`
coefficient in `(1-4z)^(-1/2)^2`. This proves (4.3). Finally the central
binomial asymptotic
`binom(2d,d)=4^d/sqrt(pi*d)(1+O(1/d))` proves (4.4). QED.

For checks, `R_1=1/2` and `R_2=3/4`. The retained constant-mode energy is
`sum_(a<d)(E e_a)^2=d/(d+1)`, so the genuine degree-at-least-two tail is
`R_d-d/(d+1)` and still diverges as `sqrt(pi*d)/2`. Therefore there is no
degree-uniform inequality `high tail <= C*pi_d`; there is not even a
degree-uniform `O(1)` branch-local bound.

This theorem is operator-level. The constant-child coordinates in (4.1) are
not asserted to occur with unit exterior mass in one actual history.

## 5. Exact terminal exterior summability

The preceding divergence does not create the suspected harmonic aggregate.
For the terminal `h=1` branch, put `n=L-1` and `d=r+1`. The accepted grouped
Cayley coefficient and split normalization give exactly

```text
eta_(n,r)=c(n,r)/[(r+1)! w_(n+2)]
 =r n^(n-r-1)(n+2)!/
   [(n-r)!(r+1)!(n+2)^(n+1)].                    (5.1)
```

The product `(n+2)!/(n-r)!` has `r+2` factors, each at most `n+2`, so

```text
0<=eta_(n,r)<=r/(r+1)!.                            (5.2)
```

For every fixed `r`, direct ratio asymptotics give

```text
eta_(n,r) -> exp(-2) r/(r+1)!    as n->infinity.   (5.3)
```

Moreover (4.3) and the standard central-binomial lower bound give
`R_(r+1)=O(sqrt(r+1))`. Hence

```text
sum_(r>=1) eta_(n,r) R_(r+1)
 <=sum_(r>=1) [r/(r+1)!] O(sqrt(r+1)) < infinity  (5.4)
```

uniformly in `n`. Thus the local square-root growth is factorially
summable after the exact terminal exterior weights. It supplies neither a
harmonic divergence nor an actual-history counterfamily.

## 6. Surviving standalone lemma

The first surviving target is the following falsifiable strengthening of
M162's one-step formulas.

> **AGGREGATED MODAL VECTOR inequality (unresolved).** For every right-heavy
> parent, decompose each actual child feature as
>
