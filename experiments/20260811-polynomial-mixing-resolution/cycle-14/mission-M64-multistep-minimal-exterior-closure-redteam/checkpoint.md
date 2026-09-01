# M64 halfway checkpoint: exact shell identity and polynomial terminal radius

## Status

The literal exterior breadth-first closure has an exact two-term boundary
identity.  Every fixed radius is polynomially leaky.  More strongly, the
positive-transition graph induced by `F_N^c` is connected with explicit
diameter `O(N^2m^3)`, so the closure equals all of `F_N^c` at a polynomially
growing radius and the M62 complement bound applies.  The remaining open
window consists of intermediate radii that grow with `N` but have not yet
saturated the exterior graph.

## 1. Exact layer identity

Let `G_K` be the undirected positive-transition graph of the literal kernel,
put `X=F_N^c`, and define

```text
E_0={y in X:K(x,y)>0 for some x in A},
E_(k+1)=E_k union {y in X:K(x,y)>0 for some x in E_k},
L_0=E_0,   L_k=E_k minus E_(k-1),
C_k=A union E_k.
```

With `W=|Omega(N,m)|` and `s_k=min{|C_k|,W-|C_k|}`, symmetry and the
breadth-first definition give the exact identities

```text
pi(C_k)=|C_k|/W,

Q_K(C_k,C_k^c)
 =W^(-1) [
    sum_(x in C_k) K(x,F_N minus A)
   +sum_(x in L_k) K(x,L_(k+1))
  ],

Phi_pm(C_k)
 ={the bracketed sum}/s_k.                            (1.1)
```

There are no omitted exterior edges: every exterior neighbor of `A` is in
`E_0`, every exterior neighbor of `E_(k-1)` is in `E_k`, and an exterior
neighbor of `L_k` outside `E_k` is exactly in `L_(k+1)`.  Formula (1.1)
retains all H3/H4/H5 transitions and the exact smaller-side orientation.

## 2. Quantitative shell criterion and fixed radii

Put

```text
D_out=sum_(r=3)^5 (m-r+1)M^r,
p_min=1/[2|R_m|(m-2)M^5],
alpha_N=(N-2)/[6(m-2)D_N Lambda_N],
D_N=(3N^2+N-12)/2,
Lambda_N=binom(m,2)(N-1)^2.
```

Every positive off-diagonal transition is at least `p_min`.  The M63
alternate-leaf targets give total `F_N minus A` flow at least
`alpha_N |A|/W`.  Every state of `L_(k+1)` has a predecessor in `L_k`, so
(1.1) yields the exact-cardinality lower criterion

```text
Phi_pm(C_k)
 >=[alpha_N|A|+p_min|L_(k+1)|]/s_k.                  (2.1)
```

Also

```text
|E_k|<=|A| sum_(j=1)^(k+1) D_out^j.
```

For `N>=5,m=2N-2`, safely `D_out<=N^11` and
`alpha_N>=1/(96N^6)`.  Therefore, for every fixed integer `k>=0`,

```text
Phi_pm(C_k)>=1/[288 N^(11k+17)].                     (2.2)
```

The exponent in (2.2) depends on `k`; it does not settle a growing radius.
Equation (2.1) shows exactly what a Terminal-B radius would require:
simultaneously `|A|/s_k` and `|L_(k+1)|/s_k` must be superpolynomially
small.

## 3. Exterior induced connectivity and saturation radius

For a state in `X`, let its labeled support components (isolates included)
have count `c`, and write a nontrivial component weight as

```text
k_i=2(v_i-1)+2g_i.
```

At `m=2N-2`, exact length accounting gives

```text
sum_i g_i=c-1.                                       (3.1)
```

Thus some component has a surplus square whenever `c>=2`.  Within a fixed
macro, the accepted quantitative Classification-H construction reaches any
chosen paired representative in at most

```text
H_N=50Nm^3
```

Hurwitz moves.  Every Hurwitz move is one literal padded-H3 positive edge.
At a paired representative, refresh a surplus square to a cross-component
square.  This merges two components, changes `(c,G)` to `(c-1,G-1)`, and
stays in `X` while `c>=3`.  Repeating reaches `c=2`, with total genus one.

Fix a label `v`.  A tailored paired representative then isolates `v` while
remaining exterior:

- if its component has at least three vertices, refresh its leaf-edge square
  to an internal square on the remainder, then refresh that surplus square
  across the other component;
- if its component has two vertices and genus zero, refresh its sole edge
  square inside the other component, then attach the other endpoint across;
- if it has two vertices and genus one, refresh both edge-square copies
  inside the other component, then attach the other endpoint across.

Every displayed replacement is `tt -> ss`, padded by one unchanged neighbor
to form an actual H3 update.  The final macro is the fixed one with isolated
`v` and a connected `(N-1)`-label component of genus one.  A last Hurwitz
normalization reaches a fixed exterior word `q_v`.

There are at most `c-2` preliminary merges, at most three isolation
refreshes, and at most `c` Hurwitz-normalization stages.  Consequently every
exterior state reaches `q_v` inside `X` in at most

```text
R_ext=50N^2m^3+N+1                                  (3.2)
```

literal positive edges.  Hence the induced exterior diameter is at most
`2R_ext`.  Since `E_0` is nonempty,

```text
E_k=F_N^c for every k>=K_ext:=2R_ext.                (3.3)
```

At those radii `C_k=F_N^c union A`; M62 and complement symmetry give

```text
Phi_pm(C_k)>=1/(24N^13).                             (3.4)
```

This uses diameter only to identify exact set saturation, not to infer a
spectral gap or conductance before saturation.

## 4. Structurally distinct thick bridge-history candidate

To avoid the now-sealed single prefix-product fibers, let `j=N-1`,
`X_j=t_1...t_j`, and let `ell(g)` be transposition length.  Define the thick
endpoint shell

```text
P_(N,q)={w in Omega(N,2N-2):ell(X_j)<=q}.            (4.1)
```

If `a_j(g)` is the number of length-`j` transposition words with product
`g`, its exact mass is

```text
pi(P_(N,q))
 =sum_(ell(g)<=q) a_j(g)^2 / a_(2j)(id).             (4.2)
```

This is a union of many endpoint fibers and automatically absorbs every
H3/H4/H5 update whose window does not cross the midpoint.  A crossing update
can change `ell(X_j)` by at most eight, and the complete action probability
is at most

```text
rho_m=sum_(r=3)^5 (r-1)/[6(m-r+1)] <=3/[2(m-4)].    (4.3)
```

Thus its full boundary is supported on the exact width-eight endpoint shell.
The finite mass/flow audit is pending.  A Terminal-B use would require a
median-oriented shell ratio that is superpolynomially small; locality alone
only supplies the polynomial factor (4.3).

## 5. Current exact computation

The deterministic `N=5,m=8` enumerator is running on the accepted balanced
path-core cut.  It constructs the literal maximal one-step exterior halo,
then computes (1.1) exactly by block size.  Its named falsification targets
are a zero next layer, a missing boundary category, or a claimed pointwise
exterior expansion rule.  No finite result will be promoted as asymptotic.

## First open proposition

**INTERMEDIATE EXTERIOR-LAYER EXPANSION.**  Uniformly for
`1<<k<2R_ext`, prove

```text
alpha_N|A|+p_min|L_(k+1)|
 >=(Nm)^(-C) min{|C_k|,|Omega|-|C_k|}
```

with universal `C`, or exhibit an explicit growing radius for which both
terms and the omitted-positive terms in the exact identity (1.1) are
superpolynomially small relative to the correctly oriented side.
