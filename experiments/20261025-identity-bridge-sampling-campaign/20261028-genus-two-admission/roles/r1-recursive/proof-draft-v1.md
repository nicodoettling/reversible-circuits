# Positive recursive connected genus-two sampler — candidate R1-T2.v1

Draft 2026-10-28. Status PROVISIONAL, not accepted. Exact target is frozen in statement-v1.md. Every claim below is a proposed proof; coordinator blind and nonauthor review remain outstanding. The main global mission remains OPEN.

## 1. Objects and inherited inputs

Let V be a nonempty canonical label set of size v, sigma a permutation with k individual cycles, and g∈{0,1,2}. F(V,sigma,g) consists of ordered transposition words of length r=v+k−2+2g, rightmost-first product sigma, whose support graph on all V is connected. Define Cg(alpha)=|F| where alpha=(a1,…,ak) lists cycle lengths, including fixed points. Distinct cycles remain distinct objects even if their lengths agree. Singleton genus0 has one empty word; singleton positive genus has no words.

Write q(a)=a^a/(a−1)! and Q(alpha)=∏q(ai). Put Bg(alpha)=Cg(alpha)/(r! Q(alpha)). The inherited exact count inputs, from canonical S1.v2 and its complete nonauthor audits, are

    B0(alpha)=v^(k−3),
    B1(alpha)=1/24 [v^(k−2) Σ_i ai(ai−1)
             + Σ_{j=2}^k (j−1)! v^(k−1−j) S_j(alpha)],

where S_j=Σ_{|J|=j}(∏_{i∈J}ai)(Σ_{i∈J}ai). Negative powers are exact rationals, v>=1. The support/genus inequality follows directly by counting cycle joins and splits: every connected support needs at least v−1 support joins, each a permutation-cycle join, giving r>=v+k−2 with matching parity. No Hurwitz transitivity theorem or mixing theorem is used.

## 2. Exact external source and normalization (R1-C2)

The new count input is I. P. Goulden and D. M. Jackson, *The Number of Ramified Coverings of the Sphere by the Double Torus, and a General Form for Higher Genera*, J. Combinatorial Theory A88(1999),259–275, Theorem1.1, equations(1)–(3),(6); [primary PDF](https://uwaterloo.ca/math/sites/default/files/uploads/documents/gjjcta1999-2.pdf). Its Section3 Lemma3.1 and Corollary3.2 provide a separate extraction check. This draft imports that published theorem rather than reproving its symbolic cut-and-join verification.

The normalization is explicitly pinned in the predecessor paper which the double-torus introduction says supplies its notation: Goulden–Jackson, *A proof of a conjecture for the number of ramified coverings of the sphere by the torus*, [arXiv:math/9902009](https://arxiv.org/pdf/math/9902009), Section2 (PDF page2), and Section3 equation(2). For every genus it states μ_m^(g)(alpha)=|Class_alpha| Cg(alpha)/v!, where Cg counts ordered transitive factorizations of a fixed permutation. Therefore μ=Cg/z_alpha, with

    z_alpha=∏_{i=1}^k ai · ∏_{a>=1} m_a!,

m_a being the number of size-a cycles. There is no extra branch factorial beyond the r! in the generating series. These are weighted cover numbers: the relation, not a naive unweighted-cover interpretation, handles the degree2 automorphism case. Transitivity equals support connectivity because edge transpositions generate a symmetric group on each support component. Opposite displayed composition conventions are related by reversing the word and inverting the endpoint; inversion preserves cycle lengths. Our constructive recursion directly fixes rightmost-first products.

In source notation,

    ψ_j(z,p)=Σ_{a>=1} a^(j−1) q(a) p_a z^a,
    s=x exp(ψ_0(s,p)),
    H2(x,p)=Σ_alpha C2(alpha)/(r! z_alpha) p_alpha x^v
            = [Q3/(1−ψ1)^3+Q4/(1−ψ1)^4+Q5/(1−ψ1)^5]/5760,
    Q3=5ψ4−12ψ3+7ψ2,
    Q4=29ψ2ψ3−25ψ2²,
    Q5=28ψ2³,

with ψ evaluated at s. These are source formulas, not new claims.

Introduce one indeterminate yi per actual endpoint cycle and substitute

    p_a=(a/q(a)) Σ_{i:ai=a} yi.

Only the original monomial p_alpha can contribute to y1…yk. Its polarization factor is (∏m_a!)(∏ai/Q(alpha)). Consequently

    [x^v y1…yk] H2 = C2(alpha)/(r! Q(alpha)) = B2(alpha).

This explicitly cancels repeated-cycle factorials without identifying the cycles. Under substitution ψ_j(z,p)=Σ_i ai^j yi z^ai, including ψ0=Σ yi z^ai.

Apply the formal-residue substitution x=z exp(−ψ0(z,p)). Since dx/x=(1−ψ1(z,p)) dz/z, for v>=1 and the rational formal series R appearing above,

    [x^v] R(ψ(s))=[z^v] R(ψ(z))(1−ψ1(z,p)) exp(v ψ0(z,p)).

This is formal Lagrange inversion; all denominators have constant term1. After selecting y1…yk, the z-degree is automatically Σai=v. Thus erase z and put L_j=Σ_i ai^j yi. We obtain

    B2(alpha)=[y1…yk] exp(v Σyi)/5760 ·
      [(5L4−12L3+7L2)/(1−L1)^2
       +(29L2L3−25L2²)/(1−L1)^3
       +28L2³/(1−L1)^4].                         (A)

## 3. Positive cycle markers

For a positive integer a define

    A(a)=a²(a−1)(5a−7),  B(a)=a²,  D(a)=a²(29a−25).

All are nonnegative; A(1)=0, while A(a)>0 for a>=2. Equation(A)'s three numerators become respectively Σ A(ai)yi, (Σ B(ai)yi)(Σ D(ai)yi), and28(Σ B(ai)yi)^3. This regrouping removes all signed arithmetic.

For a list of d labeled special weight functions w=(w1,…,wd), define

    M_j(alpha;w)=[u^j z1…zd] ∏_{i=1}^k
                  (1+ai u+Σ_{l=1}^d wl(ai) z_l).             (B)

Special slots are labeled, even when all wl=B. A cycle can be unmarked, an ordinary mark of weight ai, or occupy exactly one special slot. Thus M_j sums over injective assignments of cycles to special slots and a disjoint j-subset of ordinary marks. In particular M_j=0 when j+d>k.

The coefficient of ∏L_weight in (1−L1)^−e exp(vΣyi) equals

    Σ_{j=0}^{k−d} (e)_j v^(k−d−j) M_j(alpha;w),            (C)

where (e)_j=e(e+1)…(e+j−1), (e)_0=1. Indeed denominator expansion contributes binom(e+j−1,j), assigning its j ordered L1 factors contributes j!, and the remaining distinct unmarked variables contribute v each from the exponential. No factorial remains for special slots: their labeling in(B) already supplies the correct multiplicity.

Combining(A)–(C) gives the positive genus-two count identity

    B2=1/5760 {Σ_j (2)_j v^(k−1−j) M_j(alpha;A)
              +Σ_j (3)_j v^(k−2−j) M_j(alpha;B,D)
              +28Σ_j (4)_j v^(k−3−j) M_j(alpha;B,B,B)}.     (D)

Each sum stops at k−d. All exponents in(D) are nonnegative. For alpha=(1), every term vanishes; for alpha=(1,1), only the two-slot term contributes M0=8, giving C2=6!*8/5760=1; for alpha=(1,1,1), the coefficient is312/5760 and C2=2184. These hand checks are normalization regressions, not the proof.

The inherited genus-one expression also uses the same markers. Put q1(a)=a(a−1). Then M0(alpha;q1)=Σq1(ai), and

    M_j(alpha;B)=S_{j+1}(alpha).

The identity follows by selecting which of the j+1 marked cycles is the special slot. Hence

    B1= [v^(k−2) M0(alpha;q1)
          +Σ_{j=1}^{k−1} j! v^(k−2−j) M_j(alpha;B)]/24.    (E)

The smallest exponent here is−1, and B0 has smallest exponent−2. This marker reexpression does not change S1's accepted count.

## 4. Final-letter decomposition (R1-D2)

Let r>0, final transposition τ=(x y), x<y, and π=στ. A predecessor word u has product π and length r−1. Deleting the final edge from connected support leaves one or two support components.

If x,y lie in different sigma cycles, π merges those cycles. Its merged cycle forces both endpoints into the same predecessor support component, so u is connected and has genus g. Branch weight: Cg(type π).

If x,y lie in the same sigma cycle, π splits it into P containing x and Q containing y. A connected predecessor has genus g−1 (possible only when g>=1), with count C_(g−1)(type π). A disconnected predecessor has exactly two components A containing P and B containing Q; every other individual π-cycle is assigned wholly to one side. If the child genera are ga,gb, then ga+gb=g. At g2 the three possibilities are(0,2),(1,1),(2,0). For fixed assignment,

    W=binom(L,rA) Cga(alphaA) Cgb(alphaB),
    rA=|A|+c(π|A)−2+2ga,
    rB=|B|+c(π|B)−2+2gb,
    L=rA+rB=r−1.                                        (F)

Conversely each pair of connected child words and order-preserving interleaving, followed by τ, reconstructs a parent. Every literal parent recovers τ, its predecessor support components, genera, subsequences and interleaving positions uniquely. A is anchored by x<y, so no factor1/2 occurs. Thus all branches are disjoint and exhaustive. This argument uses neither a canonical normal form nor a proposal-rejection correction.

## 5. Arbitrary forced allocation oracle (R1-A20 and R1-A11)

Let K=k+1 cut cycles have positive lengths summing to v, with P forced to A and Q to B. Any further individual cycles may be forced to either side. At each stage, the unforced cycles remain actual labeled objects. Write s=|A|, h=c(π|A), t=v−s and K−h=c(π|B). The anchored cycles imply s,t>=1.

Factorial cancellation in(F) gives

    W=L! Q(all cycles) Bga(alphaA) Bgb(alphaB),
    L=v+K−4+2(ga+gb).                                  (G)

Each Bg is a sum of a constant number of nonnegative marker specifications from(D),(E), or B0. For one selected specification on each side, process cycles one at a time with integer table

    T[s,h,jA,maskA,jB,maskB].

A mask records which labeled special slots have been filled. Initialize T[0,0,0,0,0,0]=1. For a cycle of size a, allow its forced side only, or both sides if free. A-side placement adds a to s and1 to h; B placement leaves s,h unchanged. On the selected side choose one of: unmarked, multiplier1; ordinary marked, increment j and multiplier a (only where its specification permits ordinary marks); or one not-yet-filled special slot l, set its bit and multiply by wl(a). Other coordinates do not change. Sum entries with the same key. This is exactly multiplication of(B) plus the A/B allocation indicator, proved by induction on processed cycles. Every transition is nonnegative.

At the end retain full masks. Multiply each entry by the two scalar coefficients in(D),(E), or B0 evaluated at(s,h) and(t,K−h), then sum over keys/specifications and multiply by L!Q. The result is precisely the sum of(F) over all assignments respecting the forcing. The final answer is therefore a nonnegative integer; a zero child fiber contributes zero exactly.

For(1,1), the two sides each have at most one special slot. This table is the tensor product of the two genus-one marker transitions, with common allocation size/count. It retains cross-moments rather than multiplying marginal sums. For(2,0), at most three special slots occur, all on the genus-two side. No subset enumeration is used. The reference audit may enumerate small subsets solely to falsify the compressed production oracle.

To sample an assignment, visit free cycle indices in a fixed order. With current forced map H, compute exact masses Z(H∪{i→A}) and Z(H∪{i→B}), whose sum is Z(H), and choose by their ratio. Zero extensions have probability0. Telescoping these actual history-conditional masses yields probability W/Z(initial) for every assignment. This explicitly tracks every posterior normalizer; it does not multiply marginal bounds, assume local independence after conditioning, or reuse an invalid cached prefix.

## 6. Exact sampler and word law (R1-W2)

At a valid positive fiber compute all final-edge connected and split branch masses and choose a branch by those integers. For a connected branch recurse on its endpoint/genus, then append τ. For a split branch sample its assignment with Section5, recurse on the two labeled children, choose a uniform rA-subset of[L] and interleave in those positions, then append τ. Use sorted canonical child labels and relabel edges back. Singleton g0 is the empty base, and all zero input fibers are rejected.

An explicit continuation stack avoids an interpreter recursion-depth assumption. Every positive call removes one output letter; split child lengths sum to its predecessor length. Hence exactly r positive calls occur, with at most v zero-length singleton leaves.

For a fixed parent word in a split branch with aggregate branch mass Z, its probability is

    (Z/Cparent) · (W/Z) · (1/CA) · (1/CB) · 1/binom(L,rA)
    =1/Cparent

by(F). Connected branches cancel as(Cchild/Cparent)(1/Cchild). Unique reconstruction and induction establish exact uniformity over the full connected fixed-endpoint fiber, exact endpoint, support and length. No independently uniform support graph is sampled, so the historical graph-weight bias is not reintroduced.

An integer U uniform on[0,Z) is obtained from ceil(log2 Z) independent fair bits with rejection of values>=Z; acceptance is greater than1/2, and Z=1 is deterministic. Weighted categories use cumulative exact integer weights. Uniform interleavings use binomial unranking and the same integer primitive. Exactness is an ideal fair-bit theorem; seeded pseudorandom draws are diagnostics only.

## 7. Bit complexity (R1-B2)

Let n be the original degree. All child degrees are<=n, all lengths<=2n+2, and g never increases. A tensor allocation table has O(n^4) scalar entries: s,h,jA,jB each have O(n) possibilities, and the total special-slot mask size is bounded by a constant (at most3 slots at total genus<=2). There are O(n) cycle layers and a constant number of specifications. Therefore each arbitrary forced allocation query uses O(n^5) integer operations and O(n^4) space. A direct count needs only the single-side O(n)-by-constant marker table and O(n) layers; its operation cost is smaller.

One positive recursion node examines O(n²) candidate transpositions and at most three genus pairs per edge, plus O(n) additional oracle calls to sample the chosen assignment. This costs O(n^7) arithmetic operations. The total of O(n) positive nodes gives O(n^8) operations. Bounded-capacity caches are optional; no exponentially large collection of endpoint profiles or subsets is retained.

Each processed cycle has at most a constant number of side/mark choices and weight at most O(n^4). Thus every integer table entry is bounded by c^n n^(4n), giving O(n log(n+1)) bits. Rising factorials, factorials up to(2n+2)!, positive powers with O(n) exponent, q-products and sums share this bit order. The product ∏(ai−1)! divides n!. Only B0 and B1 introduce negative powers, at worst−2 and−1 per nonempty side; under total genus<=2 the total negative exponent magnitude is at most4. A safe common denominator for every allocation summand is

    5760² (n!)^5.

It has O(n log(n+1)) bits. All entries and summands are nonnegative and total magnitudes remain exp(O(n log(n+1))). Reduced rational intermediates therefore retain O(n log(n+1)) bits. Charging O(B³) bit operations for B-bit reduced-rational operations gives the conservative expected O(n^11 log³(n+1)) bound. Fair-bit rejection has bounded conditional expected trials for every current history; linearity of expectation over polynomially many logical choices completes the expected bit bound. No accuracy dependence is needed, so every b>=1 is met with TV error0.

## 8. Dependency graph, boundaries and falsification

Dependencies: accepted-inherited S1 count formulas + elementary genus inequality -> genus0/1 markers and final-letter classification. New primary GJ1999 theorem + explicitly pinned μ-to-C normalization + formal Lagrange inversion -> positive formula(D). Formula(D) and(E) -> forced allocation identities(A20,A11). Final-letter classification + allocation + fair-bit exact choices -> word law. Marker size and denominator bounds -> polynomial bit time.

First unproved step before external review: no internal mathematical gap is presently identified in this proposed derivation, but source translation, compressed allocation implementation, full forward law and complexity await the declared checks and fresh reviews. This status is PROVISIONAL, not accepted. There is no claimed arbitrary-genus extension.

Boundary obligations: odd identity length has zero fibers by sign; m0 is the global empty word but is connected only on a singleton; m2 connected requires v2 and is the unique repeated edge; v2 has one feasible word for every endpoint/parity and g0,1,2; singleton positive genus vanishes in the marker formulas. Minimum connected lengths are g0 and use the inherited formula. Every root/child zero mass is rejected or assigned probability0. Equal cycle lengths are polarized into distinct yi; child labels and interleaving positions are preserved.

Retained historical counterexamples: adjacent-square insertion misses(ab)^3 and its extended zero-square fibers; the S3 transposition endpoint at length5 has81 total words and80 connected; uniformly chosen support graphs have wrong literal-word weights; fixed genus does not make endpoint partition inventories polynomial; cut forgetting requires actual representation multiplicities; fixed-top-level support policies need bridge normalization; CP-1 refutes multiplication of marginal lightness bounds. None is used as a valid inference here. This construction instead supplies full forced masses and the exact per-word cancellation.

Finite checks are specified in audit-v1.py and require coordinator reservation. They can falsify the formulas/law but do not replace the all-v proof. Final results and hashes will be frozen in report-v1.md and manifest-v1.json.
