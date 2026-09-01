# M114 independent proof audit of M109

## 1. Exact recurrence and finite state graph

Write `x=(s,K,R,B)` and retain the accepted active reachable closure

```text
{(K,R)=(1,0)} union {K>R>=1}.
```

For a positive root group `(k,t)`, the `k-1` parts before `t` sum to
`s-t`, so `s-t>=k-1`.  A live child is

```text
y=(t-1,K+k,R+j,B),  t>B, t-1>=2, 1<=j<=k.
```

Consequently

```text
P(x)-P(y)=s-t-k+j+1>=j>=1,
L(x)-L(y)=s-t+1>=1,
```

for `P=s+K-R` and `L=s-B`.  Fresh children have
`K'=k+1>j=R'>=1`; nonfresh children have
`K'-R'=(K-R)+(k-j)>=1`.  Thus every retained child remains in the closure,
both progress variables descend, and `Q` is nilpotent.  Direct substitution
in the accepted M90/M96 Schur equation gives

```text
H=A_0+QH,              G=A+QG,
Q(x,y)=rho_s(k,t) nu_(K,R,k)(j),
```

with every `j=1,...,k` present and only `j=0` or inactive targets killed.
For `(K,R)=(1,0)`, both binomial factors in `nu(j)` are one and the
denominator is `k+1`, proving fresh uniformity exactly.  Since each reset
leaf in `A` is its unweighted leaf in `A_0` multiplied by `1-q_leaf in
[0,1]`, the complete positive history expansions give `G<=H` term by term.
On a right-heavy seed, `K/(R+1)=1`, so `H<=q(1-q)` implies the weighted
target `G<=U`.

## 2. Canonical-basin bound

For an endpoint `e=(A,c_2,...,c_k)` with `k=ell+1`, the accepted basin
formula is

```text
beta_e = k!/w_A sum_(p=1)^A c(A,p)/(p+ell)!.
```

The coefficient ratio is

```text
c(A,p)/w_A
 = p [A!/(A-p)!]/A^p <= p.
```

After division by `k`,

```text
beta_e/k
 <= sum_(p>=1) p ell!/(p+ell)!
 <= sum_(p>=1) p/(p+1)! = 1.
```

The middle inequality follows from
`(p+ell)!>=ell!(p+1)!`; the last series telescopes.  Hence `beta_e<=k`
with no asymptotic or finite-enumeration input.

## 3. Suffix excess zero and one

At `L=0`, only the unary composition has contextual mean one and there is no
deep child.  Every nonunary composition of length `p` appears in `p-1`
canonical basins.  The basin estimate and the accepted binomial root-degree
mean give

```text
H=A_0<=q^2(s-1)/(s+1).
```

This is at most `q(1-q)` precisely when
`2(s/(s+1))^s<=1`, which follows from `(1+1/s)^s>=2`.

For `L=1`, `s>=3`, the only nonzero compositions are `(1,s-1)` and `(s)`,
with masses `q/2,r` and means `2z,u(1-z)`.  Their weighted mean is `q=ru`.
The singleton exceptional basin and all ordinary basins yield

```text
A_0<=q^2(hbar-q/2)+(q/4)(2z-q)^2.
```

The unary live group has mass `r(1-z)` and a terminal child of split `u`,
so the complete envelope is M109 (5.2).  After division by `q`, its excess
over the target is the convex quadratic

```text
f(z)=z^2-z(q+1-u)+q(1+hbar)-u-q^2/4.
```

At `z=0`, `r(1+hbar)=2(s/(s+1))^s<=1`; and

```text
f(1/2)-f(0)=u(1-r)/2-1/4<0
```

because `u<=2/3` and `r>1/3`.  Both endpoints are nonpositive.  At `s=2`,
the only reset target and unary deep target both have auxiliary rank one and
are inactive, so the exact recurrence gives `H=0`.

## 4. Four-support and exceptional-basin audit at `L=2`

For `B=s-2`, positivity of the contextual mean forces exactly

```text
(2,B), (1,1,B), (1,s-1), (s).
```

Direct substitution gives respectively

```text
mass: q/3, q/9, q/(3v), r
mean: 2z,  3d,  v(1-d), a(1-z),
```

and their weighted sum is `q`.  The first two exceptional compositions have
path heights one and two, and `(1,s-1)` has height one, so their total basin
mass with multiplicity is

```text
q/3+2q/9+q/(3v)=5q/9+q/(3v).
```

The singleton basin `(1,1,B)`, the basin `(2,B)` containing its two
refinements, and the singleton `(1,s-1)` have exact scores and capacities
which, after division by `q`, give

```text
(3d-q)^2/27,
(3d+6z-4q)^2/54,
[v(1-d)-q]^2/(6v).
```

All remaining basins contribute at most `q` times their basin mass by
`beta_e<=degree(e)`.  Adding inactive reset edges only enlarges this
nonnegative envelope.  This reconstructs M109 (6.1) exactly.

The only possible deep groups are `(2,s-1)` and `(1,s)`.  In the first,
`nu(0)=d`, all `j=1,2` live mass is `1-d`, and the children are terminal
with split `v`.  In the second, `nu(0)=z`, `j=1` has mass `1-z`, and the
child is right-heavy with `L=1` and split `a`.  The already proved boundary
sectors therefore give exactly M109 (6.2):

```text
(1-d)(1-v)/3 +(2/3)(1-z)(1-a).
```

Nonmaterial boundary correction: at `s=3`, the nominal `(2,s-1)=(2,2)`
child has rank `t-1=1` and is inactive, rather than live and terminal.  Here
`v=w_1/w_2=1`, so its displayed envelope charge
`(1-d)(1-v)/3` is exactly zero.  The recurrence, inequality, and theorem are
unchanged; only the prose “both children are suffix-terminal” needs the
qualification `s>=4`.

## 5. Quartic shape and endpoint reduction

Independent symbolic rational algebra gives identically

```text
9(1+z)^3 E_s'(z)=N_s(z)
```

with exactly the five coefficients displayed in M109 (6.3).  Since
`a,q<=2/3`, the coefficients of `z^4,z^3,z^2` are positive, the `z^2`
coefficient is at least eight, and `N_s(0)<=-2`.  Thus `N_s''>0` on the
positive half-line.  A strictly convex `N_s` starting below zero can cross
zero at most once there, from negative to positive.  Hence `E_s` has no
interior maximum on `[0,1/2]`.

Substitution of `q=(3/2)ruv` independently yields both exact endpoint
identities in M109 (6.4).  For `s>=10`, setting `hbar` to one and `v` to its
lower bound gives the first intermediate lower bound

```text
F(r,u)=12r^2u^3+9r^2u^2-60ru+16u+4.
```

Its `r` derivative is

```text
6u[r(4u^2+3u)-10]<0,
```

because at `r<=u<=7/16`, `4u^3+3u^2<=931/1024<10`.  Thus
`F(r,u)>=F(u,u)=p(u)`.  The second endpoint's intermediate bound has

```text
d/dr =18uv[r(12uv+9u)-20]<0,
```

since the bracketed positive part is at most
`17(7/16)^2=833/256<20`.  After setting `r=u`, its derivative in `v` at
`v=u` is exactly `j(u)` and increases with `v`; positivity of `j` therefore
reduces it to `m(u)`.

The fresh checker reproduces every listed Bernstein coefficient of `p,j,m`
on `[1/3,7/16]`; all are positive.  It also reconstructs

```text
T_s(z)=18v(1+z)^2[1-q-E_s(z)]
```

as a polynomial of degree at most four and reproduces all five exact
Bernstein coefficients, not only their minima, for each `s=3,...,9`.
Therefore the finite certificate and analytic tail cover every `s>=3`.

## 6. Independent exact computation and conclusion

`independent_exact_audit.py` has no import statements and reads no frozen
output.  It independently reconstructs rational arithmetic, compositions,
root masses, contextual means, attachment laws, grouped and literal basin
energies, live children, and both resolvents.  Its selected checks include
the `s=2` exception, five `L=2` cases on both sides of the `s=10` split, and
all four M109 calibration contexts.  Only after this run completed, a
read-only cross-artifact comparison established exact numerator/denominator
equality with all four frozen ratios, all asymptotic coefficients, and all
35 finite coefficients.

No material flaw was found.  The proof establishes the stronger unweighted
full-excursion contraction only for right-heavy `L<=2`, and therefore the
weighted contraction there.  It does not establish the global all-`L`
frontier; `L=3` is the first unresolved boundary.  It supplies no auxiliary
gap, no ROOT-MEAN LIFT, no original heat-bath gap, and neither project
terminal.
