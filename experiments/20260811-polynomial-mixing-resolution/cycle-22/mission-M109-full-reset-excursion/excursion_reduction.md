# M109 excursion reduction and suffix-boundary theorems

## 1. Exact state and recurrence

This note concerns only the full nonlazy stationary-flow parking-degree
projection in the minimal long-cycle sector. It does not concern the original
lazy `{3,4,5}` identity-word heat-bath chain.

An active context is `x=(s,K,R,B)`, where `s>=2`, `1<=B<=s`, in the accepted
reachable closure `{(K,R)=(1,0)} union {K>R>=1}`. Write

```text
w_a=a^(a-1)/a!,
q_x=w_(s+1-B)w_B/w_(s+1),
U(x)=q_x(1-q_x)K/(R+1).
```

For a root composition of length `k` and last part `t`, put

```text
c(n,p)=p n^(n-p-1)/(n-p)!,  c(0,0)=1,
rho_s(k,t)=w_t c(s-t,k-1)/(k!w_(s+1)),
nu_(K,R,k)(j)=binom(R+j,j)
               binom(K-R-1+k-j,k-j)/binom(K+k,k).
```

The live deep children are exactly

```text
y=(t-1,K+k,R+j,B),  t>B, t-1>=2, j=1,...,k.
```

The `j=0` branch and every suffix-terminal/inactive branch are killed. Thus
`Q(x,y)=rho_s(k,t)nu_(K,R,k)(j)` after summing coincident children. Every
listed `j` is retained. Both

```text
P=s+K-R,   P(x)-P(y)=s-t-k+j+1>=j>=1,
L=s-B,     L(x)-L(y)=s-t+1>=1
```

strictly descend. Hence `Q` is nilpotent on the finite reachable DAG.

Let `A_0(x)` be the canonical reset energy and `A(x)` the same energy
multiplied at each reset target by `1-q_target`. The complete unweighted and
weighted reset excursions are the unique finite recurrences

```text
H=A_0+QH,  H=(I-Q)^(-1)A_0,
G=A+QG,    G=(I-Q)^(-1)A.
```

Equivalently, before the `q`-transform these are the Schur complements
`K_reset=(I-D)^(-1)J_can`. In particular

```text
H(x)=q_x K_reset 1(x),
G(x)=q_x K_reset W(x),
W(s,K,R,B)=(1-q_x)K/(R+1).
```

Every reset target is right-heavy, so its `W` is `1-q_target`. For a
right-heavy seed the two global targets are

```text
H(x)<=q_x(1-q_x)  (unweighted),
G(x)<=U(x)=q_x(1-q_x)  (weighted).
```

The first implies the second because `0<=1-q_target<=1` term by term. This
is a whole-excursion statement; no sign is imposed on one or two local
defect layers.

For a fresh context, the attachment law simplifies exactly to
`nu_(1,0,k)(j)=1/(k+1)` for `j=0,...,k`. Therefore

```text
H(s,1,0,B)=A_0(s,1,0,B)
 +sum_(k,t>B) rho_s(k,t)/(k+1)
      sum_(j=1)^k H(t-1,k+1,j,B),
```

with the identical recurrence for `G` after replacing `A_0` by `A`. At the
suffix-terminal boundary `B=s`, no `t>B` exists and `Q=0`.

## 2. Selected global lemma

> **Full-excursion right-heavy contraction.** For every active reachable
> right-heavy `x=(s,K,K-1,B)`, the complete finite-DAG recursion above obeys
> `H(x)<=q_x(1-q_x)` (and hence `G(x)<=U(x)`).

This target aggregates all depths before comparison. M98/M99's one-step
counterexamples and M103/M106's two-layer counterexample therefore neither
prove nor refute it.

## 3. A universal canonical-basin sharpening

Let an edge of the canonical first-merge tree have refined endpoint
`e=(A,c_2,...,c_k)`, where `k=ell+1>=2`, and source basin `B_e`, consisting
of all refinements of its first part. The accepted root-composition law gives

```text
beta_e := rho_s(B_e)/rho_s(e)
 =k!/w_A sum_(p=1)^A c(A,p)/(p+ell)!.
```

There is a sharper estimate than the previously used constant-`e` bound:

```text
beta_e<=k.                                           (3.1)
```

Indeed `c(A,p)/w_A=p[A!/(A-p)!]/A^p<=p`. After dividing
(3.1) by `k=ell+1`, it is enough to note

```text
sum_(p>=1) p ell!/(p+ell)!
 <=sum_(p>=1) p/(p+1)!=1,
```

where `(p+ell)!>=ell!(p+1)!` follows from
`(p+2)...(p+ell)>=2...ell`. This proves (3.1) for every `A,ell`.

## 4. Proved suffix-terminal sector

Here “suffix-terminal” means only `L=s-B=0` in this reset DAG. It is
unrelated to project Terminal A or Terminal B.

> **Theorem (suffix-terminal full-excursion contraction).** For every `s>=2` and
> every reachable `(K,R)`, at `B=s` one has
> ```text
> H(s,K,R,s)<=q(1-q),
> G(s,K,R,s)<=q(1-q)<=U(s,K,R,s),
> q=(s/(s+1))^(s-1).
> ```

**Proof.** At `B=s`, the closed contextual root mean is one on the unary
composition `(s)` and zero on every nonunary composition. Its stationary
mean is `q=rho_s((s))=w_s/w_(s+1)=(s/(s+1))^(s-1)`.

Every canonical edge basin contains only nonunary compositions. Hence its
flow score is exactly `theta_e=-q rho_s(B_e)`, while its scaled capacity is
`k rho_s(e)`. Using (3.1),

```text
theta_e^2/[k rho_s(e)]
 =q^2 rho_s(B_e) beta_e/k
 <=q^2 rho_s(B_e).
```

Adding any canonical edge whose reset target is inactive can only increase
this nonnegative upper bound. Each composition of length `p` lies in exactly
the `p-1` successive basins
on its canonical path to `(s)`. The accepted root-degree law is
`p-1~Bin(s-1,1/(s+1))`. Summing over all canonical edges yields

```text
A_0(s,K,R,s)<=q^2 E[p-1]=q^2(s-1)/(s+1).            (4.1)
```

Finally `q^2(s-1)/(s+1)<=q(1-q)` is equivalent to
`2(s/(s+1))^s<=1`, which follows from `(1+1/s)^s>=2` by the binomial
theorem. There are no deep children when `B=s`, so `H=A_0`. Also `A<=A_0`,
and reachability gives `K/(R+1)>=1`, proving all displayed inequalities.
QED.

This theorem supplies the exact `L=0` boundary of the global finite-DAG
problem.

## 5. Proved one-layer sector

> **Theorem (one-layer full-excursion contraction).** For every active
> right-heavy `x=(s,K,K-1,s-1)`, one has
> ```text
> H(x)<=q_x(1-q_x),  G(x)<=U(x).
> ```

**Proof.** First take `s>=3`. Put

```text
r=w_s/w_(s+1)=(s/(s+1))^(s-1),
u=w_(s-1)/w_s=((s-1)/s)^(s-2),
q=q_x=ru,  hbar=(s-1)/(s+1),  z=1/(K+1).
```

Only two root compositions have a nonzero contextual mean: `(1,s-1)` has
value `2z`, and the unary composition `(s)` has value `u(1-z)`. Their
stationary masses are respectively `q/2` and `r`; their contributions sum
to the required mean `q`.

The exceptional composition `(1,s-1)` belongs only to its singleton
canonical basin `e_0`. Every other canonical basin contains only
zero-contextual-mean sources. Applying (3.1) to those other basins and using
the exact score on `e_0` gives

```text
A_0(x)<=q^2(hbar-q/2)+(q/4)(2z-q)^2.                (5.1)
```

The sole possible live deep group is the unary root group `k=1,t=s`. Its
`Q`-mass is `r(1-z)`, and its child
`(s-1,K+1,K,s-1)` is right-heavy and suffix-terminal. Section 4 therefore gives

```text
H(x)<=q^2(hbar-q/2)+(q/4)(2z-q)^2
       +q(1-z)(1-u).                                (5.2)
```

After division by `q`, inequality (5.2) is at most `1-q` exactly when

```text
f(z):=z^2-z(q+1-u)+q(1+hbar)-u-q^2/4 <=0.           (5.3)
```

This is convex in `z`, while `0<z<=1/2`, so it suffices to check the two
endpoints. At zero,

```text
f(0)=u[r(1+hbar)-1]-q^2/4<=0,
```

because `r(1+hbar)=2(s/(s+1))^s<=1`. Moreover

```text
f(1/2)-f(0)=u(1-r)/2-1/4<0.                         (5.4)
```

For completeness, `u<=2/3` follows from
`(1+1/(s-1))^(s-2)>=1+(s-2)/(s-1)`, while `r>1/3` follows from
`(1+1/s)^(s-1)<sum_(j>=0)1/j!<3`. Thus
`u(1-r)<4/9<1/2`, proving (5.4) and then (5.3).

When `s=2`, both the would-be unary deep child and the reset target from the
sole edge `(1,1)` are inactive, so `H=0`. Even if that discarded reset edge
is added, its energy is bounded by

```text
(1/6)(2/(K+1)-2/3)^2<=2/27<2/9=q(1-q).
```

This proves the unweighted assertion. The weighted assertion follows term
by term as in Section 2. QED.

## 6. Proved suffix-excess-two sector

> **Theorem (suffix-excess-two full-excursion contraction).** For every active
> right-heavy `x=(s,K,K-1,s-2)`, `s>=3`, one has
> ```text
> H(x)<=q_x(1-q_x),  G(x)<=U(x).
> ```

This is a theorem about the complete excursion starting in the bounded
sector `L=2`; it is not the globally refuted condition `(I+Q)r_U>=0`.

**Proof.** Put `B=s-2` and

```text
r=w_s/w_(s+1),  u=w_(s-1)/w_s,  v=w_B/w_(s-1),
a=uv,           q=(3/2)ruv,      hbar=(s-1)/(s+1),
z=1/(K+1),      d=2z^2/(1+z).
```

The contextual mean is nonzero on exactly four root compositions:

```text
composition   stationary mass   contextual mean
(2,B)         q/3               2z
(1,1,B)       q/9               3d
(1,s-1)       q/(3v)            v(1-d)
(s)           r                 a(1-z).
```

Their weighted sum is `q`. The first three compositions generate exactly
three exceptional canonical basins: `(1,1,B)`, `(2,B)`, and `(1,s-1)`.
All other basin scores are `-q` times their basin mass. The total stationary
path height is `hbar`; the exceptional compositions account for basin mass
`5q/9+q/(3v)`. The basin estimate (3.1), with inactive reset edges harmlessly
added, therefore gives

```text
A_0(x)/q <= q[hbar-5q/9-q/(3v)]
 +(3d-q)^2/27
 +(3d+6z-4q)^2/54
 +[v(1-d)-q]^2/(6v).                               (6.1)
```

There are only the accepted live groups `(k,t)=(2,s-1)` and `(1,s)`.
For the first, the killed attachment mass is `d`, its live mass is `1-d`,
and both children are suffix-terminal with split mass `v`. For the second,
the live mass is `1-z` and its child has `L=1` with split mass `a`. Sections
4--5 hence add, after division by `q`, at most

```text
(1-d)(1-v)/3 +(2/3)(1-z)(1-a).                     (6.2)
```

Let `E_s(z)` be the sum of the right sides of (6.1)--(6.2). Thus the full
excursion, with every `j=1,2` in the two-part group retained, satisfies
`H(x)/q<=E_s(z)`. It remains to prove `E_s(z)<=1-q` for
`0<z<=1/2`.

Direct differentiation and clearing the positive denominator gives

```text
9(1+z)^3 E_s'(z)=N_s(z),
N_s(z)=(12v+72)z^4
 +(6a-14q+24v+156)z^3
 +(18a-42q+36)z^2
 +(18a-36q-18)z
 +(6a-8q-6).                                       (6.3)
```

The accepted active split bound gives `a,q<=2/3`. Hence the coefficients of
`z^4,z^3,z^2` in `N_s` are positive, the quadratic coefficient is at least
`8`, and `N_s(0)<=-2`. Consequently `N_s''(z)>0` on `z>=0`.
The derivative `N_s'` is strictly increasing, so `N_s`, starting negative,
has at most one positive zero, crossed from negative to positive. Therefore
`E_s` has no interior maximum, and only `z=0,1/2` need be checked.

Using `q=(3/2)ruv`, the two endpoint slacks are

```text
1-q-E_s(0)=v P_s/24,
P_s=-36hbar ru+12r^2u^2v+9r^2u^2-24ru+16u+4,

1-q-E_s(1/2)=M_s/216,
M_s=-324hbar ruv+108r^2u^2v^2+81r^2u^2v
    -36ruv+72uv+32v+24.                            (6.4)
```

For `s>=10`, the decreasing Cayley ratios obey

```text
1/3<r<=u<=v<=2/3,   u<=b_10=(9/10)^8<7/16.
```

Here the lower bound follows from
`(1+1/(n-1))^(n-2)<sum_j 1/j!<3`; monotonicity and the upper split bound are
accepted inputs. Since `hbar<1` and `v>=u`, the first numerator in (6.4) is
bounded below by

```text
p(u)=12u^5+9u^4-60u^2+16u+4.                       (6.5)
```

Indeed the intermediate lower bound is decreasing in `r<=u`. Similarly the
second numerator is decreasing in `r<=u`. After setting `r=u`, it is
increasing in `v>=u`, because its `v`-derivative at `v=u` is

```text
j(u)=216u^5+81u^4-360u^2+72u+32>0,
```

and that derivative only increases with `v`. It is therefore bounded below
by

```text
m(u)=108u^6+81u^5-360u^3+72u^2+32u+24.             (6.6)
```

All three polynomials are strictly positive on `[1/3,7/16]`. An exact
Bernstein certificate on that interval lists their coefficients as

```text
p: 229/81, 64/27, 4285/2304, 2659/2048,
   135563/196608, 9881/262144;
j: 161/9, 179/12, 2995/256, 16949/2048,
   307781/65536, 134143/131072;
m: 805/27, 8425/288, 32855/1152, 678385/24576,
   15627965/589824, 475484045/18874368,
   99364775/4194304.
```

Every coefficient is positive, proving both endpoint signs for `s>=10`.
For the seven remaining integers `3<=s<=9`, substitute their exact Cayley
ratios into

```text
T_s(z)=18v(1+z)^2[1-q-E_s(z)].
```

The five degree-four Bernstein coefficients on `[0,1/2]` are all positive.
Their exact minima for `s=3,...,9` are respectively

```text
359/256,
19957/46875,
3703/12000,
32277779252224/119169245671875,
2556191652291015625/10103662211651076096,
62954407990539769/259405508972981952,
3945228443496793740269971289/
 16717688340480000000000000000.
```

`boundary_exact.py` derives every coefficient with `Fraction` arithmetic and
checks the polynomial identity against (6.1)--(6.2). This finite exact
certificate plus (6.3)--(6.6) proves `E_s(z)<=1-q` for every `s>=3`.
Thus `H<=q(1-q)`, and weighted contraction follows term by term. QED.

## 7. First unresolved excursion-level step

For general `L`, expansion over complete deep histories gives

```text
H(x)=sum_(d=0)^L sum_(x=x_0 -> ... -> x_d)
       [product_(i<d)Q(x_i,x_(i+1))] A_0(x_d).       (7.1)
```

The smallest still-unproved global assertion is that, for a right-heavy
initial state, the total measure on the marked reset leaves in (7.1), with
each leaf charged by its exact canonical squared-flow energy, is at most the
initial Bernoulli budget `q_x(1-q_x)`. Any proof must control this aggregate
measure across all `L` layers. Pointwise Bellman positivity, nonfresh defect
positivity, and two-layer positivity cannot be assumed: each is already
refuted in the accepted predecessor chain. Sections 4--6 settle this measure
for suffix excess `L<=2`; the first unresolved boundary is `L=3`.
