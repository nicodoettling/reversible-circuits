# M37 halfway checkpoint: primitive zipper closes the quadratic-over-log range

## Frozen scoped theorem

Use the project convention and original lazy exact kernel.  For

```text
N>=10^6,                   m=4N^3+4,
A_N=floor(N^2/[100 log(N+1)]),
```

the proof below gives, simultaneously for every `1<=a<=A_N`,

```text
pi(V^(a))<=exp(-4N^2),
Phi_pm^K(V^(a))>=N^(-25).                              (C.1)
```

This reaches the prioritized quadratic-over-log scale.  It remains a scoped
anti-bottleneck theorem, not a global gap theorem.

## 1. Five-factor zipper lemma

Let `H=Stab(z)`.  If `g` is a product of five transpositions, there are a
transposition `tau` and four internal transpositions `a_1,...,a_4` such that

```text
g=tau a_1a_2a_3a_4.                                   (C.2)
```

If `g` moves `z`, take `tau=(z,g(z))`.  Then `h=tau g` fixes `z`; moreover
`z` and `g(z)` lie in the same cycle of `g`, so left multiplication by `tau`
splits that cycle and lowers Cayley transposition length by one.  Thus
`length(h)<=4`.  If `g` fixes `z`, its sign is odd, so choose an internal
transposition splitting a nontrivial cycle of `g`; again `h=tau g` is internal
and has length at most four.  In either case `h` is even and admits an exact
four-transposition internal factorization after square padding, proving
(C.2).

For any `H`-valued block of length at most `4q+1`, pad it on the right by
internal factors to length `4q+1`.  Apply (C.2) to its rightmost five factors,
leaving four internal factors and one transposition carrier.  Sweep left in
strides of four.  On the final window the carrier is internal because the
whole block and peeled suffix are internal.  Exactly `q` positive `H_5`
updates make the padded block internal.

## 2. Exact primitive-excursion count

For a block whose first factor crosses `{z}|[d]`, track

```text
X_j=(prefix product)^(-1)(z).
```

After the first crossing, `X_0 in [d]`.  From any `X_j in [d]`, exactly one
of the `M` transpositions, namely `(z,X_j)`, sends the next state to `z`;
the other `M-1` choices remain in `[d]`.  Therefore the exact number of
length-`l` blocks which start by leaving `z`, have no intermediate return,
and end with the unique return transposition is

```text
d(M-1)^(l-2),                 d=N-1.                   (C.3)
```

Every such primitive block has product in `H`.  The M33 outer encoding has
at most `dM^(l-2)` choices on the same interval, so the complete middle-word
entropy loss is only

```text
[M/(M-1)]^(4a)<=exp(4a/(M-1))<=2                      (C.4)
```

through `a<=A_N`.

## 3. Primitive blocks cannot be shortened by regrouping

Use source layouts with primitive blocks of minimal budgets

```text
q=ceil((l-1)/4),              l in {4q-2,...,4q+1},
sum q=a,
```

at least three internal positions between blocks, and four trailing internal
positions.  At the start and end of each block the prefix inverse-state is
`z`; it never equals `z` inside.  Hence the leftmost subgroup-valued active
cluster must contain the first whole primitive block and can end only after a
later whole primitive block.  Induction partitions all crossings into
clusters containing consecutive whole source blocks.

A group with budgets summing to `Q` has hull length at least

```text
sum(4q_j-2)+3(number_of_blocks-1)>=4Q-2,               (C.5)
```

so it needs at least `Q` update windows.  Push the final return crossing of
the rightmost block through four trailing internal factors.  The block remains
primitive, its span increases by four, and the group containing it now needs
`Q+1` windows.  The target therefore has distance at least `a+1` from the
disconnected set.

## 4. Robust outside words and source coefficient

Fix primitive block words and a layout.  Reserve the first four internal
positions after the rightmost block for the final push.  Among the remaining
`t_0=m-L-4` outside positions, require the concatenated internal word to be
robust.  Since the internal transposition sum is central, after the four
reserved factors are fixed the number of remaining sequences making the
whole word identity is one arbitrary-endpoint coefficient of `T^(t_0)`, at
least `E^(t_0)/d!` at this density.  Summing the `E^4` reserved choices restores
`E^(m-L)/d!`.  The cut/window union bound for nonrobust core sequences has
logarithm

```text
a log t_0+d log 2+log(d!)-2(t_0-5a)/d<=-N^2,          (C.6)
```

so, after restoring the reserved factors, at least
`(1/2)E^(m-L)/d!` endpoint-compatible choices remain.  In the boundary
target the four reserved factors belong to the extended primitive block;
robustness of the untouched core forces any alternate initial cut to be the
isolate cut.

For `c` blocks, layouts with three-position gaps and four trailing positions
number at least `(m-8a)^c/c!`.  Put

```text
A=(M-1)/E,                  D_A=1+A+A^2+A^3,
beta_-=(m-8a)d/E^2,         theta_-=beta_-D_A/A^4,
C=ceil(2sqrt(100a)).
```

Restricting to `c<=C`, the number `B_a` of actual boundary sources satisfies

```text
B_a >=(1/2)E^m/d! A^(4a)
 sum_{c=1}^{min(a,C)}binom(a-1,c-1)theta_-^c/c!.       (C.7)
```

The primitive decomposition is recovered uniquely from returns of the prefix
state to `z`, so no path-history multiplicity enters (C.7).

## 5. Exact entropy match to the whole shell

For the isolate outer count set

```text
R=M/E,                 D_R=1+R+R^2+R^3,
beta=md/E^2,           theta=beta D_R/R^4.
```

Here `theta<=100`.  The function

```text
f(x)=(1+x+x^2+x^3)/x^4=x^-4+x^-3+x^-2+x^-1
```

is decreasing, so

```text
theta/theta_- <=beta/beta_-.                           (C.8)
```

For `c<=C`, the right side raised to `c` is at most two because its logarithm
is at most `16aC/m`.  For `c>=C`, the exact-`a` coefficient ratio is at most
`1/4`, so the omitted large-`c` tail is controlled by its first term.  Finally
`R^(4Q)<=R^(4a)<=(M/(M-1))^(4a)A^(4a)<=2A^(4a)`, and
`binom(Q-1,c-1)<=binom(a-1,c-1)` for `Q<=a`.  Thus the cumulative outer
coefficient costs only `O(a)` times (C.7), not an exponential in `a`.

Including the trace factor and all `N` isolate cuts, and using the same
factorial suppression for every non-isolate cut as in M33, gives the rounded
bound

```text
|V^(a)|<=N^5 B_a.                                      (C.9)
```

The direct outer count and `|Omega|>=2M^m/N!` give the orientation in (C.1).

## 6. Full-kernel flow

The final push is one length-five same-product output, so its original-chain
probability is at least

```text
1/[6(m-4)M^4].                                         (C.10)
```

Retaining only these `Q_5` edges and all sources in (C.7), with every
uncharged `Q_3,Q_4,Q_5` term nonnegative, yields

```text
Phi_pm^K(V^(a))
 >=N^-5/[6(m-4)M^4]
 >=N^-25.                                              (C.11)
```

The final report will retain the loose exponent 25 and state explicitly that
radii larger than `N^2/log N` remain open.
