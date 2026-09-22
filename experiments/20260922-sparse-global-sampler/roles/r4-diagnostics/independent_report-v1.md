# R4 independent diagnostics report — R4-DIAG.v1 / R4-INEQ.v1

Frozen 2026-09-22 before nonauthor sampler review. Verdict: **keep** the exact certificate and marked-component diagnostics. The finite checks find no obstruction to H0 or to either proposed count/incidence bound. They do not certify T0, an asymptotic tail estimate, or any mixing claim.

## Law, parameters, and dependencies

The target is global Unif(Omega(N,m)), ordered transposition identity words on distinguished labels. Products act rightmost first. There is no Markov kernel. H0 retains exactly components with genus at most one or size at most the fixed TOP-LEVEL K=max{v<=N:v^(2v)<=(N+m+2)^4}. A separate deliberately smaller cutoff K=2 is always labeled diagnostic_override. K is never recomputed during a count recursion.

C(v,ell) counts connected words on one fixed labeled v-set; C(1,0)=1 is the isolate convention. The DYZ positive recurrence is an imported mathematical dependency, independently implemented here with no old-code import. Its interpretation/normalization is checked against independent tiny labeled-permutation walk counts and proper-component subtraction. This finite agreement is internal evidence, not a replacement for the source theorem audit.

Let F(s,m) count identity words using every one of s fixed labels; isolates are excluded. Connected feasibility ell>=2(v-1)>=v implies s<=m. The least active label gives

    F(s,m)=sum_{v>=2,ell} binom(s-1,v-1)binom(m,ell) C(v,ell)F(s-v,m-ell),
    F(0,0)=1.

Consequently Z(N,m)=sum_{s<=min(N,m)} binom(N,s) F(s,m). The restricted version replaces C by its allowed entries, using the same fixed K. This evaluates large-N certificates without an O(N) table. It is a second assembly representation, not an independent proof of DYZ counts. The exact global error of an exact conditional sampler is (Z-Z_A)/Z. Its numerator and denominator are stored as integers.

## Marked identities — proved combinatorially

For X_(v,ell), the number of components of type (v,ell),

    Z E[X_(v,ell)] = binom(N,v)binom(m,ell)C(v,ell)Z(N-v,m-ell).

Choose the marked label set and its positions, choose its connected internal word, and choose any identity word on the complement. The maps are bijective when a distinguished component is retained. The unrestricted remainder may contain components of the same type; that is correct. No independence assumption enters.

For ordered distinct marked components (v,ell),(w,j), the corresponding numerator is

    binom(N,v)binom(N-v,w)binom(m,ell)binom(m-ell,j)
      C(v,ell)C(w,j)Z(N-v-w,m-ell-j).

For identical types this is E[X(X-1)], not E[X^2]. Summing over excluded types gives E[B] and E[B(B-1)] for the number B of excluded components. Exact arithmetic checks 0<=P(B>0)<=E[B] and P(B>0)>=E[B]-E[B(B-1)]/2. A fixed labeled weighted macro has exactly m! product_B C(|B|,ell_B)/ell_B! literal words. These label and interleaving multiplicities were checked against independent weighted-support walk DP, not merely the assembly recurrence.

## Exact finite evidence

The first run covers m<=32 and 128 certificate rows. Tiny checks: 91 total/active/connected count cells through N<=6,m<=12, and 23 weighted-support/cutoff cases including (3,4),(4,4),(4,6),(3,6),(4,8),(4,10), N=1, N=2, m=0, m=2, odd m, high-genus tiny support, and deliberately excluded words. At N=2 every feasible even word is included by actual H0, including ell=12. Forced K=2 at (3,8) instead excludes connected genus-two components and has omitted mass 728/729. Actual-K cases where the omitted mass is zero are not used to validate a tail estimate.

The second run tested 992 connected-count inequalities, all feasible nonzero genera through ell<=64, in the normalization A_g(v)=C(v,2v-2+2g)/(2v-2+2g)!:

    A_g(v) <= A_0(v) ((v^3-v)/36)^g/g!,
    A_g(v) <= A_0(v) (sum_{i=1}^{v-1}i^2/12)^g/g!.

No counterexample occurred. The maximum actual/bound ratio for the cubic36 bound is 1/2, at v=2,g=1; the sum-squares bound is exact there. These are bounded checks of provisional proof inputs.

It also tested 517616 incidence inequalities for N=2..128 plus 256,512,1024,2048,10000,1000000, every even 2<=m<=min(N,64), and each feasible (v,ell):

    E X_(v,2q) <= binom(N,v) A(v,q) (4k/(N-2k+1)^2)^q, m=2k<=N.

No counterexample occurred. The maximum ratio is 999999/1000000 at N=1000000,m=2,v=2,ell=2. This near-equality is a useful constants stress case. The common positive binom(N,v)C(v,ell) factor was canceled before the integer comparison; all endpoint-conditioning and interleaving factors remain.

| N | m | actual K | T0 range | H0 omitted probability | any size>K probability | any genus>=2 probability |
|---|---|---|---|---|---|---|
| 82 | 14 | 5 | True | 2.98849294772e-08 | 0.00948130170402 | 8.98249195157e-07 |
| 128 | 16 | 5 | True | 7.56743290889e-09 | 0.00478411143797 | 2.03442346859e-07 |
| 128 | 18 | 5 | True | 3.25147557794e-08 | 0.00976564399454 | 3.88883724003e-07 |
| 512 | 32 | 6 | True | 4.86270136623e-11 | 0.000221745084024 | 5.79579383376e-09 |
| 2048 | 64 | 7 | True | 2.75213746115e-14 | 2.39503195357e-06 | 1.34637781261e-10 |
| 8 | 12 | 4 | False | 0.0387457825886 | 0.945103442916 | 0.0463355234775 |
| 16 | 32 | 4 | False | 0.97315024954 | 0.999999998533 | 0.973177908556 |
| 32 | 64 | 5 | False | 0.999996086256 | 1 | 0.999996093588 |
| 16 | 12 | 4 | False | 0.000728481286035 | 0.612556141933 | 0.001290937291 |
| 32 | 12 | 4 | False | 1.11809609948e-05 | 0.206818816184 | 3.88135042403e-05 |
| 64 | 14 | 5 | False | 1.913206619e-07 | 0.0216037876629 | 3.18922968819e-06 |

The first possible nonzero H0 tail in the finite search N=2..128 over all T0-feasible even lengths is N=82,m=14,K=5. Its exact omission is 7633925094110515200/255443972184307397709618401. It consists of the v=6,g=2,ell=14 sector; the stronger size-only omitted event is roughly 317260 times larger. At N=128,m=16,K=5, the omission is 3015538111971730865520000/398488912723604665601813065391959; R3 independently reproduced this exact fraction using its count path in roles/r3-sampler/crosscheck-n128-m16.json.

The data separate four marked categories: small support/low genus, small support/high genus, large support/low genus, and the excluded large support/high genus intersection. The nonzero excluded types retain v,ell,g individually, so long-length contributions can be inspected separately. At larger N the same short m does not probe the end of T0's length interval. No decreasing finite curve here supports an asymptotic conclusion by itself.

## Provenance and rerun commands

Commit 20e86f665f69053031fe7eec0c3388458affb1fc. Python3.12.3, standard library only, deterministic exact arithmetic, seed not applicable. Old source hashes were recorded before any potential import; no old code was imported or changed. Initial dirty state is preserved. R3 and R4 coordinated the initial two heavy slots; R4 released its slot after these runs.

    timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r4-diagnostics/diagnostics.py --m-max 32 --output experiments/20260922-sparse-global-sampler/roles/r4-diagnostics/results-m32.json
    timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r4-diagnostics/check_inequalities.py --m-max 64 --output experiments/20260922-sparse-global-sampler/roles/r4-diagnostics/inequality-results-m64.json

Recorded inner runtimes are about 0.067 and 2.199 seconds. Mathematical conclusions remain exactly finite; source theorem and uniform tail proof are separate obligations. No random sampling diagnostics or mixing inference was used.
