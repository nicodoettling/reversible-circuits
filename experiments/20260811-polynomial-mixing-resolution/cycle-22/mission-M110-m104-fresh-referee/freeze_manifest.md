# M110 freeze manifest

Date: 2026-08-12 UTC
Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## Freeze boundary

Fresh-referee verdict: **ACCEPT**, with zero material numbered objections.

Frozen as independently accepted:

- the fixed `(j,p,Q_L,Q_R)` raw cell is an exact Cartesian product with the
  displayed forced component lengths and factor count;
- `r_L` and `r_R` have the stated side dependence, and the `1/ell` integral
  product-mixture identity is exact;
- internal moves preserve a fixed cell, while every nontrivial seam move
  leaves it;
- the lifted/raw density, edge-flow, variance, and `D^3` lower gap comparison
  are correct;
- retaining exactly two side-color identity slots gives the valid conservative
  constants `420D^10` and `420D^13`;
- the PSD stationary-flow projection and direct variance calculation give
  `gap(L)>=alpha beta/7` and conditional denominator `2940D^13`;
- `kappa_e` is exactly the same-`d` full-label minimal genus-zero coordinate,
  with raw restriction `[(D-2)/D]P_0,d+[2/D]I`; this is the decisive
  same-size circularity obstruction, not an induction.

Explicitly not frozen as solved: an inverse-polynomial bound for
`Gamma_0(d)`, `beta(d)`, or `gamma_1(d)`; worst-source marked hitting; the
full lazy `{3,4,5}` heat-bath gap or mixing time; Terminal A or Terminal B.

## Audited M104 hashes

- M104 report: `a04c67103dd356d00b3c9ac267ba2eb255c69632d06707cb839ed8dd5ebb269b`
- M104 proof note: `f0d2138d269e4695b545379500bc64ea64ebb849d757d06b87e8fd5e899a7def`
- M104 results: `184f00e909708a3ddac114eaebee54dd8f6c1b3a65710bbb2ba69c5d13c689e3`
- M104 manifest: `f36a625702a7b93dbebabc3ded4edcfda326ba3c85dae244bb52ed92ab8412f9`

`sha256sum -c SHA256SUMS` passed all seven entries in the frozen M104
directory before the content audit.

## Audited dependency hashes

- M05 shuttle report: `d8ec2b835e5169b91977a33ac725680d206d62e9d7f6b944abbc203037d22bf4`
- M05 referee report: `d6a8be7e37dde11dd74bbc28dcdc7a7c4926913060273b48655bbf77f726fee9`
- M92 contextual report: `21662f10c53582e6fbf2fe18cc405ba7d92497948a76e7138d5a46f5a266678f`
- M95 contextual referee: `feeb86aa8fcd18cf0af9342928adb7c4780beaff25fc453f3416d66794bfe237`
- M97 report: `73ab5bec4d5ba48bb1b4511099df056525fe1f6b6f1b6caa6f79b7964feb3c99`
- M97 manifest: `6d0c28f8a4414175a3226b77fb1cff3217599f14ad707eaf5a7d3e3470babc4f`
- M101 report: `e129ea085bf10679056bee55186ec2c3382e4d192459adb90585a20a3b1635a3`

## Frozen M110 payload hashes

- `plan.md`: `8852ddfb0f66995c492ca0dd36e12860ee73f83fbcc90ac8ed0f83cda1f4242a`
- `checkpoint.md`: `7cd6ec37b5aaae5f55860b82d2a88dcc6adc839cbf797b0254e799e0161ba9df`
- `independent_audit.py`: `18831d83989bce9f4afc227c5e168dca2f0451a443194b8ebca34ce1452cbd12`
- `independent_results.json`: `7fffbafed6df1e0bbbf13fcd566a78822e2b2ab745b0fc8faeaa33e783d9bcff`
- `report.md`: `663023041d6e2a46c11c280615476835f58c5c97e75bc2ff0f46afd37c8d3519`

The hash of this manifest is recorded in `SHA256SUMS` and sent to the
coordinator.

## Exact audit

Command:

```text
PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-22/mission-M110-m104-fresh-referee/independent_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-22/mission-M110-m104-fresh-referee/independent_results.json
```

Environment: Python 3.12.3; standard library only; deterministic
(`seed=null`).  Runtime was `3.975182056427002` seconds.  The checker
exhausted the complete `d=2,3` spaces and the `d=4` circular cell, with zero
failures.  This finite check is falsification evidence only.

## Cache and worktree audit

Bytecode generation was disabled.  No `__pycache__` directory or `.pyc` file
remains in the owned directory.  Shared worktree status at freeze was:

```text
?? experiments/20260811-polynomial-mixing-resolution/
?? notes/
```

M110 edited only
`experiments/20260811-polynomial-mixing-resolution/cycle-22/mission-M110-m104-fresh-referee/`.
Other untracked content belongs to concurrent workers or the coordinator.
