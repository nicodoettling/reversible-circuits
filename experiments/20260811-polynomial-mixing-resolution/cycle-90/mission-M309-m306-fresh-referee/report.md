# M309 final referee report

Date: 2026-08-14 UTC.

## Frozen verdict

```text
ACCEPT M306 AT ITS STATED NONTERMINAL SCOPE.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL OBJECTIONS: NONE.
```

The supplied M306 top digest is exact, all nine M306 payload rows pass, and
all 30 payload rows across the four cited dependency inventories pass.  The
RCOM conditional identity and `RCOM => MRAD` follow by exact finite double
counting.  The WRAD statement is exactly the dual of the fractional action
cover LP.  `WRAD_q => MRAD_q`, while sorted weights give
`MRAD_q => WRAD_(qH_|M|)`; the accepted matching count makes the loss
`O(d log d)`.

The natural `Sym/Alt` identity matching has an exact one-action cover but
anchored score two.  This correctly refutes generic polynomial equivalence
of RCOM and MRAD without claiming an actual-M135 counterexample.  The sole
clean-room replay confirms the actual `d=3` values `11/9` and maximum
agreement two, with empty triple intersection and no Helly conclusion.

Actual RCOM/WRAD/MRAD at `d>=6` and polynomial literal representative length
remain unresolved.  No MRAD, SSTID, routing, voltage, congestion, gap,
mixing, or Terminal conclusion is accepted.

