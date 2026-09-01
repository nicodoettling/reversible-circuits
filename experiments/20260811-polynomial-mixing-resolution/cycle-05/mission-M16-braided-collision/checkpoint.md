# M16 halfway checkpoint: exact braid algebra and failed Caputo inputs

Date: 2026-08-11  
Convention: `(pq)(x)=p(q(x))`.

## Exact setup

Put `G=A_N`, `E=T_N^2`, `p(s,t)=st`, and give `E` its uniform law.  For a
feasible `h in G`, the micro bridge is the uniform law on

```text
Omega^E_(l,h)={A in E^l: p(A_1)...p(A_l)=h}.
```

For `i<j`, let `W=p(A_(i+1))...p(A_(j-1))`.  The raw complete-pair
projection `P_(i,j)` is conditional expectation given all raw coordinates
outside `{i,j}`: it replaces `(A_i,A_j)` uniformly among `(X,Y) in E^2`
such that

```text
p(X) W p(Y)=p(A_i) W p(A_j).
```

This is a self-adjoint idempotent and preserves the endpoint exactly.

## Proved algebra

For `A^g=(g^(-1)s g,g^(-1)t g)` when `A=(s,t)`, the micro Hurwitz map

```text
R(A,B)=(B,A^(p(B)))
```

is a product-preserving, measure-preserving bijection satisfying the braid
relation.  Moving the earlier coordinate `i` right through
`i+1,...,j-1`, applying the adjacent projection, and undoing the braid gives
exactly `P_(i,j)`.  The opposite positive-braid shuttle need not agree; the
`N=4,l=3` exhaustive check records a positive-support orientation witness.

Disjoint pair projections commute for separated or nested (laminar) chords.
They need not commute for crossing chords.  At `N=4,l=4`, endpoint identity,
with `a={1,3}`, `b={2,4}` (one-based sites), the exact harness gives a
transition with chronological probabilities

```text
P_a then P_b: 1/400,
P_b then P_a: 0.
```

It also constructs an exact rational `f` with

```text
<(P_a-I)f,(P_b-I)f>=-194643/759200000<0.
```

Thus both commutation and Caputo's disjoint-pair nonnegativity fail.

The witness embeds for every `N>=4`.  If `M=binom(N,2)` and
`D_N=(3N^2+N-12)/2`, its two chronological probabilities are
`36/(M D_N)^2` and zero, while the corresponding symmetrized `L^2` matrix
entry of the commutator is exactly `6/D_N^2=Theta(N^-4)`.  This certifies
polynomially diluted noncommutativity; it neither proves nor excludes a
larger, constant-size commutator elsewhere.

## Three-site threshold

The complete three-site Markov operator is

```text
T_3=(P_12+P_13+P_23)/3.
```

An all-endpoint-type finite audit found a gap below `1/3` at `N=6`.  This
was upgraded from a numerical observation to an exact rational certificate:
for endpoint `h=(3 4)(5 6)`, an explicit integer-valued function on the
2,020 group-product states, lifted to micro words, has gap Rayleigh quotient

```text
11308644378456917647 / 39796565095659282750
  = 0.28416131772363395... < 1/3.
```

The coefficient vector and exact conditional-class sums are in
`exact_three_gap_witness.json`.  Hence Caputo's needed uniform strict
threshold is rigorously false, independently of the crossing-pair failure.

## Surviving comparison and new frontier

Let

```text
T_l = binom(l,2)^(-1) sum_(i<j) P_(i,j),
C_l = (1/l) sum_(i<j) (I-P_(i,j)) = (l-1)/2 (I-T_l),
H_l = sum_(k=1)^(l-1) (I-P_(k,k+1)).
```

The correct braid shuttle and the adjacent Hurwitz gradient bound give

```text
E_(C_l)(f,f) <= l^2 E_(H_l)(f,f).
```

Therefore the nonlazy adjacent random-scan aligned-`H_4` chain `B_l` obeys

```text
gap(B_l) >= gap(T_l)/(2l^2).
```

This comparison is unconditional and has no hub congestion.

The Carlen--Geronimo--Loss leave-one-out recursion also survives.  Given
micro coordinate `A_k` with `g=p(A_k)`, delete it and conjugate every later
micro increment by `x -> g x g^(-1)`.  This is a uniform bijection to the
`(l-1)`-bridge with endpoint `h g^(-1)` and intertwines every `P_(i,j)` with
`i,j != k`.  If `gamma_l` is the discrete complete-chain gap and

```text
R_l=(1/l) sum_k E[ . | A_k],
mu_l(h)=||R_l|| on constants-perp,
```

then

```text
gamma_l(h) >= (min_u gamma_(l-1)(u)) (1-mu_l(h)).
```

The new smallest open implication is a quantitative, endpoint-uniform bound
on the nonexchangeable coordinate-correlation operator `R_l`, strong enough
to make the product of leave-one-out factors only polynomial.  CGL Lemma 5.1
does not supply the estimate, but centrality gives a sharper exact reduction
than was initially apparent.  Every forward ordered two-coordinate marginal
is position-independent.  If `Kf(x)=E[f(A_j)|A_i=x]` for `i<j`,
`theta(x)=h^(-1)xh`, and `Uf=f o theta`, cyclic bridge invariance gives

```text
K=K^*U,  KU=UK,  K^*=U^(-1)K.
```

Thus `K` is normal.  The nonzero spectrum of `R_l` is the union, over
`kappa in spec(K)`, of the spectra of the scalar `l`-by-`l` Hermitian matrices
with diagonal `1/l`, entries `kappa/l` above the diagonal, and
`conj(kappa)/l` below.  One-coordinate functions whose conditional mean is
zero inside every product fiber lie in `ker K` and contribute only `1/l`.
The remaining `K` acts on the `O(N^4)` group-product support.
