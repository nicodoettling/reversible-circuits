# Direct reduction of adjacent-pair bridge mixing to the complete-pair chain

Status: Theorem 3 below is **proved**, using the already accepted
arbitrary-product Hurwitz classification and braided comparison. The
universal complete-pair gap remains **unresolved**.

## 1. Target and kernels

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
Let `N>=3`, `T=T_N`, and `M=|T|=binom(N,2)`. For an even raw length
`m=2l>=4` and feasible `h in A_N`, put

```text
Omega_(2l)(h)={t in T^(2l):t_1...t_(2l)=h}
```

with its uniform law. Let `H_(k,2)` and `H_(k,4)` denote exact
same-product heat baths on the indicated raw block. The lazy adjacent-pair
chain is

```text
J_(2l,h)=1/2 I+1/[2(2l-1)] sum_(k=1)^(2l-1) H_(k,2). (1.1)
```

Group raw factors into microcoordinates
`A_i=(t_(2i-1),t_(2i)) in E=T^2`. The nonlazy aligned chain is

```text
B_(l,h)=1/(l-1) sum_(i=1)^(l-1) H_(2i-1,4).          (1.2)
```

For `i<j`, let `P_(i,j)` be conditional expectation given every raw
microcoordinate except `i,j`, and define the complete-pair chain

```text
C_(l,h)=1/binom(l,2) sum_(i<j) P_(i,j).               (1.3)
```

Every displayed kernel is reversible for the same uniform raw bridge law.
A singleton fiber has gap one.

## 2. Uniform four-letter internal pair gap

For a feasible `g in A_N`, let

```text
L_(4,g)=1/3 [H_(1,2)+H_(2,2)+H_(3,2)]                (2.1)
```

on the uniform fiber `Omega_4(g)`.

### Lemma 1 (proved)

For every `N>=3` and every feasible `g in A_N`, `L_(4,g)` is irreducible and

```text
gap(L_(4,g)) >= delta_4:=2/(3M^7).                    (2.2)
```

### Proof

The accepted Douvropoulos--Lewis type-A specialization (published Theorem 18
and Proposition 8(4), respectively preprint Theorem 4.2 and Proposition
2.7(4), as checked in the M14 l=4 referee) says that two
equal-length transposition factorizations of the same arbitrary product are
Hurwitz-equivalent exactly when their labeled support-graph components and
factor counts on those components agree. Every Hurwitz generator changes one
adjacent pair to another pair with the same product, so it is a positive
`H_(k,2)` outcome.

Within each macro-fiber, the accepted square-tree construction reaches a word
consisting of minimal factorizations of the endpoint cycles, adjacent square
pairs joining endpoint cycles inside each graph component, and adjacent
surplus squares. A square is directly refreshable by `H_(k,2)`:

```text
(a,a) -> (b,b).
```

If `g!=id`, fix one edge `s` inside a nontrivial cycle of `g` and refresh
every bridge and surplus square to `(s,s)`. The resulting macro has each
endpoint cycle as its own component, every fixed point isolated, and every
surplus pair on the chosen cycle; it depends only on `g` and length four. If
`g=id`, both square pairs refresh to one fixed edge. At minimum endpoint
length there is no square and the macro is already unique. Thus every state
reaches one common macro, proving irreducibility. This canonical is used only
for connectivity.

Let `V=|Omega_4(g)|`. The first three transpositions determine the fourth,
so `V<=M^3`. A two-letter product fiber has size `M` for identity, `3` for a
3-cycle, and `2` for a double transposition; hence every selected positive
transition used by a spanning tree has

```text
L_(4,g)(x,y) >= p_*:=1/(3M).                          (2.3)
```

For `V>=2`, choose any spanning tree of the connected transition graph. For
uniform `pi=1/V`, routing each ordered state pair along its unique tree path
gives

```text
Var_pi(f) <=(V-1)/2 sum_(e in tree)(nabla_e f)^2,
E_L(f,f) >=p_*/V sum_(e in tree)(nabla_e f)^2.
```

Therefore `gap(L)>=2p_*/[V(V-1)]>=2/(3M^7)`. For `V=1`, the gap-one
convention is stronger because `M>=3`. QED.

## 3. From aligned four-letter updates to the lazy pair chain

For a reversible kernel `P`, write
`E_P(f,f)=<f,(I-P)f>`. Put

```text
e_k=<f,(I-H_(k,2))f>.
```

### Lemma 2 (proved)

For every feasible `h in A_N` and every `l>=2`,

```text
E_J(f,f)
 >= [3 delta_4(l-1)]/[4(2l-1)] E_B(f,f)
 >= delta_4/4 E_B(f,f)
 >= 1/(6M^7) E_B(f,f).                                (3.1)
```

### Proof

Fix the raw complement of aligned block
`I_i={2i-1,2i,2i+1,2i+2}`. If the fixed prefix and suffix products are
`p=t_1...t_(2i-2)` and `s=t_(2i+3)...t_(2l)`, then the bridge equation
`p (block) s=h` forces the exact block endpoint

```text
g=p^(-1) h s^(-1).
```

The conditional law is uniform on this feasible `Omega_4(g)`, for every
arbitrary outside configuration. Applying Lemma 1
on every such conditional fiber and averaging the outside variables gives

```text
<f,(I-H_(2i-1,4))f>
 <=1/(3 delta_4) sum_(k=2i-1)^(2i+1) e_k.             (3.2)
```

Every raw adjacent boundary belongs to at most two aligned blocks. Averaging
`(3.2)` over `i=1,...,l-1` yields

```text
E_B(f,f) <=2/[3 delta_4(l-1)] sum_(k=1)^(2l-1)e_k.    (3.3)
```

The explicit one-half holding probability in `(1.1)` gives

```text
E_J(f,f)=1/[2(2l-1)] sum_k e_k.                       (3.4)
```

Combining `(3.3)--(3.4)` proves the first inequality. Since
`(l-1)/(2l-1)>=1/3` for `l>=2`, the second follows; Lemma 1 gives the third.
QED.

The comparison uses the four-letter canonical only to prove the fixed-size
conditional gap. It never routes global states through a canonical hub.

### Theorem 3 (proved: direct pair-to-complete reduction)

The accepted M16 braided-collision comparison, Section 2.6, gives as a
Dirichlet-form inequality (with its `T_l` equal to the present `C_(l,h)`),

```text
E_B(f,f)>=1/(2l^2) E_C(f,f).                           (3.5)
```

Consequently, for all `N>=3`, `l>=2`, and feasible `h in A_N`,

```text
E_J(f,f)>=[(l-1)/(4M^7l^2(2l-1))] E_C(f,f)
        >=1/(12M^7l^2) E_C(f,f),
gap(J_(2l,h))>=gap(C_(l,h))/(12M^7l^2).               (3.6)
```

For the identity endpoint, M01's accepted one-step comparison with the lazy
`{3,4,5}` chain `K` gives

```text
gap(K_(N,2l))
 >=gap(C_(l,id))/(36M^9l^2).                          (3.7)
```

Thus an inverse-polynomial complete-pair gap is directly sufficient for
PAIR-GAP and, together with the accepted M01 comparison, Terminal A. This is
new for the auxiliary chain `J`, but is quantitatively redundant for Terminal
A: the already accepted direct comparisons `E_K>=E_B/12` and
`E_B>=E_C/(2l^2)` transfer a universal complete-pair gap to `K` with the
stronger loss `1/(24l^2)`. Equation `(3.6)` supplies the missing explicit
PAIR-GAP reduction, not a stronger Terminal-A route.

The denominator `12M^7l^2` is a conservative uniform simplification. The
sharp coefficient proved by this argument is the first coefficient in
`(3.6)`.

## 4. Supersession map and the remaining complete-pair frontier

The accepted complete-pair CGL deletion recursion is

```text
gap(C_(l,h))
 >= min_q gap(C_(l-1,q)) [1-mu_l(h)],                 (4.1)
```

where `q` ranges over feasible shorter endpoints. The complete chain at
`l=2` is the whole-fiber heat bath and has gap one. Every fixed `l` has an
inverse polynomial in `N` from fixed-length connectivity and a finite-state
tree estimate, but the exponent grows with `l`.

The dense-tail theorem gives `mu_l(h)<5/(4l)` uniformly in the endpoint once
`l>=C_mix N log(N+1)`. Modes centered within one product fiber have exact
additive eigenvalue `1/l`; the remaining coordinate operator factors through
the `O(N^4)` products `id`, 3-cycles, and double transpositions.

The former M27 proposal that this product-increment correlation always obeys
`mu_l(h)<=A/l` is **refuted**, not open. M67 and its fresh referee prove
`mu_l(h)=Omega(l^-1/2)` on the feasible minimal odd-long-cycle family.
Iterating `(4.1)` through that witness would lose
`exp[-Omega(sqrt(l))]`; the scalar accumulation route is dead.

This refutation is not a slow complete-pair gap. M70/M72 prove
inverse-polynomial gap control on every nonzero cyclic character sector for
that fixed minimal-long-cycle bridge, including the whole Krylov closure of
M67's witness. The residual sector is the cyclic-invariant `H_0` quotient.
M73/M80 reduce its positive-correlation problem to endpoint-sharing two-step
influence. M83/M88 refute the tempting one-step `O(1/n)` influence bound but
retain the signed two-step target. M91/M93 reduce the balanced case to
`(BA2)` or direct signed L1; M94/M100 isolate `(BD)`; M102/M105 prove the
exact singular-face asymptotic and show that a naive generic bulk integral is
nonintegrable. A collision/triangle-type counterterm class is therefore
necessary, while the exact complete matching topology is not proved.

Thus the sharp accepted special-family subfrontier is:

> **LONG-CYCLE CYCLIC-INVARIANT `H_0` GAP (unresolved).** Prove an
> inverse-polynomial gap for the exact stationary-flow cyclic quotient of the
> complete-pair chain on minimal factorizations of the odd long cycle. The
> present interface is the endpoint-sharing signed two-step estimate; its
> balanced `(BA2)`/direct-L1/`(BD)`/matched-finite-part chain is a tested
> necessary subproblem.

For Terminal A, the remaining hypothesis is broader:

> **UNIVERSAL COMPLETE-PAIR GAP (unresolved).** There are universal
> `c>0,C<infinity` such that for every `N>=3`, `l>=2`, and feasible
> `h in A_N`,
>
> ```text
> gap(C_(l,h))>=c(Nl)^(-C).                            (4.2)
> ```

Equation `(3.6)` proves that `(4.2)` implies PAIR-GAP. The long-cycle `H_0`
problem is a necessary fixed-endpoint subcase, not a replacement for
arbitrary endpoints. No single fixed `l` is the obstruction: each fixed
length has a crude polynomial bound, while uniformity in growing `l` and in
the endpoint remains open.

## 5. Boundary and scope audit

- `N=2`: every feasible transposition word is forced; excluded above and
  singleton by convention.
- Odd raw identity length: empty by sign.
- `m=0`: singleton; `m=2`: the auxiliary whole-pair heat bath has gap one,
  while the project `{3,4,5}` kernel is not defined there.
- `m=4` (`l=2`): all formulas retain the whole aligned H4 block and three raw
  adjacent H2 scans.
- Nonidentity endpoints in Theorem 3 must lie in `A_N`, because raw length is
  even; infeasible fibers are not assigned a gap.
- No finite spectrum, stationary average square rate, or qualitative
  irreducibility is promoted to a growing-length gap.
- The four-letter canonical is confined to a fixed conditional block. No
  global flow is routed through it.
- The comparison is one-way. A small complete-pair or pair-chain gap would
  not by itself prove Terminal B for `K`.

Therefore Theorem 3 is a strict direct reduction, not a Terminal-A proof.
PAIR-GAP, the long-cycle `H_0` subfrontier, the universal complete-pair gap,
and both Terminals remain open. Universal `mu_l(h)<=A/l` is refuted.
