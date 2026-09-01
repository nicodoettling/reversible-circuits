# M108 halfway checkpoint

Date: 2026-08-12
Status: core direct reduction proved; universal PAIR-GAP not proved.

## Target and exact kernels

I fixed the target as the uniform law on the feasible arbitrary-endpoint bridge

    Omega_(2l)(h) = {t in T_N^(2l): t_1...t_(2l)=h},

with N at least 3, l at least 2, h in A_N, and composition
(pq)(x)=p(q(x)). The auxiliary chain is exactly

    J = (1/2)I + 1/[2(2l-1)] sum_(k=1)^(2l-1) H_(k,2).

After grouping consecutive raw factors into l microcoordinates, B is the
nonlazy uniform scan of the l-1 aligned H4 blocks. C is the nonlazy complete
scan over all unordered pairs of microcoordinates, with each update the exact
conditional expectation given all other raw microcoordinates.

## Proved local input

For every feasible arbitrary four-letter endpoint g, the internal nonlazy
three-scan H2 chain L on Omega_4(g) is connected and

    gap(L) >= delta_4 = 2/(3 M^7),  M=binom(N,2).

Connectivity uses the accepted Douvropoulos--Lewis arbitrary-product Hurwitz
classification and square-tree macro construction. The canonical target is
used only at this fixed four-letter scale. With V at most M^3 and every chosen
positive tree transition at least 1/(3M), a uniform spanning-tree Poincare
estimate gives the stated bound. Singleton fibers have gap one.

## Proved direct reduction

Conditioning outside an aligned raw block gives the exact feasible endpoint

    g = p^(-1) h s^(-1),

where p and s are the fixed prefix and suffix products. Conditional Poincare,
the fact that each raw H2 boundary occurs in at most two aligned blocks, and
the explicit one-half laziness yield

    E_J >= [3 delta_4(l-1)]/[4(2l-1)] E_B
        >= 1/(6M^7) E_B.

Combining the accepted M16 braided comparison E_B >= E_C/(2l^2) gives

    E_J >= [(l-1)/(4M^7 l^2(2l-1))] E_C
        >= E_C/(12M^7 l^2),

and hence gap(J) >= gap(C)/(12M^7 l^2). The denominator 12 is conservative;
the preceding coefficient is the sharp one delivered by this proof.

## Critical scope correction

The old M27 PRODUCT-INCREMENT BASE CORRELATION premise mu_l(h) <= A/l is
REFUTED by accepted M67, which proves an Omega(l^(-1/2)) long-cycle witness.
It is not the open theorem. M70/M72 nevertheless prove polynomial control on
the nonzero cyclic closure of that witness. The sharp accepted long-cycle
subfrontier is the cyclic-invariant H0 sector, reduced through M73/M80,
M83/M88, M91/M93, M94/M100, and M102/M105 to the endpoint-sharing signed
two-step interface and its balanced BA2, direct-L1, BD, and matched-finite-part
subproblems. M102/M105 establish a necessary collision/triangle counterterm
class, not the exact complete matching topology.

The remaining universal hypothesis is instead:

    gap(C_(l,h)) >= c (Nl)^(-C)

uniformly for all N at least 3, l at least 2, and feasible h in A_N. This
would imply PAIR-GAP by the new theorem. It remains open for arbitrary
endpoints and growing base windows. The long-cycle H0 problem is only a
necessary special-family subcase.

## Fresh checks and self-attack

The no-import script exact_matrix_audit.py rebuilt all matrices directly.
The rerun covered every feasible four-letter endpoint in S3 and S4, plus
S3 at l=3 and S4 at l=2 for the global comparisons. All required PSD margins
were at floating rounding scale. Actual local minimum gaps were 1/3 in S3
and 0.10414475595051942 in S4, far above the crude theorem constants.

Boundary audit: l=2 makes B and C the whole-fiber heat bath; empty fibers get
no gap; even raw length forces h even; N=2 is singleton; m=0 is singleton;
m=2 is outside the stated theorem but its whole-pair heat bath has gap one;
odd identity bridges are empty. The direct comparison is one-way and proves
neither the universal C gap nor either Terminal.

The new J comparison is quantitatively redundant for Terminal A because the
accepted direct K-to-B comparison and M16 B-to-C comparison already transfer
a universal C gap with the stronger loss 1/(24l^2). Its value is the requested
explicit reduction for the auxiliary PAIR-GAP chain J.
