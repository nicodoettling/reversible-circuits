# M25 halfway checkpoint: maximal disconnected halo is polynomially leaky

## Exact closure

Use `(pq)(x)=p(q(x))`, `M=binom(N,2)`, `L=N^3`, and
`m=4(L+1)`.  Let `A_N` be the complete macro-fiber union with one connected
size-three weight-four component and one connected complementary component of
weight `4L`, allowing every labeled choice, internal factorization, and color
interleaving.

Count every support-graph component, including isolated labels, and write
`c(w)` for this number.  Define

```text
U_N={w in Omega(N,m):c(w)>=2}.                         (C.1)
```

Then `A_N subset U_N`.  More strongly, `U_N` contains every disconnected
macro datum, so it absorbs:

- all same-macro color swaps;
- every internal factorization move;
- every split or label-isolating move;
- every repartition or partial merge which leaves at least two components.

It is the maximal proper union of complete disconnected macro-fibers.  The
only omitted macro is the unique datum `{([N],m)}` with connected full
support.

This corrects a tempting but invalid shortcut: M23's missing-label set
`{X>=1}` does **not** contain `A_N`, because the two components of `A_N`
together use all `N` labels.

## Dense hypothesis and exact global mass

For `N>=5`, `log(2N)<=N`, and hence

```text
4M log(2N)<=2N^2(N-1)<=2N^3<m-2=4N^3+2.              (C.2)
```

Thus the frozen M12 exact-partition theorem applies at both lengths `m` and
`m-2`.

For a labeled set partition `P`, let `E_P(k)` count length-`k` identity words
with exact support partition `P`, and put

```text
W_c(k)=sum_{P:|P|=c}E_P(k),
Z_N(m)=sum_c W_c(m).
```

The exact stationary mass is

```text
pi(U_N)=sum_{c=2}^{N-1}W_c(m)/Z_N(m).                  (C.3)
```

Every ordered color interleaving is already contained in `E_P`; no graph-only
weight is used.  The audited trace/partition argument proves

```text
W_{c+1}(m)<=q_N W_c(m),       q_N=4/N^4<=1/4.          (C.4)
```

Consequently

```text
sum_{c>=2}W_c(m)
 <=W_2(m)/(1-q_N)
 <=W_1(m)/3,                                           (C.5)

pi(U_N)<=1/4,
W_2(m)/sum_{c>=2}W_c(m)>=1-q_N>=3/4.                  (C.6)
```

This supplies the exact global orientation and says the two-component layer
is at least three quarters of the closure mass.

## Actual full-K boundary flow

Fix an exact two-block partition `P`.  Let `e` be the number of internal
transpositions and `x=M-e` the number crossing its two blocks.  The frozen
exact-support trace estimates at `m` and `m-2` imply that at any fixed
adjacent slot the fraction of `P`-words obtained by inserting a deletable
internal square is at least

```text
e E_P(m-2)/E_P(m)>=1/(4e).                             (C.7)
```

For such a square `(t,t)`, choose any crossing transposition `s` and use the
padded actual heat-bath outcome

```text
(t,t,a)->(s,s,a),             or (a,t,t)->(a,s,s).     (C.8)
```

Deletion leaves exact partition `P`, and inserting `s` merges its last two
components, so the output has `c=1` and exits `U_N`.  The exact length-three
fiber of a transposition product has size

```text
D_N=(3N^2+N-12)/2<=4M.                                 (C.9)
```

Including laziness, the `r=3` choice, its `m-2` windows, and exact heat-bath
normalization, one specified target has probability

```text
1/[6(m-2)D_N].                                         (C.10)
```

Summing all `m-1` marked insertion positions and all `x` crossing choices is
collision-free at the changed adjacent pair.  Therefore the exact averaged
exit probability from every two-component partition is at least

```text
(m-1)[1/(4e)] x/[6(m-2)D_N]
 >=x/(24eD_N)
 >=(N-1)/(96M^2)=alpha_N.                              (C.11)
```

Here `e<=M`, `D_N<=4M`, and a two-block cut has
`x=a(N-a)>=N-1`.

The complete stationary boundary flow is

```text
Q_K(U_N,U_N^c)=Q_3+Q_4+Q_5.                            (C.12)
```

Equation (C.11) retains a certified subset of `Q_3`; `Q_4` and `Q_5`, and all
other `Q_3` merges, remain present and nonnegative.  Combining (C.6) and
(C.11) gives

```text
Phi_pm^K(U_N)
 >=(3/4)alpha_N
 =(N-1)/(128M^2)
 =1/[32N^2(N-1)]
 >=1/(32N^3).                                          (C.13)
```

Thus even the maximal disconnected macro halo cannot yield a
superpolynomial bottleneck.

## Next frontier

There is only one `c=1` macro datum.  Adding that whole macro to `U_N` gives
all of `Omega(N,m)`, so the next nontrivial closure must split the connected
full-support macro internally.

> **FULL-SUPPORT ONE-STEP SHELL.**  Let `F_N` be the full-support words joined
> by one original-`K` transition to `U_N`.  Determine whether
> `V_N=U_N union F_N` is proper, compute its exact stationary orientation and
> all boundary flow, and either prove inverse-polynomial conductance or exhibit
> a superpolynomial obstruction.

This is no longer a support-component/color-interleaving cut.
