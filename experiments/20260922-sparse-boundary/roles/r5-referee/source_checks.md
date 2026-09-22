# Primary-source checks (blind phase)

Accessed 2026-09-22 through the web tool. No other role artifacts read.

1. Ravi Vakil, *Genus 0 and 1 Hurwitz numbers: recursions, formulas, and graph-theoretic interpretations*, July 3, 2000 version, https://math.stanford.edu/~vakil/files/g01hurwitz.pdf. Section 1.2 defines c^g_alpha as ordered transitive factorizations of a fixed permutation and states G^g_alpha = c^g_alpha / product(alpha_i). Corollary 1.5 gives the genus-zero and genus-one formulas. For alpha=[1^v], c=G, length=2v-2+2g, and e_j(alpha)=binomial(v,j). Thus, writing c(v,ell) for connected identity-word counts on fixed labeled vertices:

   c(v,2v-2)=(2v-2)! v^(v-3),

   c(v,2v)=(2v)! v^(v-2)/24 * [v^2-v-sum_(j=2)^v v^(2-j)(j-2)! binomial(v,j)].

   In particular both normalized coefficients c(v,ell)/(v! ell!) are at most e^v. This is the only literature input needed in the independent proof. The conversion preserves ordered positions and fixed vertex labels; the factorial v! enters only through the component assembly, not in c itself. Word reversal removes any left/right product-convention ambiguity for identity factorizations.

2. Dubrovin--Yang--Zagier, *Classical Hurwitz numbers and related combinatorics*, https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf. Inspected Section 1.2, equations (19)--(20) and the following character formula: d! H*_(k,d) counts all ordered identity words. This corroborates the labeled normalization; its character formula and positive recurrence are not used in the proof or claimed to give a decoder.

Independent check: finite_checks.py aggregates all permutation/support-partition states for v=2,...,5 through length 2v. Both formulas agree exactly, with all labels and positions included. This check can refute normalization errors but does not prove the source theorem.
