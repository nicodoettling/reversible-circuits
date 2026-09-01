# M204 checkpoint

Date: 2026-08-13 UTC.
Status: substantive audit complete; freezing `ACCEPT`.

## Immutable gate

- Ownership remained restricted to M204; M201 was never edited.
- Frozen M201 has exactly nine files (its SHA ledger plus eight payloads).
  `sha256sum -c SHA256SUMS` passed `8/8`; the SHA-ledger digest is
  `9ede2ffaf0815cc76d8a7811d542d4a967370ee10791af73a590692ecacd524a`.
- The accepted M173/M177, M179/M184, and M193/M197 dependency ledgers all
  passed before their theorems were used.

## Independent exact reconstruction

The standard-library `Fraction` checker imports no M201 code. Unlike M201's
grouped Cayley-root implementation, it expands every literal ordered
composition with mass

```text
prod_i w(c_i)/(len(c)! w(sum(c)+1)).
```

Those masses sum to one at every recursively used size `2,...,6`. The checker
deletes killed `a=d`, retains all bivariate Gram cross terms, and performs the
exact covariance subtraction only after assembling each branch.

At `(B,L)=(2,4)` it independently obtains

```text
q=3750/16807,                 q0=2/3,
U1=3299/56250,                U2=24/125,
U3=27/125,                    Delta=293289307/945393750.

T_reset=6628367198857337/21450464220937500,
T_h4=1735419680239/29524500000000,

T_reset+T_h4-Delta
 =480024264873449410111/8339940489100500000000 > 0.
```

The full actual-history sum is

```text
T1=422384074903914714287/1042492561137562500000,
(1-q)-T1
 =387506171468022785713/1042492561137562500000 > 0.
```

## Provisional-to-final verdict

`ACCEPT`, with no material objections. The witness refutes only independent
reservation/addition of the accepted `h=1,2,3` upper bounds before bounding
reset plus `h>=4`. It refutes neither the true contraction inequality nor any
individual accepted lower-height theorem. No new tail statement was tested.
