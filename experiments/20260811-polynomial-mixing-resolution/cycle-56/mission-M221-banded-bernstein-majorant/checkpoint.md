# M221 checkpoint

Date: 2026-08-13 UTC.
Status: substantive halfway theorem complete; report and freeze pending.

The requested skill/source lock has been refreshed. M210/M213 and M216/M219
all have the expected checksum-ledger digests and every frozen payload passes.
The degree-cap banded cone and exact primal/dual pair were fixed in `plan.md`
before numerical or exact certificate search began.

The single exact row is now decided. The accepted width-zero dual has positive
budget excess, while the compact rational tridiagonal matrix

```text
diag=(101/50,111/100,43/100,19/25,39/25,99/50,21/5),
off =(1/3,2/15,1/12,1/5,3/5,11/8)
```

has `C>0`, `C-A>0`, and charge `4937603/9172800`, leaving exact budget
slack `485323987/37571788800`. Both PSD claims follow from strict signed
diagonal dominance with exact rational row margins. Therefore the least
feasible coefficient bandwidth at this row is exactly one.

The closure audit is also decisive but negative: saturated likelihood lifts
preserve bandwidth, whereas a retained unsaturated `d=1,a=0` lift sends a
bandwidth-one child atom to a degree-six rank-one matrix of bandwidth five.
The general raw upper bound is `w+(L-n)`. A coarse positive-linear diagonal
envelope exists, but a cost-controlled recursive width-one envelope remains
unresolved. No recursive contraction claim follows.

