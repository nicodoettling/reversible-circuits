# Cycle 05 M18 final report: bounded-surplus component phase

## 1. Exact quantified claim and convention

Permutations are maps on `[N]`, composition means `(pq)(x)=p(q(x))`, and a
word evaluates as `t_1...t_m`. Put `M=binom(N,2)`. The target is the global
uniform law `pi` on

```text
Omega(N,m)={w in T_N^m:t_1...t_m=id},
```

and the kernel is exactly

```text
K=(1/2)I
 +(1/(2|R_m|)) sum_(r in R_m)
    (1/(m-r+1)) sum_(i=1)^(m-r+1) H_(i,r),
R_m={r in {3,4,5}:r<=m}.
```

For `g>=1`, set `m=2(N-1)+2g` and define

```text
F_(N,g)={w in Omega(N,m):the support graph is connected on all [N]}.
```

At this length `F_(N,g)` is exactly the bottom component-count layer `c=1`
and has total surplus `G=m/2-N+c=g`. The following original-`K` theorem is
proved.

> **Bounded-surplus bottom-layer anti-bottleneck.** For every integer `g>=1`
> and every `N>=max(4,g+1)`, `F_(N,g)` is nonempty and proper and
>
> ```text
> Phi_pm^K(F_(N,g))
> :=Q_K(F_(N,g),F_(N,g)^c)
>   /min{pi(F_(N,g)),pi(F_(N,g)^c)}
> >=(3/4)^g/[192 N^(5g+6)].                            (1.1)
> ```

Consequently, for every fixed `g_0`, all `1<=g<=g_0` have one common
inverse-polynomial bound in `N`. In the first case not covered by the earlier
`G<=1` sparse result, the constants sharpen to

```text
Phi_pm^K(F_(N,2))>=1/(27N^16),   N>=4.                 (1.2)
```

For `N>=g+1`, these lengths satisfy

```text
2(N-1)<m<=4N-4<2+4M log(2N),
```

so they lie in the assigned intermediate window. This rigorously rejects the
bounded-surplus connected-versus-disconnected phase family. It is scoped and
nonterminal: no Terminal-B family and no universal gap theorem is proved.

The exact stationary mass, included to account for the global rather than
macro-conditional target, is

```text
pi(F_(N,g))
 =C_g(N)/Z_(N,m),
Z_(N,m)
 =(1/N!) sum_(lambda partition N)(f^lambda)^2 c_lambda^m,              (1.3)
```

where `C_g(N)` is the connected exact-support count, `f^lambda` is the
irreducible dimension, and `c_lambda` is the Young-diagram content sum. No
orientation or asymptotic estimate for (1.3) is assumed.

## 2. Full proof

### 2.1 A cross-degree count bound from DYZ

Let `C_g(d)` denote the number of connected exact-support identity
transposition words on a fixed labeled `d`-set, with length

```text
k_(g,d)=2d-2+2g,
```

and normalize

```text
a_(g,d)=C_g(d)/k_(g,d)!.
```

The inherited proved consequence of the positive Dubrovin--Yang--Zagier
recurrence is, for every `d>=2` and `j>=1`,

```text
a_(j,d)/a_(j-1,d)<=d^3/12.                             (2.1)
```

Iteration gives

```text
a_(g,d)<=(d^3/12)^g a_(0,d).                           (2.2)
```

There is also an elementary lower bound in the opposite dimension. On any
fixed labeled `d`-set choose one fixed transposition `e`. For every connected
genus-zero word `w`,

```text
w -> (e,e)^g w                                          (2.3)
```

is an injective map to connected genus-`g` words: every adjacent pair has
ordered product identity, the suffix recovers `w`, and the support of `w`
already connects all `d` labels. Hence

```text
C_g(d)>=C_0(d).                                         (2.4)
```

The exact minimal connected count is

```text
C_0(d)=(2d-2)!d^(d-3).                                  (2.5)
```

Applying (2.2) at degree `N`, (2.4) at degree `N-1`, and then (2.5) gives

```text
C_g(N-1)/C_g(N)
 >=[12^g/N^(3g)] [C_0(N-1)/C_0(N)]
   /product_(j=1)^(2g)(2N-2+j),                         (2.6)

C_0(N-1)/C_0(N)
 =(1-1/N)^(N-4)/[N(2N-2)(2N-3)].                       (2.7)
```

For `N>=4`, `log(1-1/N)>=-1/(N-1)` implies
`(1-1/N)^(N-4)>=e^-1>1/4`. Thus

```text
C_0(N-1)/C_0(N)>=1/(16N^3).                            (2.8)
```

If `N>=g+1`, then

```text
2N-2+j<=4N,   1<=j<=2g.
```

Substitution in (2.6) yields the explicit cross-degree estimate

```text
C_g(N-1)/C_g(N)
 >=(3/4)^g/[16N^(5g+3)].                               (2.9)
```

This is polynomial for fixed `g`; no uniform-in-`g` conclusion is being
drawn.

### 2.2 Exact marked-incidence identity

For `w in F_(N,g)`, a **mark** is an adjacent pair

```text
t_i=t_(i+1)=(uv)
```

together with a distinguished endpoint `v`, such that `v` occurs in no other
factor and deletion of the pair leaves a connected exact-support genus-`g`
word on `[N] minus {v}`.

Deletion is a bijection between marked incidences and the following data:

1. the omitted label `v`, in `N` ways;
2. its neighbor `u`, in `N-1` ways;
3. a word counted by `C_g(N-1)` on the fixed remaining label set;
4. one of the `m-1` gaps in that length-`m-2` word.

Indeed, insertion of `(uv),(uv)` in the designated gap preserves the product,
adds `v` as a leaf, and produces a connected full-support word; deletion
recovers all data. If `Z(w)` is the number of marks, uniformity conditional
on `F_(N,g)` therefore gives the exact identity

```text
E_F Z
 =N(N-1)(m-1) C_g(N-1)/C_g(N).                        (2.10)
```

Since `N-1>=N/2` and `m-1>=N`, (2.9)--(2.10) imply

```text
E_F Z>=(3/4)^g/[32N^(5g)].                             (2.11)
```

A fixed omitted label can determine at most one mark, since its only two
occurrences are the displayed adjacent pair. Hence `Z<=N`, and no
independence assumption is required to conclude

```text
Pr_F[Z>=1]>=(3/4)^g/[32N^(5g+1)].                      (2.12)
```

### 2.3 A boundary-safe full-`K` exit

Choose one mark deterministically whenever `Z>=1`, and write its edge as
`e=(uv)`. Choose any transposition `f` on `[N] minus {v}`. Such an `f` exists
because `N>=4`.

If the marked pair is not the final adjacent pair, use the `H_3` window
beginning at it and specify the outcome

```text
(e,e,a)->(f,f,a).
```

If it is the final pair, use the `H_3` window ending at `m` and specify

```text
(a,e,e)->(a,f,f).
```

In either orientation the ordered block product is unchanged because
`e^2=f^2=id`. The unchanged base word connects every label other than `v`,
and the output contains no `v`, so the output is in `F_(N,g)^c`.

For a fixed product of three transpositions, choosing the first two factors
determines the third group element uniquely. Hence every relevant
same-product `H_3` fiber has size at most `M^2`. Since `m>=8`,
`|R_m|=3`, and the exact probability of the specified output is at least

```text
q_(N,g)=1/[2*3*(m-2)M^2].                              (2.13)
```

The four displayed factors are, respectively, the nontrivial outer mass,
block-size scan, window scan, and conditional heat-bath output. There is no
extra transposition-choice factor. Because `N>=g+1`, `m-2<4N`; because
`M<=N^2/2`,

```text
q_(N,g)>=1/(6N^5).                                     (2.14)
```

All `r=4,5` transitions give additional nonnegative boundary flow.

### 2.4 Global stationary flow and mass orientation

Combining (2.12)--(2.14), under the true global uniform law,

```text
Q_K(F_(N,g),F_(N,g)^c)
 =pi(F_(N,g)) E_F[K(w,F_(N,g)^c)]
 >=pi(F_(N,g))(3/4)^g/[192N^(5g+6)].                  (2.15)
```

The cut is nonempty by (2.3)--(2.5). It is proper because, for example, the
identity word consisting only of repeated copies of one transposition lies
outside it. Finally,

```text
min{pi(F_(N,g)),pi(F_(N,g)^c)}<=pi(F_(N,g)).            (2.16)
```

Thus (2.15) divided by (2.16) proves (1.1), without guessing which side is
smaller and without using component-layer unimodality.

### 2.5 Sharpening at `g=2`

For `g=2`, the four factorial-ratio factors in (2.6) are each at most `3N`,
so (2.8) gives

```text
C_2(N-1)/C_2(N)>=1/(9N^13).                            (2.17)
```

Here `m=2N+2`, and
`N(N-1)(m-1)=N(N-1)(2N+1)>=N^3`. Therefore

```text
Pr_F[Z>=1]>=1/(9N^11).                                 (2.18)
```

Also `m-2=2N`, so (2.13) and `M<=N^2/2` give
`q_(N,2)>=1/(3N^5)`. Their product is (1.2).

## 3. Worst-case probability, runtime, path, and congestion accounting

- Certified-state probability under `pi(.|F_(N,g))` is at least
  `(3/4)^g/[32N^(5g+1)]`; for `g=2` it is at least `1/(9N^11)`.
- From each certified state, one specified legal original-`K` transition
  exits with probability at least `1/[6(m-2)M^2]`, and hence at least
  `1/(6N^5)` under the theorem's parameter bounds. For `g=2` the sharper
  value is `1/(3N^5)`.
- Every exit has path length one. There is no comparison flow and no
  congestion quantity to hide.
- Selecting a recorded mark is `O(m)` after scanning occurrences. The exact
  `H_3` sampler can enumerate at most `M^2=O(N^4)` candidate prefixes, so
  this local witness and the inherited implementation have polynomial cost
  in `N,m`.
- This is an averaged conductance calculation for one exact global cut, not
  a worst-state mixing bound and not a sampler runtime theorem.

## 4. Dependencies, with status labels

- **Proved here:** the square-prefix injection (2.3), cross-degree bound
  (2.9), exact marked-incidence identity (2.10), certified-mass estimate
  (2.12), boundary-safe `H_3` exit, global flow (2.15), mass-orientation
  step (2.16), and the `g=2` sharpening.
- **Inherited proved:** the adjacent-genus bound (2.1), including its
  convolution-ratio proof from the positive DYZ recurrence; the minimal
  connected count (2.5); exact heat-bath reversibility; and the polynomial
  exact block implementation.
- **Cited and hypothesis-checked in the inherited proof:** Dubrovin--Yang--
  Zagier, *Classical Hurwitz numbers and related combinatorics*, Proposition
  1, equation (13). Its normalization differs from the labeled
  factorization count by a degree-dependent but genus-independent factor and
  therefore leaves (2.1) unchanged.
- **Proved/inherited representation identity:** the exact stationary-mass
  formula (1.3), from the regular trace of the central transposition sum.
- **Not used:** universal `W_c` unimodality, finite unimodality, a pendant
  ratio uniform in genus, a normal quotient, a Hurwitz-only gap, or any
  canonical hub.
- **Empirical dependencies:** none.

## 5. First standalone unproved proposition

> **LOWEST-LAYER INTERMEDIATE CONDUCTANCE.** There are universal constants
> `c>0,C<infinity` such that for every `N>=3` and every even
> `m` with
>
> ```text
> 2(N-1)<m<2+4 binom(N,2)log(2N),
> ```
>
> the connected full-support bottom layer `F={c=1}` satisfies
>
> ```text
> Q_K(F,F^c)/min{pi(F),pi(F^c)}>=c(Nm)^(-C).
> ```

The present theorem proves this when the surplus
`g=m/2-(N-1)` is bounded, with an exponent depending on that bound. A proof
for growing `g` needs a boundary certificate broader than pendant adjacent
squares, or an exact comparison of the smaller-side mass with the full
support-partition boundary flow.

## 6. Strongest self-attack

The exponent in (1.1) is `5g+6`, so the theorem gives no universal inverse
polynomial when `g` grows with `N`. This is not merely a loose technical
concern: at fixed degree and large genus the pendant-square ratio
`N(N-1)C_g(N-1)/C_g(N)` is exponentially small in `g`. Thus the marked
subclass used here cannot support a uniform all-genus proof. When the
connected phase has large stationary mass, the smaller denominator may be
the disconnected complement, and a reverse-flow or exact partition-mass
argument could still be polynomial; this report does not supply it.

Even the standalone proposition in field 5 would reject only the lowest
component threshold. Arbitrary component-size profiles, cuts inside a fixed
macro, and the global spectral gap would remain open. No aspect of this
result is Terminal A or Terminal B.

## 7. Calibration suite

- Odd `m`: `Omega(N,m)` is empty; the theorem uses even
  `m=2(N-1)+2g`.
- `m=0` and `N=2`: singleton regimes are outside the theorem.
- `m=2,N>=3`: the excluded disconnected-chain case is outside the theorem.
- `S_3,m=4`: the 27 words and 4 Hurwitz components are not used; the
  theorem begins at `N>=4,m>=8`.
- `S_4,m=4`: the 120 words and 13 Hurwitz components are outside scope.
- `S_4,m=6`: the 3936 words and 17 Hurwitz components are outside scope.
- At `m=4`, `H_4` is the whole-word heat bath. It remains present in the
  exact kernel definition; no theorem step drops it. The proved family has
  `m>=8` and uses a positive `H_3` subflow while retaining all other terms.
- Near-minimal doubled-tree words are `g=0`; they calibrate (2.5) and the
  earlier minimal-macro theorem. This report begins at `g=1` and includes
  the first previously untreated bounded-surplus case `g=2`.
- The cut has one support component, so there is no color interleaving to
  quotient out. All disconnected interleavings remain in the exact global
  complement and denominator (1.3).
- No edge-parity or vertex-degree-parity characterization of identity words
  is used. Identity follows from exact word products and cancelling squares.
- The move is length three and does not contradict the failed general
  length-two local simulation claim.
- No canonical normal form or tiny hub is used; the certificate is counted
  over all base words, omitted labels, neighbors, and gaps.
- Stationary mass is accounted for exactly by (1.3), and the two-sided
  denominator is handled by (2.16), not by an unsupported assumption that
  `F_(N,g)` is the smaller side.

## 8. Artifacts and reproduction commands

Artifacts in this owned directory are:

```text
plan.md
checkpoint.md
report.md
```

Repository commit at the time of the proof audit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

No finite experiment was used. The proof can be inspected with:

```bash
sed -n '1,460p' report.md
```

The universal claim is algebraic; finite enumeration could check constants
but would not prove it and was therefore not presented as evidence.

## 9. Verdict

PROVED

The verdict applies to the scoped bounded-surplus bottom-layer
anti-bottleneck theorem (1.1), not to either terminal outcome. The growing-
surplus intermediate component phase remains open at the standalone
proposition in field 5.
