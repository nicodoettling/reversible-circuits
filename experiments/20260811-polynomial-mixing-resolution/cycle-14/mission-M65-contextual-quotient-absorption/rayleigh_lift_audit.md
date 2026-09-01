# Audit of a global Rayleigh or cut lift

Date: 2026-08-12.  The exact scalar and marked-history obstructions below
do not presently give a slow mode for the full parking projection.

## 1. The synthetic mark is not a state observable

After one deep restriction, `(K,R)` records the total ordered attachment
history retained from all ancestor and sibling levels.  Equation (2.2) of
`marked_context_inheritance.md` is a mixture over those histories.  Two
different histories can reach the same unmarked last-branch macro with
different synthetic `(K,R)` values and different positional weights.

Consequently neither the bad scalar coefficient nor the event
`R=K-1` defines a subset of `J_s`.  A function of the unmarked plane tree
cannot simply read the synthetic context.  Summing history-specific Green
optimizers can create cross terms on every actual edge; this is exactly the
unresolved marked source-recovery problem from M56.

## 2. The literal ambient-fibre cut has polynomial escape

There is a genuine ambient realization of the extreme family.  For local
rank `s`, take ambient rank `r=s+K` and root composition

```text
b=(s+1,1,...,1)                 (K parts),          (2.1)
```

with the large branch leftmost, so `R=K-1`.  Its exact stationary mass is

```text
rho_r(b)=w_(s+1)/(K! Z_r).                          (2.2)
```

This realizes the contextual rates, but a cut supported inside this exact
root-composition fibre is not a superpolynomial bottleneck.  At every state
of the fibre, each of its `K-1` root child boundaries merges at total rate
`alpha_r K`, and the destination leaves the fibre.  Therefore every
`A subset F_b` satisfies

```text
Q(A,A^c)/pi(A)
 >=alpha_r K(K-1)
 =2K(K-1)/[3r(r-1)].                               (2.3)
```

For fixed `K` this is order `r^-2`, and for varying feasible `K<=r` it is
still inverse polynomial whenever nonzero.  Adding a nested unary-spine
condition inside `F_b` does not remove the root escape (2.3).

The stationary weight of a strict depth-`d` unary history also contains
the exact factor

```text
[K/(K+d)] [w_(s-d)/w_s],
```

which is exponentially small when `d` is proportional to `s`.  Thus the
most literal nested corridor has neither a closed boundary nor a
nonnegligible stationary side.

## 3. Why no Rayleigh upper bound follows

The local number

```text
||H-EH||_(-1,G_s)^2
```

is a dual energy for routing a conditional-rate charge on the accepted
root quotient.  It is not the variance of a recursively defined full-tree
observable.  Turning the local dual optimizers into a primal global test
requires extending them across neighbouring root-composition fibres to
avoid (2.3), while assigning one value to every unmarked state reached by
many marked histories.  No such consistent extension is currently known.

The first missing lift is:

> **UNMARKED NESTED-RAYLEIGH CONSISTENCY.**  Construct a real function on
> unmarked parking macros whose conditional martingale increments realize
> the marked contextual Green optimizers, with recoverable history
> collisions and with all root-merge/split edge energy accounted for.  To
> prove slow mixing, its variance/energy ratio must be superpolynomial; to
> rescue the comparison, the corresponding marked demand operator must
> instead have polynomial Green growth.

Absent this lift, the M65 results rigorously refute the scalar
disintegration template but neither upper-bound nor lower-bound the full
`Pbar_r` gap beyond inherited results.  There is also no stationary-flow
lift from this synthetic marked family to the fixed-endpoint bridge or the
original identity chain `K`; it cannot support Terminal B.
