# Halfway checkpoint: bridge-conditioned missing-cut bound

## Candidate theorem

Let `A>=1` be a universal constant for the parity-aware
Diaconis--Shahshahani estimate

```text
0 <= (n!/2) P_n^t(id,id)-1 <= 1/16
```

for the nonlazy uniform-transposition walk, every `n>=2`, and every even
`t>=A n log(n+1)` (the `n=2` case is exact).  Put `C=256(A+1)`.

For `v>=3`, even `j>=C v log(v+1)`, let `Z_v(j)` and `C_v(j)` count all and
connected-support identity words.  The audit currently gives

```text
C_v(j) = (2 M^j/v!) (1+epsilon_j),
|epsilon_j| <= 1/[128(j+2)].
```

This is strong enough at `j=k-2,k,k+2` to prove

```text
rho_v(g+1)-rho_v(g) >= 3k/M^2
```

when `k-2>=C v log(v+1)`.

## New estimate avoiding the old `v!` loss

Condition on a fixed missing cut `A`, with `q=|A|<=v/2`, `b=v-q`,
`L=binom(q,2)+binom(b,2)`, and `M=binom(v,2)`.  Given that every step is
internal, the number `J` of steps in the larger side is
`Bin(j,alpha)`, where

```text
alpha=binom(b,2)/L >= 1/2.
```

The internal return probability factors as

```text
E[P_b^J(id,id) P_q^(j-J)(id,id)].
```

Once `j>=4A v log(v+1)`, the large side has at least its pointwise-mixing
threshold except on a Chernoff event of probability at most `exp(-j/16)`.
Therefore

```text
P_internal^j(id,id) <= 3/b! + exp(-j/16).
```

For even `j`, the full return probability is at least `2/v!` because all
nontrivial character terms are nonnegative.  Also

```text
L/M = 1-qb/M <= exp(-q/v).
```

Union-bounding over all smaller cut sides gives the bridge-conditional
disconnection probability

```text
d_v(j)
 <= (3/2) sum_(q>=1) [e v^2 exp(-j/v)]^q
      + 2^(v-1) v! exp(-j/16).
```

At `j>=C v log(v+1)`, elementary monotonicity and `C>=512` make this at most
`1/[512(j+2)]`.  This is the key improvement: the factorial ratio for a
size-`q` missing side is only `v!/(v-q)!<=v^q`, and the missing-cut exponent
beats it at `O(v log v)` time.

## Remaining checkpoint work

- Freeze all scalar inequalities rather than citing asymptotic notation.
- Write the adjacent-ratio propagation and dependency/calibration audit.
- Self-attack whether the parity-conditioned subgroup walk was bounded at
  every possible binomial value of `J`.

