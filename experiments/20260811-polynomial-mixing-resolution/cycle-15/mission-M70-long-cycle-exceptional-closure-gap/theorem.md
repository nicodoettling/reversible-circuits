# Polynomial sandwich for the minimal-long-cycle exceptional mode

Date: 2026-08-12. Permutations compose as `(pq)(x)=p(q(x))`, and tuple
products are left-to-right.

Let `l>=3`, `n=2l+1`, `m=2l=n-1`, `M=binom(n,2)`, and
`h=(0 1 ... n-1)`. Let `Omega_h` be the uniform bridge of length `m`
transposition factorizations of `h`. Since `m` is the transposition length of
`h`, every state is a minimal factorization. Group consecutive raw factors
into pair coordinates `X_j=(t_(2j-1),t_(2j))`.

Define three self-adjoint chains on this same fixed-endpoint space:

```text
C_l=binom(l,2)^(-1) sum_(i<j) P_(i,j),
B_l=(l-1)^(-1) sum_(j=1)^(l-1) P_(j,j+1),
K^h=(1/2)I+(1/6)sum_(r=3)^5
       (1/(m-r+1))sum_(i=1)^(m-r+1) H_(i,r).
```

Here `P_(i,j)` is the exact heat bath of pair coordinates `i,j`, and
`H_(i,r)` is the exact length-`r` raw-factor heat bath. The superscript on
`K^h` emphasizes that its endpoint is `h`, not identity.

## Theorem

Let `F` be the aligned additive M67 frequency-two witness defined in Section
1. Then:

1. For all sufficiently large `l`,

   ```text
   gap(C_l)<=R_C(F)=O(l^(-3/2)),
   gap(B_l)<=R_B(F)=O(l^(-3/2)),
   gap(K^h)<=R_(K^h)(F)=O(l^(-3/2)).                 (T.1)
   ```

2. Let `U` be simultaneous conjugation of every raw factor by `h`, and let

   ```text
   H_k={Phi:U Phi=omega^(2k)Phi},  k in Z_n,
   omega=exp(2pi i/n).
   ```

   Every `H_k` reduces all three chains. For every `k!=0` and every
   `Phi in H_k`,

   ```text
   R_B(Phi)>=4/[M^4 n^6],
   R_C(Phi)>=8/[l M^4 n^6],
   R_(K^h)(Phi)>=1/[3M^4 n^6].                       (T.2)
   ```

   On `H_1`, which contains `F`, the constants improve to

   ```text
   R_B(Phi)>=16/[M^4 n^6],
   R_C(Phi)>=32/[l M^4 n^6],
   R_(K^h)(Phi)>=4/[3M^4 n^6].                       (T.3)
   ```

3. For `P in {C_l,B_l,K^h}`, the smallest exact `P`-invariant subspace
   containing the witness is

   ```text
   V_P(F)=span{F,PF,P^2F,...} subset H_1.             (T.4)
   ```

   It therefore has the polynomial lower bound (T.3) and the polynomial
   Rayleigh upper bound (T.1). In particular, the accepted
   `Omega(l^-1/2)` coordinate-correlation witness is a genuine polynomially slow
   direction, but its complete invariant closure cannot have a
   superpolynomially small gap.

These are scoped fixed-long-cycle results. They do not bound the invariant
sector `H_0`, the complete global bridge gap, or the identity-conditioned
chain in Terminal A/B.

## 1. Exact Rayleigh upper bounds

Let M67's accepted product-coordinate feature be

```text
a((rs))=-(omega^(-r)-omega^(-s))^2,
f(g)=E[a(t_1)+a(t_2)|t_1t_2=g],
f_i=f(t_(2i-1)t_(2i)),
F=sum_(i=1)^l f_i.
```

Put

```text
V=E|f_1|^2,
C=Re E[conj(f_1)f_2],
kappa=C/V.
```

The central two-position law makes `V,C` independent of the selected
positions. M67 proves

```text
C=48/n+o(n^-1),
V<=2d_0 n^(-1/2)+o(n^-1/2),
kappa>=(24/d_0)n^(-1/2)+o(n^-1/2),                  (1.1)
```

where `d_0=11.2404385426...`. In particular `C>0` eventually. The nontrivial
cyclic character centers `F`, and exactly

```text
||F||^2=lV+l(l-1)C=lV[1+(l-1)kappa].                (1.2)
```

For any pair-coordinate heat bath,

```text
(I-P_(i,j))F=(I-P_(i,j))(f_i+f_j).
```

Orthogonal-projection contraction therefore gives

```text
<F,(I-P_(i,j))F>
 =||(I-P_(i,j))F||^2
 <=E|f_i+f_j|^2=2(V+C).                              (1.3)
```

Averaging (1.3) with the exact scan coefficients yields both

```text
R_C(F),R_B(F)
 <=2(1+kappa)/[l(1+(l-1)kappa)].                    (1.4)
```

For a raw window of length at most five, let `J` be the set of pair
coordinates it touches. Then `|J|<=3`, all untouched `f_j` are measurable
outside the window, and, for sufficiently large `l` when `C>=0`,

```text
||(I-H_(i,r))F||^2
 <=E|sum_(j in J)f_j|^2
 =|J|V+|J|(|J|-1)C
 <=3V+6C.                                             (1.5)
```

The total coefficient of the three normalized nonlazy scans inside `K^h` is
`3/6=1/2`, so

```text
R_(K^h)(F)
 <=(3+6kappa)/[2l(1+(l-1)kappa)].                   (1.6)
```

Since `0<kappa<=1` and (1.1) gives `kappa>=c/sqrt(l)` eventually, (1.4) and
(1.6) are `O(l^-3/2)`. This proves (T.1) with every scan and laziness factor.

## 2. Exact character decomposition and full twist

Define the state bijection

```text
mathcal U(t_1,...,t_m)
 =(h^(-1)t_1h,...,h^(-1)t_mh)
```

and its Koopman operator `U Phi=Phi composed with mathcal U`. It preserves
the endpoint because the conjugated product is `h^(-1)hh=h`. Every exact
same-product conditional fiber is carried bijectively to its conjugate fiber;
hence every heat-bath projection, and all three chains, commute with `U`.
This proves the reducing decomposition into the `H_k`.

The feature obeys `a(h^(-1)t h)=omega^2a(t)`, so `F in H_1`. For a
self-adjoint finite-state operator, (T.4) is exactly the intersection of all
invariant subspaces containing `F`; commutation with `U` puts it inside
`H_1`.

Let the project Hurwitz bijection on adjacent raw positions be

```text
sigma_i(...,t_i,t_(i+1),...)
 =(...,t_(i+1),t_(i+1)t_i t_(i+1),...).              (2.1)
```

It preserves the word product and uniform measure. A direct induction gives

```text
delta:=sigma_1 sigma_2 ... sigma_(m-1):
(t_1,...,t_m) ->(t_2,...,t_m,h^(-1)t_1h).            (2.2)
```

Indeed, after moving `t_1` through the suffix, it is conjugated by
`t_2...t_m=t_1h`; since `t_1^2=id`, the last factor is `h^(-1)t_1h`.
Consequently

```text
delta^m=mathcal U.                                    (2.3)
```

This explicit full-twist word has length

```text
L=m(m-1),                                             (2.4)
```

and each generator index occurs exactly `m` times.

Let `S_i` be the Koopman unitary of `sigma_i`. Telescoping (2.3), Cauchy--
Schwarz, and invariance under every Hurwitz prefix give, for `Phi in H_k`,

```text
4sin^2(2pi k/n)||Phi||^2
 =||(U-I)Phi||^2
 <=L sum_(s=1)^L ||(S_(i_s)-I)Phi||^2.               (2.5)
```

Let `R_i` be the adjacent two-raw-factor same-product heat bath. The Hurwitz
map permutes each `R_i` conditional fiber and fixes its outside coordinates.
Thus

```text
||(S_i-I)Phi||^2
 =||(S_i-I)(I-R_i)Phi||^2
 <=4<Phi,(I-R_i)Phi>.                                (2.6)
```

With `L_n=(m-1)^(-1)sum_i R_i`, equations (2.4)--(2.6) yield the exact
sector inequality

```text
R_(L_n)(Phi)
 >=sin^2(2pi k/n)/[m^2(m-1)^2].                      (2.7)
```

The following edgewise comparison is needed on the full minimal bridge.  M27's
stated spectral theorem was restricted to a fixed parking-label multiset, so
we prove the stronger edgewise statement here instead of citing that scoped
theorem:

```text
E_(B_l)>=M^(-4)E_(L_n).                              (2.8)
```

Indeed, let `x!=y` be an `L_n` edge.  Then `x,y` differ at one unique adjacent
raw pair `(i,i+1)` and that pair has the same ordered product in the two
words.  (Changing only one of the two factors while preserving their product
is impossible.)  Choose an aligned four-position window containing the pair:
start at `i` for an interior odd `i`, at `i-1` for even `i`, and at `m-3` for
the final pair `i=m-1`.  Keep the other two padding factors fixed.  The target
word `y` has the same four-factor product and is therefore an actual outcome
of this aligned heat bath, irrespective of whether its parking macro changes.
The aligned scan chooses the window with probability `1/(l-1)`, and its fiber
has at most `M^4` words, so

```text
B_l(x,y)>=1/[(l-1)M^4].                              (2.8a)
```

Minimality rules out a repeated adjacent edge.  Hence the raw two-factor
product is a 3-cycle or a double transposition, whose ordered transposition
fiber has size three or two.  The unique scan position therefore gives

```text
L_n(x,y)<=1/[2(m-1)].                                (2.8b)
```

Equations (2.8a)--(2.8b) imply the deliberately loose pointwise inequality
`B_l(x,y)>=M^-4 L_n(x,y)` for every off-diagonal edge (`m=2l`), and summing
against the common uniform stationary law proves (2.8).  No fixed-multiset
restriction, rejected-exit convention, or deterministic common hub is used.

Because `n` is odd, multiplication by two permutes the nonzero residues.
For `k!=0`,

```text
|sin(2pi k/n)|>=sin(pi/n)>=2/n.                      (2.9)
```

Also `m,m-1<n`, so (2.7)--(2.9) prove the first inequality of (T.2). For
`k=1`, `sin(2pi/n)>=4/n` when `n>=5`, proving the first inequality of (T.3).

The complete-pair chain contains all adjacent pair-coordinate projections:

```text
E_(C_l)>=[(l-1)/binom(l,2)]E_(B_l)=(2/l)E_(B_l).     (2.10)
```

The fixed-endpoint local chain contains every aligned length-four window:

```text
E_(K^h)>=[(l-1)/(6(m-3))]E_(B_l)
         =[(l-1)/(6(2l-3))]E_(B_l)
         >=(1/12)E_(B_l).                            (2.11)
```

Equations (2.10)--(2.11) prove the remaining bounds in (T.2)--(T.3).

## 3. Residual zero-frequency quotient and scope

The only character not controlled by (2.5) is `H_0`, on which the full twist
acts trivially. Its exact reduction is nonetheless explicit. The cyclic group
generated by `mathcal U` acts freely on `Omega_h`: if a nonidentity power
fixed a word, it would fix each transposition's two-element support set, but a
nontrivial power of an odd long cycle has only odd cycles of length at least
three and fixes no two-element set. Dénes' count `|Omega_h|=n^(n-2)` therefore
gives exactly `n^(n-3)` orbits.

Thus `H_0` is isometric to functions on

```text
Omega_h/<mathcal U>,                                  (3.1)
```

with uniform orbit law. Since every chain commutes with `mathcal U`, its
restriction is the exact stationary-flow quotient

```text
bar P(O,O')=(1/n)sum_(x in O)P(x,O').                (3.2)
```

This quotient is still exponentially large, and no polynomial gap is inferred
from its size. Cyclic relabeling/rerooting is zero-cost there, suggesting an
unrooted leaf-replant or basis-exchange comparison, but the parking macro is
not lumpable and such a comparison requires full stationary-flow accounting.

There is also a sharp exact description of what survives when one starts with
a function of Stanley's parking multiplicity vector `d(w)`.  For a cyclic
orbit `O`, define its parking-macro incidence law

```text
nu_O(d)=(1/n)#{q in Z_n:d(mathcal U^q w)=d},  w in O. (3.3)
```

Then the cyclic projection of any macro function is exactly
`A_0f(O)=sum_d nu_O(d)f(d)`.  Thus its surviving quotient is the family of
incidence laws `nu_O`, not the original rooted macro.  Exact enumeration for
`3<=n<=7` gives rational image ranks `1,4,10,36,116`.  On the odd subsequence
the image is already nonconstant at `n=5`; at the first M70 value `n=7` its
rank is `116`, and it is not determined by the unlabeled support-tree degree
multiset.  This rigorously refutes the claim that cyclic averaging kills every
centered parking-macro function, but the finite ranks prove no asymptotic gap.

The original goal chain is uniform on identity words. A long-cycle prefix
fiber is not closed under windows crossing its endpoint boundary. Embedding a
word from `Omega_h` and an inverse suffix into an identity bridge neither
preserves stationary mass nor controls those crossing `H3,H4,H5` transitions.
Therefore (T.1)--(T.3) do not give a slow mode or a gap theorem for original
identity-conditioned `K`.

The smallest remaining standalone proposition is:

> **CYCLIC-ORBIT INCIDENCE GAP.** The exact stationary-flow quotient (3.2)
> of `C_l` or `B_l`, including the nonconstant incidence statistics (3.3),
> has inverse-polynomial gap in `n`.

This proposition would complete the fixed-minimal-long-cycle bridge, not the
universal arbitrary-endpoint or identity theorem.
