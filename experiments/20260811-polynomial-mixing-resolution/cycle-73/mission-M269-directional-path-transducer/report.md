# M269 final report: directional path transducer

## Verdict

```text
PROMOTE THE DECORATED CYCLIC-WIDTH TRANSDUCER FOR STRICT INTERNAL CP-2 ROWS.
DO NOT PROMOTE IT ACROSS a=1 OR AS CPR/RSPT/IDL.
```

Reindex labels cyclically from the edited incidence `R_v`. The actual open
frontier at a current path vertex `a` is not determined by `O^-` or `O^+`.
It is a lens of width

```text
r_v(a)=(R_a-R_v) mod M
```

whose black arm lies at `x_v`, whose white arm lies at `y_v`, and which
retains a literal port for every rooted child `h` of `v` with
`t(h)<r_v(a)`. Accepted canonical child substitutions form exact two-label
macros: depending on the arm, both slot rows close at distance three against
`x_v` or the current parent black vertex.

For every strict internal parent `b!=1`, with `s=r_v(b)`, the full CP-2 row
including arbitrary siblings and post-wrap children obeys

```text
F_v(r) -> F_v(s) if s<r,
F_v(r) -> C_b    if s>r,
C_a    -> C_b.
```

On contraction, direct-child ports below `s` persist and those between
`s,r` discharge. On expansion, every port discharges and the exposed label
`R_v` receives its distance-three row, leaving the canonical residual.
The analytic proof is an arbitrary-length interval induction using a literal
six-token child gadget; it is not inferred from finite data.

Direction alone fails even without ports. For every `rho>=9`, the two paths

```text
4 -> 5 -> 6 -> 1,       4 -> 7 -> 6 -> 1
```

arrive at the same next parent from `O^+`, but the first expands and seals
while the second contracts and stays open. Likewise

```text
6 -> 2 -> 3 -> 1,       6 -> 4 -> 3 -> 1
```

give different outputs from `O^-`. The theorem supplies these arbitrary-rank
families; no rank census is used.

The deterministic four-row guard covers initialization with retained and
discarded ports, contraction, expansion, canonical propagation, siblings on
both arms, and post-wrap positions. All rows and declared distance-three
endpoints pass. It is finite calibration only.

The exact first open lemma is DL-RST: feed the literal reversed base,
decorated lens, or canonical residual into M257 CP-6 at `a=1`, include the
new child `d`, and prove the two-rank endpoint/root tables through final root
completion. This mission does not evaluate that row and therefore does not
prove CPR, RSPT, repaired RSMI+, IDL, routing, a gap, mixing, or a Terminal.

Reproduction:

```text
repository commit        502a6f031c6d5a4bc0064ee5b370a4fa3914f993
command                  python3 -B four_row_guard.py
Python                   3.12.3
nonstandard dependencies none
seed                     none (deterministic)
raw output               four_row_guard_results.json
```

