# Growing hidden identities: dense-host scaling check

Date: 2026-11-10, Europe/Berlin. Starting Git commit
`c4331bada5575f58ad463e62479ff20015305759`; the preceding planted-subsequence
experiment and map integration are present as uncommitted work and preserved.

User refinement: focus on a poly(log N)-gate or N-gate hidden identity in an
N^2-gate identity host, and also consider a poly(log N)-gate plant in an
N-gate host. The earlier k=m-2 case was an attack control, not this target.

## Frozen game

Use Q4's global all-transposition law, explicit N-point permutations,
rightmost-first products, fresh hidden uniformly random k-subset on each
sample. D0=U(N,m); D1 chooses I then samples U(N,m)|E_I. No noise or oracle.
All lengths are even. The default proposed security convention is adversaries
polynomial in explicit N,m with negligible advantage in N. State separately
why inverse-polynomial-in-N leakage would not refute a different convention
using log N as security parameter. No Markov kernel or burn-in is involved.

## Named obligations

1. State candidate schedules precisely, rather than treating constant-k
   controls as evidence about growing plants.
2. Check cheap random-pair equality and shared-label tests. Use multiplicative
   completion bounds before conditioning on the potentially rare plant event.
3. Verify whether a moment-ratio lower bound reaches k=N. Keep the m=N host
   separate if long-completion smoothing fails there.
4. Check required spectral identities and the lazy/nonlazy parity translation
   against primary literature. This is a scoped dependency audit, not a broad
   literature search.

## Finite verification

Compute exact transposition return counts from partition spectra, with
dimensions from the tableau corner recurrence. Independently check these
against elementary cycle-type cut/join counts for N2..8 and short lengths.
Check pair-event ratios, spectral smoothing and the proposed radial-operator
bound at N4,6,8,12,16,24,32. For the finite schedules put L=ceil(log2(N))
and use k=N, k=2 ceil(L/2), and k=2 ceil(L^2/2). This integer-log convention
has the same asymptotic scale as rounding the logarithmic power directly;
the exact k is recorded in every row. Record infeasible parameter cases
rather than altering the game.
Use exact rational bounds on distinguishing advantage for m=N^2. For m=N,
record when the bound does not apply, without interpreting that as security.

Python 3.12.3 standard library only. Deterministic arithmetic; no random seed
or Monte Carlo conclusion. Store code, raw rational results, source audit,
proof/obstruction and a verdict. Check mandatory S3m4/S4m4/S4m6 counts and
N2/m0/m2/odd controls. Do not install packages or launch agents/campaigns.
