# M331 independent proof audit of M328

Date: 2026-08-14 UTC
Verdict: **ACCEPT at the exact frozen obstruction/reduction scope**

## 1. MIDEC normalization and conditional implication

At an authenticated node, write `W=lambda(V)`, let `C=C(P)` have mass
`c`, and use the exact full child.  The parent normalized capacities and
child normalized demands are

```text
mu_{A,B}=2 lambda_A lambda_B/W^2,
nu_{Q,R}=2 lambda_Q lambda_R/c^2.
```

Summing over their respective edge sets gives exactly

```text
sum_e mu_e=2Phi/W^2=rho,
sum_f nu_f=2T(P)/c^2=rho'.                           (1.1)
```

The row equalities and column inequalities in MIDEC therefore leave reserve

```text
sum_e mu_e-sum_f nu_f=rho-rho'.                     (1.2)
```

Consequently MIDEC's first reserve clause is precisely

```text
log(W/c)<=C log(d)(rho-rho'),                        (1.3)
```

and its second is precisely the AATSD absolute drop whenever the child is
not edgeless.  This proves the stated local implication to AATSD
`(6.1)--(6.2)`.  It does not supply AATSD's separate initial-anchor clause.
The alternating-cycle support and path-multiplicity clause are extra
restrictions; neither is needed for this normalization implication.

## 2. Exact edge partition under a pivot

Partition the parent edges as

```text
E_R=E parent intersect binom(C,2),
E_D=E parent setminus E_R.                            (2.1)
```

Every edge in `E_R` remains a child edge: if
`D(A) intersect D(B)=empty`, then its intersection with `D(P)` is also
empty.  Conversely, any parent edge absent from the child has an endpoint
outside `C`, because the child vertex set is exactly `C`.  Thus every edge
in `E_D` has at least one outside endpoint.

The child edge set is the disjoint union of the retained edges `E_R` and
the regenerated pairs

```text
E_G={ {Q,R} subset C:
      D(Q) intersect D(R) nonempty,
      D(P) intersect D(Q) intersect D(R)=empty }.    (2.2)
```

Accordingly, with the obvious weighted sums,

```text
Phi=Phi_R+Phi_D,             T(P)=Phi_R+Phi_G.       (2.3)
```

This is the exact reason a regenerated pair cannot be paid merely by
renaming an induced parent edge.

## 3. Arbitrary-weight epsilon obstruction

Fix any actual/formal node and active pivot having a genuinely regenerated
pair `f={Q,R}`.  Keep every weight on `C`, in particular
`lambda_Q,lambda_R>0`, fixed, and multiply each weight in `V setminus C`
by `epsilon>0`.  Support and all signature intersections stay unchanged for
every positive `epsilon`.  Also

```text
c_epsilon=c,
W_epsilon=c+epsilon(W-c),
nu_f=2lambda_Q lambda_R/c^2>0.                       (3.1)
```

Every deleted-edge product contains an outside coordinate, so
`Phi_D(epsilon)=O(epsilon)`.  The retained and regenerated sums are fixed.
Using `(2.3)`,

```text
rho_epsilon -> 2Phi_R/c^2,
rho'_epsilon =2(Phi_R+Phi_G)/c^2,
Phi_G>=lambda_Q lambda_R>0.                          (3.2)
```

Hence `rho_epsilon<rho'_epsilon` for all sufficiently small positive
`epsilon`.  Total parent capacity is then smaller than total child demand,
so no MIDEC transport exists even if every incidence-support restriction is
dropped.  Retained capacities do not rescue the construction: in the limit
they exactly account only for retained child demands, leaving the positive
regenerated mass as the deficit.

M135's alternating-cycle rungs are unweighted incidence objects.  They add
no `lambda` coordinate and cannot change `(3.2)`; a `d^K` bound on the
number of paths only multiplies vanishing deleted capacity by a fixed
polynomial.  This validates M328's source-local arbitrary-weight
obstruction.

## 4. Quantifier and rank firewall

The preceding argument is conditional on exposing a genuinely regenerated
pivot.  It proves that unweighted incidence cannot furnish a universal
charge for such a pivot.  It does **not** show that every actual `d>=6` node
has such a pivot, or that an actual weight-dependent selection cannot avoid
all of them.  The authenticated `d=3` star/triple realizes the pattern only
at the boundary.  Therefore neither actual `d>=6 MIDEC` nor actual
`d>=6 AATSD` is refuted.

## 5. RATSD and low-density terminality

RATSD replaces the absolute decrement by

```text
rho-rho'>=d^{-B}rho                                  (5.1)
```

while retaining logarithmic payment on the selected nonterminal steps.  It
is strictly weaker than AATSD because `rho<=1`, and it permits arbitrarily
small absolute drops at low density.

If a compatible low-density theorem supplies an edgeless child whenever
`rho<d^{-B_1}`, then above that threshold `(5.1)` gives the absolute
dichotomy

```text
child edgeless, or rho-rho'>=d^{-(B+B_1)}.           (5.2)
```

Equivalently, repeated nonterminal RATSD steps satisfy
`rho_{t+1}<=(1-d^{-B})rho_t` and reach the threshold in
`O(d^B B_1 log d)` steps, after which the terminality theorem stops the
path.  This is only a conditional stopping implication: RATSD and
low-density terminality are both unresolved.  As M328's firewall requires,
no HPRN or downstream theorem follows.  In particular, if the RATSD log
clause is stated only for nonterminal children, a final terminal pivot also
needs separate weight-loss control before one may claim a polynomial lower
bound on final mass.

## 6. Numbered objections

1. Material objections: **none**.
2. Nonmaterial objections: **none**.
3. Scope clarification: “recover the missing absolute step” means the
   density-drop/termination dichotomy `(5.2)` only; it is not a proved
   AATSD, HPRN, or terminal-mass theorem.

No computation, new rank, charge, induced-child substitution, route, or
downstream inference was introduced.

