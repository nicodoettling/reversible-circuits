# Bounded two-subagent sandbox smoke test

## Verdict

`PASS`

Exactly two subagents completed in one dispatch wave. Worker A used complete
length-four word enumeration; Worker B used four-step permutation-state dynamic
programming. Both independently obtained the exact finite counts
`S_3, m=4 = 27` and `S_4, m=4 = 120`.

Both workers created their required workspace files. Each required forbidden
`touch` attempt returned exit code `1` with a read-only-filesystem error, and
the coordinator independently confirmed that neither outside path exists.
Bubblewrap was present and reported version `0.9.0`; no bubblewrap error or
approval prompt was observed.

The coordinator inspected every required worker artifact, parsed both JSON
files, checked the method-specific implementations and composition conventions,
and reran both exact scripts. This is only a finite infrastructure validation
and makes no research or mixing-time claim.
