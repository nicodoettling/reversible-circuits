# M137 fresh referee report on frozen M135

Date: 2026-08-13 UTC. Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict and exact scope

```text
ACCEPT M135 AT ITS STATED NONTERMINAL SCOPE.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

M135 correctly proves the root-stabilizer orbit-incidence coloring

```text
chi(C_(d,i)) <= d,       d=3 or d>=5,
chi(C_(d,i)) <= d^6,     every d>=2,
```

and correctly isolates rank four by singleton classes.  It also correctly
refutes, at `d=3`, the stronger assertion that an incidence matching is
automatically realized by one fixed signed braid.  The remaining
**POLYNOMIAL MATCHING-COSET REFINEMENT** is a strict simultaneous-realization
obligation and remains unresolved.

```text
candidate                  | root-stabilizer orbit-incidence coloring
claimed target             | uniform physical minimal identity sector Z_d
identity ok                | brute/DPS exact at d=3,4; DPS/Hurwitz generally
crosses Hurwitz components | not applicable; no sampler or gap is claimed
exact diagnostics          | roots, equivariance, orbits, incidence, action cover
verdict                    | accept strict structural reduction; no gap claim
```

M135 proves no UST basis-exchange route, full rooted-product comparison,
physical minimal-sector gap, arbitrary-product `Gamma_0` result, original
lazy exact `{3,4,5}` heat-bath gap, Terminal A, or Terminal B.

## 2. Frozen provenance

All assigned immutable digests match exactly:

| M135 artifact | observed SHA-256 |
|---|---|
| `report.md` | `2d56c7e409b64f691309e950cc88aca471bfc68f84bc93f55d5d3a24b6974455` |
| `orbit_incidence_reduction.md` | `499fe5a0fd829f0fad88283e7592420e5ddbb3b0c8f89460a139f13928d4895c` |
| `conflict_coloring_audit.py` | `79ed378ae7fd7543c16bf12a1fa51e0144b817a938c91de196be960a2e6ad540` |
| `results.json` | `4a7c885629399f01805d49c96f99e65612f9d7c9fbf745becd285dd96c1c30b9` |
| `freeze_manifest.md` | `6428246337bd3c8ffc3228754e5aa6b2ee2b407d0f842421079d7798ade58541` |
| `SHA256SUMS` | `8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358` |

The fresh checker imports no M135 or predecessor module or result file.  It
only reads the frozen payload bytes to verify these assigned hashes.

## 3. Target, convention, and accepted dependencies

The auxiliary target is uniform on

```text
Z_d={(t_1,...,t_(2d-2)):t_1...t_(2d-2)=id,
                              support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  For transpositions, the signed right-Hurwitz actions are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

M135 uses only the accepted M112/M119 literal rooted DPS product with exactly
`d` white roots per physical word and M127/M130's root-independent physical
involutions `tau_i`.  M132/M134 supplies the definition of the paired-
subgroup conflict graph and the warning that conflict independence alone
does not imply simultaneous braid realization.  No new literature result or
unproved mixing input is introduced.

## 4. Root-stabilizer equivariance and orbit counts

Let `G=S_d` act by global conjugation and let `H=Stab_G(d)`.  In the accepted
rooted DPS construction the Cayley tree is rooted at the white vertex `d`.
For `rho in H`, relabeling the Cayley tree by `rho` and moving each ordered
black pair-slot to the slot indexed by `rho` carries the hairy incidences,
cyclic boundary, and intrinsic closure to their `rho`-images.  Changing the
conventional boundary start only rotates the same cyclic boundary and does
not alter the intrinsic closure.

Swapping the adjacent *values* `i,i+1` of the permutation coordinate commutes
with this slot relabeling.  After applying the already accepted
root-independence of `tau_i`, this proves

```text
tau_i(rho.w)=rho.tau_i(w),       rho in H.
```

The restriction is genuine: the fresh exact audit has zero `H`-equivariance
failures for every adjacent index at `d=3,4`, but nonzero failures for the
full `G` action.

If a global conjugation fixes a word coordinatewise, it centralizes every
factor.  Connected support means those factors generate `S_d`, so for
`d>=3` the conjugator lies in the trivial center.  The `G` and `H` actions
are therefore free.  Their orbit sizes are `d!` and `(d-1)!`, and each
`G`-orbit splits into exactly `[G:H]=d` `H`-orbits.  M135's freeness and
orbit-count claims are proved.

## 5. Goursat graph-versus-parity dichotomy

For `u,v in Z_d`, write

```text
D(u,v)=<(u_1,v_1),...,(u_m,v_m)> <= S_d x S_d,
P_d={(p,q):sgn(p)=sgn(q)}.
```

Connected support makes both coordinate projections of `D(u,v)` equal to
`S_d`.  Every literal generator is odd-odd, hence `D(u,v)<=P_d`.  Goursat's
kernel argument and the normal-subgroup classification leave, for `d=3` or
`d>=5`, only the following possibilities:

- trivial kernels, giving the graph of an automorphism of `S_d`;
- kernels `A_d`, giving exactly the parity-diagonal subgroup `P_d`; or
- kernels `S_d`, giving the full product.

The last case is impossible because `S_d x S_d` is not contained in `P_d`.
This explicit parity exclusion is necessary and is present in M135.

In the graph case, every displayed image is again a transposition, so the
automorphism preserves the transposition conjugacy class.  For `d>=5`,
noncommutation reconstructs incidence among edges of `K_d`; its unique
maximum pairwise-incident families are the vertex stars (a non-star family
is only a triangle).  The automorphism therefore permutes stars and is
conjugation by a vertex permutation.  At `d=3`, all automorphisms are inner.
At `d=6`, the exceptional outer automorphism cannot occur: the involution
classes of size 15 are transpositions and triple transpositions, and an outer
automorphism sends the former to the latter instead of preserving it.

Thus

```text
D(u,v)=graph(Ad_rho)  iff v=rho.u,
D(u,v)=P_d           otherwise,
```

for `d=3` and `d>=5`.  The proof correctly excludes `d=4`, where the extra
normal subgroup `V_4` permits an intermediate subdirect product.  The fresh
rank-three exhaustive check has zero dichotomy failures, while the rank-four
witness has literal paired subgroups

```text
(V_4 x V_4)Diag(S_4), order 96,
P_4,                  order 288,
```

before and after `tau_1`, with neither pair globally conjugate.

## 6. Regular incidence and conflict-independent matchings

For fixed `(d,i)`, M135 makes one bipartite edge for each `H`-orbit `Q`, from
the source global orbit containing `Q` to the target global orbit containing
`tau_i(Q)`.  Root-stabilizer equivariance makes the target endpoint
well-defined.  There are exactly `d` source `H`-orbits at each left vertex;
bijectivity of `tau_i` on `H`-orbits gives exactly `d` preimages at each
right vertex.  Hence this is a finite `d`-regular bipartite multigraph.

Hall's inequality follows by counting its `d|S|` incident edges against the
at-most-`d|N(S)|` available right incidences.  Removing a perfect matching
and iterating gives a proper `d`-edge-coloring, including parallel edges.

Each matching color is conflict-independent when `d=3` or `d>=5`:

- two states in the same `H`-orbit have the same literal conjugation-graph
  subgroup before and after `tau_i` by `H`-equivariance;
- two states in different matching edges share neither their left nor right
  endpoint, so both the source pair and target pair are nonconjugate and both
  paired subgroups equal `P_d`.

This proves `chi(C_(d,i))<=d` in the asserted ranks.  At `d=4`, singleton
classes give `chi<=|Z_4|=2880`, and the accepted DPS count satisfies
`2880=4*6!<4^6`.  The singleton, `d=3`, `d>=5`, and trivial `d=2` cases
together prove the stated uniform `d^6` bound.  The result is an existence
coloring; M135 correctly claims no compact coloring algorithm.

## 7. Simultaneous realization remains separate

Every signed braid action commutes with global conjugation, while `tau_i`
commutes with `H`; consequently a fixed-action agreement set is a union of
`H`-orbits.  For a representative `w_Q`, the endpoint fiber

```text
K_Q={a:a(w_Q)=tau_i(w_Q)}
```

is empty or a point-stabilizer coset.  A family of orbit edges is realized
by one action exactly when the corresponding `K_Q` have nonempty
intersection.  Nonemptiness of each atomic fiber retains the separately
tracked qualitative Hurwitz-transitivity dependency.  M135 does not turn
pairwise compatibility into an unjustified realization claim.

At `d=3`, each perfect matching has four `H`-orbits, hence eight physical
states.  Complete action-image closure gives maximum one-action agreement
six.  Therefore no incidence matching can be one-action realized.  The exact
minimum fixed-schedule cover is five.  This proves the stated refutation and
leaves polynomial matching-coset refinement, including polynomial word
length, unresolved.

Nonmaterial editorial note: the proof uses `A_d` first for the alternating
group and later for the finite braid-action image.  Renaming the latter
`mathcal A_d` would avoid a notation collision; the two uses are locally
unambiguous and do not affect any claim.

## 8. Independent exact audit

The new checker brute-enumerates the physical target before constructing the
accepted plus-mirror DPS image.  It independently reconstructs global and
root-stabilizer orbits, paired subgroups, the incidence coloring, and the
complete rank-three signed action image.

| check | `d=3` | `d=4` |
|---|---:|---:|
| brute `|Z_d|` | 24 | 2,880 |
| rooted DPS coordinates | 72 | 11,520 |
| root fiber | exactly 3 | exactly 4 |
| global orbits / size | 4 / 6 | 120 / 24 |
| `H`-orbits / size | 12 / 2 | 480 / 6 |
| `H`-orbits per global orbit | exactly 3 | exactly 4 |
| nontrivial word stabilizers | 0 | 0 |
| incidence edges / degree | 12 / 3 | 480 / 4 |
| matching-color physical sizes | three of 8 | four of 720 |
| `H`-equivariance failures | 0 | 0 |

For every adjacent index at `d=3`, the conflict graph has 80 edges and a
triangle, while the three exact matching colors contain zero conflict pairs.
Thus the fresh data independently gives `chi=3`.  Its complete action rows
are, for all three indices,

```text
action image order          216
nonempty agreement masks     23
maximum one-action agreement  6
minimum schedule cover        5
union-DP frontiers  1,23,206,811,1640,2021.
```

At `d=4`, the fresh checker reproduces zero root-stabilizer-equivariance
failures, regular degree four, the exact `96 -> 288` witness and subgroup
descriptions, nonconjugacy on both sides, and `2880<4096` for the singleton
patch.  These finite facts calibrate conventions and exceptions; the all-
rank theorem comes from Sections 4--6, not finite extrapolation.

## 9. Reproduction and hygiene

The deterministic command, run from the M137 directory, is

```text
python3 -B independent_referee.py
```

Python is `3.12.3`; dependencies are `{}`; `seed=null`.  The exact run took
about six seconds and wrote `independent_results.json`.

M137 owns only `plan.md`, `checkpoint.md`, `independent_referee.py`,
`independent_results.json`, this report, `freeze_manifest.md`, and
`SHA256SUMS`.  No M135, predecessor, coordinator, manuscript, project-skill,
or other mission file is edited.

## 10. Final decision

```text
ACCEPT. ZERO MATERIAL NUMBERED OBJECTIONS.
```

Promote M135's exact scope: the all-rank polynomial conflict coloring, the
sharper `d`-color theorem away from rank four, the explicit rank-four
singleton patch, and the `d=3` refutation of automatic matching realization.
Keep the matching-coset refinement and braid-length bound unresolved.  No
gap or terminal claim follows.
