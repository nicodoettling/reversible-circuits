# White-root monodromy and the exact relative-orientation criterion

Date: 2026-08-13 UTC.

## 1. Scope and convention

Let `d>=3`, `m=2d-2`, and let `Z_d` be the connected product-one length-`m`
transposition words in `S_d`. Write `G=S_d` and let `G` act by simultaneous
relabeling

```text
rho.w=(rho t_1 rho^(-1),...,rho t_m rho^(-1)).
```

The literal signed braid group `B=B_m` acts chronologically by

```text
R_j(a,b)=(b,b^(-1)ab),
R_j^(-1)(a,b)=(aba^(-1),a).
```

The two actions commute. The `G`-action on `Z_d` is free: a relabeler fixing
a connected word centralizes its factors, hence all of `S_d`, and the center
of `S_d` is trivial. Put `Q_d=Z_d/G`.

This note concerns only qualitative orbit lifting. It does not bound braid
word length.

## 2. The `d`-sheeted white-root cover

Define

```text
R_d=(Z_d x [d])/G,
gamma.(w,a)=(gamma.w,gamma(a)),
p([w,a])=[w]_G.
```

Freeness shows that every fiber of `p:R_d->Q_d` has exactly `d` elements.
If `H=Stab_G(d)`, the map

```text
Z_d/H -> R_d,             [w]_H |-> [w,d]
```

is a bijection. Thus this is precisely the intermediate cover whose points
are the M135 white-root or `H`-orbit lifts; no new choice of a DPS section is
being introduced.

The braid action lifts by `b.[w,a]=[b.w,a]`. It is well-defined because braid
and relabeling commute.

### Lemma 2.1 (rooted-cover monodromy; **PROVED**)

Fix `w in Z_d`, let `q=[w]_G`, and identify the root fiber over `q` with
`[d]` by `iota_w(a)=[w,a]`. If `h in B` fixes `q` and

```text
h.w=rho.w
```

for its unique physical transporter `rho in S_d`, then the monodromy of `h`
on the `d` white-root lifts is

```text
iota_w^(-1) h iota_w = rho^(-1).                     (2.1)
```

Consequently `sgn(root monodromy)=sgn(rho)`.

**Proof.** For every root label `a`,

```text
h.[w,a]=[rho.w,a]=[w,rho^(-1)(a)],
```

where the last equality applies the diagonal relabeler `rho^(-1)` in the
definition of `R_d`. This is (2.1); inversion preserves sign. QED.

The same calculation applies to a route between distinct base points. If
`u,v in Z_d` and `b.u=rho.v`, then the induced fiber bijection, expressed in
the two fixed physical trivializations, is

```text
mu_(b;u,v)=iota_v^(-1) b iota_u=rho^(-1).             (2.2)
```

This is the rooted-cover interpretation of M163's transporter parity.

## 3. Tuples and the relative-orientation cover

For an ordered width-`s` quotient tuple `q=(q_1,...,q_s)`, a stabilizer braid
has one white-root monodromy `mu_k in S_d` at each coordinate. Define its
relative orientation vector by

```text
omega(h,q)=(sgn(mu_1),...,sgn(mu_s)) mod Delta,
Delta=<(1,...,1)> <= F_2^s.                           (3.1)
```

Lemma 2.1 proves immediately that

```text
V_stab(q)={omega(h,q):h in B_q};                      (3.2)
```

that is, M163's point-stabilizer voltage image is exactly the relative sign
image of simultaneous monodromy on the physical `d`-root fibers.

There is an entirely section-free formulation. Quotient the rooted fiber by
orientation, equivalently use the double cover

```text
O_d=Z_d/A_d -> Q_d=Z_d/S_d.
```

For tuples, quotient the product deck group `F_2^s` by its diagonal subgroup.
The resulting regular relative-orientation cover `O_(d,s)->Q_d^s` has deck
group `W_s=F_2^s/Delta`. Equation (3.2) says that `V_stab(q)` is literally
the deck-monodromy image of the braid point stabilizer on this cover. Hence,
over one quotient-tuple braid orbit, the lifted braid orbits are indexed by
cosets of `V_stab(q)` in `W_s`.

## 4. Exact source-to-target zero-coset condition

Fix physical endpoint tuples

```text
U=(u^1,...,u^s),        V=(v^1,...,v^s),
q=([u^1],...,[u^s]),    r=([v^1],...,[v^s]).
```

They determine points `U^or,V^or` of the relative-orientation cover. If a
braid `b` routes `q` to `r`, let `mu_k=mu_(b;u^k,v^k)` be (2.2).

### Theorem 4.1 (physical zero-coset criterion; **PROVED**)

Assume at least one quotient route from `q` to `r` exists. The following are
equivalent:

1. the fixed-endpoint M163 route-voltage coset contains zero;
2. some quotient route `b` has `sgn(mu_1)=...=sgn(mu_s)`;
3. some quotient route induces root-fiber bijections that either all preserve
   or all reverse the physical white-root orientations;
4. `U^or` and `V^or` lie in the same braid orbit in `O_(d,s)`.

**Proof.** By (2.2), `sgn(mu_k)=sgn(rho_k)` for the unique M154/M163
transporter `rho_k`. Thus (1)--(3) say exactly that the parity vector lies in
`Delta`. The relative-orientation cover identifies precisely vectors differing
by `Delta`, so a lifted route from `U^or` to `V^or` is the same condition. QED.

This is invariant for the fixed physical endpoints. Replacing `u^k` and
`v^k` independently changes the displayed signs by the two endpoint
orientation changes, exactly M163's coboundary. Replacing a matched pair
simultaneously by `alpha.u^k,alpha.v^k` conjugates its monodromy by `alpha`
and does not change its sign.

For an M135 edge, the source and target `H`-orbits give marked root lifts
`[u^k,d]` and `[v^k,d]`. Hitting those marked roots merely says
`mu_k(d)=d`; it does **not** determine `sgn(mu_k)`. The actual zero-coset
test must retain the orientation of all `d` white-root lifts, as in Theorem
4.1.

## 5. Accepted `d>=5` M135 matching subfamilies

Let `q` be a nonempty ordered subfamily of one accepted M135 matching and
choose its fixed physical representatives. Let `K_mon(q)<=S_d^s` be the
tuple root-monodromy group of its quotient point stabilizer.

Accepted M141/M143 says that the aligned factors generate

```text
P_(d,s)={(g_1,...,g_s):sgn(g_1)=...=sgn(g_s)}.
```

Accepted M154/M158 realizes simultaneous conjugation by every element of
this group using literal braid loops. Lemma 2.1 therefore gives

```text
P_(d,s) <= K_mon(q).                                  (5.1)
```

Since `P_(d,s)` is exactly the kernel of relative sign, the first isomorphism
theorem yields the exact sequence

```text
1 -> P_(d,s) -> K_mon(q) -> V_stab(q) -> 1,           (5.2)
```

and `K_mon(q)=relative_sign^(-1)(V_stab(q))`. Thus `V_stab` is precisely the
remaining orientation quotient of the physical tuple monodromy after the
accepted inner `P_(d,s)` loops. Full voltage is equivalent to full monodromy
`S_d^s`; zero voltage is equivalent to monodromy exactly `P_(d,s)`.

## 6. What remains unresolved

The structural theorem determines the intrinsic object and the actual
source-to-target zero test. It does not decide whether every accepted
`d>=5` matching subfamily has `V_stab=W_s`, nor prove that two specified
quotient tuples are routed at all.

Even if `V_stab=W_s`, the conclusion is qualitative: it gives no polynomial
word for a desired monodromy, no polynomial quotient route, and no polynomial
aligned-generator expression for the final inner correction. No gap, mixing,
or terminal conclusion follows.
