# A rigorous dense-genus curvature bound

## Statement

For `v>=3` put `M=binom(v,2)`.  Let `C_v(k)` be the number of
length-`k` transposition words on the fixed labeled vertex set `[v]` whose
ordered product is the identity and whose support graph is connected.  The
permutation convention is `(pq)(x)=p(q(x))`; the count below is insensitive
to reversing this convention.  Put

```text
a_v(g)=C_v(k)/k!,       k=2(v-1)+2g,
rho_v(0)=0,             rho_v(g)=a_v(g-1)/a_v(g)  (g>=1).
```

The following is proved here.

> **DENSE-HURWITZ-RATE-CURVATURE.**  Let `v>=3`, `g>=1`, and
> `k=2(v-1)+2g`.  If
>
> ```text
> k-2 >= 4 M log(2v),
> ```
>
> then
>
> ```text
> rho_v(g+1)-rho_v(g) >= (2k-2/k)/M^2 >= k/M^2 > 0.       (1)
> ```

For `v=2`, `C_2(k)=1` for every positive even `k`.  Thus
`rho_2(1)-rho_2(0)=12`, while for `g>=1`, with
`k=2+2g`, `rho_2(g)=k(k-1)` and
`rho_2(g+1)-rho_2(g)=4k+2`.  Thus the only range not covered by (1) or this
explicit calculation is

```text
v>=3,  0<=g,  and  2(v-1)+2g-2 < 4 binom(v,2) log(2v).    (2)
```

The lower bound (1) is much stronger than the requested inverse polynomial
inside its range.  It does **not** settle the uniform curvature proposition,
because (2) contains infinitely many pairs `(v,g)`.

## Proof

Let `Z_v(j)` be the number of all (not necessarily connected-support)
length-`j` transposition words on `[v]` with identity product.  The regular
character formula for the central sum of all transpositions gives, for even
`j`,

```text
Z_v(j) = (1/v!) sum_{lambda partition v} (f^lambda)^2 nu_lambda^j,          (3)
```

where `f^lambda` is the irreducible dimension and `nu_lambda` is the sum of
the contents of `lambda`.  The trivial and sign representations have central
characters `M` and `-M`.  Every other partition satisfies

```text
|nu_lambda| <= M-v.                                                         (4)
```

For completeness, (4) follows by conjugation and dominance: content sum is
strictly increased by moving a box upward in dominance order, so the largest
partition below `(v)` is `(v-1,1)`, whose content sum is `M-v`; conjugation
negates contents.  Also `sum_lambda (f^lambda)^2=v!`.  Hence

```text
Z_v(j) = (2 M^j/v!) (1+u_j),
0 <= u_j <= (v!/2) exp(-j v/M).                                             (5)
```

Let `D_v(j)=Z_v(j)-C_v(j)`.  A disconnected support graph has a nonempty
proper vertex set `A`, of size `q`, across whose cut no transposition occurs.
There are `M-q(v-q)` allowed internal transpositions.  Dropping even the
identity-product requirement and union-bounding over cuts gives

```text
D_v(j) <= sum_{q=1}^{v-1} binom(v,q) [M-q(v-q)]^j
       <= 2^v M^j exp(-j(v-1)/M).                                           (6)
```

Combining (5)--(6), write

```text
C_v(j) = (2 M^j/v!) (1+e_j),
|e_j| <= E_j := (v!/2) exp(-jv/M)
                   + v! 2^(v-1) exp(-j(v-1)/M).                             (7)
```

Suppose `j>=4M log(2v)`.  Since `v!<=v^v`,

```text
E_j < (2v)^(-3v+4).                                                         (8)
```

Both summands in `(j+2)E_j` decrease once `j+2>=M/(v-1)=v/2`.
At the threshold in (8), use

```text
4M log(2v)+2 <= (2v)^3   (v>=3)
```

to get

```text
(j+2)E_j <= (2v)^(-3v+7) <= 1/36 < 1/4.                                    (9)
```

Now take `j=k-2`.  The sequence `E_j` decreases, so (9) implies that all
three errors `e_{k-2},e_k,e_{k+2}` have absolute value at most

```text
delta:=E_{k-2} <= 1/(4k).                                                    (10)
```

Consequently, for

```text
R_k=(1+e_{k-2})/(1+e_k),     R_{k+2}=(1+e_k)/(1+e_{k+2}),
```

the elementary estimate

```text
|R_k-1|, |R_{k+2}-1| <= 4 delta                                             (11)
```

holds (indeed `2 delta/(1-delta)` is enough).  From the factorial
normalization,

```text
rho_v(g)   = k(k-1) R_k/M^2,
rho_v(g+1) = (k+2)(k+1) R_(k+2)/M^2.                                       (12)
```

Using (10)--(12), the numerator of the difference after multiplication by
`M^2` is at least

```text
(k+2)(k+1)(1-4delta)-k(k-1)(1+4delta)
 >= 4k+2 - [(2k^2+2k+2)/k]
  = 2k-2/k.
```

This proves (1).

## What this estimate does and does not use

The proof is an exact-support estimate: (6) explicitly subtracts words whose
support is disconnected.  It does not infer a bridge statement merely from
the unconditioned random-transposition walk.  It also controls the errors at
three adjacent lengths; a pair of constant-factor return-count estimates
would not preserve the sign of the curvature difference, whose leading
relative scale is only order `1/k`.

The remaining standalone proposition is:

> **LOW-AND-INTERMEDIATE-GENUS CURVATURE.**  There are universal `c>0` and
> `A<infinity` such that for every `v>=3` and every `g>=0` satisfying (2),
> `rho_v(g+1)-rho_v(g) >= c(v+g+1)^(-A)`.

The zero-range theorem needs precisely these increments for every occupancy
index `g>=0`: the departure rate from an empty component is
`rho_v(0)=0`, so the first required increment is
`rho_v(1)-rho_v(0)`, not the formula obtained by differencing two positive
occupancy rates.  The dense theorem supplies the required increments only
for the high-occupancy indices satisfying its displayed threshold.
