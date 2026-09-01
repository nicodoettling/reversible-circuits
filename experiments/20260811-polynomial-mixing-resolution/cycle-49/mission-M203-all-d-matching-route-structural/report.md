# M203 final report: blockwise all-d extension obstructed

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: REJECT THE PROPOSED INDEPENDENT d5-BLOCK EXTENSION.
KEEP AN EXACT STRUCTURAL OBSTRUCTION; ALL-d ROUTE EXISTENCE REMAINS UNRESOLVED.
```

The DPS matched-target edit is not local to M181's six-factor blocks and does
not generally preserve added fillers even modulo global conjugation.

## Field 2 — immutable provenance

Every file in M181/M183, M196/M198, and M200/M202 passed its frozen manifest.
Top digests are

```text
M181 d2ae8d5a2af347eb74943db1221607d46fc706296ac2802d97abc0a024ec20b0
M183 ddd2bf1d2ce8d22e2228624d8802b38a527fee27819b92f9f06c3393b567fa46
M196 7fa987c6c776e55990c00fcfaea85e34c1d7b0e6d3f97d57fdefba8bcb5bd913
M198 1142912065699b883268b16aee8707b1c1e0d7c4b006eb1ca9bb02282ef9bd84
M200 6561e28aa199fc1d463881f399f116bd3c05222d6d26e9f54992ff1b542f2045
M202 33f34abf2f6d763b61fd15e6f64c895249792e70dab933894242584886491f70.
```

No predecessor was edited.

## Field 3 — exact target and method

The target was a structural extension of M200's `d=5` every-color quotient
routes to M181's explicit all-`d` block family. The checker uses the exact DPS
boundary closure only on M181's explicit rooted words at `d=5,6`; it does not
enumerate `Q_6` or any `Q_d` for `d>=6`.

There is no probability distribution or Markov kernel in this mission.

## Field 4 — factor-level locality failure

The all-root/all-edit bounded table has 178 rows; 106 fail six-factor-region
locality. At `d=6`, 29 rows have an active-block edit changing added filler
factors, while 22 rows have a filler-region edit changing active-block
factors.

The first distinguished-root witness is

```text
source X=(01)^2(02)^2(13)^2(04)^2(05)^2,
edit 1 target Y=(01),(15),(02),(02),(35)^2,(04)^2,(01),(05).
```

Position 9 of the added `(05)^2` leaf changes, despite edit 1 being internal
to positions 1 and 2.

## Field 5 — quotient-level obstruction

Naively append `(05)^2` to the corresponding `d=5` DPS target. Its canonical
`d=6` digest is

```text
bd651af9408f609196bcf37c3b6bfec37a7c126bd7b1ff2cfc11c7492e8d324f,
```

whereas the actual `d=6` target digest is

```text
bed555f8c63642f18b33d3c0f2d6175fd96ff5afa467e8def150a7c44f5ee35b.
```

They are different quotient classes. Across two patterns and seven edits,
naive leaf stabilization agrees in only 5 of 14 cases and fails in 9.

## Field 6 — exact structural conclusion

M181's anchored relation remains block-local and correctly proves full source
voltage. But the matched DPS target is defined through a global closure, so it
cannot generally be decomposed into independent `d=5` targets plus fixed
complement. Consequently M196's local `d=5` routes cannot be shifted/composed
to prove the desired all-`d` theorem by this argument.

The narrow surviving route requires separately proving quotient factorization
for a restricted family, or directly routing the actual coupled targets.

## Field 7 — nonreachability and voltage/length boundaries

No `d=6` target is proved unreachable. This only rejects the proposed
factorized construction. If quotient reachability is proved by another
method, M181's full voltage and M175's affine theorem still supply a
qualitative zero-voltage endpoint correction.

An ordinary quotient word need not have zero voltage. No quotient length,
correction length, corrected total length, or polynomial bound is proved here.

## Field 8 — reproduction and hygiene

Python is 3.12.3, dependencies `{}`, seed `null`. Commands were

```text
timeout 120s python3 -B run_locality_d56.py
python3 -B leaf_stabilization_probe.py
```

Both use only the standard library and exact arithmetic. Raw tables are
`locality_results.json` and `leaf_stabilization_results.json`. All writes are
confined to M203.

## Field 9 — final boundary and audit request

```text
REJECT ONLY THE AUTOMATIC INDEPENDENT-BLOCK EXTENSION.
RETAIN d=5 EVERY-COLOR ROUTING AND M181 ALL-d SOURCE FULL VOLTAGE.
LEAVE ACTUAL d>=6 MATCHED-TARGET REACHABILITY UNRESOLVED.
```

No all-`d`, nonreachability, polynomial-length, gap, mixing, or Terminal
conclusion follows. Freeze this package and request a fresh immutable referee
to reproduce the rooted descriptor, the first physical/quotient witnesses,
and the scope boundary.
