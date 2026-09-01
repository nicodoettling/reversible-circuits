# M193 halfway checkpoint

Date: 2026-08-13 UTC.
Status: analytic trace aggregate and exterior normalization closed; freeze pending.

- Every cited frozen dependency ledger passed; no predecessor was edited.
- Retained observations are `a=0,...,d-1`: exactly `d` terms. The branch
  contribution is `eta sum_a B_(d,a)`. The factor `pi_a=1/(d+1)` is already
  inside `G_(d,a)`; there is no extra observation or survival factor.
- Exact beta-moment averaging proves `(1/d) sum_a Sbar_(B,d,a)<=1` for all
  `B,d>=1`, although an individual envelope can exceed one. For `B>=2`, use
  `H0,H1<=1`, `y>=1/3`, and `b<=3/8`. The average increases in `b`; its
  unconstrained maximum in `q` occurs at
  `q*=y(d^2+11d+22)/[(d+2)(d+3)(4y+3)]`, then decreases in `y`. The worst
  slack is coefficient-positive after `d=1+e`, with coefficients
  `4829,131535,1351327,6721029,16784028,18788964,5726736`.
- `B=1` is separate. Deleting inactive coordinates lowers the nominal
  envelope; its exact slack numerator is
  `51529d^4+779710d^3+4228095d^2+9411050d+7219256>0`.
- Hence `sum_a B_(d,a)<=(3/4)d`. For `n>=1`, including `r=n`,
  `sum_r (r+1)eta^(3)_(n,r)<=36/125`, so the sector is at most `27/125`.
- At `n=0`, only `d=1,a=0` occurs and `eta=9/16`. The exact matrix norm is
  `(25+sqrt(415))/70<2/3`, and the single history envelope is at most one;
  hence the boundary is at most `3/8`. This bound is deliberately loose.
- Scope remains only fresh actual-history `h=3`. Next: freeze proof, exact
  checker, report, manifest, hashes, and request a fresh immutable audit.
