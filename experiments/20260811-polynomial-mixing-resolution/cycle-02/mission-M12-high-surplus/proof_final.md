# Final proof: dense total-surplus thresholds are not bottlenecks

This file supersedes the weaker density threshold in `proof.md`.

## 1. Exact theorem and conventions

Permutations are maps on `[N]`; `pq` means `p` after `q`, and words evaluate
as `t_1...t_m`.  Put `M=binom(N,2)`.  The stationary law `pi` is uniform on
`Omega(N,m)`, and

```text
K = (1/2)I
    + (1/(2|R_m|)) sum_{r in R_m} (1/(m-r+1)) sum_i H_{i,r},
R_m={r in {3,4,5}:r<=m}.
```

All logarithms below are natural.

**Theorem 1 (uniform dense-threshold conductance).**  Let `N>=3`, let `m` be
even, and suppose

```text
m-2 >= 4 M log(2N).                                      (1.1)
```

For `1<=c_0<=N-2`, let

```text
A(c_0)={w in Omega(N,m): c(w)<=c_0},
```

where `c(w)` counts all support-graph components, including isolated labels.
Both sides of this cut are nonempty, and

```text
Phi_pm(A(c_0))
 := Q_K(A(c_0),A(c_0)^c)/min{pi(A(c_0)),pi(A(c_0)^c)}
 >= (N-1)/(128 M^2).                                     (1.2)
```

If the nontrivial components have sizes `v_i` and factor counts `k_i`, then

```text
G(w)=sum_i [k_i-2(v_i-1)]/2=m/2-N+c(w).                  (1.3)
```

Thus (1.2) holds for every nontrivial total-surplus threshold `A_{<=g}` in
the regime (1.1), with exponent independent of `g`.  The theorem is a
restricted anti-bottleneck result, not a global gap theorem.

Equation (1.3) follows because, if `s` labels are active in `q` nontrivial
components, then `G=m/2-s+q` and `c=N-s+q`.

## 2. Uniform trace estimate, including every partition and parity mode

Fix a labeled set partition `P` of `[N]` with at least one nontrivial block.
Let its nontrivial block sizes be `n_1,...,n_r`, and put

```text
E(P)=union_i T_{n_i},
e=e(P)=sum_i binom(n_i,2),
H_P=product_i S_{n_i},
h=|H_P|=product_i n_i!.
```

Let `Z_P(k)` count length-`k` identity words using only transpositions in
`E(P)`, allowing their actual support partition to refine `P`.  Let `E_P(k)`
count the words whose exact support partition is `P`.

### Lemma 2.1 (central-walk trace)

For every even `k` such that

```text
t:=k/e >= 4 log(2N),                                     (2.1)
```

one has, uniformly over `P`,

```text
2 e^k/h <= Z_P(k) <= 4 e^k/h.                            (2.2)
```

**Proof.**  In `C[H_P]`, the element `T_P=sum_{s in E(P)}s` is central.  The
regular-representation trace is

```text
Z_P(k)=h^(-1) sum_rho dim(rho)^2 nu_rho^k,                (2.3)
```

where irreducibles are tuples `rho=(lambda_1,...,lambda_r)` and
`nu_rho=sum_i nu_{lambda_i}`.  For `S_n`, the transposition-class sum acts by
the integer content sum of `lambda`.  Its unique maximum and minimum are
`+binom(n,2)` and `-binom(n,2)`, at the trivial and sign representations.
Moreover, for every nontrivial `lambda`,

```text
binom(n,2)-nu_lambda >= n.                               (2.4)
```

Indeed the largest nontrivial content sum occurs at `(n-1,1)` and equals
`binom(n,2)-n`; conjugation gives the lower extreme.  This explicitly
includes `n=2`, whose two eigenvalues are `+1,-1`.

The all-trivial and all-sign tuples give the two terms `+e` and `-e`, proving
the lower bound in (2.2) because `k` is even.  For the upper bound, conjugate
every Young diagram when `nu_rho<0`; dimensions are preserved and `nu`
changes sign.  With

```text
D(rho)=e-nu_rho=sum_i [binom(n_i,2)-nu_{lambda_i}],
```

the inequality `(1-D/e)^k<=exp(-tD)` for `0<=nu<=e` gives

```text
sum_rho dim(rho)^2 |nu_rho/e|^k
 <= 2 product_i S_{n_i}(t),
S_n(t):=sum_{lambda partition n} dim(lambda)^2
                    exp[-t(binom(n,2)-nu_lambda)].        (2.5)
```

By (2.4) and `sum_lambda dim(lambda)^2=n!`,

```text
S_n(t) <= 1+n! exp(-tn)
         <= 1+[N/(2N)^4]^n
         <= 1+(16N^3)^(-n).                              (2.6)
```

There are at most `N/2` nontrivial blocks and every `n_i>=2`, so the product
in (2.5) is less than `2`.  Substitution in (2.3) gives the upper bound in
(2.2).  This argument retains all component-parity modes: mixed choices of
trivial and sign representations occur among the factors in (2.5), rather
than being discarded as an error with multiplicity `N!`.  QED.

The trace identity is the direct-product version of the Frobenius formula;
it is also stated for `S_d` in Dubrovin--Yang--Zagier, equations (19)--(21).

### Lemma 2.2 (exact support within a factor four)

Under (2.1), uniformly over every `P`,

```text
e^k/h <= E_P(k) <= 4 e^k/h.                              (2.7)
```

**Proof.**  The upper bound follows from (2.2).  If a word counted by
`Z_P(k)` fails to have exact partition `P`, some nominal block `B` of size
`n>=2` is disconnected.  Hence there is a nonempty proper cut `A | (B\A)`
with no used edge across it.  If `a=|A|`, refining `P` along this cut changes

```text
e' = e-a(n-a),
h/h'=binom(n,a).
```

The word is counted by `Z_{P'}(k)`.  Lemma 2.1 gives

```text
Z_{P'}(k)/Z_P(k)
 <= 2 binom(n,a) (e'/e)^k
 <= 2 binom(n,a) exp[-t a(n-a)].                         (2.8)
```

If `e'=0`, the numerator is zero for positive `k`, so (2.8) remains valid.
Summing over all subsets (which counts each unordered cut twice and is thus
a safe upper bound) gives, for this block,

```text
2 sum_{a=1}^{n-1} binom(n,a)^2 exp[-t a(n-a)]
 <= 2*4^n exp[-t(n-1)].                                  (2.9)
```

Here `sum_a binom(n,a)^2<=binom(2n,n)<=4^n` and
`a(n-a)>=n-1`.  At `t>=4log(2N)`, the right side of (2.9) is maximized over
`n>=2` at `n=2`, where it is at most `2/N^4`.  There are at most `N/2`
nontrivial blocks, so the full union bound is at most `1/N^3<1/2`.  Therefore
`E_P(k)>=Z_P(k)/2>=e^k/h`, proving (2.7).  This is inclusion--exclusion only
in the safe first Bonferroni direction; no cancellation or asymptotic
uniformity is assumed.  QED.

Condition (1.1) implies (2.1) for both `k=m-2` and `k=m`, since `e<=M`.
Thus (2.7) is available at both lengths needed below, including partitions
with size-two blocks and isolated labels.

## 3. Exact component-layer mass and its smaller-side orientation

Let

```text
W_c(k)=sum_{P:|P|=c, e(P)>=1} E_P(k),       1<=c<=N-1.    (3.1)
```

This is exactly the number of words with `c` support components; the sum
runs over labeled exact partitions, so disjoint-component color
interleavings are already counted, not suppressed.

### Lemma 3.1 (geometric layer tail)

For `1<=c<=N-2`,

```text
W_{c+1}(m) <= q_N W_c(m),
q_N:=4/N^4 <= 1/4.                                       (3.2)
```

**Proof.**  Order the blocks of `P` by smallest label and merge its first two
blocks.  Call the resulting partition `F(P)`.  If the merged block sizes are
`a,b`, then, with `e'=e(F(P))=e(P)+ab`, Lemma 2.2 gives

```text
E_P(m)/E_{F(P)}(m)
 <=4 binom(a+b,a) exp[-(m/e')ab]
 <=4 binom(a+b,a) exp[-T ab],                            (3.3)
T:=4log(2N),
```

because `e'<=M` and `m/M>=T`.

The merged block necessarily contains label `1`.  Given a target partition
`P'`, every preimage is recovered by splitting its block containing `1` into
a part containing `1` and a nonempty complement.  If that block has size
`n`, summing (3.3) over all possible preimages, and harmlessly ignoring the
condition that the complement must become the second block, yields

```text
4 sum_{a=1}^{n-1} binom(n-1,a-1)binom(n,a)
                         exp[-T a(n-a)]
 <=4*4^n exp[-T(n-1)]
 <=4/N^4.                                                 (3.4)
```

The last expression is maximized at `n=2`; for each increment of `n` the
displayed crude upper bound is multiplied by `4exp(-T)<1`.  Summing (3.4)
over target partitions proves (3.2), with every inverse multiplicity
included.  QED.

Consequently, for every `c_*>=2`,

```text
sum_{c>=c_*}W_c(m) <= W_{c_*}(m)/(1-q_N)
                    <= (4/3)W_{c_*}(m).                  (3.5)
```

Moreover `sum_{c>=2}W_c<=W_1/3`.  Therefore, for every nontrivial lower cut
`A(c_0)`, its upper-tail complement `B={c>=c_0+1}` is the smaller side:

```text
pi(B)<pi(A(c_0)).                                         (3.6)
```

This determines the denominator in (1.2); it is not an assumption about the
orientation of `A(c_0)`.

## 4. Full boundary flow through actual `H_3` updates

Fix an exact partition `P` with `c>=2`.  Write `e=e(P)` and `x=M-e`.  At any
fixed adjacent slot, insert `(t,t)` into a word counted by `E_P(m-2)`, with
`t` any internal transposition.  Deletion of that designated pair uniquely
recovers the shorter word and `t`, so the outputs are an injected subset of
`E_P(m)` of exact size `e E_P(m-2)`.  Lemma 2.2 gives

```text
e E_P(m-2)/E_P(m) >= 1/(4e).                             (4.1)
```

For these sources deletion retains exact partition `P`.  Refreshing the
square to `(s,s)` for any crossing transposition `s` therefore merges exactly
two components.

This refresh is one actual `H_3` outcome.  Pad on the right, except at the
last square position where one pads on the left.  If the padding
transposition is `a`, the old and new three-letter products are both `a`.
The exact conditional fiber size is

```text
D_N:=F_3(a)
 = M+3[2(N-2)]+2binom(N-2,2)
 = (3N^2+N-12)/2 <=4M.                                  (4.2)
```

To verify (4.2), condition on the third factor `z`: `z=a` leaves an identity
two-factor product with fiber size `M`; the `2(N-2)` choices sharing one
endpoint with `a` leave a 3-cycle with fiber size `3`; the
`binom(N-2,2)` disjoint choices leave a double transposition with fiber size
`2`.  This derivation uses the stated multiplication convention.

Thus one specified refresh at one specified square position contributes

```text
1/[2|R_m|(m-2)D_N]                                       (4.3)
```

to `K`.  This includes laziness, block-size choice, window scan, and the
exact heat-bath probability.  A crossing `s` differs from the internal `t`,
so its target has discrepancy set exactly that adjacent pair.  Targets from
different square positions are disjoint, including the two end positions
whose padded moves can use the same three-letter window.  Summing (4.3) over
all `x` crossing choices and all `m-1` adjacent positions, then using (4.1),
`|R_m|<=3`, and `(m-1)/(m-2)>=1`, gives the exact-layer averaged exit bound

```text
(m-1)[1/(4e)]x/[2|R_m|(m-2)D_N]
 >=x/(24eD_N)
 >=(N-1)/(96M^2)=:alpha_N.                              (4.4)
```

For the last inequality, `e<=M`, `D_N<=4M`, and convexity gives

```text
x=M-e >= M-binom(N-1,2)=N-1
```

for every disconnected partition.  This is the full word-chain boundary
flow averaged within each exact labeled partition, not merely a transition
of a component-count marginal.  It uses one-step transitions and has no
path length or congestion term.

## 5. Conductance proof

Let `A=A(c_0)` and `B=A^c`.  By reversibility, count flow from the smaller
side `B` to `A`.  Retain only its boundary layer `c=c_0+1` and the actual
merges in (4.4).  With `Z=|Omega(N,m)|`,

```text
Q_K(A,B)=Q_K(B,A)
 >=alpha_N W_{c_0+1}(m)/Z.                               (5.1)
```

By (3.5),

```text
pi(B)<= (4/3)W_{c_0+1}(m)/Z.                             (5.2)
```

Equation (3.6) says that the denominator of `Phi_pm` is exactly `pi(B)`.
Dividing (5.1) by (5.2) proves

```text
Phi_pm(A)>=(3/4)alpha_N=(N-1)/(128M^2).
```

The positivity in Lemma 2.2 for every exact partition proves both sides are
nonempty for `1<=c_0<=N-2`.  This completes Theorem 1.

## 6. Audit of the all-genus pendant bridge-square ratio

Let `C_g(d)` be the number of connected identity words on a fixed `d`-set of
length `k=2g+2d-2`.  After the standard cover-to-word normalization,
Dubrovin--Yang--Zagier's result P1 says, for fixed `d` as `g->infinity`,

```text
C_g(d) ~ (2/d!) binom(d,2)^k.                             (6.1)
```

At one designated slot, choosing a missing label, its attachment endpoint,
and a connected genus-`g` word on the other labels, then inserting the
pendant square, is injective.  Deletion recovers all choices.  Hence the
proportion of connected words counted by this particular pendant-square
construction is exactly

```text
R_g(d)=d(d-1)C_g(d-1)/C_g(d).                             (6.2)
```

Applying (6.1) separately at fixed degrees `d` and `d-1` gives

```text
R_g(d)
 ~ [4d^2/((d-1)(d-2)^2)]
      ((d-2)/d)^(2g+2d-2),          fixed d>=3.           (6.3)
```

Thus `R_g(d)` is exponentially small in `g`.  A uniform inverse-polynomial
all-genus lower bound for this pendant bridge-square subclass is refuted.
This says neither that all adjacent squares are rare nor that the square
down-up chain has small conductance.  In the dense regime the disconnected
side is rare, and Theorem 1 orients flow from that side using internal-square
merges.

The audited primary sources are:

- Boris Dubrovin, Di Yang, Don Zagier, *Classical Hurwitz numbers and related
  combinatorics*, P1 and equations (1), (3), (13), and (19)--(21):
  <https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf>.
  P1 fixes the degree and lets genus grow; it gives no joint error bound when
  both parameters grow.  The displayed degree-six formula has coefficients
  of both signs, so termwise positivity cannot be assumed.
- Norman Do, Jian He, Heath Robertson, *The structure of Hurwitz numbers with
  fixed ramification profile and varying genus*, Theorems 1.5--1.6:
  <https://arxiv.org/abs/2409.06655>.  These also fix the ramification profile
  in the large-genus statement and do not prove the uniform ratio needed in
  the intermediate regime.

Neither cited asymptotic is used in Theorem 1; that theorem uses only the
finite character trace (2.3) and elementary inequalities.

