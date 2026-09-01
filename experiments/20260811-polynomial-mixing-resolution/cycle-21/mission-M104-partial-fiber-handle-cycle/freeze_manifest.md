# M104 freeze manifest

Date: 2026-08-12 UTC  
Repository commit: `a7215b895249783b6315d444728aaadc95bed32e`

## Freeze boundary

Frozen as proved:

- At fixed realizable seam key `kappa=(j,p,Q_L,Q_R)`, the raw word fiber is the exact Cartesian product of its prefix and suffix factorization sets.
- The lifted conditional law is the raw product law tilted by `1/ell`, with Radon--Nikodym distortion at most `D=2d-1` in either direction.
- With `r_L(u)=j-b(uv)+1` and `r_R(v)=h(uv)-j`, one has `ell(uv)=r_L(u)+r_R(v)-1` and the exact product-mixture identity
  `1/ell = integral_0^1 z^(r_L(u)-1) z^(r_R(v)-1) dz`.
- Literal signed Hurwitz moves internal to one side preserve the seam key and admissibility; a nontrivial seam move never remains in the same fixed cell.
- The raw and lifted restricted gaps differ by at most the stated powers of `D`; the final audited candidate constants are
  `gap(P_kappa) >= Gamma_0(d)/(420 D^10)` and
  `gap(L_kappa) >= Gamma_0(d)/(420 D^13)` for `d>=3`.
- The generic projection decomposition gives the conditional implication
  `gamma_1(d) >= Gamma_0(d) beta(d)/(2940 D^13)` for `d>=3`.
- The explicit cell `kappa_e` contains the full-label, same-`d`, minimal genus-zero Hurwitz problem on one side. This is a same-size circular reduction, not an induction and not a spectral-gap proof.

The constants `420` and `2940` remain subject to a fresh independent referee audit. The two quantities `Gamma_0(d)` and `beta(d)` are unresolved. Therefore no inverse-polynomial lower bound for `gamma_1(d)`, no completion of M92, no bound for the full kernel, and no Terminal conclusion is claimed.

## Frozen dependency hashes

- M97 report: `73ab5bec4d5ba48bb1b4511099df056525fe1f6b6f1b6caa6f79b7964feb3c99`
- M97 freeze manifest: `6d0c28f8a4414175a3226b77fb1cff3217599f14ad707eaf5a7d3e3470babc4f`
- M101 report: `e129ea085bf10679056bee55186ec2c3382e4d192459adb90585a20a3b1635a3`
- M05 shuttle report: `d8ec2b835e5169b91977a33ac725680d206d62e9d7f6b944abbc203037d22bf4`
- M05 referee report: `d6a8be7e37dde11dd74bbc28dcdc7a7c4926913060273b48655bbf77f726fee9`

M92 and M95 were read as frozen contextual dependencies; M104 changes neither artifact.

## Frozen payload hashes

- `plan.md`: `58ad9784b4a539f1bf3b42ba6c52277ab8b85ec465c335e60343f84cafa86d74`
- `checkpoint.md`: `e5e17f4ea896ce7d5cd340590dea5801c3d86ece5e8b70ba11e68a7042af348c`
- `fixed_fiber_decomposition.md`: `f0d2138d269e4695b545379500bc64ea64ebb849d757d06b87e8fd5e899a7def`
- `fixed_seam_audit.py`: `38a04b6f4d03f820b94c631463235c69296dda816bb08a41a256273d26468a87`
- `results.json`: `184f00e909708a3ddac114eaebee54dd8f6c1b3a65710bbb2ba69c5d13c689e3`
- `report.md`: `a04c67103dd356d00b3c9ac267ba2eb255c69632d06707cb839ed8dd5ebb269b`

The hash of this manifest is recorded in `SHA256SUMS` and in the coordinator handoff.

## Exact audit

Command:

```text
PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M104-partial-fiber-handle-cycle/fixed_seam_audit.py --d 2 3 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M104-partial-fiber-handle-cycle/results.json
```

Environment: Python 3.12.3; no nonstandard dependencies; deterministic exhaustive run (`seed=null`). Runtime was 42.33237266540527 seconds. The finite audit is falsification evidence only. It reported zero product, component-factorization, incidence, internal-move, or side-dependence failures for `d<=4`; it does not prove an asymptotic statement.

## Cache and worktree audit

The audit was run with bytecode generation disabled. No `__pycache__` directory or `.pyc` file remains in the owned directory.

Shared worktree status at freeze contained:

```text
?? experiments/20260811-polynomial-mixing-resolution/
?? notes/
```

M104 edited only `experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M104-partial-fiber-handle-cycle/`. The other shared untracked content is outside this worker's ownership.
