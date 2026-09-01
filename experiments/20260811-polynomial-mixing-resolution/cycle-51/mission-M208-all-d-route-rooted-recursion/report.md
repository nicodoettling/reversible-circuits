# M208 final report: rooted one-leaf correction at d5-to-d6

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
KEEP AN EXACT FINITE d5->d6 SYNCHRONIZED CORRECTION THEOREM.
GENERAL-d ROOTED CONTOUR RECURSION REMAINS UNRESOLVED.
```

The two named M181 patterns admit common correction braids for all seven old
edits after adjoining one leaf. The resulting schedule table is not universal
even over all 16 d=5 trees with the same root-leaf extension template.

## Field 2 — immutable provenance

Every file listed by M181/M183, M196/M198, M200/M202, and M203/M205 passed its
frozen checksum inventory before substantive work. Top inventory digests:

```text
M181 d2ae8d5a2af347eb74943db1221607d46fc706296ac2802d97abc0a024ec20b0
M183 ddd2bf1d2ce8d22e2228624d8802b38a527fee27819b92f9f06c3393b567fa46
M196 7fa987c6c776e55990c00fcfaea85e34c1d7b0e6d3f97d57fdefba8bcb5bd913
M198 1142912065699b883268b16aee8707b1c1e0d7c4b006eb1ca9bb02282ef9bd84
M200 6561e28aa199fc1d463881f399f116bd3c05222d6d26e9f54992ff1b542f2045
M202 33f34abf2f6d763b61fd15e6f64c895249792e70dab933894242584886491f70
M203 584d5110354693e3d5979fc6c1e83193e24754fcba4f51f035c9415cba3816e6
M205 271fcc6909ab45732d55eca0ee3d88ea1d57e5d64548fceed07316c77d734cd3
```

No predecessor was edited.

## Field 3 — target, convention, and method

There is no probability distribution or Markov kernel in this mission. The
target is exact synchronized signed-Hurwitz endpoint realization. Actions are
chronological, with

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

The work reconstructs only named rooted DPS descriptors and Cayley-tree
templates. It never enumerates `Q_6`.

## Field 4 — exact rooted descriptor extension

Both d=5 M181 patterns have

```text
pi_5=(7,8 | 1,2 | 3,4 | 5,6).
```

Their d=6 source descriptor is obtained by adding tree edge `{1,6}`, moving
the root from 5 to 6, putting fresh labels 9,10 at child 1, and moving the old
child-1 slot to child 5:

```text
pi_6=(9,10 | 1,2 | 3,4 | 5,6 | 7,8).
```

Direct closure reproduces the literal physical extension by `(05)^2`. After
an old adjacent-value edit, however, physical DPS closure couples the old
target and the new leaf, as M203/M205 established.

## Field 5 — exact synchronized correction certificates

Let `N_(b,i)` be the d=5 target for pattern `b` with `(05)^2` appended, and
let `A_(b,i)` be the actual d=6 DPS target. One common word `C_i` satisfies
`C_i N_(b,i)=A_(b,i)` for both `b=0,1`. Exact correction lengths are

```text
i        1   2   3   4   5   6   7
|C_i|   13   0   9   0   5   2   1.
```

All words are displayed in `rooted_recursion.md` and stored factor-by-factor
in `rooted_extension_results.json`. The fourteen literal replays pass. Their
normalized certificate digest is
`0bcfdab81369a4fca73367bee84169dd313c698b42685b8053dae2e764ef4223`.

## Field 6 — exact finite route consequence

Embed an accepted d=5 synchronized source-to-target braid into the first eight
positions of the d=6 source pair, leaving `(05)^2` fixed, then append `C_i`.
This is an exact synchronized physical quotient route to the actual d=6 pair
for the distinguished two M181 patterns and inherited edits 1 through 7.

The correction alone has maximum length 13. This finite statement supplies
no bound for d>=7, no voltage-correction length, and no polynomial inference.

## Field 7 — template falsification and first unresolved lemma

The known `C_i` were replayed on all 16 d=5 Cayley trees whose old root 5 is a
leaf adjacent to 1, using the same `pi_5,pi_6`. Among 112 tree/edit checks,
the table fails 21 times: 11 at edit 1, 9 at edit 3, and 1 at edit 5.

The first failure is edit 3 on
`{{1,2},{1,3},{1,5},{3,4}}`. The route changes the `(24)` factor to `(25)`
and transports the filler positions, but leaves `(34)^2`; the actual target
requires `(35)^2`. Thus the derived table is sensitive to an off-contour tree
attachment despite the same bare root path `5-1-6` and the same orders.

This refutes universality only of the displayed schedule table. It does not
prove that another common or tree-dependent correction braid is impossible.
The standalone unresolved lemma is to identify sufficient local tree data and
prove a uniform general-d leaf-extension schedule with controlled length and
synchronized compatibility.

## Field 8 — computation and hygiene

Environment: Python 3.12.3; nonstandard dependencies `{}`; seed `null`.
The authoritative reproduction command is

```text
timeout 120s python3 -B rooted_extension_audit.py
```

The earlier targeted meet-in-the-middle probe searched only seven named
endpoint pairs and supplied positive words; its radius misses have no negative
interpretation. The final checker performs no route search: it replays the
literal words and applies them to the 16-tree falsification table. All writes
are confined to M208 and no cache is retained.

## Field 9 — final boundary and audit request

```text
PROVED: exact d5->d6 corrections for the two named M181 patterns, old edits
1..7, and the resulting distinguished synchronized quotient routes.

REFUTED: universality of that particular seven-word schedule table over the
full 16-tree leaf-extension template.

UNRESOLVED: another contour/tree-dependent recurrence, arbitrary H-orbit
representatives, every d6 matching color, edits 8,9, and all d>=7 routing.
```

No polynomial total length, voltage-correction length, gap, mixing, or
Terminal conclusion follows. Freeze this package and request a fresh
immutable referee of the descriptor extension, all fourteen route replays,
and the first template failure.

