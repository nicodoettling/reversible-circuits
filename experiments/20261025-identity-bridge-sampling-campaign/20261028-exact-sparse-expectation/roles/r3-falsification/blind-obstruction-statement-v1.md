# Theorem-only packet: EC-OBSTR.v1

Determine whether the following statement is true, false, or requires a missing hypothesis. This packet contains no candidate proof or verdict.

For every integer j>=64, let N=2^(8j),m=2^(6j),J=2^(3j). Let U_(N,m) be uniform on ordered length-m words in all transpositions of S_N with identity product. Labels and positions are distinguished, maps compose rightmost first. Let Vmax be the largest nontrivial support-component size and H9=sum over all nontrivial support components B of9^|B|.

Claim:

    P_U(Vmax<=J)<=2^(-1-jm/2),
    E_U H9>=9^(J+1)[1-2^(-1-jm/2)].

Consequently E_U H9 is not bounded by one polynomial in N,m on this sequence. This statement concerns the explicitly defined exponential cost statistic, not actual optimized sampler runtime or general sampling impossibility. No Markov kernel is part of its model.

Allowed primary count source: Dubrovin–Yang–Zagier, Classical Hurwitz numbers and related combinatorics, revised manuscript, Proposition1 Eq(13), Section1.2 Eqs(19)-(20), genus-zero value following Eq(28). URL https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf . C(v,ell) denotes fixed-labeled connected ordered identity words, ell=2v-2+2g. Elementary independent counting arguments are allowed. Candidate proofs and their verdicts are withheld until this report is frozen.

Boundary obligations: identify whether odd m,m0,m2,N2,singleton positive genus or negative component genus enter the displayed quantified sequence. State all source dependencies and the first unresolved implication if any. Use the exact bridge law, including its normalizer.
