# Final resource audit: an applicable parent-Hamiltonian martingale reduction

Date: 2026-08-11  
Repository base: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## 1. Exact claim and conventions

Use `(pq)(x)=p(q(x))`.  Let `G=A_N`, `E=T_N^2`, `p(u,v)=uv`, and
give `E` its uniform law.  On `C[E]^tensor n`, let `Pi_i` be the exact
two-site same-product heat-bath projection and put

```text
H_(N,n)=sum_(i=1)^(n-1)(I-Pi_i).
```

For a feasible `h in G`, let `Lambda_N(n;h)` be the first positive
eigenvalue in the sector `p(a_1)...p(a_n)=h`, and set
`Lambda_N(n)=min_h Lambda_N(n;h)`.

**Proved reduction.**  There is a universal `C_0<infinity` and, for every
`N>=3`, an integer

```text
2<=r_N<=C_0 N log(N+1)                                (1)
```

such that, for every `n>=r_N`,

```text
Lambda_N(n)>=Lambda_N(r_N)/[4(r_N-1)].                 (2)
```

Consequently, if

```text
beta_N=min_(2<=l<=r_N) Lambda_N(l),
```

then `Lambda_N(n)>=beta_N/(4r_N)` for every `n>=2`.
This removes the frozen M10 recursion's polynomial loss in long bridge
length.  It is not Terminal A because an inverse-polynomial bound on
`beta_N` is still open.

## 2. Full proof

### 2.1 Exact Peter--Weyl parent interaction

For every irreducible complex representation `rho` of `G`, take

```text
A_rho^a=|E|^(-1/2)rho(p(a)),
A^a=direct_sum_(rho in G-hat) A_rho^a.                 (3)
```

Peter--Weyl says that the length-`l` MPS span `S_l`, as its boundary
matrices vary, consists exactly of amplitudes which are functions of the
ordered product `p(a_1)...p(a_l)`.  In particular, for
`F_z={(a,b):p(a)p(b)=z}`, an orthogonal basis of `S_2` is

```text
|F_z|^(-1/2) sum_((a,b) in F_z)|a,b>.
```

Thus the canonical projector onto `S_2` is literally `Pi_i`: the physical
index is an ordered transposition pair, so no microfactor multiplicity is
lost.

The tensor (3) is block-normal.  Its one-letter product support contains the
identity and all three-cycles.  Every element of `A_N` has an even minimal
transposition factorization of length at most the largest even integer not
exceeding `N-1`; pairing the factors and padding by identity letters shows
that every group element occurs at a common physical length at most
`floor((N-1)/2)`.  Burnside's theorem then makes each irreducible block span
its full matrix algebra, and inequivalent blocks have distinct Peter--Weyl
matrix-coefficient spaces.

By the inherited arbitrary-product aligned-`H_4` connectivity theorem, every
total-product fiber is connected under the local projections.  Hence, for
every `l>=2`,

```text
ker H_(N,l)=S_l.                                        (4)
```

This is a genuine block-normal parent Hamiltonian even though its interaction
range two may be shorter than an injectivity length.  It decomposes
orthogonally by endpoint, and (4) gives

```text
Delta(H_(N,l))=min_(feasible h) Lambda_N(l;h)
              =Lambda_N(l).                            (5)
```

Thus the degenerate endpoint ground space is handled rather than discarded.

### 2.2 The exact martingale theorem

Nachtergaele's general martingale estimate appears in B. Nachtergaele,
"The spectral gap for some spin chains with discrete symmetry breaking,"
*Communications in Mathematical Physics* **175** (1996), 565--606,
Section 2, Theorem 3(i),
[doi:10.1007/BF02099509](https://doi.org/10.1007/BF02099509),
[primary preprint](https://arxiv.org/pdf/cond-mat/9410110).  For a
nearest-neighbor block-normal MPS parent it is restated in the notation used
here as Theorem 9 of M. A. Rozman, A. Molnar, and N. Schuch, "Lower Bounds
on Spectral Gaps of Parent Hamiltonians via Tensor Networks,"
arXiv:2607.19078v1, Appendix B
([primary PDF](https://arxiv.org/pdf/2607.19078)):

```text
gamma_(r,0)<1/sqrt(r)
  implies
Delta(H_(N,n))
 >=Delta(H_(N,r))/(r-1)
      (1-sqrt(r)gamma_(r,0))^2       for every n>=r.    (6)
```

Both sources use the unnormalized sum of local Hamiltonian terms.  Thus
there is no hidden random-scan factor in (6).  The theorem permits the
block-normal degenerate ground space in (4).

### 2.3 The martingale angle is a bridge-tail correlation

The nontrivial principal-angle norm `gamma_(r,0)` in (6) is formed from two
length-`2r` ground projections whose intervals overlap on `r` sites.  The
projections preserve total product, so decompose into feasible endpoint
sectors.  In a length-`3r` `h`-bridge, write the three `r`-letter words as
`L,M,R`.  Within that sector, one projection has range the functions of
`R`, the other has range the functions of `L`, and their intersection is
the constants.  The two-projection characterization of maximal correlation
therefore gives

```text
gamma_(r,0)
 =max_h rho_max(L,R | p(L)p(M)p(R)=h).                 (7)
```

If `x=p(L)` and `z=p(R)`, summing the middle word gives kernel

```text
Q_N^r(x^(-1) h z^(-1)).                                (8)
```

After the bijection `z->h z^(-1)`, this is a translate of `Q_N^r`.
Moreover `L->x->z->R` is Markov while `x,z` are functions of the raw tails,
so data processing in both directions shows that raw-tail and boundary
maximal correlations are equal.  This explicitly handles microfactor labels
and arbitrary sparse endpoints.

Suppose

```text
max_(x,y in G) ||G|Q_N^r(x,y)-1|<=epsilon<1.            (9)
```

The exact endpoint-tilt density calculation audited in M10 gives

```text
gamma_(r,0)
 <=eta(epsilon):=(4epsilon+2epsilon^2)/(1-epsilon)^2.  (10)
```

If `epsilon<=1/(16sqrt(r))` and `r>=2`, then

```text
eta(epsilon)
 <=(33/8)(256/225)epsilon
 <1/(2sqrt(r)).                                        (11)
```

### 2.4 A universal `r_N=O(N log N)`

The checked Diaconis--Shahshahani character estimate gives a positive
majorant for the left side of (9).  Their Section 3 collection is at most a
universal constant times `exp(-4c)` at

```text
s=(N/2)log N+cN,       N>10, c>0.
```

The exact parity translation is the one audited in the frozen M10 report:
the trivial/sign pair produces uniform measure on `A_N`, conjugate
partitions pair, and `Q_N^s=P_(T_N)^(2s)`.  Choose a sufficiently large
universal `C_0` and set `r_N=ceil(C_0Nlog(N+1))`.  Then the corresponding
`c` is a large multiple of `log(N+1)`, so the relative pointwise error is at
most `1/(16sqrt(r_N))`.  Enlarging `C_0` handles the finite irreducible,
aperiodic walks `3<=N<=10`.  Equations (10)--(11) give

```text
gamma_(r_N,0)<=1/(2sqrt(r_N)).                          (12)
```

Substitution of (5) and (12) into (6) proves (1)--(2).

## 3. Probability, runtime, path, and congestion accounting

- Pointwise middle-kernel error: at most `1/(16sqrt(r_N))`.
- Principal angle: at most `1/(2sqrt(r_N))`.
- Martingale loss: exactly at most `4(r_N-1)` in Hamiltonian normalization.
- Aligned random scan: `gap(B_(N,n))=Lambda_N(n;e)/(n-1)`.
- Full-chain comparison for original length `m=2n>=6`:
  `gap(K_(N,m))>=gap(B_(N,n))/12`.
- No canonical path, routing hub, or congestion estimate is used.
- The theorem is analytic.  The current Rozman--Molnar--Schuch exact `Xi`
  computation is polynomial in MPS bond dimension, but here
  `D=sum_rho dim(rho)>=sqrt(|A_N|)`, hence is not a polynomial-time algorithm
  in `N`.  This does not affect the analytic angle bound (10).
- Exact local heat-bath sampling retains its inherited polynomial per-step
  cost.

## 4. Dependencies

- **Cited and checked:** Nachtergaele Section 2, Theorem 3(i), including
  local-gap denominator and unnormalized Hamiltonian convention.
- **Cited and checked:** Rozman--Molnar--Schuch arXiv:2607.19078v1,
  definitions of normal/block-normal MPS, Theorems 3--4, and Appendix B
  Theorem 9.
- **Cited and previously checked:** Diaconis--Shahshahani Lemma 14 and the
  Section 3 partition-zone estimates, with the `A_N,Q_N` translation.
- **Proved here:** Peter--Weyl local-projector identification, block
  normality, endpoint direct sum, bridge-tail angle identity, and (10)--(12).
- **Inherited proved:** arbitrary-product aligned-`H_4` connectivity and the
  exact `K`-to-`B` Dirichlet comparison.
- **Empirical dependency:** none.  The exact finite harness below is only
  falsification evidence.

## 5. First unproved standalone proposition

> **BASE-SCALE PARENT GAP.**  There exist universal `c>0,C<infinity` such
> that for every `N>=3`, every `2<=l<=r_N`, and every feasible `h in A_N`,
> `Lambda_N(l;h)>=c(Nl)^(-C)`.

This is the same growing `O(Nlog N)` base window exposed by M10, now without
any additional power loss in longer bridge length.

## 6. Strongest self-attack

The result takes the minimum over all feasible endpoints because a local
subinterval of an identity bridge can have an arbitrary feasible endpoint.
Qualitative connectivity does not control its gap.  The general spanning-tree
bound `Lambda_N(l)>=2M^(-(4l+4))`, inserted at
`l=Theta(Nlog N)`, is superpolynomially small and does not close the theorem.

Generic MPS estimates do not remove this term.  Rozman--Molnar--Schuch
Theorem 3 multiplies the angle factor by the finite blocked-term gap; Theorem
4 computes the angle but has superpolynomial bond dimension here.  Classical
FNW transfer estimates contain fixed-point condition factors such as
`Tr(rho^(-1))`, and crude pseudoinverse or minimum bridge-mass bounds pay at
least factorial-scale parameters.  Thus (2) is a genuine reduction, not a
disguised proof of the base estimate.

## 7. Calibration

- Odd original `m`: empty.  `m=0` and `N=2` are singleton boundaries.
- Grouped `n=1` is original `m=2`, with no aligned site and excluded.
- Grouped `n=2` is original `m=4`; its sole parent term is a whole-word heat
  bath, with Hamiltonian gap one in every feasible sector.  Its coefficient
  in the lazy full `K` is `1/4`.
- The 27 `S_3,m=4` and 120 `S_4,m=4` words agree with the whole-fiber case.
  The 3,936 `S_4,m=6` words and 17 pure-Hurwitz components do not contradict
  the connected aligned parent fiber.
- Sparse endpoints are included in (10).  Near-minimal doubled-tree words,
  repeated-edge hubs, color interleavings, and the false raw length-two
  simulation are not used.
- A deterministic check at `N=3,4`, grouped `n=2,3`, found one aligned
  component per feasible endpoint and verified the local projector and
  regular-representation product basis exactly.  It can refute these finite
  algebra claims but cannot prove the universal theorem.

## 8. Artifacts, reproduction, and primary citations

Main artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/mps_parent_checkpoint.md
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/mps_parent_hamiltonian_audit.md
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/mps_lane/plan.md
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/mps_lane/checkpoint.md
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/mps_lane/report.md
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/mps_lane/local_projector_check.py
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/mps_lane/results.json
```

Reproduce the deterministic finite audit with Python 3.12.3:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/mps_lane/local_projector_check.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/mps_lane/results.json
```

Primary sources are linked in Section 2.2.  The pointwise walk input is
P. Diaconis and M. Shahshahani, "Generating a Random Permutation with Random
Transpositions," *Z. Wahrscheinlichkeitstheorie verw. Gebiete* **57**
(1981), 159--179,
[doi:10.1007/BF00535487](https://doi.org/10.1007/BF00535487).

## 9. Verdict

**PROVED.**

This verdict is for the uniform-in-length parent-Hamiltonian reduction
(1)--(2).  The base-scale proposition in Section 5 remains open, so this is
nonterminal.
