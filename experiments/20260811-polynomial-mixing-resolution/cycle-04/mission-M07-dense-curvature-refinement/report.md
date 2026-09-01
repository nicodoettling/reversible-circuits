# Report: `O(v log v)` dense Hurwitz-rate curvature

## 1. Exact claim and conventions

Permutations are multiplied with `(pq)(x)=p(q(x))`.  Let
`M=binom(v,2)`, and let `C_v(j)` be the number of length-`j` transposition
words on `[v]` with identity product and connected support.  Put

```text
a_v(g)=C_v(k)/k!,       k=2(v-1)+2g,
rho_v(0)=0,             rho_v(g)=a_v(g-1)/a_v(g)  (g>=1).
```

Let `A>=1` be a universal constant such that the parity-aware pointwise
Diaconis--Shahshahani estimate in Section 2.1 below holds, and define

```text
C_* = 256(A+1).
```

**Theorem.** For every `v>=3` and `g>=1`, if

```text
k-2 >= C_* v log(v+1),
```

then

```text
rho_v(g+1)-rho_v(g) >= 3k/M^2 > 0.                 (1)
```

Thus the previous `4M log(2v)=Theta(v^2 log v)` dense threshold is replaced
by `C_*v log(v+1)`.  This is a nonterminal theorem: an infinite
`k=O(v log v)` low/intermediate zone remains.

## 2. Full argument

### 2.1 Primary pointwise input and amplification

Let `P_n` be the nonlazy random walk which multiplies by a uniformly chosen
transposition, and let `r_lambda` be its scalar in the irreducible
`S_n`-representation `lambda`.  For even `t`, Fourier inversion at the
identity gives

```text
P_n^t(id,id) = (2/n!)(1+u_n(t)),
u_n(t)=(1/2) sum_(lambda not trivial,sign)
                    (d_lambda)^2 r_lambda^t >=0.      (2)
```

The pointwise input is the partition-zone estimate in P. Diaconis and
M. Shahshahani, "Generating a random permutation with random
transpositions," *Z. Wahrscheinlichkeitstheorie verw. Gebiete* **57**
(1981), 159--179, Lemma 14 equation (3.1), the zone bounds (3.2), (3.3),
(3.5), (3.7), (3.13), and their collection in the proof of Theorem 1
([primary PDF](https://www.imo.universite-paris-saclay.fr/~pierre-loic.meliot/symmetric/texts/Diaconis%2C%20Shahshahani%20-%20Generating%20a%20random%20permutation%20with%20random%20transpositions.pdf)).

The normalization translation, already audited in cycle-03 M10, is as
follows.  For the with-replacement lazy law in that source,

```text
z_lambda=1/n+(n-1)r_lambda/n.
```

Pair conjugate partitions in (2), choose the member with `r_lambda>=0`, and
use `0<=r_lambda<=z_lambda`; self-conjugate partitions have
`r_lambda=0`.  The absolute pointwise error in (2) is therefore bounded by
the Plancherel sum in Diaconis--Shahshahani Lemma 14.  Their partition-zone
bounds imply that there is a universal `A>=1` such that, for every `n>=3`
and every even `t>=A n log(n+1)`,

```text
0 <= u_n(t) <= 1/16.                                  (3)
```

For `n=2`, (3) holds with `u_2(t)=0`.

Every nontrivial, nonsign representation satisfies the exact character-ratio
bound

```text
|r_lambda| <= (binom(n,2)-n)/binom(n,2)
             =1-2/(n-1).                              (4)
```

Indeed content sum is monotone in dominance order; the largest proper shape
is `(n-1,1)`, and conjugation changes the sign.  Let `t_n` be the least even
integer at least `A n log(n+1)`.  From (2)--(4), for later even `j`,

```text
u_n(j) <= (1/16) exp[-2(j-t_n)/(n-1)].                 (5)
```

Take `n=v`, set `x=v+1`, and suppose `j>=C_*v log x`.  The function
`(j+2)exp[-2(j-t_v)/(v-1)]` is decreasing in this range.  Since
`t_v<=Av log x+2`, at the threshold (5) gives

```text
u_v(j) <= (e^2/16) x^[-2(C_*-A)].
```

The following explicit scalar check will also be used below.  With
`C_*=256(A+1)>=512`, `v>=3`, `x>=4`, `C_*<=2^(C_*/4)`, and
`v log x<=x^2`,

```text
512(j+2)u_v(j)
 <= 512 C_* / x^(255 C_*/128)
 <= 1.                                                 (6)
```

Thus `u_v(j)<=1/[512(j+2)]` throughout the claimed range.

### 2.2 Disconnected support under the identity bridge

Let

```text
d_v(j)=Pr(the support is disconnected | product=id).
```

Fix a vertex cut with smaller side of size `1<=q<=v/2`, and write

```text
b=v-q,
L=binom(q,2)+binom(b,2)=M-qb,
alpha=binom(b,2)/L >=1/2.
```

Conditioned on choosing no crossing transposition, the word is the product
walk on `S_q x S_b`.  The number `J` of its `j` steps falling in the larger
factor is `Bin(j,alpha)`, and its exact identity-return probability is

```text
E[P_b^J(id,id) P_q^(j-J)(id,id)].                     (7)
```

Use the constant coordinate convention when `q=1`.  If `J` is odd then the
first return factor is zero.  If `J` is even and at least
`A b log(b+1)`, (3) makes it at most `3/b!`; below that threshold use the
trivial bound one.  Since `j>=C_*v log(v+1)` puts the threshold below half
the binomial mean, Chernoff's inequality gives

```text
Pr[J<A b log(b+1)] <= exp(-j/16).
```

Consequently (7) is at most

```text
3/b! + exp(-j/16).                                     (8)
```

This is where conditioning on return saves the old factorial loss.  For even
`j`, (2) gives `P_v^j(id,id)>=2/v!`.  Also

```text
(L/M)^j <= exp(-qj/v),                                 (9)
```

because `qb/M>=q/v`.  Union-bound all cuts by their smaller sides.  From
(8)--(9), `v!/b!<=v^q`, and
`binom(v,q)<=(ev/q)^q`,

```text
d_v(j)
 <= (3/2) sum_(q=1)^[floor(v/2)]
            [e v^2 exp(-j/v)]^q
      + 2^(v-1)v! exp(-j/16).                          (10)
```

Put `R=e v^2 exp(-j/v)`.  In the stated range `R<=1/2`, so the first term in
(10) is at most `3R`.  Both `(j+2)e^{-j/v}` and
`(j+2)e^{-j/16}` decrease in the range.  At
`j=C_*v log x`, the two exact checks are

```text
1024(j+2) 3e v^2 e^(-j/v)
 <= 6144e C_* v^3 log(x) x^(-C_*)
 <= 6144e C_* / x^(C_*-4)
 <= 1,                                                 (11)

1024(j+2) 2^(v-1)v! e^(-j/16)
 <= 2048 C_* / x^((C_*/16-2)v-2)
 <= 2^(27-C_*/8)
 <= 1.                                                 (12)
```

For (11), use `6144e<2^15`, `C_*<=2^(C_*/4)`, and `x>=4`; for (12), also use
`2^(v-1),v!<=x^v`.  Hence

```text
d_v(j) <= 1/[512(j+2)].                                (13)
```

No unconditioned coupon-collector probability was divided by an unexplained
`2/v!`: the subgroup return probability (8) is retained before the division.

### 2.3 Connected counts at three adjacent lengths

Let `Z_v(j)=M^jP_v^j(id,id)` count all identity-return words.  Equations
(2), (6), and (13) give

```text
C_v(j)=Z_v(j)(1-d_v(j))
      =(2M^j/v!)(1+epsilon_j),
|epsilon_j|<=1/[128(j+2)]                              (14)
```

for every even `j>=C_*v log(v+1)`.  Indeed
`epsilon=u-d-ud`, and both `u,d` are at most
`1/[512(j+2)]`.

Now set `j=k-2`.  At each of `k-2,k,k+2`, (14) gives a common bound

```text
|epsilon| <= delta:=1/(128k).
```

Therefore both adjacent connected-count correction ratios differ from one
by at most

```text
2delta/(1-delta) <= 3delta < 1/(32k).                  (15)
```

The factorial normalization gives

```text
rho_v(g)   = [k(k-1)/M^2]
             (1+epsilon_(k-2))/(1+epsilon_k),
rho_v(g+1) = [(k+2)(k+1)/M^2]
             (1+epsilon_k)/(1+epsilon_(k+2)).           (16)
```

Using (15), the numerator of their difference after multiplication by `M^2`
is at least

```text
(k+2)(k+1)(1-1/(32k))-k(k-1)(1+1/(32k))
 =4k+2-(2k^2+2k+2)/(32k)
 >=3k.                                                 (17)
```

Equations (16)--(17) prove (1).

## 3. Probability, runtime, path, and congestion accounting

This is an enumerative/functional estimate, not a comparison-flow
construction.  All probabilities are exact before inequalities:

- missing a fixed cut: `(L/M)^j`;
- large-side step count: `Bin(j,alpha)`, `alpha>=1/2`;
- bad allocation tail: at most `e^{-j/16}`;
- full even return: at least `2/v!`;
- all cut multiplicities: explicitly summed in (10).

There is no algorithmic runtime, path length, or congestion claim.  The
result supplies a rate-curvature constant for a later zero-range Poincare
argument.

## 4. Dependencies

- **Cited, hypotheses and normalization checked:** Diaconis--Shahshahani,
  Lemma 14 and the partition-zone estimates in the proof of Theorem 1,
  translated from their with-replacement lazy transposition measure to the
  parity-aware even nonlazy return as in Section 2.1.
- **Proved here:** every `g in S_n` parity return formula (2); spectral
  amplification (4)--(6); exact product-walk return decomposition (7);
  Chernoff/cut union (8)--(13); adjacent-ratio propagation (14)--(17).
- **Inherited, proved:** the relation between `C_v`, `a_v`, and `rho_v`; the
  all-genus lower bound `rho_v(g)>=12/v^3` is not used here.
- **No empirical dependency.**

## 5. First unproved standalone proposition

> **LOW/INTERMEDIATE HURWITZ-RATE CURVATURE.** There are universal `c>0` and
> `B<infinity` such that for every `v>=3`, every `g>=0`, and
> `k=2(v-1)+2g` with `k-2<C_*v log(v+1)`,
> `rho_v(g+1)-rho_v(g)>=c(v+g+1)^(-B)`.

The unresolved genus window has shrunk from `O(v^2 log v)` to
`O(v log v)`, but it remains infinite.

## 6. Strongest self-attack

The theorem depends on a universal pointwise constant `A` extracted from the
Diaconis--Shahshahani partition-zone proof rather than a numerically optimized
value.  This is sufficient for an existential universal theorem and every
subsequent scalar constant is explicit in `A`, but it is not a useful
numerical cutoff.  More importantly, no monotonicity or recurrence argument
is supplied below the cutoff; dense smoothing cannot by itself settle the
remaining `O(v log v)` occupancies.

The main technical failure mode was a hidden factorial penalty for a small
unmixed side of a missing cut.  Equation (7) keeps the larger-side return and
loses only `v!/(v-q)!`, while the Chernoff term retains an exponential
`e^{-j/16}` strong enough to absorb the full `v!`; this closes that failure
mode without assuming the small side mixes.

## 7. Calibration

- `v=2`: excluded from the theorem and exactly known; the first increment is
  12, and later increments are `4k+2`.
- `v=3,4`: all scalar inequalities hold (very conservatively) because
  `C_*>=512`; exact low-genus values remain the relevant calibration below
  the cutoff.
- `g=0`: the required increment is `rho_v(1)-rho_v(0)` with
  `rho_v(0)=0`; it never falls in this dense range and is not silently treated
  by differencing two positive rates.
- Known values `C_0(2)=1`, `C_0(3)=24`, `C_0(4)=2880` and the positive
  `v=4` increments are consistent but are not evidence for the universal
  claim.
- Odd lengths have zero identity-return count and are never used.

## 8. Artifacts and reproduction

Artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M07-dense-curvature-refinement/plan.md
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M07-dense-curvature-refinement/checkpoint.md
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M07-dense-curvature-refinement/report.md
```

The primary PDF used in the audit was already downloaded as
`/tmp/m15-diaconis-shahshahani.pdf`; the durable direct link is given in
Section 2.1.  No computation was used.

## 9. Verdict

**PROVED.**  The assigned `O(v log v)` dense-curvature refinement is proved.
This is a nonterminal partial theorem; the named low/intermediate proposition
in Section 5 remains open.

