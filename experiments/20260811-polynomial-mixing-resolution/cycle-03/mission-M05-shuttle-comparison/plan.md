# M05 plan: coupled color/internal shuttle comparison

## Exact target

Fix N>=3, even m>=4, and a feasible labeled weighted support-component
datum alpha. Use the project convention (pq)(x)=p(q(x)) and evaluate words
as t_1...t_m. Let K^alpha be the standard rejected-exit restriction of the
exact lazy {3,4,5} heat-bath chain.

Write the uniform macro-fiber as

    I_alpha x product_a X_a,

where I_alpha is the fixed-content component-color word and X_a is the set
of connected identity transposition factorizations on component C_a with
length k_a.

Define the full physical Hurwitz walk P_H^alpha, the adjacent color shuffle
Q_col, and independent connected-factorization Hurwitz walks P_a. Compare
P_H^alpha with an ideal convex product chain and then invoke the inherited
Dirichlet comparison from K^alpha to P_H^alpha.

## Proposed shuttle path

For consecutive internal factors of color a occupying physical positions
u<v, shuttle the factor at u right across the intervening disjoint colors,
apply the desired right or inverse Hurwitz move at v-1,v, and shuttle the new
first factor left to u. Use the fixed schedule

    R_u,...,R_{v-2}, R_{v-1}^{epsilon}, R_{v-2},...,R_u.

The path must preserve alpha, restore the original color word, and have
length below 2m.

## Congestion audit

For every occurrence of a physical directed edge on a shuttle path, record

    (component a, original positions u<v, orientation epsilon, stage s).

For fixed metadata the prefix is a fixed composition of bijective Hurwitz
maps. Inverting it from the edge tail should recover at most one source.
Count all metadata, repeated colors, central/shuttle collisions, and
duplicate generator outputs. Direct color flow is charged separately.

## Required calibration

Audit one-color and singleton fibers, k_a=2, rare colors, endpoints, m=4
with its whole-word heat bath retained, the S_3,m=4, S_4,m=4, and S_4,m=6
references, near-minimal doubled trees, and the N=5,m=24 color word
(ABBBBB)^4. The construction must not claim a length-two heat-bath
simulation or use a canonical normal-form hub.
