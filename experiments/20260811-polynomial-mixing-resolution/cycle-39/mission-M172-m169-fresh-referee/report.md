# M172 fresh referee report on frozen M169

Date: 2026-08-13 UTC. Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict, numbered objections, and exact scope

```text
FINAL DECISION: ACCEPT M169 AT ITS EXACT QUALITATIVE, NONTERMINAL SCOPE.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

M169 correctly identifies transporter parity with white-root monodromy sign,
constructs the relative-orientation cover, gives the fixed-physical-endpoint
zero-coset criterion, and proves for accepted nonempty `d>=5` M135 matching
subfamilies

```text
1 -> P_(d,s) -> K_mon(q) -> V_stab(q) -> 1.
```

It does not determine `V_stab` at `d>=5`, supply a specified quotient route,
bound braid length, or imply any spectral or terminal result.

Numbered objections:

1. None.

Nonmaterial notation clarification: throughout the tuple-cover claim,
`O_(d,s)` must mean the diagonal-deck quotient
`Z_d^s/P_(d,s)`, not the unquotiented product `O_d^s`. M169's final report
states exactly this correct formula; its proof's preceding verbal construction
has the same meaning.

```text
candidate                  | root monodromy / relative-orientation reduction
claimed target             | qualitative diagonal signed-Hurwitz orbit lifting
identity ok                | Hurwitz and relabeling preserve product one
crosses Hurwitz components | not applicable; no sampler or gap is claimed
exact diagnostics          | bounded clean-room S_3 root/orientation audit
verdict                    | accept exact structural theorem only
```

## Field 2 — immutable provenance and hash gate

M169's relative-name checksum list passed from its intended frozen directory
before any conclusion. Frozen M141/M143, M154/M158, and M163/M164 checksum
lists also passed before their results were used. No frozen file was imported,
executed, or modified.

| frozen M169 artifact | observed SHA-256 |
|---|---|
| `plan.md` | `89092dc1069753e39ea33fb08c3e78c1e84383e09eb1ff65fd3464d3679b3ae1` |
| `checkpoint.md` | `2945a8c24af0f8ea592e321967381ac5f9ba4c3e4cf8b692fdf4f57932e4ec6b` |
| `halfway_checkpoint.md` | `8820fcb9e9b4f89216b4ab319cf0ce989e4f5b92aca5fc3a98f0c993762aaeb9` |
| `proof.md` | `8cedecf4a3f1c3f56996f3b66cc9991a43cc7c0162ee1c794c460ce1631ea936` |
| `results.json` | `cf9800d0ddefd982419e39157a6571af258997d06d630c4aed5c5231edd4d377` |
| `report.md` | `b6cd6b9bfbc571789f2e4e6e2d8c2df8da292f72c6049dc9ad648dac9b777729` |
| `freeze_manifest.md` | `f5d68a368c9e1579a86d162cc7bc66b740593beb8a98e58d72941be9a48df512` |
| `SHA256SUMS` | `1798d68d10f3fa3b2b113e055e869c3f27eaf8e105e9387e7856fa261fd62b29` |

## Field 3 — target, freeness, and rooted quotient

For `d>=3`, M169 works on

```text
Z_d={(t_1,...,t_(2d-2)): product=id, support connected on [d]},
Q_d=Z_d/S_d.
```

Permutations use `(pq)(x)=p(q(x))`; the braid acts by the stated signed
right-Hurwitz moves, and `S_d` acts by simultaneous relabeling. The two
actions commute. Connected transposition support generates `S_d`, so a
relabeler fixing a word centralizes `S_d`; its center is trivial for `d>=3`.
The relabeling action on `Z_d` is therefore free.

Put `H=Stab_(S_d)(d)`. The map

```text
Z_d/H -> (Z_d x [d])/S_d,       [w]_H |-> [w,d]
```

is well-defined, injective, and surjective. Freeness also shows that the
fiber over `[w] in Q_d` consists of the `d` distinct points `[w,a]`. Hence
M169's `R_d` is exactly the physical `d`-sheeted white-root quotient used in
the accepted incidence construction; it introduces no section choice.

## Field 4 — inverse transporter and root-monodromy group law

If a quotient loop `h` satisfies `h.w=rho.w`, then

```text
h.[w,a]=[rho.w,a]=[w,rho^(-1)(a)].
```

Thus the induced root permutation is exactly `mu(h)=rho^(-1)`, and
`sgn(mu)=sgn(rho)`. The same calculation with source trivialization `u` and
target trivialization `v` proves the route formula when `b.u=rho.v`.

The inverse is also what turns the transporter anti-homomorphism into the
actual monodromy homomorphism. If `h_i.w=rho_i.w`, commutation of braid and
relabeling gives

```text
rho(h_2 h_1)=rho_1 rho_2,
mu(h_2 h_1)=rho_2^(-1)rho_1^(-1)=mu(h_2)mu(h_1).
```

Therefore the image called `K_mon(q)<=S_d^s` is genuinely a subgroup, with
the composition convention used in M169. No parity sign is lost by inversion.

## Field 5 — tuple relative-orientation cover and `V_stab`

For width `s`, coordinatewise sign gives the surjective homomorphism

```text
lambda:S_d^s -> W_s=F_2^s/Delta,
ker(lambda)=P_(d,s)
 ={(g_1,...,g_s):sgn(g_1)=...=sgn(g_s)}.
```

Because `P_(d,s)` is normal, the exact regular cover is

```text
O_(d,s)=Z_d^s/P_(d,s) -> Z_d^s/S_d^s=Q_d^s,
deck group W_s.
```

The diagonal braid action commutes with its deck action. For a base tuple
`q`, its point-stabilizer monodromy on this cover is precisely

```text
lambda(K_mon(q))
 ={relative signs of its physical transporters}
 =V_stab(q).
```

Over one base braid orbit, choose one lifted point. Two deck translates lie
in the same lifted braid orbit exactly when their quotient in `W_s` lies in
`V_stab(q)`. Thus the lifted orbits are indexed by `W_s/V_stab(q)`, exactly
as M169 states. This is a group-action fact, not a finite extrapolation.

## Field 6 — fixed physical endpoints, coboundary, and marked roots

Fixed physical tuples `U,V` define the points `[U]_[P]` and `[V]_[P]` in
`O_(d,s)`. If a quotient route has unique transporter tuple `rho`, then it
maps these two relative-orientation lifts exactly when

```text
rho in P_(d,s)
iff all coordinate monodromy signs agree
iff its fixed-endpoint relative voltage is zero.
```

This proves M169's four-way zero-coset/orientation-orbit equivalence, under
its explicit assumption that at least one quotient route exists.

The endpoint warning is essential and correct. If
`U'=alpha.U`, `V'=beta.V`, then the same route has transporter

```text
rho'=alpha rho beta^(-1),
lambda(rho')=lambda(alpha)+lambda(rho)+lambda(beta).
```

Independent endpoint changes can therefore translate the displayed affine
coset. Applying the same coordinatewise relabeler at both ends conjugates
`rho` and preserves its sign. The criterion is intrinsic for the declared
physical endpoints, not for arbitrary independently chosen lifts.

An M135 marked white-root hit imposes only `mu_k(d)=d`. Since
`Stab(d)~=S_(d-1)` contains both parities for `d>=3`, this does not determine
orientation and is strictly weaker than zero relative voltage. M169's warning
is correct.

## Field 7 — exact sequence: inclusion, kernel, and surjectivity

Let `q` be the ordered source or target tuple of a nonempty subfamily of one
accepted `d>=5` M135 matching. Accepted M141/M143 proves that its aligned
factor tuples generate exactly `P=P_(d,s)`. Accepted M154/M158 proves that
for every `p in P` a literal braid sends the aligned word `X` to

```text
p^(-1) X p.
```

This braid fixes `q` in the absolute quotient. In the relabeling convention
its transporter is `p^(-1)`, so its root monodromy is `p`. As `p` ranges over
`P`, this proves the crucial inclusion

```text
P_(d,s) <= K_mon(q).
```

Restrict `lambda` from Field 5 to `K_mon(q)`. Its image is `V_stab(q)` by
definition, so the map is surjective. Its kernel is

```text
K_mon(q) intersect ker(lambda)
=K_mon(q) intersect P_(d,s)
=P_(d,s),
```

where the final equality uses the displayed inclusion. This proves every
arrow, the kernel, and surjectivity in

```text
1 -> P_(d,s) -> K_mon(q) -> V_stab(q) -> 1.
```

It also proves M169's stronger full-preimage identity. If
`lambda(x) in V_stab`, choose `k in K_mon` with the same image; then
`xk^(-1) in P<=K_mon`, hence `x in K_mon`. Therefore

```text
K_mon(q)=lambda^(-1)(V_stab(q)).
```

Consequently full voltage is equivalent to `K_mon=S_d^s`, and zero voltage
is equivalent to `K_mon=P_(d,s)`. These conclusions are qualitative: M154's
factor generation supplies no polynomial word-length bound.

## Field 8 — bounded clean-room symbolic audit

`independent_symbolic_audit.py` imports no predecessor module or data. It
reconstructs only `S_3`, all 24 words in `Z_3`, their four absolute classes,
the rooted quotient, signed Hurwitz edges, the two-coordinate monodromy
closure, and the relative-orientation lift.

| check | exact result |
|---|---:|
| `Z_3`, `Q_3` sizes | `24`, `4` |
| `Z_3/H` and rooted-cover sizes | `12`, `12` |
| signed-Hurwitz inverse checks | `144`, zero failures |
| inverse-monodromy root checks | `72`, zero failures |
| ordered-distinct base orbit | `12` |
| augmented root states | `216` |
| actual `K_mon` and `P_(3,2)` orders | `18`, `18`, equal |
| relative-orientation orbit | `12`, with two deck-coset orbits total |
| fixed-endpoint equivalence checks | `12`, zero failures |
| endpoint coboundary checks | `3456`, zero failures |

These finite facts test conventions and possible counterexamples only. The
general exact sequence rests on the proof and accepted inputs in Field 7;
no `d=5` closure or finite all-rank inference was attempted.

## Field 9 — remaining obligations, reproduction, and hygiene

The first unresolved structural question remains exactly:

> For every accepted nonempty ordered `d>=5` M135 matching subfamily,
> determine `V_stab(q)<=F_2^s/Delta`, in particular whether it is full.

For specified source and target tuples, quotient-route existence and orbit
equality of their fixed relative-orientation lifts remain separate. Even full
voltage would not provide a polynomial quotient route or a polynomial inner
correction. No physical-sector gap, original lazy exact `{3,4,5}` heat-bath
gap, mixing theorem, Terminal A, or Terminal B follows.

Deterministic reproduction from this M172 directory, Python `3.12.3`,
standard library only, `seed=null`:

```text
python3 -B independent_symbolic_audit.py
```

Owned artifacts are `plan.md`, `checkpoint.md`, `halfway_checkpoint.md`,
`independent_symbolic_audit.py`, `independent_results.json`, this report,
`freeze_manifest.md`, and `SHA256SUMS`. M169 and every predecessor remain
unmodified.

```text
ACCEPT. ZERO MATERIAL NUMBERED OBJECTIONS.
PROMOTE ONLY THE ROOT-MONODROMY, RELATIVE-ORIENTATION, FIXED-ENDPOINT,
AND ACCEPTED-MATCHING EXACT-SEQUENCE THEOREMS.
LEAVE FULL d>=5 VOLTAGE, ROUTING, LENGTH, EVERY GAP, AND TERMINALS UNRESOLVED.
```
