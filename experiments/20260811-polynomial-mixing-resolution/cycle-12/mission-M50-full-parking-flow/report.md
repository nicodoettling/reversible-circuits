# M50 final report: full actual parking flow

Date: 2026-08-11.  Frozen scoped bundle version 1.

## 1. Exact claim, quantifiers, and convention

Permutations compose as `(pq)(x)=p(q(x))`, and displayed factor tuples
multiply left-to-right.  For `r>=1`, let

```text
J_r={d in N^r:sum_i d_i=r and sum_(i=0)^q d_i>=q+1 for q<r},
pi_r(d)=r!/[(r+1)^(r-1) product_i d_i!].
```

Append `d_r=0` and identify `d` with the rooted plane tree whose preorder
outdegrees are `(d_0,...,d_r)`.  Let `Pbar_r` be the full **nonlazy**
stationary-flow projection of the uniform scan of the `r-1` adjacent exact
rank-two heat baths on minimal factorizations of `(0 1 ... r)`.

The assigned claim `gap(Pbar_r)>=r^-C` remains open.  The following scoped
claims are proved for every indicated `r`.

1. **Full child-boundary rate (`r>=2`).**  If vertex `h` has ordered child
   intervals `I_1,...,I_k`, then for each `p<k` the total rate of upward
   moves merging `I_p,I_(p+1)` is exactly

   ```text
   2d_h/[3r(r-1)].                                  (1.1)
   ```

   Every destination attaches the later branch at a vertex on the right
   spine of the earlier branch, and every upward move belongs to one such
   boundary.

2. **Root-composition quotient (`r>=2`).**  Let `a=(a_1,...,a_k)` be the
   ordered root branch sizes, including their root edges.  Put

   ```text
   Z_s=(s+1)^(s-1)/s!, Z_0=1,
   w_a=a^(a-1)/a!, alpha_r=2/[3r(r-1)].
   ```

   The stationary-flow quotient `Rroot_r` has

   ```text
   rho_r(a)=(1/Z_r)(1/k!) product_i w_(a_i).         (1.2)
   ```

   If `a^merge` replaces adjacent parts `A,B` by `A+B`, then

   ```text
   Rroot_r(a,a^merge)=alpha_r k,
   Rroot_r(a^merge,a)=alpha_r w_A w_B/w_(A+B),       (1.3)
   gap(Rroot_r)>=2/[9e r(r-1)].                      (1.4)
   ```

   This is a stationary-flow projection, not a strong lumping.

3. **Exact rejected-exit restrictions.**  Conditional on root composition
   `a`, put `s_i=a_i-1`.  The fiber law is `tensor_i pi_(s_i)`, and its
   rejected-exit restriction has Dirichlet form

   ```text
   sum_(i:s_i>=2) [s_i(s_i-1)/(r(r-1))]
       E_(Pbar_(s_i))^(i).                          (1.5)
   ```

   Its gap is the minimum of those scaled coordinate gaps, with singleton
   conventions when all `s_i<=1`.

4. **Balanced recursion reduction.**  If universal `A,C` satisfy

   ```text
   E_(Rroot_r)(F_f,F_f)<=A r^C E_(Pbar_r)(f,f),
   F_f(a)=E_pi_r[f|a],                              (1.6)
   ```

   then `gap(Pbar_r)>=B^(-1)r^(-D)` universally with
   `D=max{4,C+3}` and a universal `B`.

5. **Cayley child-sorting obstruction.**  For every even `r=2q>=6`, one
   labelled Cayley basis exchange of exact rate `1/[rq(q+1)]` can produce
   child-sorted degree vectors at `L^1` distance `2r-8`.  Every `Pbar_r`
   route between them has length at least `r-4`.  This refutes bounded-length
   or pointwise one-move Cayley domination, not a polynomial fractional flow.

These claims concern only the minimal long-cycle parking projection.  They
are not a result for the original identity-word chain `K` and are not a
Terminal-A or Terminal-B conclusion.

## 2. Full argument

### 2.1 Boundary marks and exact normalization

For a fixed degree vector `d`, Stanley--Biane identifies the raw words with
all permutations of the parking multiset, so

```text
|O_d|=r!/product_h d_h!.
```

The interval-component lemma gives one lower-`h` factor for each child
interval of `h`.  Goulden--Yong incident-edge order puts those factors in
reverse child order.  A specified internal gap among the `d_h` occurrences
is empty in exactly the fraction

```text
binom(r-1,d_h-1)/binom(r,d_h)=d_h/r
```

of multiset permutations.  Hence one child boundary has
`d_h|O_d|/r` marked word/scan pairs.  The relevant ordered factors have form

```text
(h,b)(h,j), h<j<b,
```

and their same-product fiber is

```text
(h,b)(h,j), (h,j)(j,b), (j,b)(h,b).
```

Exactly two outcomes replace one lower label `h` by `j`.  Dividing by the
`r-1` scan sites and the three fiber states proves (1.1), including the
factor `3r(r-1)`.  Immediately before the later child interval is read, the
open preorder stack in the earlier interval is exactly its right spine;
this proves the destination and completeness statements.

At the root, (1.1) gives the forward rate in (1.3), pointwise for every
internal branch shape.  Root weight `1/k!` and independent subtree weights
give (1.2).  Detailed balance and

```text
rho_r(a)/rho_r(a^merge)=(1/k)w_Aw_B/w_(A+B)
```

give the reverse rate.  Reverse rates are not pointwise constant inside a
coarse fiber.  At `r=3`, macros `(0,1,1)` and `(0,1,2)` both have root
composition `(3)`, but their rates to composition `(1,2)` are `0` and
`1/9`.

### 2.2 Root quotient gap

Route every ordered composition to `(r)` by repeatedly merging its first
two parts, and route each all-pairs heat-bath commodity through this hub.
Paths have length at most `2(r-1)`.  For a used edge with refined endpoint

```text
s=(A,c_2,...,c_(ell+1)),
```

the recoverable source basin consists exactly of arbitrary refinements of
the first part `A` with the suffix fixed.  Put

```text
C_(A,p)=sum_(b_1+...+b_p=A) product_i w_(b_i).
```

For `T(z)=sum_(a>=1)w_a z^a=z exp(T(z))`, Lagrange inversion gives

```text
C_(A,p)=[z^A]T(z)^p=p A^(A-p-1)/(A-p)!.
```

Therefore the basin-to-edge density ratio is at most

```text
(1/w_A)sum_p C_(A,p)/p!=Z_A/w_A
 =(1+1/A)^(A-1)<=e.                                 (2.1)
```

Put `h(x)=number of parts of x minus one`.  Its exact stationary law is
`Bin(r-1,1/(r+1))`, so `E h<1`.  If `M_s` is the first moment of `h` over
the basin of a refined endpoint `s=(A,c_2,...,c_k)`, the same Lagrange sum
and

```text
k!(p+k-2)/(p+k-1)!<=k/p!
```

give `M_s<=e k rho_r(s)`.  Counting both hub-path halves, including both
traversals when they overlap, the total length-weighted load is at most
`3e k rho_r(s)`.  The exact edge capacity is

```text
rho_r(s) 2k/[3r(r-1)], k>=2.
```

Thus congestion is at most `9e r(r-1)/2`, proving (1.4).  This
stationary-length sharpening is coordinator M41 Section 11, audited here
against the exact basin factorials and occurrence count.  Although the
composition hub has constant mass at least `e^-1`, no fixed plane-tree
shape is used.

### 2.3 Product restrictions

Deleting each root edge identifies the root-composition fiber with
`product_i J_(s_i)` and factors its conditional weight.  For a branch with
`s` internal edges, consider the uniformly selected global scan site.  A
fixed local adjacent gap has no outside entry in its interleaving gap with
probability `s/r`, and its resulting global site is selected with probability
`1/(r-1)`.  Hence each local scan site is selected with probability
`s/[r(r-1)]`, and all `s-1` sites together have action probability

```text
s(s-1)/[r(r-1)].
```

Conditioned on this event, the local update is exactly `Pbar_s`, including
its uniform local scan and two- or three-state heat-bath normalization.
Different child coordinates are independent, proving (1.5) and its exact
gap formula.

### 2.4 Why one mean-lift closes the recursion

Use total variance at the root.  Equation (1.4) and the hypothetical (1.6)
bound the variance of fiber means by `(9eA/2)r^(C+2)` times the full energy.
Inside a root fiber, product variance tensorization and induction with
inverse gap `B s^D` give the internal coefficient

```text
B max_(2<=s<=r-1) r(r-1)s^(D-1)/(s-1).
```

For `D>=4`, the maximum is at `s=r-1`; relative to `B r^D` it is

```text
R_D(r)=(1-1/r)^D/(1-2/r)
 <=(r-1)^3/[r^2(r-2)]<=1-1/(9r).                    (2.2)
```

Choosing `D>=C+3` and `B>=81eA/2` lets the `1/(9r)` margin in (2.2) absorb
the root term.  Strong induction from the exact `r=1,2` cases proves (1.6)
implies the polynomial full-projection gap.  Thus no per-depth polynomial
is multiplied.

### 2.5 Cayley exchange calibration

For `r=2q`, make root branch `A` the labelled path
`1-(q+2)-...-2q` and branch `B` the star with centre `2` and leaves
`3,...,q+1`.  Deleting `{0,1}` and adding `{0,2q}` reroots `A` and changes
the sorted root-child order from `A,B` to `B,A`.  The degree vectors are

```text
(2,1^(q-1),0,q-1,0^(q-1)),
(2,q-1,0^(q-1),1^(q-1),0),
```

whose `L^1` distance is `4(q-2)`.  Every actual macro move is a unit degree
transfer and changes this distance by at most two, proving the lower bound
`r-4`.  The deleted cut has component sizes `q,q+1`, giving Cayley down-up
rate `1/[rq(q+1)]` exactly.

## 3. Probability, runtime, path, and congestion accounting

- Actual scan: `r-1` sites; nontrivial pair fiber: three states; favorable
  boundary outcomes: two.  These give (1.1) with no suppressed constants.
- Root quotient path length: at most `2(r-1)`; source-basin density: at most
  `e`; stationary mean path height: below one; stationary capacity:
  `rho(s)2k/[3r(r-1)]`; congestion: at most `9e r(r-1)/2`.
- A positive quotient split has
  `w_Aw_B/w_(A+B)>=4/[3r^(3/2)]`, so its rate is at least
  `8/[9r^(5/2)(r-1)]`.  This gives only a one-level polynomial Radon bound.
- A branch of internal size `s` receives exactly the action fraction
  `s(s-1)/[r(r-1)]`; a giant `s=r-1` branch is not exponentially frozen.
- The conditional mean-lift induction has exact margin `1/(9r)` and would
  produce exponent `D=max{4,C+3}`.
- The Cayley counterfamily has ideal edge rate `1/[rq(q+1)]` and necessary
  actual path length `r-4`; no congestion lower bound follows.
- All constructive tree, composition, and path operations above take
  polynomial time in `r`.  Exact enumeration is exponential and is used
  only to falsify named structural/normalization claims.

## 4. Dependencies, labeled

- **Proved here:** full child-boundary support/rate; root-composition law,
  transition rates, basin identity, and gap; exact root-fiber product
  restrictions and action rates; balanced induction from ROOT-MEAN LIFT;
  explicit linear Cayley child-sorting obstruction.
- **Proved and accepted in M35/M41/M46:** Stanley--Biane parking-multiset
  count; interval-component lemma; M35 aggregate departure and leaf rates;
  `pi_r` as child-sorted uniform Cayley pushforward; full-projection bypass
  of the restricted-leaf separator; the Cayley basis-exchange projection
  has `gap>=1/r`.
- **Cited with project convention checked:** Goulden--Yong, JCTA 98 (2002),
  Theorem 2.2(f1)--(f3), Proposition 2.4, and Lemma 2.5; Stanley, EJC 4(2)
  (1997), Theorem 3.1 and Proposition 4.1; Biane, EJC 9 (2002), Theorem 3.1.
- **Conditional:** ROOT-MEAN LIFT (1.6), or alternatively a polynomial
  Cayley-exchange-to-`Pbar_r` fractional comparison.
- **Empirical exact only:** reconstruction through `n=r+1<=8`.  A finite
  pass proves no asymptotic claim.

## 5. First unproved standalone proposition

> **ROOT-MEAN LIFT.**  There are universal constants `A,C<infinity` such
> that for every `r>=2` and every real `f` on `J_r`, if
> `F_f(a)=E_pi_r[f|root composition a]`, then
>
> ```text
> E_(Rroot_r)(F_f,F_f)<=A r^C E_(Pbar_r)(f,f).
> ```

By Section 2.4, this proposition alone implies a universal inverse-polynomial
gap for the full actual parking projection.  A sufficient alternative is:
route every edge of the accepted child-sorted Cayley basis-exchange
projection through `Pbar_r` with polynomial path length and total stationary
congestion, retaining the exchanged labels in source-recovery metadata.

## 6. Strongest self-attack

Forward root merges have stationary source marginal, but their reverse
target marginal inside the coarse fiber is biased.  If `a` refines `b`, its
density relative to `pi(.|b)` is exactly

```text
Pbar_r(y,F_a)/Rroot_r(b,a),
```

which is at most `(9/8)r^(5/2)(r-1)` by the crude split-rate bound.  This is
polynomial for one merge, but multiplying it through a depth-`Theta(r)`
history is superpolynomial.  The root quotient is not strongly lumpable, as
the exact `r=3` witness shows, so Jensen cannot erase this bias.  Likewise,
the Cayley lift has the correct uniform stationary law but child sorting can
reorder linear blocks.  Neither result supplies the recoverable randomized
flow required by (1.6).  The proved quotient and restriction gaps therefore
must not be combined via a multiplicative depth recursion and reported as a
full gap.

## 7. Calibrations

- `r=1`: singleton; all recursive statements use the singleton convention.
- `r=2`: the two root compositions have exact merge/split rates `2/3,1/3`;
  their two-state gap is one, retaining the `3(r-1)` normalization.
- Stars and paths have stationary weight ratio `r!`; no pointwise density
  comparison or fixed star/path plane-tree hub is used.
- The one-part **composition** hub has mass
  `(r/(r+1))^(r-1)>=e^-1`; its internal shape is never fixed.
- Balanced rare-label/two-hop obstructions from M35 are not bypassed by a
  false short-path assertion.  The Cayley path/star family instead proves a
  genuine linear lower bound on comparison length.
- Exact reconstruction for every `3<=n<=8` has zero failures for right-spine
  support, per-boundary rate, quotient rates, basin bound, and internal
  product scaling.  The first reverse nonlumpability witness occurs at
  `r=3` as stated.
- The M48 maximum-degree pebble cut is crossed by full `Pbar_r` with
  inverse-polynomial flow at least `4(beta_r-bprime_r)/[3r(r-1)]`; it is not
  reused as a full-chain bottleneck.
- Original `S_3,m=4`, `S_4,m=4`, `S_4,m=6`, whole-word `H_4`, odd/empty,
  `N=2`, and excluded `m=2` calibrations are untouched because this report
  makes no claim beyond the minimal long-cycle projection.

## 8. Artifacts and reproduction commands

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-12/
  mission-M50-full-parking-flow/
```

Universal proofs are in `root_composition_projection.md`,
`internal_branch_restrictions.md`, `balanced_mean_lift.md`, and
`cayley_exchange_geometry.md`.  The bounded deterministic falsifier uses
Python standard library only, no random seed, Python 3.12.3, and repository
commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M50-full-parking-flow/root_composition_audit.py --n-max 8 --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M50-full-parking-flow/root_composition_results.json
```

The output records the exact command, environment, raw counts, all failure
lists, basin maxima, `r=2` calibration, and first nonlumpability witness.
Artifact hashes are recorded after cleanup in `SHA256SUMS`.

## 9. Verdict

**OPEN AT A NAMED STEP: ROOT-MEAN LIFT.**

This verdict concerns the assigned full-parking-projection claim only.  The
root-composition quotient and rejected-exit restriction theorems are
`PROVED`; no claim is made for the original identity chain `K`.
