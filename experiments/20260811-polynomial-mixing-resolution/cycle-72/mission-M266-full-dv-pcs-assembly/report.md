# M266 report: unconditional fixed-cell response through PCS

Date: 2026-08-14 UTC.

Repository commit at start:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Verdict

```text
PROMOTE FOR FRESH IMMUTABLE AUDIT.
FULL DV AND THE AUXILIARY FIXED-CELL RESPONSE CHAIN THROUGH PCS ARE PROVED.
FD-BOUND OR MINORITY-SIGN REMAINS THE EXACT STOP.
```

All named predecessor inventories pass.  M251/M255's exact `Y-DV` bound
with constant `18400` and M258/M263's exact identity `X-Y=Theta` plus TAV
constant `500` have identical observables and domains.  Their direct
triangle therefore proves full DV with common constant `K_V=18900` for odd
`k>=3`, every cutoff `2<=ell<=(3k-1)/2`, and every adjacent rank
`1<=s<=k-2`.

Accepted DE has constant `7164`.  Substituting the discharged DV constant
into M252/M253 and M256/M259 gives

```text
K_J=18900K_E+7185,
C_W=18K_1+9K_2+340200K_E+129330.
```

`K_E,K_1,K_2` are the accepted absolute constants in the earlier scalar and
channel-one estimates; their sources do not freeze numerical values.  The
complete proved auxiliary chain is

```text
full DV + DE
 => full WPCR
 => SCBR
 => BR <=> BIR
 => Delta_k(C_k)=O(n^-2)
 <=> PCS-bound.
```

The audit retains the size-one singleton, both cutoff endpoints, the shared
and unequal-disjoint-mass channel-two endpoints, odd `n=3k`, and the full
`k=3` boundary case.  Nonnegative channel masses and the common `J=0`
cancellation license the exact full-prefix mixture.  No pointwise PCR is
used or proved.

PCS is a signed-total estimate.  The independent FD-bound

```text
k^2 sum_y|z_k(y+1)-z_k(y)|=O(1)
```

or the alternative minority-sign estimate remains necessary to reach
absolute fixed-cell L1.  Accordingly this report makes no FCL1,
`A_k(1,1)=O(1)`, direct-L1, all-edge, H0, bridge-gap, polynomial-mixing, or
Terminal claim.  Even a future FD closure would cover only the first
auxiliary fixed cell.

## Reproduction

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-72/mission-M266-full-dv-pcs-assembly/verify_assembly.py
python3 -m compileall -q experiments/20260811-polynomial-mixing-resolution/cycle-72/mission-M266-full-dv-pcs-assembly/verify_assembly.py
```

The checker is deterministic, standard-library only, and uses no randomness.
Its finite domain scan is arithmetic/domain falsification only, not the proof
of the universal inequalities.
