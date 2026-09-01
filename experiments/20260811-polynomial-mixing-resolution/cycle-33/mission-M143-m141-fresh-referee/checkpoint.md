# M143 checkpoint

Date: 2026-08-13 UTC.

## Durable status

- Read the project handoff, goal specification, project skill, sampling
  reference, and experiment standard.
- Resolved assignment shorthand to M141's frozen filenames.
- Verified all assigned immutable SHA-256 values exactly:
  - report `ebda7181e031603f598648d2409f8a484645022f24acd34e92ef5813459afb87`
  - theorem `7c9588dc64e3731a90e3e59bbe60a4d15dc8a42c4f98ce7ed60c386c7e8b8678`
  - checker `44f8fd167808bb41d2823bb10943951d6404d88aa4530697760a914b1e321d93`
  - results `548ddf460a9184ebdc36c449ba35e8e2b8c3719b4994200808afa8868590c241`
  - manifest `b45f4a80ca8745a9f7e6291b5118b27a64e22040a7799f872773624aff671e62`
  - checksum list `9aa52349d288f04b7f46895cf7fe01373dcea807abf69892ef3ccea705acc057`
- Read M141's theorem, report, and checker plus the accepted M135 proof and
  M137 referee report on the exact pair dichotomy used as an input.
- Preliminary proof inspection finds the scope separation explicit: M141
  claims a necessary generated-subgroup invariant only, not common-braid
  realization.

## Environment note

Ordinary shell calls are currently blocked before execution by
`bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`.  Approved
read-only elevated calls work.  This is an execution-environment issue, not
an input-integrity blocker.

## Next

Complete a line-by-line clean-room proof audit, implement and run a bounded
independent checker, then write the nine-field final referee report with an
explicit numbered-objection verdict.

## Final checkpoint

- The bounded clean-room checker compiled and completed successfully in about
  3.4 seconds, with no predecessor module or result import.
- It reconstructed all `24` words and `72` rooted coordinates at `d=3`, and
  all `2880` words and `11520` rooted coordinates at `d=4`.
- It reproduced all decisive M141 exceptional-rank counts, the exact rank-four
  `96 -> 288` witness, and exact normal-generation checks for `A_5,A_6`.
- The proof audit found zero material numbered objections. Final verdict:
  accept M141 only as its stated nonterminal negative sharpening.
