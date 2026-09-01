# M309 sole finite reconstruction: `d=3`

Date: 2026-08-14 UTC.

The sole finite replay used M304's frozen clean-room checker, whose payload
hash is

```text
3302ce4083990b97c19fc9c029068ee552df66e03fce257e61a58c173f15ecba
```

The checker imports and reads no project artifact.  Inspection confirms that
it directly enumerates identity connected transposition words, constructs
the DPS edit maps, closes the six signed Hurwitz generators, forms the
global and root-stabilizer orbits, enumerates every perfect matching, and
then forms the action fibers.  The exact replay command was

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-87/mission-M304-m301-fresh-referee/independent_d3_check.py
```

and returned

```text
Z3=24 A3=216 global=4 H=12
guards=[(1, 12, 12, 0), (2, 12, 12, 0), (3, 12, 12, 0)]
matching=[0,1,2,9] witness=[0,2,9] pairs={0,2}:{45} {0,9}:{49} {2,9}:{89} triple=empty
```

Each of the three witness fibers has size nine.  Therefore, for any one of
the three anchors, the self-intersection contributes nine and the other two
pair intersections contribute one each, giving the exact RCOM score

```text
(9+1+1)/9=11/9.
```

Every displayed singleton action lies in exactly two witness fibers, so the
maximum agreement is at least two.  Empty triple intersection makes it at
most two.  Thus `max_a r_U(a)=2` exactly.  The zero in each guard row says
that none of the twelve complete matchings for any edit index is pairwise
compatible; complete-matching MT2H is therefore vacuous at this rank.  This
finite reconstruction supplies neither a Helly inference nor any statement
at actual `d>=6`.

