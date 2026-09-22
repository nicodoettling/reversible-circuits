# Load-bearing source audit — SRC-SB.v1

Coordinator reopened the primary DYZ PDF on 2026-09-22 during this run: https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf. Named obligation: verify the connected count recurrence and normalizations supporting component majorants. No broad literature search was performed.

Proposition 1, Eq(13), PDF page4 gives the positive recurrence for h(g,d). Section1.2, Eqs(19)–(20), PDF page5 identifies the disconnected exponential series and ordered transposition tuples, with degree-label factor d!. The genus-zero value immediately after Eq(28), PDF page7 is h(0,d)=d^(d-3)/d!. Consequently for a fixed labeled v-set, C(v,ell)=v! ell! h(g,v), ell=2v-2+2g. Connectivity is transitivity of the generated transpositions. Reversing all factors transfers product conventions while preserving identity and support.

Let F_v(t)=sum C(v,ell)t^ell/ell!, A_g(v)=C(v,2v-2+2g)/(2v-2+2g)!. Multiplying the source recurrence by v! yields

    v²(v-1)F_v = 2 sum_(a+b=v) binom(v,a) a b² (cosh(at)-1) F_a F_b.

This is a formal-series coefficient identity; none of the proofs needs convergence of the joint degree/genus series. The genus-zero coefficient gives A_0(v)=v^(v-3).

Coordinator rechecked the inherited majorant rather than taking its prior verdict on trust. With b_v=(v³-v)/36 and H_v=F_v/[v^(v-3)t^(2v-2)], the recurrence is a convex combination of L(at)H_aH_b, with L(z)=2(cosh z-1)/z². Coefficientwise L(z)<=exp(z²/12): 2/(2j+2)!<=1/(12^j j!), because the ratio for the next coefficient is 12(j+1)/[(2j+4)(2j+3)]<=1. Also b_v-b_a-b_b=abv/12>=a²/12. Induction proves A_g(v)<=v^(v-3)b_v^g/g! for every g>=0,v>=2. Singleton F_1=1 is separate. This is deterministic coefficientwise comparison; no posterior independence is asserted.

For the proposed obstruction only this counting input is load-bearing; the H0 g0/1 word decoder is not needed to bound the support of any sampler confined to A. For a positive extension using unchanged code, the old decoder and bit-complexity proof remain separate dependencies and are assigned to R4 for current audit.

The embedded-subgroup denominator has an elementary proof: for even positive m=2k, let p_k be the distribution of the all-transposition walk on S_r. Symmetry gives p_(2k)(id)=sum_g p_k(g)^2. The walk at time k lies in one parity class of size r!/2. Cauchy–Schwarz implies p_(2k)(id)>=2/r!, hence Z(N,m)>=Z(r,m)>=2 binom(r,2)^m/r! for 2<=r<=N. The statement excludes m0; r2 works exactly. This does not assume that a random support graph has independent edges.
