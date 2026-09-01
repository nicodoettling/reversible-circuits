# M168 final report: fixed-cell phase collapse and scalar closure

Date: 2026-08-13. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
VERDICT: STRICT EXACT PHASE-COLLAPSE REDUCTION.
FCL1: UNRESOLVED.
```

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
For `n=3k`, odd `k>=3`, this report concerns only M73's nonlazy cyclic
rank-two quotient kernel at the balanced sources
`A_k=(0,k,2k)`, `B_k=(0,1)(k,2k)` and M161's fixed separated cell
`t_y=(0,1)(y+1,y+2)`. It proves no direct-L1, all-edge, H0, gap, bridge,
identity-chain, mixing, or Terminal claim.

## 2. Strongest proved result

For an intermediate `s`, put `q=s^-1h`. Every polygon boundary edge that
can lower the rank of `q` is an actual adjacent residual-cycle edge. If
`g_i` counts such generic edges in residual component `i` and `a_i` counts
ambient-adjacent pairs among them, the complete lag sum counts

```text
g_i(g_i-1)-2a_i       ordered disjoint same-component pairs,
2g_i g_j              ordered cross-component pairs.
```

Their completion weights depend only on the residual sizes after isolating
two singleton tails. Proposition 1 of `phase_collapse_reduction.md` gives
the exact component-moment formula `(PC)`. Substitution in M161's accepted
raw convolution gives `(PCS)` for `sum_y z_k(y)`. Both source channels, all
triangle/double intermediates, and `IS/IN/X` target topologies are combined
before any absolute value. No quotient matrix or shell scan is used.

Because each physical fixed-cell orbit occurs twice in the colored `y`
list, the signed sum is exactly the physical cell-event contrast divided by
its constant orbit mass, as stated in `(CE)`.

## 3. Deterministic FCL1 reduction

For every real length-`N` sequence,

```text
sum_i|x_i|<=|sum_i x_i|+N sum_(i<N)|x_(i+1)-x_i|.
```

Applying this to `x_y=Z_k(y)=kz_k(y)`, `N=3k-3`, proves that FCL1 follows
from exactly the two named scalar estimates

```text
(PCS-bound) k|sum_y z_k(y)|=O(1),
(FD-bound)  k^2 sum_y|z_k(y+1)-z_k(y)|=O(1).
```

This avoids a positivity theorem. Alternatively, the exact negative-mass
identity `(NEG-id)` shows that `(PCS-bound)` plus a uniform bound on the
minority sign mass would suffice; universal one-sign would be stronger.

## 4. Probability, multiplicity, and cancellation accounting

- The target is the uniform minimal long-cycle factorization law, not the
  identity-word law or the lazy `{3,4,5}` heat-bath chain.
- Triangle and double intermediate lift multiplicities remain `3` and `2`.
- The target double lift factor cancels only against the identical factor in
  the constant target orbit mass.
- Every physical target orbit has two colored appearances; `(CE)` includes
  the required factor `1/2`.
- `IS`, `IN`, and `X`, both M91 source channels, and all lower-support terms
  remain inside the signed sum before absolute value.
- No schemawise L1 estimate or continuum collision deletion is used.

## 5. Dependencies and status labels

- **Accepted proved:** M73's raw/quotient rank-two kernel and schemas;
  M91's complete two-channel source contrast; M94/M100's orbit-aware raw
  convolution; M155/M159's fixed-cell motivation; M161/M166's constant
  target mass, literal lag/correlation formula, reflection, and FCL1
  normalization.
- **Proved here:** `(PC)`, `(PCS)`, `(CE)`, `(TV-close)`, `(NEG-id)`, and
  the sufficient scalar closure `(SC)`.
- **Exact finite only:** frozen exact reproduction at `k=3,5,7` and a
  targeted exact sign check at `k=9`.
- **Floating finite only:** signed phase sums at `k=9,11,13,15`.
- **Unresolved:** `(PCS-bound)`, `(FD-bound)`, the sign/negative-mass
  alternative, FCL1, every further cell, direct L1, all-edge/H0/gap and both
  Terminals.

## 6. Falsification and finite calibration

The standard-library checker exactly reproduces the sum of frozen M161's
individual scores at `k=3,5,7`. Exact/floating `k sum_y z_k(y)` for
`k=3,5,7,9,11,13,15` is approximately

```text
3.12033, 2.43231, 2.17959, 2.05295, 1.97715, 1.92673, 1.89079.
```

The corresponding physical-event values `n^2 Delta_k(mathcal C_k)` are

```text
2.66440, 1.51186, 1.19283, 1.04895, .96771, .91568, .87955.
```

A targeted exact M161 run at `k=9` gives `A_k(1,1)=0.7698574787` and all 24
scores positive. These are finite diagnostics only; no asymptotic scale or
sign claim is inferred.

## 7. Strongest self-attack and first unproved step

Phase collapse does not bound the resulting signed component-moment average.
The counts `g_i,a_i` are not determined by unordered residual cycle sizes,
and separate source-channel absolute values would lose the cancellation the
mission was required to preserve. Thus `(PCS-bound)` remains open.

Likewise M161's decreasing finite sequence-variation diagnostic proves no
uniform `(FD-bound)`. The factor `N` in `(TV-close)` forces the stronger
scale `k^2 V(z_k)=O(1)`; a generic variation bound at scale `kV(z_k)=O(1)`
does not close FCL1. Positivity through `k=9` does not establish universal
positivity or even a one-sign-change theorem.

The first standalone obligations are therefore the pair `(PCS-bound)` and
`(FD-bound)`, or `(PCS-bound)` plus the negative-mass alternative in
`(NEG-id)`.

## 8. Artifacts, command, reproducibility, and hygiene

Owned artifacts are `plan.md`, `checkpoint.md`, `halfway_checkpoint.md`,
`phase_collapse_reduction.md`, `signed_cell_sum_probe.py`,
`signed_cell_sum_results.json`, this report, and the freeze files.

The retained deterministic command was

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-38/mission-M168-fixed-cell-fcl1/signed_cell_sum_probe.py \
  --k 3 5 7 9 11 13 15 --exact-through 7 \
  --frozen-m161 experiments/20260811-polynomial-mixing-resolution/cycle-37/mission-M161-fixed-boundary-cell-score/fixed_cell_results.json \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-38/mission-M168-fixed-cell-fcl1/signed_cell_sum_results.json
```

Python `3.12.3`; standard library only; deterministic; `seed=null`. No
package, network, commit, push, predecessor, coordinator, manuscript, goal,
skill, or shared project file was changed. Generated cache is removed before
freeze. Final hashes are recorded in `SHA256SUMS` and `freeze_manifest.md`.

## 9. Final action

**KEEP AND FREEZE THE STRICT EXACT PHASE-COLLAPSE/SCALAR-CLOSURE REDUCTION;
SEND IT FOR FRESH INDEPENDENT AUDIT. FCL1 REMAINS UNRESOLVED.**

No inference from this one cell to direct L1, an all-edge theorem, H0, a
spectral gap, a bridge gap, the identity heat-bath chain, or Terminal is
valid.

