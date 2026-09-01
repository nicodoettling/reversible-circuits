# M113 freeze manifest

Frozen: 2026-08-12 UTC.

Mission: M113 handle-cell projection gap.

Repository commit recorded by all scripts:
502a6f031c6d5a4bc0064ee5b370a4fa3914f993.

Status: partial theorem and named obstruction, not a terminal result.
The exact reduction beta(d)>=gap(A_d)/(2d-1)^3 is proved.  The standalone
LOCAL UNICYCLE INCIDENCE GAP remains unresolved.

Target: uniform connected-support identity transposition words of length 2d.

Convention: (pq)(x)=p(q(x)); factors multiply left-to-right.

## Frozen payload

| file | SHA-256 |
|---|---|
| plan.md | b1265ea52d96dd29cc0489ca9c108d925cf751ed34b33ea52b6bd51318c4f226 |
| checkpoint.md | 5383d24e6c66d355a8b2abf263fa6933f1fa574c2d3bda3bc2f07fca62bc2291 |
| projection_reduction.md | 65cbfa834da08509a5beccb3ec79a8e645e2804eaa7bb2f6607975c56dde04bb |
| projection_audit.py | 6f1ca459ae6bb749548e89a02ee11c51a484d35dc5b5765d8db017fbb8d6bee1 |
| results.json | 20b28269a70fce94612c8d85be5a9591cb8ad98c1077c1a8660149add9408a48 |
| forest_lift_audit.py | 6147f5995214ed601859a389fae401ba65bebdfe9d19780b784073a19b54fd23 |
| forest_lift.json | d2ed1a25ffb4bd7a2782239b74839d2197193d072949f514ad69f1250092a22a |
| lorentzian_forest_audit.py | 3028462686ba50db61d5da385f48abcc2d5a6511f0d764ade131f296dbcfed07 |
| lorentzian_forest.json | 2a5258f6d0538f6ac2ce0361268404214927108f9580fdd3eb98f6969141e11e |
| edge_obstruction.py | add1dca9d3333d2fdea9c666724796a496670ed1461591f66efe626411745d3b |
| edge_obstruction.json | 62b0c145ebfc883f7876a736b3e71fe6d2510d97d7022c91d541afad4a32a74e |
| report.md | 295c6d50b70117915cc99d9ebe6e1e88cbfab258a404db66a0b1543ea01cfe47 |

## Upstream dependencies

| artifact | SHA-256 |
|---|---|
| M97 report | 73ab5bec4d5ba48bb1b4511099df056525fe1f6b6f1b6caa6f79b7964feb3c99 |
| M97 freeze manifest | 6d0c28f8a4414175a3226b77fb1cff3217599f14ad707eaf5a7d3e3470babc4f |
| M101 report | e129ea085bf10679056bee55186ec2c3382e4d192459adb90585a20a3b1635a3 |
| M101 freeze manifest | 37e454eaca9d1e992e87109b9b0f6f731a57b53d7953e62e02f5f0ac29e0f661 |
| M104 report | a04c67103dd356d00b3c9ac267ba2eb255c69632d06707cb839ed8dd5ebb269b |
| M104 fixed-fiber proof | f0d2138d269e4695b545379500bc64ea64ebb849d757d06b87e8fd5e899a7def |
| M104 results | 184f00e909708a3ddac114eaebee54dd8f6c1b3a65710bbb2ba69c5d13c689e3 |
| M104 freeze manifest | f36a625702a7b93dbebabc3ded4edcfda326ba3c85dae244bb52ed92ab8412f9 |
| M110 report | 663023041d6e2a46c11c280615476835f58c5c97e75bc2ff0f46afd37c8d3519 |
| M110 independent results | 7fffbafed6df1e0bbbf13fcd566a78822e2b2ab745b0fc8faeaa33e783d9bcff |
| M110 freeze manifest | 9fd3074ef08f60a571aff1ab9c7d9bfb9da8ed0c168d917f239d40789122b68a |

## Validation

- projection_audit.py completed for d=2,3,4.
- forest_lift_audit.py completed for c=2,3,4.
- lorentzian_forest_audit.py completed for c=2,3,4.
- edge_obstruction.py completed for even d=6,8,10,12,16,20,30,40.
- All Python sources passed ast.parse.
- All JSON artifacts parsed.
- report.md contains exactly nine fields.
- No Python cache directory remained at freeze time.

SHA256SUMS hashes every payload file above and this manifest; it intentionally
does not hash itself.

