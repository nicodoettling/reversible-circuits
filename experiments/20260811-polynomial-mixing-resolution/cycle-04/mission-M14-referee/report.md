# M14 fresh referee report: universal pair-length-three bridge theorem

## 1. Claim, quantifiers, and convention

Permutations are maps on [N], composition is

    (pq)(x)=p(q(x)),

and the displayed transposition word t_1...t_6 has that ordered product.
Put M=binom(N,2). For endpoint pair u,v in A_N, set h=u^{-1}v and let
Omega_3(h) be the uniform fiber of six-transposition words with product h,
grouped as three ordered pairs.

Let H_1 and H_2 be the exact heat baths on positions 1,...,4 and 3,...,6,
respectively, and define

    B_3=(H_1+H_2)/2.

The frozen claim is:

For every N>=3 and every u,v with Q_N^3(u,v)>0, Omega_3(u^{-1}v) is
irreducible under B_3 and

    gap(B_3;u,v)>=M^{-16},
    Lambda_N(3;u,v)=2 gap(B_3;u,v)>=2M^{-16}.           (1.1)

A singleton fiber uses gap convention one.

Referee conclusion: the claim is correct. The finite computation is promoted
to a universal computer-assisted theorem only because the independent
finite-basis argument is valid.

## 2. Full audit

### 2.1 Composition, support, and multiplicities

The author source defines compose(p,q)=p after q and evaluates pair products
as compose(t_1,t_2), matching the frozen convention. If q is the product of
two transpositions, then q is exactly one of:

- the identity, with M ordered microfactorizations (t,t);
- a 3-cycle, with three ordered microfactorizations;
- a product of two disjoint transpositions, with two orderings.

Thus

    Sigma_N=supp(Q_N)
      ={identity, 3-cycles, double transpositions}

and the recorded multiplicities are exact. The independent N=3,4 enumerator
reproduces these values directly.

For a bridge from u to v, multiplication of the increments telescopes to
u^{-1}v. Left translation therefore identifies the endpoint-pair chain with
the e-to-h word fiber used by the code. Every six-transposition word has the
same unconditioned probability M^{-6}, so the conditional microfactor law is
uniform.

### 2.2 Microfactor-to-product-path quotient

Let A_i be the i-th ordered transposition pair and q_i=prod(A_i). Projection
to (q_1,q_2,q_3) preserves components in both directions.

First, an aligned four-factor update changes two adjacent q_i while retaining
their ordered product, so every micro edge projects to a product-path edge.

Conversely, any adjacent product-path replacement lifts from every
microstate: choose any ordered two-transposition realization of each new
increment and use their concatenation as the requested four-factor heat-bath
outcome.

Finally, all microstates over one fixed product path communicate. To replace
the ordered realization of one q_i, select an adjacent four-factor window,
retain the neighboring increment exactly, and use the desired realization of
q_i. Every site belongs to at least one aligned window at pair length three.

Hence microfactor labels and their multiplicities affect stationary weights,
but they create no additional connected components.

### 2.3 Exact incidence graph

A product state (a,b,c) satisfies abc=h, so b is forced by a,c:

    b=a^{-1} h c^{-1}.                                  (2.1)

Create a bipartite graph with left copy a of Sigma_N, right copy c of
Sigma_N, and incidence a--c precisely when the value in (2.1) belongs to
Sigma_N.

At fixed c, H_1 makes every feasible (a,b) a clique. At fixed a, H_2 makes
every feasible (b,c) a clique. Thus product states are incidences and their
heat-bath components are exactly the nonisolated incidence-graph components.

The further quotient from exact outer microfactor pairs to pair products is
also exact. All microfactor copies with product a have identical
neighborhoods. If active, any two such copies share a neighbor and are in the
same component; the same holds on the right. There is no ambient ordering or
multiplicity invariant hidden by this quotient.

The independent referee script enumerates the actual six-factor graph at
N=3,4, forming heat-bath cliques by fixed exact first or last transposition
pair. Its component counts agree with a separately implemented product
incidence quotient for every endpoint element, not only every cycle type.

### 2.4 Endpoint enumeration and code completeness

An endpoint of six transpositions is feasible exactly when its transposition
defect is even and at most six. Necessity follows from parity and minimal
transposition length. Sufficiency follows from a minimal factorization padded
by adjacent squares.

The author code enumerates every integer partition of N satisfying precisely
that condition. Simultaneous conjugation by any element of S_N intertwines
the transposition heat baths, so one ordinary S_N cycle-type representative
is sufficient. This also covers split A_N conjugacy classes: an odd
conjugator is still an automorphism of the all-transposition chain.

The source was read completely. For every endpoint it independently forms
Sigma_N from all M^2 ordered pairs, evaluates (2.1), uses union-find on the
bipartite quotient, retains the exact multiplicity product a_N(a)a_N(b)a_N(c),
and checks the class-weighted total M^6. Through N=6 it also constructs the
ordered outer-microfactor incidence graph and asserts equal component and
incidence counts.

The four frozen JSON files cover exactly N=3,...,12 and exactly

    2,3,4,6,8,12,15,17,18,19

feasible endpoint types. Every component count is one and every class-mass
identity is M^6.

The author report says representative products are asserted, while the author
source only constructs and emits them. This is a documentation discrepancy,
not a proof failure: the referee verifier independently evaluated all 104
emitted six-transposition representatives and every one equals the exact
cycle-type representative claimed.

Independent reruns give:

- N=3,...,6: all mathematical fields reproduce, including the ordered-micro
  checks and N=6 mass 15^6=11,390,625;
- N=12: every mathematical field reproduces exactly after ignoring only
  elapsed time and output-command text; all 19 endpoint types are connected
  and the mass is 66^6=82,653,950,016;
- an independent actual-state implementation at N=3,4 reproduces
  |Omega(3,4)|=27, |Omega(4,4)|=120, |Omega(4,6)|=3936.

No floating-point value enters the certificate.

### 2.5 Finite basis and ambient labels

Take any ambient-N six-transposition state w and let U be the union of labels
appearing in w. Then |U|<=12 and supp(h) is contained in U. Relabeling U
identifies w with a state in the exactly checked S_|U| fiber. Every path found
inside S_U embeds as a positive path in S_N; the larger ambient conditional
fiber changes probabilities but cannot delete those transitions.

If h is nonidentity, its defect is 2, 4, or 6. Fix once and for all a minimal
transposition factorization of h using only supp(h), then pad to length six
with adjacent squares using a transposition on supp(h). The resulting c_h
depends only on h and lies in every S_U containing an h-fiber state.
Connectivity for |U|<=12 therefore sends every ambient state to the same
c_h. The possible |U|=2 nonidentity case does not occur.

If h is identity and |U|>=3, the certificate connects w to (s,s)^3 for any
chosen transposition s in U. The |U|=2 fiber is a singleton. Supportwise
square canonicals are joined in the ambient group by

    (s,s,s,s,s,s)
      -> (r,r,r,r,s,s)
      -> (r,r,r,r,r,r),                                (2.2)

using first the left and then the right aligned window; both old and new
four-factor block products are identity.

This resolves the only plausible ambient-label mismatch and proves universal
irreducibility from the N<=12 certificate.

### 2.6 Spanning-tree Poincare estimate

Let V=|Omega_3(h)|. Trivially V<=M^6. A selected aligned window has scan
probability 1/2. Its conditional fiber has size F_{4,N}(g)<=M^4, so every
specified positive outcome has probability at least

    p_*=1/(2M^4).                                       (2.3)

Choose any spanning tree of the connected transition graph. For uniform pi,

    Var_pi(f)
      =(1/(2V^2)) sum_{x,y}(f(x)-f(y))^2
      <=((V-1)/2) sum_{e in tree}(nabla_e f)^2.         (2.4)

Indeed, every tree path has length at most V-1 and each tree edge is charged
by at most V^2 ordered pairs. Since B_3 is symmetric,

    E_{B_3}(f,f)
      >=(p_*/V) sum_{e in tree}(nabla_e f)^2.           (2.5)

Therefore, for V>=2,

    gap(B_3)
      >=2p_*/[V(V-1)]
      >=1/(M^4V^2)
      >=M^{-16}.                                       (2.6)

The local Hamiltonian is

    (I-H_1)+(I-H_2)=2(I-B_3),

so Lambda_N(3;u,v)=2gap(B_3;u,v). This proves (1.1). The spanning tree need
not be the canonical-state paths used qualitatively. At fixed pair length
three the whole fiber has polynomial size, so even the crude V^2 load is
polynomial and does not invoke a scalable common-hub claim.

## 3. Probability, runtime, path, and congestion accounting

- Window scan probability: 1/2.
- Specified selected-window outcome: 1/[2F_{4,N}(g)].
- Universal positive-transition floor: p_*=1/(2M^4).
- State count: V<=M^6.
- Tree path length: at most V-1<=M^6-1.
- Ordered-pair load per tree edge: at most V^2<=M^12.
- Resulting gap: at least M^-16.
- Hamiltonian constant: twice the B_3 gap.
- Exact H_4 sampling by full enumeration costs at most O(M^4) candidates.
- Author N=12 run: 50.416 seconds; referee rerun: 48.822 seconds.
- Independent N=3,4 actual-state audit: deterministic, approximately three
  wall-clock seconds including process startup.
- No random seed or stochastic conclusion is involved.

## 4. Dependencies with labels

- PROVED MATHEMATICALLY: microfactor quotient, incidence characterization,
  endpoint feasibility, conjugacy reduction, finite-basis theorem,
  identity-canonical glue, and spanning-tree Poincare constants.
- EXACT COMPUTER-ASSISTED: connectedness of every incidence certificate for
  every feasible endpoint at N=3,...,12.
- INDEPENDENTLY VERIFIED: actual-state versus quotient components at N=3,4;
  every JSON endpoint type, mass, component count, and all 104 representative
  products; fresh author-code reruns at N=3,...,6 and N=12.
- INHERITED BUT NOT USED: arbitrary-product Hurwitz classification, long
  bridge recursion, K>=B/12, and identity-only aligned connectivity.
- EMPIRICAL OR CONDITIONAL DEPENDENCIES: none.
- EXTERNAL LITERATURE DEPENDENCIES: none.

## 5. First unproved step

The frozen l=3 theorem has no unproved step. The next standalone bridge
proposition is:

For every N>=3 and every feasible endpoint h of defect at most eight, the
pair-length-four product-path graph on

    (q_1,q_2,q_3,q_4) in Sigma_N^4,
    q_1q_2q_3q_4=h,

is connected under adjacent same-product pair replacement.

The finite-basis lemma reduces this qualitative proposition to N<=16, but
the existing l=4 computation stops at N=7. Even completing l=4 would not
supply the uniform gap exponent needed for all l<=O(N log N).

## 6. Strongest self-attack

This remains a computer-assisted theorem. A correlated implementation error
in permutation arithmetic or endpoint enumeration is the strongest residual
risk. It is substantially reduced by the independent actual-state
implementation, complete class-mass identities, explicit certificate
evaluation, ordered-micro cross-check, and fresh boundary rerun.

The M^-16 bound is useful only because l=3 is fixed. Repeating the same
state-count proof at growing l gives an exponent proportional to l and does
not resolve the M10 base regime. Nor would failure of the auxiliary aligned
chain refute K, since K>=B/12 is a one-way lower comparison.

The author source's missing explicit representative-product assertion should
be corrected for documentation hygiene, but the independent verifier closes
that check for the frozen files and it is not a numbered objection to the
theorem.

## 7. Calibrations

- Odd original word length: empty and outside this paired bridge.
- m=0: singleton.
- N=2: only one transposition; every paired bridge is singleton.
- Original m=2,N>=3: excluded and not inferred.
- Pair length l=2: its sole aligned H_4 is a whole-word heat bath of gap one.
- S_3,m=4: exact identity count 27 reproduced.
- S_4,m=4: exact identity count 120 reproduced.
- S_4,m=6: exact identity count 3936 reproduced.
- Singleton l=3 endpoint fibers: gap convention one.
- Identity endpoint: handled by the explicit two-edge square-canonical glue.
- Nonidentity endpoints: every feasible defect 2,4,6 cycle type is included.
- Support union: at most twelve labels, with embedding into larger N checked.
- Ordered positions and all microfactor multiplicities are retained.
- Split A_N classes are covered by S_N conjugation.
- Whole-word H_4 and the distinct l=2 behavior are not discarded.
- No edge-parity surrogate or finite convergence claim is used.

## 8. Artifacts and commands

Referee artifacts are under

    experiments/20260811-polynomial-mixing-resolution/cycle-04/
      mission-M14-referee/

Files:

- plan.md
- checkpoint.md
- report.md
- independent_l3_audit.py
- independent_results.json
- verify_author_outputs.py
- certificate_verification.json
- author_rerun_N3_to_N6.json
- author_rerun_N12.json

Commands:

    python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-referee/independent_l3_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-referee/independent_results.json

    python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-referee/verify_author_outputs.py --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-referee/certificate_verification.json experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/results_N3_to_N6_l3.json experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/results_N7_to_N10_l3.json experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/results_N11_l3.json experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/results_N12_l3.json

    python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/l3_endpoint_quotient.py --N 3 --N 4 --N 5 --N 6 --verify-micro-through 6 --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-referee/author_rerun_N3_to_N6.json

    python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/l3_endpoint_quotient.py --N 12 --verify-micro-through 0 --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-referee/author_rerun_N12.json

All runs use Python 3.12.3, commit
502a6f031c6d5a4bc0064ee5b370a4fa3914f993, and seed null.

## 9. Verdict and numbered objections

ACCEPT

Numbered objections: none.
