# M177 independent proof audit of frozen M173

Date: 2026-08-13 UTC.

## 1. Integrity and scope gate

Before reading the mathematical payload, I ran

```text
sha256sum -c SHA256SUMS
```

in frozen M173. All seven recorded payloads passed, the inventory agreed with
`freeze_manifest.md`, and no M173 file was changed. The audited target is only
the normalized unweighted reset excursion `F=H/q` in the auxiliary nonlazy
minimal-long-cycle parking projection. The project target remains the uniform
fixed-length identity-transposition bridge law. No sampler, gap, original-chain
mixing result, Terminal A, or Terminal B is under audit here.

## 2. Exact retained-branch AMV identity

Let `L_a dmu=pi_a dmu_a` and

```text
f_a=sqrt(eta/pi_a)L_a Phi_a.
```

Applying Bayes to `L_a||Phi_a||^2`, rather than to `||Phi_a||^2`, gives

```text
E_mu||f_a||^2
 =(eta/pi_a)E_mu[L_a^2||Phi_a||^2]
 =eta E_mu_a[L_a||Phi_a||^2].                     (2.1)
```

This is M173's sensitive trace normalization. Writing under `mu_a`

```text
Phi_a=M_a+x C_a/sigma_a^2+Z_a,
x=U-p_a,
E Z_a=E[xZ_a]=0,
```

the weighted trace in (2.1), divided by `eta`, expands into exactly six
terms:

```text
lambda_0||M||^2,
2lambda_1<M,C>/sigma_a^2,
lambda_2||C||^2/sigma_a^4,
2<M,Z_0>,
2<C,Z_1>/sigma_a^2,
Z_2.                                               (2.2)
```

There is no orthogonality cancellation after insertion of `L_a`; all three
cross terms in (2.2) are necessary. Independently,

```text
E_mu[(U-p)f_a]
 =sqrt(eta*pi_a)(delta_a M_a+C_a),
```

so the first-mode subtraction is

```text
eta*pi_a ||delta_a M_a+C_a||^2/sigma_parent^2.    (2.3)
```

This retains the signed covariance cross term. The observation `a=d` is the
killed rank `j=0` and is omitted before the direct-sum norm is taken; there is
no conditioning on survival. Exact rational recomputation of (2.1)--(2.3) on
an asymmetric two-coordinate polynomial produced the six signed trace terms
independently and passed.

## 3. Unrestricted finite-summary obstruction

Under the child law `Beta(1,2)`, direct Gram calculations give

```text
P_2=u^2-4u/5+1/10,       ||P_2||^2=1/300,
P_3=u^3-9u^2/7+3u/7-1/35, ||P_3||^2=1/4900.
```

Both are orthogonal to the child constant and first mode. After unit
normalization, both therefore have `(M,C,||Z||^2,T_1)=(0,0,1,1)`. Direct
integration against the retained likelihood `1-u` gives charges `18/35` and
`32/63`. Thus the displayed finite summaries do not determine the exact
lift. This is correctly labeled an unrestricted-operator refutation, not an
actual-history counterexample.

## 4. The all-degree constant-child bound

Put `A_d=4^d/binom(2d,d)`. In M173's formula for `R_d`, the last two terms
sum to

```text
d/(d+2)[-1+3d/((d+1)(d+2))]<0,
```

because the missing numerator is `d^2+2`. Also

```text
A_(d+1)/A_d=2(d+1)/(2d+1)<=sqrt((d+1)/d),
```

so `A_d<=2sqrt(d)`. For `d>=8`,

```text
R_d<(d+1)A_d/(2d+1)
    <=(18/17)sqrt(d)<=3d/8.
```

The last step is exactly `sqrt(d)>=48/17`, true from `d=8`. Independent
rational integration of every retained coordinate reproduces `R_d` and the
six listed slacks for `d=2,...,7`. Equality occurs only at `d=2`. Hence the
all-degree proof, not merely its finite bases, is valid.

## 5. Exact terminal first moment, including `r=n`

For `n>=1`, substituting

```text
eta_(n,r)=c(n,r)/[(r+1)!w_(n+2)]
```

gives

```text
sum_(r=1)^n (r+1)eta_(n,r)
 =1/w_(n+2) sum_(r=1)^n c(n,r)/r!
 =1/w_(n+2) (n+1)^(n-1)/n!
 =((n+1)/(n+2))^n.                                (5.1)
```

The `r=n` summand is included because `c(n,n)=1`; no negative-power product
estimate is being used. The value is `2/3` at `n=1` and is smaller thereafter.
Combining (5.1) with `R_(r+1)<=3(r+1)/8` proves

```text
sum_(r=1)^n eta_(n,r)R_(r+1)<=1/4,
```

with equality only at `n=1`.

## 6. Actual-history `h=1` exterior and varying observations

For a fresh parent `xi=(B+L,2,1,B)`, let `n=L-1`. A live `h=1` root has
`t=B+1`, degree `d=r+1`, and root-group mass

```text
m_s(d,t)=w_(B+1)c(n,r)/[(r+1)!w_(B+L+1)].         (6.1)
```

Its child has suffix excess zero, so

```text
q_child/q_parent
 =[w_B/w_(B+1)]/[w_(n+2)w_B/w_(B+L+1)]
 =w_(B+L+1)/[w_(B+1)w_(n+2)].                    (6.2)
```

Multiplying (6.1)--(6.2) proves exactly

```text
eta=m_s q_child/q_parent
   =c(n,r)/[(r+1)!w_(n+2)].                       (6.3)
```

There is no additional split, observation, `q_0`, or parent-`q` factor.
Selected independent exact rows include both `r<n` and `r=n` and multiple
values of `B`; all reduce to (6.3).

Freshness gives `pi_a=1/(d+1)`. For a constant observation-dependent child
vector, define `e_a=L_a/sqrt(pi_a)`. Its exact coordinate charge is

```text
eta Q(e_a)||M_a||^2.
```

Crucially, every scalar coefficient is nonnegative:

```text
Q(e_a)=||e_a-Proj_span(U-1/2)e_a||^2 >=0.         (6.4)
```

Therefore, without assuming a common vector or common norm,

```text
sum_(a<d) eta Q(e_a)||M_a||^2
 <=eta max_(a<d)||M_a||^2 sum_(a<d)Q(e_a)
 =eta R_d max_(a<d)||M_a||^2.                    (6.5)
```

The child coordinates are `kappa'=d+2`, `D'=a+1`, hence in `(K,R)` notation
`K'=d+1`, `R'=d-a`. For every retained `a<d`, `K'>R'>=1`; when `B>=2` this
is exactly M109/M114's active reachable suffix-zero sector. Their accepted
theorem yields

```text
||M_a||^2=F(child)<=1-q_(B,0).
```

Equations (6.3)--(6.5) and the quarter theorem prove M173's actual-history
`h=1` bound for `L>=2`.

## 7. Boundaries and numbered objections

1. **Material objections: none.** The audited claims and normalizations are
   correct within their stated auxiliary scope.
2. **Nonmaterial expository point.** Positivity belongs to each projection
   residual `Q(e_a)`, not to the three algebraic summands of the closed
   aggregate formula for `R_d`. M173's max argument is valid when read in
   this coordinatewise sense; (6.4) makes the reason explicit.
3. **Scope guard.** The result removes only live fresh-parent `h=1`
   descendants. It gives no bound for reset terms, `h>=2`, nonfresh parents,
   the total AMV budget, a gap, or either project terminal. M173 states this
   limitation correctly.
4. **Boundary wording.** At `B=1`, the live condition `t-1>=2` already removes
   the `h=1` group; describing its would-be child as inactive is equivalent
   and does not alter the zero contribution.

At `L=1`, `(n,r)=(0,0)`, direct normalization gives `eta=1` and direct
projection gives `R_1=1/2`, so the separate `(1-q_0)/2` bound is correct.
At `L=0`, no `h=1` descendant exists and the absent first mode is harmlessly
zero-extended. Original-chain cases `m` odd, `m=0,2`, and `N=2` are outside
this auxiliary statement.

