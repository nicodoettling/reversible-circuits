# bridge-decorrelation-bootstrap

- Created UTC: 2026-10-20T07:33:34.386119+00:00
- Objective: Find a static conditional-decorrelation assumption that bootstraps small-complexity local mixing to all endpoints and lengths
- Target distribution: Uniform fixed-length transposition words with prescribed endpoint in S_N
- Parameters: N=3,4,5 with m=4,...,12; N=6 with m=4,...,8; all
  feasible endpoint conjugacy types. Split a=floor(m/3), b=m-2a, a.
- Kernel: K_A=I/2+H/4+R/4 with uniform linear adjacent slots and signed
  Hurwitz moves; R refreshes equal pairs to a uniform square. Rightmost-first
  products. Target remains uniform on the prescribed-product fiber.
- Claim: a uniform bound rho(first third,last third)<=1-delta under every
  conditioned bridge, together with a small-length base gap, implies a
  polynomial gap by recursively overlapping two intervals. Delta is a
  universal positive constant, not an unspecified inverse polynomial.
- Commands: `python3 -B experiments/20261020-073334-bridge-decorrelation-bootstrap/check.py`.
- Raw data: results.jsonl, including input/source hashes and Python version.
- Numerics: exact integer bridge counts; two fixed seeds 20261020,20261021
  for singular-value power iteration. Those estimates are empirical lower
  approximations, not certified upper bounds. Exact rational LDL certificates
  at N<=4 check rho<99/100. Enumeration validates the joint count formula
  on identity S3,m4 and S4,m4,m6. No production sampler is changed.
- Expected failure modes: endpoint blindness mistaken for conditional tail
  decorrelation; polynomial per-level loss compounded into quasipolynomial
  time; normalization by m paid at every recursive level; finite tests
  mistaken for a uniform theorem; sparse exceptional fibers omitted.
- Interpretation: keep a falsifiable static hypothesis and prove the
  conditional implication; do not assert the hypothesis has been proved.
- Next changes: proof, report, ledger and provisional map integration;
  preserve prior research and archived overlap results.
