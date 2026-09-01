# M203 obstruction: DPS targets do not stabilize blockwise

Date: 2026-08-13 UTC.

## 1. Proposed premise

The hoped-for all-`d` extension was to regard M181's word as independent
six-factor `U/V` blocks plus fixed doubled-edge fillers, use M200/M196's
`d=5` quotient routes on the active block, and leave every other factor
unchanged. This requires at least the following compatibility:

> If an M181 word is enlarged by an untouched doubled leaf or another block,
> then applying a DPS adjacent-value edit internal to the old block produces,
> modulo global conjugation, the old DPS target enlarged by that same untouched
> data.

This premise is false already from `d=5` to `d=6`.

## 2. First exact physical witness

Take M181 pattern `0` at `d=6`, with distinguished root 5:

```text
X=(01)^2(02)^2(13)^2(04)^2(05)^2.
```

The clean targeted DPS inverse finds a rooted descriptor after 37 trials.
Swapping DPS values `1,2` (edit 1) gives the literal physical target

```text
Y=(01),(15),(02),(02),(35),(35),(04),(04),(01),(05).
```

Thus factor position 9 in the added leaf pair changes from `(05)` to `(01)`,
although both swapped DPS values lie in positions 1 and 2 of the original
six-factor block. The active-block edit is not filler-fixing.

Conversely, edit 7 in the nominal filler region changes positions 1--4 of the
active block. The coupling is two-way and comes from the global noncrossing DPS
closure, not ordinary adjacent-factor replacement.

Across the bounded all-root/all-edit `d=5,6` audit there are 178 rows, with
106 six-factor-region locality failures. At `d=6`, 29 active-block edits alter
filler factors and 22 filler-region edits alter active-block factors.

## 3. Quotient-level obstruction

Literal factor leakage alone could conceivably disappear modulo global
conjugation, so the checker performs a stronger comparison. At `d=5`, take
the exact DPS target for the same pattern and edit, then append an unchanged
new leaf `(05)^2`. Its canonical `d=6` quotient digest is

```text
bd651af9408f609196bcf37c3b6bfec37a7c126bd7b1ff2cfc11c7492e8d324f.
```

The actual `d=6` DPS target `Y` has canonical digest

```text
bed555f8c63642f18b33d3c0f2d6175fd96ff5afa467e8def150a7c44f5ee35b.
```

The classes are unequal. Among both patterns and all seven internal `d=5`
edits at the distinguished root, naive leaf stabilization agrees in 5 of 14
cases and fails in 9 of 14.

## 4. Exact no-go and surviving conditional lemma

Therefore M200's `d=5` paired target routes cannot be embedded into general
M181 words merely by shifting the braid to a block and treating other blocks
or fillers as synchronized fixed data. The anchored 200-move relation proves
full source voltage because it really is factor-block-local; the *DPS target
edit* has a different, global closure dependence. Conflating these two
operations is the failed premise.

The narrow surviving conditional statement is taut but exact:

> If, for a declared family of rooted embedded words and an edit, the actual
> matched quotient target tuple is globally conjugate coordinatewise to a
> product of independently routed local target blocks with synchronized fixed
> complement, then the corresponding local quotient words may be embedded and
> composed. M181's full-voltage theorem then allows a qualitative endpoint
> voltage correction after quotient reachability is established.

M203 proves that this factorization hypothesis is not automatic, failing at
the first added-leaf boundary. An all-`d` theorem now requires routes for the
actual globally coupled DPS targets or a new invariant/classification; the
`d=5` route table alone is insufficient.

## 5. Scope

This is not a proof that any `d=6` target is unreachable. It does not refute a
different all-`d` route theorem. It makes no statement about polynomial
quotient length, voltage-correction length, corrected total length, spectral
gap, mixing, or Terminal outcomes.
