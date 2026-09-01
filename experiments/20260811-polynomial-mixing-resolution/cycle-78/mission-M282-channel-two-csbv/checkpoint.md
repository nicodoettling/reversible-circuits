# M282 checkpoint

Status: exact coefficient reduction and analytic ACBV/CSBV proof obtained;
fresh audit required.

Claim status: **CSBV proved, subject to fresh immutable audit**.

The immutable M272/M276/M279 and relevant M192/M195, M217/M222, M248/M249
inventories all pass. The Abel vector has been collapsed exactly to
`sum_s (p_hat_s-q_hat_s)Phi_s^D`; its ordered support-pair coefficients and
the literal two-seam phase embedding are now explicit in
`csbv_coefficient_reduction.md`.

The proof writes `c=A+M`. The first-edge coefficient has endpoint-inclusive
half-BV `O(1/k)`. For the disjoint kernel, subtracting the same Borel profile
from every paired row costs only `O(1/R)` in BV; the exact signed identity
`sum W_s=-sum q_s(a_F/a_L-1)=O(k^-2)` cancels the common profile before any
norm. Thus `TV(M)=O(1/k)`, ACBV holds, and the exact phase embedding proves
CSBV. The raw paired rows themselves do not have `O(1/R)` variation.

The single exact formula-only checker reproduces M272's independent CSBV
norms at `k=3,5,7` and checks additional ranks through `31`. This is finite
falsification only. No CEBV or downstream obligation is attempted.
