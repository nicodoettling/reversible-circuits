# Fixed handle-cycle fibers: exact product law, polynomial tilt, and circularity

Date: 2026-08-12.

Every universal statement below is **PROVED** unless marked otherwise.  The
finite computation at the end is only a falsification audit.  This note uses
no Classification H, no canonical word, and no asymptotic inference from
`d<=4`.

## 1. State law, convention, and kernels

Fix `d>=2`, put `D=2d-1`, and let

```text
X_d={w=(t_1,...,t_(2d)): eval(w)=id, support(w) connected}.
```

Permutations compose as `(pq)(x)=p(q(x))`; word factors multiply left-to-
right.  On `X_d` use the half-lazy signed adjacent-Hurwitz kernel

```text
P_d=(1/2)I+[1/(4D)]sum_(i=1)^D(R_i+R_i^(-1)),          (1.1)
R_i(a,b)=(b,bab),       R_i^(-1)(a,b)=(aba,a).
```

Let `J(w)={j:b(w)<=j<h(w)}` be M97's accepted nonempty interval of central
cuts, `ell(w)=|J(w)|`, and

```text
A_d={(w,j):w in X_d,j in J(w)},
tilde_pi(w,j)=pi_d(w)/ell(w),
L((w,j),(w',j'))=P_d(w,w')/ell(w').                    (1.2)
```

M97/M101 prove `gap(L)=gap(P_d)=:gamma_1(d)`, including the reducible case.
At `d=2`, `X_2` and `A_2` are singletons and every gap below has the declared
singleton value one.  The nontrivial analysis starts at `d>=3`.

## 2. Fixed seam cells and their exact raw product law

At a central cut `w=uv` after `j` factors, put

```text
p=eval(u),  Q_L=support partition of u,
Q_R=support partition of v.
```

Fix a realizable seam key

```text
kappa=(j,p,Q_L,Q_R),
C_kappa={(u,v):(uv,j) in A_d and has key kappa}.       (2.1)
```

Let

```text
U_kappa={u: |u|=j, eval(u)=p, support partition Q_L,
                 every support component has genus zero},
V_kappa={v: |v|=2d-j, eval(v)=p^(-1), support partition Q_R,
                 every support component has genus zero}.
```

**Proposition 2.1 (literal product).**

```text
C_kappa=U_kappa x V_kappa.                             (2.2)
```

Thus the raw uniform law `mu_kappa=Unif(C_kappa)` is the independent product
of the two uniform side laws.  Its exact cardinality is

```text
|C_kappa|=|U_kappa||V_kappa|.                         (2.3)
```

**Proof.**  Membership conditions on `u` and `v` are disjoint once their
products and support partitions are fixed.  Any pair has product
`p p^(-1)=id`.  The accepted M97 incidence theorem says that the bipartite
graph whose vertices are `Q_L,Q_R` and whose edges are the cycles of `p` is
connected unicyclic for every realizable key.  Hence the union of the side
supports is connected, independently of the chosen factorizations.  Both
sides have genus zero by definition, so `j` is central.  Conversely every
word in the cell supplies exactly such a pair.  QED.

There is a finer literal component factorization.  If `C` is a block of
`Q_L`, let `p_C` be the restriction of `p` to `C` and let `c(p_C)` be its
number of cycles.  Genus zero forces exactly

```text
k_C=|C|+c(p_C)-2                                      (2.4)
```

factors supported in `C`.  Let `F(C,p_C,k_C)` be the set of connected
length-`k_C` transposition factorizations of `p_C`.  Scanning a color word
and inserting the next factor from the corresponding component gives

```text
U_kappa = I_(k_C:C in Q_L) x product_(C in Q_L)F(C,p_C,k_C),  (2.5)
|U_kappa| = [j!/product_C k_C!] product_C |F(C,p_C,k_C)|.     (2.6)
```

The same formulas hold for `V_kappa` with `p^(-1)` and `Q_R`.  Isolated
blocks have `k_C=0` and one empty factorization.  Equation (2.4) follows by
adding the genus formula over support components.  It also proves that
conditioning on `p,Q_L,Q_R` introduces no hidden sum over component lengths.

## 3. The lifted conditional: bounded tilt and product-mixture identity

Let `nu_kappa` be `tilde_pi` conditioned on `C_kappa`.  Put

```text
S_kappa=sum_(x in C_kappa) 1/ell(x).
```

Then

```text
nu_kappa(x)=1/[S_kappa ell(x)],
d nu_kappa/d mu_kappa=|C_kappa|/[S_kappa ell(x)].       (3.1)
```

Since `1<=ell<=D`, one has `|C|/D<=S<=|C|`, and hence

```text
1/D <= d nu_kappa/d mu_kappa <= D.                    (3.2)
```

This is the only departure from the raw product law.

It has additional exact structure.  For `x=(u,v)` in a fixed cell define

```text
r_L(u)=j-b(uv)+1,       r_R(v)=h(uv)-j.                (3.3)
```

At fixed `kappa`, the prefix state at time `j` is fixed by `(p,Q_L)`, so the
forward continuation to the unique handle depends only on suffix `v`; hence
`r_R` is side-right.  Under reversal, the state after the reversed suffix is
fixed by the key (the suffix product and `Q_R` are fixed), so continuation to
the reversed handle depends only on `reverse(u)`; hence `r_L` is side-left.
Consequently

```text
ell(u,v)=h-b=r_L(u)+r_R(v)-1,                          (3.4)
1/ell(u,v)=integral_0^1 z^(r_L(u)-1)z^(r_R(v)-1) dz.  (3.5)
```

Thus `nu_kappa` is an exact continuous mixture of product weights on the two
sides.  This may be useful for a later noncanonical variance argument.  It
does not by itself provide a Poincare inequality because a mixture of product
measures may have a slow mixing coordinate.

## 4. Literal moves and the exact fixed-cell restriction

**Proposition 4.1 (internal preservation).**  A signed Hurwitz proposal at
`i<i_cut=j` or `i>j`—that is, with both factors wholly on one side—preserves
`kappa` and cut admissibility.

**Proof.**  A Hurwitz move preserves the ordered product of the changed pair,
so it preserves the whole side product.  It also replaces `(a,b)` by
transpositions supported on exactly the same vertex union: conjugating `a`
by `b` replaces at most one endpoint by the other endpoint of `b`.  More
directly, both oriented maps are braid operations and preserve the subgroup
and support-component partition generated by the whole side.  The other side
is unchanged.  Hence `(j,p,Q_L,Q_R)` is fixed.  Side genera depend only on
length, product cycle count, and support-component count, all fixed; both
remain zero, so `j` remains admissible.  QED.

**Proposition 4.2 (seam separation).**  A proposal at `i=j`, across the
physical seam, either is a self-loop or leaves the fixed key.  In fact, if
the boundary factors are `a,b`, the new prefix products are respectively

```text
p a b       under R_j,
p b a       under R_j^(-1).                            (4.1)
```

because the old prefix is `p` ending in `a`; cancellation shows equality
with `p` exactly when `a=b`.  For equal transpositions both oriented Hurwitz
moves fix `(a,a)`.  Thus no nontrivial seam edge lies inside one cell.  It may
change the key while retaining admissibility or make this cut inadmissible.

Let `P_kappa` be the rejected-exit restriction to `C_kappa` of the raw
fixed-cut physical kernel

```text
P^cut=(1/2)I+[1/(4D)]sum_(i=1)^D(R_i+R_i^(-1)).        (4.2)
```

By Propositions 4.1--4.2 its only off-diagonal edges are literal internal
side Hurwitz edges.  Let `L_kappa` be the standard restriction of `L` to the
same cell (all moves ending outside the cell, including cut refreshes to a
different key, are held).  For distinct `x,y in C_kappa`, equations (1.2)
and (3.1) give stationary edge flows

```text
Q_Lk(x,y)=P_d(x,y)/[S_kappa ell(x)ell(y)],
Q_Pk(x,y)=P_d(x,y)/|C_kappa|,                          (4.3)
Q_Lk/Q_Pk=|C_kappa|/[S_kappa ell(x)ell(y)].            (4.4)
```

Since `|C|/D<=S<=|C|` and `1<=ell<=D`,

```text
D^(-2) <= Q_Lk/Q_Pk <= D.                             (4.5)
```

The density bound also yields, for every function `f`,

```text
D^(-1) Var_mu(f) <= Var_nu(f) <= D Var_mu(f).          (4.6)
```

The upper bound follows by minimizing `E_nu[(f-a)^2]` over `a` and using
`nu<=D mu`; the lower bound is symmetric.  Therefore

```text
D^(-3) gap(P_kappa) <= gap(L_kappa) <= D^2 gap(P_kappa). (4.7)
```

This is the requested quantitative tilt transfer.  It is valid even if a
restriction is reducible, in which case both relevant lower bounds are zero.

## 5. Conditional side tensorization, with all scan normalizations

Define the family of component factor spaces appearing in (2.5)--(2.6).
For such a nonempty connected factorization space `F(C,q,k)`, let

```text
H_(C,q,k)=1/2 I+[1/(4(k-1))]sum_(r=1)^(k-1)(R_r+R_r^(-1)),  k>=2,
```

and give a singleton factor space gap one.  Define the exact unresolved
side input

```text
Gamma_0(d)=min gap(H_(C,q,k)),                         (5.1)
```

where the minimum ranges over every factor space occurring in any realizable
genus-one seam cell on `[d]`, on either side, with componentwise genus zero.
Thus `|C|<=d`, `q` is a permutation of `C`, and
`k=|C|+c(q)-2`.  `Gamma_0(d)` is **UNRESOLVED** uniformly; it is zero if any
such signed-Hurwitz space is reducible.  No Classification H is assumed.

Apply the accepted M05 shuttle construction separately to both side color
interleavings and all component coordinates, but with the full physical scan
denominator `4D`.  Let `P_*` be the equal mixture of all nonempty internal
chains and exactly two side-color slots.  Retain a color slot as the identity
chain when that side has a singleton color space or is empty.  If `s` is the
number of mixture slots, then

```text
2<=s<=d+2<=D+2<=3D.                                   (5.2)
```

The bound uses M97's unicyclic identity
`|Q_L|+|Q_R|=c(p)<=d`: the total number of positive internal component
coordinates is no larger than the total number of partition blocks.

For a nontrivial side color space, the half-lazy adjacent color chain of
length at most `D+1` has gap at least
`2/(D+1)^3>=1/(4D^3)`; an identity color slot is a singleton coordinate with
gap one.  Hence

```text
gap(P_*) >= Gamma_0(d)/(12D^4),                       (5.3)
```

using `Gamma_0<=1`.  A requested internal move shuttles two consecutive
same-component occurrences through disjoint components on its own side and
back.  Its length is `<2(D+1)<4D`.  Metadata
`(side,component,u,v,orientation,stage)` has fewer than
`2*d*D^2*2*4D <=16dD^3<=16D^4` possibilities.  An
internal labeled-generator flow is `mu(x)/[4s(k-1)]<=mu(x)/8`, because
`s>=2` and every nontrivial internal word has `k>=2`; every physical oriented
edge has capacity at least `mu(x)/(4D)`.  Therefore internal comparison
congestion is at most

```text
(16D^4)(mu/8)(4D)/(mu/(4D)) <=32D^6.                 (5.4)
```

Direct color edges contribute at most `3D`; crudely the total is at most
`35D^6`.  Combining (5.3)--(5.4) gives the uniform explicit bound

```text
gap(P_kappa)>=Gamma_0(d)/(420D^10),    d>=3.          (5.5)
```

At `d=2` the cell is a singleton.  Combining (4.7) and (5.5),

```text
gap(L_kappa)>=Gamma_0(d)/(420D^13),    d>=3.          (5.6)
```

The exponent and constant are deliberately loose.  The important point is
that fixed-cell expansion reduces to the side gap with only polynomial loss.

## 6. Projection decomposition and the unresolved seam coefficient

Let the cells `C_kappa` partition `A_d`; write their `tilde_pi` masses
`bar_pi(kappa)`.  Define the exact projection chain

```text
bar L(kappa,lambda)=
  [1/bar_pi(kappa)]
  sum_(x in C_kappa,y in C_lambda) tilde_pi(x)L(x,y), lambda!=kappa,
```

and put the remaining row mass on the diagonal.  It is reversible for
`bar_pi`.  It is also positive semidefinite: it is the compression of the
positive-semidefinite `L` to cell-constant functions.  Set

```text
beta(d)=gap(bar L),                                    (6.1)
```

with singleton projection convention one.  An inverse-polynomial lower bound
on `beta(d)` is **UNRESOLVED**.  Propositions 4.1--4.2 show that its
off-diagonal flow comes from nontrivial physical seam proposals and from the
independent cut refresh in (1.2); this mission proves no lower bound for that
flow.

For completeness, a generic decomposition with explicit constants is
available.  Put

```text
alpha(d)=min_kappa gap(L_kappa).                       (6.2)
```

For any `f`, let `g(kappa)=E[f|C_kappa]`.  Restricted Poincare inequalities
give

```text
sum_kappa bar_pi(kappa) Var(f|C_kappa)
 <= E_L(f,f)/alpha.                                    (6.3)
```

For every cross-cell directed pair `(x,y)` with cell means `g_k,g_l`,

```text
(g_k-g_l)^2
 <=3[(f(x)-f(y))^2+(f(x)-g_k)^2+(f(y)-g_l)^2].        (6.4)
```

Summing stationary cross flow, the first term is at most `3E_L(f,f)` under
the convention `E=(1/2)sum Q Delta^2`.  For a fixed `x`, total outgoing
cross flow is at most `tilde_pi(x)`; the two endpoint terms together are at
most `3 sum_k bar_pi(k)Var(f|C_k)`.  Thus

```text
E_barL(g,g) <=3E_L(f,f)+3 withinVar.                   (6.5)
```

Projection Poincare and total variance now give

```text
Var(f)=withinVar+Var_barpi(g)
 <= [1/alpha+3/beta+3/(alpha beta)] E_L(f,f).
```

Since `alpha,beta<=1`,

```text
gap(L)>=alpha beta/7.                                 (6.6)
```

Combining (5.6), (6.1), and M97's exact spectrum identity yields the proved
conditional implication

```text
gamma_1(d)=gap(L)
 >= Gamma_0(d) beta(d)/[2940 D^13],    d>=3.          (6.7)
```

This is a valid strict coordinate decomposition, but it is not a polynomial
gap result because both `Gamma_0(d)` and `beta(d)` lack quantitative lower
bounds.

## 7. Exact same-size circular cell

Fix an edge `e` on `[d]`, let

```text
kappa_e=(j=2d-2, p=id,
         Q_L={[d]}, Q_R={{endpoints(e)} plus all other isolates}). (7.1)
```

Then

```text
U_kappa_e=Z_d
 ={connected identity words on [d] of length 2d-2},
V_kappa_e={(e,e)},
C_kappa_e=Z_d x {(e,e)}.                              (7.2)
```

Every `z in Z_d` gives a connected genus-one word `z(e,e)`, and the cut is
central.  Conversely the fixed data force exactly (7.2).  Let

```text
P_0,d=1/2 I+[1/(4(2d-3))]
                  sum_(i=1)^(2d-3)(R_i+R_i^(-1))      (7.3)
```

be the half-lazy signed-Hurwitz walk on `Z_d`.  The raw fixed-cell
restriction has `2d-3=D-2` internal positions, each with coefficient
`1/(4D)`, while the last internal square move and the seam move are held.
Therefore exactly

```text
P_kappa_e=[(D-2)/D] P_0,d+[2/D]I,
gap(P_kappa_e)=[(D-2)/D] gap(P_0,d).                   (7.4)
```

For `d=2`, both spaces are singletons and (7.4)'s kernel identity still
holds, while its gap-scaling identity is replaced by the singleton-gap
convention `gap(P_kappa_e)=gap(P_0,2)=1`.

Equation (7.4) is the decisive route obstruction: the fixed-cell theorem
reintroduces the full-label minimal genus-zero Hurwitz gap at the **same
label size `d`**.  There is no induction on labels, length, or genus.  The
bounded `1/ell` tilt changes this by only polynomial factors, not by a new
source of expansion.  Hence (6.7) is a circular sufficient reduction unless
one independently proves the minimal genus-zero gap or bypasses this cell
through projection/mean-lift flow.

This is not evidence that `gamma_1`, `Gamma_0`, or the full heat-bath gap is
small.  It refutes only the claim that M97's fixed-fiber tensorization alone
creates an inductive polynomial-gap proof.

## 8. Exact finite falsification audit

`fixed_seam_audit.py` exhausts `d=2,3,4`.  It found respectively
`1,240,131040` connected genus-one states and `1,336,234720` lifted states.
Across `1,9,101` fixed seam cells it found:

- zero raw-product cardinality failures;
- zero component-length, incidence, or internal-key-preservation failures;
- zero cases in which one side failed to determine its handle distance;
- no nontrivial seam proposal staying in one key;
- maximum within-cell `ell` ratios `1,3,5`, attaining `D`;
- exact `kappa_e` cell sizes `1,24,2880`, matching the known minimal
  connected identity counts, with one suffix word.

At `d=4`, the `kappa_e` tilt has `ell=1,2,3,4,5` with counts
`480,744,936,528,192`.  Thus the lifted conditional is already nonuniform on
the same-size minimal genus-zero coordinate; it is not literally the raw
product law.  These exact finite results calibrate the universal proofs and
falsify stronger assertions only.  They do not establish any asymptotic gap.
