# MPS/parent-Hamiltonian martingale audit

## 1. Exact audited claim and conventions

Use `(pq)(x)=p(q(x))`.  Put

```text
G=A_N,  M=binom(N,2),  E=T_N x T_N,
nu(e)=M^(-2),  p(t,u)=tu,  Q=p_*nu=P_T^2.
```

For `n>=2`, let `mathcal H_n=sum_{i=1}^{n-1}(I-P_i)` on `E^n`, where
`P_i` is exact conditional expectation given all coordinates outside
`{i,i+1}` and the ordered product `p(e_i)p(e_{i+1})`.  On the sector with
total product `h`, this is exactly the continuous-time microfactorized
fixed-endpoint `Q`-bridge Hamiltonian.

The following reduction is **proved**.

> There are universal `C<infinity` and integers
> `R_N<=C N log(N+1)` such that, for every `N>=3` and every `n>=R_N`,
>
> ```text
> Delta(mathcal H_n)
>   >= Delta(mathcal H_R_N)/(4(R_N-1)).                 (1.1)
> ```
>
> Moreover
>
> ```text
> Delta(mathcal H_l)
>   = min_{h:Q^l(h)>0} Lambda_N(l;e,h),                 (1.2)
> ```
>
> where `Lambda_N` is the full microfactorized local-Hamiltonian Poincare
> constant in the frozen M10 notation.

Thus this MPS route gives a stronger dependence on the long bridge length
than the frozen affine recursion, but it does **not** prove an inverse
polynomial in `N`: the finite base gap in (1.1) remains unbounded
quantitatively.

## 2. Exact local-projector and Peter--Weyl algebra

For `r>=1` and `g in G`, define the unnormalized fiber vector

```text
Phi_{r,g}
 = sum_{x in E^r: p(x_1)...p(x_r)=g}
       sqrt(nu^r(x)) |x>.
```

Its squared norm is `Q^r(g)`, and different endpoint fibers are orthogonal.
Consequently

```text
Pi_r = sum_{g:Q^r(g)>0}
         |Phi_{r,g}><Phi_{r,g}|/Q^r(g)                 (2.1)
```

is the orthogonal projector onto amplitudes of the form
`sqrt(nu^r(x)) f(p(x_1)...p(x_r))`.  Since `nu` is uniform on the expanded
alphabet `E`, `Pi_2` is literally the uniform same-product two-site heat
bath `P_i`; no non-unitary similarity is being hidden.  If one collapses
`E` to increments in `G`, the same statement has weights `Q(g)`, which is
why retaining the microfactor labels is the clean formulation.

Let `G-hat` be the inequivalent unitary irreducible representations of `G`
and set

```text
C^e = M^(-1) direct_sum_{rho in G-hat} rho(p(e)),
D_N = sum_{rho in G-hat} d_rho.                         (2.2)
```

For a block-diagonal boundary matrix `X=direct_sum X_rho`, the length-`r`
MPS amplitude is

```text
M^(-r) sum_rho Tr[X_rho rho(p(x_1)...p(x_r))].          (2.3)
```

Peter--Weyl says that the matrix coefficients in (2.3) span every function
on `G`; hence the MPS span in length `r` is exactly `range(Pi_r)`.

This tensor is block-normal.  Indeed, a minimal transposition factorization
of `g in A_N` has even length `N-c(g)`.  Pair its transpositions and pad by
`(t,t)` identity increments.  It follows that

```text
Q^ell(g)>0 for every g in A_N
when ell>=floor((N-1)/2).                               (2.4)
```

For each irreducible `rho`, products of `ell` physical matrices therefore
span `{rho(g):g in G}=M_{d_rho}` by Burnside's theorem.  Thus every block is
normal with injectivity length at most `floor((N-1)/2)`.  Inequivalent blocks
generate different matrix-coefficient spaces.

The local range is only two sites, below the automatic `ell+1` parent range
for large `N`.  Here that is not a mismatch, because the inherited
arbitrary-product aligned-`H_4` theorem proves that adjacent same-product
two-site replacements connect every feasible product fiber for every
`n>=2`.  Therefore

```text
ker(mathcal H_n)=range(Pi_n)                            (2.5)
```

for every `n>=2`: this is literally a block-normal parent Hamiltonian, not
only a weak parent Hamiltonian.

Finally, every local term preserves the total endpoint, so

```text
l2(E^n)=direct_sum_h l2({x:p(x_1)...p(x_n)=h}),
mathcal H_n=direct_sum_h mathcal H_{n,h}.               (2.6)
```

Connectivity makes the kernel in each feasible sector one-dimensional.
The smallest positive eigenvalue of the full direct sum is therefore the
minimum sector gap, proving (1.2).  Selecting one endpoint does not turn the
bulk tensor into a normal-MPS parent interaction: it is a global invariant
sector, not a tensor-product local restriction.  The block-normal theorem is
the applicable result.

## 3. Primary theorem audit

### Rozman--Molnar--Schuch (public July 2026 preprint)

Milán Ádám Rozmán, András Molnár, and Norbert Schuch,
"Lower Bounds on Spectral Gaps of Parent Hamiltonians via Tensor Networks,"
[arXiv:2607.19078v1](https://arxiv.org/abs/2607.19078), 21 July 2026.  The
cited source is public and was read in full; it is not an inaccessible or
not-yet-public citation.

- Theorem 3, equations (22)--(23), says that for the blocked parent
  Hamiltonian
  `Delta >= (1-2 gamma_{p,q}) Delta(tilde h)`.  It always retains the
  finite blocked-term gap `Delta(tilde h)`.
- Theorem 4, equation (25), computes the optimal `gamma_{p,q}` from a
  `D^4`-dimensional tensor expression `Xi` containing the pseudoinverse of
  the length-`2p+q` vertical Gram map.  This controls the angle, not the
  blocked local gap.
- Corollary 5 and Theorem 6 prove a positive gap uniform in chain length for
  each fixed normal or block-normal tensor.  They do not give a uniform
  lower bound for a family whose tensor and bond dimension grow with `N`.
- Appendix B, Theorem 7, equation (61), restates the FNW estimate
  `a(p)=Tr(rho_*^{-1}) ||T^p-T_infinity||`; even after the overlap is
  controlled, Theorem 3 still multiplies by a local finite-volume gap.
- Appendix B, Theorem 8, equation (85), gives the block-normal overlap bound
  with a sum over blocks and the inter-block overlap matrix.  It likewise
  only controls the angle.
- Appendix B, Theorem 9, equation (86), is the directly useful result here:
  if `gamma_{r,0}<1/sqrt(r)`, then for every chain length `n>=r`,

  ```text
  Delta(mathcal H_n)
   >= Delta(mathcal H_r)/(r-1)
      (1-sqrt(r) gamma_{r,0})^2.                        (3.1)
  ```

  This is the sum-of-projectors normalization, exactly the normalization of
  `mathcal H_n`; there is no random-scan factor in (3.1).

### Classical sources

M. Fannes, B. Nachtergaele, and R. F. Werner, "Finitely Correlated States on
Quantum Spin Chains," *Communications in Mathematical Physics* 144
(1992), 443--490,
[doi:10.1007/BF02099178](https://doi.org/10.1007/BF02099178).  Their Theorem
6.4 treats a purely generated/unique finitely correlated ground state and
gives a positive global gap in terms of a finite-volume gap and an
exponentially decaying projection-overlap error.  It is not directly the
factorially degenerate full endpoint ground space, and it retains the local
finite gap in any event.

Bruno Nachtergaele, "The Spectral Gap for Some Spin Chains with Discrete
Symmetry Breaking," *Communications in Mathematical Physics* 175 (1996),
565--606, [doi:10.1007/BF02099509](https://doi.org/10.1007/BF02099509),
[arXiv:cond-mat/9410110](https://arxiv.org/abs/cond-mat/9410110).  Its general
Theorem 3(i) gives

```text
gap >= gamma_{l+1}/d_{l+1}
       (1-epsilon_l sqrt(l+1))^2,                       (3.2)
```

under conditions C1--C3; Proposition 12, equations (6.10)--(6.11), gives
the block-degenerate GVBS specialization, again with the finite-volume gap
`gamma_{2m}`.  Rozman--Molnar--Schuch Appendix-B Theorem 9 is the modern MPS
restatement with the exact normalization used in (3.1).  None of these
classical results removes the base gap.

## 4. Exact identification and bound for `gamma_{r,0}`

On `E^{3r}`, write

```text
L = Pi_{2r} tensor I_r,
R = I_r tensor Pi_{2r},
G0 = Pi_{3r}.
```

The optimal overlap parameter is

```text
gamma_{r,0}=||LR-G0||.                                 (4.1)
```

This is the projection-angle identity used in RMS Theorem 4 and stated in
the proof of its Theorem 7.  All three projections preserve total product,
so (4.1) is the maximum over endpoint sectors `h`.

Inside the sector `h`, `L` is conditional expectation onto the raw right
tail of length `r`, `R` is conditional expectation onto the raw left tail,
and `G0` projects onto constants.  Thus (4.1) is exactly

```text
max_h rho(left raw r-tail, right raw r-tail
          | total product h).                          (4.2)
```

Let `a` be the product of the left tail and let `b` be the prefix product
after the middle segment.  The endpoint-conditioned boundary law is

```text
mu_h(a,b) proportional to
 Q^r(a) Q^r(a^(-1)b) Q^r(b^(-1)h).                     (4.3)
```

The raw tails form the Markov chain
`left tail -> a -> b -> right tail`, while `a` and `b` are functions of the
two raw tails (with `h` fixed).  Hence data processing in both directions
makes the maximal correlation in (4.2) equal to that of `(a,b)`.

Suppose

```text
max_g ||G| Q^r(g)-1| <= epsilon <1.                    (4.4)
```

The arbitrary-endpoint tilt calculation from frozen M10 applies to (4.3),
including outer weights with zeros, and gives

```text
gamma_{r,0}
 <= eta(epsilon)
 :=(4 epsilon+2 epsilon^2)/(1-epsilon)^2.               (4.5)
```

For `epsilon<=1/16`, `eta(epsilon)<=8 epsilon`.  Therefore

```text
epsilon <= 1/(16 sqrt(r))
 ==> gamma_{r,0} <= 1/(2 sqrt(r)).                      (4.6)
```

The parity-aware Diaconis--Shahshahani character sum audited in frozen M10
is bounded by `B exp(-2c)` for `N>10` at time
`r=(N/2)log N+cN` (the primary proof collects the zone estimates after its
equation (3.13)).  Take `c=A log(N+1)` with universal `A` large enough.
Then (4.4) is at most `1/(16 sqrt(r))`; enlarge `A` for the finitely many
`3<=N<=10`.  Nonnegative `Q` eigenvalues make the bound monotone at later
times.  This produces

```text
R_N <= C N log(N+1)                                    (4.7)
```

satisfying (4.6).  Substitution in (3.1) gives (1.1).

## 5. Probability, normalization, runtime, and size accounting

- The density-to-product-marginals error used in (4.5) is exactly
  `(4 epsilon+2 epsilon^2)/(1-epsilon)^2`; no stationary minimum mass enters
  that correlation estimate.
- `mathcal H_n` is the continuous sum of `n-1` projector terms.  The aligned
  nonlazy random scan has gap `Delta(mathcal H_n)/(n-1)`, paid once.  The
  inherited comparison to the original lazy `{3,4,5}` chain then pays its
  separate factor at most 12.
- The physical dimension is `|E|=M^2=O(N^4)`, but the chosen Peter--Weyl bond
  dimension obeys

  ```text
  D_N^2 >= sum_rho d_rho^2=|A_N|=N!/2.                 (5.1)
  ```

  In fact any MPS spanning all `|A_N|` endpoint ground states needs
  `D^2>=|A_N|` by rank.
- For the canonical fixed point in a block `rho`,
  `Tr(rho_*^{-1})=d_rho^2`.  Since the number of `A_N` irreducibles is
  `exp(O(sqrt N))`, at least one such factor is
  `|A_N|/exp(O(sqrt N))`.  The legacy FNW bound therefore has a factorial
  prefactor before transfer decay is used.
- RMS Section 4.4 reports `O(D^10)` construction and `O(D^12)` full
  diagonalization for `Xi` (or `O(D^6)` structured Krylov work).  These are
  not polynomial in `N` here.  The probabilistic proof of (4.5) avoids this
  computation.
- At the smoothing scale, `min_g Q^r(g)` is of order `1/|A_N|`; consequently
  the raw fiber normalization in (2.1), and the vertical-Gram pseudoinverse
  in RMS Theorem 4, can have factorial norm.  Exact projection/correlation
  cancellations avoid that loss, but a naive minimum-entry or pseudoinverse
  bound does not.
- Most importantly, every cited quantitative theorem retains
  `Delta(mathcal H_r)`.  Generic diagonalization acts on dimension
  `|E|^r` with `r=O(N log N)`, and supplies neither a polynomial proof nor a
  polynomial computation of this gap.

The exact block heat-bath sampler itself remains polynomial-time per step;
the MPS representation does not alter the chain or its implementation.

## 6. Dependencies and status

- **Proved here:** local projector formula (2.1), Peter--Weyl MPS span,
  block-normality and injectivity-length bound, endpoint direct sum,
  tail-correlation identity (4.2)--(4.3), and the deductions
  (4.5)--(4.7) and (1.1).
- **Proved inherited:** arbitrary-product aligned-`H_4` connectivity, which
  is the needed parent/intersection property; endpoint-tilt density lemma;
  the parity-aware Diaconis--Shahshahani pointwise character estimate; and
  the comparison from the aligned scan to `K`.
- **Cited with hypotheses checked:** RMS Theorems 3, 4, 6, 7, 8, and 9;
  FNW Theorem 6.4; Nachtergaele Theorem 3 and Proposition 12.
- **Empirical dependencies:** none.
- **Exact finite falsification only:** the local script described below.

## 7. First unproved standalone proposition

> **BASE-SCALE FIXED-ENDPOINT GAP.**  For the `R_N` in (4.7), there are
> universal `c>0,C<infinity` such that for every `N>=3`, every
> `2<=l<=R_N`, and every `h in A_N` with `Q_N^l(h)>0`,
>
> ```text
> Lambda_N(l;e,h) >= c(Nl)^(-C).
> ```

For long chains, Theorem 9 only needs the single base length `R_N`; the full
terminal theorem also includes all shorter lengths, hence the displayed
range.  This is the same quantitative obstruction identified by frozen M10,
not a new terminal proof.

## 8. Strongest self-attack and calibration

The main possible hypothesis failure was that a two-site weak parent
interaction below injectivity range could have extra zero modes.  Here this
would be exactly a disconnected arbitrary-product aligned-`H_4` fiber.  The
inherited arbitrary-product connectivity theorem rules it out.  If that
theorem were withdrawn, the MPS application would become conditional at this
precise point.

The large bond dimension and factorial Gram inverse do not refute the exact
angle estimate: (4.5) bypasses them.  Conversely, the constant angle does not
control the finite base gap, so using RMS Theorem 6's fixed-tensor existence
statement as an `N`-uniform polynomial bound would be invalid.

Boundary calibration:

- Original odd `m` is empty; the paired model concerns even `m=2n`.
- The requested regime `m>=4` is exactly `n>=2`, where the parent equality
  holds.  At `n=2` the only local term is a whole-sector heat bath and has
  sector Hamiltonian gap one.
- `N=2` is excluded and elementary.  `N=3,4` are covered by the finite-
  parameter enlargement in (4.7).
- The deterministic harness checked `N=3,4` and micro-lengths `n=2,3`
  (`m=4,6`).  It found one aligned component per feasible endpoint and exact
  local projector ranks.  These finite checks can falsify the algebra but
  cannot prove the universal result.

## 9. Artifacts and reproduction

Artifacts:

- `plan.md`
- `checkpoint.md`
- `local_projector_check.py`
- `results.json`
- this `report.md`

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
Python: 3.12.3.  The computation is deterministic.

```bash
python3 -m compileall experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/mps_lane/local_projector_check.py
python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/mps_lane/local_projector_check.py --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/mps_lane/results.json
```

## Verdict

**OPEN AT A NAMED STEP: BASE-SCALE FIXED-ENDPOINT GAP.**

