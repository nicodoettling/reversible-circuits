# M04 final report: color-interleaving projection

## 1. Exact claim with all quantifiers and conventions

Use maps on `[N]` and multiplication `(pq)(x)=p(q(x))`; evaluate a word as
`t_1...t_m`.  Put

```text
M = binom(N,2),
R_m = {r in {3,4,5}: r<=m},
B = |R_m|,
K = (1/2)I
  + (1/(2B)) sum_{r in R_m} (1/(m-r+1)) sum_i H_{i,r}.
```

Fix `N>=3`, even `m>=4`, and any feasible labeled weighted
support-component datum

```text
alpha=((C_a,k_a): a in A),   sum_a k_a=m.
```

The sets `C_a` are the nontrivial labeled support components and `k_a` is
the number of factors supported on `C_a`.  Let `Omega_alpha` be the
corresponding macro-fiber and let `K^alpha` be the standard rejected-exit
restriction:

```text
K^alpha(x,y)=K(x,y)                         for distinct x,y in Omega_alpha,
K^alpha(x,x)=K(x,x)+K(x,Omega\Omega_alpha).
```

Let `chi` record only the component color of every factor, and let
`Kbar_col^alpha` be the stationary-flow projection of `K^alpha` through
`chi`.

**Theorem (proved).**  If at least two colors occur, then

```text
gap(Kbar_col^alpha)
 >= [1-cos(pi/m)]/[B (m-2) M^2]
 >= 2/[3 m^3 M^2]
 >= 8/[3 N^4 m^3].                                  (1.1)
```

If one color occurs, the projected state space is a singleton; its Poincare
gap is set to one.  The bound is uniform in the number of components, their
sizes and weights, including rare colors and near-minimal connected words.
It proves the assigned color-projection claim, not the gap of `K^alpha` or
of the global chain.

## 2. Full argument

### 2.1 Exact conditional product structure

For every `a`, let `X_a` be the set of connected-support identity
transposition words of length `k_a` on the fixed labeled set `C_a`.  Let

```text
I_alpha={sigma in A^m: color a occurs k_a times}.
```

There is a bijection

```text
Psi: I_alpha x product_a X_a -> Omega_alpha.          (2.1)
```

Scan `sigma` from left to right and at each occurrence of `a` take the next
factor of the word in `X_a`.  Factors belonging to distinct components have
disjoint supports and commute, so the resulting interleaving still has
product identity.  Conversely, the color word and the within-color
subsequences are recovered uniquely from a word in `Omega_alpha`.

Consequently the uniform conditional law `pi_alpha` is the product of the
uniform law on `I_alpha` and the uniform laws on the `X_a`.  In particular,
if

```text
D_alpha=product_a |X_a|,
```

then every color fiber has size `D_alpha` and the projected stationary law
`pibar` is uniform on `I_alpha`.

For color words `sigma,tau`, the stationary-flow transition is exactly

```text
Kbar_col^alpha(sigma,tau)
 = (1/D_alpha) sum_{z in product_a X_a}
       K^alpha(Psi(sigma,z), chi^{-1}(tau)).           (2.2)
```

All lower bounds below are applied inside this exact average; no
renormalized proposal chain is substituted for the rejected-exit
restriction.

### 2.2 Every adjacent unequal-color swap is an actual `H_3` outcome

Fix `sigma` and an adjacent pair `j,j+1` whose colors are distinct.  For a
fixed internal tuple `z`, write the actual factors in these positions as
`p,q`.  Since their support components are disjoint,

```text
pq=qp.                                                 (2.3)
```

Use the following boundary-safe padding.

- If `j<=m-2`, take the length-three window beginning at `j`.  If its block
  is `(p,q,s)`, use the target `(q,p,s)`.
- If `j=m-1`, take the window beginning at `m-2`.  If its block is
  `(s,p,q)`, use the target `(s,q,p)`.

Equation (2.3) shows that the target triple has exactly the same ordered
product as the current triple.  It has the adjacent-swapped color word and
the same within-color subsequences, so it lies in `Omega_alpha` and is not
rejected.

For every triple product `h`,

```text
F_3(h)<=M^2,                                           (2.4)
```

because after the first two transpositions are chosen, the third
permutation is uniquely determined; only some choices make it a
transposition.  The exact heat bath therefore chooses the specified target
with probability at least `M^{-2}`.  Including laziness, block-size choice,
and the `m-2` length-three windows gives

```text
K^alpha(Psi(sigma,z),Psi(S_j sigma,z))
 >= beta,
beta = 1/[2B(m-2)M^2].                                (2.5)
```

This holds for every `z`, so (2.2) yields

```text
Kbar_col^alpha(sigma,S_j sigma)>=beta                 (2.6)
```

whenever the two colors differ.

There is no hidden duplicate-target loss.  Two distinct adjacent unequal
swaps cannot produce the same off-diagonal word.  For disjoint pairs this is
seen at the first changed position; for overlapping pairs, equality of
`(b,a,c)` and `(a,c,b)` would force `a=b`.  Any additional heat-bath target
or alternative window yielding the same projected state is aggregated in
(2.2) and only increases its transition probability.

### 2.3 Adjacent multiset walk and its exact gap

Define the lazy adjacent-transposition chain on `I_alpha` by

```text
Q = (1/2)I + [1/(2(m-1))] sum_{j=1}^{m-1} S_j,         (2.7)
```

where `S_j` swaps positions `j,j+1`; equal colors give a self-loop.  Each
`S_j` is an involution, so `Q` is reversible for the uniform law.

The labeled version of (2.7) is the half-lazy interchange process on the
path with `m` vertices.  The continuous-time unit-edge-rate path random walk
has first nonzero eigenvalue

```text
2[1-cos(pi/m)].                                        (2.8)
```

Caputo--Liggett--Richthammer, Theorem 1.1, proves that the interchange
process has the same gap as this one-particle walk.  Their colored exclusion
corollary, equation (4.2), applies directly to arbitrary fixed color
multiplicities.  Converting the unit-rate generator to (2.7) gives

```text
gap(Q)=[1-cos(pi/m)]/(m-1)                             (2.9)
```

for every nontrivial content vector.  Equivalently, this follows by viewing
`Q` as a quotient of the labeled interchange process; quotienting cannot
decrease the Poincare gap.  Thus a color of multiplicity two, or even one in
the abstract quotient, causes no loss.  The cited primary source is:

- Pietro Caputo, Thomas M. Liggett, Thomas Richthammer,
  [*Proof of Aldous' spectral gap conjecture*](https://arxiv.org/abs/0906.1238),
  JAMS 23 (2010), Theorem 1.1 and Section 4.

### 2.4 Dirichlet comparison

Every off-diagonal transition of `Q` has probability `1/[2(m-1)]`.
Equations (2.5)--(2.6) therefore imply the entrywise off-diagonal and
Dirichlet-form domination

```text
Kbar_col^alpha >= rho Q,
E_Kbar(f,f) >= rho E_Q(f,f),
rho = 2(m-1)beta
    = (m-1)/[B(m-2)M^2].                               (2.10)
```

Combining (2.9) and (2.10) proves the first inequality in (1.1).  Finally,

```text
1-cos(pi/m)=2 sin^2(pi/(2m)) >= 2/m^2,
B<=3,  m-2<=m,  M<=N^2/2,
```

which proves the other displayed bounds.

### 2.5 What a second decomposition would and would not give

Applying the accepted JSTV decomposition theorem to `K^alpha`, partitioned
by exact color word, gives formally

```text
gap(K^alpha)
 >= (1/3) gap(Kbar_col^alpha)
       min_sigma gap((K^alpha)^sigma),                 (2.11)
```

where `(K^alpha)^sigma` is again the standard rejected-exit restriction,
now to one exact color word.  This is an exact two-stage inequality, but its
minimum can be zero.

Here is a concrete obstruction.  Take `N=5,m=24` with components

```text
C_A={1,2,3}, k_A=4;       C_B={4,5}, k_B=20,
sigma=(A B B B B B)^4.
```

There are 24 connected identity words of length four on `C_A`, while the
word on the two-label component `C_B` is unique.  Thus the fixed-color
subfiber has 24 states.  Every allowed window has length at most five and
contains at most one `A`.  In an update that retains the exact color word,
equality of products splits in the direct product `S_{C_A} x S_{C_B}`.  A
window containing one `A` must therefore retain that single `A`
transposition, while every `B` factor is the unique transposition on `C_B`.
Hence the fixed-color restriction is the identity kernel on 24 states and
has gap zero.

This does not contradict (1.1): full `K^alpha` can first swap colors and
bring occurrences of `A` together.  It shows that a naive iteration of JSTV
over exact color words cannot prove the full macro-fiber gap.

## 3. Probability, runtime, path length, and congestion accounting

- Worst specified padded-swap probability:
  `beta=1/[2B(m-2)M^2]`.
- At `m=4`, `B=2`, so `beta=1/(8M^2)` and
  `rho=3/(4M^2)`.  The `r=4` whole-word heat bath remains present with
  coefficient `1/4`; it is not discarded or charged negatively.
- At even `m>=6`, `B=3`, so `beta=1/[6(m-2)M^2]`.
- Every reference transition uses one actual `K` transition: path length
  one.  The comparison congestion is at most
  `rho^{-1}=B(m-2)M^2/(m-1)<=3M^2`; no canonical state or hub is used.
- Projection averaging spreads the reference flow over all
  `D_alpha` internal tuples rather than concentrating it.
- Exact block sampling has polynomial cost independently of the comparison.
  A brute-force exact sampler enumerates at most `M^(r-1)<=M^4` prefixes for
  `r<=5`, computes the forced last permutation, and samples uniformly from
  the valid list.  The relevant `r=3` enumeration uses at most `M^2`
  prefixes.  The promoted direct `r=4,5` samplers are faster but are not
  needed for polynomiality.

## 4. Dependencies

- **Proved here:** the macro-fiber/color/internal-word bijection in the form
  needed for stationary flow; padded adjacent swap; `F_3<=M^2`; exact kernel
  normalization; transition aggregation; Dirichlet comparison; endpoint and
  `m=4` audits; fixed-color zero-gap example.
- **Previously proved project input:** conditional macro-fiber factorization
  and reversibility of exact heat baths and rejected-exit restrictions.
- **Cited and convention-checked:** Caputo--Liggett--Richthammer Theorem 1.1
  and colored exclusion equation (4.2).  Their chain is continuous time; the
  factor `1/[2(m-1)]` converting it to (2.7) is derived explicitly above.
- **Cited/accepted durable project input:** JSTV's factor-three
  projection/restriction inequality, used only for the non-closing statement
  (2.11).
- **Empirical dependencies:** none.

## 5. First unproved step

**Uniform macro-fiber gap proposition.**  Prove universal constants `c>0`
and `C<infinity` such that for every feasible `alpha`,

```text
gap(K^alpha) >= c (Nm)^(-C).
```

The color projection is no longer the missing part.  Exact-color
restrictions can be reducible, so the proposition needs a decomposition that
allows color rearrangement and internal refresh to cooperate, or a direct
quantitative bound for the already inherited Hurwitz/full-restriction
comparison.

## 6. Strongest self-attack

The theorem controls only functions constant on internal-word fibers.  It
does not bound modes coupling a slowly changing connected factorization to
the positions of its colors.  Equation (2.11) cannot repair this because the
explicit `(N,m)=(5,24)` fixed-color restriction has gap zero.  Therefore the
new polynomial color gap is a genuine constituent result but neither a proof
of the full restricted-fiber gap nor evidence against an internal
superpolynomial bottleneck.

The one-edge comparison also uses all-transposition support critically:
different labeled support components give disjoint transpositions that
commute.  It does not automatically transfer to a restricted gate library.

## 7. Calibration suite

- Odd `m`: `Omega(N,m)` is empty; theorem not asserted.
- `m=0`: singleton global state; theorem not asserted.
- `N=2`, even `m`: singleton state/color projection.
- `m=2,N>=3`: excluded; `r=3` is unavailable and the displayed
  normalization deliberately does not extend to it.
- `S_3,m=4`: every feasible macro-fiber has one nonzero component color, so
  the color projection is a singleton.  The 27 global words and four
  Hurwitz components are consistent with, but not used by, the theorem.
- `S_4,m=4`: two-disjoint-edge macro-fibers have content `(2,2)` and are
  covered by the adjacent-swap proof; one-color fibers are trivial.  The
  whole-word `H_4` term has coefficient `1/4` and is retained.
- `S_4,m=6`: contents such as `(2,4)` are covered uniformly; no lower bound
  depends on balanced colors.
- Near-minimal connected components: the swap retains each internal word
  exactly, so no square, surplus, or internal Hurwitz opportunity is assumed.
- Disjoint components commute, but their nontrivial ordered interleaving is
  precisely the state space of `Q`; it is not collapsed.
- A fixed canonical hub is never used.

## 8. Artifacts and reproduction

Artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-02/
  mission-M04-color-interleaving/plan.md
  mission-M04-color-interleaving/checkpoint.md
  mission-M04-color-interleaving/report.md
```

No computation was used, so there is no random seed or raw-output file.  The
argument is reproduced by checking equations (2.1)--(2.10); the fixed-color
obstruction is the explicit finite construction in Section 2.5.

## 9. Verdict

PROVED

This verdict applies exactly to the stationary-flow color-interleaving
projection claim in Section 1.  The global polynomial-mixing goal and the
full macro-fiber restriction gap remain open.
