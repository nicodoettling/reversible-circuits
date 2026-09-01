# M295 report: fixed-middle GOCI pairing fails exactly

Date: 2026-08-14 UTC.

Verdict: **REJECT `(FMCP_1)`; KEEP the exact factorization and obstruction
for fresh audit.**

## Strongest result

For channel one, the accepted coefficient factors as

```text
beta_1(ef)=gamma_k(e)nu_M(f),
eta_1(F_ell)=sum_f nu_M(f) sum_e gamma_k(e)F_ell(ef).
```

This motivates a non-atomwise signed pairing: combine every exterior chord
at fixed middle chord and ask that the resulting cell be nonnegative.  The
candidate was frozen before computation and would imply `(GOCI_1)`.

It is false exactly at the sole tested new rank `k=5`.  The minimum witness
is

```text
f=(6,9), ell=6:
-779985545058827083283361063988362608513
/11367752922135489592720891699200000000000.
```

There are 16 negative fixed-middle cells among 120.  The reflected witness
at `ell=9` agrees exactly.  Nevertheless, every fully averaged channel-one
lag is positive, and the minimum accepted weighted `alpha_1 CP_1` value is
reproduced bit-for-bit.  This refutes only fixed-middle signing; it is not a
GOCI counterexample.

## Evidence

- all eight prerequisite M266/M268, M274/M277, M280/M283, and M285/M287
  frozen inventories pass `sha256sum -c`;
- exact standard-library checker `fmcp_k5.py`;
- machine-readable exact output `fmcp_k5.json`;
- direct residual-cycle, repaired autocorrelation, and independent positive
  `S/N` composition responses agree;
- exact normalization and reflection guards pass.

## Claim ledger

| claim | status | assumptions | evidence | action |
|---|---|---|---|---|
| exact `beta_1=gamma nu_M` fixed-middle factorization | proved | accepted M285/M287 conventions | `proof.md`, checker | retain |
| `(FMCP_1)` implies `(GOCI_1)` | proved | positive middle chord law | equation (2.3) | retain |
| universal `(FMCP_1)` | refuted | none beyond accepted scope | exact witness (4.1) | do not reuse |
| cancellation across middle-chord phases is necessary for this channel-one pairing route | proved | exact `k=5` witness plus positive full average | `fmcp_k5.json` | require cross-middle grouping |
| `(GOCI_1)` and `(GOCI_2)` | unresolved | accepted auxiliary fixed cell | no all-rank proof/counterexample | remain open |

## Scope firewall

No CP, OS+, MS, FCL1, FD, bridge-gap, mixing-time, or Terminal conclusion is
drawn.  No claim concerns odd `m`, `m=0`, `m=2`, or `N=2` in the main chain;
this mission acts only at the already-reduced odd-`k` auxiliary cell.

