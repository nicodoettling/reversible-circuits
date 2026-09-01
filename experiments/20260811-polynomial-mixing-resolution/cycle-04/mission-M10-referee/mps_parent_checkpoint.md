# Checkpoint: Peter--Weyl parent Hamiltonian and martingale reduction

Status: proof assembled and independently confirmed; see
`mps_lane/report.md` and the final resource audit.

## 1. Exact object

Use `(pq)(x)=p(q(x))`.  Put `G=A_N`, `E=T_N^2`, and
`p(u,v)=uv`.  Give `E` the uniform measure, so the image law on `G` is
`Q_N=P_(T_N)^2`.  On `C[E]^tensor n`, let `Pi_[i,i+1]` be the orthogonal
projection which replaces the two physical letters by the uniform law on
their same-product fiber.  Define the unnormalized aligned Hamiltonian

```text
mathcal H_(N,n)=sum_(i=1)^(n-1)(I-Pi_[i,i+1]).          (1)
```

It preserves each total-product sector.  Let `Lambda_N(n;h)` be its first
positive eigenvalue in the feasible sector `p(a_1)...p(a_n)=h`, and let
`Lambda_N(n)=min_h Lambda_N(n;h)`.

## 2. The heat-bath projector is an exact MPS parent term

For every irreducible complex representation `rho` of `G`, define the
physical matrices

```text
A_rho^a=|E|^(-1/2) rho(p(a)),       a in E,
A^a=direct_sum_(rho in G-hat) A_rho^a.                 (2)
```

For a boundary matrix `X=direct_sum X_rho`, the corresponding length-`l`
MPS amplitude at `(a_1,...,a_l)` is a linear combination of matrix
coefficients of

```text
p(a_1)...p(a_l).
```

Peter--Weyl therefore shows that its span `S_l` is exactly the space of
vectors whose amplitude is a function only of that ordered product (on the
products feasible at length `l`).  In particular, if

```text
F_z={(a,b) in E^2:p(a)p(b)=z},
```

then `S_2` has orthogonal basis

```text
|phi_z>=|F_z|^(-1/2) sum_((a,b) in F_z)|a,b>,
```

and the canonical parent projector onto `S_2` is precisely the two-site
same-product heat bath `Pi` in (1).  Keeping `a=(u,v)` as the physical
letter is important: it retains all ordered-transposition microfactor
multiplicities, and their pushforward in the transfer operator is exactly
`Q_N`.

Each block in (2) is normal.  Indeed `p(E)` contains the identity and all
three-cycles, hence generates `A_N`; after a common finite exact word length,
its products contain every element of `G`.  Burnside's theorem then says
that the matrices in each irreducible block span its full matrix algebra.
The identity letter pads shorter words.  Inequivalent blocks generate
distinct matrix-coefficient spaces once all group elements occur.  Thus
(2) is block-normal (equivalently it is the Peter--Weyl resolution of the
regular/G-injective construction).

The inherited arbitrary-product aligned-`H_4` connectivity theorem implies

```text
ker mathcal H_(N,l)=S_l,       l>=2.                    (3)
```

Indeed a zero-energy function is constant on every local same-product move
component, and those components are exactly the total-product fibers.
Consequently (1) is a genuine two-site block-normal parent Hamiltonian, not
merely a weak parent Hamiltonian.  It decomposes orthogonally over `h`, so

```text
Delta(mathcal H_(N,l))=Lambda_N(l).                     (4)
```

The large ground-space degeneracy is therefore handled exactly; a lower
bound on (4) applies in particular to the identity sector.

## 3. Exact martingale theorem

B. Nachtergaele, "The spectral gap for some spin chains with discrete
symmetry breaking," *Commun. Math. Phys.* **175** (1996), 565--606,
Section 2, Theorem 3(i)
([primary preprint](https://arxiv.org/pdf/cond-mat/9410110)), proves the
general martingale estimate under its conditions C1--C3.  For a
nearest-neighbor block-normal parent Hamiltonian, the specialization is
restated explicitly as Theorem 9 of M. A. Rozman, A. Molnar, and N. Schuch,
"Lower Bounds on Spectral Gaps of Parent Hamiltonians via Tensor Networks,"
arXiv:2607.19078v1, Appendix B
([primary PDF](https://arxiv.org/pdf/2607.19078)):

```text
if gamma_(r,0)<1/sqrt(r), then, for every l>=r,

Delta(mathcal H_(N,l))
 >= Delta(mathcal H_(N,r))/(r-1)
       (1-sqrt(r) gamma_(r,0))^2.                       (5)
```

Here `gamma_(r,0)` is the nontrivial principal-angle norm of the two local
ground spaces on two length-`2r` intervals overlapping in `r` sites.  In the
notation of Rozman--Molnar--Schuch Theorem 4, it is also the square root of
the largest eigenvalue below one of their `Xi` matrix.  Equation (5) uses
the unnormalized sum of local Hamiltonian terms, exactly as (1); there is no
random-scan factor in (5).  It allows block-normal/degenerate ground spaces.

The current 2026 theorem also gives an exact way to compute `gamma`, but its
cost is polynomial in the MPS bond dimension.  For (2),

```text
D=sum_rho dim(rho) >=sqrt(|A_N|),
```

so that advertised computation is not polynomial in the project parameter
`N`.  The analytic estimate below avoids that computation.

## 4. Exact bound on the martingale angle

Both ground projections in `gamma_(r,0)` preserve total product, so their
angle decomposes over a feasible endpoint `h`.  In an `h`-sector of a
length-`3r` bridge, write the three consecutive `r`-letter words as
`L,M,R`.  The first interval ground range consists of functions of `R`, the
second of functions of `L`, and their intersection consists of constants in
that sector.  The standard two-projection characterization therefore gives

```text
gamma_(r,0)=sup_h rho_max(L,R | p(L)p(M)p(R)=h).        (6)
```

This also proves that retaining physical microfactor labels introduces no
extra angle.

Let `x=p(L)` and `z=p(R)`.  Summing the middle word gives the boundary
kernel

```text
Q_N^r(x^(-1) h z^(-1)).                                (7)
```

After the bijection `z -> h z^(-1)`, this is a translate of `Q_N^r`.
Moreover `L -> x -> z -> R` is Markov and `x,z` are functions of their
respective tails, so the tail and boundary maximal correlations are equal.

Suppose

```text
max_(x,y in G)||G|Q_N^r(x,y)-1|<=epsilon<1.             (8)
```

The exact arbitrary-tilt calculation from the frozen M10 theorem applies to
(7), including sparse endpoint weights, and yields

```text
gamma_(r,0)
 <=eta(epsilon):=(4epsilon+2epsilon^2)/(1-epsilon)^2.   (9)
```

For `epsilon<=1/(16 sqrt(r))` and `r>=2`, use
`epsilon<=1/16` in (9) to obtain

```text
eta(epsilon)
 <=[(33/8)(256/225)]epsilon
 <1/(2 sqrt(r)).                                       (10)
```

This strictly meets the hypothesis of (5).

## 5. Choosing a polynomial overlap length

The checked Diaconis--Shahshahani partition-zone estimates imply a universal
constant `C` such that, for `N>10` and

```text
s=(N/2)log N+cN,
```

the positive character majorant for the relative pointwise error of
`Q_N^s` is at most `C exp(-4c)`.  This is the same parity/character
translation audited in the frozen M10 report, now with `c` allowed to grow.
Choose a sufficiently large universal `C_0` and set

```text
r_N=ceil(C_0 N log(N+1)).                               (11)
```

Then `c=r_N/N-(1/2)log N` is a sufficiently large multiple of
`log(N+1)` that (8) is at most `1/(16 sqrt(r_N))`.  For the finitely many
`3<=N<=10`, irreducibility, the identity holding probability, and an
increase of the same `C_0` give the same conclusion.  Thus

```text
r_N<=C_1 N log(N+1),
gamma_(r_N,0)<=1/(2 sqrt(r_N)).                         (12)
```

No total-variation-to-pointwise inference is used: (8) comes from Fourier
inversion and the Diaconis--Shahshahani Plancherel sum.

Combining (4), (5), and (12) proves the proposed stronger reduction

```text
Lambda_N(l)>=Lambda_N(r_N)/[4(r_N-1)]
                                                for all l>=r_N. (13)
```

Equivalently, with

```text
beta_N=min_(2<=j<=r_N) Lambda_N(j),
```

one has

```text
Lambda_N(l)>=beta_N/(4r_N)       for every l>=2.       (14)
```

For the random-scan aligned bridge `B`, the only further loss is exactly
`1/(l-1)`.  For the full local chain on `m=2l>=6`, the audited comparison
then loses at most another factor `12`.

## 6. Smallest remaining implication and self-attack

The first unproved proposition is:

> **BASE-SCALE PARENT GAP.**  There exist universal `c>0,C<infinity` such
> that for every `N>=3`, every `2<=l<=r_N`, and every feasible endpoint
> `h in A_N`, `Lambda_N(l;h)>=c(Nl)^(-C)`.

The martingale theorem cannot create this base gap.  The elementary spanning
tree bound `Lambda_N(l)>=2 M^(-(4l+4))` at
`l=Theta(N log N)` is exponentially small in a polynomial of `N`, so
substituting it into (13) is nonresponsive.  Rozman--Molnar--Schuch Theorem
4 still multiplies its angle factor by the finite blocked-term gap, and its
exact matrix computation has superpolynomial bond dimension here.  Thus the
new result removes the recursive power loss in long bridge length but does
not prove Terminal A.

The strongest possible failure of this checkpoint is an indexing or
identification error between the `gamma_(r,0)` in (5) and the two conditional
projections in (6).  That is the focus of the pending independent audit.

## 7. Calibration

- `N=2` is singleton and outside the statement; odd original word lengths
  are empty.
- Grouped length one is the excluded `m=2` case with no local term.
- Grouped length two (`m=4`) has one whole-word parent projector; every
  endpoint sector has Hamiltonian gap one.  In the full lazy `K`, that
  projector has coefficient `1/4`.
- The 27 `S_3,m=4` and 120 `S_4,m=4` words agree with that whole-fiber
  description.  The 3,936 `S_4,m=6` words may occupy 17 pure-Hurwitz
  components, but the aligned parent fiber is connected.
- Sparse endpoints are allowed in (9).  Near-minimal words, repeated-edge
  hubs, color interleavings, and the false length-two local simulation are
  not used.
- The statement is polynomial in `N` and bridge length, not in `log N`.

## 8. Checkpoint verdict

**PROVED AS A NONTERMINAL REDUCTION.**  The independent audit accepted
(5)--(6); the base-scale fixed-endpoint gap remains open.
