# M143 fresh referee report on frozen M141

Date: 2026-08-13 UTC. Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and numbered objections

```text
ACCEPT M141 AT ITS EXACT NONTERMINAL SCOPE.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

M141 correctly proves that, for `d>=5`, every nonempty subfamily of an
arbitrary matching in M135's orbit-incidence multigraph has both source and
target aligned generated subgroup equal to the common-parity group
`P_(d,s)`. This rules out all arities of the aligned generated-subgroup test
as an obstruction. It does not prove a simultaneous signed braid, a
polynomial matching-coset refinement, or any spectral-gap statement.

```text
candidate                  | multisource aligned generated-subgroup invariant
claimed target             | uniform physical minimal identity sector Z_d
identity ok                | DPS targets remain in Z_d by accepted construction
crosses Hurwitz components | not applicable; no sampler or gap is claimed
exact diagnostics          | d=3 actual/abstract failures; d=4 pair exception
verdict                    | accept proved negative sharpening only
```

## Field 2 — immutable provenance

All six assigned SHA-256 values match the frozen bytes. The assignment used
descriptive shorthand for three filenames; M141's own manifest resolves them
unambiguously to `multisource_subgroup_theorem.md`,
`multisource_subgroup_audit.py`, and `freeze_manifest.md`.

| frozen artifact | observed SHA-256 |
|---|---|
| `report.md` | `ebda7181e031603f598648d2409f8a484645022f24acd34e92ef5813459afb87` |
| `multisource_subgroup_theorem.md` | `7c9588dc64e3731a90e3e59bbe60a4d15dc8a42c4f98ce7ed60c386c7e8b8678` |
| `multisource_subgroup_audit.py` | `44f8fd167808bb41d2823bb10943951d6404d88aa4530697760a914b1e321d93` |
| `results.json` | `548ddf460a9184ebdc36c449ba35e8e2b8c3719b4994200808afa8868590c241` |
| `freeze_manifest.md` | `b45f4a80ca8745a9f7e6291b5118b27a64e22040a7799f872773624aff671e62` |
| `SHA256SUMS` | `9aa52349d288f04b7f46895cf7fe01373dcea807abf69892ef3ccea705acc057` |

No frozen file was executed or modified by the fresh checker.

## Field 3 — statement, target, convention, and dependencies

The auxiliary target is uniform on

```text
Z_d={(t_1,...,t_(2d-2)):t_1...t_(2d-2)=id,
                              support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. Signed right-Hurwitz moves are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

The accepted dependencies are precisely M135/M137's root-stabilizer
incidence multigraph and literal graph-versus-parity pair dichotomy, plus
connected transpositions generating `S_d` and simplicity of `A_d` for
`d>=5`. M141 proves its direct-power lemma internally and introduces no new
literature dependency.

For a nonempty matching subfamily `I`, `s=|I|`, its exact claim is

```text
Gamma_U(I)=Gamma_V(I)=
P_(d,s)={(g_1,...,g_s):sgn(g_1)=...=sgn(g_s)}.
```

## Field 4 — arbitrary matching and arbitrary representatives

The proof genuinely applies to an arbitrary matching, not only to one
perfect color. An edge is an `H=Stab(d)` orbit. Distinct edges of a matching
have distinct left endpoints, hence arbitrary physical representatives of
those edges lie in distinct global `S_d`-conjugacy orbits. M135's dichotomy
is stated for every literal pair `u,v in Z_d`; it is not restricted to
canonical representatives. Therefore every two-coordinate source projection
is exactly

```text
P_d={(x,y):sgn(x)=sgn(y)}.
```

The same reasoning applies on the right: `tau_i` maps each selected physical
representative into the target orbit labeling that edge, and matching right
endpoints are distinct. Every target pair is thus also nonconjugate and has
projection `P_d`. Perfection is useful only because M135's proper coloring
produces perfect matchings; M141 needs only endpoint distinctness. The proof
is consequently independent of the matching decomposition and of all
representative choices.

## Field 5 — passage to the alternating direct power

Every aligned generator is a tuple of transpositions and is odd in every
coordinate. Hence every element of `Gamma` has one common coordinate parity
and `Gamma<=P_(d,s)`. Set

```text
N=Gamma intersect A_d^s.
```

For any coordinate pair and any `(x,y) in A_d x A_d`, the pair projection
`P_d` supplies an element of `Gamma` with those two even coordinates. The
already established common-parity containment forces all its remaining
coordinates to be even as well, so that element belongs to `N`. Thus every
pair projection of `N` is exactly `A_d^2`. This parity-lifting step is
explicit and correct; it does not assume that intersection commutes with
projection in general.

M141's simple-power induction is valid. Project `L<=S^s` onto its first
`s-1` factors; induction makes this projection surjective. Its kernel is
`1^(s-1) x K`. Pair fullness gives surjectivity to the last coordinate, so
conjugating kernel elements by lifts proves `K normal S`. Simplicity leaves
`K=1` or `S`.

- If `K=S`, the full last-factor kernel and surjectivity onto the first
  factors give `L=S^s`.
- If `K=1`, `L` is the graph of a surjective homomorphism
  `f:S^(s-1)->S`. Images of the direct factors are normal and pairwise
  commuting. Nonabelian simplicity makes exactly one image equal to `S`
  and all others trivial, so `f` is an automorphism after one coordinate
  projection. The corresponding two-coordinate projection of `L` is then
  an automorphism graph, contradicting pair fullness.

The bases `s=1,2` are correct. This excludes inner, outer, and multi-block
diagonal couplings alike.

## Field 6 — `s=1`, odd-coset recovery, and ranks five/six

For `s=1`, connected transposition support generates `S_d` on both source and
target, so `Gamma=P_(d,1)=S_d`; no direct-power argument is needed.

For `s>=2`, the lemma applied to `N` gives `A_d^s`. `Gamma` contains every
displayed factor tuple, in particular one fixed all-odd tuple. Multiplying
that tuple by `A_d^s` gives the entire all-odd coset. Together with
`Gamma<=P_(d,s)`, this recovers exactly `P_(d,s)`, with no missing parity
coset or orientation issue.

At `d=5`, `A_5` is nonabelian simple; at `d=6`, `A_6` is nonabelian simple.
The fresh finite check independently found that every nonidentity alternating
conjugacy class normally generates the full group at both ranks. M135/M137
already excludes the exceptional outer automorphism of `S_6` in the pair
input because a graph automorphism here must preserve transpositions. Once
pair projections are full, any exceptional automorphism of `A_6` would still
produce a proper graph in some pair projection and is excluded by the
simple-power lemma. There is no boundary-rank exception.

## Field 7 — exact exceptional-rank falsification

The clean-room checker imports no M141, M137, or M135 module or result. It
reconstructed the accepted rooted DPS definition directly at only `d=3,4`:

| rank | physical words | rooted coordinates | root-fiber size |
|---:|---:|---:|---:|
| 3 | 24 | 72 | 3 |
| 4 | 2880 | 11520 | 4 |

Across the three `d=3` edits and three deterministic matching colors per
edit, it independently obtained nine colors and the following aggregate:

| width | source order histogram | target order histogram | literal equal/total |
|---:|---:|---:|---:|
| 1 | `6:36` | `6:36` | `36/36` |
| 2 | `18:54` | `18:54` | `54/54` |
| 3 | `18:36` | `18:36` | `3/36` |
| 4 | `18:9` | `18:9` | `0/9` |

Thus pair projections are full while higher-arity groups can remain proper
and source/target groups can differ. The abstract `A_3^3` product-one kernel
extended by one simultaneous odd tuple has order `18`, all three pair
projections of order `18=P_3`, but common-parity order `54`; arity three is
the first possible failure.

At `d=4`, the exact physical `tau_1` witness was reproduced. Neither source
nor target pair is globally conjugate, while the literal paired group changes
from `(V_4 x V_4)Diag(S_4)` of order `96` to `P_4` of order `288`. Hence
M135's pair premise is genuinely false there, and M141 correctly excludes
rank four rather than applying the nonsimple-power argument. The existing
singleton patch remains `|Z_4|=2880<4^6=4096`.

## Field 8 — necessity versus sufficiency and remaining frontier

Diagonal signed-Hurwitz moves are Nielsen transformations of the aligned
factor tuple and preserve its generated subgroup. Equality of source and
target aligned groups is therefore necessary for a common signed braid.
M141 consistently labels it only necessary. Its own `d=3` data demonstrates
that pairwise or higher generated-subgroup compatibility does not supply a
common action.

The exact remaining obligation is unchanged:

> Refine M135's matchings into polynomially many subfamilies whose action
> cosets have nonempty common intersection, and exhibit polynomial-length
> signed-braid representatives.

M141 proves no common braid, action-coset intersection, braid diameter,
compact matching evaluator, UST comparison, physical-sector gap, original
lazy exact `{3,4,5}` heat-bath gap, Terminal A, or Terminal B conclusion.

## Field 9 — reproduction, artifacts, manifest, and hygiene

Deterministic reproduction from this mission directory, Python `3.12.3`,
dependencies `{}`, `seed=null`:

```text
python3 -c 'from pathlib import Path; p=Path("independent_referee.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
python3 -B independent_referee.py
```

The bounded run took about `3.4` seconds; elapsed time is printed but omitted
from deterministic `independent_results.json`. Finite ranks are capped at
`3,4,5,6`, and the results explicitly state that the universal claim rests on
the proof audit rather than finite extrapolation.

Owned artifacts are `plan.md`, `checkpoint.md`, `independent_referee.py`,
`independent_results.json`, this report, `freeze_manifest.md`, and
`SHA256SUMS`. M143 modifies no predecessor, coordinator, manuscript,
project-skill, or other mission file.

```text
FINAL DECISION: ACCEPT.
ZERO MATERIAL NUMBERED OBJECTIONS.
PROMOTE ONLY THE d>=5 MULTISOURCE COMMON-PARITY NEGATIVE SHARPENING.
KEEP SIMULTANEOUS MATCHING-COSET REALIZATION UNRESOLVED.
```
