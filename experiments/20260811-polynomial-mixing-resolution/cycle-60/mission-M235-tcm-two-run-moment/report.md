# M235 report: signed two-run coefficient moment

Date: 2026-08-13 UTC.

## Verdict

**PROMOTE TCM AS PROVED, SUBJECT TO FRESH INDEPENDENT AUDIT.**

For every odd k at least 3 and every integer cutoff
2 <= ell <= (3k-1)/2, the exact literal signed two-run coefficient prefix
of accepted M226/M229 obeys

    |sum_(y=2)^ell c^T_(k,y)| <=160 sqrt(ell)/k.

This closes only TCM.  YCM remains open, so no WBE, DE, conditional J2,
downstream response, gap, mixing, or Terminal follows.

## Exact reconstruction

The B raw law is written with both parent orientations r=s,D-s, every cyclic
first start, every internal middle child, and every placement.  If t=r-d is
the retained source length, its complementary two-run face has exact size

    t+k 1{large B seam retained}+1{small B seam retained}.

This retains simultaneous seam hits, same/cross kinds, and collision
multiplicity.  Averaging a fixed retained set over the cyclic start yields
the large-seam exclusion factor (D-t)/D.

The A law splits exactly into marked-parent and untouched-cycle cases:

    T_A^mark =
     sum_s q_s sum_(r in {s,k-s}) sum_(2<=t<=min(ell,r-1))
      (t-1)K_R(r,t)(k-t)/k,

    T_A^unt =
     sum_s q_s(s/k) sum_(1<=c<=ell-k-s)cK_R(k,c).

No channel-two kind or seam is dropped.

## Proof

Uniform Stirling bounds, the rooted-tree convolution, and
sum_(t<=L)t b_t<=sqrt(L) give separate positive estimates

    T_B(k,ell)<=84 sqrt(ell)/k,
    T_A(k,ell)<=61 sqrt(ell)/k.

The difficult B regime is the long parent with t>r/2.  Writing d=r-t gives,
only in that parametrization, D-t=s+d.  This seam-exclusion gain makes the
high-t contribution O(k^-1/2), and that regime exists only for ell
proportional to k.  Triangle inequality proves the displayed constant 160.

This does not contradict M226's exact refutation of the fixed-placement
bound 4min(ell,a).  M235 averages over cyclic starts and then uses exact
Borel and first-split weights; it makes no constant pointwise count claim.

## Exact diagnostics

tcm_exact_check.py is standard-library only and imports no predecessor code
or data.  At k=3,5,7 it:

- reconstructs every literal ordered disjoint pair by permutation
  composition;
- independently evaluates the B two-seam and A marked/untouched formulas;
- matches both sides coefficient-by-coefficient, including all sizes;
- checks the B placement inequality at every finite tuple and cutoff.

All checks pass.  The finite calculations calibrate formulas and can
falsify them; they are not used in the universal proof.

## Dependencies and next action

All frozen inventories in M192/M195, M199/M207, M211/M215, M217/M222, and
M226/M229 passed before use.  Freeze M235 and request a fresh referee focused
on (3.3)--(3.6), the A untouched coefficient in (5.3), all convolution
ranges, and the explicit constant bookkeeping.

