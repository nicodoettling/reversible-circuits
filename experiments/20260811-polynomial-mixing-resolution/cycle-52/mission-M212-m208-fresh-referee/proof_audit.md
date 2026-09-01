# M212 proof audit of frozen M208

## 1. Independent rooted-DPS reconstruction

The referee implements the plus-mirror hairy-tree boundary trace and intrinsic
distance-one/distance-three closure directly. It imports no M208 code.

For the two named patterns it reconstructs

```text
T_0={{1,2},{1,3},{1,5},{2,4}},
T_1={{1,2},{1,3},{1,4},{1,5}},
pi_5=(7,8,1,2,3,4,5,6).
```

Direct closure gives respectively

```text
(01)^2(02)^2(13)^2(04)^2,
(01)^2(02)^2(03)^2(04)^2.
```

Adjoining `{1,6}` to each tree and using

```text
pi_6=(9,10,1,2,3,4,5,6,7,8)
```

closes to the same d=5 word followed by `(05)^2`. Every reconstructed source
and edited endpoint evaluates to identity under the declared left-to-right
factor convention.

## 2. Correction-word replay

The referee independently transcribes the seven chronological signed-Hurwitz
words from M208 and implements

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

For every old edit `i=1,...,7` and both patterns, it constructs the naive
endpoint `F_5(T_b,s_i pi_5)(05)^2`, applies `C_i`, and compares the literal
physical word with `F_6(T_b+{1,6},s_i pi_6)`. All fourteen equalities hold.

The independently regenerated lengths are `13,0,9,0,5,2,1`. Encoding the
complete route and endpoint rows with sorted compact JSON gives

```text
0bcfdab81369a4fca73367bee84169dd313c698b42685b8053dae2e764ef4223,
```

exactly M208's certificate digest. Every descriptor/certificate field in
frozen `rooted_extension_results.json` matches.

## 3. Composition with the accepted d5 route theorem

The seven distinguished-root `[4,4]` incidence rows in accepted M200 are all
covered by M196. Independent physical replay shows a useful distinction:

```text
stored M196 word hits exact fixed physical targets: edits 1,2,4,6;
stored M196 word hits only the required quotient classes: edits 3,5,7.
```

For the first group, embedding the literal stored word on positions 1 through
8 of the d=6 source and then applying `C_i` directly replays to the actual
d=6 pair.

For edits 3,5,7 one must not append `C_i` directly to the stored M196 quotient
word. The accepted M200/M202 theorem invokes M181 full voltage and M175's
affine criterion to supply some exact fixed-physical-endpoint d5 braid; its
length is not known. If `B_i` is any such braid, all its generators have
indices at most 7, so its action on the ten-factor source leaves positions 9
and 10 equal to `(05)^2`. Therefore it reaches the naive endpoint exactly,
and appending `C_i` reaches the actual endpoint. This proves M208's existential
composition while preserving its no-length boundary.

## 4. Complete 16-tree falsification replay

Lexicographic Prüfer generation gives exactly 16 trees on `[5]` in which root
5 is a leaf adjacent to 1. For each tree and edit 1 through 7, the referee
constructs the naive and actual endpoints and applies only the known `C_i`.
The exact 112-row outcome is

```text
known-route failures: 21,
edit histogram: 1 -> 11, 3 -> 9, 5 -> 1.
```

The first failure is tree index 2,
`{{1,2},{1,3},{1,5},{3,4}}`, edit 3. The naive target, route output, and actual
target all match frozen M208. The output retains `(34)^2`, whereas the actual
target contains `(35)^2`.

This is a complete refutation of universality of the seven archived words on
the declared 16-tree template. It is not a complete orbit decision and says
nothing negative about alternative common or tree-dependent words.

## 5. Logical verdict and boundary

M208's finite theorem, existential composition, template falsification, and
scope statements are all valid. Numbered objections: **none**.

Accepted scope is only the two named patterns at d5-to-d6 and inherited edits
1 through 7, plus failure of the specific schedule table on the larger
template. There is no theorem for edits 8,9, arbitrary physical
representatives without the accepted qualitative voltage dependency, every
d6 matching color, general d, corrected route length, polynomial mixing,
spectral gap, or Terminal.

