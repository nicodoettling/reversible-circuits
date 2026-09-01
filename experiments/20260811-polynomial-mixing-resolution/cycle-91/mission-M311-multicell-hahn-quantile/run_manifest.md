# M311 Run Manifest

Date: 2026-08-14 UTC

```text
repository commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
Python: 3.12.3
nonstandard dependencies: none
deterministic: yes
random seed: null
target: auxiliary channel-one all-middle MCLP_1 coefficient
candidate: pre-frozen QBP_1 maximal Abel sign-block compensation
new finite ranks: exactly k=11
alternate groupings: none
```

The candidate was written to `candidate_frozen.md` after the analytic QBD_1
derivation and before any finite execution.  The sole guard command, run once
from the repository root, was

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-91/mission-M311-multicell-hahn-quantile/qbp_k11.py --output experiments/20260811-polynomial-mixing-resolution/cycle-91/mission-M311-multicell-hahn-quantile/qbp_k11.json
```

Frozen code/output hashes:

```text
qbp_k11.py    703f4d8db29c60ee3f1d3f1cd7418aa11782f9a309a310c2a259d8d30d09eb94
qbp_k11.json  d661dc818b676825055f9366d52a6b4bc104f7f9df44bfd3ece2f3043bdceba6
```

The checker imports no project or predecessor code/data and uses exact
`Fraction` arithmetic.  No stochastic run, second rank, replay, or
replacement-candidate search was performed.
