# Post-freeze nonauthor audit, version RF-A1

Audit started after blind_report.md was frozen at 09:34:39 UTC. Its content and hash remain unchanged. Exact received proofs and their hashes are preserved under review_inputs/. Coordinator statements of confidence were received after freeze and were not used as evidence. Same-model reviews are correlated.

## Separate verdicts

| Exact claim | Status | Remaining obligation |
|---|---|---|
| R2-O1: N=2^(8j), m=2^(6j), j>=64 implies Z_A/Z<=2^(-1-jm/2) | **ACCEPT / proved with checked primary-source input** | None identified in the counting claim; coordinator synthesis remains separate |
| UPPER.v2 statistical bound on Q_A,Q_B for even m<=N^(2/3) ln(N)/4 | **ACCEPT / proved with checked primary-source input** | Interpret auxiliary J as an integer; define S explicitly |
| UPPER.v2 expected O(P^20) bit-time / O(P^10) storage sampler theorem | **CONDITIONAL in this referee report** | Current R4 audit of the exact H0/H1 decoders and resource model |
| Original full-range negligible-error claims for Q_A,Q_B | **REFUTED** | Preserve original range and policies when stating repairs |
| Existence of another polynomial sampler over the original full range | **UNRESOLVED here** | Literal algorithm, uniformity proof and bit-cost accounting |

R2 input SHA256: a6716e623768ded49b5ba1a2441abdddc8cb18c61be52d8a96b79387fe68b33f.
R1 proof-v2.md SHA256: b76f706aad3dae20ed3550298b98bd260b295f7cc9752eb3f1ecef663c87ac3c. Its heading still says UPPER.v1; the audited strongest theorem is Section 3, UPPER.v2.
Coordinator source-check input SHA256: 7940610828041f50b7ff94ae339114f1e874d31fac15ebf66c29c12c53fb9337.

## DYZ dependency reconstructed from primary source

I had independently opened the primary DYZ paper during the blind phase. I now rechecked Proposition 1, equation (13), together with the labeled-word identification in Section 1.2, equations (19)--(20) and following text. Write F_v(t)=sum C(v,ell)t^ell/ell!, A_g(v)=C(v,2v-2+2g)/(2v-2+2g)!. The normalized recurrence is

    v²(v-1) F_v
      =2 sum_(a+b=v) binomial(v,a) a b² (cosh(at)-1) F_a F_b.

The genus-zero coefficient is A_0(v)=v^(v-3), with F_1=1. Dividing by A_0(v)t^(2v-2) makes the recurrence a convex combination of L(at)H_a H_b, where

    H_v=F_v/[A_0(v)t^(2v-2)],
    L(z)=2(cosh z-1)/z².

The weights are explicitly

    w_(a,b)=binomial(v,a) a^a b^(b-1)/[v^(v-1)(v-1)].

They are nonnegative and sum to one by the same genus-zero coefficient identity. Coefficientwise,

    L(z) <= exp(z²/12),

because 2/(2j+2)! <=1/(12^j j!), initially with equality, and the successive ratio is 12(j+1)/[(2j+4)(2j+3)]<=1. If b_v=(v³-v)/36 then

    b_v-b_a-b_b=abv/12 >= a²/12.

Induction on v therefore gives H_v<=exp(b_v t²), hence

    A_g(v) <= v^(v-3) b_v^g/g!.

This checks the actual all-genus dependency instead of inheriting its previous certification. The singleton case has b_1=0. No convergence of a sum over unbounded degree is required and no conditional independence is asserted. Source: https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf.

## R2-O1 audit

I checked the complete coefficient assembly, retaining the factor (N)_s, v!, ell! and component multiplicity factorial separately. Replacing (N)_s by N^s and adding profiles with too many vertices is an upper bound, including all high-genus small components. The genus majorant is evaluated only at fixed bounded degree before the displayed convergent geometric domination.

With x=k/N² and q=3Nx, the candidate's S_0 and S_1 computations give exactly

    S_0 <=9k/[8(1-q)],
    S_1 <=kx/[4(1-q)].

The three conditions q<=1/2, x<=1 and b_K x<=1 imply S_A<=29k/4<8k. The bound K<=16j+2, the j=1 check, and monotonic decrease of (16j+2)^3/[72*2^(10j)] all hold. Arbitrarily high genus on components v<=K is included, not silently removed.

The denominator 2*binomial(r,2)^m/r! follows because a half-length walk lies in one parity class of S_r; inversion symmetry identifies the return probability with the square sum of the midpoint distribution. This proof handles r=2 exactly and excludes m=0 as required. For r=floor(m/(6j)), every floor, factorial, and power-of-two estimate in the candidate is in the correct direction. The remaining constant is bounded by 2^18, and 2^18 j²<=2^(j/2) follows from the j=64 check and the displayed monotone ratio. Thus the exact claimed 2^(-1-jm/2) bound survives.

My frozen blind report supplies a differently bounded proof for every sufficiently large N along m_*(N), using only genus-zero/one formulas and crude small-component counts. It corroborates the conclusion but does not replace this check or imply reviewer independence.

## UPPER.v2 incidence and conditioning audit

For clarity define S(N,k)=Z(N,2k)/(2k)!, and S(0,0)=1. The exact marked-component identity is

    E_U X_v = binomial(N,v) sum_(g=0)^(k-v+1)
       A_g(v) S(N-v,k-v+1-g)/S(N,k).

This is an equality under the conditioned uniform bridge law. It is not a calculation under an independent-edge graph approximation.

I independently reconstructed the pair-insertion comparison. A base identity word of length 2(k-q) has at most 2(k-q) active vertices, hence at least N-2k+2q fresh labels. Choose q disjoint fresh edges, insert each twice, and interleave them with the base word. For D=N-2k+1>0, each base has at least

    D^(overline(2q))/(2^q q!)

choices of unordered edges and

    (2k)!/[(2k-2q)! 2^q]

interleavings. A final word has at most k isolated repeated-edge components; deleting q of them yields at most binomial(k,q) preimages. This proves

    S(N-v,k-q)/S(N,k)
       <=4^q (k)_q/D^(overline(2q))
       <=4^q (k)_q/D^(2q).

The fact that the original base uses a prescribed N-v subset only reduces the number of possible preimages. This closes the old incidence dependency directly. The support-size bound for the base follows from the connected-component feasibility relation, or from the impossibility of an identity word with a vertex used exactly once.

Substituting the checked genus majorant, writing q=v-1+g and h=k-v+1, leaves the finite sum

    sum_(g=0)^h (h)_g (4b_v/D²)^g/g!
      =(1+4b_v/D²)^h.

The genus>=2 version subtracts exactly 1+h(4b_v/D²). This handles h=0,1 without a fake omitted high-genus component. There is no replacement of a conditional estimate by a marginal one; a deterministic incidence bound controls the exact normalizer ratio.

## UPPER.v2 constants and quantifiers

The inequality (1+s³)<=(1+s)³, followed by log(1+s)<=s, gives the candidate's exp(z_new v) bound. Together with binomial(N,v)<=N^v/v! and v!>=(v/e)^v it yields E X_v<=N c_new rho_new^(v-1)/v³. Summing for integer v>J proves (NT) for integer J>=1. The proof only uses J=K, which is an integer. The file should say this explicitly rather than leaving the auxiliary threshold's domain implicit.

At N>=2^2048, L=ln N>1000. I rechecked m<=N/4, D>=3N/4, z_new<=L/4, Nx<=L exp(-L/3), and ln rho_new<=-L/24. The cutoff lower bound can be made self-contained: v0=floor(2L/ln L)<=L for L>=1000, so 2v0 ln(v0)<=4L and v0 is feasible; also v0>=L/ln L. Thus the same fixed top-level K works uniformly in m.

Finally L/(48ln L)>3, and the absorption of 2e N^(5/4) gives exactly

    eta(N)=exp[-(ln N)^2/(48lnln N)].

Taking ln N>=max(2048ln2,(48a)^2) proves eta(N)<=N^(-a) for any fixed a>0 without changing the algorithm, cutoff, or claimed resource exponent. The smaller length regime is essential. It does not repair the original full benchmark, which R2-O1 refutes for these policies.

## Fresh finite checks and boundaries

candidate_checks.py is separate from R3's code. It reconstructs exact connected counts from permutation/support-partition dynamic programming through v=5,m=8, then uses the anchor-vertex component recurrence for total bridge counts through N=24,m=8. The recurrence agrees with the direct small-group totals. Using exact rational arithmetic, all 370 fresh-pair ratio cells, 190 finite-genus sum cells, 10 component-genus majorant cells, and 31 normalized L(z) coefficient cells pass. candidate_checks.json preserves raw total counts, command, environment and commit.

The independent blind phase also checked the source genus-zero/one formulas through v=5,m=10. These finite checks are normalization/regression evidence; the all-parameter results rest on the proofs above. No sampling code was changed, so distributional Monte Carlo tests would not discharge an additional claim here.

m=0 and m=2 have zero truncation error. At N=2, K=2 and every even word is allowed; only m=0 satisfies the original sparse benchmark. Odd m has empty target. N=1 has only the empty word. The near-minimal branches h=0 and h=1 are explicitly retained. The positive conditional law is well-defined because repeated copies of one edge always give a B word when N>=2 and m is even.

No sequential multiplication or cache reuse is present, so the cached-prefix regression is inapplicable to these static counting claims. It remains relevant to any later adaptive sampler argument.

## Retained caveats and requested edits

1. Add S(N,k)=Z(N,2k)/(2k)! and integer J>=1 to the polished statistical proof. These are clarity/scope corrections; the main theorem already uses integer K.
2. Rename the frozen proof heading consistently with UPPER.v2 in its successor version, preserving this exact input and hash.
3. Keep sampler implementability and bit complexity conditional until the exact current decoder audit closes. Scalar Hurwitz numbers alone do not supply a decoder.
4. A range repair must state the original A/B refutation nearby. Neither obstruction nor positive-range result proves hardness or local Markov mixing.
