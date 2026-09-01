# M144 freeze manifest

Frozen: 2026-08-13 UTC.

Verdict: **ACCEPT**, with zero material objections.

Accepted only within the explicit auxiliary dependency boundary:

```text
C_s<74969/100000<3/4 for every s>=100;
H(s,K,K-1,s-5)<q(1-q) for every s>=6,K>=1,
q=w_6 w_(s-5)/w_(s+1).
```

The second statement is relative to accepted M109/M114, M115/M116,
M117/M121 recurrence and lower-excess inputs and M138's corrected structural
implication. It uses one-power `q a_E lambda_E`; the rejected M131
`lambda_E^2` display is not used. No gap, mixing theorem, or terminal
follows.

## Frozen payload

| file | SHA-256 |
|---|---|
| `plan.md` | `f5220e3318bf58a8e661426ef36ba0692d85cfa7269013cfad4c9672b0c12e85` |
| `checkpoint.md` | `b800684282a8552bd70dcb869c769f0a0277784ec8f4f15d3041ecd2db17d019` |
| `fresh_referee.py` | `a95b6a6c048a70f583050a5e9336b6ae662e42493949d49d908f3196d50a8ea2` |
| `fresh_referee.json` | `6c000e1a56f645267abed3786bfbc9df25dd13c92f782e40f747866d8f2a395e` |

The final report and this manifest are added to `SHA256SUMS` after their
bytes are fixed. `SHA256SUMS` intentionally does not hash itself.

## Exact outcome

The clean-room result has zero failures, 1,222 positive finite coefficients
with digest `733243ff50622263540085ff0d6d4b01246164cc8119003cacb5dbeda11684f7`,
and 4,212 positive tail coefficients with digest
`2c1aa8475dba3ae3d3c09f587662facb78b1c11e14aec2d04ae8d87bb5adf22f`.
The `s=6` boundary is strict.

