# Canonical smaller positive extension — SB-T1.v1

Audit disposition of these exact bytes is recorded in claim_ledger.md. This canonical synthesis incorporates UPPER.v2 and the separately audited unchanged algorithmic dependencies. Internal same-model review is correlated, not external human certification. This is global sampling, not local mixing.

For N>=2 and even m>=0 let Omega(N,m) be the ordered, labeled transposition words with identity product, using (ab)(x)=a(b(x)); U is its uniform law. Put P=N+m+2 and K=max{1<=v<=N:v^(2v)<=P^4}, fixed once at the original input. A nontrivial connected component has size v>=2 and length 2v-2+2g, g>=0; an isolate is(1,0). H0 allows g<=1 OR v<=K; H1 allows v<=K. Both include arbitrary genus on small support.

**SB-T1.v1.** The unchanged exact H0 and H1 algorithms have expected O(P^20) bit time and O(P^10) storage and, uniformly over all even m<=N^(2/3)ln(N)/4, global TV error at most eta_new(N) in Section3. They always return a literal length-m identity word. This is a smaller extension, not the full T0 benchmark m^4<=N^3. The same algorithm and polynomial exponent serve every inverse-power error target. Exact randomness uses independent fair bits.

Notation: Z(n,2j)=|Omega(n,2j)| and S(n,j)=Z(n,2j)/(2j)!. Let C(v,ell) be the connected identity-word count on one fixed v-set and A_g(v)=C(v,2v-2+2g)/(2v-2+2g)!. The checked DYZ input and induction in source_checks.md give A_g(v)<=v^(v-3)b_v^g/g!, b_v=(v^3-v)/36.

For clarity the two imported combinatorial identities are stated here. Marking a component of size v and cost q gives exactly E X_(v,q)=binom(N,v) A_(q-v+1)(v) S(N-v,k-q)/S(N,k), m=2k. To compare the normalization, a base macro of cost k-q uses at most2(k-q) labels. Add q disjoint fresh size-two minimal components among its isolated labels. Each contributes normalized weight1/2. There are at least D^(2q)/(2^q q!) choices, D=N-2k+1, so total extension weight is at least D^(2q)/(4^q q!) times base weight. Any final macro has at mostk such pairs and at mostbinom(k,q) preimages; requiring a specified removed v-set to be isolated after deletion only reduces this number. Summing exact incidence weights yields S(N-v,k-q)/S(N,k)<=4^q q!binom(k,q)/D^(2q). The case q0 uses empty products; zero residual counts contribute zero. This is a count comparison under the actual bridge normalizer.

## 1. Immediate algebraic range of old tail

For m=2k<=N, D=N-2k+1, x=4k/D², z=k²(k+2)/(9D²), old rho=exp(1+z)Nx. The old bound is N exp(1+z) rho^K/[(K+1)^3(1-rho)] whenever rho<1. For m=c N^(2/3)(log N)^(1/3), log rho=(c³/72-1/3)log N+(1/3)loglog N+O(1). Thus any fixed c<24^(1/3) already yields a negligible tail exp(-Omega((log N)^2/loglog N)). This is an algebraic corollary, not a new mechanism. The literal equality-boundary c=24^(1/3) does not satisfy rho<1 asymptotically.

## 2. Finite binomial genus majorant

Use the hash-frozen old exact marking formula and factorial genus bound A_g(v)<=v^(v-3)b_v^g/g!, b_v=(v³-v)/36. The old incidence proof gives the sharper, already stated first inequality

S(N-v,k-q)/S(N,k) <= 4^q q! binom(k,q)/D^(2q) = 4^q (k)_q/D^(2q).

For a size-v component q=v-1+g and necessarily 0<=g<=k-v+1. Thus for 2<=v<=k+1,

E X_v <= binom(N,v) v^(v-3) (k)_(v-1)(4/D²)^(v-1) (1+4b_v/D²)^(k-v+1).  (FG)

Indeed (k)_(v-1+g)=(k)_(v-1)(k-v+1)_g and the remaining finite sum is exactly the binomial theorem. This retains both constraints the old proof discarded. Its normalizer is the exact bridge count; no random graph independence is used.

The finite H0 version sums g>=2 instead, giving the same prefactor times [(1+a)^h-1-ha], a=4b_v/D²,h=k-v+1. H1 uses the full (1+a)^h. Both union bounds sum only v>K through min(N,k+1), and cap at 1.

## 3. Explicit new logarithmic range — UPPER.v2

Define z_new=3k/(9D²)^(1/3), c_new=exp(1+z_new), rho_new=c_new N x. Since 1+s³<=(1+s)³ and log(1+s)<=s for s>=0,

(1+4b_v/D²)^(k-v+1) <= exp[k log(1+v³/(9D²))] <= exp(z_new v).

Consequently E X_v <=N c_new rho_new^(v-1)/v³. For any integer J>=1 with rho_new<1,

Pr_U(max nontrivial support size>J) <=min(1,N c_new rho_new^J/[(J+1)^3(1-rho_new)]). (NT)

When J>=k+1 the event is empty. H1 error is the event probability; H0 error is at most it. All component and genus constraints are unchanged.

For N>=2^2048 let L=ln N>1000. If m<=N^(2/3)L/4 then m<=N/4, D>=3N/4. The elementary inequality L<=exp(L/3) gives the first assertion. We have

z_new=3m/[2(9D²)^(1/3)] <=m/N^(2/3)<=L/4,
Nx=2Nm/D²<=4m/N<=L exp(-L/3).

For L>=1000, 1+ln L<=L/24, so ln rho_new<=1+ln L-L/12<=-L/24. Thus rho_new<=1/2 and c_new<=e N^(1/4). As in the old proof, v0=floor(2L/ln L) is feasible in the fixed top-level cutoff and K>=L/ln L. Discard the cubic denominator in (NT):

Pr_U(max size>K)<=2e N^(5/4) exp[-L²/(24ln L)]<=exp[-L²/(48ln L)].

The last inequality follows because L/(48ln L)>=1000/(48ln1000)>3 and hence L²/(48ln L)>3L>(5/4)L+ln(2e). Monotonicity holds for L>e. This proves one explicit uniform negligible bound

eta_new(N)=1 for 2<=N<2^2048;
eta_new(N)=exp[-(ln N)²/(48lnln N)] for N>=2^2048.

For every fixed a>0 it suffices to take ln N>=max(2048ln2,(48a)²), since ln L<=sqrt(L) for L>=100, to get eta_new(N)<=N^(-a). Neither policy, cutoff, algorithm nor polynomial runtime exponent depends on a. The imported exact algorithms retain expected O(P^20) bit time and O(P^10) storage; this argument changes only their proved accuracy regime. Their exact global laws and algorithmic theorem are checked in roles/r4-construction/algorithm-audit.md against frozen source hashes; details are summarized in Section6.

The extension m<=N^(2/3)ln N/4 is strictly larger than every c N^(2/3)(ln N)^(1/3) old-tail regime. It is strictly smaller asymptotically than the proposed m^4<=N³ benchmark. It therefore establishes a new smaller extension but does not establish P0, P1 or T0 at that benchmark.

## 4. Sharper finite variant

The same incidence proof permits a better denominator. A cost-(k-q) base has at least N-2k+2q isolates, so its number of ordered fresh labels is at least the rising factorial D^(overline(2q)). Thus replace D^(2q) in every genus term by D(D+1)...(D+2q-1). This improves the finite union bound but sacrifices the simple binomial closed form. It introduces no new assumption.

H0: sum v>K and g=2..k-v+1. H1: sum v>K and g=0..k-v+1. In each case each term is

binom(N,v) v^(v-3)b_v^g/g! * 4^q(k)_q / D^(overline(2q)), q=v-1+g.

A zero residual bridge can only decrease the true marked count. The bounds assume m<=N so D>0. They are statements about exact conditioned laws, not unconditioned transposition graphs.

## 5. Dependencies, boundaries and first open step

Dependencies: old exact marked component formula; old fresh-pair incidence argument; old DYZ-derived factorial genus majorant and genus-zero count; imported H0/H1 literal decoders and top-level K/runtime theorem. The present new step is the finite binomial summation, followed by elementary inequalities. No new external theorem, sequential product bound, random-graph independence or mixing hypothesis is used.

m=0: empty word and zero error. m=2: repeated-edge law and zero error. N=2: every even length has the unique repeated edge and zero error. N=1 has only m=0; positive/odd lengths have empty target and are outside theorem. A nontrivial component requires v<=k+1; near-minimal v=k+1 has h=0 and only g=0, and v=k has h=1 and no H0 omitted component. Fixed K>=2 includes every positive genus component on two labels. No zero-count branch is normalized.

The full benchmark is separate: obstruction.md refutes P0 and P1, so an extension of these unchanged policies to all m^4<=N³ is impossible. The existence target T0 remains unresolved and would require another policy or algorithm. No missing inequality is hidden in the smaller SB-T1.v1 result.

Finite falsification: R3 reports 53,300 exact rational component-term cells and 7,300 finite-binomial sums/identities through m<=48,N<=1000, all passed. Full domains and hashes must be read from that role's raw artifact before promotion. These checks do not prove the asymptotic result; the proof above does.

## 6. Literal algorithm and resources

The unchanged implementation is ../20260922-sparse-global-sampler/roles/r3-sampler/sampler-v4.py, SHA256 cdb91799b02539190bc31ce7d6fe31ee5af0477b1cc653f43452eb18de734002, through the unchanged sample.py wrapper hash2d74da262e4c53005a05d4f171b85c5469ade520e38b91b1b0df14f4cbe8386e. Its exact conditional laws and resources hold for every even input length, independently of any tail theorem.

For each allowed type put D(v,ell)=C(v,ell), and put zero on other nontrivial types, with D(1,0)=1. Least-label assembly uses

    Z_D(n,t)=sum_(v,ell) binom(n-1,v-1)binom(t,ell)D(v,ell)Z_D(n-v,t-ell).

Choose component size/length with these integer weights, its remaining labels and positions uniformly, and its connected word by the exact primitive; recurse on the residual labels/positions with ORIGINAL K. Each final word uniquely recovers these choices, giving probability1/Z_D(N,m). Zero-weight branches are never selected. The global error is exactly1-Z_D/Z.

For v<=K, connected suffix counts retain remaining length r, literal prefix permutation p and exposed support partition pi. The terminal indicator is[p=id and pi has one block], and each literal edge contributes its exact continuation count after right-multiplying p and joining its support blocks. Selecting an edge with that count telescopes to the uniform connected-word law. An explicit stack implements the recurrence. For H0 only, larger g0/1 components use the unchanged September7 constructive fixed-endpoint genus0/1 decoder with positive conditional choices; its frozen proof and source checks are reviewed in algorithm-audit.md. H1 avoids this extra dependency.

At v<=K, v!Bell(v)<=v^(2v)<=P^4; including all remaining lengths and eligible degrees gives at most(m+1)K P^4<=P^6 memo keys. Counts have O((m+1)logP) bits. The positive count and assembly recurrences cost O(N²(m+1)²) exact arithmetic operations. The old conservative bound explicitly charges dictionary operations, keys, stacks, random integer rejection and the H0 g01 primitive, giving expectedO(P^20) bit time and O(P^10) storage at every even length. Exact integer rejection uses fewer than two expected trials. No exponent depends on an accuracy parameter. Reproduction and all regression domains are in coordinator_report.md and regression_registry.md.
