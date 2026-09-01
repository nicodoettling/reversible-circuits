# M292 report: fresh audit of M289 CEBV

Date: 2026-08-14 UTC.

## Verdict

**ACCEPT M289 AS FROZEN AT CEBV-ONLY SCOPE.**

Material objections: none.  Nonmaterial objections: none.

The audit independently reconstructs the ordered first-two-factor B/A laws,
raw masses `12a_L(s)` and `12a_F(s)`, literal subprobability normalizer,
two-seam and one-wrap phase maps, Lemma 1 with all endpoints and both tail
extensions, generalized component stabilization including `r=1,2`, the
untouched row, triangular cross term, and `k=3`.  Every analytic step needed
for

```text
||sum_(s<k/2) qhat_s(Phi_s^D-Psi_s^D)||_1=O(1/k)
```

survives.

## Integrity and independent check

M289's top digest is
`327176968d69eb447ff862354eb566ed00cfd2c56b2e77079231bcc077f93680`;
its exact nine-payload inventory and all twelve cited predecessor ledgers
pass.  The independent checker imports no M289/project code and exactly
recovers

```text
k=3: 148/135,
k=5: 1411115143/1382976000.
```

A post-reconstruction replay of M289's checker is byte-identical to its
frozen result.

## Exact stop

This report accepts CEBV only.  M276/M279's separate exact implication
`CSBV+CEBV => CIBV` is left to coordinator synthesis.  No CIBV, DOR, SET,
PBV, FD, FCL1, spectral-gap, polynomial-mixing, or Terminal A/B claim is
made here.
