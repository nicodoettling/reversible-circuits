# Mission M234 Checkpoint

Date: 2026-08-13
Status: initialized; no conclusion yet

The required project sources have been read.  The audit is locked to the frozen M231 exact finite `d=6 -> 7` descriptor-compression claim.  No M231 code or data will be imported into the clean-room checker, and no predecessor file will be modified.

## Independent result fixed before normalization comparison

The no-input clean-room checker now reconstructs the full template from the
DPS hairy-tree closure.  It does not execute, import, or read M231 code/data.
The first fixed run gives:

```text
carrier checks                 840 / 840
initial-run sign checks         21 / 21
trees / odd edits / rows       125 / 4 / 500
endpoint passes / failures     500 / 0
D_B classes by edit/global     101,101,101,101 / 404
Z1 classes by edit/global      12,7,6,2 / 27
Z2 classes by edit/global      6,4,3,2 / 12
closed rows                    193
odd / boundary / total words  12 / 2 / 14
```

The independently fixed native canonical digests are

```text
rows ff8d7beeec42a12003ad14241cd82e42dfeead0858bce3c1d4a78e2a36927bbb
Z1   07de53c3181c11af5c53a1f08da3ace4d2d53f889a78be230146964263afe449
Z2   18f1375cdbc892f00ee5125c288c7b733d9006b224913d3dd6e23264d3f45164
```

These values were fixed before any M231 serialization code was inspected.
The structural counts and census match the frozen claim.  Next: perform a
quarantined read-only normalization audit to see whether applying M231's
published canonical serialization to these independently constructed objects
reproduces its row/Z1/Z2 digests, then freeze the referee report.
