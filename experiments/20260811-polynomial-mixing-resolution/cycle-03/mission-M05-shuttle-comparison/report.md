# M05 final report: coupled color/internal shuttle comparison

## 1. Exact claim with all quantifiers and conventions

Permutations are maps on [N], multiplication is (pq)(x)=p(q(x)), and a word
is evaluated as t_1...t_m. Fix N>=3, even m>=4, and a feasible labeled
weighted support-component datum

    alpha=((C_a,k_a): a in A),   sum_a k_a=m.

Only positive-weight, nontrivial components are indexed by A; fixed isolated
labels create no coordinate. Put q=|A|, M=binom(N,2), and B=|R_m|. Let
K^alpha be the standard rejected-exit restriction of the exact lazy
{3,4,5} heat-bath chain to the macro-fiber Omega_alpha.

For every a, let X_a be the connected-support identity transposition words
of length k_a on C_a. Define the lazy symmetric connected-factorization
Hurwitz chain

    P_a
      = (1/2)I
        + [1/(4(k_a-1))]
            sum_{ell=1}^{k_a-1}(R_ell+R_ell^{-1})

on X_a. A singleton X_a has gap convention one. Write gamma_a=gap(P_a) and

    delta=min(1,min_a gamma_a).

Define the full physical macro Hurwitz walk

    P_H^alpha
      = (1/2)I
        + [1/(4(m-1))]
            sum_{i=1}^{m-1}(R_i+R_i^{-1}).

The Hurwitz maps are

    R_i(p,q)=(q,qpq),
    R_i^{-1}(p,q)=(pqp,p).

Theorem, proved here. If Omega_alpha is non-singleton, then

    gap(P_H^alpha) >= delta/m^10,                         (1.1)

and consequently

    gap(K^alpha)
      >= [(m-1)/(2B(m-2)M^2 m^10)] delta
      >= [2/(3N^4 m^10)] delta.                          (1.2)

For singleton Omega_alpha, both displayed lower bounds remain valid under
the gap convention one. Thus a universal inverse-polynomial gap for the
connected-factorization chains P_a implies a universal inverse-polynomial
gap for every full macro-fiber restriction K^alpha. No exact-color
restriction is used.

## 2. Full proof

### 2.1 Product coordinates and the three chains

Let I_alpha be the set of color words of length m in which color a occurs
k_a times. Scanning a color word from left to right and taking successive
factors from each internal word gives the exact bijection

    Psi: I_alpha x product_a X_a -> Omega_alpha.          (2.1)

Factors from different support components have disjoint supports and commute.
The uniform law pi_alpha is therefore the product of the uniform laws on
I_alpha and the X_a.

On I_alpha define the half-lazy adjacent multiset-transposition chain

    Q_col
      = (1/2)I
        + [1/(2(m-1))] sum_{i=1}^{m-1} S_i,              (2.2)

where equal adjacent colors give a self-loop. Lift Q_col and every P_a to
the full product space and define the ideal chain

    P_*
      = [Q_col + sum_a P_a]/(q+1).                       (2.3)

This is a reversible Markov chain for pi_alpha. The equal coefficients are
deliberately conservative; q<=m/2 because every positive component weight is
even and at least two.

The audited adjacent-interchange theorem gives, for q>=2,

    gamma_col=gap(Q_col)
      = [1-cos(pi/m)]/(m-1)
      >= 2/m^3.                                         (2.4)

For q=1, I_alpha is a singleton and gamma_col is set to one, which also
satisfies (2.4).

For independent product coordinates, conditional variance decomposition
gives

    gap(P_*)
      >= [1/(q+1)] min(gamma_col,min_a gamma_a).          (2.5)

Indeed, condition on all coordinates except one, apply that coordinate's
Poincare inequality, and sum; the Dirichlet form of P_* is 1/(q+1) times
the sum of the coordinate Dirichlet forms. Since q+1<=m, delta<=1, and
gamma_col>=2/m^3,

    gap(P_*) >= 2 delta/m^4.                             (2.6)

If the entire product space is a singleton, it is handled separately and no
variance inequality is needed.

### 2.2 Physical interpretation of Hurwitz generators

Suppose adjacent physical factors have different colors. Their supports are
disjoint, so they commute. Both Hurwitz orientations then give the same
simple swap:

    R_i(p,c)=(c,p)=R_i^{-1}(p,c).                        (2.7)

This changes only the color word and preserves every internal subsequence.

If adjacent factors have the same color a, they are consecutive in the
within-a subsequence. A physical R_i or R_i^{-1} acts exactly as the
corresponding internal Hurwitz generator on X_a and leaves the color word
unchanged.

Thus P_H^alpha contains every physically available adjacent color swap and
every internal move whose two factors happen already to be physically
adjacent. The next construction simulates every other internal move while
allowing the color word to change temporarily.

### 2.3 Shuttle path

Fix a product state x=(sigma,z). Fix a component a, an internal index ell,
and an orientation epsilon in {+,-}. Let the ell-th and (ell+1)-st occurrences
of a in sigma occupy physical positions u<v. Write their actual factors as
p and r, and put d=v-u-1. By consecutiveness, none of the d intervening
factors has color a, so every one has support disjoint from C_a.

Use the following fixed sequence of physical generators:

    R_u,R_{u+1},...,R_{v-2},
    R_{v-1}^{epsilon},
    R_{v-2},R_{v-3},...,R_u.                            (2.8)

When d=0, the sequence consists only of its central move. The first d right
moves commute p right through the intervening factors. Immediately before
the central step, p and r are adjacent in their original internal order.
The central step produces

    (p,r) -> (r,rpr)             if epsilon=+,
    (p,r) -> (prp,p)             if epsilon=-.           (2.9)

In either case, shuttle the new first factor left through the same disjoint
factors using the final d right moves. The original color word and the
physical values and order of every intervening factor are restored. The
within-a subsequence has undergone exactly the requested internal generator.

Every step is a Hurwitz move and hence remains in Omega_alpha. The path
length is

    L(u,v)=2(v-u-1)+1 <=2m-3 <2m.                       (2.10)

The construction uses no normal form, special state, or length-two heat-bath
replacement.

### 2.4 Congestion: injective source recovery

It is useful to decompose every ideal internal transition into its labeled
generator flow. For source x, component a, internal index ell, and orientation
epsilon, the stationary reference flow is

    pi_alpha(x)/[4(q+1)(k_a-1)].                        (2.11)

Self-loop generator instances contribute zero Dirichlet energy and need no
path.

Fix a directed physical transition e=(w,w') used by a shuttle path. Charge
each occurrence using the coarse metadata

    mu=(a,u,v,epsilon,s),                               (2.12)

where u,v are the original physical positions and s is the path stage at
which e is traversed. For fixed mu, the list of physical generator maps
before stage s is fixed by (2.8). Every Hurwitz generator is a bijection.
Consequently the edge tail w uniquely determines a possible source x by
applying the inverse prefix. The recovered source either has consecutive
a-occurrences at u,v and generates the charged path, or it does not. In
particular, at most one source is charged for fixed metadata.

No internal index is missing from the metadata: after recovering x, ell is
the rank of position u among the a-occurrences. Repeated intervening colors
cause no ambiguity. Central and shuttle stages are distinguished by s.
If right and inverse generators have the same output, epsilon still
distinguishes and counts both labeled reference flows.

There are at most

    q * binom(m,2) * 2 * (2m-3) < m^4                  (2.13)

possible metadata values, using q<=m/2. Since q>=1 and k_a>=2, (2.11) is
at most pi_alpha(x)/8. Each path has length below 2m. Every used directed
physical edge has P_H^alpha transition probability at least
1/[4(m-1)], because at least its selected oriented generator produces the
edge. Uniformity of pi_alpha therefore gives internal comparison congestion

    A_internal
      < [m^4 (pi_alpha/8)(2m)]
          /[pi_alpha/(4(m-1))]
      = m^5(m-1)
      < m^6.                                            (2.14)

This calculation counts path occurrences: stage s remains in the metadata
even if one path were to visit the same transition more than once.

### 2.5 Direct color flow and comparison

For an unequal adjacent-color pair, Q_col assigns off-diagonal probability
1/[2(m-1)]. After the mixture in (2.3), its stationary flow is

    pi_alpha/[2(q+1)(m-1)].                             (2.15)

By (2.7), the two physical Hurwitz orientations aggregate to
P_H^alpha probability 1/[2(m-1)] for the same transition. Route this
reference edge directly. Its congestion contribution is at most 1/(q+1).
Equal-color S_i proposals are self-loops.

Adding direct color load to (2.14), including possible collisions with shuttle
edges, gives the deliberately loose universal bound

    A <= m^6+1 <=2m^6.                                  (2.16)

The canonical-path comparison theorem now yields

    E_{P_*}(f,f) <=2m^6 E_{P_H^alpha}(f,f),

and hence, by (2.6),

    gap(P_H^alpha)
      >= gap(P_*)/(2m^6)
      >= delta/m^10.                                   (2.17)

This proves (1.1).

### 2.6 Transfer to the exact heat-bath restriction

The inherited, fully normalized padded-Hurwitz comparison states

    E_{K^alpha}(f,f)
      >= [(m-1)/(2B(m-2)M^2)]
           E_{P_H^alpha}(f,f).                         (2.18)

It uses actual H_3 outcomes, retains K's outer laziness and block/window scan
rates, and applies to the standard rejected-exit restriction. Combining
(2.17) and (2.18) proves the first inequality of (1.2).

Finally B<=3, (m-1)/(m-2)>=1, and M<=N^2/2, so

    (m-1)/[2B(m-2)M^2] >=2/(3N^4).                     (2.19)

This proves the universal form in (1.2).

## 3. Probability, runtime, path length, and congestion accounting

- Physical Hurwitz proposal per position and orientation:
  1/[4(m-1)].
- Aggregated physical swap of unequal colors: 1/[2(m-1)].
- Ideal internal labeled proposal after mixture:
  1/[4(q+1)(k_a-1)].
- Ideal adjacent-color transition after mixture:
  1/[2(q+1)(m-1)].
- Shuttle length: 2(v-u-1)+1<=2m-3.
- Recovery metadata count: below m^4.
- Internal comparison congestion: below m^6.
- Total comparison congestion including direct color flow: at most 2m^6.
- K-to-Hurwitz Dirichlet factor:
  (m-1)/[2B(m-2)M^2].
- Constructing a shuttle path requires one scan of the color word and O(m)
  transposition-Hurwitz operations; this is polynomial in N and m.
- An exact K step also has polynomial cost. Brute-force exact block sampling
  enumerates at most M^(r-1)<=M^4 prefixes for fixed r<=5, although the
  project's direct r=4 and r=5 samplers are faster.

No randomized slot choice is needed because the deterministic shuttle has an
injective polynomial-metadata recovery map rather than a shared hub.

## 4. Dependencies

- Proved here: ideal-chain definition and stationarity; product Poincare
  bound; exact physical shuttle; path length; injective source recovery;
  repeated-color and orientation accounting; comparison congestion; final
  gap transfer.
- Previously proved project input: the macro-fiber product bijection and
  uniform product law.
- Previously proved and audited project input: the color chain gap
  [1-cos(pi/m)]/(m-1), obtained from the adjacent interchange process.
- Previously proved and audited project input: equation (2.18), the exact
  K^alpha-to-full-Hurwitz Dirichlet comparison with all normalizations.
- Cited and convention-checked project input: Ben-Itzhak--Teicher Theorem 3.4
  makes every connected X_a a Hurwitz orbit, so every non-singleton P_a is
  irreducible and gamma_a>0.
- Empirical dependencies: none.

## 5. First unproved step, as a standalone proposition

Uniform connected-Hurwitz gap proposition. There exist universal constants
c>0 and C<infinity such that for every v>=2, every even
k>=2(v-1), and every labeled v-set C, the chain

    P_H^{C,k}
      = (1/2)I
        + [1/(4(k-1))]
            sum_{ell=1}^{k-1}(R_ell+R_ell^{-1})

on connected-support length-k identity transposition factorizations satisfies

    gap(P_H^{C,k}) >= c(vk)^(-C).                       (5.1)

Proposition (5.1), together with (1.2), closes the restricted macro-fiber
Poincare obligation. It does not by itself prove the macro projection or
global mean-lift bounds in regimes where those remain open.

## 6. Strongest self-attack

The theorem is a one-way sufficient-route comparison. A superpolynomially
slow connected Hurwitz chain would invalidate this route but would not imply
that K^alpha, much less global K, is slow: H_4 and H_5 may cross a Hurwitz
bottleneck that P_a cannot.

The proof uses uniformity and the exact product structure of a fixed
all-transposition macro-fiber. It does not automatically transfer to a
restricted gate library or to a nonuniform bridge law.

The m^6 congestion estimate is intentionally crude. Its validity does not
depend on typical color spacing: even the largest separation is charged.
The essential injectivity statement is source recovery under fixed
(a,u,v,epsilon,s); omitting s would indeed allow stage collisions.

## 7. Calibration suite

- Odd m: Omega(N,m) is empty; no claim is made.
- m=0: singleton, outside the displayed denominators.
- N=2 and even m: the global and macro state spaces are singleton.
- m=2,N>=3: excluded; the K-to-Hurwitz H_3 comparison is unavailable.
- S_3,m=4: every macro has one color. The shuttle length is one for each
  internal generator, and the comparison reduces to the connected Hurwitz
  coordinate. The 27 words and four global Hurwitz components are consistent.
- S_4,m=4: a two-disjoint-edge macro has two singleton internal coordinates
  and only the color shuffle; one-color macros use direct internal moves.
  The whole-word H_4 term remains in K and is merely unused in the lower
  comparison.
- S_4,m=6: unbalanced contents and repeated intervening colors are covered
  with no minimum-frequency loss beyond q<=m/2.
- k_a=2: feasibility forces a two-label component and X_a is singleton;
  gamma_a is set to one.
- One color: I_alpha is singleton. Consecutive internal factors are already
  physically adjacent, so every shuttle has d=0.
- Endpoints: u=1 or v=m cause no exceptional generator; all indices in (2.8)
  remain in 1,...,m-1.
- Near-minimal doubled trees: the comparison assumes no square or surplus.
  Their possible slowness is isolated exactly in gamma_a.
- N=5,m=24 with color word (ABBBBB)^4: consecutive A positions are distance
  six, so each A-Hurwitz update uses an eleven-edge shuttle. This leaves the
  exact-color subfiber temporarily and returns, directly bypassing the
  identity-restriction obstruction from M04.
- Known length-two simulation failure: no arbitrary same-product pair is
  resampled. Only a Hurwitz generator is performed after external
  commutation padding, so there is no contradiction.
- No canonical paired or doubled-tree hub is visited.

## 8. Artifacts and reproduction commands

Owned artifacts:

    experiments/20260811-polynomial-mixing-resolution/cycle-03/
      mission-M05-shuttle-comparison/plan.md
      mission-M05-shuttle-comparison/checkpoint.md
      mission-M05-shuttle-comparison/report.md

No computation or random seed was used. Reproduce the result by checking
the generator sequence (2.8), inversion argument (2.12)-(2.14), product
Poincare bound (2.5)-(2.6), and inherited comparison (2.18).

## 9. Verdict

PROVED

This verdict is scoped to the polynomial comparison (1.1)-(1.2). The global
terminal goal remains open at the connected-Hurwitz gap and the separately
tracked macro projection/global decomposition obligations.
