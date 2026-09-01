# M291 framed-stabilizer reduction and paired-chart prefix obstruction

Date: 2026-08-14 UTC.  Status: **proved from the frozen inputs listed in
Section 2; fresh audit requested**.

## 1. Exact outcome

For `d>=6`, put `m=2d-2` and let `Z_d` be the connected-support identity
transposition words of length `m` on `[d]`.  Fix an adjacent DPS edit
`tau_i`, and fix an arbitrary perfect-matching color of M135's
root-stabilizer orbit-incidence multigraph.

This note proves two statements and stops there.

1. Every actual `H`-orbit edge selected by that color has separate source
   and target frames through one fixed valid doubled-star extension chart.
   Each frame has signed-braid length at most

   ```text
   L_d=50 d (2d-2)^3,
   ```

   and the resulting individual endpoint route has length at most `2L_d`.
   The complete literal braid fiber is an exact framed translate of the
   chart stabilizer.
2. The named **common-prefix paired-chart cover** cannot have polynomially
   many classes.  Even if its allowed targets are enlarged from valid
   extension charts to *all* ordered consecutive doubled Cayley trees and
   its prefixes have unlimited length, it needs at least

   ```text
   (2d-2)!/[d^2(d-1)!] >= d^(d-3)
   ```

   classes on the physical states of the chosen color.

The second statement is not a lower bound on the number of true common
schedule classes.  Source and target frames can still cancel through the
chart stabilizer.  That exact intersection remains the M135 polynomial
matching-coset refinement.

## 2. Conventions and frozen inputs

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors are displayed in
left-to-right product order.  The signed right-Hurwitz generators are

```text
R_j(a,b)=(b,bab),        R_j^(-1)(a,b)=(aba,a).
```

For braid words `x;y`, first apply `x`, then `y`.  Write `A_beta(w)` for the
result of applying the literal braid word `beta`, so
`A_(x;y)=A_y o A_x`.  Literal word length counts one signed generator per
letter.

The proof uses exactly these accepted inputs.

- M13 Claim D: if two identity-transposition words of length `m` in `S_N`
  have the same labeled weighted support components, their signed-Hurwitz
  distance is at most `50Nm^3`.  Its constructive audit supplies an explicit
  route, not a common-flow assertion.
- M112/M119: the rooted DPS bijection is
  `CayleyTrees([d]) x S_(2d-2)`, and forgetting the white root is exactly
  `d`-to-one.  Hence

  ```text
  |Z_d|=d^(d-3)(2d-2)!.
  ```
- M135/M137: `G=S_d` and `H=Stab_G(d)` act freely on `Z_d`; every matching
  color contains exactly one `H`-orbit edge over each left global `G` orbit;
  every such physical orbit has size `(d-1)!`; and `tau_i` is
  `H`-equivariant.
- M278/M281: a consecutive doubled word from a tree rooted at the leaf `d`
  with root edge `{1,d}` is a valid rank-extension chart in the locked DPS
  convention.

The accepted M240/M242--M278/M281 local correction table, M284/M288's
literal rank-lift intersection, and its chart-coverage obstruction are scope
checks only; no local correction is used to manufacture a same-rank common
schedule here.  M175/M176, M181/M183, and M200/M202 remain downstream or
finite-rank-only inputs and are not invoked in either proof.

## 3. One fixed valid chart

Let

```text
c_d=((1,2),(1,2),(1,3),(1,3),...,(1,d),(1,d)).       (3.1)
```

Its product is identity, its support is the star centered at `1`, and its
length is `2d-2`.  Root that star at its leaf `d`.  The root edge is
`{1,d}`, and the factor order in (3.1) is exactly the consecutive doubled
canonical-slot order of M278 (after converting its zero-based factor
labels to `[d]`).  Thus `c_d` is a valid doubled-tree extension chart.

The point of fixing `c_d` is only to coordinatize endpoint fibers.  The
fibers themselves will be intrinsic and independent of the chosen route to
the chart.

## 4. Polynomial individual framing and the exact fiber

Let `Q` be any actual `H`-orbit edge selected by the fixed M135 color.
Choose a source representative `w_Q` and put

```text
v_Q=tau_i(w_Q).
```

Both `w_Q` and `v_Q` lie in `Z_d`, as does `c_d`.  They therefore have the
same single labeled weighted support component.  Applying M13 Claim D twice
gives literal signed braid words `alpha_Q,delta_Q` such that

```text
A_(alpha_Q)(w_Q)=c_d,       |alpha_Q|<=L_d,
A_(delta_Q)(v_Q)=c_d,       |delta_Q|<=L_d.            (4.1)
```

Consequently

```text
beta_Q=alpha_Q;delta_Q^(-1)                           (4.2)
```

maps `w_Q` to `v_Q` and has length at most
`100d(2d-2)^3`.  Braid actions commute with global conjugation, while
`tau_i` commutes with `H`.  Hence the same `beta_Q` maps every
`rho.w_Q` to `tau_i(rho.w_Q)=rho.v_Q` for `rho in H`: (4.2) realizes the
whole actual orbit edge, not merely its chosen representative.

Now define the *literal braid stabilizer*

```text
BStab_d={s in B_m:A_s(c_d)=c_d}
```

and the literal endpoint fiber

```text
Ktilde_Q={beta in B_m:A_beta(w_Q)=v_Q}.
```

Then the exact identity is

```text
Ktilde_Q=alpha_Q ; BStab_d ; delta_Q^(-1).             (4.3)
```

Indeed, every word on the right follows the route
`w_Q -> c_d -> c_d -> v_Q`.  Conversely, if `beta` maps `w_Q` to `v_Q`,
then

```text
s=alpha_Q^(-1);beta;delta_Q
```

fixes `c_d`, and `beta=alpha_Q;s;delta_Q^(-1)`.

Equation (4.3) is independent of all normalization branches.  If
`alpha'_Q` is another source-to-chart frame, then
`alpha'_Q=alpha_Q;s_1` for some `s_1 in BStab_d`; similarly
`delta'_Q=delta_Q;s_2`.  Therefore

```text
alpha'_Q;BStab_d;(delta'_Q)^(-1)
 =alpha_Q;BStab_d;delta_Q^(-1).                       (4.4)
```

For a family `S` of matching-selected orbit edges, one literal braid works
on the whole family if and only if

```text
intersection_(Q in S)
  (alpha_Q;BStab_d;delta_Q^(-1)) is nonempty.          (4.5)
```

Moreover a representative of polynomial length is still separately
required.  Thus the exact necessary-and-sufficient framed signature is the
intrinsic fiber in (4.3), equivalently the pair of source/target chart-frame
cosets together with their common stabilizer.  Chart choice and
normalization branches alone are not the missing data.

## 5. Literal braids versus their finite action image

Let `p_d:B_m -> Acal_d` be the global finite braid-action image on `Z_d`.
For one orbit edge, put

```text
K_Q={a in Acal_d:a(w_Q)=v_Q}.
```

Then `p_d(Ktilde_Q)=K_Q`.  At this one fixed rank, common nonemptiness is
also preserved exactly:

```text
p_d(intersection_Q Ktilde_Q)=intersection_Q K_Q.      (5.1)
```

For the reverse inclusion, lift one common action to any braid word; the
lift has that same action on every source and hence lies in every literal
fiber.  Nevertheless `p_d` can collapse many distinct braid words, so
finite-action membership says nothing by itself about the shortest literal
representative demanded by M135.  No action-image embedding between ranks is
defined or used here.  In particular, (5.1) does not replace M284's
word-level rank-lift identity.

## 6. The common-prefix paired-chart cover

Define the broad paired-tree set

```text
P_d={e_(sigma(1))^2 ... e_(sigma(d-1))^2:
     {e_1,...,e_(d-1)} is a Cayley tree on [d],
     sigma orders its edges}.                         (6.1)
```

Every member is a connected identity word in `Z_d`.  Different labeled
trees and edge orders give different factor words, so Cayley's formula gives

```text
|P_d|=d^(d-2)(d-1)!.                                  (6.2)
```

Every valid consecutive doubled-tree extension chart is in `P_d`; (6.1)
is deliberately much larger than the locked M278 chart family.

Let `C` be the union of the physical `H`-orbits in an arbitrary fixed
perfect-matching color for `(d,i)`.  Freeness and left-perfectness give

```text
number of left G-orbits = |Z_d|/d!,
|C|=(|Z_d|/d!)(d-1)!=|Z_d|/d
   =d^(d-4)(2d-2)!.                                   (6.3)
```

This is the physical set associated with the actual selected `H`-edge over
every global orbit; it is not a preferred-root surrogate.

A **common-prefix paired-chart cover** of `C` consists of sets
`S_1,...,S_q` covering `C` and one fixed braid word `a_r` for each set,
such that

```text
A_(a_r)(w) in P_d       for every w in S_r.            (6.4)
```

The sets may overlap, need not be orbit-invariant, and may use prefixes of
unbounded length.  Condition (6.4) even allows different target paired
trees for different words in one class.

Each braid action is a bijection of `Z_d`.  Therefore

```text
|{w in C:A_(a_r)(w) in P_d}| <= |P_d|.                (6.5)
```

Summing (6.5) over a cover and using (6.2)--(6.3) proves

```text
q >= |C|/|P_d|
  = (2d-2)!/[d^2(d-1)!]
  = ((d+1)(d+2)...(2d-2))/d
  >= d^(d-3).                                         (6.6)
```

Thus the named cover has superpolynomial cardinality in `d`.  Since the
allowed target in (6.4) contains all valid extension charts, the same lower
bound applies a fortiori to common prefixes that canonicalize into the
valid chart family.  Because `P_d` is globally relabeling-invariant and
braid actions are equivariant, mapping one representative of an `H`-orbit
into `P_d` maps the whole orbit into `P_d`; hence (6.6) also applies when
the cover is formulated directly on M135 orbit edges.  By bijectivity of
`tau_i`, the analogous target-to-chart common-suffix strategy has the same
obstruction after inversion.

No finite enumeration is used: (6.6) is an arbitrary-rank counting proof.

## 7. What the obstruction does not say

The lower bound (6.6) concerns a prefix chosen before the target frame is
used.  A true common schedule `beta` only requires

```text
alpha_Q^(-1);beta;delta_Q in BStab_d                  (7.1)
```

for every `Q`.  The `Q`-dependent source and target frames in (7.1) may
cancel through different stabilizer elements even when no common prefix
sends the sources to paired charts.  Consequently (6.6):

- does not lower-bound the number of nonempty common-schedule classes;
- does not lower-bound the shortest representative of a nonempty common
  action fiber;
- does not obstruct every possible polynomial base-route signature; and
- supplies no path multiplicity, congestion, voltage, spectral-gap, mixing,
  or heat-bath conclusion.

The first open lemma is therefore unchanged in substance but is now in an
exact chart-framed form:

> **FRAMED-STABILIZER COMMON-INTERSECTION.**  For the actual `H`-orbit
> edges of an arbitrary M135 matching color, cover the fibers (4.3) by
> `d^O(1)` families whose intersections contain literal braid
> representatives of length `d^O(1)`, or prove that no such cover exists.

M284/M288 can be invoked only after such a genuine common base schedule is
present.  The complete local old-padded/new-rank correction table and the
chartless `V_D` obstruction neither fill nor strengthen (4.5).

## 8. Boundary and scope

The framing theorem applies in the requested regime `d>=6`; its formulas
also make sense whenever the cited inputs do.  The counting inequality
(6.6) already holds for `d>=3`.  No `d=5` or `d=6` guard is needed because
all steps are exact group actions and cardinality identities.

This note concerns deterministic routes in `Z_d` only.  It proves no
every-color common-schedule theorem, no statement about arbitrary-product
sectors, and no result for the global fixed-length target beyond this
minimal connected slice.
