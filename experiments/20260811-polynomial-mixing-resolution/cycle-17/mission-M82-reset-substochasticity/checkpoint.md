# M82 halfway checkpoint: ordinary reset mass and augmented-variance route

Date: 2026-08-12. Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Scope and exact operator

This checkpoint concerns only the full nonlazy stationary-flow parking
projection in the minimal long-cycle sector.  It is not a result for the
identity-word heat-bath chain `K`.

For `x=(s,K,R,B)`, put

```text
q_x=w_(s+1-B)w_B/w_(s+1),        P(x)=s+K-R.
```

The deep coefficient attached to a root composition with `k` parts and
last part `t>B`, followed by attachment rank `1<=j<=k`, is

```text
D(x,y)=rho_s(k,t) q_y nu_(K,R,k)(j)/q_x,
y=(t-1,K+k,R+j,B).
```

For the canonical edge with refined endpoint `(A,c_2,...,c_k)`, basin
current `theta_e`, and `Q_G(e)=rho_s(refined)k`, the reset coefficient is

```text
J_can(x,y_e)=theta_e^2/[Q_G(e)q_x],
y_e=(A+c_2-1,k-1,k-2,c_2).
```

Every `D` and `J_can` child strictly lowers `P`, so
`K_reset=(I-D)^(-1)J_can` is a finite DAG sum.  No raw Bellman inequality
is assumed.

## Exact reproduction

An independent `fractions.Fraction` evaluation using the displayed formulas
reproduced M79 and extended the exhaustive scan to all
`2<=s<=8`, `1<=K<=8`, `0<=R<K`, and `1<=B<=s`.  There were no violations of

```text
K_reset 1(x)<=(K-R)(1-q_x).
```

The worst normalized ratio through this range is the reachable reset seed

```text
x=(8,1,0,3),
K_reset 1=253985287689718867427349453367883132399
          /473678965726019627503656524945817600000,
q_x=896/6561,
K_reset 1/(1-q_x)=0.621004266940768... .
```

This is exact finite evidence only.  It proves no universal inequality.
The grouped predecessor trajectory for the worst seed rises from
`.690924...` at rank 14 to `.808199...` at rank 30, so a limiting argument
or a counterfamily remains necessary.

## Structural lead, not yet a theorem

For a fresh reset seed `(K,R)=(1,0)`, the pointwise contextual statistic on
the exact parking macros takes values in `[0,1]` (verified exactly through
local rank five), has mean `q_x`, and the eliminated reset energy satisfies

```text
q_x K_reset 1(x) <= Var(Phi_x)
```

in every exact instance checked through local rank five.  For example, the
ratio of the left side to the full variance stays below `.736` in those
checks, even though the same ratio to the root-composition conditional
variance already exceeds one at rank six.  Thus any viable proof must use
the full augmented recursive statistic, not only `H=E[Phi|C]`.

The promising formulation is an augmented attachment/composition
filtration: retain the negative-hypergeometric `j` choice at a deep step,
and seek a Bessel/Haar inequality assigning each canonical basin-current
square `theta_e^2/Q_G(e)` to a disjoint conditional-variance increment.
Synthetic descendants can have `K-R>1` and pointwise values above one, so
the augmentation must retain the original marked opportunity; treating
every formal child as an independent Bernoulli is invalid.

## Current status and next falsification target

- **Proved/reproduced:** exact normalization, strict `P` descent, and the
  bounded scan stated above.
- **Unresolved:** right-heavy `K_reset 1<=1` and the stronger multitype
  inequality.
- **Rejected proof shortcut:** root conditional variance alone; canonical
  path energy can exceed `Var(H)`.
- **Next step:** derive the augmented Haar identity explicitly and check its
  local edge-budget formula exactly.  In parallel, accelerate the grouped
  seed recurrence to ranks well above 30 to detect any approach through or
  beyond one; any numerical violation will be certified rationally.

