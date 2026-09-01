# M304 Run Manifest

Date: 2026-08-14 UTC

- Mission: `M304-m301-fresh-referee`
- Owner: `/root/m302_m297_fresh_referee`
- Role: fresh immutable referee of frozen M301
- Convention: `(pq)(x)=p(q(x))`; chronological signed right-Hurwitz action
- M301 top digest:
  `ae7ca4a3089259ac59df8e15ea3ff8d957c01956d842454f2dd1dcf3a881adcd`
- Analytic scope: action covers, residual density, and MRAD formulation
- Finite scope: exact `d=3` only
- Author replay: `python3 -B mt2h_d3_diagnostic.py --output /tmp/m304_m301_rerun_results.json`
- Independent command: `python3 -B independent_d3_check.py`
- Independent checker: standard library only; imports/reads no project artifact
- Seed: null; deterministic
- Dependencies installed: none
- Network used: no
- Files edited outside this mission directory: none

