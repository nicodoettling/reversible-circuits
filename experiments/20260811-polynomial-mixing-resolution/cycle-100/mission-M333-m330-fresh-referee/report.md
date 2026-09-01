# M333 final referee report

Date: 2026-08-14 UTC

## Frozen verdict

```text
ACCEPT M330'S APPEND-ONLY SALVAGE.
MATERIAL OBJECTIONS: 0.
NONMATERIAL OBJECTIONS: 0.
```

## Numbered objections

1. None.

## Findings

1. M330 has the required top
   `623ec4026179c81cc2a1ec49ce3318af470562924d7a34ac5bc6a6ba76547f93`;
   all 12 payloads verify. M323 and M329 verify at their required tops.
   M326's known malformed checksum row is exactly the provenance defect
   repaired by M329 and is not a mathematical objection to M330.

2. In the sole fixed `k=7,H_2,(1,1)` cell,
   `N_A=2037915313150409615825963/288085426550809623412604928>0`,
   from exactly 590 positive-residual non-Touch A raw slots. The first has
   `e=(3,4)`, `f=(4,5)`, slot 1, empty owner support, and heads
   `{2,3,4}`.

3. That A atom has residual mass
   `1064930878419049375/91417600301718608805888`. With M323's fixed
   non-Touch B atom, its exact token mass is
   `65802548799959422226562500000/706358481579483924710894769596909369>0`;
   the total fixed-B/nonTouch-A mass is
   `119877371361788800930939000000000/2119075444738451774132684308790728107>0`.
   The B prefix has opposite-A ranks `18->19->18`, so its switched raw
   atom is absent.

4. Both endpoints are non-Touch. The positive-mass token is outside the
   OR-defined `Exc_pf`, while `S_pf` is undefined on it. M323 plus M330
   therefore proves an actual off-`Exc_pf` failure of frozen `S_pf` at
   exactly this finite scope.

5. No new cell, rank, surgery, compatible coboundary, Borel estimate, MPCF
   statement, or downstream inference was made.

The sole replay is byte-identical to M330's frozen JSON. M330 and every
predecessor package remain unchanged.
