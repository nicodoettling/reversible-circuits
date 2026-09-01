# M223 freeze manifest

Date: 2026-08-13 UTC.

## Frozen verdict

`ACCEPT M220 AS FROZEN`. Numbered material objections: none. Numbered
nonmaterial objections: none.

## Exact certificates

```text
M220 SHA256SUMS digest       0b953e9c517cfeb379d32abe04b32ea928dd2a83e67bc1ac40d61f87fccd1316
carrier checks              840 / 840
double-inverse checks       210 / 210
single-inverse checks       441 / 441
d5 trees / rows / failures  16 / 112 / 0
d6 trees / rows             125 / 1125
d6 passes / failures        1098 / 27
pass counts by edit         114,125,125,125,125,125,109,125,125
d6 row digest               f0deca809ef570f7d557a88a94d517e3885f971f0178ac7ef2938bad651341c0
```

The exact first witness, equal descriptor, 17-move common word, and positions
7--8 `(45)^2` versus `(46)^2` mismatch all replay independently.

## Method and scope

`fresh_recurrence_referee.py` is the authoritative clean-room checker. It has
no M220 import/path/data dependency, no route search, and no quotient-state
enumeration. A post-hoc comparison was performed only after all expected
assertions passed.

The accepted no-go refutes only the displayed key-to-word recurrence. It does
not refute a different braid, richer descriptor, or other all-rank route. New
edits 8/9 are finite facts only. No every-color, length, gap, mixing, or
Terminal conclusion follows.

## Payload inventory

The frozen payload is exactly the files listed in `SHA256SUMS`; no bytecode
cache is included.

