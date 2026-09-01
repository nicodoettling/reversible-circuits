# M243 report: fresh immutable referee of M241

Date: 2026-08-14 UTC.

## Verdict

**ACCEPT**, with no material objection.

Frozen M241 proves, uniformly on its exact stated domains,

    R1: H_(k,x,s)<=36,
    R2: smooth absolute aggregate <=34(x+1)/k,
    R3: comparison strip <=42sqrt(x)/R,
        actual strip <=28sqrt(x)/R.

The accepted coefficient interface and only these estimates yield exactly

    |G_k(x)-2b_x|<=128(x+1)b_x/k,  1<=x<=k/4,
    G_k(x)<=70/[k sqrt(D-x)],       j<=x<=(3k-3)/2.

This accepts `SG=128` and `GG2=70`; it does not accept or claim `YCM`.

## Immutable gate

M241's complete frozen inventory passes before and after inspection.  Its
checksum-file digest is

    07918bbf968c93f34cbd252f938b1e6e21566ba2907836872592bb744ef53936.

The accepted M226/M229 inventories also pass, with checksum-file digests

    a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a
    6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688

respectively.  M229's corrected `G_k` domain was used throughout.

## Independent audit

The ratio identity
`rho_n=e(1-1/n)^(n-2)` is decreasing, and its product from
`r-x+1` through `r` has no missing endpoint, including `r=2,x=1`.
The resulting explicit shifted-ratio bound proves R2.  The R3 actual mass
cancels `b_s` before summation; the comparison and actual tails then reduce
to elementary `s^(-1/2)` sums.  Stirling bounds and monotonicity put R1
below `27`, leaving slack in the advertised `36`.

For SG, the independently checked constants are `104` for shifted
fragmentation, `2` for the no-shift baseline, and `22` for the survivor;
they sum to `128`.  For GG2, positivity and Borel convolution give `54`
for the long parent and the sole endpoint survivor gives `16`, totaling
`70`.

The `k=3` SG domain is empty; `x=1` has an empty strict strip; the GG2
proof covers `k=3`, `x=j`, `x=L-1`, and empty long sums.

## Diagnostics

Command:

    python3 boundary_check.py

Python `3.12.3`; deterministic; seed null; standard library only; imports no
predecessor code or data.  Certified rational arithmetic checks all stated
quantities for odd `3<=k<=35`: 3,706 R1 tuples, 72 SG cases, and 323 GG2
cases.  All pass.  This is finite falsification evidence only.

## Numbered objections and scope

1. Material objections: none.
2. Nonmaterial: M241's pointwise R2 line is correct after rewriting it as
   `[(r-x-1)(Q-1)-(x+1)]/R`; displaying this identity would make the
   triangle step more transparent.
3. Nonmaterial: the intermediate R3 comparison constant `36` implicitly
   uses `2sqrt(2)<3`; the advertised constant `42` has ample slack.

`YCM`, `WBE`, `DE`, `J2`, `PCR`, every spectral-gap or mixing claim, and
both Terminals remain open.
