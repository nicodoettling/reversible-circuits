# Cycle 06 M24 report: fixed balanced component separators rejected

## 1. Exact claim, quantifiers, and convention

Permutations satisfy `(pq)(x)=p(q(x))`; words evaluate as `t_1...t_m`.
The global target `pi` is uniform on

```text
Omega(N,m)={w in T_N^m:t_1...t_m=id},
```

and the exact chain is

```text
K=(1/2)I
 +(1/(2|R_m|)) sum_(r in R_m)
   (1/(m-r+1)) sum_(i=1)^(m-r+1)H_(i,r),
R_m={r in {3,4,5}:r<=m}.                              (1.1)
```

Fix a nontrivial labeled bipartition `[N]=S disjoint union S^c`, put

```text
a=|S|,  b=N-a,
L=binom(a,2)+binom(b,2),

A_S={w in Omega(N,m):no factor crosses (S,S^c)}.      (1.2)
```

For `N>=3`, `L>0`.  The proved general theorem is:

> **Fixed-separator anti-bottleneck.**  For every `N>=3`, every even
> `m>=4`, and every nontrivial `S`, both sides of `A_S` are nonempty and
>
> ```text
> Phi_pm^K(A_S)
> :=Q_K(A_S,A_S^c)/min{pi(A_S),pi(A_S^c)}
> >=ab/[6L(m-2)D_N],
> D_N=(3N^2+N-12)/2.                                  (1.3)
> ```

For a balanced split `a=floor(N/2)`, `b=ceil(N/2)`,

```text
Phi_pm^K(A_S)
 >=1/[6(m-2)D_N]
 >=1/(12mN^2).                                       (1.4)
```

Thus every fixed balanced support-component separator has polynomial
full-`K` escape at every allowed length, including the complete low/base
regime below `2+B_*N log(N+1)`.  For `N>=4`, both sides contain at least two
labels, so the argument is genuinely different from refreshing a single
isolated label.  This theorem does not control the union over separators
and is not a terminal outcome.

## 2. Full proof

### 2.1 Exact global stationary mass and orientation

Let

```text
Z_(d,j)=|Omega(d,j)|,
```

with `Z_(d,0)=1`; for positive `j`, take `Z_(0,j)=Z_(1,j)=0`.  Define

```text
Z_(a|b,m)
 =sum_(j=0)^m binom(m,j)Z_(a,j)Z_(b,m-j).             (2.1)
```

To obtain a word in `A_S`, choose the `j` positions colored by `S`, choose
an identity word on `S` in their inherited order, and choose an identity
word on `S^c` in the other positions.  Conversely, factors in the two
disjoint subgroups commute, so a word with no crossing edge has global
product identity exactly when both colored subwords do.  Hence (2.1) is an
exact bijective count, including every nontrivial color interleaving.

Therefore

```text
pi(A_S)=Z_(a|b,m)/Z_(N,m),                            (2.2)

min{pi(A_S),pi(A_S^c)}
 =min{Z_(a|b,m),Z_(N,m)-Z_(a|b,m)}/Z_(N,m).           (2.3)
```

No mass asymptotic or orientation guess is used.  Because `L>0`, repeating
one internal edge `m` times gives a state in `A_S`; repeating one crossing
edge gives a state in `A_S^c`.  Both products are identity because `m` is
even.

### 2.2 Even return monotonicity for the internal product walk

Let `H=S_a x S_b`, with trivial factors allowed when `a=1` or `b=1`.
Choose uniformly from the `L` internal transpositions and multiply on one
side.  Its Markov operator `P_H` is real symmetric.  If

```text
p_H(j)=P_H^j(id,id),
```

the spectral theorem gives

```text
p_H(j)=sum_theta w_theta lambda_theta^j,
w_theta>=0,  sum_theta w_theta=1,
-1<=lambda_theta<=1.                                 (2.4)
```

For even `m`, each summand in (2.4) satisfies
`lambda_theta^(m-2)>=lambda_theta^m`.  Thus

```text
p_H(m-2)>=p_H(m).                                    (2.5)
```

The walk may be periodic; (2.5) is precisely parity-aware and requires no
aperiodicity or mixing theorem.  Its word count is

```text
Z_(a|b,j)=L^j p_H(j).                                (2.6)
```

### 2.3 Exact adjacent-square incidence

For `w in A_S`, let

```text
Y(w)=#{i in {1,...,m-1}:t_i=t_(i+1)}.
```

Deleting a marked adjacent square is a bijection with:

1. a word counted by `Z_(a|b,m-2)`;
2. one of the `L` internal transpositions; and
3. one of the `m-1` insertion gaps.

The marked position makes the map injective even when several adjacent
squares overlap.  Under the exact conditional law `pi(.|A_S)`,

```text
E[Y]=(m-1)L Z_(a|b,m-2)/Z_(a|b,m).                   (2.7)
```

Since `Y<=m-1`, equations (2.5)--(2.7) imply

```text
Pr(Y>=1)
 >=L Z_(a|b,m-2)/Z_(a|b,m)
 =[1/L]p_H(m-2)/p_H(m)
 >=1/L.                                              (2.8)
```

This is uniform in component sizes, surplus, and density.

### 2.4 Boundary-safe H3 crossing refresh

On a state with `Y>=1`, select the first adjacent square `e,e`.  If it is
not the final pair, use the length-three window beginning at it; if it is
final, use the window ending at position `m`.  With padding transposition
`c`, specify respectively

```text
(e,e,c)->(f,f,c),       (c,e,e)->(c,f,f),             (2.9)
```

where `f` is any edge crossing `(S,S^c)`.  Both ordered block products are
`c`.  There are exactly `ab` distinct choices of `f`, and every output lies
in `A_S^c`.

For a transposition product, the exact length-three conditional fiber has
size

```text
D_N=M+3[2(N-2)]+2binom(N-2,2)
   =(3N^2+N-12)/2,    M=binom(N,2).                   (2.10)
```

Indeed, choose the third transposition.  The first two must factor the
identity, a 3-cycle, or a double transposition, which have respectively
`M`, three, or two ordered transposition factorizations.

The exact kernel selects the nontrivial branch and block size with factor
`1/[2|R_m|]`, the chosen window with probability `1/(m-2)`, and one of the
`D_N` triples uniformly.  Therefore every certified state satisfies

```text
K(w,A_S^c)
 >=ab/[2|R_m|(m-2)D_N]
 >=ab/[6(m-2)D_N].                                   (2.11)
```

The second inequality is conservative at `m=4`, where `|R_m|=2`.

### 2.5 Full r=3,4,5 boundary flow and two-sided conductance

For every available `r`, define

```text
Q_r(A_S,A_S^c)
 =pi(A_S)/[2|R_m|(m-r+1)]
   E_(w|A_S)[sum_(i=1)^(m-r+1)H_(i,r)(w,A_S^c)].     (2.12)
```

Laziness contributes zero and

```text
Q_K(A_S,A_S^c)=sum_(r in R_m)Q_r(A_S,A_S^c).         (2.13)
```

All terms are nonnegative.  Combining the certified `r=3` subflow
(2.8)--(2.11) gives

```text
Q_K(A_S,A_S^c)
 >=pi(A_S)ab/[6L(m-2)D_N].                           (2.14)
```

The complete `r=4,5` flow remains in (2.13) and can only increase this
quantity.  Reversibility makes (2.14) the common boundary flow in either
orientation.  Divide by the exact smaller-side mass (2.3), which is at most
`pi(A_S)`, and obtain (1.3).

For `a=floor(N/2)` and `b=ceil(N/2)`,

```text
2(ab-L)=N-(a-b)^2>0,                                 (2.15)
```

so `ab/L>=1`.  Finally `D_N<=2N^2` and `m-2<=m` give (1.4).

## 3. Worst probability, runtime, path, and congestion accounting

- Under `pi(.|A_S)`, an adjacent square occurs with probability at least
  `1/L`.
- Conditional on certification, the summed specified exit probability is
  at least `ab/[6(m-2)D_N]`.
- Every witness is one transition of the original chain.  There is no
  comparison path and no congestion factor.
- Scanning for the first square takes `O(m)` time.  Listing all `ab<=M`
  crossing outcomes and evaluating `D_N` takes `O(N^2)` arithmetic work.
  Exact local sampling has polynomial cost in `N,m`.
- The exact stationary mass includes all `binom(m,j)` color interleavings;
  no graph-only quotient is substituted for the ordered word.

## 4. Dependencies with status

- **PROVED HERE:** exact mass and orientation, the product-walk spectral
  monotonicity, marked-square incidence, boundary-safe refresh, exact
  `D_N`, full stationary flow, and the balanced simplification.
- **INHERITED PROVED:** heat-bath reversibility/stationarity and polynomial
  implementation of the exact local fibers.
- **CITED DEPENDENCIES:** none.
- **NOT USED:** dense bridge smoothing, isolated-label conductance,
  component-count unimodality, fixed-genus asymptotics, Hurwitz mixing,
  finite spectra, or a canonical hub.
- **EMPIRICAL/COMPUTATIONAL DEPENDENCIES:** none.

## 5. First unproved standalone proposition

> **BALANCED-SEPARATOR UNION CONDUCTANCE.**  Let
>
> ```text
> B_(N,m)=union_(|S|=floor(N/2)) A_S.
> ```
>
> Prove universal constants `c>0,C<infinity` such that every nontrivial
> `B_(N,m)` satisfies
>
> ```text
> Q_K(B_(N,m),B_(N,m)^c)
> /min{pi(B_(N,m)),pi(B_(N,m)^c)}>=c(Nm)^(-C),
> ```
>
> or construct an explicit infinite family with superpolynomially small
> full-`K` conductance, including exact mass and all `r=3,4,5` flow.

The related stronger profile cut `max component size<=N/2` is also open.

## 6. Strongest self-attack and Terminal-B audit

The event `A_S` allows the actual support partition to refine the fixed
separator; it is not the event of exactly two connected components.  This
generality is what makes the product-walk return identity exact.  A word
with many components can belong to exponentially many balanced-separator
events.  After (2.9) leaves one `A_S`, it can remain in another, so neither
stationary masses nor boundary flows can be union-bounded from (1.3).

Consequently, this theorem rejects all fixed balanced separators but not
their union, the largest-component threshold, or internal full-support
cuts.  No superpolynomial family survived; Terminal B is not claimed.

## 7. Calibration

- Odd `m` gives an empty bridge; `m=0` is singleton; `N=2` at even length is
  singleton; and `m=2,N>=3` is the excluded disconnected local chain.  The
  theorem starts at even `m=4,N>=3`.
- At `S_3,m=4`, the balanced split is `1+2`, so `L=1` and
  `Z_(1|2,4)=1`; hence `pi(A_S)=1/27`.  This small case degenerates to an
  isolated side, while the theorem is non-isolated for `N>=4`.
- At `S_4,m=4`, a fixed `2+2` split has two commuting internal edges.  The
  identity words are the eight binary color words having even counts, so
  `pi(A_S)=8/120=1/15`.
- At `S_4,m=6`, the same count is `2^5=32`, hence
  `pi(A_S)=32/3936=1/123`.
- The `27/120/3936` total counts and their `4/13/17` pure-Hurwitz components
  are respected, but no pure-Hurwitz transition is used.
- At `m=4`, `R_m={3,4}` and `H_(1,4)` is a whole-word heat bath.  It remains
  explicitly present in (2.12)--(2.13); using `|R_m|<=3` only weakens the
  certified `H_3` rate.
- Near-minimal doubled-tree words can cross the separator or lie on one
  side; (2.8) averages over the exact fixed-separator bridge and makes no
  typical-tree assumption.  Disjoint-component color order is retained by
  the binomial interleaving in (2.1).
- No edge/degree parity characterization, failed length-two simulation,
  graph-only edge shift, or fixed canonical hub enters the proof.

## 8. Artifacts and reproduction commands

Owned artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M24-balanced-component-redteam/plan.md
experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M24-balanced-component-redteam/checkpoint.md
experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M24-balanced-component-redteam/report.md
```

No computation was used.  Reproduction consists of checking the exact
interleaving bijection (2.1), finite symmetric-operator identity (2.4),
marked-square deletion, fiber count (2.10), and full flow (2.12)--(2.14).
Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED

This verdict applies to the fixed-separator theorem (1.3)--(1.4), not to
either global terminal outcome.
