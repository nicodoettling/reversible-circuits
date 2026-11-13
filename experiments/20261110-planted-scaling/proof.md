# A low-order obstruction for growing plants in quadratic-length bridges

Status: **proved by the argument below, using the checked classical spectral
input in source-audit.md; not independently proof-reviewed**. Finite checks
are separate validation, not the proof of the asymptotic claim.

## Model and the proposed assumption

N is the permutation degree, not the number of wires. Let q=binom(N,2), and
Z_j=|Omega(N,j)| for all transpositions of S_N. Products act rightmost first.
Let U_m be global uniform on ordered labeled length-m identity words. The
planted law P_(m,k) chooses a fresh uniform hidden k-subset I of positions and
then draws U_m conditioned on the selected ordered subsequence being identity.
There is one noiseless word, no key reuse or oracle. Both m and k are even.

For simplicity take even N in the two quadratic-host schedules below; odd N
can instead use even-rounded lengths. A precise proposed assumption would be:
for every adversary running in time poly(N,m), the distinguishing advantage
between U_m and P_(m,k) is negligible in N. Examples are

    m=N^2, k=2 ceil((log_2 N)^c/2), fixed c>0;
    m=N^2, k=N;
    m=N,   k=2 ceil((log_2 N)^c/2), fixed c>0, k<m.

The first two versions of this negligible-in-N assumption are **refuted** by
the following attacks. The third is **unresolved here**. This statement does
not cover Toffoli libraries, connected-only bridge laws, or a different
planting mechanism. It makes no claim about recovering the hidden I.

## 1. Preserve relative accuracy when conditioning on the plant

Write p_j(g) for the j-step pure-transposition walk. For any fixed s positions,
the selected tuple a has probability

    q^(-s) p_(m-s)((product a)^(-1)) / p_m(id).                  (1)

This follows by stably moving those gates to the left with Hurwitz moves,
preserving their values and order, and counting completions. The explicit
bijection is rederived in the preceding planted-subsequence experiment.

Define the parity-correct relative pointwise error

    delta_j = max_(sign(g)=(-1)^j) |p_j(g)/(2/N!) - 1|.

It is nonincreasing with j: applying a uniform transposition averages relative
densities and maps the uniform measure on one parity class to the other.
Let delta=delta_(m-k-2)<1, requiring m>=k+2. For any union S of the planting
positions and two inspected positions, |S|<=k+2. Equation (1) has density
relative to iid uniform gates between

    (1-delta)/(1+delta) and (1+delta)/(1-delta).

After conditioning on E_I, its normalization lies between the same two
bounds. The conditional density is therefore between their ratio and its
reciprocal. The expectation of any [0,1]-valued tuple statistic changes by
at most the conservative bound

    beta = 4 delta/(1-delta)^2.                                (2)

There is no factor 1/Pr(E_I): the original approximation is multiplicative,
not merely an absolute TV estimate. The unconditioned two-coordinate null
comparison also has error at most beta. Thus comparing the two worlds to
their respective iid/conditioned-iid surrogates costs at most 2 beta.

The surrogate planted word has a U_k tuple at I and independent uniform
gates outside I. This is used only for local observables, not as a replacement
for the complete identity-word law.

## 2. A random equal-gate pair distinguisher

Choose an unordered pair J of distinct word positions uniformly and accept
the planted world iff the two transpositions are equal. This needs two gate
comparisons after index selection; even a sequential scan is polynomial.
The algorithm does not enumerate candidate plants or know their positions.

Inside a uniform k-bridge every fixed pair agrees with probability

    b_k = q Z_(k-2)/Z_k.                                      (3)

Indeed, any two-coordinate marginal has the first-two law, and an equal first
pair has q Z_(k-2) completions. In the conditioned-iid surrogate, a pair not
entirely contained in I agrees with probability 1/q. Consequently, with
M=binom(m,2), the actual distinguishing advantage is at least

    [binom(k,2)/M] (b_k - 1/q) - 8 delta/(1-delta)^2.           (4)

The exact null acceptance is q Z_(m-2)/Z_m. The formula above is a conservative
bound; it is not a claim that the full planted word has independent gates.

## 3. A second elementary test for k=o(N)

Choose the random pair J as above, then choose one endpoint uniformly from
its first transposition. Accept iff that endpoint occurs in the second
transposition. Its score is half their support intersection size, in [0,1].
For iid gates its expectation is 2/N.

In any length-k identity word every used label occurs at least twice. If a
label x occurred only in a gate (x,y), write the word A(x,y)B; both A,B fix x,
so the full product sends x to A(y), which is not x. This contradicts identity.
Let d_x count gate occurrences of label x. Then sum_x d_x=2k and

    sum_x binom(d_x,2) >= k.

The left side counts gate-pair intersections. A uniformly chosen pair from
the planted k-word therefore has normalized expected intersection at least
1/(k-1). Outside I the conditional-iid score remains 2/N. The actual advantage
is consequently at least

    k/[m(m-1)] [1-2(k-1)/N] - 8 delta/(1-delta)^2.             (5)

For k=poly(log N), the bracket tends to one. This is a direct lower bound on
a public test, without an estimate of the short bridge's typical structure.

## 4. A return-moment bound that also reaches k=N

The bound (5) alone is insufficient at k=N. To use (4), we give a lower bound
on b_k. Let k=2r and let C be the unnormalized Cayley adjacency operator,
the sum of right multiplication by all q transpositions. With delta_id the
unit vector at identity,

    Z_(2r)=||C^r delta_id||_2^2.

Organize permutations by transposition distance h=N-number_of_cycles. Each
edge changes h by one. A vertex at level h has at most

    s_h=h(h+1)/2

neighbors at level h-1: splitting edges number sum_cycles binom(length,2),
whose maximum at total defect h is a single (h+1)-cycle. A vertex at level
h-1 has at most q neighbors at level h. The rectangular adjacency block
between these levels has norm at most sqrt(q s_h), by its row/column sums.

Restrict to levels 0,...,r, and let D be the (r+1)-by-(r+1) symmetric
tridiagonal with off-diagonal entries b_h^*=sqrt(h(h+1)/2). Applying the
preceding block bound to the norms of vector components gives

    ||C_restricted|| <= sqrt(q) ||D||.

The vector C^(r-1) delta_id is supported at levels <=r-1; applying C to it
stays within the restriction. Hence

    Z_(2r) <= q ||D||^2 Z_(2r-2).                              (6)

For r>=2, bound the row sums of D^2 using
b_h^* <= (h+1/2)/sqrt(2). Interior rows h<=r-2 are bounded by
2(h+1)^2+1; the last two rows are bounded by
3r^2/2-r+5/8 and r^2+r/2. Thus

    ||D||^2 <= B_r
      = max{2r^2-4r+3, 3r^2/2-r+5/8, r^2+r/2}.              (7)

For r=1 take B_1=1. For r>=6 the maximum is 2r^2-4r+3.
Combining (3) and (6) yields b_(2r)>=1/B_r.

At k=N=2r>=12, q=2r^2-r, so q-B_r=3r-3>0. The positive main term in (4) is
therefore at least

    (3r-3) / [binom(m,2)(2r^2-4r+3)].                         (8)

This is of order N^(-5) when m=N^2. It applies to a growing N-gate plant,
not the previous near-full k=m-2 control. The bound is conservative; the
finite exact return ratios give stronger numerical values.

## 5. Why quadratic hosts satisfy the smoothing premise

The checked Diaconis--Shahshahani Fourier/L2 estimate for the walk with
identity mass 1/N gives a constant A with d2 at t=(N/2)(log N+c) at most
A exp(-c). Source conventions and exact passages are recorded in
[source-audit.md](source-audit.md).

Let theta_lambda be the pure-transposition eigenvalue and
alpha_lambda=1/N+(N-1)theta_lambda/N the source walk's eigenvalue. Conjugate
partitions pair theta,-theta with the same dimension. For even j=2t,
Fourier inversion and |character(g)|<=dimension give

    delta_(2t) = (1/2) sum_(lambda != trivial,sign) d_lambda^2 theta_lambda^(2t)
               <= sum_(lambda != trivial) d_lambda^2 alpha_lambda^(2t)
               = d2(source walk at t, uniform S_N)^2.

For each theta>=0, alpha>=theta; this proves the inequality after pairing.
The equality for delta holds because all even-power terms are nonnegative
and the pointwise bound is attained at identity. For odd j use monotonicity.
Thus, for sufficiently large j/N-log N>0,

    delta_j <= A^2 exp[-2((j-1)/N-log N)].                      (9)

With m=N^2 and k<=N, j=m-k-2 and delta_j=exp(-Omega(N)). The error in (4)
and (5) is negligible compared with their inverse-polynomial main terms.

**Proved consequence.** For fixed c>0 and even-rounded k=(log_2 N)^c,
the shared-label test has advantage Omega(k/N^4). For k=N on even N,
the equal-gate test has advantage Omega(N^(-5)). Both run in polynomial time
and use only one challenge word. Therefore both proposed quadratic-host
ensembles fail computational indistinguishability with negligible error in N.
These lower bounds do not claim a constant advantage or optimality.

When m=N and k=poly(log N), the suffix is of order N and (9) does not give
small error. Neither (4) nor (5) is asserted to refute that regime. Bounds
that return delta>=1 are recorded as unavailable, not as evidence of hardness.

## 6. Security parameter and generation caveats

This obstruction uses the explicit convention poly(N,m)-time and negligible
advantage in N. If the security index is n=log_2 N, an N^(-5) advantage is
exponentially small in n. It does not refute negligible-in-n security.
But an m=N^2 word is then exponentially long in n, and poly(N,m) running time
is not polynomial in n. Specify the representation, access model and intended
time/advantage requirements before describing that as a standard efficient
cryptographic assumption.

No exact sampler for arbitrary U(N,N) or U(N,N^2) is supplied here. Short
plant generation and host generation are different obligations. The public
attack does not need either sampler; its probabilities concern the defined
ideal challenge laws. A practical construction would additionally need actual
generation with a declared distribution/error guarantee.

## Validation, dependencies and unresolved step

The finite checker uses exact return spectra, compared independently with
cycle-type cut/join enumeration for N2..8. It reproduces 27,120,3936 at the
mandatory cases and tests all row-bound inequalities for r1..500. Earlier
complete word laws independently check the local comparison formula wherever
delta<1, including exact-zero-error S3 cases. Finite certificates use exact
delta and do not need the unknown constant A from the asymptotic theorem.

Exceptional cases: odd m or k are infeasible; k0/km are identical laws;
N2 is a singleton law and has no distinguishing gap; m0/m2 have no nontrivial
plant length. The N-gate plant theorem is stated for even N>=12 and
sufficiently large N for the asymptotic error comparison. It does not assert
that the loose bound B_r is sharp.

Proved elementary inputs are (1)--(8), with the stable-sort ingredient
rederived in the preceding report. The external input is precisely the
source walk's Fourier/L2 estimate, translated above. No identity-Hurwitz
classification, local-chain irreducibility or gap theorem is imported.

**First unresolved obligation:** for m=N and k=even-rounded (log N)^c,
derive the actual joint bridge/plant two-coordinate law (or another efficient
observable's law) without long-completion smoothing, and determine whether
it yields an inverse-polynomial bias. Surviving this test would not establish
hardness. A different gate library or a null law calibrated to planting's
visible statistics is a new model and requires its own generation analysis.
