# M209 checkpoint

Date: 2026-08-13 UTC.
Status: substantive audit complete; provisional `ACCEPT`.

## Immutable gate

- Frozen M206 has exactly nine files: `SHA256SUMS` plus eight payloads.
- All eight M206 payload hashes pass. Its SHA-ledger digest is
  `32aaa34fc8ec8a19851621a912d834eec5d7b00e339fea8826a589286417a866`.
- Every cited accepted ledger passed: M173/M177, M179/M184, M193/M197,
  M201/M204.
- M206 and all predecessors remained immutable.

## Independent reconstruction

The standard-library `Fraction` checker imports no predecessor and evaluates
only `(B,L)=(2,4),(3,4)`. It uses grouped Cayley root masses, independently of
M206's M204-backed literal-root implementation. It retains full bivariate
Gram kernels, every likelihood cross term, parent covariance subtraction, and
deletes killed `a=d` explicitly.

The assembled history-kernel `T_1` equals the sum of reset and height-sector
charges in both rows, independently checking orthogonal-sector additivity.
Every promoted exact fraction reproduces.

## Structural and logical audit

- At total/bottom `(2,2)`, the compositions `(2),(1,1)` produce neither an
  active reset endpoint nor a live root group. Hence `Phi=0` for every beta
  parameter pair, and every fresh `B=2` height-one sector is actually zero.
- At `B=2,L=4`, `S_1-X>0` exactly.
- At `B=3,L=4`, `S_1-X<0` and `S_1+S_2-X>0` exactly.
- With `S_h=U_h-T_h`, `Delta=1-q-sum U_h`, and
  `X=T_reset+sum_(h>=4)T_h-Delta`, direct algebra gives
  `(1-q)-T_1=sum S_h-X`; all signs are correct.
- The two-rung positive result is finite only. M206 does not claim a
  universal two-rung inequality or universal contraction. Its cumulative
  three-rung lemma remains unresolved.

Provisional verdict: `ACCEPT`, no material objections.
