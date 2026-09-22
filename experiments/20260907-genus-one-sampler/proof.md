# Canonical connected sampler proof — S1.v2 (accepted)

Status: proved, accepted after current-version nonauthor proof and
implementation audits in roles/r2-structural/recursive_audit.md and
roles/r3-referee/candidate_audit.md. Core mathematics is the frozen R1-T1.1
derivation, unchanged. The coordinator checked the primary source, read the
complete arguments and reports, and reran the decisive exact checks in fresh
processes. The blind referee independently derived an alternative signed
coefficient DP before seeing R1. This is internal adversarial audit, not
external human certification; complete source reports are retained.

The theorem meets the unchanged user target T0 exactly: for every integer
N>=2 and b>=1 it returns a member of X_N with TV error zero, in expected bit
time O(N^10 log^3(N+1)) in the independent-fair-bit model. The implementation
uses an explicit work stack and needs no recursion-limit configuration.
The input model uses binary permutations on canonical labels [N] and exact
binary integer/rational arithmetic with independent fair random bits. Any
unbounded external vertex-name encoding cost is additional; T0 has canonical
labels. No unproved mixing, Hurwitz-classification or sampler assumption is
used. The final artifact consistency check is recorded separately.

Research entry points: `sample.py` (connected X_N and separately declared
restricted component assembly) and `roles/r1-recursive/sampler.py` (arbitrary
connected endpoint, g=0 or 1). Labels in Python are zero-based; the CLI
relabels output to [N]. Fixed PRNG seeds are diagnostic only; the theorem
uses ideal fair random bits.

The global consequence is separate: `global_consequence.md` proves the
conditional assembly law and exact omitted-mass accounting. A connected
sampler does not itself sample global Omega(N,2N).

---

# R1 recursive sampler proof, version R1-T1.1

Status: proved / accepted as canonical S1.v2 after the two nonauthor audits named above. The original worker's R1-T1.1 proof and provisional report remain frozen in its role directory as the exact review inputs. The core argument below is unchanged; its current certification status supersedes the historical provisional annotation.

## Frozen objects and theorem

For a finite nonempty labeled set V, a specified permutation sigma of V, and g in {0,1}, let F(V,sigma,g) be the ordered transposition words of length r=|V|+c(sigma)-2+2g, with product sigma and connected support graph on all V. Products act rightmost first. A graph on one vertex is connected, so F({v},id,0) contains the empty word and F({v},id,1) is empty. Let C_g(alpha) be its cardinality, where alpha lists the lengths of the individual cycles of sigma (including fixed points).

**R1-T1.** Every nonempty F(V,sigma,g), g in {0,1}, has an exact uniform sampler in expected bit time polynomial in |V|. In particular F([N],id,1)=X_N gives the frozen T0 for every N>=2 and every b>=1, with zero TV error. The resource variable is N, not log N. No Markov kernel or mixing assumption is used.

## External count dependency R1-C1

Direct primary source: Ravi Vakil, *Genus 0 and 1 Hurwitz numbers: recursions, formulas, and graph-theoretic interpretations*, dated July 3, 2000, https://math.stanford.edu/~vakil/files/g01hurwitz.pdf, Section 1.2, Corollary 1.5, and the positive expansion in the proof of Proposition 3.2.

Section 1.2 defines c^g_alpha as the number of transitive factorizations of a **fixed** permutation into r transpositions and states G^g_alpha=c^g_alpha/product(alpha_i). Thus these are ordered labeled words, with no division by r!, |V|!, conjugacy-class size, equal-cycle factorials, or cyclic shift. Our displayed counts are c, not the weighted cover counts G. Transitivity is equivalent to support connectivity because edge transpositions generate the product of symmetric groups on support components. Inverting/reversing all words, if necessary, translates action conventions bijectively; the recursion below directly uses the stipulated rightmost-first convention.

Write v=sum a_i, k=number of a_i, q(a)=a^a/(a-1)!, and Q(alpha)=sum_i a_i(a_i-1). Define

    S_j(alpha) = sum_{J subset [k], |J|=j} (product_{i in J} a_i)(sum_{i in J} a_i).

The positive count formulas are

    C_0(alpha)/r_0! = (product_i q(a_i)) v^(k-3),

    C_1(alpha)/r_1! = (product_i q(a_i))/24 *
      [v^(k-2) Q(alpha)
       + sum_{j=2}^k (j-1)! v^(k-1-j) S_j(alpha)].             (1)

Powers with negative exponents are exact rationals; v>=1. The genus-one expression follows from the positive graph expansion in Proposition 3.2, or algebraically from Corollary 1.5 using S_j=v e_j-(j+1)e_{j+1} and Q=v^2-v-2e_2. The latter telescoping identity is only a proof of (1); the sampler uses the nonnegative expansion, not cancellation as probabilistic weights. The q product is common to every allocation of a fixed list of cycles into two components.

For one singleton, (1) gives C_0=1 and C_1=0. For a single v-cycle, C_0=v^(v-2), agreeing with the elementary minimal-factorization count. For identity at v=2,3,4, C_1 gives 1,240,131040. These are checks of normalization, not its proof.

## Elementary genus bound R1-C2

For a connected word on v labels ending at k cycles, let J and S count, along its successive prefix products, the transpositions that join and split permutation cycles. Then J-S=v-k and r=J+S. Every transposition joining distinct current support components joins distinct current permutation cycles. Connectivity needs at least v-1 such support-component joins, so J>=v-1. Therefore r>=v+k-2 and r-(v+k-2)=2g with integer g>=0. This applies componentwise, including the zero-length singleton. Odd identity length is impossible by sign.

## Disjoint final-letter decomposition R1-C3

For r>0 choose the final transposition tau=(x y), with x<y, and put pi=sigma tau. A predecessor word u has length r-1 and product pi. Deleting one edge from the connected support graph leaves either one or two connected components.

1. If x,y lie in different cycles of sigma, pi has k-1 cycles and its cycle containing x,y forces them into the same support component of u. Hence u must be connected. Its genus remains g. The branch weight is C_g(type(pi)).
2. If x,y lie in one sigma cycle, pi splits that cycle into distinct cycles P and Q containing x and y respectively; every other cycle stays unchanged. A connected predecessor has genus g-1, so this branch exists only for g=1, with weight C_0(type(pi)).
3. In the same-cycle case, a disconnected predecessor has exactly two components A,B, with x in A and y in B. Each pi-cycle lies wholly in a component. P is forced into A, Q into B, and each other individual pi-cycle is assigned to one of them. If their genera are g_A,g_B, the length identity implies g_A+g_B=g. Conversely any such assignment, connected child words of those genera, and interleaving of their letters, followed by tau, reconstruct a valid parent word. For fixed assignment the number of words is

    W(A,B,g_A,g_B) = binom(r-1,r_A) C_{g_A}(type(pi|A))
                                    C_{g_B}(type(pi|B)),       (2)

    r_A=|A|+c(pi|A)-2+2g_A,   r_B=r-1-r_A.

There is no 1/2 factor: A is distinguished by x<y. Repeated cycle lengths still correspond to distinct cycle objects. Every output word determines tau, connected/disconnected status, the support components, their genera, the two child subsequences, and their position sets uniquely. Consequently this is a disjoint word-level decomposition and all its branch weights sum exactly to C_g(type(sigma)).

## Positive polynomial allocation DP R1-C4

Fix P,Q and g_A+g_B=g<=1. Let the cycle lengths after cutting be a list of K=k+1 positive integers with sum v. Assign P to A and Q to B. Some additional cycles may already be forced to A or B during sequential sampling; the others are free.

Let s be the total size of A and h its number of cycles. For each (s,h), aggregate over all allowed assignments:

    M[s,h] = number of assignments,
    Qsum[s,h] = sum Q(type(pi|A)),
    E[s,h,j] = sum e_j(type(pi|A)),
    S[s,h,j] = sum S_j(type(pi|A)).

Use E[s,h,0]=M[s,h]. These are integers. Start from the empty allocation with E[0,0,0]=1 and other entries zero. Process each individual cycle of length a. Assigning it to B copies all records without changing (s,h). Assigning it to A changes (s,h) to (s+a,h+1), with

    E'_j += E_j + a E_{j-1},
    S'_j += S_j + a S_{j-1} + a^2 E_{j-1},
    Qsum' += Qsum + a(a-1) E_0.                              (3)

Missing indices are zero. For a free cycle allow both choices; for a forced cycle only its allowed choice. Every transition and entry is nonnegative. There are O(v^3) scalar entries per layer and v layers, so O(v^4) integer operations and O(v^3) storage suffice. The loops range over sizes, cycle counts, and marker counts, not over partitions or subsets. Empty groups never occur because P,Q are forced to opposite sides.

Let t=v-s, h_B=K-h and L=r-1. Factorial cancellation in (2) leaves L! times the product of the normalized counts in (1). Thus multiply the following aggregated expressions by

    L! product_{all cut cycles} q(a_i):

    g_A=g_B=0: sum_{s,h} M[s,h] s^(h-3) t^(h_B-3),

    g_A=1,g_B=0: (1/24) sum_{s,h} t^(h_B-3)
        [s^(h-2) Qsum[s,h]
         + sum_{j=2}^h (j-1)! s^(h-1-j) S[s,h,j]].            (4)

For g_A=0,g_B=1, swap the roles of A and B in the DP. Equations (1)-(3) prove (4) equals the sum of the genuine nonnegative integer branch counts (2); therefore its final value is an integer, including zero for infeasible branches.

To sample an allocation, visit each free **labeled cycle** in a fixed order. Evaluate (4) with that cycle additionally forced to A and to B. Choose by their integer weights, then retain the choice. This sequential law is exactly W(A,B,g_A,g_B) divided by its total, by telescoping the nested partial-assignment sums. No marginal-independence or cached-prefix assumption is used: every weight is recomputed for the actual exposed assignment. At most O(v) allocation-oracle calls are made, not all 2^K assignments.

## Algorithm and per-word law R1-C5

    Sample(V,sigma,g):
      if |V|=1 and g=0: return empty word
      compute the connected and disconnected branches of R1-C3
      choose a branch by its exact integer count
      if connected:
        u <- Sample(V, sigma tau, indicated genus)
      else:
        sample cycle assignment with R1-C4 for selected (g_A,g_B)
        u_A <- Sample(A, (sigma tau)|A, g_A)
        u_B <- Sample(B, (sigma tau)|B, g_B)
        choose a uniform r_A-subset of [r-1]
        u <- interleave u_A,u_B in those positions, preserving orders
      return u followed by tau

Zero-weight branches are never selected. Sample a random integer in [0,Z) by drawing ceil(log2 Z) fair bits and rejecting values >=Z; acceptance exceeds 1/2 (Z=1 is deterministic). Uniform interleavings use the same exact integer primitive and ordinary binomial unranking. Every recursive call has smaller length; a split conserves the remaining total child length r-1. The recursion has exactly r positive-length nodes and at most |V| zero-length singleton leaves.

For any fixed parent word with a disconnected final-letter branch, multiply: selected branch mass D/C_parent; exact assignment mass W/D; child masses 1/C_A and 1/C_B; interleaving mass 1/binom(L,r_A). By (2) this equals 1/C_parent. For a connected branch it is (C_child/C_parent)(1/C_child)=1/C_parent. The disjoint reconstruction proves this is the full word probability, with no omitted preimages or extra multiplicity. Induction proves exact uniformity and exact support, product and length. This is an exact conditional-probability identity, not a product of unconditional accuracy estimates.

## Bit complexity R1-C6

Let N be the original degree. Every recursive degree is <=N and every length <=2N. Each positive node scans O(N^2) transpositions, each using at most O(N^4) arithmetic operations for (4), plus O(N^2) for the direct count formula. Sampling the selected cycle assignment requires at most O(N) further O(N^4) evaluations, dominated by O(N^6) per node. There are O(N) nodes, so O(N^7) exact arithmetic operations suffice, without memoizing an exponentially growing inventory of endpoints or cycle subsets. Polynomial storage suffices; DP layers may be discarded after each oracle call.

The DP coefficients sum at most 2^N allocations, each with at most 2^N marked subsets, products bounded by N^N, and marked sums <=N; hence have O(N log(N+1)) bits. Formula powers have exponent at most N and the only negative exponents are >=-2 on each component size (>=-1 in the genus-one factor). The product of the (a_i-1)! denominators divides N!. Every rational summand's denominator therefore divides 24(N!)^5, a uniform integer of O(N log(N+1)) bits. All terms are nonnegative, their magnitudes and sums are at most exp(O(N log(N+1))), and reduced rational intermediates consequently have O(N log(N+1)) bits. The completed branch counts are integers bounded by binom(N,2)^(2N), with the same bit bound. Standard exact arithmetic therefore gives a polynomial bit bound; allowing O(B^3) bit operations for a reduced-rational operation on B-bit operands gives the conservative O(N^10 log^3(N+1)) bound, plus polynomial expected fair-bit work. The theorem only needs an expected polynomial bound; no dependence on b is necessary for the exact sampler.

## Dependencies, first gap, and exclusions

Load-bearing external dependency: the specified Vakil count formulas and their fixed-permutation normalization, checked directly against the primary source. Everything after R1-C1 is elementary combinatorial disintegration and dynamic programming. Exact executable validation of R1-C4/C5 is recorded in roles/r1-recursive/report.md and roles/r1-recursive/results.json. The complete nonauthor reviews in roles/r2-structural/recursive_audit.md and roles/r3-referee/candidate_audit.md accept the mathematical argument, bit bound, repaired explicit-stack implementation, and integrated sampler. No mathematical completion lemma remains missing for g<=1 under the checked published count theorem. This does not give a general arbitrary-genus sampler, a prescribed exposed-prefix connectivity oracle, all-length global sampling, a local-chain gap, or polynomial complexity in log N wires.

Historical failures retained: adjacent-square insertion omits (ab)^3 and its tree extensions; scalar identity counts alone do not decode words; ordinary prefix permutation does not encode the needed support joining; fixed genus does not bound the number of endpoint partitions polynomially. This construction uses none of those implications. The recorded tests cover these examples, all singleton/length/parity boundaries, and complete small-case per-word probabilities; the audit reports preserve their precise finite domains.
