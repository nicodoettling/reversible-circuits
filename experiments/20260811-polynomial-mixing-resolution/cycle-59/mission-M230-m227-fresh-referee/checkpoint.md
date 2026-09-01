# M230 checkpoint

Date: 2026-08-13 UTC.
Status: decisive audit complete; freeze in progress.

The isolated ownership boundary, immutable M227 digest target, clean-room
reconstruction obligations, exact certificate checks, and prohibited
inferences are fixed in `plan.md`. No M227 payload has been modified.

M227's checksum ledger has digest
`7b679294f7c6a4aa956a3577ae3350880698eb92d7b5776157f5f0e444e09105`;
all eight payloads and the complete nine-file inventory pass.

Verdict: `REJECT M227 AS A SELF-CONTAINED FROZEN PROOF`, with material
objection M-1. Its six-coordinate primal restriction does not generally
preserve `<G,C>`, and its six-dimensional dual matrices are not by themselves
certificates for the declared seven-dimensional program.

The numerical conclusions are independently salvaged. The clean-room checker
constructs exact seven-dimensional dual completions. For width one it uses
`y=(869/1494)X[:,5]` with Schur pivot `25/747`; for width two it uses
`y=(-43/54)X[:,4]+(419/324)X[:,5]` with Schur pivot `97/3564`. Every on-band
entry equals the full `G`, every full exact `LDL^T` pivot is positive, and
`e_6=0` preserves the dual objective. Zero extension supplies the full primal
certificates. Thus the two brackets and all three strict separations are
correct in full dimension. The corrected theorem will be frozen only in M230.
