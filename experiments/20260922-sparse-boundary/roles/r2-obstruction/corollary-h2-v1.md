# H2-QC boundary obstruction — R2-O2.v1

Status: proved by author, nonauthor check pending. This is a separately
versioned corollary, suggested by the coordinator and checked by R2. It
does not modify the frozen H0 policy or R2-O1. Input H2-QC.v1 policy is
roles/r4-construction/proof-v1.md: admit precisely all feasible connected
components of size v<=L, with arbitrary genus, where

    L=max{1<=v<=N:3^v<=(N+m+2)^4}

is computed once at the top-level input. Let D be its word set.

**Claim.** For N=2^(8j),m=2^(6j), every integer j>=64,

    |D|/|Omega(N,m)| <=2^(-1-jm/2).

Thus any sampler supported on D has TV error at least1-2^(-1-jm/2).
In particular this applies to the proposed exact uniform H2-QC sampler.
The same obstruction applies to its hybrid union with genus0/1 components.

**Proof.** For any fixed integer cutoff J>=2, let A_J admit all components
with g<=1 OR v<=J. The finite numerator proof in R2-O1 uses no property of
K beyond b_K x<=1, where b_J=(J^3-J)/36 and x=k/N^2, k=m/2. Therefore
the same proof, with identical constants, gives

    |A_J|<=m!(N^2/k)^k exp(8k)

whenever3Nx<=1/2,x<=1,b_Jx<=1. This is a generalization of the bound's
explicit finite hypotheses, not an assertion that H0 silently changed.

On the exact subsequence, P<=2N and3^L>=2^L imply

    L<=4log_2P<=32j+4,
    b_L x<=(32j+4)^3/[72*2^(10j)]<1.

At j1 the final upper bound is46656/73728<1. Its consecutive ratio is
((32j+36)/(32j+4))^3/1024<8/1024<1, so it remains below1 for all
integer j>=1. The other numerator hypotheses were already verified in
R2-O1. Since D subset A_L, apply the same embedded-subgroup denominator
and exact j>=64 constants from R2-O1. This proves the claim.

For any output law Q supported on D, the event Omega\D has Q-mass zero
and target mass1-|D|/|Omega|, giving the stated TV lower bound directly.
No correctness or complexity assumption about the new decoder is needed
for this support obstruction. H2 need not contain H0, and the two are not
identified. It remains possible that a sampler admitting larger-support,
higher-genus components achieves the full benchmark; existence T0 is not
refuted.

Dependencies: R2-O1 finite numerator/denominator argument, uniform
factorial genus majorant, exact H2 policy definition. Boundaries m0,m2,N2
are unchanged and do not intersect the asymptotic claim. This proof uses
only the stated sequence j>=64 and does not extrapolate finite examples.
