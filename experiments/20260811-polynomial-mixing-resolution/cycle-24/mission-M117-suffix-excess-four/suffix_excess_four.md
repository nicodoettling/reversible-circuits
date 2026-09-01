# M117 suffix-excess-four full-excursion theorem

## 1. Scope, convention, and theorem

This note concerns only the auxiliary full **nonlazy stationary-flow
parking-degree projection** in the minimal-long-cycle sector. It is not a
mixing theorem for the original lazy `{3,4,5}` heat-bath chain. Permutations
compose as `(pq)(x)=p(q(x))`, with factors displayed left-to-right.

Use the accepted recurrence

```text
H=A_0+QH=(I-Q)^(-1)A_0,
G=A+QG=(I-Q)^(-1)A.
```

Every attachment rank `j=1,...,k` is retained in `Q`; only `j=0` and
inactive rank-one children are killed. M109/M114 prove `G<=H` term by term,
the all-deficit terminal theorem, and right-heavy contraction for `L<=2`.
M115/M116 prove right-heavy contraction for `L=3` and the arbitrary-deficit
`L=1` envelope used below.

> **Theorem (suffix-excess-four full-excursion contraction).** For every
> `s>=5`, `K>=1`, and right-heavy context
> ```text
> x=(s,K,K-1,B),  B=s-4,
> ```
> the complete finite-DAG excursion obeys
> ```text
> H(x)<=q_x(1-q_x),  G(x)<=U(x)=q_x(1-q_x).
> ```

This extends the accepted boundary theorem exactly one layer, from `L<=3`
to `L<=4`. It proves no all-`L` statement, auxiliary gap, ROOT-MEAN LIFT,
original-chain gap, or project terminal.

## 2. Parameters, attachment law, and the 16 supported compositions

Write `b_n=w_n/w_(n+1)=(n/(n+1))^(n-1)` and put

```text
r=b_s, u=b_(s-1), v=b_(s-2), y=b_(s-3), x=b_(s-4),
z=1/(K+1),
d=2z^2/(1+z),
e=6z^3/[(1+z)(1+2z)],
f=24z^4/[(1+z)(1+2z)(1+3z)],
q=(125/24)ruvyx,
c_1=xy, c_2=(3/2)vyx, c_3=(8/3)uvyx,
h_0=(s-1)/(s+1), h_1=(s-4)/(s-2), h_2=(s-3)/(s-1).
```

Thus `q=q_(s,B)` because `w_5=125/24`. For a right-heavy parent define

```text
delta_k=k! z^k / prod_(a=1)^(k-1)(1+az).
```

In particular `delta_1=z`, `delta_2=d`, `delta_3=e`, and `delta_4=f`.
The exact attachment law is

```text
nu_k(0)=delta_k,
nu_k(j)=(k!/j!) z^(k-j)(1-z)
        prod_(a=1)^(j-2)(1+az) / prod_(a=1)^(k-1)(1+az),
        1<=j<=k,                                      (2.1)
```

with empty products equal to one. It sums to one.

For `B=s-4`, positivity of the contextual mean gives exactly the following
16 ordered root compositions. The middle column is `rho/q`; the last column
is the contextual mean.

```text
composition(s)                              rho/q              mean
(4,B)                                       32/125             2z
(1,3,B), (3,1,B)                            6/125 each         3d
(2,2,B)                                     4/125              3d
(1,1,2,B), (1,2,1,B), (2,1,1,B)             1/125 each         4e
(1,1,1,1,B)                                 1/625              5f

(3,s-3)                                     18/(125x)          x(1-d)
(1,2,s-3), (2,1,s-3)                        4/(125x) each      x(1-e)
(1,1,1,s-3)                                 1/(125x)           x(1-f)

(2,s-2)                                     12/(125xy)         xy(1-d)
(1,1,s-2)                                   4/(125xy)          xy(1-e)

(1,s-1)                                     12/(125xyv)        (3/2)xyv(1-d)
(s)                                         24/(125uvyx)       (8/3)uvyx(1-z).
```

Their `rho*f` sum is `q`, equivalently the mass-ratio times mean column sums
to one. The positive `(k,t)` support comprises 11 groups:

```text
t=B:     k=2,3,4,5;
t=s-3:   k=2,3,4;
t=s-2:   k=2,3;
t=s-1:   k=2;
t=s:     k=1.
```

Only the last seven groups (`t>B`) send deep mass.

## 3. The 15 exceptional canonical basins

For an endpoint `E=(A,c_2,...,c_k)`, its canonical basin contains every
source obtained by refining `A`. Put

```text
T_E=theta_E/q,
C_E=cap_E/q=k rho(E)/q.
```

The contribution of that edge to `A_0/q` is `T_E^2/C_E`. There are exactly
15 exceptional basins. To keep the table readable, a prefix `P` means the
endpoint `(P,t)` for the displayed last part `t`, and the source column lists
the supported prefixes in its basin.

### 3.1 Last part `B`

```text
P       source prefixes                    T_E                                      C_E
1111    1111                               (5f-q)/625                               1/125
211     211,1111                           (20e+5f-6q)/625                          4/125
121     121                                (4e-q)/125                               4/125
31      31,121,211,1111                    (90d+40e+5f-41q)/625                    18/125
112     112                                (4e-q)/125                               4/125
22      22,112                             (12d+4e-5q)/125                         12/125
13      13                                 6(3d-q)/125                             18/125
4       all eight prefixes                 (320z+240d+60e+5f-256q)/625             64/125
```

### 3.2 Last part `s-3`

```text
P      source prefixes          T_E                                               C_E
111    111                      [x(1-f)-q]/(125x)                                 4/(125x)
21     21,111                   [5x-4xe-xf-5q]/(125x)                            12/(125x)
12     12                       4[x(1-e)-q]/(125x)                               12/(125x)
3      3,12,21,111              [27x-18xd-8xe-xf-27q]/(125x)                    36/(125x)
```

### 3.3 Last parts `s-2` and `s-1`

```text
last   P     source prefixes      T_E                                               C_E
s-2    11    11                   4[xy(1-e)-q]/(125xy)                            12/(125xy)
s-2    2     2,11                 [16xy-12xyd-4xye-16q]/(125xy)                  24/(125xy)
s-1    1     1                    12[(3/2)xyv(1-d)-q]/(125xyv)                   24/(125xyv)
```

The four endpoints beginning with `(1,1)` are inactive reset targets. Adding
their nonnegative square terms, as well as inactive ordinary edges, only
enlarges the upper bound.

Every supported source occurs in exactly one exceptional basin for each edge
of its canonical path. Consequently the supported exceptional path mass,
divided by `q`, is exactly

```text
S_4=369/625 + 37/(125x) + 4/(25xy) + 12/(125xyv).   (3.1)
```

The total stationary canonical path height is `h_0`. Every ordinary basin has
current `-q` times its basin mass, and the accepted
`rho(basin)/rho(endpoint)<=degree(endpoint)` estimate bounds its energy by
`q^2 rho(basin)`. Therefore the complete reset envelope is

```text
A_0(x)/q <= R_4:=q(h_0-qS_4)+sum_(15 exceptional E) T_E^2/C_E.   (3.2)
```

Equations (3.1)--(3.2) and the table specify every term; no exceptional basin
is hidden in an ellipsis.

## 4. Standalone arbitrary-deficit `L=2` envelope

The live parent group `(k,t)=(2,s-1)` has a deficit-two child, so the accepted
right-heavy `L=2` theorem cannot be applied to both ranks. The required new
bound is the following.

> **Proposition (general-attachment two-layer envelope).** Let
> ```text
> X=(S,K_0,R_0,S-2), S>=3, K_0>R_0>=1,
> D=K_0-R_0,
> p=D/(K_0+1),
> d_0=D(D+1)/[(K_0+1)(K_0+2)],
> p'=D/(K_0+2),
> R=w_S/w_(S+1), U=w_(S-1)/w_S, Y=w_(S-2)/w_(S-1),
> a=UY, q_0=(3/2)RUY,
> H_0=(S-1)/(S+1), H_1=(S-2)/S.
> ```
> Define the accepted `L=1` envelope
> ```text
> F_1(b,y,h;p)=b(h-b/2)+(2p-b)^2/4+(1-p)(1-y).      (4.1)
> ```
> Then
> ```text
> H(X)/q_0 <= F_2,
> F_2=R_2+D_2,                                      (4.2)
> R_2=q_0[H_0-5q_0/9-q_0/(3Y)]
>     +(3d_0-q_0)^2/27
>     +(3d_0+6p-4q_0)^2/54
>     +[Y(1-d_0)-q_0]^2/(6Y),                      (4.3)
> D_2=(1-d_0)(1-Y)/3
>     +(2/3)(1-p)F_1(a,Y,H_1;p').                  (4.4)
> ```

**Proof.** The contextual mean is supported on exactly four compositions:

```text
composition    mass          mean
(2,S-2)        q_0/3         2p
(1,1,S-2)      q_0/9         3d_0
(1,S-1)        q_0/(3Y)      Y(1-d_0)
(S)            R             a(1-p).
```

Their weighted mean is `q_0`. Exactly three basins are exceptional:
`(1,1,S-2)`, `(2,S-2)`, and `(1,S-1)`. Their supported occurrence mass is
`5q_0/9+q_0/(3Y)`. The exact currents and capacities give, after division by
`q_0`, respectively

```text
(3d_0-q_0)^2/27,
(3d_0+6p-4q_0)^2/54,
[Y(1-d_0)-q_0]^2/(6Y).
```

The ordinary-basin estimate supplies the first term of (4.3), proving the
reset bound.

There are only two live groups. For `(2,S-1)`, the killed mass is `d_0` and
the total retained mass is `1-d_0`; every retained child is suffix-terminal
with split `Y`. Its normalized charge is `(1-d_0)(1-Y)/3`. For the unary
group, the killed mass is `p`, the live mass is `1-p`, and the child is an
arbitrary-deficit `L=1` context with split `a`, unchanged deficit `D`, and
attachment parameter `p'`. Since `Ra/q_0=2/3`, the accepted (4.1) gives the
second term of (4.4). This proves (4.2).

At `S=3`, the nominal first group's children have rank one and are inactive;
here `Y=w_1/w_2=1`, so its displayed charge is zero. Thus the formula covers
the boundary without a limiting argument. QED.

The proposition is an envelope for `H/q_0`; it does not claim right-heavy
contraction for arbitrary `D`.

## 5. Every live group and the full descendant envelope

For use below, let `F_2^(2)` denote (4.2) for the deficit-two child with

```text
(R,U,Y)=(v,y,x),
p=2z/(1+2z),
d_0=6z^2/[(1+2z)(1+3z)],
p'=2z/(1+3z),
(H_0,H_1)=(h_2,h_1).
```

For the `t=s-2` groups put

```text
p_(k,j)=(k+1-j)z/(1+kz).
```

Using the exact attachment masses (2.1), all seven live groups contribute,
after division by the parent `q`, at most

```text
D_4=
 (1-x)/125 [18(1-d)+8(1-e)+(1-f)]

 +(12/125) sum_(j=1)^2 nu_2(j) F_1(xy,x,h_1;p_(2,j))
 +( 4/125) sum_(j=1)^3 nu_3(j) F_1(xy,x,h_1;p_(3,j))

 +(18/125)[nu_2(1)F_2^(2)+nu_2(2)(1-c_2)]
 +(64/125)(1-z)(1-c_3).                            (5.1)
```

Every coefficient follows by cancelling the child split against the parent
group mass:

```text
group(s)             parent mass/q        child sector and cancellation
(2,3,4;s-3)          18,8,1 /(125x)       x(1-x), sum live=1-d/e/f
(2;s-2)              12/(125xy)           xy F_1
(3;s-2)               4/(125xy)           xy F_1
(2;s-1)              12/(125xyv)          c_2=(3/2)xyv, product 18/125
(1;s)                24/(125uvyx)          c_3=(8/3)uvyx, product 64/125.
```

In `(2,s-1)`, `j=1` has deficit two and uses the new proposition; `j=2` is
right-heavy and uses the accepted `L=2` contraction `H/c_2<=1-c_2`. The
unary child is right-heavy `L=3` and uses M115/M116. No attachment rank is
discarded.

At `s=5`, the nominal `t=s-3` children have rank one and are inactive; here
`x=1`, so the entire first line of (5.1) is zero. All other boundary child
lemmas already include their rank-one qualifications.

Combining (3.2) and (5.1) gives

```text
H(x)/q <= E_4:=R_4+D_4.                            (5.2)
```

This is a whole-excursion inequality. It uses no refuted one-step or
two-layer defect sign.

## 6. Exact universal sign certificate

It remains to prove `E_4<=1-q` for every `s>=5` and `0<z<=1/2`. Set

```text
Delta(z)=prod_(a=1)^4(1+az),
T=Delta(z)^2[1-q-E_4].                             (6.1)
```

Every denominator in (2.1), (4.1)--(4.4), and (5.1) divides `Delta^2`.
After the apparent inverse Cayley-ratio factors cancel against `q` or the
corresponding child split, `T` is polynomial. Inspection of the squared
currents and descendant terms gives multidegree at most

```text
(2,2,2,2,2,10) in (r,u,v,y,x,z).                  (6.2)
```

The degree ten is sharp; it comes from clearing the squared `delta_4` term.

### 6.1 Finite ranks `5<=s<=21`

For each of these 17 exact Cayley-ratio tuples, `l4_exact.py` interpolates
(6.1), verifies exact degree ten by an eleventh finite difference, and
converts it to the degree-ten Bernstein basis on `z in [0,1/2]`. Every one
of the `17*11=187` coefficients is strictly positive. The smallest is

```text
71734022477173585947 / 9023189417984000000000
```

at `s=7`, coefficient index zero. The script also checks the interpolant
against a direct evaluation at the independent coordinate `2/7` for every
`s`.

### 6.2 All ranks `s>=22`

The consecutive ratios are

```text
(r,u,v,y,x)=(b_s,b_(s-1),b_(s-2),b_(s-3),b_(s-4)).
```

The accepted monotonicity and lower bound give `b_n>1/3`. Since
`s-4>=18` and the exact inequality

```text
b_18=(18/19)^17<2/5
```

holds, all five ratios lie in `[1/3,2/5]`. Moreover
`0<h_0,h_1,h_2<1`. Each height occurs in `E_4` with a nonnegative
coefficient: `h_0` in the ordinary reset charge, `h_1` in the `L=1`
envelopes, and `h_2` in the new `L=2` reset envelope. Replacing all three by
one therefore enlarges `E_4` and is pessimistic for the slack.

On

```text
[1/3,2/5]^5 x [0,1/2],
```

the complete tensor Bernstein expansion at the multidegree (6.2) has

```text
3^5*11=2673
```

coefficients. `l4_exact.py` derives all of them with exact `Fraction`
arithmetic. Every coefficient is positive; the exact minimum is

```text
742081/227812500
```

at tensor index `(2,2,2,2,0,0)`. A separate off-grid tensor evaluation
matches the direct rational formula exactly. Thus `T>0` on the full box,
and hence on every actual tuple for `s>=22`.

The finite and tensor certificates prove `E_4<1-q` for every `s>=5` and
`0<=z<=1/2`. Equation (5.2) gives `H<=q(1-q)`. Positive histories give
`G<=H`, and the seed is right-heavy, so `U=q(1-q)`. The theorem follows.
QED.

## 7. Independent exact audits and limitations

`l4_exact.py` imports no predecessor source or output. It reconstructs the
root law, contextual means, attachment law, grouped exact reset recurrence,
literal all-composition basin recurrence, every individual child rank, both
resolvents, the new child envelope, and both certificate families.

The literal path enumerates every active canonical basin for selected
`5<=s<=9`, verifies exact equality with the grouped reset recurrence, and
matches each of the 11 active exceptional currents and capacities. The four
inactive exceptional square terms are present only in the upper envelope.

The arbitrary-deficit audit covers all 252 contexts

```text
3<=S<=9, 2<=K_0<=9, 1<=R_0<K_0.
```

For each it directly checks the four supported masses and means, the mean
identity, `exact reset <= q_0 R_2`, and
`exact resolvent <= q_0(R_2+D_2)`. The largest observed reset-to-envelope
ratio is about `.9994582`; the largest full ratio is about `.9973788`.
These tight rows audit the formula but are not used as a universal proof.

The retained full L=4 scan covers all `5<=s<=20` and
`K in {1,2,5,64,4096}`. It has zero reset, resolvent, envelope, or target
failures. The universal assertion comes from Section 6, not from this scan.

The strongest limitation is unchanged from M115: the number of exceptional
basins doubles with suffix excess, and the present certificate is local to
`L=4`. It supplies no automatic organization for general `L`; the first
unresolved excursion boundary is now `L=5`.
