# Canonical marked-flow reduction and exact deep contraction

Date: 2026-08-12.  This note concerns only the full nonlazy
minimal-long-cycle parking projection `Pbar_s`.  It is not a theorem about
the identity bridge chain `K`.

## 1. Normalization and status

Permutations compose as `(pq)(x)=p(q(x))`, and factor tuples multiply
left-to-right.  Write

```text
alpha_s=2/[3s(s-1)],              G_s=R_s/alpha_s,
rho_s(C)=w_(s+1)^(-1) [1/k!] product_i w_(c_i),
w_a=a^(a-1)/a!,                   C=(c_1,...,c_k).
```

For a contextual mark `x=(s,K,R,B)`, let `H_x` be M65's root-composition
conditional mean and

```text
q_x=E_rho H_x=w_(s+1-B)w_B/w_(s+1).
```

Sections 2--6 below are universal proved statements.  Section 7 is a
proved audit explaining why they do not yet give an actual-edge flow.
The surviving proposition is isolated in Section 9.

## 2. Every canonical quotient residual resets to a right-heavy mark

Route a root-composition charge to the one-part hub by repeatedly merging
the first two parts.  A used quotient edge has refined endpoint

```text
e: (A,c_2,...,c_k) -> (A+c_2,c_3,...,c_k),          k>=2.       (2.1)
```

In M56's residual formula, the boundary position `p` is the number of
displayed boundaries strictly to the left of the merged boundary.  Thus
the first-boundary route has `p=0`.  Substitution in M71 equation (H.1)
gives the child

```text
y_e=(A+c_2-1, k-1, k-2, c_2).                      (2.2)
```

In particular, every quotient child is right-heavy:

```text
K_y-R_y=1.                                         (2.3)
```

This is an exact accounting statement.  It does not say that later deep
inheritance remains right-heavy; a deep child is
`(t-1,K+k,R+j,B)` and can have `K-R+k-j>1`.

## 3. Canonical quotient energy

Put `g=H_x-q_x`.  For (2.1), let `B_e` be the M50 source basin: all
compositions obtained by arbitrarily refining `A`, with the displayed
suffix `(c_2,...,c_k)` fixed.  The canonical current is

```text
theta_x(e)=sum_(C in B_e) rho_s(C)g(C).             (3.1)
```

This has the correct divergence `rho_s g`, because the first-merge edges
form a tree oriented to the one-part hub.  M50 gives

```text
rho_s(B_e)<=e rho_s((A,c_2,...,c_k)),
Q_G(e)=rho_s((A,c_2,...,c_k)) k.                    (3.2)
```

Cauchy--Schwarz and (3.2) imply

```text
theta_x(e)^2/Q_G(e)
 <=(e/k) sum_(C in B_e)rho_s(C)g(C)^2.              (3.3)
```

A source composition with `ell` parts belongs to exactly the basins of
the edges on its deterministic merge path, whose refined part counts are
`ell,ell-1,...,2`.  Summing (3.3) therefore proves

```text
E_can(g):=sum_e theta_x(e)^2/Q_G(e)
 <=e H_s^(harm) Var_rho(H_x)
 <=e(1+log s) Var_rho(H_x).                         (3.4)
```

Here `H_s^(harm)=sum_(j=1)^s 1/j`; it is unrelated to the contextual
mean `H_x`.  All capacities in (3.2)--(3.4) are for `G_s`; returning to `R_s` multiplies
the energy by `alpha_s^(-1)`, exactly as in M56.

There is also a uniform pointwise bound on the closed M65 mean.  First,

```text
w_a w_b/w_(a+b)<=1.                                 (3.5)
```

If `a,b>=2`, the left side is

```text
binom(a+b,a)(a/(a+b))^a(b/(a+b))^b (a+b)/(ab)<=1;
```

the binomial-probability factor is at most one and `ab>=a+b`.  If one
part is one, (3.5) reduces to `((n-1)/n)^(n-2)<=1`.

For the terminal line put `u=K-R`.  The numerator in

```text
T_(K,R)(k)
 =K binom(k+u-2,u-1)/binom(k+K-1,K-1)              (3.6)
```

increases with `u`, so setting `u=K` gives `T<=k`.  For fixed `(u,k)`,
`K/binom(k+K-1,K-1)` is nonincreasing in `K>=u`; setting `K=u` instead
gives `T<=u`.  The deep line is at most one by (3.5) and `D<=1`.
Since `k,u>=1`, this proves

```text
0<=H_x(C)<=min(s,K-R).                              (3.7)
```

For a nonnegative random variable `H<=M`,
`Var(H)<=E H^2<=M E H`.  Combining this with (3.4)--(3.7) yields the
normalized canonical base estimate

```text
a_can(x):=E_can(H_x-q_x)/q_x
 <=e(1+log s) min(s,K-R).                           (3.8)
```

By (2.3), every freshly reset quotient child satisfies the sharper bound

```text
a_can(y_e)<=e(1+log rank(y_e)).                     (3.9)
```

Equation (3.9), rather than an arbitrary-context maximum, is the usable
gain from the canonical route.

## 4. Exact stationary deep-descendant kernel

Put

```text
S=s+1-B,                         L=s-B=S-1.
```

There is no deep continuation when `S=1`.  Suppose `S>=2`, write
`n=s-t` for the total prefix size before the last part, and define

```text
A_n=sum_(p>=0) 1/(p+1)!
       sum_(a_1+...+a_p=n) product_i w_(a_i).        (4.1)
```

The empty prefix contributes `A_0=1`.  After stationary mass, the M65
deep split ratio, and `q_x` are cancelled, the total deep child measure is
bounded by the probability law

```text
P_S(n)=A_n w_(S-n-1)/w_S,          0<=n<=S-2.       (4.2)
```

The only discarded factor is `D_(K,R)(p+1)<=1`; summing the marked
negative-hypergeometric weights gives exactly that `D`.

To normalize (4.2), let

```text
T(z)=sum_(a>=1)w_a z^a=z exp(T(z)),
A(z)=sum_(n>=0)A_n z^n
    =(exp(T(z))-1)/T(z)=1/z-1/T(z).                 (4.3)
```

Then

```text
A(z)T(z)=T(z)/z-1,
```

and the coefficient of `z^(S-1)` is `w_S`, proving normalization.

The first moment is also exact.  From (4.3) and
`zT'(z)/T(z)=1/(1-T(z))`,

```text
sum_n n A_n w_(S-n-1)
 =[z^(S-1)] zA'(z)T(z)
 =[z^(S-1)] {-T(z)/z+1/(1-T(z))}.
```

Lagrange inversion gives

```text
[z^N]1/(1-T(z))=N^(N-1)/(N-1)!,
```

so

```text
E_(P_S)n=(S-1)^(S-1)/S^(S-2)-1.                   (4.4)
```

For `S>=8`, the standard inequality
`(1-1/S)^(S-1)>=e^(-1)` gives

```text
E n >=(S-1)/e-1 >=(S-2)/4.
```

Direct substitution in (4.4) verifies the same inequality for
`2<=S<=7`.  Thus universally

```text
E_(P_S)n >=(S-2)/4.                                (4.5)
```

This strengthens M65's asymptotic descendant calculation to an exact
finite-rank moment bound.

## 5. Fixed-factor suffix-excess contraction

For a deep child, the new suffix excess is

```text
L_y=(t-1)-B=S-n-2=L-1-n.                           (5.1)
```

Let `Wdeep(x,y)` denote the exact coefficient (H.4) in the separated
marked DAG, including the sum over `j`.  Equations (4.2), (4.5), and
`D<=1` prove

```text
sum_y Wdeep(x,y)L_y <=(3/4)(L-1)_+,                  (5.2)
sum_y Wdeep(x,y)(L_y+1) <=(3/4)(L+1).              (5.3)
```

For (5.3), use that the total deep weight is at most one:
the left side is at most
`1+(3/4)(L-1)=(3/4)L+1/4<=(3/4)(L+1)`.
When `L=0` there is no deep child; when `L=1`, every deep child has
`L_y=0`, and the same inequality holds.

Consequently, along a segment containing only deep inheritance, the
expected occupation of `L+1` is at most

```text
sum_(d>=0) (3/4)^d(L+1)=4(L+1).                    (5.4)
```

This is a genuine weighted/non-max contraction.  It handles every
stationary prefix composition and every collision of `j`-marks within the
same deep transition; it does not yet handle a new quotient reset.

## 6. Harmonic positional marks

Let `J` have M65's full negative-hypergeometric law on `0<=J<=k`.
Each of the `k` inner attachments lies before `O_(R+1)` with probability
`(R+1)/(K+1)`, hence

```text
E J=k(R+1)/(K+1).                                  (6.1)
```

For the child `(K+k,R+J)`, (6.1) gives the exact harmonic identities

```text
E [(R+J+1)/(K+k+1)] =(R+1)/(K+1),
E [(K-R+k-J)/(K+k+1)] =(K-R)/(K+1).                (6.2)
```

The actual deep recursion deletes the nonnegative `J=0` term.  Therefore
both fractions in (6.2) are superharmonic for the substochastic marked
deep kernel.  This prevents an exponential count of positional histories
at the level of their total weighted mass.  It does not bound the squared
load created by different quotient-reset origins on one actual edge.

## 7. What basin aggregation does, and does not, unmark

At the root-composition level, (3.1) already aggregates all source
histories in the same M50 basin.  Thus there is one current per canonical
quotient edge, not one current per refinement history, and its quotient
energy is the additive quantity (3.4).

Disintegrating that current over the actual fine crossing edges is exact
at the refined endpoint because the forward merge rate is pointwise
constant.  At the coarse endpoint, however, its density relative to the
conditional stationary law is

```text
Pbar_s(y,F_refined)/R_s(coarse,refined),            (7.1)
```

which is generally nonconstant.  The residual of (7.1) is precisely the
right-heavy child (2.2).  Basin aggregation does not make this residual
zero.

The smallest exact witness is `s=3`: the root composition `(1,2)` merges
with probability one to unary macro `(0,1,2)`, whereas the stationary law
inside root composition `(3)` assigns masses `1/3,2/3` to
`(0,1,1),(0,1,2)`.  Even after aggregating all starting root degrees,
canonical coalescence has endpoint densities `15/16,33/32`, not one.
Therefore a recurrence which simply drops all quotient-reset children is
not an accounting identity.  One must either prove cancellation after
grouping the signed right-heavy residuals, or route their aggregate with a
polynomial actual-edge load.

There is a polynomial number of *current* labels in ambient rank `r`:
along a deep segment, `K` increases by the current inner root degree, and
the rank drop is at least that degree, so `K<=K_0+r`; also
`0<=R<K`, `1<=B<=r`, and the active root and last reset edge have only
polynomially many locations.  This observation alone is insufficient.
Cauchy--Schwarz applied anew at every depth would multiply the label count;
the required bound must group histories once, or use an occupation
identity such as (5.4).

## 8. Two falsification facts

First, `(k,last part)` is not a strong lumping of `G_s`.  At `s=5`, the
compositions `(1,3,1)` and `(2,2,1)` both have `(k,last)=(3,1)`, but their
aggregate split rates to `(k,last)=(4,1)` are respectively

```text
2w_1w_2/w_3=4/3,             2w_1w_1/w_2=2.        (8.1)
```

Thus the closed form for `H_x` does not reduce the Green problem to a
strongly lumped `(k,last)` chain.

Second, `canonical_marked_probe.py` evaluates the exact rank-acyclic
separated recurrence with (3.1).  With all `K<=8`, every `R,B`, and the
additional displayed `K` slices through `4096`, its largest values through
rank fourteen are

```text
s       2     3     4     5     6     7     8
max T  .444  1.145 1.764 2.533 3.157 3.676 4.155

s       9    10    11    12    13    14
max T  4.654 5.083 5.458 5.803 6.153 6.463.
```

This is compatible with polynomial, roughly linear growth.  It is a finite
falsifier only and still uses separate capacity copies for marked residuals.

## 9. Remaining standalone proposition

Let `D` be the exact deep kernel (H.4), and let `J_can` be the canonical
quotient-reset kernel whose coefficient on (2.2) is
`theta_x(e)^2/[Q_G(e)q_x]`.  Every row of `J_can` lands in the right-heavy
set, while (5.3) gives a `3/4` contraction for `D` in suffix-excess weight.
The remaining analytic statement is:

> **CANONICAL RIGHT-HEAVY RESET OCCUPATION.**  Prove that the rank-acyclic
> Green expansion generated by `D+J_can`, started from any ambient-feasible
> contextual mark, has total base cost at most a universal polynomial in
> the ambient rank.  Equivalently, control repeated applications of
> `(I-D)^(-1)J_can` on the right-heavy reset set.  Then group the resulting
> signed reset currents on actual `Pbar` edges with only one polynomial
> source-recovery loss.

Equations (2.3), (3.9), (5.3), and (6.2) prove all one-segment inputs to
this proposition.  Equation (7.1) and the `s=3` witness show why the reset
operator cannot simply be omitted.  No infinite obstruction that survives
unmarking is proved here, and no polynomial energy comparison for actual
unmarked `Pbar` is yet claimed.
