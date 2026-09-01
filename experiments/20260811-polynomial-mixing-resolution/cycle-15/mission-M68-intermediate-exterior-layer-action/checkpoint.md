# M68 checkpoint: uniform whole-macro merge action, but partial fibers remain

## 1. Convention and scope

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and words evaluate as
`t_1...t_m`.  Here `N>=5`, `m=2N-2`, `M=binom(N,2)`, and the literal chain is

```text
K=(1/2)I+(1/6) sum_(r=3)^5
       (1/(m-r+1)) sum_i H_(i,r).
```

This checkpoint proves a uniform-in-genus *whole support-component macro*
action estimate and two exact obstructions to upgrading it pointwise.  It
does not prove the required one-radius conductance bound for the M64 sets
`C_k=A union E_k`.

## 2. Uniform deletable-surplus-square lemma

Let `Gamma` be one labeled weighted support-component macro in `F_N^c`.
Write its nontrivial components as `(V_j,k_j,g_j)`, where

```text
|V_j|=d_j>=2,
k_j=2(d_j-1)+2g_j,
sum_j g_j=c-1,
```

and `c>=2` counts isolated labels as well.  Choose deterministically a
component `U` with `g=g_U>=1`, put `d=|U|` and `k=k_U`, and let `C_g(d)` be
the number of connected identity words on this fixed `d`-set at length `k`.

Call an internal adjacent square marked if deleting it leaves a connected
genus-`g-1` word on the same label set.  Inserting a chosen edge in a chosen
gap gives the exact marked-incidence identity

```text
E[Z_int]
 =(k-1) binom(d,2) C_(g-1)(d)/C_g(d).                (2.1)
```

The accepted positive DYZ recurrence consequence from M18 is

```text
[C_g(d)/k!]/[C_(g-1)(d)/(k-2)!] <= d^3/12.          (2.2)
```

Therefore

```text
E[Z_int] >= 12 binom(d,2)/(d^3 k)
          = 6(d-1)/(d^2 k).                         (2.3)
```

Conditional on `Gamma`, component words are independent uniform words and
their colors are uniformly interleaved.  A fixed pair of consecutive
internal occurrences of a color of multiplicity `k` remains consecutive in
the global length-`m` word with exact probability `k/m`.  If `Z` is the
number of globally adjacent marked squares from `U`, then

```text
E_Gamma[Z] >= 6(d-1)/(d^2 m).                        (2.4)
```

Since `Z<=m-1`, `(d-1)/d^2>=1/(2N)`, and no independence is needed,

```text
Pr_Gamma(Z>=1) >= 3/[N m(m-1)].                     (2.5)
```

This bound is uniform in the component genus `g`, including `g` growing with
`N`.  The deletion mark is essential: it says that removing the square does
not disconnect `U`.

## 3. Exact downward action

Put

```text
D_N=(3N^2+N-12)/2,
theta_N=1/[2N m(m-1)(m-2)D_N].                      (3.1)
```

On a certified word choose one marked pair `e,e`.  Pad on the right unless
the pair is final, in which case pad on the left.  If `V` is another support
component and `s` is a cross edge from `U` to `V`, then

```text
(e,e,a) -> (s,s,a),  or  (a,e,e) -> (a,s,s)         (3.2)
```

is one literal H3 outcome.  Both blocks have ordered product `a`.  Deleting
`e,e` leaves `U` connected, and inserting `s,s` merges exactly `U` and `V`.
The exact probability of one specified outcome is

```text
1/[6(m-2)D_N],                                      (3.3)
```

including laziness, the `r=3` scan, the window scan, and the exact
transposition-product triple-fiber size.  All H4/H5 action remains present
and nonnegative.

It follows from (2.5)--(3.3) that:

- if `c>=3`, the uniform law on `Gamma` has average K probability at least
  `theta_N` of moving to component count `c-1` while remaining exterior;
- if `c=2`, then the positive-genus component has genus one.  Deleting the
  mark leaves two minimal connected components.  Among their
  `d(N-d)>=N-1` cross edges, at most one gives the one fixed path join tree
  underlying `A`.  Summing the other outcomes gives average K probability

  ```text
  E_Gamma K(x,F_N minus A) >= (N-2)theta_N.          (3.4)
  ```

For the uniqueness in the second bullet, the target join tree is the union
of the two component join trees and the inserted cross edge.  A fixed tree
has at most one edge across a fixed bipartition.

## 4. Dense/partial macro dichotomy

Let `S=E_k` and, for one exterior macro `Gamma`, put

```text
u_Gamma=1-|S intersect Gamma|/|Gamma|.
```

For the appropriate downward event in Section 3 write its pointwise
probability as `q(x)<=1` and its whole-macro mean lower bound as
`theta_Gamma`, where `theta_Gamma=theta_N` for `c>=3` and
`theta_Gamma=(N-2)theta_N` for `c=2`.  Then exactly

```text
(1/|Gamma|) sum_(x in S intersect Gamma) q(x)
 >= theta_Gamma-u_Gamma.                             (4.1)
```

Thus a macro missing at most `theta_Gamma/2` of its states retains at least
half of its polynomial whole-macro downward flow.  In particular, summing
over all such dense two-component macros gives

```text
Q_K(C_k,C_k^c)
 >=[(N-2)theta_N/2]
   pi(union of dense c=2 macrofibers).               (4.2)
```

For partial macros there is only a multiradius statement.  The accepted
within-macro Hurwitz diameter is

```text
H_N=50Nm^3.
```

Every Hurwitz move is a padded literal H3 move and stays in the same exterior
macro.  Hence, if `Gamma intersect E_k` is nonempty, then

```text
Gamma subset E_(k+H_N).                              (4.3)
```

If `u_Gamma>theta_Gamma/2`, (4.3) implies

```text
|Gamma intersect (E_(k+H_N) minus E_k)|
 >=[theta_Gamma/(2-theta_Gamma)]|Gamma intersect E_k|
 >=(theta_N/2)|Gamma intersect E_k|.                 (4.4)
```

This proves polynomial *H_N-window growth* of every sparse partial macro,
but not one-step expansion at radius `k`.  A polynomial diameter cannot
replace that missing one-radius estimate.

For dense macros with `c>=3`, stationary inflow gives the exact absorption
inequality

```text
(theta_N/2) pi(union dense c-macros)
 <= Q_K(C_k,C_k^c)+pi(E_k intersect {component count c-1}).  (4.5)
```

Iterating (4.5) naively multiplies `theta_N` through up to `N` component
levels and is therefore superpolynomially lossy.  An additive marked
coalescence flow or a direct one-radius partial-fiber inequality is still
needed.

## 5. Exact refutations of two shortcuts

### 5.1 E0 is not macro-saturated

Exact N=5 enumeration gives 90 exterior labeled weighted macros.  The M64
one-step exterior closure `E_0` fully contains only 2, partially contains 47,
and misses 41.  Its component-count occupancy is

```text
c=2: 308409/739200,
c=3:   6362/23730,
c=4:      0/10.
```

Thus one cannot apply the whole-macro mean (3.4) directly to every `E_k`.

### 5.2 Pointwise exterior-to-minimal leakage is false

The exact N=5 full H3/H4/H5 audit finds 90 three-component states and all 10
four-component states with

```text
K(x,F_5 minus A)=0.
```

The repeated-edge word is the smallest displayed witness.  There is also an
infinite structural family.  Let `y_N=e^(2N-2)`.  One update changes at most
five factors, so a target has support on at most `2+2*5=12` labels.  Hence

```text
K(y_N,F_N)=0,  N>=13.                                (5.1)
```

Nevertheless M64 exterior connectivity puts `y_N` in some exterior layer.
That layer radius grows: a connected word contains at least `N-1` distinct
support edges, so it agrees with `e^(2N-2)` in at most `N` positions and has
Hamming distance at least `N-2`; a local update changes at most five
positions.  Therefore the exterior distance from `A` is at least
`ceil((N-2)/5)`, up to the `E_0` radius offset.  This rigorously refutes a
uniform per-state direct-exit proof even at growing intermediate radii.  It
does not give a bottleneck: `y_N` can have substantial flow to other exterior
states.

## 6. Current exact frontier

The surviving proposition is:

> **ONE-RADIUS EXTERIOR MACRO/FIBER ABSORPTION.**  Prove universal
> `c>0,C<infinity` such that the M64 boundary identity obeys
> `Q_K(C_k,C_k^c)>=cN^-C min(pi(C_k),pi(C_k^c))` for every intermediate
> `k`, by an additive marked component-coalescence flow and a one-radius
> expansion bound for partial macrofibers; or produce a literal-chain family
> where the complete H3/H4/H5 boundary violates every inverse polynomial.

The new estimates show that high component genus is not the obstruction for
whole macros.  The exact obstruction is the geometry of partial macrofiber
balls at one radius and the need to avoid multiplying a polynomial loss over
linearly many component mergers.

Verdict at checkpoint: **OPEN AT A NAMED STEP: ONE-RADIUS EXTERIOR
MACRO/FIBER ABSORPTION.**
