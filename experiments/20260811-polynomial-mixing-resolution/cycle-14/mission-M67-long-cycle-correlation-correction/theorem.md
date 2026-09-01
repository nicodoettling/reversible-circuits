# Corrected minimal-long-cycle product-correlation refutation

Date: 2026-08-12. This is the append-only corrected version of M61's
`minimal_long_cycle_refutation.md` (rejected frozen SHA-256
`2b3be8e7b645a9ea6065f83892ca22d93aae27e76c315bf5d946da435ec07f34`).
It incorporates exact repairs to the disjoint-pair count and shared-endpoint
estimate. The rejected file is not modified.

Permutations compose as `(pq)(x)=p(q(x))`, and tuple products are multiplied
from left to right. All Hilbert spaces are complex. This theorem concerns the
complete-pair auxiliary bridge, not the original local `{3,4,5}` chain.

## Theorem

Let `l>=3`, set `n=2l+1`, and let `h_n=(0 1 ... n-1) in S_n`. Group a
uniform minimal transposition factorization

```text
t_1 ... t_(n-1)=h_n
```

into raw pairs `X_i=(t_(2i-1),t_(2i))`, with products
`G_i=t_(2i-1)t_(2i)`. Let `mu_l(h_n)` be the top mean-zero eigenvalue of
M16's averaged one-coordinate projection `A_(l,h_n)`. Then

```text
liminf_(l->infinity) sqrt(l) mu_l(h_n)
 >=24/(sqrt(2)d_0)=1.5097776376...,

d_0=8/sqrt(2pi) int_0^1
        sin^4(pi x)/[x(1-x)]^(3/2) dx
   =11.2404385426....
```

Consequently no universal finite `A` satisfies `mu_l(h)<=A/l` for every
`N>=3`, feasible `h in A_N`, and
`3<=l<C_mix N log(N+1)`. This refutes PRODUCT-INCREMENT BASE CORRELATION. It
does not upper-bound the complete-pair gap, the aligned-sector gap, or the
gap of original `K`, and it is not Terminal B.

## 1. Exact rank-two moments

Write

```text
omega=exp(2pi i/n),  u_v=omega^(-v),
a((r s))=-(u_r-u_s)^2,
A_k=k^(k-2)/(k-1)!=k^(k-1)/k!,  A_1=1.
```

Since `sum_v u_v^2=0`,

```text
a(t)=sum_v u_v u_(t(v)).                              (1.1)
```

Conjugating every factor by `h_n` preserves the bridge and multiplies (1.1)
by a nontrivial frequency-two character, so `E a(t_i)=0`.

Let `T=sum_(t in T_n)t` in the group algebra. Centrality permits the factors
at any two distinct positions to be moved next to the coefficient extraction,
giving, for every `i!=j`,

```text
Pr(t_i=e,t_j=f)
 =[h_n] e f T^(n-3)/[h_n]T^(n-1),                    (1.2)
[h_n]T^(n-1)=n^(n-2).
```

Thus the joint law is independent of the position separation. If a residual
permutation of transposition rank `r` has cycle sizes `q_1,...,q_k`, its
number of minimal transposition factorizations is

```text
r! product_s A_(q_s).                                 (1.3)
```

This follows by minimally factoring each disjoint cycle and interleaving the
factor lists; it is Féray--Kortchemski, Lemma 2.1.

### 1.1 One-edge moment

For a fixed first edge whose endpoints have clockwise gap `d`, the residual
cycle sizes are `d,n-d`, so it has
`(n-2)!A_dA_(n-d)` completions. There are `n/2` unoriented edges for each
value in the sum over `d=1,...,n-1`, and
`|a((r,r+d))|^2=16sin^4(pi d/n)`. Hence, exactly,

```text
v_n:=E|a(t_i)|^2
 =8n (n-2)!/n^(n-2)
   sum_(d=1)^(n-1) A_d A_(n-d) sin^4(pi d/n).         (1.4)
```

The uniform Stirling bound

```text
A_k<=C_0 e^k k^(-3/2)                                (1.5)
```

and the fourth-order sine zeros at both endpoints give an integrable
Riemann-sum envelope. Stirling's formula in (1.4) yields

```text
sqrt(n)v_n -> d_0.                                    (1.6)
```

### 1.2 Disjoint pairs: exact `16n` count

Repeated edges cannot occur in a minimal long-cycle factorization: its
support graph is connected on `n` vertices with exactly `n-1` factor
occurrences, hence is a tree with distinct edges. Direct cycle tracing also
shows that a crossing disjoint chord pair is not an extendible minimal
two-factor prefix.

Every **ordered extendible disjoint pair** has the following unique
parameterization. Choose positive cyclic gaps `a,b,u,v` with
`a+b+u+v=n` and a cyclic start `r`, and put

```text
e=(r,r+a),
f=(r+a+u,r+a+u+b).                                   (1.7)
```

For a nested noncrossing pair, choose `r` at the endpoint preceding the empty
arc of the first ordered chord; this puts it in the same form. Conversely
(1.7) is disjoint and noncrossing. Thus the representation is unique for the
ordered pair. Multiplying (1.7) into the long cycle and tracing the three
resulting cycles gives residual cycle sizes

```text
a, b, u+v.                                            (1.8)
```

Put `s_k=sin(pi k/n)`. Directly from the feature definition,

```text
a(e)=4 exp[-2pi i(2r+a)/n]s_a^2,
a(f)=4 exp[-2pi i(2r+2a+2u+b)/n]s_b^2,

conj(a(e))a(f)
 =16s_a^2s_b^2 exp[2pi i(v-u)/n].                    (1.9)
```

There are exactly `n` choices of `r`, and (1.3),(1.8) give
`(n-3)!A_aA_bA_(u+v)` completions. Pairing the terms `u,v` and `v,u` when
taking the real part yields the exact disjoint-edge contribution

```text
D_n=16n (n-3)!/n^(n-2)
 sum_(a,b,u,v>=1; a+b+u+v=n)
 A_a A_b A_(u+v) s_a^2 s_b^2
 cos(2pi(v-u)/n).                                    (1.10)
```

This proves, rather than assumes, the audit-sensitive factor `16n`.

### 1.3 Shared endpoints: uniform absolute bound

For three cyclic gaps `a,b,c>=1`, `a+b+c=n`, there are six ordered pairs of
distinct edges on the three vertices. Direct cycle tracing shows that exactly
one of the two orders at each possible central vertex is extendible; hence
exactly three are minimal prefixes. Under cyclic relabeling, the three cases
are all represented by the ordered gap sum below. Formula (1.3) gives residual
cycle sizes `a,b,c`; taking absolute values in the three cyclic cases gives

```text
|R_n| <=16n (n-3)!/n^(n-2)
 sum_(a+b+c=n) A_a A_b A_c s_a^2 s_b^2.              (1.11)
```

We now give a uniform summable estimate, rather than a dyadic outline. By
(1.5), after removing the common `e^n`, the sum to bound is

```text
S_n=sum_(a+b+c=n)
       a^(-3/2)b^(-3/2)c^(-3/2)s_a^2s_b^2.           (1.12)
```

At least one of `a,b,c` is at least `n/3`. Uniformly for `1<=k<n`,

```text
k^(-3/2)s_k^2 <= C k^(1/2)/n^2.                     (1.13)
```

On the part `c>=n/3`, apply (1.13) to both `a,b` and use
`c^(-3/2)<=C n^(-3/2)`:

```text
sum_(c>=n/3)(...) <= C n^(-11/2)
 sum_(a,b<=n) a^(1/2)b^(1/2)=O(n^(-5/2)).            (1.14)
```

On the part `a>=n/3`, use `a^(-3/2)s_a^2<=C n^(-3/2)`, apply (1.13) to
`b`, and use `sum_(c>=1)c^(-3/2)<infinity`:

```text
sum_(a>=n/3)(...) <=C n^(-7/2)
 sum_(b<=n)b^(1/2) sum_(c<=n-b)c^(-3/2)
 =O(n^(-2)).                                         (1.15)
```

The `b>=n/3` part is identical. The three parts cover the simplex, so
`S_n=O(n^-2)`. Finally Stirling gives

```text
n e^n (n-3)!/n^(n-2)=O(sqrt(n)).                    (1.16)
```

Combining (1.11)--(1.16) proves

```text
R_n=O(n^(-3/2)).                                     (1.17)
```

### 1.4 Two-edge limit

In (1.10), first sum over `u+v=z` using

```text
sum_(u=1)^(z-1) cos(2pi(z-2u)/n)
 =sin(2pi(z-1)/n)/sin(2pi/n).                        (1.18)
```

The sine zeros again give an integrable boundary envelope with (1.5).
Stirling and dominated Riemann summation give

```text
nD_n -> (4/pi^2) int_(x,y>0,x+y<1)
  sin^2(pi x)sin^2(pi y)sin(2pi(1-x-y))
  /[xy(1-x-y)]^(3/2) dxdy =12.                       (1.19)
```

For completeness, with `s=x+y`, the inner convolution is

```text
int_0^s sin^2(pi x)sin^2(pi(s-x))/[x(s-x)]^(3/2) dx
 =pi^2/s[J_1(2pi s)-2cos(pi s)J_1(pi s)].            (1.20)
```

Substitution, the Bessel equation, and integration by parts evaluate the
unscaled triangle integral as `3pi^2`. Equivalently, expanding the three sine
factors gives an absolutely convergent Dirichlet-integral series; duplication
and Chu--Vandermonde twice give the same value. Together with (1.17),

```text
Re c_n:=Re E[conj(a(t_i))a(t_j)]
 =12/n+o(1/n)                                        (1.21)
```

uniformly for every pair of distinct positions.

Féray--Kortchemski use the opposite multiplication convention
(`sigma tau=tau o sigma`). Reversing the tuple translates their Lemma 2.1,
Proposition 1.1, and Corollary 1.2. The central class-sum derivation (1.2) is
internal to the project convention, so no positional-order ambiguity remains.

## 2. Legitimate product-sector witness

For one raw pair `X=(r,s)`, write `g=rs` and define

```text
B(X)=a(r)+a(s),
f(g)=1/q(g) sum_(r,s in T_n:rs=g)[a(r)+a(s)],        (2.1)
```

where `q(g)` is the number of ordered lifts. Thus `f(G)=E[B(X)|G]` is a
genuine frequency-two function on
`{id,3-cycles,double transpositions}` and is centered.

The raw bridge weight depends on a raw pair only through its product. Given
two products, their raw lifts are independent uniforms on the two product
fibers. Hence, for `i<j`,

```text
E[conj(f(G_i))f(G_j)]
 =E[conj(B(X_i))B(X_j)]=4c_n.                        (2.2)
```

The last equality expands four cross terms and uses (1.2). Conditional
expectation is an `L^2` contraction, so

```text
V_f:=E|f(G_i)|^2
 <=E|B(X_i)|^2
 =2v_n+2Re c_n
 =2d_0 n^(-1/2)+o(n^(-1/2)).                        (2.3)
```

For all sufficiently large `n`, (1.21) is positive. Therefore the real
Rayleigh quotient of M16's forward product-correlation block satisfies

```text
kappa_f:=Re<f,Kf>/||f||^2
 >=(24/d_0)n^(-1/2)+o(n^(-1/2)).                    (2.4)
```

Put the same `f` in all `l` coordinate slots of M16's exact block Gram form.
The Gram numerator is

```text
lV_f+l(l-1)Re<f,Kf>,
```

and the direct-sum norm is `lV_f`, so its Rayleigh quotient is exactly

```text
mu_f=1/l+(l-1)kappa_f/l.                             (2.5)
```

The nonzero spectra of this Gram operator and `A_(l,h_n)` coincide. Thus
`mu_l(h_n)>=mu_f`. Multiplying (2.4)--(2.5) by `sqrt(l)` and using
`n=2l+1` proves the theorem.

## 3. Range and scope

The odd cycle `h_n` is even and its bridge length `n-1=2l` is feasible and
even. For every fixed positive `C_mix`,
`l<C_mix n log(n+1)` for all sufficiently large `l`, so this is a literal
counterexample to the assigned base-range bound.

The `m=0` and `N=2` singleton cases and the excluded `m=2` case are outside
the theorem. It changes none of the `S_3,m=4`, `S_4,m=4`, or `S_4,m=6`
calibrations, and it does not omit the whole-word `H4` update at `m=4`:
original `K` is not being analyzed. The parity identity `Q=P_T^2` is
respected because every paired increment and `h_n` are even.

The conclusion is a lower bound on an auxiliary coordinate-retention mode,
not an upper bound on any chain gap. Inserting it mechanically in the naive
CGL product accumulation yields only an `exp(-Omega(sqrt(l)))` lower-bound
factor, exposing failure of that proof input. A weaker accumulated inequality
or a direct polynomial exceptional-closure gap remains possible.
