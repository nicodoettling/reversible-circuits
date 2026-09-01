# M145 checkpoint

## Status

Required project skill and core sources have been read.  Frozen predecessor
proof artifacts were reconciled.  M140's corrected `L=5` theorem and scalar
bound `C_s<3/4` have now passed M144's independent referee and are accepted
inputs.

## Environment note

The default workspace sandbox currently fails during `bwrap` loopback setup
with `RTM_NEWADDR: Operation not permitted`.  Approved escalated commands are
therefore being used for scoped reads and writes inside the owned directory.

## Halfway structure

At `L=6` the exact support has 64 rows, 63 exceptional canonical basins,
22 positive `(k,t)` groups, 16 live deep groups, and 51 nominal positive
attachment ranks.  At the minimum boundary `s=7`, the six `t=2` groups have
rank-one children and exactly 31 ranks remain.  For a live group at height
`h`, degree `k`, and rank `j`, the child has suffix excess `h-1` and deficit
`k+1-j`; every `j=1,...,k` is retained before the rank-one boundary is
applied.

## Halfway obstruction and repair

The first natural envelope—corrected root reset followed by the full
`q_child(1-q_child)` budget for every right-heavy child—fails rigorously.  At
`s=7,K=128` it is `1.0003190402...` times the target, although the exact
finite-DAG value is only `0.6265122819...` times the target.  Thus this is an
envelope obstruction, not an `H` counterexample.

The repair is a uniform refined-reset recurrence.  For every canonical basin
let `c_E=degree(E)rho(E)`, `b_E=rho(B_E)=c_E lambda_E`.  Replacing an ordinary
basin by its exact exceptional current subtracts the full ordinary baseline
`b_E lambda_E=c_E lambda_E^2`.  This is one power of `lambda_E` on full basin
mass `b_E`, not the rejected `a_E lambda_E^2`.  Propagating the same refined
envelope through every child, including right-heavy children, yields a
multiaffine function of all Cayley ratios.

## Halfway exact result

The capped deterministic checker passes with zero failures:

```text
finite: s=7,...,104, degree 14 in z, 1470/1470 coefficients positive
tail:   seven ratios in [4/11,187/500], z in [0,1/2],
        C_S=3/4, multidegree (1,1,1,1,1,1,1,14),
        1920/1920 coefficients positive
```

The exact tail minimum is

```text
11435975715855226131133337 / 149750370000000000000000000.
```

Literal and grouped resets/resolvents agree on the selected `s=7,8` roots.
All 270 arbitrary-deficit checks through `L=4` pass; the tightest exact/bound
ratio is `761/763`.  The remaining work is proof exposition, independent
rerun/hash freeze, and the nine-field report; no broader extension will be
attempted.
