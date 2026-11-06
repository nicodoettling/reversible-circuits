# Theorem-only packet: M-GROW.v1 and fixed-genus specialization

Determine whether the following mathematical statement is true, false, or requires a missing hypothesis. Do not assume a verdict from its presentation. Provide a full argument or exact obstruction. This packet contains definitions, quantified statement and explicit allowed input, not the candidate proof.

Let Omega(N,m) be the ordered length-m words in all transpositions of S_N whose product is identity. Labels [N] and positions are distinguished; maps compose rightmost first. For N>=2 and even m>=0, U_(N,m) is uniform on this finite set. Every nontrivial support component B has v>=2 vertices and a restricted subword of even length ell=2v-2+2g; g>=0 is its genus. Isolates have v=1,ell=0. No Markov kernel is defined.

Set P=N+m+2 and L=max{1<=v<=N:3^v<=P^4}, fixed once using the original input. For integer G>=0, let E_(G,L) be the event that every nontrivial support component satisfies g<=G OR v<=L.

Statement: for every integer j>=64, N=2^(8j), m=2^(6j), and every integer0<=G<=2^j,

    U_(N,m)(E_(G,L)) <= 2^(-1-jm/2).

Hence any probability law Q supported on E_(G,L) has TV distance at least1-2^(-1-jm/2) from U_(N,m). The claimed fixed-G corollary has threshold j>=max{64,ceil(log_2(max{1,G}))}; the G=2 specialization is included. No claim of impossibility for all polynomial samplers or of a Markov-chain gap is part of the statement.

Allowed published count input: Dubrovin–Yang–Zagier, Classical Hurwitz numbers and related combinatorics, revised manuscript, Proposition1 Eq(13), Section1.2 Eqs(19)-(20), and genus-zero value following Eq(28). URL https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf . The project uses C(v,ell)=v!ell!h(g,v) for fixed labeled connected identity words, ell=2v-2+2g. A primary-source check may retain or challenge that convention translation explicitly. Elementary identities and independent derivations are allowed. Other role proofs/reports and the candidate argument are excluded until this report is frozen.

Boundary obligations: odd m, m=0,m=2,N=2, singleton positive genus, negative genus, and minimal connected components. State whether any lies inside the displayed quantified sequence. Treat a conditional bridge normalizer explicitly; an unconditioned support-graph model is not the declared law. Give all dependencies and the first unresolved implication if any.
