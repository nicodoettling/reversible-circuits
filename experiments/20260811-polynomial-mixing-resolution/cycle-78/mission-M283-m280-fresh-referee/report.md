# M283 fresh immutable referee report on M280

Date: 2026-08-14 UTC.

## Verdict

```text
ACCEPT M280'S STRICT EXACT OWNER-CORRELATION REDUCTION.
FATAL OBJECTIONS: ZERO.
MAJOR OBJECTIONS: ZERO.
MINOR OBJECTIONS: ZERO.

CP/OCI, OS+, MS, FCL1, GAP, MIXING, AND TERMINALS REMAIN OPEN.
```

The accepted statement concerns only the first separated fixed cell of the
auxiliary uniform minimal long-cycle factorization law under M73's nonlazy
cyclic rank-two quotient kernel, for odd `k>=3`, `n=3k`, with
`(pq)(x)=p(q(x))`.  It is not a result about the global identity-word law or
the lazy exact `{3,4,5}` heat-bath chain.

## 1. Immutable source gate

M280's checksum-file digest is exactly

```text
60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9.
```

Its exact inventory contains ten payloads: `plan.md`, `checkpoint.md`,
`halfway_checkpoint.md`, `channel_positivity_reduction.md`,
`exact_cp_k11.py`, `exact_cp_k11.json`, `report.md`, `run_manifest.md`,
`fresh_audit_request.md`, and `freeze_manifest.md`.  Every payload passes;
`SHA256SUMS` excludes itself.

All entries in the required M161/M166, M168/M171, M174/M178, M266/M268,
and M274/M277 inventories pass.  Their ten checksum-file digests exactly
match M280's checkpoint; the full table is recorded in
`halfway_checkpoint.md`.  No predecessor was modified.

## 2. Independently reconstructed exact formula

For a supported product `s`, let the three residual owners have sizes
`d_a`, generic-edge indicators `chi_a`, and rooted-tree ratios

```text
kappa_aa=tau(d_a-2)/tau(d_a),
kappa_ab=tau(d_a-1)tau(d_b-1)/[tau(d_a)tau(d_b)]  (a!=b).
```

Completion-count cancellation gives exactly

```text
F_ell(s)=sum_(a,b)kappa_ab sum_r chi_a(r)chi_b(r+ell),

CP_j(k,y)=Lambda_n/[(n-3)(n-4)] * eta_j(F_ell),

Lambda_n=(n-2)(1-2/n)^(-(n-3)),
ell=y+1 in {2,...,n-2}.
```

The target double lift two cancels its identical factor in the constant cell
mass; source triangle/double lifts remain in the normalized `H` laws.

Independent substitution into those laws confirms both direct raw formulas.
Channel one has the explicit fair mixture of `C_-` and `C_+`.  Channel two's
full two-cycle ordered law `N_F` already chooses its first equal-rank
component fairly, so no extra `1/2` is permitted.  Conditioning on the
smaller first exterior split and summing by parts proves M280's complete
Borel–Abel formula with all `D_u` and `q_u` normalizations.

The source product kind `T/D`, target `IS/IN/X` partition, every cyclic
phase, both endpoints, and both channels remain inside the signed response.
Symmetry of `kappa` gives the statewise identity
`F_ell=F_(n-ell)`, hence channelwise reflection.

## 3. Collision/decorated form and logical hierarchy

Writing `I_ell` for support-head collisions and
`Q_ell=sum_(a,b)(e^2 kappa_ab-1)C_ab(ell)`, the pointwise owner-free count
gives

```text
e^2 eta_j(F_ell)=2eta_j(T)+eta_j(I_ell)+eta_j(Q_ell).
```

The exact conditional kind transfers are

```text
eta_1(T)=0,
eta_2(T)=theta_k=6(k-1)/[k(2k-3)(2k-1)]>0.
```

Therefore M280's first unresolved inequalities are precisely

```text
(OCI_1) eta_1(I_ell)+eta_1(Q_ell)>=0,
(OCI_2) 2theta_k+eta_2(I_ell)+eta_2(Q_ell)>=0.
```

Neither is proved.  Collision and decoration must remain together.

With positive source masses,

```text
CP => OS+ => MS => FCL1 given accepted PCS.
```

Only the last arrow uses M266/M268's proved PCS input, via the exact
positive/negative-mass identity.  M280 states this hierarchy at the correct
strength and makes no downstream inference.

## 4. Independent exact checks

The standard-library checker `cleanroom_cp_audit.py` imports no M280 code
and newly enumerates only `k=3`.  It verifies exact source/channel/split
normalization; the direct and Abel formulas at both channels and all six
lags; reconstruction from all six `T/D × IS/IN/X` pieces; channelwise
reflection/endpoints; `eta_1(T)=0`, `eta_2(T)=4/15`; and the collision affine
identity.  All twelve finite CP values are positive, which is finite-only.

The checker then verifies, without re-enumerating `k=11`, that M280's frozen
JSON has digest
`d08c8b0d9b2abe61e26752033d91438e0e9c912397c087734cc9b4fe10a10f93`.
All 60 exact scores reconstruct from their six pieces, reflection and
endpoints hold, both channel minima are tied at `y=9,22`, and the reported
phase total is reproduced.  This checks the frozen artifact, not the
universal inequality.

## 5. Numbered objections

1. **Fatal objections: none.**
2. **Major objections: none.**
3. **Minor objections: none.**
4. **Mandatory scope firewall:** finite positivity at `k=3` and frozen
   `k=11` is not an all-rank sign proof.  CP and OCI remain unresolved; no
   later-cell, direct-L1/H0, spectral-gap, mixing, or Terminal conclusion is
   licensed.

## 6. Final status ledger

```text
M280 and ten required source inventories                verified immutable
owner-correlation CP normalization                      proved exact
direct raw and Borel–Abel equivalence                   proved exact
channel-two fair-component convention                   proved exact
T/D, IS/IN/X, reflection, endpoint retention            proved exact
collision/decorated OCI_1 and OCI_2 reformulation       proved exact
CP => OS+ => MS => FCL1 given PCS                       proved implication
k=3 positivity                                          exact finite only
frozen k=11 positivity/artifact integrity               exact finite only
CP/OCI, OS+, MS, FCL1                                   unresolved
gap, mixing, Terminal                                   no inference
```

Final action: **accept and freeze M280's strict exact reduction with zero
substantive objections; continue only from OCI/CP (or the weaker
cross-channel minority-mass target).**
