# M287 independent reconstruction of M285

Date: 2026-08-14 UTC.

Status: the coefficient, cyclic-composition, owner-correlation, and finite
quadratic-witness claims below are independently verified.  GOCI/OCI and all
downstream conclusions remain unresolved.

## 1. Scope and convention

Use `(pq)(x)=p(q(x))`, with displayed factors multiplied left-to-right.  Fix
odd `k>=3`, put `n=3k`, and use the first separated fixed cell of the
auxiliary uniform minimal factorization law of the long cycle.  This audit
does not concern the global uniform identity-word law or directly analyze
the lazy exact same-product `{3,4,5}` heat-bath chain.

For a permutation `Q` of transposition rank `r`, with cycle sizes `d_i`, the
minimal-completion count is

```text
F_r(Q)=r! product_i tau(d_i),
tau(d)=d^(d-2)/(d-1)!,   tau(1)=1.
```

## 2. Independent derivation of `beta_1` and `beta_2`

Let

```text
L=(1,...,k-1,2k,...,3k-1),       M=(k,...,2k-1),
C_-=(0,...,k-1),                 C_+=(2k,...,3k-1),
F=C_- C_+,                       r=2k-2.
```

For a chord `e` of a `d`-cycle, cutting it into sizes `u,d-u` leaves
`(d-2)!tau(u)tau(d-u)` completions.  Dividing by
`(d-1)!tau(d)` gives

```text
nu_C(e)=tau(u)tau(d-u)/[(d-1)tau(d)].
```

In channel one, the merged source has one independent `L` factor and one
independent `M` factor.  The split source chooses `C_-` or `C_+` fairly and
then takes an independent `M` factor.  The two possible color orders commute
and were already conditioned into the channel mass.  Therefore the signed
normalized product coefficient is exactly

```text
beta_1(s)
 =sum_(ef=s; e in T(L), f in T(M))nu_L(e)nu_M(f)
  -1/2 sum_(C in {C_-,C_+})
        sum_(ef=s; e in T(C), f in T(M))nu_C(e)nu_M(f).
```

For channel two, a rank-two supported product has exactly three ordered
transposition lifts if it is a forward triangle and two if it is a double.
After two ordered factors with product `s=ef`, the residual is
`(ef)^-1 Q=s^-1Q`.  Hence, with `a(s)=3` or `2`, respectively,

```text
H_(2,Q)(s)=a(s) F_(r-2)(s^-1 Q)/F_r(Q),

beta_2(s)=a(s)[F_(r-2)(s^-1 L)/F_r(L)
                  -F_(r-2)(s^-1 F)/F_r(F)].
```

The full denominator

```text
F_r(F)=r!tau(k)^2
```

contains the binomial interleaving of the two length-`k-1` component
factorizations.  In particular, its first factor chooses either component
with probability `(k-1)/(2k-2)=1/2`; adding a further `1/2` would destroy
normalization.  Also `F_r(L)=r!tau(2k-1)`.  Both channel laws have mass one,
so `sum_s beta_j(s)=0`.

The clean-room exact `k=3` reconstruction derives these coefficients both
from the displayed formulas and from the unconditional residual
factorization law divided by the channel probabilities.  The dictionaries
agree state by state.  It obtains `F_4(F)=54`, `F_4(L)=125`, and unit mass
on all four normalized source laws.

## 3. Positive cyclic compositions and owner intervals

List the support vertices in positive cyclic order as

```text
v_0=r, v_1=r+g_1, ..., v_(q-1)=r+g_1+...+g_(q-1),
```

where all gaps are positive and sum to `n`.  Rank compatibility with the
ambient long cycle permits exactly the forward triangle

```text
s_T=(v_0,v_1,v_2)
```

on three support vertices.  Its cycle notation has three possible starting
support vertices, so every supported triangle has exactly three
`(r,g)` representations.

On four cyclically ordered support vertices, the compatible double pairings
are

```text
s_S=(v_0,v_1)(v_2,v_3),
s_N=(v_0,v_3)(v_1,v_2).
```

For any fixed supported double, choosing each of its four support vertices
as anchor produces exactly one of `S,N`, alternating with the anchor.  Thus
the combined `S/N` sum represents every supported double exactly four
times.  The anchor `r` is already part of this enumeration; there is no
additional multiplicative factor `n`.

Let `I_i` be the `g_i-1` polygon-edge tails following `v_(i-1)` and ending
just before the edge whose head is `v_i`.  The latter edge is null because
its head belongs to the support.  Directly tracing `s^-1h` gives:

```text
T owners: I_1, I_2, I_3;             sizes g_1,g_2,g_3,

S owners: I_1, I_3, I_2 union I_4;   sizes g_1,g_3,g_2+g_4,

N owners: I_2, I_4, I_1 union I_3;   sizes g_2,g_4,g_1+g_3.
```

The intervals may be translated by `r`; circular overlaps are translation
invariant, which explains why M285 suppresses `r` inside `I_i(g)`.  Inserting
these owners into the rooted completion matrix gives M285's `R_K(g,ell)`.
The 3-to-1 and 4-to-1 maps therefore prove its formula `(2.5)` exactly.
The outer triangle/double label is retained.  Within each same-owner overlap,
the literal cyclic order of the two edge pairs partitions phases into
`IS/IN`; unequal owners give `X`.  This is a partition before summation, not
an inequality.

At `n=9`, the clean-room checker verifies 252 triangle representations and
1,008 double representations, covering 84 and 252 distinct states with
multiplicity three and four.  It also checks all 1,260 owner records and all
their admissible-lag responses against the direct residual cycles.

## 4. Rooted-owner autocorrelation and the size-two repair

Put

```text
a_d=tau(d-1)/tau(d),
b_d=tau(d-2)/tau(d),
delta_d=b_d-a_d^2,
A_s(x)=a_(d_owner(x)) on a generic phase and 0 otherwise.
```

Off the owner diagonal, `kappa_ab=a_(d_a)a_(d_b)`; on the diagonal,
`kappa_aa=b_(d_a)`.  Expanding the circular correlations therefore gives
the identity

```text
F_ell(s)=sum_x A_s(x)A_s(x+ell)
          +sum_i delta_(d_i) C_ii^s(ell).             (4.1)
```

The successive ratio is

```text
tau(d)/tau(d-1)=(d/(d-1))^(d-2).
```

For real `x>2`, the derivative of
`(x-2)log(x/(x-1))` equals

```text
log(1+1/(x-1))-(x-2)/[x(x-1)]>0.
```

Thus `tau` is log-convex and `delta_d>=0` for `d>=3`.  Explicitly,

```text
a_d=(1-1/d)^(d-2),
b_d=(1-1/d)(1-2/d)^(d-3).
```

Uniform Taylor remainder bounds for `1/d<=1/4` give

```text
log(b_d/a_d^2)=3/(2d^2)+O(d^-3),
delta_d=O(d^-2),
delta_d~3e^-2/(2d^2),
```

and the finitely many smaller `d` are absorbed in the constant.

At `d=2`, `a_2=1`, `b_2=0`, so `delta_2=-1`.  A residual owner of size two
has at most one generic polygon-edge tail: a one-run owner has one, while a
two-run owner has none.  Hence its autocorrelation `C_ii(ell)` vanishes for
every nonzero circular lag.  Deleting only the `d=2` correction changes
lag zero and no other lag.  In particular, for every admissible
`2<=ell<=n-2`, `(4.1)` equals exactly

```text
sum_x A_s(x)A_s(x+ell)
 +sum_(i:d_i>=3)delta_(d_i)C_ii^s(ell),
```

a sum of nonnegative autocorrelations with nonnegative Fourier spectrum
state by state.

## 5. What GOCI is—and is not

M285's positive-composition formula is exactly `eta_j(F_ell)`.  The repaired
response equals literal `F_ell` at every admissible lag.  Consequently, for
odd `k>=3` and `2<=ell<=3k-2`,

```text
GOCI_j  <=>  eta_j(F_ell)>=0  <=>  CP_j(k,ell-1)>=0,
```

because the M280/M283 prefactor is positive.  GOCI is therefore an exact
structural reformulation of OCI on the admissible lag set.  Its value is that
the responses are now explicit positive interval autocorrelations and every
remaining sign sits in `beta_j`; it is not a proof of their signed sum.
Nothing here establishes OS+, MS, FCL1, FD, a gap, or mixing.

## 6. Independent exact `k=3` obstruction

The checker imports no M285 or predecessor code/data.  It reconstructs both
source laws using exact `Fraction` completion counts, then independently
reconstructs the explicit beta laws and the literal/repaired owner responses.
All six admissible entries in each channel are strictly positive.  Thus the
finite row neither proves nor refutes GOCI.

For the repaired channel-two circular sequence `D_2`, set

```text
M_(ab)=D_2((b-a) mod 9),
v=(10,8,2,-5,-9,-9,-5,2,8).
```

Direct exact summation gives

```text
v^T M v=-310962953715709/12252303000000<0.
```

This exactly matches M285 and proves that its canonical signed repaired
channel-two sequence is not positive semidefinite.  It refutes only this
signed-PSD-dominance route.  The witness uses the repaired circular extension
outside the admissible lag set and is not a negative OCI value.

## 7. Audit conclusion

No normalization, multiplicity, interval, lag, or logical-scope defect was
found.  M285's strict GOCI reduction and the stated narrow PSD obstruction
are exact.  GOCI/OCI and all downstream claims remain open.

