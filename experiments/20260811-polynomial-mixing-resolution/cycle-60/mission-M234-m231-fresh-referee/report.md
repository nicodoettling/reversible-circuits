# M234 final report: fresh immutable referee of M231

Date: 2026-08-13 UTC.  Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Verdict

```text
ACCEPT M231 AS AN EXACT FINITE d=6 -> 7 FORMULA-COMPRESSION THEOREM.
```

No material objection survives the clean-room reconstruction.  M231's full
`D_B`, `Z1`, and `Z2` class counts, symbolic literal-word kernel, all 500
endpoint replays, three normalized digests, and 12-odd-plus-2-boundary word
inventory are reproduced exactly.

## 1. Target and convention

There is no target distribution or Markov kernel in this mission.  The object
is deterministic endpoint correction for the 125 rooted trees at `d=6` and
ordinary odd edits `{1,3,5,7}`:

```text
N_(T,i)=F_6(T,s_i pi_6)(06)^2,
A_(T,i)=F_7(T+{{1,7}},s_i pi_7).
```

M234 uses chronological signed right-Hurwitz action

```text
R_j(a,b)=(b,bab),
R_j^-1(a,b)=(aba,a).
```

All factor transpositions are stored with increasing endpoints.  Both DPS
endpoints independently evaluate to the identity before route comparison.

## 2. Frozen inventory and independence

Every one of M231's twelve frozen payloads passes `sha256sum -c`; the digest
of its `SHA256SUMS` is

```text
63b6e790a86f1cfae2db971b28a46c1a173ad9c27560857ac60ce9c7ba0421db.
```

The M234 checker imports and reads no predecessor code or data.  It separately
implements Prüfer enumeration, rooted orientation, the DPS hairy-boundary
trace and LIFO closure, transposition conjugation, signed Hurwitz action,
descriptor extraction, and the formula route.  Descriptor and route are
assigned before either endpoint is built.  There is no route search or
quotient-state enumeration.

The independent table and native hashes were fixed before M231's serializer
was inspected.  A later compatibility layer applies only its published
normalization to the already constructed objects.

## 3. Formal and complete finite checks

The checker verifies the five-move carrier on all `7P4=840` ordered choices
of distinct symbols and the sign automaton on all 21 initial-run cases with
length `0,...,5`.  Two Prüfer constructions agree on the complete 125-tree
root-leaf template.

The exact endpoint census is

```text
descriptor              edit 1   edit 3   edit 5   edit 7   global
D_B classes                101      101      101      101      404
Z1 classes                  12        7        6        2       27
Z2 classes                   6        4        3        2       12
endpoint passes            125      125      125      125      500
endpoint failures            0        0        0        0        0
```

The shared closed `Z2` class has 193 rows, with per-edit counts
`75,60,41,17`.  The eleven open classes have the exact census

```text
v=2: ---:1, --+:3, -+-:11, +--:11, +-+:24
v=3: --:5,  -+:14, +-:46
v=4: -:24,  +:60
v=5: empty:108
```

Every `Z1` and `Z2` class is literal-word homogeneous and endpoint-correct.

## 4. Symbolic `Z2` iff

The independent proof in `symbolic_iff_audit.md` verifies both directions.
The formula visibly factors through `Z2`.  Conversely, identity is the unique
zero-length word; an open word has length `4L+5`, which determines `v` at
fixed `d`; and the first differing `epsilon` entry changes the first signed
transport pair at which two same-`v` words can differ.  Hence `Z2` is exactly
the kernel of the literal formula-word map at fixed rank.

This syntactic result does not imply endpoint correctness at another rank.

## 5. Digests and word inventory

Applying M231's normalization to the independently generated table reproduces
all three published digests:

```text
rows  43f9171c42c7b99be6de5b154a34cfc1cee0cee67c1db24743900df2f5d51ad3
Z1    50e4027978e590b6794c608a7d181d6c7bb9171d4f711baf624be6c56e31f2c2
Z2    fdf2836fee0b96d78a0bcf8c29b06a1a99b5209bcd8ac8e0c069efab34c8c512
```

There are exactly 12 odd formula words: identity plus eleven open carrier
conjugates.  The fixed nonidentity boundary words

```text
(R_7^-1)^2,
R_10^-1
```

are distinct from those twelve, giving fourteen full-table words.  The exact
signed-pair inventory is machine-readable in `cleanroom_results.json`.

Two consecutive runs of the final checker produced identical result bytes.

## 6. Numbered objections

**Material objections: none.**

**N-1 (nonmaterial provenance qualification).**  The predeclaration order is
supported by internal source assertions and filesystem chronology
(`quotient_descriptors.md` predates the checker and result), but not by a
cryptographic timestamp or external commitment.  This does not affect the
mathematical finite theorem: both quotients were derived symbolically, and
M234 reconstructed every endpoint without using M231 outputs.

## 7. Reproduction and strict scope

Environment: Python 3.12.3; nonstandard dependencies `{}`; seed `null`.

```text
cd experiments/20260811-polynomial-mixing-resolution/cycle-60/mission-M234-m231-fresh-referee
python3 -B m231_cleanroom_referee.py
```

The accepted result is only the exact finite `d=6 -> 7` ordinary odd-edit
formula compression.  It proves no all-rank closure, every-color or
arbitrary-representative route, voltage-corrected or polynomial total length,
spectral gap, mixing bound, or Terminal conclusion.

