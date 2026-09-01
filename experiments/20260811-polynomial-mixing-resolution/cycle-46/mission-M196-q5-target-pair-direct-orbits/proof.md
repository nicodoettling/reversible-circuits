# M196 exact target-pair classification proof

Date: 2026-08-13 UTC.

## 1. Statement and scope

Let `X=Q_5` be M191's frozen 8,400-point quotient action, with signed Hurwitz
symbols `1,...,7,-1,...,-7` applied chronologically on the right. Let the
diagonal action on `X^2` start at `(v,u)=(16,0)`. For each of the 54 named M191
target rows `(v_j,u_j)`, there is an explicit word `w_j` such that

```text
(v,u)^w_j = (v_j,u_j).
```

Consequently all 54 named `d=5`, width-two targets lie in the diagonal
component of `(16,0)`. This is an exact classification of that named finite
target list. It is not a classification of arbitrary pairs or of the full
diagonal orbit.

## 2. Adjustment and deduplication

For every first target `v_j`, the independently rebuilt chronological BFS
transversal supplies a tree word `alpha_j` with

```text
16^alpha_j = v_j.
```

Define

```text
z_j = u_j^(alpha_j^(-1)).
```

The 54 rows yield exactly 41 distinct values of `z_j`. The inverse convention
is literal signed-word inversion: reverse the word and negate every symbol.
All 8,400 tree words replay to their indexed endpoints; their maximum length
is 13 globally and 9 on the named targets.

## 3. Target-directed pair certificates

Build the diagonal product-action ball of radius eight from `(16,0)`. Its
exact level sizes are

```text
1, 6, 40, 190, 795, 2,976, 10,416, 34,256, 105,713,
```

for 154,393 distinct states in total. For a fixed adjusted target `(16,z)`,
run a backward BFS under the same signed generators until it meets the forward
ball. If `f_z` sends `(16,0)` to a meeting point and `b_z` sends `(16,z)` to
the same point, then chronological right action gives

```text
h_z = f_z b_z^(-1),
(16,0)^h_z = (16,z).
```

This is checked by literal replay, rather than inferred from a bounded miss.
The search found all 41 adjusted targets: 15 directly in the forward ball and
26 by a nonempty backward segment. Maximum lengths are `|f_z|=8`, `|b_z|=7`,
and `|h_z|=15`.

## 4. Original target words

For target row `j`, set

```text
w_j = h_(z_j) alpha_j.
```

Since `h_(z_j)` fixes 16 and maps 0 to `z_j`, while `alpha_j` maps 16 to
`v_j` and maps `z_j` to `u_j` by the definition of `z_j`, the word `w_j`
maps `(16,0)` to `(v_j,u_j)`. All 54 words are stored explicitly, not merely
reconstructible, in `targeted_results.json`. Their maximum length is 22.

The independent verifier reloads only the frozen action and the output JSON,
checks every meeting decomposition, replays all 41 stabilizer words, checks all
54 adjustment equations, verifies the exact target-ID inventory, and replays
all 54 full endpoint words. It returns `PASS`.

## 5. Exact boundary

The positive certificates complete the requested 54-row finite classification;
no negative certificate is needed and no negative claim is made. The search
does not compute the full stabilizer orbit, does not enumerate `Q_5^2`, and
does not imply every-color or all-`d` routing. The maximum length 22 is only a
fact about these archived finite witnesses; it has no asymptotic or polynomial
route-length consequence. There is no gap, mixing, or Terminal conclusion.
