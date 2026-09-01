# M239 report: interrupted-M232 YCM salvage

Date: 2026-08-14 UTC.

## Verdict

**PROMOTE YCM.** For every odd `k>=3` and
`2<=ell<=(3k-1)/2`, the exact M226/M229 one-run coefficients satisfy

    |sum_(y=2)^ell c^Y_(k,y)| <=7000 sqrt(ell)/k.

This is an analytic all-rank theorem, not an inference from finite data.

M232 is explicitly recorded as **interrupted before freeze**. Its plan and
checkpoint were hashed as immutable inputs and were not edited. M239 found
that M232's skeleton had the correct architecture but did not quantify its
SG/GG2 steps. M241 supplied and froze those missing scalar lemmas; M243
independently accepted M241. M239 then proved GG1 and completed every
coefficient and prefix range.

## Strongest proved steps

Using `D=2k-1`, `j=(k-1)/2`, and `L=(3k-1)/2`:

    |G_k(x)-2b_x| <=128(x+1)b_x/k,  1<=x<=k/4,
    G_k(x) <=172b_x,                1<=x<=j,
    G_k(x) <=70/[k sqrt(D-x)],      j<=x<=L-1.

These imply the four coefficient envelopes

    |c_(k,y)| <=3000/[k sqrt(y)],       2<=y<=j,
    |c_(k,k-m)| <=176/[k sqrt(m)],      1<=m<=j,
    |c_(k,k)| <=70k^(-3/2),
    |c_(k,k+z)| <=242/[k sqrt(z)],      1<=z<=j.

Elementary square-root summation gives the sharper displayed prefix constant
`6906`, rounded to the theorem constant `7000`. The same proof covers
`k=3,5,7`; no finite enumeration is needed for boundary ranks.

## Immutable gates

- M226 checksum-file digest:
  `a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a`.
- M229 checksum-file digest:
  `6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688`.
- M241 checksum-file digest:
  `07918bbf968c93f34cbd252f938b1e6e21566ba2907836872592bb744ef53936`.
- M243 checksum-file digest:
  `99e30270a3852d53ecbdf70222f5a6490b6d12d01a4720e18745e3e30351d59b`.
- Interrupted M232 plan SHA-256:
  `42530e2f07a16d2a6c0049ab1dab35075efacb3589d748a70a5e321353386b4a`.
- Interrupted M232 checkpoint SHA-256:
  `f71c2697c53d8d48b8ad71369ef5e4e84341d45106fe8e129725351bf5656450`.

## Falsification check

Command from repository root:

    python3 experiments/20260811-polynomial-mixing-resolution/cycle-61/mission-M239-m232-salvage-freeze/ycm_formula_check.py

Environment: source commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`,
Python `3.12.3`, standard library only, deterministic, seed null.

The checker imports no predecessor code or data and directly evaluates the
closed formulas at odd `3<=k<=21`. All SG/GG1/GG2, coefficient-envelope,
normalization, and YCM checks pass. The largest observed scaled YCM prefix is
about `0.519`. These finite values are falsification evidence only.

## Scope

The target here is the exact scalar YCM coefficient prefix from M226/M229.
TCM is not used or re-proved. This report makes no WBE, DE, J2, PCR,
spectral-gap, mixing-time, or Terminal claim.

## Independent-audit request

Audit the frozen proof from the definitions, especially GG1's three positive
sources, the small-`y` A expansion, all seam domains, and the four prefix
ranges. Re-run the checker only as secondary falsification evidence.

