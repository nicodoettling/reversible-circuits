# M165 proof audit of frozen M162

Date: 2026-08-13 UTC.

## 1. Immutable gate and exact scope

All coordinator-supplied hashes match, and M162's complete `SHA256SUMS`
verifies from the frozen directory:

```text
f0916943bbd47b9245bf8171e3598ee1e3aeb50f9e54d036c49c6ff898fd02a7  report.md
989d83d74038a7734e79883b56ea5cd285b28d1e3648216c8fa8a5f7e12a3862  vector_beta_theorem.md
4347755c5dac4751534514d9ae43133a9fd0d299bbd7ada875671a651d769094  vector_beta_exact.py
fc4b0506e14a044fa0727e08f67d70f3c8caccc77b186184b78fe20ce3b325d3  vector_beta_exact.json
2dc7b122eb9ee19af9a0f5998e24833c0d72b6f800eee54d3c6d8e269eea6031  freeze_manifest.md
```

The audited object is only `F=H/q`, the normalized full unweighted reset
excursion in the auxiliary nonlazy minimal-long-cycle parking projection.
The project target remains uniform fixed-length identity transposition words,
with `(pq)(x)=p(q(x))` and displayed factors left-to-right.  No sampler,
all-suffix contraction, gap, polynomial mixing theorem, or project terminal
is part of M162's proved scope.

## 2. Actual-history scaling and normalization

Write `q_x=q_(B,L)` and let one live root group have mass `m`, degree `d`,
last part `t`, and child split mass `q_y`.  For retained observation `a<d`,
let

```text
pi_a=E_x L_a(U),
eta=m q_y/q_x,
L_a(u)=binom(d,a)u^a(1-u)^(d-a).
```

M162's child feature coordinate is

```text
sqrt(eta/pi_a) L_a(u) Phi_y(u).
```

Its Gram term is therefore

```text
(eta/pi_a)L_a(u)L_a(v)K_y(u,v),
```

which is exactly M157/M160's accepted shared-observation transfer with the
normalized exterior coefficient `m q_y/q_x`.  Bayes gives

```text
L_a dmu_x = pi_a dmu_y.
```

Thus the mean child coordinate is `sqrt(eta*pi_a) M_y`; its squared norm is
`eta*pi_a F(y)`.  This equals the normalized scalar recurrence term

```text
m pi_a H(y)/q_x = (m q_y/q_x)pi_a F(y).
```

This confirms all three sensitive factors: `q_y/q_x`, one denominator
`pi_a` rather than `pi_a^2`, and one retained branch probability after taking
the mean.  The branch `a=d` is omitted, not survival-conditioned.  The compact
checker independently verifies retained mass `1-pi_d` in three asymmetric
beta-binomial cases.

The reset coordinate `J_E/sqrt(q_x c_E)` gives
`J_E(u)J_E(v)/(q_x c_E)`, so its mean-square contribution is exactly
`A_0/q_x`.  On the diagonal, Bayes leaves

```text
eta integral L_a(u)||Phi_y(u)||^2 dmu_y(u),
```

confirming M162 equation (4.7).  Suffix excess decreases along every child,
so the recursive direct sum is finite.  Its degree is at most `L`: reset
currents have that bound, while a branch satisfies
`d+(t-1-B)<=L` because the `d-1` preceding positive parts sum to `s-t`.

## 3. Jacobi convention, Parseval, and the upper bound

Under `z=2u-1`, the standard weight
`(1-z)^alpha(1+z)^beta` becomes a constant times
`(1-u)^alpha u^beta`.  Hence `Beta(D,kappa-D)` requires

```text
(alpha,beta)=(kappa-D-1,D-1),
```

exactly as M162 states.  Independent exact Gram--Schmidt reproduces, for
example,

```text
Beta(1,4): P_1=u-1/5,
           P_2=u^2-(4/7)u+1/21;
Beta(4,1): P_1=u-4/5,
           P_2=u^2-(10/7)u+10/21.
```

For the finite vector polynomial `Phi`, scalar Parseval in each actual-history
coordinate and summation over coordinates give

```text
S=sum_(n=0)^L ||A_n||^2,
F=||A_0||^2,
T_r=S-sum_(n=1)^r ||A_n||^2
   =F+sum_(n=r+1)^L ||A_n||^2 >= F.
```

No positivity of the signed pointwise kernel is used.  This is a valid
actual-history upper bound.  The endpoint `r=L` is tautological, as M162
explicitly says.

There is one nonmaterial notation clarification: Theorem 3.1 defines `T_r`
for `r<=L`, whereas the open `T_1` boundary is stated for `L>=0`.  At `L=0`,
one should either state the row separately or define the absent `A_1` as zero;
then `T_1=T_0=F` and the boundary is trivial.  This does not change any
claimed theorem or finite row.

## 4. First centered mode

Let `p_x=D/kappa`, `C_x=E[(U-p_x)Phi_x]`, and
`sigma_x^2=Var_x(U)`.  Since the monic first polynomial is `U-p_x`, its
energy is `||C_x||^2/sigma_x^2`.

For a retained branch, write `delta=p_y-p_x`.  Bayes gives exactly

```text
E_x[(U-p_x)L_a(U)Phi_y(U)]
 =pi_a E_y[(U-p_x)Phi_y(U)]
 =pi_a(delta M_y+C_y).
```

After multiplying by the feature scale and using orthogonality of distinct
history blocks, its first-mode contribution is

```text
eta*pi_a/sigma_x^2 ||delta M_y+C_y||^2.
```

Expansion retains
`delta^2||M_y||^2+2delta<M_y,C_y>+||C_y||^2`; neither the signed cross term nor
its sign can be discarded.  The killed `a=d` block is absent.  This proves
M162 equations (4.4)--(4.6).

## 5. Independent compact exact check

`independent_referee.py` imports no predecessor code and uses a different
representation: a rational list of weighted univariate features
`K=sum weight*f tensor f`.  Equal polynomial features are merged only by
adding positive weights.  It checks 42 shared-observation monomial-pair
identities, asymmetric Jacobi laws, and exactly the four reported repair
states—no grid.

| state `(s,kappa,D,B)` | trace | first energy | `T_1` | `1-q` |
|---|---:|---:|---:|---:|
| `(8,2,1,2)` | 0.8136933467 | 0.3205346599 | 0.4931586868 | 0.8032201338 |
| `(7,2,1,3)` | 0.8552821152 | 0.3075458600 | 0.5477362551 | 0.8497962952 |
| `(8,2,1,3)` | 0.9398822216 | 0.3381835264 | 0.6016986952 | 0.8634354519 |
| `(9,2,1,3)` | 1.0055813860 | 0.3612150815 | 0.6443663045 | 0.8729390800 |

Every displayed quantity is computed as an exact fraction and matches the
frozen M162 value.  At each state the clean-room check also verifies:

- feature mean-square equals an independent scalar `H/q` recursion;
- feature trace equals the likelihood-weighted diagonal recursion;
- modal energies are nonnegative and sum exactly to the trace;
- degree-zero energy equals `H/q`, hence `T_1>=H/q`;
- the `delta M+C` recursion equals the directly computed first energy; and
- trace exceeds the budget while `T_1` is below it.

The run has zero failures.  This independently supports the four finite
repair rows, but it supplies no information at `L>=7`.

## 6. Referee disposition

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CLARIFICATION: define the absent degree-one mode as zero at L=0,
or state that trivial boundary separately.
```

Promote M162 only as an exact feature/Jacobi reduction and exact finite
`L<=6` evidence.  The all-suffix `T_1` boundary, all-suffix contraction,
auxiliary gap, `ROOT-MEAN LIFT`, original-chain gap, polynomial mixing,
Terminal A, and Terminal B remain unresolved.
