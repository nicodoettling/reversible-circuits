# M176 substantive audit notes

## 1. Local transporter and inverse convention

Fix a section `sigma:Q_d -> Z_d` and write

```text
g sigma(a) = rho_g(a).sigma(ga).
```

The free simultaneous relabeling action makes `rho_g(a)` unique. Applying
`g^{-1}` and using commutation with relabeling gives

```text
rho_(g^{-1})(ga) = rho_g(a)^{-1}.
```

Thus the reverse directed edge has the same sign bit. For a chronological
route `g_1,...,g_L`, the physical transporter is the ordered product of its
local transporters (the nonabelian order depends on the action convention),
while parity is unambiguously the sum of local sign bits. Therefore M175's
tuple gain

```text
gamma_g(a_1,...,a_s)
 = [sgn rho_g(a_1),...,sgn rho_g(a_s)] in F_2^s/Delta
```

is exactly the accepted M163 voltage and, by M169, exactly the relative sign
of root monodromy. The signed inverse implemented in both M175 and the M176
checker is

```text
R_j^{-1}(a,b)=(a b a^{-1},a),
```

which is the inverse of `R_j(a,b)=(b,b^{-1}ab)` under the declared
composition convention.

## 2. Fundamental-cycle span: both inclusions

Let `T` be a spanning tree of the actual synchronized signed-generator
Schreier component rooted at `q`, and let `p(x)` be the gain on its literal
tree route `q -> x`. For every directed edge `e:x -> y`, put

```text
z(e)=p(x)+gamma(e)+p(y).
```

Realizability is literal: concatenate the tree word `q -> x`, generator edge
`e`, and the signed inverse of the tree word `q -> y`. This is an actual
signed braid word closing at `q`, including when `e` is a loop or a parallel
edge, and its voltage is exactly `z(e)`. Hence every chord column, and every
binary sum of them by concatenation, lies in `V_stab(q)`.

Conversely, let a stabilizer word trace a closed walk
`x_0=q,x_1,...,x_L=q` with directed edges `e_l:x_(l-1)->x_l`. Then directly
over `F_2`:

```text
sum_l z(e_l)
 = sum_l gamma(e_l)
   + sum_l (p(x_(l-1))+p(x_l))
 = gain(C),
```

because the potential terms telescope in pairs. Every stabilizer voltage is
therefore in the chord span. This proves M175 Theorem 3.1 exactly; it is not
a relaxation to independently selected coordinate paths. It supplies no
diameter or polynomial word-length bound.

## 3. Section and endpoint formulas

Under a section change `sigma'(a)=eta(a).sigma(a)`, the local sign changes by
the vertex coboundary

```text
kappa'_g(a)=sgn eta(a)+kappa_g(a)+sgn eta(ga).
```

Consequently tuple tree potentials acquire the corresponding endpoint
coboundary, but every `z(e)` is unchanged. Thus the chord span and
`V_stab(q)` are section-independent.

For fixed physical endpoints write

```text
U=n_U.sigma(q),  V=n_V.sigma(r),
b_T sigma(q)=c_T.sigma(r).
```

The physical transporter of the tree route relative to `U,V` is

```text
tau_T=n_U c_T n_V^{-1},
a_T(U,V)=relative_sign(tau_T).
```

All physical route voltages are exactly `a_T(U,V)+V_stab(q)`, because the
difference between any route and the tree route is a literal stabilizer
loop. Since `W_s` has exponent two, zero is present iff `a_T(U,V)` belongs to
the chord span. If the section changes while the physical endpoints remain
fixed, the endpoint coordinates and `c_T` change compatibly and `a_T(U,V)`
itself is unchanged. Independently replacing the physical endpoints instead
translates `a_T` by their endpoint coboundary; that is a different declared
fixed-endpoint problem. M175's final report makes this distinction correctly.

## 4. M169 exact-sequence interface

For an accepted nonempty ordered `d>=5` matching subfamily, M169/M172 gives
the relative-sign homomorphism

```text
lambda:K_mon(q)->W_s,
ker(lambda)=P_(d,s),  image(lambda)=V_stab(q),
```

where the kernel equality uses the independently accepted inclusion
`P_(d,s)<=K_mon(q)`. Thus

```text
1 -> P_(d,s) -> K_mon(q) -> V_stab(q) -> 1
```

and Theorem 3.1 legitimately identifies `K_mon(q)/P_(d,s)` with the chord
column space. This corollary has exactly the accepted `d>=5` matching scope;
M175 does not extend it to its exceptional `d=4` calibration.

## 5. Bounded exact replay

The independent M176 checker reconstructs all of `Z_3`, `Q_3`, the signed
local cocycle, and all ordered quotient pairs. It obtains exactly

```text
|Z_3|=24, |Q_3|=4,
(pair component size, chord rank)=(4,0),(12,0).
```

The augmented relative-orientation closure independently confirms the root
voltage set `{0}` in both components.

At `d=4`, M176 follows the coordinator's cap and replays only the displayed
literal certificate, without closing `Q_4`. Applying the chronological list
`[R_4,R_3,R_5,R_4]` to M175's two physical words closes both absolute
quotient points. The exact transporters are

```text
(0,1,3,2), sign 1;   (1,0,3,2), sign 0,
```

and the independently accumulated local canonicalization sign lists are
`[0,1,0,0]` and `[0,0,0,0]`. Hence the relative voltage is one. Because
`W_2` is one-dimensional, this proves full rank in that certificate's
component.

M175's remaining `d=4` component histogram was inspected rather than
re-enumerated: its checker visits all `120^2=14400` pairs, computes every
fundamental-cycle bit, and cross-checks every component by an independent
augmented-cover BFS. The recorded rows
`(120,0),(240,0),(4320,1),(9720,0)` sum to all pairs; no algorithmic defect
was found. The rank-one row is independently certified as above.

## 6. Numbered objections and clarifications

Material objections: none.

1. **Nonmaterial chronology notation.** Sections 6/report Field 7 call
   `R_4 R_3 R_5 R_4` a *chronological* word. The JSON and checker clearly
   mean the left-to-right application list `[4,3,5,4]`. If the symbols are
   instead read as the algebraic product `b=g_L...g_1` used in proof (2.4),
   the written product for that route is reversed. A durable citation should
   retain the phrase "chronological application list" or print the list.
   This does not affect the exact certificate.
2. **Nonmaterial section wording.** The last paragraph of proof Section 5
   compresses section changes and independent physical-endpoint changes into
   one sentence. For fixed physical endpoints, changing only the section
   leaves endpoint-corrected `a_T(U,V)` invariant; changing the physical
   endpoints translates it. The final report distinguishes these cases, and
   the theorem is correct.
3. **Boundary notation.** "Every tuple width" should be read as `s>=1`.
   At `s=1`, `W_1=0` and all claims reduce correctly. Empty width is not an
   accepted matching subfamily and is not defined by the displayed `Delta`.

No clarification changes a theorem, finite certificate, or scope verdict.
