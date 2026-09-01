# M54 halfway checkpoint: root quotient accepted, mean lift isolated

Date: 2026-08-11.  Permutations compose as `(pq)(x)=p(q(x))`;
factor tuples multiply left-to-right.  The chain in this note is the full
nonlazy adjacent-rank-two stationary-flow parking projection `Pbar_r` in
the minimal factorization sector of `(0 1 ... r)`.  Nothing below is a
claim for the original identity-word chain `K`.

## 1. Fresh referee verdicts

### 1.1 ACCEPT: M50 root-composition theorem

I independently checked the current theorem note
`root_composition_projection.md` (SHA-256
`ca1e71b814f75155fd508f49d26f81ee65d5d4af4318d40dd7cf7a1674a3338e`).
There is no numbered objection.

For an ordered root composition `a=(a_1,...,a_k)`, put

```text
Z_s=(s+1)^(s-1)/s!,  w_a=Z_(a-1)=a^(a-1)/a!,
alpha_r=2/[3r(r-1)].
```

The root weight is `1/k!`, and deleting the root edges gives independent
branch weights `Z_(a_i-1)`.  Hence

```text
rho_r(a)=Z_r^(-1)(k!)^(-1) product_i w_(a_i).
```

For a fixed child boundary of a vertex of degree `d_h`, the chosen two
lower-`h` occurrences are adjacent in exactly the fraction

```text
binom(r-1,d_h-1)/binom(r,d_h)=d_h/r
```

of the multiset words.  The pair fibre has three states and exactly two
upward outcomes.  The exact boundary rate is therefore

```text
(d_h/r)(1/(r-1))(2/3)=2d_h/[3r(r-1)].
```

At the root this gives, for every fixed adjacent pair of parts,

```text
Rroot_r(a,a^merge)=alpha_r k.
```

Detailed balance and
`rho(a)/rho(a^merge)=w_Aw_B/[k w_(A+B)]` give the stated reverse rate
`alpha_r w_Aw_B/w_(A+B)`.  All scan, fibre, and stationary-flow
normalizations are retained.

### 1.2 ACCEPT: M41 Section 11 stationary-length sharpening

I independently checked M41 checkpoint Section 11 (checkpoint SHA-256
`891eb088411476677464a7a2a504d5d179201dc8b888d3875f8d47f99d3df5aa`).
There is no numbered objection.  For every `r>=2`,

```text
gap(Rroot_r)>=alpha_r/(3e)=2/[9e r(r-1)].
```

Here are the requested delicate checks.

1. If `s=(A,c_2,...,c_k)`, the basin first moment is exactly

   ```text
   M_s=rho(s)[k!/w_A]
       sum_p (p+k-2) C_(A,p)/(p+k-1)!.
   ```

   This follows because a basin source has `p+k-1` parts and therefore
   height `p+k-2`.

2. The factorial inequality

   ```text
   k!(p+k-2)/(p+k-1)! <= k/p!
   ```

   is equivalent to
   `p+k-2<=binom(p+k-1,p)` and is valid for all `p>=1,k>=2`.
   Lagrange inversion then gives `M_s<=e k rho(s)`.

3. Root degree minus one has exactly
   `Bin(r-1,1/(r+1))` law.  Algebraically,

   ```text
   rho(number of parts=k)
    =binom(r-1,k-1) r^(r-k)/(r+1)^(r-1),
   ```

   so `E h=(r-1)/(r+1)<1`.

4. A fixed undirected edge occurs on the source half iff `x` is in its
   basin and on the reversed target half iff `y` is in its basin.
   When both happen both traversals must be counted.  Thus the full
   ordered-pair length load is

   ```text
   2[M_s+rho(B_s) E h] <=3e k rho(s).
   ```

   If one groups Dirichlet form by undirected edges, its leading `1/2`
   actually cancels this two-orientation duplication.  Dividing the full
   displayed load by the undirected capacity
   `rho(s)alpha_r k`, as the note does, is conservative by a factor two;
   it is not a missing factor.  The claimed congestion `3e/alpha_r`
   and gap lower bound are therefore valid.

5. For `r=2`, the two compositions have rates `2/3` and `1/3`;
   their gap is one, so the universal bound holds with slack.

This improves the old quotient inverse-gap order from `O(r^3)` to
`O(r^2)`.  In M50's balanced induction it changes the sufficient exponent
from `max{4,C+4}` to `max{4,C+3}`: a ROOT-MEAN LIFT cost `A r^C`
creates a root-variance term `O(r^(C+2))`, which fits in the exact
`Theta(r^(D-1))` induction margin when `D>=C+3`.

### 1.3 ACCEPT: exact root-fibre restrictions and balanced induction

I independently checked `internal_branch_restrictions.md` (SHA-256
`c04d08504c2f70b7a6602540cfe7f69e7a83a243e149f86c81a3fca8eead06e8`)
and `balanced_mean_lift.md` (SHA-256
`9ebab2dbcd316bf224c47800a5e353c122c3323f3fe232d445441441b4b03701`).
There is no numbered objection.

For a branch with `s` internal edges, a specified gap of its local
subsequence is empty in the global interleaving with probability `s/r`;
the resulting global site is selected with probability `1/(r-1)`.
Summing its `s-1` local gaps gives the exact action fraction

```text
s(s-1)/[r(r-1)].
```

Conditional on this event the local fibre and scan are literally those of
`Pbar_s`.  Root-edge/internal pairs and pairs in different branches can
only hold at the degree-macro level or leave the root-composition fibre.
Thus the rejected-exit restriction is the claimed weighted product.

The balanced induction is also correct.  Its worst branch is `s=r-1`,
and for `D>=4`

```text
R_D(r)=(1-1/r)^D/(1-2/r)
 <=(r-1)^3/[r^2(r-2)] <=1-1/(9r).
```

The last inequality is equivalent to `8r^2-25r+9>=0` for integer
`r>=3`.  Taking `D=max{4,C+3}` and `B>=81eA/2` absorbs the mean term.
This conditional theorem does not prove ROOT-MEAN LIFT.

## 2. New universal aggregate reverse-split lemma

Let `b=(c_1,...,c_k)` be a coarse root composition with at least one
splittable part.  For `d` in its fibre, let

```text
p_b(d)=Pbar_r(d, union of all one-root-split refinements of b).
```

Put `H(b)=sum_i(c_i-1)/c_i`.  Then:

```text
q_b:=E_[pi(.|b)] p_b
    =2 alpha_r H(b),                                 (2.1)
p_b(d)<=alpha_r(r-k),                                (2.2)
d nu_b/d pi(.|b)=p_b/q_b
    <=(r-k+1)/2 <=r/2.                               (2.3)
```

Here `nu_b` is the target marginal obtained by aggregating every incoming
refinement edge.

Proof of (2.1): Lagrange inversion gives

```text
sum_(A=1)^(c-1) w_Aw_(c-A)/w_c=2(c-1)/c.
```

Summing the exact quotient split rates over all parts proves (2.1).

Proof of (2.2): every split neighbour has degree vector
`d'=d+e_0-e_j` for one `j` with `d_j>=1`.  In the refined state
`d'`, the reverse merge uses one fixed root-child boundary.  Its rate to
the particular target `d` is at most the full boundary rate
`alpha_r(k+1)`.  The exact stationary ratio is

```text
pi(d')/pi(d)=d_j/(k+1).
```

Detailed balance therefore bounds this neighbour's reverse split
contribution by `alpha_r d_j`.  There is at most one macro neighbour for
each `j`; summing over every feasible `j` and then enlarging to all
nonroot vertices gives

```text
p_b(d)<=alpha_r sum_(j>=1)d_j=alpha_r(r-k).
```

Finally, if `x_i=c_i-1` and `sum x_i=r-k`, merging two positive
surpluses can only decrease
`sum x_i/(x_i+1)`.  Hence

```text
H(b)>= (r-k)/(r-k+1).
```

Dividing (2.2) by (2.1) proves (2.3).  This is linear aggregate
absolute continuity, stronger than applying the individual-edge
`O(r^(7/2))` bound separately.

There is also an exact equilibrium crossing inequality.  If
`F(a)=E[f|a]` and `Var_b(f)=Var(f|b)`, then

```text
E_Rroot(F,F)
 <=2 E_Pbar,root-cross(f,f)
   +2 sum_b rho(b) E_[pi(.|b)]
       [p_b(d)(f(d)-F(b))^2].                        (2.4)
```

Indeed, on each refined-to-coarse edge the crossing source marginal is
exactly stationary in the refined fibre.  Write the mean difference as
the expected crossing increment plus the target bias, apply
`(u+v)^2<=2u^2+2v^2`, use Jensen, and aggregate over all refinements
entering the same `b`.  Detailed balance turns their target mixture into
`pi(d|b)p_b(d)`, proving (2.4).

Equation (2.4) does **not** yet give an additive inverse-gap recursion.
Using (2.2) and the quotient inverse gap produces the multiplier
`1+O(r-k)` on the coarse-fibre Poincare cost; for a unary root this
is already `1+O(r)` at each recursive level.

This failure is not just an artifact of loose algebra.  Consider the
three-state reversible chain with uniform law, edges `a--b_1` of
capacity `q/3` and `b_1--b_2` of capacity `epsilon/3`, and enough
holding to make the kernel positive.  Partition it as
`{a},{b_1,b_2}`.  The forward crossing source is stationary and its
target density in the coarse fibre is at most two.  For
`f(a)=f(b_1)=0,f(b_2)=1`,

```text
E_quotient(E[f|fiber]) / E_full(f)=q/(4 epsilon).
```

Thus even constant aggregate target density and one-sided exact lumping
do not imply a mean-lift bound without quantitative internal geometry.
This refutes an abstract shortcut, not the actual parking inequality.

## 3. Bounded falsification

`root_quotient_spectrum.py` builds all `2^(r-1)` ordered compositions
and the exact quotient rates.  The numerical values of
`gap(Rroot_r)/alpha_r` decrease from `3` at `r=2` to
`2.20225831845` at `r=14`; every value is far above the proved
`1/(3e)`.  This can falsify a proposed strengthening on the tested range
but cannot prove a limiting constant.

The same script exactly enumerates parking macros through `r=7`.  It
finds no failure of (2.1)--(2.3).  The worst observed aggregate RN maximum
is `57/32` at `r=7,b=(5,1,1)`, while the worst observed chi-square
density is `419/1350`.  These small finite values suggest that (2.3) is
crude; they prove no universal constant bound.

`root_mean_lift_exact.py` builds both exact stationary-capacity matrices
and solves the generalized eigenproblem

```text
sup_f E_Rroot(E[f|root])/E_Pbar(f).
```

The sharp numerical constants for `r=2,...,7` are

```text
1.000000, 1.075269, 1.116345, 1.156997, 1.198451, 1.240218.
```

This directly rejects no polynomial mean-lift conjecture and supplies
finite evidence only.

## 4. Two proposed shortcuts do not close

1. **Cyclic root averaging.**  Conjugation of a micro factorization by
   the long cycle is a chain automorphism, but it does not descend to the
   parking degree macro.  If `epsilon_a` records incidence of the old
   last label `r`, then after shifting labels by one,

   ```text
   d'_0=sum_a epsilon_a,
   d'_j=d_(j-1)-epsilon_(j-1), 1<=j<=r-1.
   ```

   The extra incidence data is not retained by `d`.  Already at `r=2`,
   factor lists `(01),(12)` and `(12),(02)` have the same source macro
   but conjugate to different macros.  Thus a cyclic average may still be
   useful on an incidence-augmented microstate, but the branch product law
   and fibre means used here do not factor after conjugation.  Merely
   averaging the `r+1` equivalent fixed-root inequalities gives no
   `1/r` improvement for an arbitrary observable.

2. **Move the same distinguished leaf throughout.**  The exact `r=3`
   path with root--`h`--`c` and a marked leaf inserted as the first
   child of `h` before `c` has macro `(0,1,1)` and degrees
   `(1,2,0,0)`.  The marked leaf has no left sibling, so it cannot be the
   later branch of an upward child-boundary rotation; it is not last, so it
   cannot move by the reverse rotation.  Its marked insertion slot is
   isolated although replanting it at the root is a valid ideal move.
   This exact M56 obstruction refutes only a rigid marked-subtree route:
   unmarked `Pbar` may move the sibling `c` or swap route metadata.

## 5. Resource audit

The primary sources located do not supply ROOT-MEAN LIFT.

- Caraceni--Stauffer, arXiv:1809.05092v3, Theorem 3 proves
  `gap>=C_r n^(-9/2)` for their leaf-replanting chain on **uniform
  coloured plane trees**.  Our law is proportional to
  `product_v1/d_v!`, with star/path density ratio `r!`, and the exact
  parking move is a restricted sibling/right-spine rotation.  Neither
  stationary law nor move matches.
- Fleurat, arXiv:2411.03065v3, Theorem 1 covers Poisson offspring and
  supplies a Markov growth coupling by adding a right-leaning leaf.  It
  asserts existence/aggregate balance, not a same-size rotation-chain
  Poincare inequality or pointwise polynomial transition bound.  The
  project has already extracted a polynomial weighted replanting source
  gap from its aggregate balance; comparison to actual rotations remains
  geometric.
- Evans--Winter, arXiv:math/0502226v3 studies a continuum subtree
  prune-and-regraft Dirichlet process with Brownian CRT stationary law.
  It is not a finite conditioned-Poisson plane-tree chain and gives no
  finite-`r` comparison.
- Abraham--Delmas--He, arXiv:1007.0370v2 studies size-changing pruning of
  Galton--Watson trees (and infinite conditioned variants), not a
  fixed-size reversible local rotation chain with the parking law.

No primary quantitative theorem matching both the conditioned-Poisson
stationary law and the full parking child-boundary move was found.

## 6. Exact frontier

The quotient theorem, product restriction, and balanced sufficiency theorem
are accepted.  The first unproved standalone proposition remains:

> **ROOT-MEAN LIFT.**  There are universal `A,C<infinity` such that for
> every `r>=2` and every real `f` on `J_r`,
> ```text
> E_Rroot_r(E[f|root],E[f|root]) <= A r^C E_Pbar_r(f,f).
> ```

An equivalent next route is a source-recoverable, polynomial-congestion
flow that corrects reverse-split target bias using actual internal
right-spine rotations without multiplying a fresh loss at every depth.
The status is nonterminal.
