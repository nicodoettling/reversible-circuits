# M187 final report: anchored representative quotient routing

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and exact scope

```text
FINAL VERDICT: KEEP A CONDITIONAL ANCHORED-EDGE ROUTING THEOREM.

PROVED: if all color-selected representatives admit the same pair-aligned
or boundary-aligned rooted DPS local form, the matched quotient tuple is
reached by the empty word or one common R_i.

EXACT FINITE: 14 positive d=5 width-two route certificates among 54 targeted
eligible quotient targets, at search radius five.

UNRESOLVED: quotient-route existence for every perfect-matching color.
```

The finite forty misses are not used negatively. No route-length, gap,
mixing, or Terminal claim is made.

```text
candidate                  | M181 anchored doubled-tree source family
claimed target             | matched DPS target quotient tuple
identity ok                | imported M181 theorem; targeted reconstructions pass
crosses Hurwitz components | only for stated conditional/positive witnesses
exact diagnostics          | targeted d=5 roots/edits; d=3,4 local falsification
verdict                    | keep conditional lemma; every-color route unresolved
```

## Field 2 — target, conventions, and frozen gate

For `d>=5`, `m=2d-2`, the auxiliary target is diagonal signed-Hurwitz orbit
existence on ordered tuples in

```text
Q_d=Z_d/S_d,
Z_d={(t_1,...,t_m):t_1...t_m=id, support connected on [d]}.
```

Permutations compose as `(p q)(x)=p(q(x))`; braid symbols act
chronologically. All fourteen assigned immutable manifests passed before use:
M135/M137, M141/M143, M146/M148, M154/M158, M169/M172, M175/M176,
and M181/M183. No frozen file was edited.

There is no declared distribution or Markov kernel in this structural
mission. No voltage search was performed.

## Field 3 — exact representative mismatch

An M135 perfect matching chooses one `H=Stab(d)`-orbit edge `Q_c=H.u_c`
over each M181 left global orbit. It does not choose the literal gadget word.
Writing `u_c=alpha_c.W_c`, the relabeler `alpha_c` may move `d`.

Every braid is `G=S_d`-equivariant, which is why M181's stabilizer loops
transfer to `u_c`. But the DPS endpoint map satisfies only

```text
tau_i(h.w)=h.tau_i(w),       h in H.
```

Therefore `tau_i(alpha_c.W_c)` cannot be replaced by
`alpha_c.tau_i(W_c)` in general. Matching perfectness supplies uniqueness on
the left and distinctness on the right, not a canonical rooted representative.
This invalidates the proposed automatic every-color transfer, without
proving any selected target unreachable.

## Field 4 — conditional rooted local theorem

For a doubled-tree word

```text
W=(e_1,e_1,...,e_(d-1),e_(d-1)),
```

fix a rooted DPS coordinate. A pair-aligned edit swaps the two labels on one
degree-two black vertex. Root forgetting makes its quotient endpoint `[W]`.
A boundary-aligned edit `i=2k` exchanges the touching labels of consecutive
doubled edges `e_k,e_(k+1)`, where those edges are disjoint or meet at the
distinguished root. Their hairy-tree sectors are noninterleaving, and the
literal distance-one/distance-three closure gives exactly `R_i[W]`, fixing
all outside factors.

Hence if every coordinate selected by a matching color admits the same type,
the synchronized route exists: empty for pair-aligned representatives and
`R_i` for boundary-aligned representatives. This theorem is all-`d` but
conditional on representative selection. M135 does not show that an
arbitrary color supplies these `H`-orbits.

## Field 5 — targeted d=5 positive witnesses

The clean-room checker reconstructs rooted DPS coordinates only for

```text
V=(01)^2(02)^2(13)^2(04)^2,
U=(01)^2(02)^2(03)^2(04)^2,
```

their five possible roots, and their seven adjacent-value edits. It obtains
54 distinct eligible target quotient pairs. A quotient BFS limited to radius
five visits 4,008 states and certifies 14 targets at lengths

```text
0,1,1,1,1,1,1,2,2,3,3,3,3,5.
```

For the common gadget-anchor root pair, the positive certificates are empty
at `i=1,3,7`, and `R_i` at `i=2,4,6`. No radius-five certificate was found
for the anchored pair at `i=5`; this is not a nonreachability conclusion.
The full raw target table is retained for exact reproduction, while
`compact_results.json` records only the claim-bearing summary.

## Field 6 — boundary and falsification audit

A separate doubled-tree replay at `d=3,4` tests the precise local hypotheses,
without enumerating `Q_5` or any quotient component:

| `d` | pair-aligned tests | failures mod `G` | boundary-aligned tests | failures |
|---:|---:|---:|---:|---:|
| 3 | 24 | 0 | 2 | 0 |
| 4 | 576 | 0 | 84 | 0 |

Removing the boundary incidence hypothesis produces failures, as expected:
meeting at a nonroot white vertex can interleave the two sectors. These
finite rows are convention/falsification checks; the structural DPS argument
in `proof.md` is the all-`d` proof.

## Field 7 — accepted interfaces and exact residual obligation

M141/M143 and M146/M148 remove only the aligned group and factor-class
obstructions. They are not treated as a classification. M154/M158 supplies
literal inner loops but not these targets. M169/M172 identifies the source
monodromy kernel/interface. M175/M176 says that fixed physical endpoint
orientation is an affine chord-space membership problem after a quotient
route exists. M181/M183 gives full source chord rank for the constructed
family, but explicitly leaves that route conditional.

Thus the residual statement is:

> For each M135 color, show that its arbitrary selected `H`-orbit edges over
> the M181 source vertices have matched targets in one synchronized quotient
> component, or exhibit an exact orbit invariant/counterfamily.

This remains unresolved. Full voltage cannot discharge it.

## Field 8 — reproduction, artifacts, and hygiene

The checker uses Python `3.12.3`, standard library only, dependencies `{}`,
and seed `null`. The principal command is

```text
python3 -B targeted_dps_probe.py
```

It performs ten targeted rooted inversions and a bounded search only; it does
not enumerate `Z_5`, `Q_5`, an action group, or a quotient component. Owned
artifacts are `plan.md`, `checkpoint.md`, `halfway_checkpoint.md`,
`proof.md`, `targeted_dps_probe.py`, `targeted_results.json`,
`compact_results.json`, this report, `freeze_manifest.md`, and `SHA256SUMS`.
No predecessor, coordinator, manuscript, skill, or file outside M187 is
edited.

## Field 9 — final decision and fresh-audit request

```text
KEEP THE CONDITIONAL ROOTED REPRESENTATIVE-SELECTION THEOREM.
KEEP THE 14 d=5 ROUTES AS EXACT POSITIVE WITNESSES ONLY.
DO NOT PROMOTE TO EVERY PERFECT-MATCHING COLOR.
```

A fresh immutable referee should verify the frozen hashes, the mismatch
between `G`-equivariance of braids and `H`-equivariance of `tau_i`, the exact
rooted hypotheses in Lemma 3.1, the common-route conclusion, and the finite
14/54 scope. It should not infer coverage from the BFS, generated-subgroup
sufficiency, route-length asymptotics, a gap, mixing, or Terminal.
