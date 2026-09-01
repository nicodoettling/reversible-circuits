# M173 aggregated modal-vector recursion and fresh terminal-sector bound

Date: 2026-08-13 UTC.

## 1. Scope and status

This note concerns only the normalized full unweighted reset excursion
`F=H/q` in the auxiliary nonlazy minimal-long-cycle parking projection. The
project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors
left-to-right.

The following are **proved**:

1. an exact parent recursion for the actual-history modal decomposition
   `Phi=M+(u-p)C/sigma^2+Z`, including all six likelihood-weighted vector
   terms and exact omission of killed observation `a=d`;
2. an exact unrestricted-operator witness showing that retaining only
   `(M,C,||Z||^2)` (or `(M,C,T_1)`) does not close that recursion;
3. the uniform fresh terminal operator aggregate
   `sum eta_(n,r)R_(r+1)<=1/4`; and
4. an actual-history corollary bounding the entire live `h=1` descendant
   contribution at a fresh parent by `(1-q_0)/4` for suffix excess at least
   two, with the one-layer boundary `(1-q_0)/2` stated separately.

The general aggregated modal-vector budget, universal all-suffix `T_1`
boundary, every gap, and both project terminals remain **unresolved**. No
weighted/root-mean statement, original-chain statement, or polynomial-mixing
statement is inferred.

## 2. Accepted coordinates

Write a state as

```text
xi=(s,kappa,D,B),       mu=Beta(D,kappa-D),
p=D/kappa,              sigma^2=Var_mu(U),
q=q_(B,s-B).
```

For a live root group `(d,t)` and observation `a=0,...,d`, put

```text
L_a(u)=binom(d,a)u^a(1-u)^(d-a),
pi_a=E_mu L_a,
mu_a=Beta(D+a,kappa-D+d-a),
xi_a=(t-1,kappa+d,D+a,B),
eta_(d,t)=m_s(d,t)q_(xi_a)/q.                     (2.1)
```

Every `a<d` is retained. The value `a=d`, equivalently attachment rank
`j=0`, is killed and absent; there is no conditioning on survival. M162/M165's
accepted actual-history feature block is

```text
f_a(u)=sqrt(eta_(d,t)/pi_a)L_a(u)Phi_(xi_a)(u).    (2.2)
```

For any Hilbert-valued polynomial `f`, define the parent first-Jacobi
functional

```text
Q_mu(f)=E_mu||f||^2-||E_mu[(U-p)f]||^2/sigma^2.   (2.3)
```

Orthogonality of the history direct sum makes `T_1` the sum of (2.3) over
the reset and all retained branch coordinates.

## 3. Exact aggregated modal-vector recursion

Fix one retained child and abbreviate its law by `mu_a`. Put

```text
p_a=E_(mu_a)U,              sigma_a^2=Var_(mu_a)(U),
delta_a=p_a-p,
M_a=E_(mu_a)Phi_a,
C_a=E_(mu_a)[(U-p_a)Phi_a],
Z_a(u)=Phi_a(u)-M_a-(u-p_a)C_a/sigma_a^2.         (3.1)
```

Then

```text
E_(mu_a)Z_a=0,
E_(mu_a)[(U-p_a)Z_a]=0.                            (3.2)
```

Define the exact likelihood-weighted quantities, with `x=U-p_a`,

```text
lambda_0=E_(mu_a)L_a,
lambda_1=E_(mu_a)[L_a x],
lambda_2=E_(mu_a)[L_a x^2],
Z_0=E_(mu_a)[L_a Z_a],
Z_1=E_(mu_a)[L_a x Z_a],
Z_2=E_(mu_a)[L_a ||Z_a||^2].                      (3.3)
```

> **Theorem 3.1 (exact AMV branch recursion).** The contribution of (2.2)
> to the parent's `T_1` is `eta_(d,t) B_a`, where
>
> ```text
> B_a=
>   lambda_0 ||M_a||^2
>  +2 lambda_1/sigma_a^2 <M_a,C_a>
>  +lambda_2/sigma_a^4 ||C_a||^2
>  +2<M_a,Z_0>
>  +2/sigma_a^2<C_a,Z_1>
>  +Z_2
>  -pi_a/sigma^2
>     {delta_a^2||M_a||^2
>       +2delta_a<M_a,C_a>+||C_a||^2}.             (3.4)
> ```

Consequently, if `T_1^reset(xi)` is (2.3) applied to the reset-coordinate
direct sum, then the exact actual-history recursion is

```text
T_1(xi)=T_1^reset(xi)
 +sum_(live (d,t)) sum_(a=0)^(d-1) eta_(d,t) B_a. (3.5)
```

**Proof.** Bayes' identity is

```text
L_a dmu=pi_a dmu_a.                                (3.6)
```

It gives the sensitive normalization

```text
E_mu||f_a||^2
 =(eta/pi_a)E_mu[L_a^2||Phi_a||^2]
 =eta E_(mu_a)[L_a||Phi_a||^2],                   (3.7)
```

not `eta E_mu[L_a||Phi_a||^2]`. It also gives

```text
E_mu[(U-p)f_a]
 =sqrt(eta*pi_a)(delta_a M_a+C_a).                (3.8)
```

Expanding the squared norm of (3.1) in (3.7) produces the first six terms
of (3.4), including all three vector cross terms. Squaring (3.8) produces
the final brace. Orthogonality of distinct history blocks then proves (3.5).
The killed `a=d` block never appears. QED.

There is an equivalent second-posterior form. Let

```text
muhat_a=Beta(D+2a,kappa-D+2(d-a)).                 (3.9)
```

Since `L_a dmu_a=lambda_0 dmuhat_a`, every quantity in (3.3) is
`lambda_0` times its corresponding `muhat_a` expectation. Thus (3.4) is an
exact recursion if `Z_a` is retained as the full Hilbert-valued polynomial,
or if all five required weighted `Z` moments are retained. The decomposition
symbol `(M,C,Z)` does not mean that one scalar norm of `Z` suffices.

## 4. Exact finite-summary nonclosure

Take parent `mu=Beta(1,1)`, degree `d=1`, retained `a=0`, killed `a=1`, and
child `mu_0=Beta(1,2)`. Then `L_0=1-u` and `pi_0=1/2`. The monic child
Jacobi polynomials of degrees two and three are

```text
P_2(u)=u^2-(4/5)u+1/10,             ||P_2||^2=1/300,
P_3(u)=u^3-(9/7)u^2+(3/7)u-1/35,   ||P_3||^2=1/4900.   (4.1)
```

For `Z_j=P_j/||P_j||`, both unrestricted operator inputs have

```text
M=0, C=0, ||Z_j||^2=1, T_1(child)=1.               (4.2)
```

Their unit-exterior parent charges are nevertheless

```text
E_(Beta(1,2))[(1-U)Z_2(U)^2]=18/35,
E_(Beta(1,2))[(1-U)Z_3(U)^2]=32/63.                (4.3)
```

The parent first-mode subtraction vanishes by child orthogonality. Hence the
two inputs have identical `(M,C,||Z||^2)` and identical scalar child `T_1`,
but distinct exact transfers. This proves nonclosure of those finite
summaries. These are unrestricted operator examples; neither polynomial is
asserted to be a complete actual-history child feature.

## 5. Terminal operator aggregate

For the fresh law `Beta(1,1)`, M167/M170's accepted normalized constant-child
charge at degree `d` is

```text
R_d=(d+1)/(2d+1)[4^d/binom(2d,d)-1]
    -d/(d+2)+3d^2/[(d+1)(d+2)^2].                 (5.1)
```

For the terminal `h=1` exterior, put `n=L-1`, `d=r+1`, and

```text
eta_(n,r)=c(n,r)/[(r+1)!w_(n+2)],
c(n,r)=r n^(n-r-1)/(n-r)! .                       (5.2)
```

The formula includes `r=n`, where `c(n,n)=1`.

> **Lemma 5.1 (linear constant-child charge).** For every integer `d>=2`,
>
> ```text
> R_d<=3d/8,                                       (5.3)
> ```
>
> with equality only at `d=2`.

**Proof.** Put `A_d=4^d/binom(2d,d)`. The last two terms of (5.1) have sum

```text
d/(d+2)[-1+3d/((d+1)(d+2))]<0                    (5.4)
```

because `(d+1)(d+2)-3d=d^2+2`. Hence

```text
R_d<(d+1)A_d/(2d+1).                              (5.5)
```

Also `A_1=2` and

```text
A_(d+1)/A_d=(2d+2)/(2d+1)<=sqrt((d+1)/d),         (5.6)
```

where the squared inequality is
`4d(d+1)<=(2d+1)^2`. Induction gives `A_d<=2sqrt(d)`. For `d>=8`,

```text
R_d<=(18/17)sqrt(d)<=3d/8;                        (5.7)
```

the last inequality follows from `sqrt(d)>=48/17`. The six exact slacks
`3d/8-R_d` for `d=2,...,7` are

```text
0, 277/1400, 89/210, 8579/12936,
3365/3696, 89821/77220.                           (5.8)
```

This completes all degrees. QED.

> **Lemma 5.2 (exact terminal first moment).** For every `n>=1`,
>
> ```text
> sum_(r=1)^n (r+1)eta_(n,r)
>   =((n+1)/(n+2))^n<=2/3.                        (5.9)
> ```

**Proof.** Direct substitution and the binomial theorem give

```text
sum_(r=1)^n c(n,r)/r!
 =sum_(r=1)^n n^(n-r-1)/[(r-1)!(n-r)!]
 =(n+1)^(n-1)/n!.                                 (5.10)
```

Dividing by `w_(n+2)=(n+2)^(n+1)/(n+2)!` yields the equality in (5.9),
including the boundary `r=n`. At `n=1` the value is `2/3`. For `n>=2`,
Bernoulli's inequality gives

```text
(1+1/(n+1))^n>=1+n/(n+1),
```

so the reciprocal is at most `(n+1)/(2n+1)<2/3`. QED.

> **Theorem 5.3 (fresh terminal quarter bound).** For every `n>=1`,
>
> ```text
> S_n:=sum_(r=1)^n eta_(n,r)R_(r+1)<=1/4.         (5.11)
> ```

**Proof.** Lemmas 5.1--5.2 give

```text
S_n<=3/8 sum_(r=1)^n (r+1)eta_(n,r)<=1/4.         (5.12)
```

Equality holds at `n=1`; the inequality is strict for `n>=2`. QED.

This is a uniform analytic theorem, not an inference from finite values. It
strengthens M167's factorial summability for the fresh constant-child
operator sector. It is not by itself a parent budget inequality.

## 6. Actual-history fresh `h=1` descendant sector

Consider a fresh right-heavy parent

```text
xi=(B+L,2,1,B),       L>=1,                       (6.1)
```

and only its live `h=1`, equivalently `t=B+1`, descendant contribution to
`T_1`. Put

```text
q_0=q_(B,0)=w_1 w_B/w_(B+1).                     (6.2)
```

Every retained child is `(B,2+d,1+a,B)`, hence has suffix excess zero. By
the accepted M109/M114 all-deficit theorem,

```text
F(child)<=1-q_0.                                  (6.3)
```

M162/M165's degree bound makes its feature constant in `u`, so
`Phi_child=M_child` and `||M_child||^2=F(child)`. Each scalar `Q` coefficient
in (5.1) is nonnegative by orthogonal projection.

Here is the normalization explicitly. For `L>=2`, the live terminal roots
have

```text
t=B+1,        n=L-1,
d=r+1,        r=1,...,n.                          (6.4)
```

Summing the stationary masses of all prefixes of length `r` and total `n`
gives `c(n,r)`. After multiplying by the child/parent split ratio in
M162's `eta=m_s(d,t)q_child/q_parent`, the grouped exterior is exactly

```text
eta_(n,r)=c(n,r)/[(r+1)!w_(n+2)],                 (6.5)
```

with no additional `q_0`, parent-`q`, or observation factor. Freshness means
the parent law is `Beta(1,1)`, hence `pi_a=1/(d+1)`. For a fixed child
constant vector `M_a`, summing the exact retained coordinate charges over
`a=0,...,d-1` gives

```text
eta_(n,r) R_d ||M_a||^2                           (6.6)
```

when the norm is common; with the actual observation-dependent children it
is bounded by the same expression with
`max_(a<d)||M_a||^2`. Equation (6.3) bounds every one of those norms by
`1-q_0`. Therefore grouping exact root/Cayley coefficients gives

```text
T_1^(h=1)(xi)
 <=(1-q_0) sum_(r=1)^n eta_(n,r)R_(r+1).          (6.7)
```

For `L>=2`, Theorem 5.3 proves the standalone actual-history bound

```text
T_1^(h=1)(xi)<=(1-q_0)/4.                         (6.8)
```

At the exceptional one-layer boundary `L=1`, `(n,r)=(0,0)`, the only degree
is `d=1`, its exterior coefficient is one, and `R_1=1/2`. Thus

```text
T_1^(h=1)(xi)<=(1-q_0)/2.                         (6.9)
```

If `B=1`, the child target is inactive and both bounds are trivially zero.
Equations (6.8)--(6.9) close only the fresh terminal descendant sector. They
do not include the parent's reset term, any `h>=2` descendant, or a
right-heavy parent with `kappa>2`.

## 7. Dependencies, boundary checks, and first unresolved step

Accepted dependencies are M147/M151's all-suffix attachment/root
coefficients, M157/M160's shared-observation kernel, M162/M165's
actual-history feature and degree bound, M167/M170's formula (5.1) and
terminal coefficient (5.2), and M109/M114's all-deficit suffix-zero theorem.
Every cited frozen SHA ledger verifies. M170's correction at `r=n` is handled
explicitly in Lemma 5.2.

Boundary audit:

- `a=d` is killed exactly in every recursion formula.
- At suffix excess `L=0`, the absent first mode is zero-extended; no child
  recursion is needed.
- The exceptional terminal `L=1,d=1` row is separated because (5.3) begins
  at `d=2`.
- `B=1` yields an inactive suffix-zero target.
- Original-chain cases `m` odd, `m=0,2`, and `N=2` do not enter this
  separated auxiliary statement and receive no new conclusion.

The first unresolved standalone lemma is now narrower:

> Bound the aggregate (3.5) for a fresh parent after removing the proved
> `h=1` contribution (6.5), retaining the full weighted `Z` moments for every
> `h>=2` child and the exact reset cross terms. A closure on
> `(M,C,||Z||^2)` is impossible by Section 4. The resulting total, not each
> branch separately, must be compared with `1-q_parent`.

No `L=7` enumeration or broad scan was run.

## 8. Compact exact audit

Run from this mission directory:

```text
python3 -B terminal_modal_exact.py --output terminal_modal_exact.json
```

Python 3.12.3, standard library only, deterministic `seed=null`. The checker
imports no predecessor code. It verifies one asymmetric two-coordinate
instance of every term in (3.4), both exact nonclosure witnesses, all six
rational bases (5.8), and five selected eta/aggregate identities including
the equality row `n=1`. It reports zero failures. These checks audit the
algebra; Theorems 3.1 and 5.3 and the all-degree proofs above establish the
claims.
