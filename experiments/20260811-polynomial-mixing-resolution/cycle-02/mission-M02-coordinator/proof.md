# Exact stationary-flow macro projection and square down-up comparison

## 1. Macro states and stationary weights

Throughout, `(pq)(x)=p(q(x))`.  Let `T=T_N` and
`M=|T|=binom(N,2)`.  For a word `w`, its macro datum `A(w)` is the unordered
collection

```text
alpha = {(B,k_B)}
```

where the `B` are the nontrivial labeled connected components of its
factorization graph and `k_B` is the number of word positions whose edge lies
in `B`.  Isolated labels are implicit.  A datum is feasible exactly when its
blocks are disjoint, every `|B|>=2`, every `k_B` is even and at least
`2(|B|-1)`, and `sum_B k_B=m`.

For a fixed labeled `v`-set, let `C(v,k)` be the number of connected identity
transposition words of length `k` on exactly that support.  The inherited
macro-fiber factorization gives the exact fiber size

```text
W_m(alpha)
  = m! product_{(B,k_B) in alpha} [C(|B|,k_B)/k_B!].       (1.1)
```

Indeed, choose the independent internal connected words and then their
uniform color interleaving.  Thus, with `Z_m=|Omega(N,m)|=M^m p_m`, the exact
projected stationary law is

```text
mu_m(alpha)=W_m(alpha)/Z_m.                                (1.2)
```

Formula (1.1) retains all labeled blocks and all color interleavings.

## 2. Exact projection formula for all block sizes

For `r in R_m`, a word `w`, and a window beginning at `i`, write

```text
h_{i,r}(w)=t_i ... t_{i+r-1},
F_r(h)=#{a in T^r : a_1...a_r=h}.
```

For a target macro datum `beta`, let

```text
N_{i,r}(w,beta)
 = #{a in T^r : product(a)=h_{i,r}(w),
                   A(w with its i-window replaced by a)=beta}.
```

The JSTV stationary-flow projection is exactly

```text
bar_K(alpha,beta)
 = (1/2) 1{alpha=beta}
   + (1/(2|R_m|)) sum_{r in R_m} (1/(m-r+1))
       sum_{i=1}^{m-r+1} (1/W_m(alpha)) sum_{w:A(w)=alpha}
          N_{i,r}(w,beta)/F_r(h_{i,r}(w)).                 (2.1)
```

This is an exact finite formula for every transition induced by `r=3,4,5`;
no reachability-to-rate inference is made.  Equivalently,

```text
bar_Q(alpha,beta)=mu(alpha)bar_K(alpha,beta)
 = sum_{x:A(x)=alpha,y:A(y)=beta} pi(x)K(x,y).             (2.2)
```

Reversibility of each heat bath makes (2.2) symmetric, so `bar_K` is
reversible for (1.2).

## 3. A fixed-slot square down-up chain

For a feasible length-`m-2` macro datum `gamma` and an edge `t in T`, let
`A_t gamma` be the macro datum obtained by inserting the adjacent square
`(t,t)` into any word in the `gamma` fiber.  It is independent of the chosen
word and position.  Concretely:

- if the endpoints of `t` lie in the same active block, that block's weight
  increases by two and total surplus increases by one;
- if they lie in different blocks, allowing an isolated singleton as a
  zero-weight block, the blocks merge and their weights plus two are added;
  total surplus is unchanged;
- two isolated endpoints create a size-two, weight-two component.

Put

```text
d_gamma(alpha)=#{t in T : A_t gamma=alpha}.                (3.1)
```

Define a word chain `R` as follows: inspect positions one and two.  If they
are unequal, hold.  If they are `(t,t)`, choose `s` uniformly from all `M`
transpositions and replace them by `(s,s)`.  This preserves the exact ordered
product and is symmetric for the uniform bridge law.  Its stationary-flow
projection `S` has, for distinct `alpha,beta`, the exact transition

```text
S(alpha,beta)
 = [1/(M W_m(alpha))] sum_gamma W_{m-2}(gamma)
       d_gamma(alpha)d_gamma(beta),                         (3.2)
```

and diagonal equal to the remaining row mass.  To verify stochasticity, note
that `sum_beta d_gamma(beta)=M` and that

```text
[1/W_m(alpha)] sum_gamma W_{m-2}(gamma)d_gamma(alpha)
```

is exactly the conditional probability that the first two positions are
equal in the uniform `alpha` fiber.  Reversibility follows because multiplying
(3.2) by (1.2) makes it symmetric in `alpha,beta`.

## 4. Exact `K`-to-`S` stationary-flow comparison

If a source word begins `(t,t,c,...)`, its first length-three block has
product `c`.  Replacing it by `(s,s,c)` is one outcome of `H_{1,3}`.  The
length-three fiber size for a fixed transposition `c` is

```text
D_N:=F_3(c)
 = M + 3[2(N-2)] + 2 binom(N-2,2)
 = (3N^2+N-12)/2.                                         (4.1)
```

The three terms correspond respectively to the third factor being `c`,
sharing exactly one endpoint with `c`, or being disjoint from `c`; the
associated two-transposition fiber sizes are `M`, `3`, and `2`.  In
particular,

```text
D_N <= 4M.                                                 (4.2)
```

The exact contribution of the selected `r=3`, `i=1` update to each specified
square replacement is

```text
1/[2|R_m|(m-2)D_N].                                       (4.3)
```

The corresponding `R` transition is `1/M`.  Therefore, off the diagonal,

```text
K(x,y) >= c_sq R(x,y),
c_sq=M/[2|R_m|(m-2)D_N] >= 1/[24(m-2)].                  (4.4)
```

Averaging (4.4) within macro-fibers gives the pointwise projected comparison
and hence

```text
E_{bar_K}(g,g) >= c_sq E_S(g,g),
gap(bar_K) >= c_sq gap(S).                                (4.5)
```

More explicitly, every distinct pair `alpha,beta` has stationary flow

```text
bar_Q(alpha,beta)
 >= [1/(Z_m 2|R_m|(m-2)D_N)]
       sum_gamma W_{m-2}(gamma)
          d_gamma(alpha)d_gamma(beta).                     (4.6)
```

This identifies quantitatively useful merge, split, support-expansion,
support-contraction, and surplus-transfer moves.  The possibly small ratio
`W_{m-2}(gamma)/W_m(alpha)` is visible rather than canceled.

## 5. Qualitative connectivity and the quantitative frontier

Every feasible macro datum has an identity representative made entirely of
adjacent square pairs: doubled tree edges inside each component plus surplus
pairs.  At the macro level a transition of `S` may replace any one of these
pair edges, because the selected pair can be placed in positions one and two.
Replacing the at most `m/2` pair edges successively by a fixed transposition
connects every macro datum to the single component on its two endpoints with
weight `m`.  Thus `S`, and consequently `bar_K`, is irreducible, with macro
diameter at most `m` via this common state.

The diameter statement is not a gap proof.  The common state can have
exponentially small stationary mass, and (4.6) does not bound multicommodity
congestion.  The exact remaining proposition is:

> **SQUARE-DOWN-UP-GAP.** There are universal `c>0,C<infinity` such that for
> every `N>=3` and even `m>=4`, the chain `S` in (3.2) satisfies
> `gap(S)>=c(Nm)^(-C)`.

By (4.5), this proposition would prove the projection constituent of JSTV,
but it would not prove the rejected-exit restriction gaps.
