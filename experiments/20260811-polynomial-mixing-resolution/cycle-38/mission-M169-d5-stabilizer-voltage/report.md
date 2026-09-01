# M169 final report: white-root monodromy and stabilizer voltage

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and exact scope

```text
FINAL VERDICT: KEEP A PROVED, SECTION-FREE RELATIVE-ORIENTATION-COVER
CRITERION AND THE ACCEPTED-MATCHING MONODROMY EXACT SEQUENCE.

PROVED for every d>=3: transporter parity is the sign of monodromy on the d
white-root lifts.

PROVED for fixed physical tuple endpoints: the M163 route-voltage coset
contains zero exactly when their relative-orientation lifts are in one braid
orbit.

PROVED for accepted d>=5 M135 matching subfamilies:
1 -> P_(d,s) -> K_mon(q) -> V_stab(q) -> 1.

UNRESOLVED: whether V_stab(q)=F_2^s/Delta, quotient-route existence for a
specified matching source and target, and every polynomial word-length bound.
```

This meets the mission's permitted fallback of determining the actual
source-to-target zero-coset condition. No `d=5` group closure was launched.

## Field 2 — target, action, and immutable inputs

The auxiliary target is uniform on

```text
Z_d={(t_1,...,t_(2d-2)):t_1...t_(2d-2)=id,
                              support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. Chronological signed right-Hurwitz moves are

```text
R_j(a,b)=(b,b^(-1)ab),
R_j^(-1)(a,b)=(aba^(-1),a).
```

All frozen `SHA256SUMS` lists in M135/M137, M141/M143, M146/M148,
M154/M158, and M163/M164 verified exactly before use. The proof uses accepted
M135's `H=Stab(d)` white-root orbits, M141's aligned common-parity generation,
M154's inner-conjugation braids, and M163's stabilizer-coset theorem. No
literature classification or predecessor computation is imported.

## Field 3 — the rooted cover and its monodromy

Let `G=S_d` act freely on `Z_d` by simultaneous relabeling and put
`Q_d=Z_d/G`. Define the physical rooted cover

```text
R_d=(Z_d x [d])/G,       gamma.(w,a)=(gamma.w,gamma(a)).
```

It is a `d`-sheeted cover of `Q_d`, and

```text
Z_d/Stab_G(d) -> R_d,       [w]_H |-> [w,d]
```

is a bijection. Thus its sheets are exactly M135's white-root lifts rather
than lifts chosen by a new section.

If a quotient-loop braid `h` has unique physical transporter `rho`, so that
`h.w=rho.w`, then for every root `a`,

```text
h.[w,a]=[rho.w,a]=[w,rho^(-1)(a)].
```

Therefore its root-fiber monodromy is `rho^(-1)`, and its sign is exactly
`sgn(rho)`. The same formula holds for a route `u->v` when the two fiber
coordinates are trivialized by the fixed physical endpoints.

## Field 4 — tuple voltage is relative root orientation

For an ordered width-`s` quotient tuple, a point-stabilizer braid has
coordinate root monodromies `mu_1,...,mu_s in S_d`. The theorem gives

```text
V_stab(q)
 ={(sgn(mu_1),...,sgn(mu_s)) mod Delta:h in B_q},
Delta=<(1,...,1)>.
```

Equivalently, define the regular relative-orientation cover

```text
O_(d,s)=Z_d^s/P_(d,s) -> Q_d^s,
P_(d,s)={(g_1,...,g_s):sgn(g_1)=...=sgn(g_s)}.
```

Its deck group is `W_s=F_2^s/Delta`. The subgroup `V_stab(q)` is literally
the deck-monodromy image over `q`. Consequently, above one quotient-tuple
braid orbit, the lifted braid orbits are indexed by the cosets
`W_s/V_stab(q)`. This is a structural identity, not a finite extrapolation.

## Field 5 — exact physical source-to-target zero-coset condition

Fix physical endpoint tuples `U,V`, not merely their absolute quotient
classes. They determine points `U^or,V^or` in `O_(d,s)`. Assuming at least
one quotient route exists, the following are equivalent:

1. the M163 route-voltage coset for these fixed endpoints contains zero;
2. some route has coordinate root-monodromy signs all equal;
3. some route's root-fiber bijections are either all orientation-preserving
   or all orientation-reversing;
4. `U^or` and `V^or` lie in the same braid orbit in `O_(d,s)`.

This is the actual section-free zero-coset criterion requested by the
mission. It does not assume that a quotient route exists; rather, it states
the exact additional lifting test once quotient routing is nonempty.

## Field 6 — accepted M135 matching exact sequence

Fix a nonempty ordered subfamily of an accepted `d>=5` M135 matching and
fixed physical representatives. Let `K_mon(q)<=S_d^s` be the set of tuple
root monodromies of quotient point-stabilizer braids. Accepted M141 says its
aligned factors generate `P_(d,s)`, and accepted M154 supplies literal braid
loops realizing conjugation by every element of that group. Their monodromies
therefore give

```text
P_(d,s) <= K_mon(q).
```

The relative-sign kernel in `S_d^s` is exactly `P_(d,s)`. By the definition
of `V_stab` and the first isomorphism theorem,

```text
1 -> P_(d,s) -> K_mon(q) -> V_stab(q) -> 1,
K_mon(q)=relative_sign^(-1)(V_stab(q)).
```

Thus full voltage is equivalent to `K_mon(q)=S_d^s`, while trivial voltage
is equivalent to `K_mon(q)=P_(d,s)`. This isolates the exact qualitative
braid-stabilizer theorem still needed; inner loops contribute precisely the
kernel and cannot decide the orientation quotient.

## Field 7 — marked roots are not orientation data

An M135 incidence edge specifies an `H`-orbit at its source and target,
equivalently one marked white-root lift on each side. A route hitting the
marked roots says only

```text
mu_k(d)=d.
```

For `d>=3`, the point stabilizer of `d` contains permutations of both signs.
The marked-root condition therefore does not determine `sgn(mu_k)` and is
strictly weaker than zero voltage. All `d` root lifts, or equivalently the
orientation double cover, are essential.

## Field 8 — section/coboundary and boundary audit

Changing the physical source or target representative changes the displayed
fiber bijection by its endpoint relabelers. At the sign level this is exactly
M163's endpoint coboundary. The criterion above fixes the physical endpoints,
so it is intrinsic. Simultaneously relabeling both members of a matched pair
conjugates its root monodromy and preserves its sign.

The proof requires `d>=3` only for the free global action. At width `s=1`,
`W_1=0`, so stabilizer voltage is necessarily trivial and any existing
quotient route passes the relative-parity test. At every `s>=2`, the
orientation-cover criterion remains nontrivial. The accepted matching exact
sequence begins at `d>=5` because that is the scope of M141; no rank-four
extension is asserted.

No `d=5` Schreier closure, group-order computation, or finite matching audit
was run. This honors the mission cap and avoids turning a failed large closure
into evidence.

## Field 9 — remaining obligations, reproduction, and hygiene

The first unresolved qualitative statement is now exactly:

> For every accepted ordered `d>=5` M135 matching subfamily, determine the
> orientation deck-monodromy image `V_stab(q)<=F_2^s/Delta`; equivalently,
> determine whether `K_mon(q)=S_d^s`.

For specified source and target tuples, quotient-route existence and orbit
equality of their relative-orientation lifts are logically separate tests.
Even full voltage gives no polynomial braid word. Polynomial quotient-route
length and polynomial aligned inner-transporter length remain separate
quantitative obligations.

The mission is proof-only. `results.json` records claim status and the
deliberate absence of a `d=5` closure; there is no stochastic seed or finite
output to reproduce. Owned artifacts are `plan.md`, `checkpoint.md`,
`halfway_checkpoint.md`, `proof.md`, `results.json`, this report,
`freeze_manifest.md`, and `SHA256SUMS`. No predecessor, coordinator,
manuscript, project skill, or other mission file was edited.

```text
KEEP THE ROOT-MONODROMY AND RELATIVE-ORIENTATION-COVER THEOREMS.
KEEP THE ACCEPTED-MATCHING MONODROMY EXACT SEQUENCE.
LEAVE FULL d>=5 VOLTAGE, ROUTING, AND ALL WORD-LENGTH BOUNDS UNRESOLVED.
NO GAP, MIXING, OR TERMINAL INFERENCE.
```
