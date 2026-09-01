# R4/R5 substantive checkpoint

## 1. Exact closure imported from R1 and R3

With maps composed as `(alpha beta)(x)=alpha(beta(x))`, R1's orientation is
confirmed: after stable sorting at rank `r`, old endpoint `h`, star endpoint
`q`, and external endpoint `g` obey

```text
q=h^{-1}g,  equivalently h=gq^{-1}.                 (1)
```

Writing `d=binom(r-1,2)`, the complete exact recursion is

```text
Count(r,L,g)
 = sum_(k=0)^L binom(L,k) sum_(h in S_(r-1))
     Count(r-1,L-k,h) StarCount(r,k,h^{-1}g).       (2)
```

`Sample` draws `(k,h)` proportional to the summand, invokes the lower-rank
sampler and the R3 prescribed-endpoint star sampler, chooses a uniform binary
pattern, and invokes the R1 inverse.  This is exact for every feasible
arbitrary endpoint and length.

R3 makes each individual `StarCount/StarSample` query polynomial, but the
literal `h` loop in (2) has `(r-1)!` labeled states.  The endpoint itself has
only `O(r log r)` bits; the explosion belongs to this specified explicit
branch-table implementation, not to endpoint representation and not to an
unconditional hardness claim.

## 2. Positive projected-star collapse

Let

```text
A_a(h)=[h]C_(r-1)^a,  a=L-k,
F_a=2d^a/(r-1)!,
x=g^{-1}(r).
```

On the parity-compatible coset, replace `A_a(h)` by `F_a`.  For a labeled
star word `v` with `q=eval(v)`, equation (1) forces `h=gq^{-1}`.  This lies in
the stabilizer exactly when

```text
(gq^{-1})(r)=r
iff q^{-1}(r)=g^{-1}(r)=x.                          (3)
```

The sign of this `h` is automatically `(-1)^(L-k)` whenever
`sign(g)=(-1)^L`, because a length-`k` star word has sign `(-1)^k`.

Put

```text
Z_r(k,x)=#{v in {(i r):i<r}^k: eval(v)^{-1}(r)=x}.
```

Then the flat positive lift chooses `k` with weight

```text
binom(L,k) d^(L-k) Z_r(k,x),                        (4)
```

samples `v` uniformly in this projected fiber, sets `h=g eval(v)^{-1}`,
recurses on `(r-1,L-k,h)`, chooses a uniform pattern, and applies the R1
inverse.  The constant `2/(r-1)!` cancels from (4).  This derivation samples
an actual labeled `h`; it does not enumerate the stabilizer and it does not
use a signed character sum.

### Exact projected chain

Let `s=r-1`.  For the prefix state `y_j=eval(v_1...v_j)^{-1}(r)`, the next
factor acts as

```text
y_(j+1)=(i r)(y_j).
```

Thus, with `c_k=Z_r(k,r)` and `l_k=Z_r(k,x)` for each fixed `x<r`,

```text
c_(k+1)=s l_k,
l_(k+1)=c_k+(s-1)l_k,
c_0=1, l_0=0.
```

Diagonalizing this two-state recurrence gives the integer formulas

```text
Z_r(k,r) = (s^k+s(-1)^k)/r,
Z_r(k,x) = (s^k-(-1)^k)/r,  x<r.                   (5)
```

A uniform projected word can be sampled backwards: at target state `y_j`,
choose last factor `(i r)` with weight equal to the number of length-`j-1`
prefixes ending at `(i r)(y_j)`.  This costs `O(rk)` integer operations, or
less using the two orbit values.  Formula (5) also makes all `L+1` branch
weights (4) exactly computable with polynomial-bit integers.

## 3. Uniform pointwise old-walk estimate

For the non-lazy random-transposition walk on `S_n`, remove the trivial and
sign eigenvectors.  Its exact absolute spectral radius is

```text
rho_n=1-2/(n-1),  n>=3.                            (6)
```

This follows from the complete-graph case of
Caputo--Liggett--Richthammer, Theorem 1.1, with the sign anti-commutation
handling negative eigenvalues.  A kernel-entry spectral bound therefore
gives, for every parity-compatible labeled `h`,

```text
| P_n^a(e,h)/(2/n!) - 1 |
 <= delta_n(a):=(n!/2)rho_n^a.                     (7)
```

Consequently, on any retained branch for which `delta_n(a)<1`, normalized
exact and flat positive branch laws differ in TV by at most
`delta_n(a)/(1-delta_n(a))`.  This is a bridge-weight comparison: it compares
the exact positive completion weight `A_a(h)` to `F_a` before normalization.
It is not merely an unconditioned endpoint-mixing assertion.

## 4. Feasibility and the short-branch issue

If `a>=r-2`, every parity-compatible `h in S_(r-1)` is feasible, since
`r-2` is the maximum transposition length there.  Short branches cannot be
ignored without an error bound.

The current retained-length construction uses the global top rank `N` and
rational rank weights.  Let

```text
ell=ceil(log_2 N),  s_N=ceil(sqrt(N ell)),
w_r=1/(r ceil(sqrt(r))) + 100 s_N/(N r),  4<=r<=N,
W_N=sum_(r=4)^N w_r,
c_3=1,
c_r=1+(sum_(j=4)^r w_j)/W_N,
B_2=0,
B_r=ceil(N r(r-1)c_r),  r>=3.                      (8)
```

Then `c_N=2` and

```text
B_N=2N^2(N-1)<2N^3.
```

At rank `r>=4`, retain only branches with `a>=B_(r-1)`; rank three closes
exactly over `S_2` and needs no truncation.  The retained calls are feasible
and satisfy the pointwise estimate (7).  Because `c_r-c_(r-1)=w_r/W_N`, the
old-count cutoff lies above its binomial mean deficit by two deliberately
separate margins: one yields an `exp(-Omega(N))` tail, while the
`sqrt(log N/N)/r` term yields enough extra exponent to pay for the `r!`
worst-case bridge-denominator factor.

The constant audit of this tail and the final explicit per-rank error are the
remaining proof steps.  If they fail, the projected lift remains a correct
one-rank reduction but not a recursively closed negligible-error sampler.

## 5. Boundaries already settled

- `N=2`: the unique transposition gives the exact base sampler at every
  feasible parity.
- `L=0`: only `g=e` is feasible; return the empty word.
- odd identity length: the target is empty and must be rejected.
- arbitrary `g`: feasibility is exactly
  `sign(g)=(-1)^L` and `L>=r-cycles(g)`; a minimal cycle factorization and
  pair padding prove sufficiency.
- retained recursive endpoints: (3) and the cutoff make parity and minimum
  length automatic.

Status at checkpoint: the exact recurrence, projected-star proposal,
orientation, projected sampler, and one-rank relative-error lemma are
**proved**.  Full dense recursive closure is **conditional** on completing
the explicit retained-length tail calculation and telescope.

## 6. Post-checkpoint integration of the stronger R2 lift

The R2 checkpoint supplies a complementary star-long branch and has now been
audited against (1)--(5).  At current rank `r`, write old length `s=L-k`,
`d=binom(r-1,2)`, and `b=r-1`.  After one common scaling, its exact positive
proposal weights are

```text
r binom(L,k)d^s Z_r(k,g^{-1}(r)),  s>=k,
  binom(L,k)d^s b^k,                k>s.             (9)
```

For `s>=k`, this is exactly the projected old-flat construction above; it
samples the star word and recurses on the forced `h`.  For `k>s`, it draws an
unconditioned old word (thereby retaining the exact old count), sets its
actual endpoint `h`, and invokes R3 on `h^{-1}g` after flattening the star
endpoint count.  The star-long branch therefore terminates the rank recursion
rather than passing a short old bridge downward.

The star-walk pointwise bound can be audited without Jucys--Murphy machinery:
apply Caputo--Liggett--Richthammer Theorem 1.1 to the star graph
`K_(1,r-1)`, whose one-particle Laplacian gap is `1`; after normalization by
degree `r-1` and sign twisting, the nontrivial absolute radius is
`(r-2)/(r-1)`.  Hence R2's two-sided single-lift bound is sound.

This improves the recursive task sharply: only old-long branches recurse,
and they have `s>=L/2`.  The retained-length floor is now needed solely to
exclude the rare event that a recursing old-long branch falls below the next
rank's certified dense floor.  Star-long short-old branches remain in the
proposal and are sampled directly.  The final report will use (9), not the
weaker one-sided architecture, and will complete the exact conditioned-tail
and telescope calculation.
