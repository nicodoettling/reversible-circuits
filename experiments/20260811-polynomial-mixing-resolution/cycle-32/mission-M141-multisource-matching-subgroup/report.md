# M141 final report: multisource common-parity theorem

Date: 2026-08-13 UTC.  Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and exact scope

```text
FINAL VERDICT: KEEP AS A PROVED NEGATIVE SHARPENING.
PROVED for d>=5: every nonempty subfamily of any M135 matching has
  source and target aligned generated subgroup exactly P_(d,s).
PROVED: every multi-source generated-subgroup invariant is therefore passed.
REFUTED at d=3: pairwise-full projections force the full multisource group.
UNRESOLVED: simultaneous action-coset intersection and polynomial braid length.
```

The theorem applies in particular to each perfect-matching color in M135's
`d`-edge-coloring, and more generally to an arbitrary matching.  It rules out
one entire family of prospective higher-order obstructions; it does not
construct a common signed braid.

```text
candidate                  | multisource generated-subgroup invariant
claimed target             | uniform physical minimal identity sector Z_d
identity ok                | DPS targets remain in Z_d by accepted construction
crosses Hurwitz components | not applicable; no sampler or gap is claimed
exact diagnostics          | all d=3 matching subgroups plus abstract rank-3 witness
verdict                    | keep d>=5 theorem as negative sharpening only
```

## Field 2 — target, convention, and accepted dependencies

For `d>=2`, `m=2d-2`, the auxiliary target is uniform on

```text
Z_d={(t_1,...,t_m):t_1...t_m=id,
                         support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  Signed right-Hurwitz moves are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

Accepted inputs are M135/M137's root-stabilizer orbit-incidence construction,
the matching endpoint property, and their graph-versus-parity pair dichotomy
for `d>=5`.  The proof also uses connected transpositions generating `S_d`
and the standard simplicity of `A_d` for `d>=5`.  The required direct-power
lemma is proved from scratch.  No unverified literature input is introduced.

## Field 3 — exact statement

Fix `d>=5`, an adjacent DPS edit `tau_i`, and an arbitrary matching `M` in
M135's incidence multigraph.  Choose any representative `u^q` of every edge
and put `v^q=tau_i(u^q)`.  For any nonempty subfamily `I` of size `s`, form

```text
Gamma_U(I)=<(u_j^q)_(q in I):1<=j<=m> <= S_d^s,
Gamma_V(I)=<(v_j^q)_(q in I):1<=j<=m> <= S_d^s.
```

Then

```text
Gamma_U(I)=Gamma_V(I)
          =P_(d,s)
          ={(g_1,...,g_s):sgn(g_1)=...=sgn(g_s)}.      (3.1)
```

For `s=1`, the parity condition is vacuous: connected support gives
`Gamma_U=Gamma_V=S_d`.  For `s>=2`, the proof below applies.  The result is
independent of representative choice, matching decomposition, and subfamily.

## Field 4 — pair projections and representative audit

Distinct edges in an arbitrary matching have distinct left endpoints, hence
any physical representatives of those edges lie in distinct global
`S_d`-conjugacy orbits.  M135's dichotomy applies to each literal pair of
representatives and gives pair projection `P_d`.  This does not depend on
which representative is selected within an `H`-orbit.

Distinct edges also have distinct right endpoints.  Each
`v^q=tau_i(u^q)` lies in the target global orbit labeling its edge, so every
literal target pair is also nonconjugate and has pair projection `P_d`.
Thus all two-coordinate projections of both aligned groups are exactly
`P_d`.  This verifies the pair input for arbitrary matchings, not just one
particular perfect-matching color or canonical representative choice.

## Field 5 — simple-power proof and ranks five/six

Every aligned generator is all-odd, so `Gamma<=P_(d,s)`.  Put

```text
N=Gamma intersect A_d^s.
```

The `P_d` pair projections imply that every projection of `N` onto two
coordinates is `A_d x A_d`.  The proof note establishes by induction:

> If `S` is nonabelian simple and `L<=S^s` has every pair projection equal
> to `S^2`, then `L=S^s`.

Project to the first `s-1` coordinates.  The last-coordinate kernel is
normal in `S`, hence trivial or `S`.  A trivial kernel makes `L` the graph of
a surjective map `S^(s-1)->S`; commuting direct-factor images show that this
map factors through one coordinate, contradicting fullness of that pair
projection.  Hence the kernel is `S`, and induction gives the full product.

Apply this with `S=A_d` to obtain `N=A_d^s`.  One all-odd factor tuple then
supplies the second coset, proving `Gamma=P_(d,s)`.  `A_5` and `A_6` are both
nonabelian simple.  At rank six, any inner or outer diagonal coupling would
produce a graph in some pair projection and is excluded; M135/M137 already
exclude the `S_6` outer automorphism in the input pair dichotomy because it
does not preserve transpositions.

## Field 6 — exact exceptional-rank findings

The deterministic checker verifies the frozen M137 checker digest, rebuilds
its accepted `d=3` DPS incidence matchings, and closes every aligned subgroup.
Across all three adjacent edits and all three colors (nine matchings total):

```text
one-source groups                 36/36 have order 6 = |S_3|,
source and target pair groups    108/108 have order 18 = |P_3|,
literal source/target pair equal 54/54 aligned pairs,
triple groups                    72/72 have order 18, not 54,
literal source/target triple equal 3/36 aligned triples,
four-source groups               18/18 have order 18, not 162,
literal source/target full equal 0/9 matchings.
```

It also constructs the smallest abstract counterexample: in `S_3^3`, extend
`{(x_1,x_2,x_3) in A_3^3:x_1x_2x_3=id}` by one simultaneous odd tuple.  The
result has order `18`, every pair projection is `P_3` of order `18`, but the
full common-parity group has order `54`.  Thus nonabelian simplicity is
essential and arity three is the first possible failure.

At `d=4`, `A_4` is not simple and M135's pair premise already fails through
its exact `96 -> 288` witness.  M135 uses singleton colors there.  No rank-
four extension is claimed.  At `d=2`, the incidence setup is degenerate and
irrelevant to the `d>=5` theorem.

## Field 7 — consequence and remaining first unproved step

Diagonal signed-Hurwitz moves preserve the subgroup generated by the aligned
factor tuples, so equality of source and target multisource groups is a
necessary condition for a common braid.  Theorem (3.1) proves that this
condition is automatic, at every arity, inside a `d>=5` matching.

It is not sufficient.  The exact remaining step is still:

> **POLYNOMIAL MATCHING-COSET REFINEMENT.** Refine the M135 matchings into
> polynomially many subfamilies whose action cosets `K_Q` have nonempty
> common intersection, and give a signed-braid representative of polynomial
> length.

No common action, braid diameter, compact matching evaluator, or polynomial
number of matching edges follows from this mission.

## Field 8 — reproduction, artifacts, and hygiene

Deterministic reproduction, Python `3.12.3`, dependencies `{}`, `seed=null`:

```text
python3 -c 'from pathlib import Path; p=Path("multisource_subgroup_audit.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
python3 -B multisource_subgroup_audit.py
python3 -c 'import json; q=json.load(open("results.json")); rows=q["actual_d3_matching_rows"]; assert len(rows)==3; colors=[c for r in rows for c in r["matching_colors"]]; assert len(colors)==9; assert all(c["source"]["order_histogram_by_width"]["2"]=={"18":6} and c["target"]["order_histogram_by_width"]["2"]=={"18":6} for c in colors); assert all(c["source"]["order_histogram_by_width"]["3"]=={"18":4} and c["source"]["order_histogram_by_width"]["4"]=={"18":1} for c in colors); assert all(c["aligned_source_target_comparison_by_width"]["4"]["equal_literal_subgroups"]==0 for c in colors); a=q["abstract_d3_pairwise_full_counterexample"]; assert (a["subgroup_order"],a["common_parity_group_order"])==(18,54); print("assertions ok")'
```

The checker uses the frozen M137 checker read-only after verifying SHA-256
`bb62d449c7cad72a448389f9f7dd7ee76618e8c71b68189db20e19f4e2244341`.
Owned artifacts are `plan.md`, `checkpoint.md`,
`multisource_subgroup_theorem.md`, `multisource_subgroup_audit.py`,
`results.json`, this report, `freeze_manifest.md`, and `SHA256SUMS`.  No file
outside the owned mission directory was edited.

## Field 9 — final decision and scope boundary

```text
KEEP THE d>=5 MULTISOURCE COMMON-PARITY THEOREM.
KEEP THE d=3 ACTUAL MATCHING COUNTEREXAMPLE AND ABSTRACT MINIMAL WARNING.
DO NOT INFER SIMULTANEOUS BRAID REALIZATION.
```

This is a proved negative sharpening of the realization frontier: future
work should study the simultaneous action-coset intersection itself rather
than search for higher-arity generated-subgroup conflicts.  It proves no UST
basis exchange, all-edge comparison, physical minimal-sector gap, arbitrary-
product `Gamma_0`, original lazy exact `{3,4,5}` heat-bath gap, Terminal A,
or Terminal B outcome.
