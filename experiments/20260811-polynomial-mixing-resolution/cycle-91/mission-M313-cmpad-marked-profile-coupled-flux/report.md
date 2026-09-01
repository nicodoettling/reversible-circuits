# M313 report: common marked-profile endpoint flux

Date: 2026-08-14 UTC.

## Verdict

**Strict analytic reduction; MPCF remains unresolved.**

M313 proves that M305's two marked Abel sums are exactly one common-quantile
endpoint divergence, makes zero-profile handling literal with fixed owner
slots, and constructs one explicit globally antisymmetrized profile flux.
The Borel-scaled net-edge lemma MPCF would imply CMPAD.  No all-rank bound on
that net edge table is proved.

## Exact construction

The common-uniform split coupling is

```text
pi_(s,t)=Leb((Q_(s-1),Q_s] intersection (P_(t-1),P_t]),
```

with marginals `q,p`, support `s<=t`, and crossing mass `-D_u`.  Therefore

```text
sum_(s,t)pi_(s,t)(F_t-G_s)
 =sum_u D_u(F_u-F_(u+1))+sum_s q_s(F_s-G_s).
```

For H/A, three owner slots are retained; for C, six ordered owner-pair slots
are retained.  Mismatched or zero responses are mapped to profile zero, so
every extended conditional law has the same fixed mass.  Both live channels
are combined before applying the canonical common-part/residual-product
coupling.  Raw lifts and state-level `1/3` triangle and `1/4` combined-double
averages retain all `T/S/N` kinds, phases, seams, and actual incidences.

After summing every quantile cell, the coupling is antisymmetrized into one
net profile-edge flux `J`.  With the controlling factor
`c_X=r_X(alpha_1+alpha_2)`, its divergence is exactly the zero-slot extension
of `mu^X`; deleting profile zero recovers M305's response-relevant measure.
The elementary inequality

```text
||div J||_TV<=2||J||_edge
```

proves that the three predeclared Borel-scaled MPCF edge bounds imply CMPAD.

## Sole finite guard

The only computation used `k=13`, row `H_2`.  It checks the exact split
marginals and divergence equality.  The fixed flux survives:

```text
k||J||_edge/(2b_2)          3.3053774998628103
k||mu_nonzero||_TV/(2b_2)   2.3951607793712415
```

This is finite-only.  It neither proves an absolute constant nor supplies an
asymptotic obstruction.  No other coupling, rank, or row was searched.

## Exact status

```text
common-quantile endpoint identity                  proved exact
zero-slot fixed-mass extension                     proved exact
global net-flux divergence = extended mu           proved exact
MPCF => CMPAD                                      proved exact implication
k=13 H2 fixed-flux survival                        exact finite only
MPCF / CMPAD / CBPV / SOCL                         unresolved
BODT/DOR/PBV/FD/FCL1/gap/mixing/Terminals          unresolved
```

The first unproved step is one standalone lemma: bound the already-combined
global net edge table in the three MPCF Borel scales.  Estimating either Abel
sum, channel, source, type, or incidence separately is not licensed.

