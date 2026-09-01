# Central-double bulk defect: a required matched Borel finite part

Status: Proposition 1 below is **proved**; the finite pointwise-sign witness
is **empirical**.  `(BD)` is **unresolved**.
Nothing here proves or refutes direct signed L1, H0, a bridge gap, the original
identity heat-bath gap, or either Terminal.

## 1. Exact starting formula

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors multiply
left-to-right.  Let `n=3k`, odd `k>=3`, and retain M94's

```text
A=(0,k,2k),             B=(0,1)(k,2k),
E=E_k={double targets with every cyclic support gap >=(k+1)/2}.
```

With M94's critical-Borel quantities `beta_3,beta_5`, lift count `a(s)`,
`R_n=(n-3)(n-4)`, and

```text
d_k(s)=beta_5(B,s)/beta_3(B)-beta_5(A,s)/beta_3(A),
```

the exact invariant-event convolution is

```text
Delta_k(E)=1/R_n^2 sum_s a(s)d_k(s)/beta_3(s)
                    sum_(t in E)a(t)beta_5(s,t).       (1.1)
```

Equivalently, define the channel-combined event responses

```text
R^Phi_(j,k)(s)=Phi_(j,s)(K 1_E),
R^Psi_(j,k)(s)=Psi_(j,s)(K 1_E).
```

M91's exact Abel identity gives

```text
Delta_k(E)
 =sum_(j=1)^2 alpha_(j,k) {
   sum_(u=1)^(k-2)D_(u,k)[R^Phi_(j,k)(u)-R^Phi_(j,k)(u+1)]
  +sum_(s<k/2)q_(s,k)[R^Phi_(j,k)(s)-R^Psi_(j,k)(s)] }.
                                                               (1.2)
```

No absolute value or square occurs inside `(1.1)` or `(1.2)`.

## 2. The tempting unrenormalized bulk integral is invalid

If every positive residual length in `(1.1)` is naively replaced by its
Stirling density, generic double intermediates and double targets formally
give an eight-support-point integral at scale `k^-2`.  This is not an
ordinary improper Lebesgue integral.

### Proposition 1 (proved: explicit nonintegrable collision face)

There is an open rational cell in the generic double/double parameter space
and a collision coordinate `delta>0` on which the complete two-target-color
integrand from `(1.1)`, already retaining the source difference `B-A`, obeys

```text
F(delta)=-C delta^(-3/2)+O(delta^(-1/2)), C>0.         (2.1)
```

Consequently its unrenormalized integral diverges to `-infinity` at that
face.  In particular, one cannot prove `(BD)` by passing directly to the
generic double/double Riemann integral and bounding all collision strata as
negligible.

#### Proof

Choose, within a small open neighborhood preserving all cyclic orders,

```text
s=(1/10,1/9,24/25,24/25+delta),       s-color S,
t=(1/7,9/20,5/7,15/16),               t-color S or N.
```

At `delta=0`, delete the single residual factor equal to `delta`.  The
remaining positive residual lengths are exactly

```text
A^-1 h after s:
  1/90,29/90,1/3,1/3;

B^-1 h after s, after deleting B's endpoint singleton:
  1/90,1/3,59/90;

s^-1 h:
  1/90,89/90;

(s t_S)^-1h:
  1/90,25/112,43/140,2311/5040;

(s t_N)^-1h:
  1/90,979/5040,37/140,297/560.       (2.2)
```

These lists follow directly by following the cycles of `g^-1h`; they are
also frozen exactly by `collision_face_symbolic.py`.  Write `P(L)` for the
product of a displayed positive list.  Since a critical-Borel Stirling
density contributes `P(L)^(-3/2)`, the coefficient in `(2.1)` is

```text
C=-[ (5400/59)^(3/2)-(2700/29)^(3/2) ]
     (89/8100)^(3/2)
     [ (284497920/99373)^(3/2)
       +(1317120000/398453)^(3/2) ].                  (2.3)
```

It is strictly positive because

```text
5400/59 < 2700/29
```

is the exact inequality `156600<159300`, while all other factors are
positive.  The neighboring residual lengths stay bounded away from zero, so
their smooth factors have a first-order Taylor remainder.  Multiplication by
`delta^(-3/2)` therefore gives the rigorously justified
`O(delta^(-1/2))` remainder; no derivative cancellation is claimed.  The
nested intermediate color is bounded on this face.  Thus `(2.1)` holds
throughout a small open set of the other coordinates.  Since
`integral_0^epsilon delta^(-3/2)d delta=infinity`, the naive integral is not
locally integrable.  QED.

The deterministic floating cross-check tends to coefficient `-8990.626...`,
but the proof uses only the exact radical expression and strict rational
inequality.

## 3. What must cancel the divergence

The collision `delta=0` is precisely the face where the separated double
intermediate degenerates: one transposition support gap becomes zero.  In the
finite lattice, `delta` is not a continuum variable below `1/n`; the first
few layers have a residual Borel component of integer size `r=O(1)`.  Their
weights are not described uniformly by the bulk formula
`b_(delta n)~(2 pi)^(-1/2)(delta n)^(-3/2)`.

The exact Borel sum contains the matching discrete small-component layers:

```text
r=1,2,...,epsilon n
```

of separated double intermediates.  At the collision itself the two-edge
support loses one dimension and is represented by the corresponding
three-support-point/triangle boundary topology (including its literal lift
multiplicity).  These are the boundary terms omitted when one first replaces
all double intermediates by a smooth four-support-point density.  Since the
finite exact defect is finite, their combined contribution must renormalize
the `epsilon^(-1/2)` divergence of the truncated bulk.  This is a structural
necessity, not a proved value or sign for the remaining finite part.

### Finite falsification 2 (empirical: pointwise event positivity fails)

A separate shortcut also fails: the stationary score

```text
z_k(t)=[K^2(B,t)-K^2(A,t)]/pi(t)
```

need not be nonnegative on `E_k`.

#### Proof

The quotient construction uses exact integer completion counts and is
converted at the final matrix arithmetic step to double precision.  It gives
at `k=9` the separated target with gaps `(5,5,5,12)` and
`9z_k=-0.410159...`.  The same deterministic program gives seven negative
event orbits at `k=9` and three at `k=7`; the margins are many orders of
magnitude above floating roundoff.  This is a reproducible finite
counterexample candidate, but because the retained computation is not an
exact-rational certificate, the universal pointwise statement is labeled
**empirically refuted**, not proved false.  The retained witness is in
`bulk_score_probe_k9.json`.  QED for the stated finite-floating fact only.

## 4. First unproved standalone lemma

The correct asymptotic interface is a matched expansion, not an ordinary
bulk Riemann sum.

> **MATCHED BOREL FINITE-PART TRANSFER `(MBF)` (unresolved).**  Truncate
> `(1.1)` to intermediate separated-double support gaps at least
> `epsilon n`, add the exact small-gap layers `1<=r<epsilon n` and the
> collision/triangle boundary topology with its literal lift and orbit
> multiplicities, and keep the two source channels and both target colors
> signed.  There exists a finite constant `C_*` such that, uniformly along
> odd `k`,
>
> ```text
> k^2 Delta_k(E_k)=C_*+o(1),                          (MBF)
> ```
>
> where the `epsilon^(-1/2)` terms cancel before `epsilon->0`.

To settle `(BD)` one must additionally prove `C_* !=0`.  A useful proof form
is an Euler--Maclaurin/Abelian subtraction of the exact Borel tail:

```text
sum_(r>=1)b_r H_k(r/k)
 =sum_(r>=1)b_r[H_k(r/k)-H_k(0)]
  +H_k(0)sum_(r>=1)b_r,                              (4.1)
```

performed only after the collision topology and the complete signed channels
are combined.  The bracket removes the nonintegrable `x^-3/2` term; the last
term is the discrete boundary/triangle counterterm.  Uniform control of the
next `x^-1/2` singularity would make the finite part integrable.  No such
uniform expansion or nonzero evaluation is proved here.

This obstruction explains why M94's finite embedding and gradient pieces can
be individually much larger and cancel to a stable `k^-2` signal.  It also
prevents promotion of finite `k<=11` values or a quadrature of only the
generic bulk.

## 5. Scope and falsification accounting

- **Proved:** exact reformulations `(1.1)--(1.2)` as inherited from M94/M91
  and the explicit nonintegrable collision face `(2.1)--(2.3)`.
- **Deterministic finite only:** `k=7,9` event-score table and the small Sobol
  probe which first exposed the divergence; pointwise positivity is
  empirically refuted by a large-margin finite-floating witness.
- **Unresolved:** `(MBF)`, its finite-part constant, `(BD)`, `(BA2)`, direct
  signed L1, the strict-edge lemma, H0, every bridge/identity-chain gap, and
  both Terminals.

Boundary cases remain those of M94: the family begins at `k=3,n=9`; even
`k`, `k=1`, other odd `n`, identity endpoints, `m=0,2`, and `N=2` are outside
this statement.
