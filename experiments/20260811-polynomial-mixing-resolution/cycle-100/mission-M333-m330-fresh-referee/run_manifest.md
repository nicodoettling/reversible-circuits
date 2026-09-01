# M333 run manifest

Date: 2026-08-14 UTC
Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
Role directory:
`experiments/20260811-polynomial-mixing-resolution/cycle-100/mission-M333-m330-fresh-referee`

Read-only work: M330 top and 12-payload verification; M323/M326/M329/M297
locks and inventories; direct M323 guard/result and M297 primitive locks; one
isolated Python 3 `-B` replay of frozen `na_k7_h2_a_fiber.py`; byte
comparison with the frozen result; final checksum and repository checks.

Replay parameters were exactly `k=7`, `n=21`, `H_2`, cell
`(1,1)`, `Sigma={0,1,6,14,20}`, and fixed B edges
`((6,14),(3,5))`. Output was temporary and is not frozen. No randomness,
nonstandard dependency, other cell, rank, row, or surgery was used.
