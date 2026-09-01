# M247 checkpoint

Status: final audit complete; freeze preparation in progress.

All M244 payload hashes verify, with top inventory digest
`134082cd80dac7dcd890669fb84db0c8a978811c1f177564263c8b56f692628d`.
M240 and M242 verify at their declared top digests, and the locked DPS PDF
verifies at
`98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2`.

The canonical slot, literal excursion, and bottom-up colored pruning proof
have passed independent line audit.  Theorem 3.1 leaves exactly `W^R_a` and
correctly excludes edited `x_v`.

The RSMI/full-IDL package is rejected.  Literal unqualified RSMI(2) has a
one-row exact counterexample at `d=7`, and the written implication also omits
factor-level assertions needed for IDL-a, IDL-c, and the sealed/closed root
case.  Repaired `RSMI+` and IDL remain unresolved after rejecting the frozen
formulation.
