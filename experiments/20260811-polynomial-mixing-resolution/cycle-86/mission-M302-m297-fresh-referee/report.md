# M302 Fresh Referee Report on M297

Date: 2026-08-14 UTC

## Verdict

**ACCEPT M297 AS FROZEN AT STRICT REDUCTION-ONLY SCOPE.**

Material objections: none.  Nonmaterial objections: two notation
clarifications, neither affecting a derivative or conclusion.

## Accepted result

For every odd `k>=3`, M297 correctly proves that accepted M290/M293 BODT
differs by an `O(1/k)` vector from SODT.  This removes every large-owner term
inside a boundary state, including both `U_small/U_large` correlation
orientations, only after the complete signed coefficient `omega=P_B-P_A` is
formed.

M297 also correctly expands SODT into

```text
-sum_d u_d Delta H_d
+sum_(d,e)u_d u_e Delta C^off_(d,e)
+sum_d(u_d^2+e^2 delta_d)Delta A_d.
```

The ordered off-diagonal and diagonal conventions are exact.  Size-one rows
vanish; at sizes two and three only the self-owner derivative vanishes, while
first-order and distinct-owner rows remain.  The three displayed SOCL bounds
would imply the scalar estimate by Borel-mass summability.

Thus the accepted chain is

```text
SOCL => SOCT <=> SODT <=> BODT <=> DOR,
```

where SOCL remains unresolved and removal equivalences are at the `O(1/k)`
assertion level.

## Integrity and stop

M297's top digest is
`a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792`.
Its inventory and all twelve cited predecessor inventories pass.

This report does not infer SOCL, BODT/DOR, PBV/FD, FCL1, a spectral gap,
polynomial mixing, or either Terminal.  The next obligation is an all-rank
proof or counterexample for SOCL, or a direct proof of weaker SOCT.

