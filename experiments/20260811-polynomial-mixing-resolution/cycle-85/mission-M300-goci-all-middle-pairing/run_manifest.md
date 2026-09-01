# M300 run manifest

Date: 2026-08-14 UTC.

```text
repository commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
Python: 3.12.3
nonstandard dependencies: none
deterministic: yes
random seed: null
target: auxiliary first separated fixed-cell channel-one GOCI coefficient
permutation convention: (pq)(x)=p(q(x)); displayed factors left-to-right
new finite ranks: exactly k=7, n=21
```

Commands, run from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-85/mission-M300-goci-all-middle-pairing/mclp_k7.py --output experiments/20260811-polynomial-mixing-resolution/cycle-85/mission-M300-goci-all-middle-pairing/mclp_k7.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-85/mission-M300-goci-all-middle-pairing/exterior_abel_k7.py --output experiments/20260811-polynomial-mixing-resolution/cycle-85/mission-M300-goci-all-middle-pairing/exterior_abel_k7.json

python3 -m compileall -q experiments/20260811-polynomial-mixing-resolution/cycle-85/mission-M300-goci-all-middle-pairing
```

The first command evaluates the sole predeclared candidate falsifier. The
second checks only coefficient formulas at that same rank; it is not a
second rank or response-sign scan. Replays to `/tmp` matched both frozen raw
outputs byte-for-byte and were then removed.

The source instruction `references/experiments.md` did not resolve; the
skill-owned actual path
`.codex/skills/reversible-circuit-sampler/references/experiments.md` was
read and used.
