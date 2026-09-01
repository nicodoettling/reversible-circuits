# M135 final report: orbit-incidence conflict coloring

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and exact scope

```text
FINAL VERDICT: KEEP AS A STRICT STRUCTURAL REDUCTION.
PROVED: chi(C_(d,i)) <= d for d=3 and every d>=5.
PROVED: the uniform all-rank bound chi(C_(d,i)) <= d^6.
REFUTED at d=3: automatic one-braid realization of the d matching colors.
UNRESOLVED: polynomial matching-coset refinement with polynomial braid length.
```

This fully discharges the **conflict-coloring** half of M132/M134's surviving
frontier. The remaining issue is only simultaneous realization. The theorem
uses an intrinsic orbit-incidence multigraph and does not reuse the refuted
`O(d^40)` contour key.

```text
candidate                  | root-stabilizer orbit-incidence edge coloring
claimed target             | uniform physical minimal identity sector Z_d
identity ok                | exact d=3,4; DPS/Hurwitz preserve it generally
crosses Hurwitz components | not applicable; no sampler or gap is claimed
exact diagnostics          | DPS roots, equivariance, conjugacy orbits, action cover
verdict                    | keep proved coloring and exact coset reduction
```

No UST basis-exchange route, all-edge comparison, physical gap, arbitrary-
product `Gamma_0` result, original heat-bath gap, Terminal A, or Terminal B
is proved or refuted.

## Field 2 — target, convention, kernel context, and dependencies

For `d>=2`, `m=2d-2`, the auxiliary target is uniform on

```text
Z_d={(t_1,...,t_m):t_1...t_m=id,
                         support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. Signed right-Hurwitz actions are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

The associated half-lazy physical kernel `P_(0,d)` is context only and is not
bounded here. Accepted dependencies are M112/M119's rooted DPS bijection and
exact `d`-to-one root quotient, plus M127/M130's root-independent physical
involutions `tau_i`. The proof also uses standard proved group facts: connected
transpositions generate `S_d`; the normal subgroups of `S_3` and of `S_d` for
`d>=5`; Goursat's kernel argument; and Hall's theorem. No new literature
dependency is introduced.

## Field 3 — root-stabilizer equivariance

Let `G=S_d` act on words by global conjugation and put

```text
H=Stab_G(d) ~= S_(d-1).
```

Relabel a rooted DPS Cayley tree and its black-vertex pair slots by any
`rho in H`. The hairy incidence, cyclic boundary, and intrinsic closure are
carried to their `rho`-images. Swapping the values `i,i+1` of `pi` commutes
with this slot relabeling. Therefore

```text
tau_i(rho.w)=rho.tau_i(w)                              (3.1)
```

for every `d,i,w,rho`. This is **PROVED** in
`orbit_incidence_reduction.md`. It is deliberately not extended to all of
`G`; exact source conjugacy orbits can split into `d` target orbits.

Global conjugation acts freely for `d>=3`: a stabilizer centralizes the
connected transposition support, hence all of `S_d`, whose center is trivial.
Thus every `G`-orbit has size `d!`, every `H`-orbit has size `(d-1)!`, and a
`G`-orbit contains exactly `d` `H`-orbits.

## Field 4 — exact paired-subgroup dichotomy

For `u,v in Z_d`, let

```text
D(u,v)=< (u_1,v_1),...,(u_m,v_m) > <= S_d x S_d,
P_d={(p,q):sgn(p)=sgn(q)}.
```

Both projections of `D(u,v)` are `S_d`, while every literal generator is
odd-odd, so `D(u,v)<=P_d`. For `d=3` or `d>=5`, Goursat leaves only:

- the graph of an automorphism, when the two kernel groups are trivial; or
- `P_d`, when both kernels are `A_d`.

Goursat's full-product case is excluded explicitly by `D(u,v)<=P_d`. In the
graph case the automorphism maps transpositions to transpositions. The
incidence graph of transpositions reconstructs the vertex stars of `K_d`, so
such an automorphism is inner. At `d=6` this also rules out the exceptional
outer automorphism: it cannot preserve transpositions and consequently swaps
their size-15 involution class with the triple-transposition class.

Hence, for `d=3` or `d>=5`,

```text
D(u,v)=graph(Ad_rho)  iff v=rho.u,
D(u,v)=P_d           otherwise.                       (4.1)
```

This dichotomy is **PROVED**. Rank four is the exact exception because of
`V_4`: M132's independently reconstructed nonconjugate-to-nonconjugate pair
changes subgroup order `96 -> 288`.

## Field 5 — the proved polynomial conflict coloring

Fix `d,i`. Make a bipartite multigraph `B_(d,i)` with one edge per `H`-orbit
`Q` in `Z_d`. Its left endpoint is the global `G`-orbit containing `Q`; its
right endpoint is the global `G`-orbit containing `tau_i(Q)`. Equation (3.1)
makes the right endpoint well-defined.

Every left and right degree is exactly `d`. Repeated perfect matchings give a
proper `d`-edge-coloring. Union the physical `H`-orbits of each edge color.
Within one `H`-orbit, (3.1) preserves the same literal graph subgroup. Across
different edges of one matching, both the source and target global orbits are
different, so (4.1) gives `P_d` before and after. Each color is therefore
conflict-independent. This proves

```text
chi(C_(d,i)) <= d,           d=3 or d>=5.              (5.1)
```

At `d=2`, the target is a singleton. At `d=4`, use the `2,880` singleton
classes; the exact DPS count gives

```text
2880=4*6! < 4^6.
```

Thus the uniform all-rank result is

```text
chi(C_(d,i)) <= d^6,         every d>=2.               (5.2)
```

This is an existence theorem. No efficient compact algorithm for evaluating
a fixed edge coloring on an exponentially large state space is claimed.

## Field 6 — simultaneous realization is an exact coset intersection

Let `A_d` be the finite signed-braid action image on `Z_d`. Braid actions
commute with all global conjugations, while `tau_i` commutes with `H`.
Therefore every fixed-action agreement set is a union of `H`-orbits.

For an `H`-orbit `Q`, choose `w_Q` and put

```text
K_Q={a in A_d:a(w_Q)=tau_i(w_Q)}.
```

This is empty or a point-stabilizer coset. A family `S` of orbit edges is
realized by one fixed action exactly when

```text
intersection_(Q in S) K_Q != empty.                   (6.1)
```

Thus the first unproved step is **POLYNOMIAL MATCHING-COSET REFINEMENT**:
for `d>=5`, refine the `d` matchings into `d^O(1)` total subfamilies, each
having an intersection (6.1) with a representative signed braid of length
`d^O(1)`. This is **UNRESOLVED**. Qualitative nonemptiness for each atomic
orbit additionally depends on the separately tracked connected-support
Hurwitz-transitivity input; the coloring theorem does not.

## Field 7 — exact finite calibration and falsification

The independent script reconstructs the accepted plus-mirror DPS map rather
than importing predecessor code or output.

At `d=3`:

```text
|Z_3|=24, rooted coordinates=72,
global G-orbits=4 of size 6, H-orbits=12 of size 2,
B_(3,i): 4+4 vertices, 12 edges, degree 3,
three edge colors: 8 physical states each, zero paired conflicts.
```

Complete closure of the signed action image independently gives, for every
adjacent index,

```text
|A_3|=216, max one-action agreement=6,
exact minimum schedule cover=5.
```

Every three-edge-color class has size eight, so no such class can be one-
schedule realized. The named assertion

```text
every orbit-incidence matching is one-schedule realizable
```

is therefore **REFUTED at `d=3`**, even though every matching is conflict-
independent.

At `d=4`, the script reconstructs `|Z_4|=2,880`, 120 global orbits, 480
`H`-orbits, degree-four incidence, and zero root-stabilizer equivariance
failures. It also directly checks the rank-four exception: both source and
target pairs are nonconjugate, while paired subgroup order changes
`96 -> 288`. The computed four edge colors at rank four are not promoted as
conflict-independent; (5.2) uses singletons.

All small-rank rows are **EXACT FINITE** convention/falsification facts. The
all-rank coloring is proved separately, not inferred from them.

## Field 8 — conditional recovery, reproduction, artifacts, and hygiene

If a future refinement supplies `q(d)` fixed schedules of length at most
`L(d)`, prefix inversion gives at most one physical source conditional on
`(i,class,scheduled time,direction)` and a directed physical action. Deleting
scheduled holds costs at most another factor `L(d)`. Including the `2d-3`
indices and exact `d` white roots gives descriptor bounds

```text
2d(2d-3)q(d)L(d),       scheduled time retained,
2d(2d-3)q(d)L(d)^2,     compressed time only.
```

These are polynomial when `q,L` are; no all-edge stationary congestion is
claimed.

Deterministic reproduction, Python `3.12.3`, dependencies `{}`, `seed=null`:

```text
python3 -B conflict_coloring_audit.py --d 3 4 --output results.json
python3 -c 'from pathlib import Path; p=Path("conflict_coloring_audit.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
```

Owned artifacts are `plan.md`, `checkpoint.md`,
`orbit_incidence_reduction.md`, `conflict_coloring_audit.py`, `results.json`,
this report, `freeze_manifest.md`, and `SHA256SUMS`. No predecessor,
coordinator, manuscript, skill, or file outside this mission directory is
edited.

## Field 9 — final decision and open obligations

```text
KEEP THE ORBIT-INCIDENCE THEOREM: chi(C_(d,i)) <= d^6.
KEEP d COLORS FOR d=3 AND d>=5; KEEP d=4 SINGLETON PATCH EXPLICIT.
KEEP THE d=3 REFUTATION OF AUTOMATIC MATCHING REALIZATION.
```

The next admissible positive step is the polynomial matching-coset refinement
with a polynomial braid-length bound. A negative asymptotic result would need
a superpolynomial lower bound on the number of nonempty coset-intersection
subfamilies or on their shortest representatives; another finite collision
would not suffice.

UST basis exchanges, the full rooted-product comparison, every physical gap,
arbitrary-product `Gamma_0`, the original exact heat-bath chain, and both
terminal outcomes remain unresolved.
