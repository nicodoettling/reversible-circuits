# M121 independent proof audit of frozen M117

## 1. Claim, target, convention, and provenance

The project target remains the uniform law on fixed-length identity words in
`Omega(N,m)`, with `(pq)(x)=p(q(x))` and factors displayed left-to-right. The
claim audited here is only

```text
H(s,K,K-1,s-4) <= q(1-q),  s>=5, K>=1,
```

for the auxiliary full nonlazy stationary-flow parking-degree projection in
the minimal-long-cycle sector. Positive histories then give `G<=H`; a
right-heavy seed has `U=q(1-q)`. This is not an auxiliary gap, ROOT-MEAN LIFT,
an original lazy `{3,4,5}` heat-bath gap, polynomial mixing, or a project
terminal.

Before audit, all supplied immutable hashes matched: report
`65213fb2...b8044`, proof `e9a1d5ca...c5398`, source
`13f37f60...63d`, JSON `e4acb81c...af94`, and manifest
`93b420a9...01a`. No M117 file was edited.

## 2. Independent recurrence and two reset paths

Starting from M109/M114's accepted recurrence, the fresh checker uses

```text
Q(x,y)=rho_s(k,t) nu_(K,R,k)(j),
y=(t-1,K+k,R+j,B), j=1,...,k.
```

Only `j=0` and targets of auxiliary rank below two are killed. For every live
child, both `L=s-B` and `P=s+K-R` descend, so the recursion is a finite DAG.

The reset energy was reconstructed twice. The literal path enumerates every
ordered composition and every active canonical basin. The aggregate path uses
the independently checked forest identity

```text
sum_(alpha models A, ell(alpha)=p) prod_i w_(alpha_i)
 = p A^(A-p-1)/(A-p)!.
```

For endpoint `(A,c_2,...,c_k)`, it sums over `p` before forming the current.
The two paths agree at all 213 recursive states reached from the 15 smallest
audited `L=4` roots.

## 3. Sixteen supported rows

Put

```text
r=b_s, u=b_(s-1), v=b_(s-2), y=b_(s-3), x=b_(s-4),
z=1/(K+1), d=2z^2/(1+z),
e=6z^3/[(1+z)(1+2z)],
f=24z^4/[(1+z)(1+2z)(1+3z)],
q=(125/24)ruvyx.
```

Direct enumeration and substitution give exactly these 16 rows:

```text
composition(s)                         rho/q             contextual mean
(4,B)                                  32/125            2z
(1,3,B),(3,1,B)                        6/125 each        3d
(2,2,B)                                4/125             3d
(1,1,2,B),(1,2,1,B),(2,1,1,B)         1/125 each        4e
(1,1,1,1,B)                            1/625             5f

(3,s-3)                                18/(125x)         x(1-d)
(1,2,s-3),(2,1,s-3)                    4/(125x) each     x(1-e)
(1,1,1,s-3)                            1/(125x)          x(1-f)

(2,s-2)                                12/(125xy)        xy(1-d)
(1,1,s-2)                              4/(125xy)         xy(1-e)
(1,s-1)                                12/(125xyv)       (3/2)xyv(1-d)
(s)                                    24/(125uvyx)      (8/3)uvyx(1-z).
```

Their mass-times-mean sum is exactly `q`. Their positive support comprises 11
groups: `k=2,3,4,5` at `t=B`; `k=2,3,4` at `t=s-3`; `k=2,3` at `t=s-2`;
`k=2` at `t=s-1`; and `k=1` at `t=s`.

## 4. All 15 exceptional currents and capacities

For a canonical endpoint `E`, write `T_E=theta_E/q` and
`C_E=cap_E/q`. Literal basin membership gives the following complete table.
The prefix shown is followed by the indicated last part.

```text
last  prefix  T_E                                      C_E
B     1111    (5f-q)/625                               1/125
B     211     (20e+5f-6q)/625                          4/125
B     121     (4e-q)/125                               4/125
B     31      (90d+40e+5f-41q)/625                    18/125
B     112     (4e-q)/125                               4/125
B     22      (12d+4e-5q)/125                         12/125
B     13      6(3d-q)/125                             18/125
B     4       (320z+240d+60e+5f-256q)/625             64/125
s-3   111     [x(1-f)-q]/(125x)                       4/(125x)
s-3   21      [5x-4xe-xf-5q]/(125x)                  12/(125x)
s-3   12      4[x(1-e)-q]/(125x)                     12/(125x)
s-3   3       [27x-18xd-8xe-xf-27q]/(125x)           36/(125x)
s-2   11      4[xy(1-e)-q]/(125xy)                   12/(125xy)
s-2   2       [16xy-12xyd-4xye-16q]/(125xy)          24/(125xy)
s-1   1       12[(3/2)xyv(1-d)-q]/(125xyv)           24/(125xyv).
```

Every entry was obtained both by literal source nesting and by its displayed
closed formula. The four endpoints whose full composition begins `(1,1)` are
inactive; adding their squares is harmless in an upper bound. The supported
basin mass with path multiplicity is exactly

```text
q[369/625+37/(125x)+4/(25xy)+12/(125xyv)].
```

After the accepted ordinary-basin estimate `rho(basin)/rho(endpoint)<=degree`,
this yields precisely M117's reset envelope

```text
A_0/q <= q(h_0-qS_4)+sum_E T_E^2/C_E.
```

## 5. General-attachment `L=2` proposition

For `X=(S,K_0,R_0,S-2)`, put `D=K_0-R_0`,

```text
p=D/(K_0+1), d_0=D(D+1)/[(K_0+1)(K_0+2)],
p'=D/(K_0+2), q_0=(3/2)RUY, a=UY.
```

Direct enumeration leaves exactly

```text
(2,S-2): q_0/3, 2p
(1,1,S-2): q_0/9, 3d_0
(1,S-1): q_0/(3Y), Y(1-d_0)
(S): R, a(1-p).
```

The three exceptional basins are `(1,1,S-2)`, `(2,S-2)`, and `(1,S-1)`.
Their normalized `(current,capacity)` pairs are

```text
((3d_0-q_0)/9,                    1/3),
((3d_0+6p-4q_0)/9,               2/3),
((Y(1-d_0)-q_0)/(3Y),            2/(3Y)).
```

Their energies give exactly the three squares in M117's `R_2`, while the
ordinary path height gives its first term. There are exactly two descendant
groups. The `(2,S-1)` group has retained mass `1-d_0`, terminal split `Y`,
and normalized charge `(1-d_0)(1-Y)/3`. The unary group has retained mass
`1-p`, child split `a`, unchanged deficit `D`, attachment parameter `p'`, and
charge `(2/3)(1-p)F_1(a,Y,H_1;p')`. Thus the displayed `D_2` normalization is
exact. At `S=3` the first group's children have rank one and are absent;
`Y=1` makes its displayed charge zero.

The fresh bounded audit covers all 252 contexts `3<=S<=9`, `2<=K_0<=9`,
`1<=R_0<K_0`. Literal and aggregate resets agree, and both reset and full
resolvent bounds pass. This proposition bounds `H/q_0`; it is not an
arbitrary-deficit contraction theorem.

## 6. Seven live groups and every rank

For a right-heavy parent,

```text
nu_k(0)=delta_k,
nu_k(j)=(k!/j!)z^(k-j)(1-z)
        prod_(a=1)^(j-2)(1+az)/prod_(a=1)^(k-1)(1+az).
```

The fresh checker compares this with the defining binomial attachment law at
every rank. The complete list is

```text
h=1, k=2: j=1,2       all-deficit L=0
h=1, k=3: j=1,2,3     all-deficit L=0
h=1, k=4: j=1,2,3,4   all-deficit L=0
h=2, k=2: j=1,2       arbitrary-deficit L=1
h=2, k=3: j=1,2,3     arbitrary-deficit L=1
h=3, k=2: j=1         arbitrary-deficit L=2
          j=2         right-heavy L=2
h=4, k=1: j=1         right-heavy L=3.
```

For every row, `deficit=k+1-j`, `sum_(j>=1)nu_k(j)=1-delta_k`, and the child
suffix excess is `h-1`. Multiplying each child bound by its parent mass and
attachment probability, before aggregation, reproduces M117 equation (5.1)
exactly. No rank or child split is missing. When `s=5`, the `h=1` children are
inactive and `x=1` makes their displayed charge zero.

## 7. Universal polynomial certificate

Let `Delta=prod_(a=1)^4(1+az)` and

```text
T=Delta^2[1-q-E_4].
```

Algebraic denominator inspection shows that every attachment and child
denominator divides `Delta^2`. Squared currents make every Cayley ratio at
most quadratic. After clearing, the largest `z` degree is ten: the squared
`delta_4` term has a `z^8` numerator and retains a quadratic factor from
`Delta^2`; a fresh generic slice confirms that degree ten is sharp. Thus the
multidegree is at most, and generically exactly,
`(2,2,2,2,2,10)` in `(r,u,v,y,x,z)`.

The referee implementation evaluates at evenly spaced nodes inside each
certified interval, rationally inverts the Vandermonde matrix, converts power
coefficients to Bernstein coefficients, and applies the transform one tensor
axis at a time. This is independent of M117's integer-node Lagrange route.

For each `s=5,...,21`, the eleventh difference vanishes, the tenth does not,
and all eleven degree-ten Bernstein coefficients on `z in [0,1/2]` are
positive. Across all 187 coefficients, the exact minimum is

```text
71734022477173585947/9023189417984000000000
```

at `s=7`, index zero. Every finite interpolant passes an independent off-grid
identity.

For the tail, `b_n=(n/(n+1))^(n-1)`. The function
`(x-1)log(1+1/x)` is increasing because

```text
log(1+1/x)>1/(x+1)>(x-1)/[x(x+1)].
```

Hence `b_n` decreases. Also `b_n>1/3` follows from
`(1+1/n)^(n-1)<e<3`, and exact arithmetic gives
`b_18=(18/19)^17<2/5`. For `s>=22`, all five ratio indices are at least 18,
so `(r,u,v,y,x)` lies in `[1/3,2/5]^5`.

The three path heights enter `E_4` with nonnegative coefficients: `h_0`
appears as `q h_0`; `h_1` appears inside `F_1` with coefficient equal to its
positive split, including the nested `F_1` in `F_2`; and `h_2` appears in the
`F_2` reset term as its positive child split. Replacing them by one therefore
enlarges the envelope.

On `[1/3,2/5]^5 x [0,1/2]`, all 2673 tensor Bernstein coefficients are
positive. The exact minimum is

```text
742081/227812500 at (2,2,2,2,0,0).
```

Sharp slice degrees and an independent six-dimensional off-grid identity
pass. Bernstein positivity proves the sign everywhere on the full box, not
only on sampled ranks.

## 8. Finite DAG and post-hoc comparison

The literal and grouped full resolvents agree for all 15 roots
`5<=s<=9`, `K in {1,2,5}`. Every root satisfies

```text
exact reset <= reset envelope,
exact H <= q E_4 <= q(1-q).
```

The active literal-basin counts for `s=5,...,9` are
`11,23,47,95,191`. These checks audit formulas; the Bernstein argument gives
universality.

Only after the independent output was complete, a read-only comparison with
the frozen M117 JSON found exact numerator/denominator equality for all 187
finite coefficients, all 2673 tensor coefficients, all 15 common DAG ratios,
and all 252 arbitrary-deficit ratios.

## 9. Referee conclusion

No omitted support row, nested basin, attachment rank, normalization factor,
boundary exception, nonpositive certificate coefficient, or scope inflation
was found.

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
```

The accepted conclusion is auxiliary right-heavy contraction through `L=4`.
The first open suffix excess is `L=5`; every gap, mixing, and terminal claim
remains unresolved.
