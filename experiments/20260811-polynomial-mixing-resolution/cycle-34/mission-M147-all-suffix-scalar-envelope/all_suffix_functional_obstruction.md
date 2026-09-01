# M147 all-suffix functional envelope and scalar nonclosure

Date: 2026-08-13 UTC.

## 1. Scope and status

This note concerns only the full unweighted reset excursion of the auxiliary
nonlazy stationary-flow parking-degree projection in the minimal-long-cycle
sector.  It proves no auxiliary gap, ROOT-MEAN LIFT, original-chain gap,
polynomial mixing result, Terminal A, or Terminal B.

The project target remains uniform on fixed-length identity transposition
words.  Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors
left-to-right.

The results are:

1. an exact all-suffix functional recurrence on the attachment state
   `(kappa,D)`;
2. its corrected one-power exceptional-current envelope using the accepted
   `C_s<3/4` input where applicable;
3. an infinite reachable family proving that suffix data, `q`, `C_s`, any
   finite collection of Cayley ratios, and even `K` (or `z=1/(K+1)`) do not
   form a closed Bellman state when the deficit `D=K-R` is omitted; and
4. a precise first necessary additional statistic: `D`, equivalently
   `p=D/(K+1)`.  The exact recurrence is closed by the pair `(kappa,D)`.

No claim is made that this obstruction rules out every possible amortized
argument which allows a child envelope to exceed its local budget and pays
that excess elsewhere.

## 2. Exact suffix coordinates

Put

```text
w_n=n^(n-1)/n!,
b_n=w_n/w_(n+1)=(n/(n+1))^(n-1),
c(n,p)=p n^(n-p-1)/(n-p)!,  c(0,0)=1.
```

Fix a bottom rank `B>=1` and suffix excess `L>=0`, so `s=B+L`.  Define

```text
q_(B,L)=w_(L+1)w_B/w_(B+L+1)
       =w_(L+1) product_(r=B)^(B+L)b_r.
```

For an attachment context set

```text
kappa=K+1,  D=K-R.
```

The accepted reachable closure is the fresh state `(K,R)=(1,0)`, hence
`(kappa,D)=(2,1)`, together with `K>R>=1`.  For a root group of degree `d`,
the exact attachment law is

```text
nu_(kappa,D,d)(j)
 =binom(d,j)(D)^(rise)_(d-j)(kappa-D)^(rise)_j
   /(kappa)^(rise)_d,               j=0,...,d.       (2.1)
```

This is just the accepted binomial formula after writing
`R+1=kappa-D`.  Vandermonde's identity proves that (2.1) sums to one.
A retained rank `j>=1` changes the state by

```text
(kappa,D) -> (kappa+d,D+d-j).                       (2.2)
```

Thus the deficit is preserved only on the `j=d` branch; all smaller
positive ranks create non-right-heavy descendants.

## 3. Root support in suffix form

For `h=0,...,L`, let the last root part be `t=B+h`.  Let `alpha` be an
ordered composition of `L-h`, and put `d=length(alpha)+1`.  Write

```text
P_(B,h)=w_B/w_(B+h)=product_(r=B)^(B+h-1)b_r,
q_(B,h-1)=w_h w_B/w_(B+h)             (h>=1).
```

The exact stationary root mass divided by `q_(B,L)` is

```text
rbar_(L,B)(h,alpha)
 =product_i w_(alpha_i)/[d! w_(L+1)P_(B,h)].        (3.1)
```

Its contextual mean is

```text
f_(kappa,D)(h,alpha)
 = d (D)^(rise)_(d-1)/(kappa)^(rise)_(d-1),        h=0,

 = q_(B,h-1)[1-(D)^(rise)_d/(kappa)^(rise)_d],     h>=1.  (3.2)
```

Summing (3.1) over compositions of fixed length gives the normalized group
mass

```text
mbar_(L,B)(h,d)
 =c(L-h,d-1)/[d! w_(L+1)P_(B,h)].                  (3.3)
```

The exact root-mean identity is

```text
sum_(h,alpha) rbar(h,alpha)f(h,alpha)=1.            (3.4)
```

Equations (3.1)--(3.4) are definitions-level identities, not an
extrapolation from the `L<=5` tables.  In particular, they organize all
`2^L` supported rows without enumerating `L=6`.

## 4. Exact all-suffix functional recurrence

Let

```text
F_(B,L)(kappa,D)=H(B+L,kappa-1,kappa-1-D,B)/q_(B,L).
```

Let `A_(B,L)(kappa,D)` be the exact active canonical reset energy divided by
`q_(B,L)`.  The accepted all-`j` recurrence becomes

```text
F_(B,L)(kappa,D)
 =A_(B,L)(kappa,D)
  +sum_(h=1)^L 1[B+h-1>=2]
    sum_d mbar_(L,B)(h,d)
    sum_(j=1)^d nu_(kappa,D,d)(j) q_(B,h-1)
      F_(B,h-1)(kappa+d,D+d-j).                    (4.1)
```

Only `j=0` and rank-one targets are killed.  Every child has suffix excess
`h-1<L`; the accepted phase also strictly decreases.  Therefore (4.1) is a
finite nilpotent recursion for every fixed state.  It is the requested
all-suffix functional envelope before any inequality is imposed.

The crucial point is visible in (4.1): a scalar `E_L` cannot substitute the
right-heavy value at every child, because `D+d-j` ranges through
`D,...,D+d-1`.

## 5. Corrected one-power reset envelope

For a supported canonical endpoint `E`, normalize by the parent split mass:

```text
cbar_E=c_E/q,  abar_E=a_E/q,  thetabar_E=theta_E/q,
lambda_E=b_E/c_E,
```

where `c_E=degree(E)rho(E)`, `b_E=rho(B_E)`, and
`a_E=rho(B_E intersect S_x)`.  Hence

```text
0<=abar_E<=b_E/q=cbar_E lambda_E.
```

The accepted corrected subtraction gives the all-suffix upper bound

```text
A_(B,L)(kappa,D)
 <=R_(B,L)(kappa,D)
 :=q_(B,L)[C_(B+L)-q_(B,L)sum_E abar_E lambda_E]
   +sum_E thetabar_E^2/cbar_E.                      (5.1)
```

The sum is over supported exceptional endpoints; adding inactive endpoint
squares is harmless.  Formula (5.1) contains one power of `lambda_E`.
Indeed, the removed ordinary amount is

```text
q a_E lambda_E<=q b_E lambda_E,
```

so its remainder is nonnegative.  The rejected M131 two-power display is not
used.

Replacing `A` by `R` in (4.1) and recursively doing the same at every child
defines a rigorous all-suffix functional majorant
`E_(B,L)(kappa,D)`.  M140/M144 prove `C_s<3/4` for `s>=100`, so `3/4` may be
substituted for `C_s` in (5.1) in that range.  This is an exact finite
functional prescription, but it is not a scalar contraction theorem: the
state remains `(B,L,kappa,D)` and the exceptional currents remain
context-dependent.

## 6. Infinite exact scalar-nonclosure family

The obstruction already occurs at the smallest nonterminal suffix.  Take

```text
s=3, B=2, L=1, q=q_(2,1)=3/8,
p=D/(K+1)=D/kappa.
```

There are two active canonical basins.  The only live deep child has
`s=B=2` and exact reset energy zero.  Direct current/capacity calculation
therefore gives the exact complete excursion

```text
F_(2,1)(K+1,D)
 =H(3,K,K-D,2)/q
 =1/16+(2p-3/8)^2/4.                               (6.1)
```

Now fix the same `K` in two contexts.

### Right-heavy context

For `R=K-1`, `D=1` and `p=1/(K+1)`.  For every `K>=1`,

```text
F_(2,1)(K+1,1)<5/8=1-q.                            (6.2)
```

For example, at `K=32`,

```text
F=24313/278784,
H=24313/743424<15/64=q(1-q).                       (6.3)
```

### Same scalar data, large deficit

For `R=1`, `D=K-1` and `p=(K-1)/(K+1)`.  Equation (6.1) gives

```text
F>5/8
 iff 2p-3/8>3/2
 iff p>15/16
 iff K>31.                                         (6.4)
```

Thus every integer `K>=32` is a strict failure of the local contraction
budget.  At the first witness,

```text
F_(2,1)(33,31)=175033/278784,
H(3,32,1,2)=175033/743424
            >15/64,
H-q(1-q)=793/743424>0.                             (6.5)
```

The two `K=32` contexts in (6.3) and (6.5) have identical

```text
L, B, s, q, C_s=C_3=9/32, K, z=1/(K+1),
```

and identical Cayley ratios -- not merely any fixed finite selection, but
the entire ambient Cayley-ratio sequence.  They differ only in `D`.

Consequently:

> **Scalar Bellman nonclosure theorem.**  No state map omitting `D` and using
> only suffix data, `q`, `C_s`, any finite collection of Cayley ratios, and
> even `K` or `z`, can (i) determine the exact excursion value, or (ii)
> support a pointwise Bellman majorant which dominates every reachable child
> and is at most the local budget `1-q` at every such state.

This theorem does not exclude a nonlocal amortization which permits some
children to exceed `1-q`.

## 7. Reachability from right-heavy seeds

The bad states are not artificial members of the closure.  Fix `K>=32` and
start from the fresh right-heavy parent

```text
x_K=(K+2,1,0,2),  L_parent=K.
```

Choose the positive root group with degree `d=K-1`, last part `t=4`, and
prefix consisting of `K-2` ones.  This group has strictly positive stationary
mass.  Fresh attachment is uniform on `j=0,...,d`, so the `j=1` branch has
probability `1/K>0`.  Its child is exactly

```text
(t-1,1+d,0+1,B)=(3,K,1,2).                         (7.1)
```

Thus arbitrarily large-deficit violations (6.4) occur as positive-mass
children of right-heavy seeds at unbounded suffix excess.  Any all-suffix
induction must carry an arbitrary-deficit child bound rather than reusing the
right-heavy boundary theorem.

## 8. Why a fixed moment truncation is not an exact substitute

Equation (2.1) queries rising factorials of degree `d`, and root degrees are
unbounded as `L` grows.  The following algebraic proposition makes that
statement precise for schemes which aggregate a distribution of descendant
deficits by finitely many moments.

Fix `r>=0`, set `n=r+1`, and choose any `kappa>=r+4`.  On the valid deficit
set `{1,...,r+2}`, define

```text
mu_even(1+i)=binom(n,i)/2^(n-1) for even i, else 0,
mu_odd (1+i)=binom(n,i)/2^(n-1) for odd  i, else 0.
```

Both are probability measures.  Finite-difference cancellation gives

```text
E_even[P(D)]=E_odd[P(D)]
```

for every polynomial `P` of degree at most `r`, while

```text
E_even[(D)^(rise)_n]-E_odd[(D)^(rise)_n]
 =(-1)^n n!/2^(n-1) !=0.                           (8.1)
```

Therefore their averaged killed attachment masses
`E[nu_(kappa,D,n)(0)]` differ.  No fixed list of the first `r` polynomial
or factorial moments determines the exact attachment operator for all root
degrees.

This is a theorem about unrestricted moment-compression schemes.  It does
not assert that the two displayed measures themselves are the attachment
laws of two single parents.  The deterministic exact state `(kappa,D)`
avoids the obstruction entirely.

## 9. First additional statistic and remaining theorem

At `L=1`, equation (6.1) shows that the first necessary extra statistic is

```text
p=D/(K+1),
```

equivalently `D` once `K` is known.  For all suffixes, the exact sufficient
attachment state is the pair `(kappa,D)`, propagated by (2.2).  If one
aggregates many descendants rather than retaining them pointwise, the
equivalent sufficient object is their full joint measure on `(kappa,D)` (or
its complete attachment generating polynomial), not a fixed moment window.

The first unresolved positive theorem is now cleanly stated:

> Find a nonnegative potential `V_(B,L)(kappa,D)` satisfying the corrected
> reset-plus-descendant recursion (4.1)--(5.1) for every reachable state, and
> prove `V_(B,L)(kappa,1)<=1-q_(B,L)` on right-heavy seeds.  The potential is
> allowed to exceed `1-q` at non-right-heavy children such as (6.5), but their
> aggregate charge must be paid by the parent budget.

This is an all-suffix renewal problem with an essential deficit coordinate;
the scalar right-heavy induction is rigorously refuted as a closure method.

