# M272 freeze manifest

Date: 2026-08-14 UTC.

## Verdict

```text
EXACT FULL D/q SIGNED ENDPOINT-COUPLING IDENTITY.
CHANNEL-ONE COLLISION O(1/k) AND CHANNEL-TWO TRIANGLE O(1/k) PROVED.
EXACT CHANNEL-TWO DISJOINT VECTOR ABEL REDUCTION.
CSBV, CEBV, CIBV, DOR, SET, PBV, AND FD REMAIN UNRESOLVED.
```

For odd `k>=3`, `n=3k`, the frozen result is limited to the balanced
first fixed cell of the auxiliary minimal-long-cycle factorization law and
M73's nonlazy cyclic rank-two kernel.

The strongest exact identity couples the complete merged exterior law to
the separate two-cycle law:

```text
eta(g)=sum_j alpha_j E_j[g(X_T)-g(Y_S)],

sum_K<w,T_(K,ell)>
 =1/n sum_j alpha_j E_j[E_ell(X_T)-E_ell(Y_S)].
```

The `D_u/q_u` flows telescope before any cost.  The affine collision
coefficient is narrowed to a proved complete channel-one bound, proved
channel-two triangle bound, and two literal signed disjoint vectors CSBV and
CEBV.  These are the remaining subcoefficients of CIBV.  The decorated
owner-ratio coefficient DOR remains separate and open.

## Frozen payload

- `plan.md`
- `checkpoint.md`
- `halfway_checkpoint.md`
- `adjacent_transport.md`
- `phase_incidence_lemma.md`
- `channel_two_collision_reduction.md`
- `phase_incidence_probe.py`
- `phase_incidence_results.json`
- `channel_two_collision_probe.py`
- `channel_two_collision_results.json`
- `report.md`
- `fresh_audit_request.md`
- this `freeze_manifest.md`

`SHA256SUMS` is generated after this manifest, inventories every payload
above, and excludes itself.

## Validation and scope firewall

- All required M91/M94, M261/M264, and M267 checksum inventories passed
  before use; no predecessor was edited.
- The two deterministic exact-rational checkers retain both channels,
  triangle/double kinds, phase categories, ordered factors, and all
  completion weights.
- Python syntax, JSON parsing, deterministic reruns, and mission
  `git diff --check` pass before freeze.
- The finite seam-only counterexample is not promoted to an asymptotic
  obstruction; the adjacent-norm data do not prove divergence.
- No SET, PBV, FD, SR/TPR, FCL1, direct-L1, H0, gap, mixing, or Terminal
  claim is included.

Fresh independent audit is required before coordinator promotion.
