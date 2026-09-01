# M22 halfway checkpoint: the desert has a polynomial color boundary

## Status

The natural infinite thickening of the M04 fixed-color obstruction is
rigorously rejected as a full-`K` bottleneck.  The calculation is global, not
conditional on the rare-component macro.

Use `(pq)(x)=p(q(x))`, `M=binom(N,2)`, and

```text
K = (1/2)I
  + (1/6) sum_{r=3}^5 1/(m-r+1) sum_i H_{i,r}
```

in the family below (`m>=6`, so all three block lengths occur).

## Candidate family and exact mass

Fix `N>=5`, put `L=N^3` and `m=4(L+1)`.  For a three-element set `S`, let
the factors on `S` form a connected identity word of the minimal length four,
and let the factors on `S^c` form a connected identity word of length `4L`.
Call the former color `A` and the latter color `B`.  Let `D_{N}` be the set of
all such global identity words for which at least `L` copies of `B` lie between
each consecutive pair of the four copies of `A`.  Endpoint `B`-runs are
unconstrained.  This includes the rigid word `(A B^L)^4`.

Write `C_v(k)` for the number of connected-support identity transposition
words of length `k` on one fixed labeled `v`-set.  There are
`C_3(4)=27-3=24` rare internal words.  If the endpoint gaps are `b_0,b_4>=0`
and the three internal gaps are `b_i=L+c_i`, then

```text
b_0+b_4+c_1+c_2+c_3=L.
```

Hence the number of desert color words is `binom(L+4,4)` and the exact global
cardinality is

```text
|D_N| = binom(N,3) 24 C_{N-3}(4L) binom(L+4,4).       (C.1)
```

There is no overcount at `N=6`: the component of weight four is distinguished
from the component of weight `4L`.

For even `m`, Cauchy--Schwarz for the `m/2`-step random-transposition law on
its parity coset gives

```text
|Omega(N,m)| >= 2 M^m/N!.                             (C.2)
```

Indeed `P^m(e,e)=sum_g P^{m/2}(e,g)^2>=2/N!`.  Put
`M_B=binom(N-3,2)`.  From `C_{N-3}(4L)<=M_B^{4L}` and
`24 binom(L+4,4)<=m^4`, (C.1)--(C.2) give

```text
pi(D_N)
 <= [N! N^3 m^4/(2M^4)] (M_B/M)^{4L}
 <= (1/2) exp(-15N^2) < 1/2.                          (C.3)
```

For the last estimate,

```text
1-M_B/M = 6(N-2)/[N(N-1)] >= 9/(2N),
4L(1-M_B/M)>=18N^2,
m<=8N^3,
N!<=N^N,
(N+15)log N+12log 2 <=3N^2       (N>=5).
```

Thus the orientation is proved against the *global* stationary law.

## Exact boundary layer and actual full-K exit

The subfamily with the first internal gap tight, `c_1=0`, has
`binom(L+3,3)` color words.  Since every color word supports the same number
of internal tuples and label choices, its exact fraction inside `D_N` is

```text
binom(L+3,3)/binom(L+4,4)=4/(L+4).                    (C.4)
```

Take a state in this boundary layer and write the first three factors from
the first tight gap as `(a,b,c)`, where `a` has color `A` and `b,c` have
color `B`.  The supports are disjoint, so `ab=ba` and

```text
abc=bac.                                               (C.5)
```

The exact `H_3` heat bath can therefore output `(b,a,c)`.  This preserves the
labeled weighted component macro and both within-color subsequences, but it
leaves only `L-1` copies of `B` between the first two `A` factors, so it exits
`D_N`.  Every length-three product fiber has size at most `M^2`, hence the
specified outcome has full-chain probability at least

```text
q = 1/[6(m-2)M^2].                                    (C.6)
```

Combining (C.3)--(C.6), with
`Phi_K(A)=Q_K(A,A^c)/pi(A)` for this oriented set, gives

```text
Phi_K(D_N)
 >= 2/[3(L+4)(m-2)M^2]
 >= 4/(15N^10).                                       (C.7)
```

The rigid exact pattern `(A B^L)^4` is even less viable: every one of its
states admits the first-boundary swap, so its conductance is at least

```text
1/[6(m-2)M^2] >= 2/(15N^7).                           (C.8)
```

This also proves a more general color-thickening statement.  For any fixed
macro with four rare factors and any feasible separation threshold `h>=1`,
the fraction of threshold color words with first gap exactly `h` is
`4/(m-3h)`.  Moving the threshold outward merely moves a boundary layer; it
does not make its relative size superpolynomially small.

## Accounting for all block sizes and macro changes

The boundary flow has the exact nonnegative decomposition

```text
Q_K(D_N,D_N^c)
 = Q_{3,swap}+Q_{3,other}+Q_{4,other}+Q_{5,other}.      (C.9)
```

Equation (C.7) keeps only `Q_{3,swap}`.  Every omitted outcome, including
every component merge or split, increases the flow.  Thus this is valid for
the original full `Q_3+Q_4+Q_5` kernel; omitting these terms would be invalid
for a bottleneck upper bound, but is conservative for the rejection lower
bound.

The deterministic exact harness exhausts every conditional outcome from the
representative `N=5,m=24,L=5` word.  Its update-part probabilities (each
already includes the relevant `1/6` block-size/laziness coefficient) are:

| block | macro-changing exit | target-macro non-desert exit | stays |
|---|---:|---:|---:|
| 3 | 0.1573083779 | 0.0037878788 | 0.0055704100 |
| 4 | 0.1640233871 | 0.0015589569 | 0.0010843226 |
| 5 | 0.1663310962 | 0.0002157239 | 0.0001198466 |

The total one-step exit probability is exactly
`1454531591/2949019920 = 0.4932254208`.  In particular, the finite source of
the exact-color restriction obstruction has enormous full-chain
macro-changing flow.  This finite computation is falsification-only; (C.7)
is the universal proof for the named infinite family.

## Current first gap

The standalone unresolved proposition after rejecting this cut is:

> **RARE-MACRO-CLOSURE.** Determine the globally oriented conductance of a set
> which contains the entire rare-component macro and enough adjacent
> merge/split macros that no same-macro color swap leaves it.

That is a genuinely different set from the M04 exact-color obstruction and
from the desert threshold treated here.
