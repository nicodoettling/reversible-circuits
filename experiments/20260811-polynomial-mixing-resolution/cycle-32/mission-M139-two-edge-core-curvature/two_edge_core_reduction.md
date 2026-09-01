# M139 exact two-edge-core cavity reduction and curvature obstructions

Date: 2026-08-13 UTC.

## 1. Scope and imported input

This note concerns the auxiliary M113/M118 incidence-key law

```text
rho(kappa)=|C_kappa|/Z_inc,
H[d,c]=M[d,d-c].
```

It is not the uniform identity-word law.  The only enumerative inputs are the
M125/M129 exact cycle-type coefficient formula and the M133/M136 positive
unique-cycle expansion.  Let `H_2[d,c]` be M133's contribution whose unique
bipartite incidence core consists of two parallel edges.  The desired
standalone theorem

```text
H_2[d,c]^2 >= H_2[d,c-1] H_2[d,c+1]                 (1.1)
```

for `d>=4`, `3<=c<=d-1` remains unresolved below.  What is proved is an exact
marked-pair recurrence and a formal cavity/Lagrange/beta-integral reduction;
two stronger curvature routes are refuted exactly.

## 2. Marked-pair characterization

Fix indexed cycle atoms `E` with positive sizes `a_e`.  An ordered pair of
partitions `(pi_L,pi_R)` gives a bipartite multigraph whose coloured vertices
are partition blocks and whose labelled edges are the atoms.  On the M125
diagonal

```text
|pi_L|+|pi_R|=|E|,
```

join-indiscreteness makes this graph connected with `V=E`, hence unicyclic.

**Theorem 2.1 (proved).**  Such a graph has core length two if and only if
there is an unordered atom pair `{e,f}` lying in a common block of `pi_L` and
a common block of `pi_R`.  In that case the pair is unique.

**Proof.**  The block condition says exactly that the two labelled edges have
the same left and right endpoints, so they are parallel and form a length-two
cycle.  A connected unicyclic multigraph has only one cycle, so no other such
pair exists.  Conversely, the two edges of a length-two core share both
endpoints and therefore satisfy the block condition.  QED.

This gives an exact recurrence independent of M133's explicit core traversal.
For two fixed marked sizes `a,b` and an unmarked size multiset `nu`, let
`P^bullet_(a,b;nu)(y)` count one-colour weighted partitions in which the marks
are co-blocked.  If `e<=nu`, write `|e|` for its atom count and `||e||` for
its total original-label size.  With M125's ordinary partition polynomial
`P_nu(y)`, exact binomial selection of the other marked-block atoms gives

```text
P^bullet_(a,b;nu)(y)
 = y sum_(e<=nu) binom(nu,e)
       (a+b+||e||)^(|e|-1) P_(nu-e)(y).               (2.1)
```

Indeed the marked block has `2+|e|` atoms, so its block-weight exponent is
`2+|e|-3=|e|-1`.  Put

```text
A^bullet_nu(y,z)=P^bullet_nu(y)P^bullet_nu(z).
```

Both marks already lie in the same join component.  Selecting the unmarked
atoms `e` in that component gives the exact connected extraction

```text
C^bullet_nu
 = A^bullet_nu
   - sum_(proper e<nu) binom(nu,e) C^bullet_e A_(nu-e). (2.2)
```

Summing the diagonal of `C^bullet` over unordered marked atom pairs isolates
the two-edge core exactly by Theorem 2.1.  Equations (2.1)--(2.2) are the
recurrence implemented in `two_edge_core_scan.py`.  They aggregate equal-size
unmarked atoms without changing any indexed multiplicity.

## 3. Labelled atom species and planted cavity

Let

```text
h(a)=a^a/(a-1)!,
q_a=h(a)^2/a=a^(2a+1)/(a!)^2,
xi_a=u q_a x^a.                                      (3.1)
```

The identity

```text
n(lambda) product_i h(a_i)^2
 = d! product_a q_a^(m_a)/m_a!                       (3.2)
```

is exactly the exponential-form translation of M125's cycle-type factor;
`x` marks total size and `u` marks cycle atoms.

For a boundary edge of size `s` and a vector `B=(B_b)_(b>=1)`, define

```text
Phi_s(B)
 = sum_(k>=0) 1/k! sum_(b_1,...,b_k>=1)
     (s+sum_i b_i)^(k-2) product_i B_(b_i),           (3.3)

Psi_s(B)
 = sum_(k>=0) 1/k! sum_(b_1,...,b_k>=1)
     (s+sum_i b_i)^(k-1) product_i B_(b_i).           (3.4)
```

`Phi` is the one-boundary root transform: with `k` child edges the root has
degree `k+1`, hence exponent `k-2`.  `Psi` is the two-boundary core-vertex
transform: the degree is `k+2`, hence exponent `k-1`.

There is a unique formal solution with every `B_a=O(u)` to

```text
T^L_a=y Phi_a(B^R),       B^L_a=xi_a T^L_a,
T^R_a=z Phi_a(B^L),       B^R_a=xi_a T^R_a.           (3.5)
```

Uniqueness follows recursively in the atom marker `u`.  The boundary atom is
not included in `T`; every child edge contributes `xi_b` once and begins the
opposite-colour planted subtree.  The unordered pair of core atoms gives the
factor `1/2`, including equal sizes by the exponential formula.  Therefore

**Theorem 3.1 (proved).**  The two-edge-core species is exactly

```text
U_2(x,u,y,z)
 = yz/2 sum_(a,b>=1) xi_a xi_b
       Psi_(a+b)(B^R) Psi_(a+b)(B^L).                 (3.6)
```

**Proof.**  Delete the two parallel core edges.  Every remaining component is
a tree attached to exactly one of the two core vertices; otherwise the graph
would be disconnected or have another cycle.  Root deletion gives the
unordered child branches in (3.3), with the correct full incident-size
weight.  Conversely, two core edges plus the planted trees from (3.5) create
one connected unicycle of core length two.  The SET factors `1/k!` and `1/2`
account exactly for unordered branches and the unordered core pair.  These
operations are inverse and preserve `x,u,y,z` and all weights.  QED.

## 4. Lagrange collapse of the core vertices

For a fixed vector `B`, let `tau_B` be the unique formal solution

```text
tau_B=sum_(b>=1) B_b exp(b tau_B).                    (4.1)
```

**Lemma 4.1 (proved).**

```text
Psi_s(B)=exp(s tau_B)/s.                              (4.2)
```

**Proof.**  Introduce a child marker `v` and solve
`tau=v sum_b B_b exp(b tau)`.  Lagrange inversion gives, for `k>=1`,

```text
[v^k] exp(s tau)/s
 = 1/k [w^(k-1)] exp(sw)(sum_b B_b exp(bw))^k
 = 1/k! sum_(b_1,...,b_k)
      (s+sum_i b_i)^(k-1) product_i B_(b_i).
```

The constant coefficient is `1/s`, the `k=0` term of (3.4).  Set `v=1`.
QED.

Write

```text
Q(X)=sum_(a>=1)q_a X^a,
I_2(sum_n f_n X^n)=sum_n f_n X^n/n^2,
X=x exp(tau_(B^L)+tau_(B^R)).                         (4.3)
```

Substitution in (3.6) gives the exact product/integral transform

```text
U_2=(u^2 yz/2) I_2(Q(X)^2).                           (4.4)
```

Only the positive one-boundary map `Phi` in the coupled cavity equations
remains.  It too has an exact positive integral representation:

```text
Phi_s(B)
 = integral_0^1 t^(s-1)
     Psi_s((t^b B_b)_(b>=1)) dt.                      (4.5)
```

Indeed a degree-`k` monomial with total child size `S` is multiplied under
the integral by `integral_0^1 t^(s+S-1)dt=1/(s+S)`, changing the exponent in
`Psi` from `k-1` to `k-2` exactly.  Equations (3.5), (4.1), (4.4), and (4.5)
are a strict scalar-core/multitype-cavity reduction of M133's general planted
recurrence.

## 5. Positive beta integral for the cut factorials

For `j=d+c-2L`, the beta identity is

```text
j!(2d-j)!
 =(2d+1)! integral_0^1 t^j(1-t)^(2d-j)dt.             (5.1)
```

Every monomial of `U_2` has total colour degree `L+R=c`.  Set

```text
y=(1-t)/t,       z=t/(1-t).
```

Then `yz=1` and

```text
t^d(1-t)^d y^L z^R=t^(d+R-L)(1-t)^(d+L-R).
```

Combining (3.2) and (5.1) proves the exact extraction

```text
H_2[d,c]
 =d!(2d+1)! [x^d u^c]
   integral_0^1 t^d(1-t)^d
     U_2(x,u,(1-t)/t,t/(1-t)) dt.                    (5.2)
```

Thus (1.1) is reduced to coefficient log-concavity, in `u` at fixed
`x`-degree, of one explicitly defined positive beta integral of the coupled
`Phi` fixed point.  There is no connected-component subtraction and the two
core vertices have already collapsed by Lagrange inversion.

## 6. Exact boundary coefficients

Put

```text
S_n=sum_(a=1)^(n-1)q_a q_(n-a).
```

At `c=2` there are no off-core atoms; at `c=3` one atom attaches to either
coloured core vertex.  Equations (3.6) or a direct block-weight calculation
give

```text
H_2[d,2]=(d!)^3/(2d^2) S_d,                           (6.1)

H_2[d,3]
 =d!(d-1)!(d+1)!
   sum_(n=2)^(d-1) (S_n/n) q_(d-n)/(d-n)^2.           (6.2)
```

For (6.2), a core of total size `n` contributes `1/n` at the unattached
degree-two core vertex, while the off-core leaf of size `d-n` contributes
`1/(d-n)^2`; the attached core vertex has degree three and weight one.  The
two colour choices combine the equal `(d-1)!(d+1)!` cut factors.  The bounded
certificate checks (6.1)--(6.2) against every exact row through `d=18`.

## 7. Why the direct total-positivity route stops

In homogeneous child count `k`, the `Phi` kernel in boundary size `s` and
total child size `S` is, up to the harmless factor `1/k!`,

```text
K_k(s,S)=(s+S)^p,       p=k-2.                        (7.1)
```

For `s_1<s_2`, `S_1<S_2`, its `2x2` minor has the sign of

```text
r(S_2)^p-r(S_1)^p,
r(S)=(s_2+S)/(s_1+S).
```

Since `r` is strictly decreasing, the minor is positive for `p<0`, zero for
`p=0`, and negative for `p>0`.  Hence the homogeneous `Phi` kernels are TP2
for `k=0,1`, rank one for `k=2`, and reverse-TP2 for every `k>=3`.
Degree summation in the cavity equation mixes these orientations, so the
standard same-sign TP2 composition closure does not apply.

This is a genuine local obstruction, not merely a failure to identify a
theorem.  Under the one-species specialization `B_1=t`, `B_b=0` for `b>1`,

```text
Phi_1(t)=1+t/2+t^2/2+2t^3/3+...,
```

whose first ordinary log-concavity margin is

```text
(1/2)^2-1*(1/2)=-1/4.                                (7.2)
```

Thus neither coefficient log-concavity nor a PF strengthening is available
at the raw cavity level.  This does not refute log-concavity after the coupled
fixed point, Lagrange core map, and beta functional in (5.2).

## 8. Exact curvature obstructions and capped finite facts

The first three `d=4` values are

```text
(H_2[4,2],H_2[4,3],H_2[4,4])=(80136,109440,44928).
```

Shifted ULC would require the centre squared to dominate four times the side
product.  It is **REFUTED** exactly:

```text
109440^2-4*80136*44928=-2424287232.                   (8.1)
```

A uniform inverse-linear surplus is also **REFUTED**.  At `(d,c)=(16,12)`,

```text
H_2[16,11]=15339706693275758759417829532728706703572126924800000,
H_2[16,12]= 8801172795119208736433518466349564786249616588800000,
H_2[16,13]= 4798920138978605227248331071925220344236657868800000,
```

and

```text
16 H_2[16,12]^2-17 H_2[16,11]H_2[16,13]
=-12068184285817619472004173248675719963879857493070204183335383575630227635520668657140147159040000000000.
                                                                    (8.2)
```

So a theorem with multiplicative curvature `1+1/d` is false.  The weaker
candidate `1+1/d^2` survives the exact capped scan through `d=18`, but is
only a conjecture.

**EXACT FINITE, not a theorem.**  Ordinary (1.1) has no failure through
`d=18`.  The weakest tested H2 ratio is about `1.03153815847` at
`(d,c)=(18,13)`.  With `E[d,c]=H[d,c]/H_2[d,c]`, the exact M133 budget

```text
H_2[d,c]^2/(H_2[d,c-1]H_2[d,c+1])
 >= E[d,c-1]E[d,c+1]/E[d,c]^2                        (8.3)
```

also has no failure through `d=18`; its weakest tested ratio of left side to
right side is about `1.03265462955`, again at `(18,13)`.  These signs are
falsification data only and supply no asymptotic higher-core bound.

## 9. First unresolved lemma and downstream scope

The first unresolved analytic statement is now:

> For the unique positive formal solution (3.5), prove that the fixed-`x`
> coefficient sequence in `u` of the beta functional (5.2) is log-concave;
> quantitatively, seek at least an inverse-polynomial surplus and compare it
> to the exact higher-core correction in (8.3).

This is narrower than M133's arbitrary-core planted expansion: the core has
been marked, both two-boundary transforms have collapsed to `I_2(Q^2)`, and
the cut factorials are one positive integral.  The remaining obstruction is
the coupled one-boundary `Phi` transform with mixed TP orientation.

Even a future proof of (1.1) does not by itself prove full `H` log-concavity;
the higher-core correction (8.3) remains mandatory.  Full log-concavity would
only imply DEFECT NO-VALLEY, which in turn yields at most M120's conditional
one-dimensional defect-projection gap.  Fixed-defect expansion, `gap(A_d)`,
the handle projection, the original lazy exact `{3,4,5}` heat-bath gap, and
both terminal outcomes remain unresolved.
