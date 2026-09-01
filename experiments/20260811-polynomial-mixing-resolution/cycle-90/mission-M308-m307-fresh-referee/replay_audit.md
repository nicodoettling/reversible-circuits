# M308 Replay Audit

Date: 2026-08-14 UTC

Successful command, run once from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-89/mission-M307-eha-quantile-pairing/qcp_k9.py --output /tmp/m308_qcp_k9_replay.json
```

Environment:

```text
repository commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
Python: 3.12.3
nonstandard dependencies: none
random seed: null (deterministic exact arithmetic)
new ranks: none beyond frozen sole rank k=9
```

Digest comparison:

```text
a77083ebf5ec54dcb5f31d434821921e06a274506b2993c6615db0cc4ca7dd61  /tmp/m308_qcp_k9_replay.json
a77083ebf5ec54dcb5f31d434821921e06a274506b2993c6615db0cc4ca7dd61  frozen qcp_k9.json
```

Two initial tool invocations failed before process creation because the local
sandbox launcher path was absent.  They executed no checker and produced no
output.  The successful authorized invocation above is the mission's sole
replay.  No broad census, second rank, or alternate pairing search was run.
