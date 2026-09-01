# M113 final report: exact handle-cell projection reduction

Date: 2026-08-12 UTC.

## Field 1 — decision and claim status

Verdict: PROMOTE the exact reduction and the named comparison obstruction;
KEEP the polynomial handle-cell gap open.

PROVED:

- the exact projected stationary law and cut-refresh Gibbs flow;
- a comparison beta(d)>=gap(A_d)/(2d-1)^3 to an explicit local
  connected-unicycle incidence chain A_d;
- universal qualitative connectivity of A_d, including d=2;
- the fixed-p colored-forest family is the basis family of a first Higgs
  lift matroid;
- the natural exact Hurwitz-weighted Higgs basis polynomial is not
  Lorentzian at d=4;
- an infinite split family has exponentially small individual A_d edges but
  inverse-polynomial aggregate flow.

UNRESOLVED: gap(A_d)>=d^{-O(1)}, hence also the requested
beta(d)>=d^{-O(1)}.  No claim is made about gamma_1, the full heat-bath
chain, or a terminal project outcome.

## Field 2 — target, convention, and exact kernel

The target is the uniform law pi_d on connected-support identity
transposition words X_d of length 2d, d>=2.  Permutations compose as
(pq)(x)=p(q(x)); word factors multiply left-to-right.  With D=2d-1,

    P_d=I/2+[1/(4D)] sum_i(R_i+R_i^{-1})

is M104's half-lazy signed adjacent-Hurwitz kernel.  M97's
spectrum-preserving lift is

    tilde_pi(w,j)=1/(|X_d|ell(w)),
    L((w,j),(w',j'))=P_d(w,w')/ell(w'),

where J(w) is the set of central cuts and ell(w)=|J(w)|.  Projection cells
are kappa=(j,p,Q_L,Q_R), with p the prefix product and Q_L,Q_R the two
support partitions.  Beta(d) is the spectral gap of the exact
stationary-flow projection bar L.

## Field 3 — exact stationary law, flows, and comparison

For S_kappa=sum_{w incident to kappa}ell(w)^{-1},

    bar_pi(kappa)=S_kappa/|X_d|.                         (3.1)

The explicit holding half of P_d keeps w and refreshes j uniformly.  Doubling
that subkernel gives a Markov kernel G_d with

    G_d(kappa,lambda)
      =S_kappa^{-1}
       sum_{w incident to both kappa,lambda}ell(w)^{-2},
    Q_G(kappa,lambda)
      =|X_d|^{-1}
       sum_{w incident to both kappa,lambda}ell(w)^{-2}. (3.2)

This is exactly the Gibbs update K to W to K under the joint law
Pr(W=w,K=kappa(w,j))=1/(|X_d|ell(w)).  Physical signed seam moves add
nonnegative Dirichlet flow, so beta(d)>=gap(G_d)/2.

Let Z_inc=sum_kappa|C_kappa|=sum_w ell(w) and
rho(kappa)=|C_kappa|/Z_inc.  Define A_d by

    Q_A(kappa,lambda)
      =|C_kappa intersect C_lambda|/(2Z_inc)             (3.3)

when the cuts differ by one and are compatible, and hold otherwise.  It is
the exact sampler kappa to uniform w in C_kappa to a uniformly chosen
left/right adjacent central-cut shift.  Since 1<=ell<=D,

    D^{-1}<=bar_pi/rho<=D,
    Q_G>=2D^{-2}Q_A.

The variance comparison must use bar_pi<=D rho.  Consequently,

    gap(G_d)>=2D^{-3}gap(A_d),
    beta(d)>=D^{-3}gap(A_d).                            (3.4)

This corrects a stronger preliminary constant that used the measure
comparison in the wrong direction.  Compression's beta>=gamma_1 inequality
is circular here and was not counted as progress.

## Field 4 — combinatorial state space, local moves, and exact weights

A key is realizable exactly when Q_L,Q_R coarsen the cycle partition of p,
the bipartite block-incidence multigraph with one edge per p-cycle is
connected-unicyclic, and

    j=d+|Q_R|-|Q_L|.                                    (4.1)

Conversely, minimal connected block factorizations and side interleaving
construct a word for every such key.

Adjacent cells kappa=(j,p,Q_L,Q_R) and
lambda=(j+1,p',Q'_L,Q'_R) overlap exactly when

    t=p^{-1}p' is a transposition,
    Q'_L=join(Q_L,t),
    Q_R=join(Q'_R,t).                                   (4.2)

Then

    C_kappa intersect C_lambda=U_kappa x {t} x V_lambda,
    |C_kappa intersect C_lambda|=|U_kappa||V_lambda|.    (4.3)

The two cases are local left coagulation of two p-cycles/Q_L blocks, or
right fragmentation when t cuts a p-cycle.  There is no hidden-word count.
The convention-checked genus-zero Hurwitz formula yields

    |C_kappa|=j!(2d-j)!
      product_{B in Q_L union Q_R}|B|^{c_B-3}
      product_{p-cycle a}
        [|a|^{|a|}/(|a|-1)!]^2.                         (4.4)

The last product depends on p but not its incidence grouping.

PROVED qualitative connectivity: split singleton cycles off p until p=id;
then alternate a local join through a common opposite-color block and a
singleton split to reduce |Q_L|.  This reaches an extreme key with one left
block and one right two-label block.  Extreme keys communicate through a
single transposition on three labels.  At d=2 there is one key.  This is
only a reachability proof, not a canonical-hub flow argument.

## Field 5 — forest lift, named obstruction, and aggregate audit

At fixed p with c cycle atoms, let M be the direct sum of red and blue
graphic matroids on doubled K_c, and N the graphic matroid after forgetting
colors.  Every N-flat is an M-flat, so N is a quotient of M.  The first
Higgs lift

    r_H(X)=min(r_M(X),r_N(X)+1)

has rank-c bases exactly when each color is a forest and the uncolored union
is connected.  Contracting color components gives precisely the
connected-unicycle incidence keys.

The natural exact augmentation nevertheless fails the accepted
Lorentzian/SLC down-up route.  On the p=id,d=4 slice, a colored basis with r
red edges has exact coefficient

    w(B)=(2r)!(8-2r)!/
         product_{C in Q_L union Q_R}|C|.               (5.1)

For the derivative in red01 and red02, the Hessian principal submatrix on
red03, blue01, blue02, blue13 is

    [  0 180 180 180 ]
    [180   0   0  64 ]
    [180   0   0  48 ]
    [180  64  48   0 ],

whose exact determinant is 8,294,400.  Nonsingularity, zero trace, and the
positive determinant give inertia (2,2).  Interlacing therefore refutes the
required one-positive-eigenvalue signature.  Without the cut factorial tilt,
the analogous determinant is still positive, exactly 1/82944.  This
refutes only direct application to this natural exact polynomial, not all
augmentations or comparisons.

For even d>=6, the source

    sigma_d=(3,(01),{{0,1,2},{3},...,{d-1}},{[d]})

has adjacent targets lambda_A with p'=id, the same Q_L, and
Q'_R={A,A^c}, for 0 in A and 1 not in A.  If |A|=a,

    A_d(sigma_d,lambda_A)
      =a^{a-3}(d-a)^{d-a-3}/[8(2d-3)d^{d-4}].           (5.2)

At a=d/2 each edge is
2^{-d+3}/[(2d-3)d^2], but there are
binomial(d-2,d/2-1) such edges, giving aggregate probability at least

    2/[(d-1)(2d-3)d^2].                                 (5.3)

Thus pointwise minimum-edge comparison is refuted, while this family is not
an aggregate bottleneck.  A uniform aggregate bound over every key remains
unproved and unrefuted.

## Field 6 — exact d<=4 diagnostics

All state spaces and rational flows were built by exhaustive deterministic
enumeration; displayed gaps use symmetric numerical diagonalization.

| d | keys | components | gap(A_d) | gap(G_d) | beta(d) |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 | 1 | 1 |
| 3 | 9 | 1 | 0.1414353635 | 0.0896143806 | 0.1461033961 |
| 4 | 101 | 1 | 0.1254163084 | 0.0980244430 | 0.1288510552 |

The comparison (3.4) gives finite lower bounds 0.0011314829 at d=3 and
0.0003656452 at d=4.  The minimum singleton-split-or-reverse A_d probability
is 1/4 at d=3 and 1/3 at d=4, with no zero-rate key.  At d=2 the single key
has no off-diagonal flow and gap one by convention.  Formula (4.4),
overlap (4.3), row mass, reversibility, and physical-move target closure all
passed; floating residuals are recorded in results.json.

The exact rho marginals by j are

    d=3: (j=2,3,4) = (3,8,3)/14,
    d=4: (j=2,3,4,5,6) = (12,38,63,38,12)/163.

By cycle type they are

    d=3: 1^3 -> 3/7,  2,1 -> 4/7;
    d=4: 1^4 -> 627/3260,  2,1,1 -> 76/163,
         2,2 -> 96/815,  3,1 -> 729/3260.

These finite values falsify reducibility and normalization failures only;
they are not asymptotic evidence.

## Field 7 — dependencies and reproduction

Required local inputs were read before the analysis: HANDOFF.md, GOAL_SPEC.md,
the reversible-circuit-sampler skill and sampling-problem reference,
references/experiments.md, M97, M101, M104, and M110.  Frozen upstream hashes:

- M97 report: 73ab5bec4d5ba48bb1b4511099df056525fe1f6b6f1b6caa6f79b7964feb3c99
- M97 manifest: 6d0c28f8a4414175a3226b77fb1cff3217599f14ad707eaf5a7d3e3470babc4f
- M101 report: e129ea085bf10679056bee55186ec2c3382e4d192459adb90585a20a3b1635a3
- M104 report: a04c67103dd356d00b3c9ac267ba2eb255c69632d06707cb839ed8dd5ebb269b
- M104 proof: f0d2138d269e4695b545379500bc64ea64ebb849d757d06b87e8fd5e899a7def
- M104 results: 184f00e909708a3ddac114eaebee54dd8f6c1b3a65710bbb2ba69c5d13c689e3
- M104 manifest: f36a625702a7b93dbebabc3ded4edcfda326ba3c85dae244bb52ed92ab8412f9
- M110 report: 663023041d6e2a46c11c280615476835f58c5c97e75bc2ff0f46afd37c8d3519
- M110 independent results: 7fffbafed6df1e0bbbf13fcd566a78822e2ab745b0fc8faeaa33e783d9bcff
- M110 manifest: 9fd3074ef08f60a571aff1ab9c7d9bfb9da8ed0c168d917f239d40789122b68a

The simple-Hurwitz count (4.4) is the project's convention-checked
Goulden-Jackson/Vakil genus-zero formula; projection_audit.py independently
checks it on every d<=4 cell.

Reproduction commands, run from repository root:

    python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-23/mission-M113-handle-projection-gap/projection_audit.py --d 2 3 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-23/mission-M113-handle-projection-gap/results.json
    python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-23/mission-M113-handle-projection-gap/forest_lift_audit.py --c 2 3 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-23/mission-M113-handle-projection-gap/forest_lift.json
    python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-23/mission-M113-handle-projection-gap/lorentzian_forest_audit.py --c 2 3 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-23/mission-M113-handle-projection-gap/lorentzian_forest.json
    python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-23/mission-M113-handle-projection-gap/edge_obstruction.py --output experiments/20260811-polynomial-mixing-resolution/cycle-23/mission-M113-handle-projection-gap/edge_obstruction.json

Environment: commit 502a6f031c6d5a4bc0064ee5b370a4fa3914f993,
Python 3.12.3, NumPy 1.26.4, seed null.

## Field 8 — self-attack, boundaries, and hygiene

- d=2 was separated: one key, no off-diagonal edge, gap one.
- Zero-flow endpoints were not assumed away; realizability was characterized
  exactly, and d=3,4 enumeration checked every key.
- G_d and A_d are different chains with different stationary laws
  bar_pi and rho; the D-factor measure comparison is explicit.
- The full projected beta values include signed physical moves; the proof
  lower bound uses only the explicit holding/cut-refresh half.
- The connectivity proof uses an extreme family only for reachability and
  supplies no canonical-path congestion bound.
- The Higgs-lift theorem is exact at fixed p, but A_d changes p-cycle atoms.
  The determinant refutes only the natural exact SLC augmentation.
- Formula (5.3) is source-specific.  It cannot be promoted to a uniform
  local drift lemma.
- Exact d<=4 spectra are not used to infer asymptotics.
- No files outside the owned M113 directory were edited.  Generated bytecode
  and a superseded preliminary JSON were removed before freezing.

## Field 9 — standalone first open lemma and handoff

LOCAL UNICYCLE INCIDENCE GAP.  For d>=3, let A_d have the realizable
connected-unicyclic key space (4.1), stationary weights (4.4), and local
coagulation/fragmentation stationary flows (3.3), equivalently (4.2)--(4.3).
Prove

    gap(A_d)>=d^{-O(1)}.

By (3.4), this alone proves beta(d)>=d^{-O(1)} for M104's exact handle-cell
projection.  A useful strictly weaker precursor is the uniform aggregate
drift statement: from every key, the total A_d probability of all
singleton-cycle splits and their reverses is at least d^{-O(1)}.  The
finite audit and split family survive that statement, but it remains
unresolved.

The recommended next attack is a non-hub decomposition by cycle type and cut
level, using the exact local ratios (4.4), with the fixed-p Higgs bases only
as conditional fibers.  Do not invoke the refuted natural Lorentzian
polynomial or a pointwise minimum-edge bound.

