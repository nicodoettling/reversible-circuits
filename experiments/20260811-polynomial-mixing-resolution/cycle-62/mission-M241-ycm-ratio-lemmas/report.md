# M241 report: explicit YCM ratio and strip lemmas

Date: 2026-08-13 UTC.

## Verdict

**PROVED R1--R3 WITH EXPLICIT CONSTANTS; STRICT SCOPED PROGRESS ONLY.**

On their exact candidate domains:

- R1's GG2 bracket is at most `36`;
- R2's stronger absolute smooth aggregate is at most
  `34(x+1)/k`;
- R3's comparison and actual strip masses are at most
  `42sqrt(x)/R` and `28sqrt(x)/R`.

These estimates, combined only with the accepted coefficient and Borel
identities, give the explicit skeleton bounds

    |G_k(x)-2b_x|<=128(x+1)b_x/k,   1<=x<=k/4,
    G_k(x)<=70/[k sqrt(D-x)],       j<=x<=L-1.

This proves SG and GG2 as used in the interrupted M232 skeleton. It does not
prove YCM: GG1, the four coefficient-region bounds, prefix assembly, and
finite-rank handling were not audited by M241.

## Proof mechanism

The exact recurrence
`rho_n=b_(n-1)/b_n=e(1-1/n)^(n-2)` is decreasing and satisfies
`0<=log rho_n<=2/n`. Its indexed product yields a quantitative shifted
Borel ratio bound for every `r>=2x`. This directly proves R2.

On `x<s<2x`, the inequality `q_s<12b_s` and cancellation of the
`b_s` denominator in `a_s(x)` reduce R3 to
`sum_(t<=x)t b_t=O(sqrt(x))`.

For R1, monotonicity puts the worst bracket at `x=s=j`; a two-sided
Stirling envelope gives the uniform explicit constant. Positivity and the
weighted Borel convolution then yield GG2.

## Immutable gate

M226 and M229 passed their complete frozen checksum inventories before use.
Their checksum-file digests are respectively

    a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a
    6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688

M232 and M239 were used only as immutable candidate snapshots whose hashes
are recorded in `checkpoint.md`. No predecessor was edited.

## Diagnostics

Command:

    python3 ratio_strip_check.py

Python `3.12.3`; deterministic; seed null; standard library only. Exact
`Fraction` arithmetic and a rigorous rational enclosure of Euler's number
check 2,585 R1 tuples and 56 cases each for R2 and R3 over odd
`3<=k<=31`. All pass. This finite result is falsification evidence only.

## Scope

YCM, TCM, WBE, DE, J2, PCR, every downstream spectral-gap or mixing claim,
and both Terminals remain open. Request a fresh immutable audit of the exact
domains, product indexing, constants, and SG/GG2 sufficiency calculations.
