# Infinite refutation of the inverse-split-mass supersolution

## Statement and scope

Let `D,J_can,q` be exactly the auxiliary marked kernels and split mass in
frozen M76. For the reachable right-heavy seeds

```text
x_s=(s,1,0,s),    s>=3,
```

put

```text
R_s=q_(x_s) sum_y [(I-D)^(-1)J_can](x_s,y)/q_y.
```

Then

```text
R_s >= q_s^3 sum_(A=1)^(s-1)(A/(A+1))^2,           (1)
q_s=w_s/w_(s+1)=(s/(s+1))^(s-1),
```

and consequently

```text
R_s >=(s-1)/108.                                    (2)
```

Thus M76's open inequality `R_s<=1` is false for infinitely many `s`.
Moreover, every proposed relaxed bound `R_s<=1+C/(s+1)` with fixed finite
`C` is false, and `(s+1)(R_s-1)=Omega(s^2)`.

This theorem concerns only the auxiliary nonlazy long-cycle parking
projection. It is neither a gap upper bound nor a conclusion for the original
identity-word heat-bath chain.

## Proof

For `B=s`, M65's contextual root observable is one on the unary composition
`(s)` and zero on every nonunary composition. No last part is greater than
`B`, so there are no deep transitions and `(I-D)^(-1)J_can=J_can` on this
row.

Restrict `J_can` to the canonical first-boundary edges with degree-two
refined endpoint

```text
(A,s-A)->(s),       1<=A<=s-1.
```

Write `b=s-A`. The source basin consists of every refinement of `A`, followed
by the fixed suffix `b`; it does not contain the unary composition. Hence its
current is `theta_A=-q_s rho(basin_A)`. The exact canonical capacity is

```text
Q_G(A,b)=2 rho(A,b).
```

M50's exact basin identity gives

```text
beta_A=rho(basin_A)/rho(A,b)
      =(2/w_A) sum_(p=1)^A C_(A,p)/(p+1)!.
```

The sum is M76's `A_A=[z^A](e^T-1)/T`. Since

```text
(e^T-1)/T=(T/z-1)/T=1/z-1/T
```

and `T=z e^T`, Lagrange inversion gives

```text
A_A=A w_A/(A+1),       beta_A=2A/(A+1).             (3)
```

The reset child is `(s-1,1,0,b)`, whose split mass is

```text
q_child=w_Aw_b/w_s.
```

Also

```text
rho(A,b)=w_Aw_b/(2w_(s+1))=(q_s/2)q_child.
```

Therefore this one edge contributes to the transformed row

```text
theta_A^2/[Q_G(A,b)q_child]
 =q_s^2 beta_A^2 rho(A,b)/(2q_child)
 =q_s^3 beta_A^2/4
 =q_s^3(A/(A+1))^2.
```

Summing proves (1). Since `q_s>=e^-1` and `A/(A+1)>=1/2`, (2) follows.

For completeness,

```text
sum_(A=1)^(s-1)(A/(A+1))^2
 =s-2H_s+H_s^(2),
```

so the degree-two subrow alone is asymptotic to `e^-3 s`. The exact full
row grows faster: grouped finite values have `R_40=2.1637325`,
`R_80=4.4618404`, and `R_200=11.4579066`.

## Surviving occupation lemma

The negative theorem does not refute polynomial occupation. It shows only
that `h=1/q` is the wrong multiplicative supersolution. The narrow surviving
statement is

> **DEEP-ELIMINATED RESET SUBSTOCHASTICITY.** For every right-heavy reset
> seed `x=(s,K,K-1,B)`, prove
> ```text
> [(I-D)^(-1)J_can]1(x)<=1.
> ```

Because every reset strictly lowers the integer `P=s+K-R`, this statement
would give

```text
sum_(n<P) delta_x K_reset^n 1 <=P.
```

Together with M76's `b(x)<=eP^2(1+log P)`, this yields separated marked base
occupation at most `eP^3(1+log P)`—indeed slightly sharper than M76's
conditional inverse-`q` bound.

Independent exact enumeration over every context through `s=7,K<=6`
supports the stronger multitype candidate

```text
K_reset 1(x)<=(K-R)(1-q_x),
```

whose right-heavy specialization is `<=1-q_x`. A direct one-step induction
is false: `(D+J)1` can exceed one, so any proof must use the full
pure-deep-eliminated filtration or an augmented-event martingale. Grouped
right-heavy scans attain `.690924` through `s=14`, `.756830` through `s=20`,
and `.808200` on the seed slice through `s=30`. These are finite discovery
facts, not a proof of the lemma.
