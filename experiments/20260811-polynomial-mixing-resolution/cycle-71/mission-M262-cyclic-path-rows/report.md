# M262 final report: cyclic path rows

## Verdict

```text
REFUTE THE STATED CPR FIRST-ASCENT/FIRST-ABOVE-v TRANSITION.
RETAIN M257/M260 CP-1--CP-6.
```

For every rank `rho>=8`, the admissible tree (2.1) has stopped path
`4 -> 6 -> 1` and exposed set `E_4={6}`. Direct CP-5 substitution into the
strict nonroot CP-2 row at `a=6` gives

```text
W_6^6 S B_6^6 -> S,
```

so the exposed label has distance one, not distance three. The exact residual
is

```text
S S B_4^9 B_4^8 B_4^7 S W_4^7 W_4^8 W_4^9 W_4^10 S S,
```

another literal open frontier rather than a sealed canonical word. The two
new labels at rank `rho+1` disappear through the same distance-one interval
chains, so the obstruction is rank-coupled and arbitrary-rank.

The first repair must distinguish at least `O^-` (current vertex below `v`)
and `O^+` (current vertex above `v`). In the boundary path `v<a->1`, an
actual `O^+` word reaches the root seam, making the old abstract `O/C` RST
input insufficient. A refined directional transducer and its literal root
tables remain open.

The minimal checker replays only ranks eight and nine:

```text
python3 -B literal_row_check.py
```

It is a falsification guard for the displayed rewrite, not a rank census and
not the proof of the universal claim.

Reproduction metadata:

```text
repository commit        502a6f031c6d5a4bc0064ee5b370a4fa3914f993
Python                   3.12.3
nonstandard dependencies none
seed                     none (deterministic)
raw output               literal_row_results.json
```

This refutation does not refute IDL itself, any accepted finite endpoint
identity, or the possibility of a refined signed/directional proof. No fixed
edit, routing, congestion, spectral-gap, mixing, or Terminal conclusion is
made.
