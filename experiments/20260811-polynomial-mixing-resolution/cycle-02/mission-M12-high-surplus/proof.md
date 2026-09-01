# Uniform component-threshold conductance in the extreme-dense regime

## 1. Convention, kernel, and statement

Permutations are maps on `[N]`, `pq` means `p` after `q`, and a word is
evaluated as `t_1...t_m`.  Put `M=binom(N,2)`.  The target `pi` is uniform on
`Omega(N,m)`, and the exact kernel is

```text
K = (1/2)I
    + (1/(2|R_m|)) sum_{r in R_m} (1/(m-r+1)) sum_i H_{i,r},
R_m={r in {3,4,5}:r<=m}.
```

For a word `w`, let `c(w)` be the number of support-graph components,
including isolated vertices.  The following theorem is proved below.

**Theorem 1 (all thresholds at extreme density).**  Let `N>=3`, let `m` be
even, and suppose

```text
m-2 >= L_N := 2 N^3 log(2N).
```

For every integer `c_0` with `1<=c_0<=N-2`, set

```text
A(c_0)={w in Omega(N,m):c(w)<=c_0}.
```

Then `A(c_0)` and its complement are nonempty and

```text
Q_K(A(c_0),A(c_0)^c)
-------------------------------- >= (N-1)/(128 M^2).       (1.1)
min{pi(A(c_0)),pi(A(c_0)^c)}
```

For fixed `N,m`, total surplus satisfies

```text
G(w)=m/2-N+c(w).                                           (1.2)
```

Consequently (1.1) holds for every nontrivial total-surplus threshold
`A_{<=g}` in this regime, with an exponent independent of `g`.

This is a restricted theorem, not TERMINAL A or TERMINAL B.

## 2. Surplus is component count

Let the nontrivial support components have label sizes `v_i` and factor
counts `k_i`; isolated labels contribute neither factors nor surplus.  If
there are `q` nontrivial components on `s` active labels, then

```text
G(w) = sum_i [k_i-2(v_i-1)]/2
     = m/2-s+q.
```

The total number of support components is `c=N-s+q`, proving (1.2).  In
particular adjacent surplus layers at fixed length are adjacent component-
count layers.

## 3. Uniform return-count estimate for every support partition

Let `P` be a labeled set partition of `[N]` with at least one block of size
at least two.  Define

```text
E(P) = union_{B in P} T_B,
e(P) = |E(P)| = sum_{B in P} binom(|B|,2),
H_P  = product_{B in P} S_B,
h(P) = |H_P| = product_{B in P} |B|!.
```

Isolated blocks make trivial factors in `H_P`.  Let `Z_P(k)` count length-`k`
identity words whose factors all lie in `E(P)`; their exact support partition
may refine `P`.  Let `E_P(k)` count those whose exact support partition is
`P`.

### Lemma 3.1 (trace bound)

For every even `k` and `e=e(P)>=1`,

```text
2 e^k/h(P) <= Z_P(k)
              <= 2 e^k/h(P) + max(e-2,0)^k.               (3.1)
```

**Proof.**  In the group algebra of `H_P`, put
`T_P=sum_{t in E(P)}t`.  This is central.  The regular-representation trace
gives

```text
Z_P(k)=h(P)^(-1) sum_rho dim(rho)^2 nu_rho^k,              (3.2)
```

where `nu_rho` is the scalar by which `T_P` acts in the irreducible `rho`.
For `S_n`, the transposition-class sum has scalar equal to the sum of the
contents of the Young diagram.  Its unique maximum and minimum are
`+binom(n,2)` and `-binom(n,2)`, at the trivial and sign representations; any
other scalar is at distance at least `n>=2` from the corresponding extreme.
For the direct product, the scalars add.  Hence `+e` and `-e` are simple and
every other scalar has absolute value at most `e-2`.  Since `k` is even, all
terms in (3.2) are nonnegative.  The two one-dimensional extremal terms give
the lower bound, and the remaining squared dimensions sum to at most `h(P)`,
giving the upper bound.  If `e=1`, `H_P` has one active `S_2` factor and only
the two extremal representations, so the remainder is zero.  QED.

The same formula is the product-group version of the classical Frobenius
return formula.  Dubrovin--Yang--Zagier state the `S_d` formula explicitly in
their equation (19)--(21) discussion; no asymptotic result is being imported
into this lemma.

### Lemma 3.2 (exact-support estimate)

If `N>=3`, `k` is even, and `k>=L_N`, then, uniformly over every `P` with
`e=e(P)>=1`,

```text
e^k/h(P) <= E_P(k) <= 4 e^k/h(P).                         (3.3)
```

**Proof.**  First (3.1), `h(P)<=N!`, `e<=M<=N^2/2`, and
`1-x<=exp(-x)` imply, for `e>=2`,

```text
[h(P)/2] (1-2/e)^k
 <= [N!/2] exp(-2k/e)
 <= [N!/2] exp(-8N log(2N)) < 1.
```

Thus

```text
2e^k/h(P) <= Z_P(k) <= 4e^k/h(P).                         (3.4)
```

The same conclusion is immediate for `e=1`.

If a word counted by `Z_P(k)` does not have exact support partition `P`,
then some nontrivial block `B` of `P` is disconnected by the word.  Therefore
there is an unordered nonempty proper cut `A | (B\A)` across which no factor
appears.  Let `P'` be the refinement splitting `B` along that cut.  If
`a=|A|`, `b=|B\A|`, then

```text
e(P')=e-ab <= e-1,
h(P)/h(P')=binom(a+b,a) <= 2^N.
```

Using (3.4) for `P'` (the case `e(P')=0` contributes zero) and the lower
bound in (3.4) for `P`,

```text
Z_{P'}(k)/Z_P(k)
 <= 2 binom(a+b,a) (1-ab/e)^k
 <= 2^(N+1) exp(-k/e).                                   (3.5)
```

There are at most `N 2^(N-1)` candidate cuts over all blocks.  Since
`k/e>=4N log(2N)`, a union bound gives

```text
[Z_P(k)-E_P(k)]/Z_P(k)
 <= N 2^(2N) exp[-4N log(2N)] <= 1/2                     (3.6)
```

for every `N>=3`.  Combining (3.4) and (3.6) proves (3.3).  Notice that
overcounting a disconnected word in (3.6) only strengthens the upper bound.
QED.

## 4. Component layers have a geometric stationary tail

Let

```text
W_c(k)=sum_{P: |P|=c, e(P)>=1} E_P(k),        1<=c<=N-1.  (4.1)
```

Thus `W_c(m)` is exactly the number of bridge words with `c` support
components.  There are no length-positive words with `c=N`.

### Lemma 4.1 (uniform layer ratio)

Under the hypotheses of Theorem 1,

```text
W_{c+1}(m) <= q_N W_c(m),
q_N := 2^(2N+1) exp(-m/M) <= 1/4                         (4.2)
```

for every `1<=c<=N-2`.

**Proof.**  Order the blocks of any partition by their smallest label.  Map
a partition `P` with `c+1` blocks to `F(P)` by merging its first two blocks.
If their sizes are `a,b`, put `e=e(P)` and `e'=e(F(P))=e+ab`.  Lemma 3.2
gives

```text
E_P(m)/E_{F(P)}(m)
 <= 4 [h(F(P))/h(P)] (e/e')^m
 = 4 binom(a+b,a) (1-ab/e')^m
 <= 4 2^N exp(-m/M).                                    (4.3)
```

The merged block necessarily contains label `1`.  Given `F(P)`, a preimage
is determined by splitting that block into a part containing `1` and a
nonempty complementary part; ignoring the ordering constraint leaves at most
`2^(N-1)` choices.  This proves the first inequality in (4.2), including
every multiplicity.  Finally `m/M>=4N log(2N)`, and for `N>=3`

```text
(2N+1)log 2 - 4N log(2N) <= -log 4,
```

so `q_N<=1/4`.  QED.

It follows that for every `c_*>=2`,

```text
sum_{c>=c_*} W_c(m) <= W_{c_*}(m)/(1-q_N) <= (4/3)W_{c_*}(m).  (4.4)
```

Also `sum_{c>=2}W_c<=W_1/3`.  Thus, for every nontrivial lower threshold
`A(c_0)`, the smaller stationary side is always its upper-tail complement.
This explicitly fixes the mass orientation rather than assuming
`pi(A(c_0))<=1/2`.

## 5. Exact boundary flow through deletable squares

Fix an exact partition `P` with `c>=2`, and abbreviate `e=e(P)` and
`x=M-e`.  At any fixed adjacent position, insert `(t,t)` into an exact-
support word counted by `E_P(m-2)`, where `t` is any of the `e` internal
transpositions.  Deleting the designated pair uniquely recovers both the
shorter word and `t`, so this is an injection of size `e E_P(m-2)` into the
words counted by `E_P(m)`.  Lemma 3.2 gives the fixed-position probability

```text
e E_P(m-2)/E_P(m) >= 1/(4e).                             (5.1)
```

For every word in this injected set, deletion leaves exact partition `P`.
Replacing the designated square by `(s,s)` for any of the `x` crossing
transpositions therefore merges exactly two blocks and decreases `c` by one.

This replacement is an actual `r=3` move of `K`.  Pad on the right unless
the square occupies the last two positions, in which case pad on the left.
If the padding transposition is `a`, both old and new three-letter blocks
have ordered product `a`.  The exact length-three fiber size at a
transposition is

```text
D_N := F_3(a)
     = M + 3[2(N-2)] + 2 binom(N-2,2)
     = (3N^2+N-12)/2 <= 4M.                              (5.2)
```

Indeed, condition on the third factor `z`.  If `z=a`, the first two factors
have identity product and there are `M` choices.  If `z` shares exactly one
endpoint with `a`, there are `2(N-2)` such `z` and the resulting 3-cycle has
two-transposition fiber size `3`.  If `z` is disjoint, there are
`binom(N-2,2)` choices and the double transposition has fiber size `2`.
This also independently checks the pending coordinator square-refresh lemma.

For one specified square position and one specified replacement, the exact
kernel contribution is

```text
1/[2 |R_m| (m-2) D_N].                                   (5.3)
```

Summing (5.3) over the `x` crossing replacements and over all `m-1` adjacent
positions, then using (5.1), `|R_m|<=3`, and `(m-1)/(m-2)>=1`, shows that a
uniform state in the exact `P` layer has average `K`-probability at least

```text
(m-1) [1/(4e)] x / [2|R_m|(m-2)D_N]
 >= x/(24eD_N)
 >= (N-1)/(96M^2) =: alpha_N                             (5.4)
```

of moving to the layer with `c-1` components.  The last inequality uses
`e<=M`, `D_N<=4M`, and

```text
x=M-e >= M-binom(N-1,2)=N-1
```

for every disconnected partition.  Equation (5.4) includes laziness, block-
size choice, window choice, and exact conditional-fiber probability.  If one
ordered source-target pair is represented by more than one padded window,
the corresponding kernel contributions add; no disjointness assumption or
path routing is used.

## 6. Proof of Theorem 1

Let `B=A(c_0)^c={c>=c_0+1}`.  Reversibility permits counting flow from `B`
to `A`.  Retain only source states in its boundary layer `c=c_0+1` and the
merges counted in (5.4).  With `Z=|Omega(N,m)|`,

```text
Q_K(A,B)=Q_K(B,A)
 >= alpha_N W_{c_0+1}(m)/Z.                              (6.1)
```

By (4.4),

```text
pi(B) <= (4/3)W_{c_0+1}(m)/Z.                            (6.2)
```

The paragraph after (4.4) proves `pi(B)<pi(A)`, so the denominator of the
two-sided conductance is exactly `pi(B)`.  Dividing (6.1) by (6.2) gives

```text
Phi_pm(A) >= (3/4)alpha_N = (N-1)/(128M^2),
```

as claimed.  QED.

## 7. What the all-genus formulas do and do not prove

Let `C_g(d)` count connected identity words on a fixed `d`-set of length
`k=2g+2d-2`.  With the cover-to-word normalization checked in Cycle 01,
Dubrovin--Yang--Zagier's fixed-degree large-genus formula becomes

```text
C_g(d) ~ (2/d!) M_d^k,       M_d=binom(d,2),              (7.1)
```

for `g -> infinity` with `d` fixed.  The fixed-position construction that
adds a new label by a pendant square has exactly

```text
d(d-1) C_g(d-1)                                                 (7.2)
```

outputs: deletion recovers the missing label, the other endpoint, and the
shorter connected word.  Dividing by `C_g(d)` and applying (7.1) in degrees
`d` and `d-1` gives, for each fixed `d>=3`,

```text
d(d-1)C_g(d-1)/C_g(d)
 ~ [4d^2/((d-1)(d-2)^2)] ((d-2)/d)^(2g+2d-2).            (7.3)
```

Thus this particular bridge-square probability is exponentially small in
`g`; a uniform inverse-polynomial lower bound for it is false.  The signed
finite-exponential formulas do not give a joint error bound when `d,g` both
vary, and fixed-genus formulas cannot repair that gap.  Theorem 1 avoids the
false direction by orienting conductance from the smaller disconnected tail
and using internal-square merges.

The external inputs audited here are:

- Boris Dubrovin, Di Yang, Don Zagier, *Classical Hurwitz numbers and related
  combinatorics*, especially equations (1), (3), (13), and (19)--(21):
  <https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf>.
- Norman Do, Jian He, Heath Robertson, *The structure of Hurwitz numbers with
  fixed ramification profile and varying genus*, Theorems 1.5--1.6:
  <https://arxiv.org/abs/2409.06655>.

Both are cited dependencies for the audit and asymptotic statement (7.1)--
(7.3), not for Theorem 1 itself.  DYZ's recurrence computes the numbers but
does not state the uniform positive ratio required for intermediate density;
their degree-six exponential example visibly has coefficients of both signs.

