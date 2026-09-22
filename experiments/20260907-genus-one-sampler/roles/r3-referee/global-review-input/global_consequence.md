# Global component consequence — G1.v1 (provisional, awaiting nonauthor audit)

Target: uniform on all ordered identity words Omega(N,m), with arbitrary
support. Composition is rightmost-first. No Markov kernel is involved.

Let C(v,ell) be the number of connected identity words on a fixed labeled
v-set, with C(1,0)=1 for isolates and C(1,ell>0)=0. Define A_01 to be the
subset of Omega(N,m) whose every nontrivial component has genus at most one,
that is, ell=2v-2 or ell=2v. Put Z_01=|A_01| and Z=|Omega(N,m)|.

## G1-COUNT.v1: exact counts and selector

DYZ, *Classical Hurwitz numbers and related combinatorics*, Proposition 1,
equation (13), and Section 1.2 equations (19)-(20), give C(d,k)=d!k!h_(g,d)
for k=2d-2+2g. Primary source checked during this run:
https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf
(PDF pages 4-5). Its labeled monodromy tuples have the sheet-label quotient
d!, while h also divides by the branch-position factorial k!. Connected
covers correspond to transitive monodromy, equivalently connected support.
Reversing all factors translates any inverse product convention and preserves
the identity target.

Multiplication of the positive recurrence by d!k! gives

    d^2(d-1) C(d,k)
      = 2 sum_(a+b=d) binom(d,a)
          sum_(k1+k2+r=k; r even>=2)
            multinomial(k;k1,k2,r) a^(r+1)b^2 C(a,k1)C(b,k2).

All divisions are exact. Two binomial convolutions per degree split give
O(N^2(m+1)^2) arithmetic operations. Positive accumulated numerators are
bounded by d^2(d-1)C(d,k); all counts are at most binom(N,2)^m. Precomputed
binomials/powers and all operands therefore have O((m+1)log(N+1)) bits.
The base m=0 can be filled directly. This is polynomial bit complexity in
N,m; it counts words but does not itself decode them.

For D(v,ell)=C(v,ell) or its restriction to allowed g<=1 entries, define

    Z_D(0,0)=1,
    Z_D(n,k)=sum_(v=1..n,ell=0..k)
      binom(n-1,v-1) binom(k,ell) D(v,ell) Z_D(n-v,k-ell).

Distinguish the least label, choose its component size and length with the
displayed integer weights, choose the other component labels uniformly and
its positions uniformly, fill those positions with a uniform connected
internal word, and recurse. Each literal word has one such decomposition.
The selection factors cancel to 1/Z_D(n,k) by induction. The full macro
weight is m! product_B C(|B|,ell_B)/ell_B!, with isolated labels implicit.
Equal component sizes are not counted as distinguishable unless their labels
distinguish them. This recursion avoids enumerating set partitions.

The selector has the same polynomial count-bit bound. Exact random integer
draws use fair bits with rejection below twice the desired range, hence
fewer than two trials in expectation. Uniform label and position subsets
are sampled by exact binomial conditionals. At most N components are drawn.

## G1-SAMPLE.v1: consequence of connected samplers

If exact expected-polynomial connected samplers for genera zero and one
are accepted, the above algorithm samples exactly Unif(A_01) in expected
time polynomial in N,m. For Z_01>0 its global TV error is exactly

    1 - Z_01(N,m)/Z(N,m).

The rational certificate is computable in polynomial bit time. If internal
components are approximate, require conditional TV error at most
epsilon/(2N) for every allowed component type and every preceding selection
history. Couple each draw to its exact component conditional law and union
bound the at most N coupling failures. The resulting global TV is at most
1-Z_01/Z+epsilon/2. This uses conditional couplings, not products of marginal
success probabilities. If exact component laws are used, no b-dependent
precision computation is required.

Boundaries: m=0 gives the empty word; odd m gives an empty identity fiber;
m=2 gives a repeated uniform edge. At N=2 all feasible even words are
singletons, including higher genera; the literal g<=1 subset excludes
lengths >=6 even though those singleton components can separately be added
to a larger hybrid. At N=1 only m=0 is feasible. No global sampler is claimed
from a zero-mass restricted set.

## G1-SAT.v1: characterization at m=2N

For N>=2, A_01(N,2N) consists exactly of partitions of all N labels into
nontrivial genus-one components. In particular it has no isolates or
genus-zero components. Indeed, if s labels are active, k components are
nontrivial, and G is their total genus, then

    2N = 2s-2k+2G <= 2s <= 2N.

Equality forces s=N and G=k, and each component genus is at most one.
The converse follows by summing their lengths 2v.

Consequently A_01 is nonempty for every N>=2 (one connected genus-one
component suffices), and its count also satisfies the separate recurrence

    A(0)=1, A(1)=0,
    A(N)=sum_(v=2..N) binom(N-1,v-1) binom(2N,2v) C(v,2v) A(N-v).

## G1-OMIT.v1: genus<=1-only global error tends to one at m=2N

This is a named-method obstruction, not a hardness claim. Subject to the
checked classical count formula, it is a universal proof independent of the
finite mass table below.

Vakil, *Genus 0 and 1 Hurwitz Numbers*, Corollary 1.5 with Section 1.2
normalization, gives for the identity profile 1^v

    a_v := C(v,2v)/(2v)!
      = v^(v-2)/24 [v^2-v-sum_(j=2..v) v^(2-j)(j-2)! binom(v,j)]
      <= v^v/24 <= 3^v v!.

Primary source: https://math.stanford.edu/~vakil/files/g01hurwitz.pdf,
PDF pages 3-4. The final inequality follows from v!>=(v/e)^v and e<3.
All terms subtracted in the bracket are nonnegative; its nonnegativity
also follows from the counting interpretation.

By G1-SAT and the exact macro formula,

    Z_01(N,2N)/(2N)! = sum_(set partitions pi, |B|>=2) product_B a_|B|
                    <= 3^N sum_pi product_B |B|!
                    <= 3^N N! 2^(N-1) <= 6^N N!.

For the penultimate inequality, order k blocks and sum over ordered
compositions v1+...+vk=N, vi>=2. Each composition contributes N!/k! after
its product of vi! cancels label-allocation denominators. Discarding 1/k!
and allowing all positive compositions gives 2^(N-1).

For any integer 2<=r<=N, embed words supported on a fixed r-subset. The
unconditioned transposition walk on S_r has N-step probabilities p_N(q)
with p_N(q)=p_N(q^-1), supported on one parity class of size r!/2.
Cauchy-Schwarz therefore gives

    Z(N,2N) >= binom(r,2)^(2N) sum_q p_N(q)^2
             >= 2 binom(r,2)^(2N)/r!.

Thus the explicit finite bound is

    Z_01/Z <= min(1, (2N)! N! 6^N r!/[2 binom(r,2)^(2N)]).

For all sufficiently large N choose r=floor(N/log N), which lies in [2,N].
Then log binom(r,2)=2log N-2loglog N+O(1) and log(r!)=O(N), while
log((2N)!N!6^N)<=3Nlog N+O(N). It follows that

    log(Z_01/Z) <= -Nlog N+4Nloglog N+O(N) -> -infinity.

Therefore exact genus<=1-only assembly has global TV tending to one at
length 2N. Any output law supported on A_01 has TV at least 1-Z_01/Z,
so approximate internal draws cannot repair the omitted support mass.
This does not exclude a hybrid that includes higher-genus components.

## Exact finite evidence (not asymptotic inference)

Command, standard library Python 3.12.3, deterministic, no seed:

    timeout 240s python3 -B experiments/20260907-genus-one-sampler/global_mass.py --n-max 64 --m-max 128 --output experiments/20260907-genus-one-sampler/global_mass_results.json

The run took approximately 5.24 seconds. It checked 91 total/connected
count cells against an independent labeled-permutation DP followed by
subtraction of proper support components, through N=6,m=12. Direct word
enumeration checks all required cases and every allowed word's assembly
probability, including N=4,m=8 (131040 connected and 140160 total words).
All tests passed. No old experiment was edited; the imported count code's
SHA-256 and commit are recorded in the machine-readable result.

| N | m=2N covered mass | exact counts when compact |
|---|---|---|
| 2 | 1 | 1/1 |
| 3 | 80/81 | 240/243 |
| 4 | 4375/4672 | 131250/140160 |
| 8 | 0.4749275971790145 | full integers in JSON |
| 16 | 0.026822091443972705 | full integers in JSON |
| 32 | 0.000003906412046870242 | full integers in JSON |
| 48 | 0.00000000005016303872254337 | full integers in JSON |
| 64 | 0.00000000000000012153123245476415 | full integers in JSON |

The machine-readable file stores 369 exact rational certificates. Decimal
renderings are for readability; conclusions at a requested epsilon use exact
integer comparisons. The separate saturated recurrence agrees throughout.

Current verdict: keep as provisional proof and exact certificate; request
nonauthor audit of G1-COUNT, G1-SAMPLE, G1-SAT and G1-OMIT before promotion.
