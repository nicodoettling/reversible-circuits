# M146 final report: DPS aligned tuple-conjugacy

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and exact scope

```text
FINAL VERDICT: KEEP AS A PROVED NEGATIVE SHARPENING.
PROVED: exact conjugacy-class splitting formula in P_(d,s).
PROVED for d>=5: every M135 matching subfamily automatically preserves the
  aligned factor-tuple conjugacy-class multiset; no refinement is needed.
EXACT at d=3: zero new class-multiset obstructions beyond subgroup changes.
UNRESOLVED: simultaneous action-coset intersection and polynomial braid length.
```

The candidate invariant collapses because every aligned factor is an all-odd
tuple of transpositions and all such tuples form one class in the common-
parity group. This closes the assigned invariant negatively; it does not
construct a common braid.

```text
candidate                  | aligned factor-tuple conjugacy multiset
claimed target             | uniform physical minimal identity sector Z_d
identity ok                | DPS targets remain in Z_d by accepted construction
crosses Hurwitz components | not applicable; no sampler or gap is claimed
exact diagnostics          | class splitting d<=4; centralizers/transporters d<=7; all d3 matchings
verdict                    | keep theorem as negative sharpening only
```

## Field 2 — target, convention, and dependencies

For `d>=2`, `m=2d-2`, the auxiliary target is uniform on

```text
Z_d={(t_1,...,t_m):t_1...t_m=id,
                         support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. Signed right-Hurwitz moves are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

The only project dependencies are the frozen accepted M135/M137 matching
construction and M141/M143 theorem that every nonempty `d>=5` matching
subfamily has both aligned generated groups equal to `P_(d,s)`. The
conjugacy classification is proved from scratch and uses no new literature.

## Field 3 — exact common-parity conjugacy classification

Let `G=S_d^s`, let `sigma:G->F_2^s` record coordinate parities, and let

```text
P_(d,s)=sigma^(-1)({(e,...,e):e in F_2}).
```

For `x in P`, call coordinate `q` rigid when its centralizer in `S_d` is
entirely even. This happens exactly when the coordinate cycle type consists
of distinct odd parts. If `r` coordinates are rigid, one ambient
`S_d^s`-conjugacy class splits into exactly

```text
2^max(r-1,0)
```

`P_(d,s)` classes. More precisely, for any coordinatewise transporter from
`x` to `y`, the transporter parities at rigid coordinates are well-defined;
`x,y` are `P`-conjugate exactly when those parities all agree.

The proof observes that nonrigid coordinate centralizers independently flip
transporter parity. The orbit count is the index of the diagonal parity
subspace plus the centralizer parity image in `F_2^s`.

## Field 4 — all-odd and transposition collapse

Every odd permutation is itself an odd element of its centralizer. Hence an
all-odd product element has no rigid coordinates, and its ambient product
class does not split in `P_(d,s)`. All transpositions have the same
`S_d` cycle type. Therefore all `s`-tuples of transpositions form one
`P_(d,s)` conjugacy class for every `d>=2,s>=1`.

Equivalently, coordinatewise transposition transporters can all be chosen
even: if a transporter is odd, multiply it by the source transposition in its
centralizer. The resulting all-even tuple is a conjugator in `P_(d,s)`.

## Field 5 — the Hurwitz invariant and its automatic preservation

For aligned factors `x_j=(u_j^1,...,u_j^s)`, a common Hurwitz move replaces

```text
(x_j,x_(j+1)) by
(x_(j+1),x_(j+1)^(-1)x_jx_(j+1)).
```

It therefore preserves the literal generated group and the multiset of
conjugacy classes of the factors inside that group. This is a necessary, not
sufficient, condition for a common braid.

For any nonempty subfamily of any `d>=5` M135 matching, M141/M143 gives both
source and target group `P_(d,s)`. Every aligned source and target factor is
an all-odd tuple of transpositions, so all factors occupy the one class from
Field 4. Both multisets are exactly `2d-2` copies of that class. Thus the
descriptor is constant and the matching requires no refinement for this
invariant.

## Field 6 — rank-three and boundary calibration

The deterministic checker reconstructs all nine accepted `d=3` matchings
and all fifteen nonempty subfamilies of each:

| width | group equal and class multiset equal | literal group changed |
|---:|---:|---:|
| 1 | 36 | 0 |
| 2 | 54 | 0 |
| 3 | 3 | 33 |
| 4 | 0 | 9 |

There are zero class-multiset changes among all `93` literal-group-equal
cases. The other `42` cases already fail the stronger necessary literal-
group equality. This exact rank-three fact calibrates but does not prove the
universal theorem.

The full class-splitting formula was also enumerated over every element of
`P_(d,s)` for `2<=d<=4`, `1<=s<=3`, with zero failures. One representative
of every cycle type through `d=7` passed the centralizer criterion, and every
ordered transposition pair through `d=7` admitted the checked explicit even
transporter. Rank four remains excluded from the M135/M141 application
because its paired-subgroup premise fails; the conjugacy theorem itself does
not fail there.

## Field 7 — consequence and first unresolved step

The tuple-conjugacy multiset cannot distinguish the endpoints of any
`d>=5` M135 matching subfamily and cannot provide a useful polynomial
matching refinement. Together with M141/M143, this removes generated
subgroups and factor conjugacy multisets as candidate obstructions.

The first unresolved step remains exactly the **POLYNOMIAL MATCHING-COSET
REFINEMENT**: refine the M135 matchings into polynomially many subfamilies
whose action cosets have nonempty common intersection and provide polynomial-
length signed-braid representatives. Passing the invariant here supplies no
coset intersection.

## Field 8 — reproduction, artifacts, and hygiene

Deterministic reproduction, Python `3.12.3`, dependencies `{}`, `seed=null`:

```text
python3 -c 'from pathlib import Path; p=Path("tuple_conjugacy_audit.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
python3 -B tuple_conjugacy_audit.py
python3 -c 'import json; q=json.load(open("results.json")); assert all(not r["failures"] for r in q["centralizer_parity_audit"]); assert all(not r["formula_failures"] and r["all_transposition_class_count"]==1 for r in q["direct_class_splitting_audit"]); assert q["d3_aggregate_by_width"]=={"1":{"class_multiset_equal":36},"2":{"class_multiset_equal":54},"3":{"class_multiset_equal":3,"literal_group_changed":33},"4":{"literal_group_changed":9}}; print("assertions ok")'
```

The checker uses the frozen M137 fresh-checker read-only after verifying
SHA-256
`bb62d449c7cad72a448389f9f7dd7ee76618e8c71b68189db20e19f4e2244341`.
Its caps are: cycle-type centralizers and explicit transposition transporters
through `d=7`; complete common-parity class enumeration through `d=4,s=3`;
and complete `d=3` matching calibration. No `d=5` DPS enumeration was run,
because the universal proof makes it unnecessary.

Owned artifacts are `plan.md`, `checkpoint.md`,
`tuple_conjugacy_theorem.md`, `tuple_conjugacy_audit.py`, `results.json`,
this report, `freeze_manifest.md`, and `SHA256SUMS`. No predecessor,
coordinator, manuscript, skill, or other mission file was edited.

## Field 9 — final decision and scope boundary

```text
KEEP THE EXACT P_(d,s) CONJUGACY CLASSIFICATION.
KEEP THE d>=5 AUTOMATIC-PRESERVATION THEOREM AS A NEGATIVE SHARPENING.
DO NOT INFER SIMULTANEOUS BRAID REALIZATION.
```

This proves no UST basis exchange, all-edge comparison, physical minimal-
sector gap, arbitrary-product `Gamma_0`, original lazy exact `{3,4,5}` heat-
bath gap, Terminal A, or Terminal B outcome.
