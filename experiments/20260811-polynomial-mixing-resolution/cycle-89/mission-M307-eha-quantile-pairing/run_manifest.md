# M307 run manifest

Date: 2026-08-14 UTC.

```text
repository commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
Python: 3.12.3
nonstandard dependencies: none
deterministic: yes
random seed: null
target: accepted M300/M303 channel-one all-middle EHA_1 coefficient
permutation convention: (pq)(x)=p(q(x)); displayed factors left-to-right
new finite ranks: exactly k=9, n=27
```

The analytic QCP_1 candidate and sole rank were fixed in `plan.md`, and the
quantile identity was written in `checkpoint.md`, before this command was
run from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-89/mission-M307-eha-quantile-pairing/qcp_k9.py --output experiments/20260811-polynomial-mixing-resolution/cycle-89/mission-M307-eha-quantile-pairing/qcp_k9.json
```

The checker is standard-library only, imports no project or predecessor
code/data, and fixes `k=9` in its source.  It was replayed once at the same
rank to `/tmp/m307_qcp_k9_replay.json`; both outputs have SHA-256 digest

```text
a77083ebf5ec54dcb5f31d434821921e06a274506b2993c6615db0cc4ca7dd61.
```

The script digest is

```text
4338b4f3572fa8ab1907838d2c7ef831bd224108d1d534217c90e81ceab57eb7.
```

No other rank or weaker-pairing search was run.
