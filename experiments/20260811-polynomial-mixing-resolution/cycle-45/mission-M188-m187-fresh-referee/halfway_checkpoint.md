# M188 halfway checkpoint

Date: 2026-08-13 UTC.

## Immutable gate

Frozen M187 passed every one of its thirteen listed payload checks. Its
top-level digest is

```text
02b9ab4d382c6b52945492d6b808a3dad22eb51eb6d0d3e8eecc364a06bc28b2  SHA256SUMS
```

`final_scope.md`, `audit_correction.md`, and the controlling freeze manifest
were read before `proof.md` or `report.md`. M187 has not been edited.

## Independent result

The clean-room checker imports no M187 code or result. It reconstructs the two
named `d=5` source words, ten rooted DPS descriptors, and all seventy
coordinate/root/edit targets. Every source and target evaluates to identity
and has connected all-label support.

Across `7*5*5=175` root-pair occurrences, all right endpoint pairs are
eligible and they collapse to exactly 54 distinct quotient target tuples. The
signed-Hurwitz ball of radius five has level sizes

```text
1, 6, 40, 190, 795, 2976
```

for 4,008 visited tuples. Exactly fourteen targeted tuples occur in that ball,
with path lengths

```text
0,1,1,1,1,1,1,2,2,3,3,3,3,5.
```

Every one of the fourteen stored paths was applied afresh and reached its
recorded target. Their normalized route digest is

```text
e87ecd4742ab7392b3ef189f3f05a17757b75fac3fdba675074216468947fdc2
```

Post-replay comparison found all seventy target rows and every claim-bearing
summary field identical to frozen M187. The forty remaining distinct targets
are outside the radius-five witness set and have no negative interpretation.

## Scope audit

The formal endpoint criterion is correct: if all selected coordinates already
satisfy `[tau_i(u_c)]=[u_c]`, the empty word works; if all satisfy
`[tau_i(u_c)]=R_i[u_c]`, the one-letter synchronized word `R_i` works. This
criterion is invariant across each selected `H`-orbit but is formal/tautological.
M135 perfectness does not supply either hypothesis, because it chooses an
arbitrary `H`-orbit edge over each left global orbit and `tau_i` is only
`H`-equivariant. Thus every-color route existence remains unresolved.

There are stale-scope artifacts: `proof.md`, `report.md`, the noncontrolling
freeze manifest, and checkpoints retain the superseded geometric all-`d`
claim. They must not be cited as accepted. Also, frozen M187 archives route
counts and lengths but not the explicit sequences despite a report sentence
saying the paths are stored. M188's result now records all sequences.

## Next action

Write the numbered-objection audit note and nine-field report, then freeze the
M188 artifacts. No further search or enumeration is needed.
