# M240 halfway checkpoint

Date: 2026-08-13 UTC.

## Source/target relation fixed

For arbitrary old rank `d>=5` and ordinary odd edit `i=2v-3`, the target is
the exact physical endpoint comparison

```text
N=F_d(T,s_i pi_d)(0,d)^2,
A=F_(d+1)(T+{{1,d+1}},s_i pi_(d+1)).
```

The chronological convention is

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

No further finite-rank census has been performed.

## Substantive reduction

The open `Z_2` route has been reduced to a coordinatewise DPS Initial-Defect
Lemma (IDL).  With `x=v-1,y=d-1,z=0,n=d`, IDL specifies:

- one initial cursor discrepancy `(x,y)` versus `(x,n)`;
- for each larger direct child `r` of `v`, the doubled discrepancy
  `(r-1,y)^2` versus `(r-1,n)^2`;
- a common doubled parent edge at every other larger-label slot; and
- the exact four boundary factors needed by the five-move carrier.

The closed half of IDL says the naive and actual endpoints agree when the
stopped path is not strictly decreasing.

Generic Hurwitz algebra then proves the rest.  A positive pair transports a
cursor across any square; an inverse pair conjugates the square.  On a direct
child, the two conjugated squares both become `(r-1,v-1)^2`.  This yields a
literal induction through `Q` and the terminal carrier `B_d`.  The conditional
route length is `4(d-v-1)+5`.

## Strict status

The square identities, direct-child equalization, scan induction, terminal
carrier, and conditional length are proved.  IDL itself is not yet derived
from the global DPS stack closure.  Consequently no unconditional all-rank
route, every-color statement, congestion/gap/mixing result, or Terminal is
claimed.

