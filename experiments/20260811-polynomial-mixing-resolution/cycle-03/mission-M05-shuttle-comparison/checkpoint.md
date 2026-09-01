# M05 halfway checkpoint

## Frozen ideal-chain normalization

Let q be the number of positive-weight components. Define

    P_H^alpha
      = (1/2)I
        + [1/(4(m-1))] sum_i (R_i+R_i^{-1}),

    Q_col
      = (1/2)I
        + [1/(2(m-1))] sum_i S_i,

and, for each component of weight k_a,

    P_a
      = (1/2)I
        + [1/(4(k_a-1))] sum_l (R_l+R_l^{-1}).

All coordinate chains are lifted to the product space, and

    P_* = [Q_col + sum_a P_a]/(q+1).

If gamma_a=gap(P_a) and delta=min(1,min_a gamma_a), product variance
decomposition and the audited color gap give

    gap(P_*) >= 2 delta/m^4.

## Shuttle construction

If consecutive internal a-factors occupy physical positions u<v and
d=v-u-1, use

    R_u,...,R_{v-2}, R_{v-1}^{epsilon}, R_{v-2},...,R_u.

The first d moves commute the left a-factor right through disjoint-support
colors. The central move performs the desired internal Hurwitz generator.
The final d moves commute the new first a-factor back. Thus the path has
length 2d+1<2m, stays inside alpha, restores the color word, and makes
exactly the requested internal update.

## Injective recovery and provisional congestion

For metadata (a,u,v,epsilon,s), the sequence of the first s physical
Hurwitz maps is fixed and bijective. A directed used-edge tail therefore
recovers at most one source by applying the inverse prefix. The internal
index is then the rank of u among the a-occurrences.

There are fewer than

    q * binom(m,2) * 2 * (2m) < m^4

metadata choices. Each labeled ideal internal flow is at most pi_alpha/8,
each path has length below 2m, and each used physical directed edge has
P_H^alpha capacity at least pi_alpha/[4(m-1)]. Hence internal congestion is
below m^6. Adding the direct color flow gives total congestion at most
2m^6.

## Remaining audit

Check singleton conventions, exact product-gap inequalities, all calibration
cases, the inherited K-to-Hurwitz coefficient, and write the final
standalone connected-Hurwitz gap.
