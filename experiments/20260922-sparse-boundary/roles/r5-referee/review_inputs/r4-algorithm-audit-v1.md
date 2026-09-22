# R4 algorithm dependency audit — ALG.v1

Status: ACCEPT for the all-even-length exact H0/H1 law and stated coarse
resource envelope, subject to the already named published count and H0-only
genus-zero/one dependencies. This is a nonauthor current-input algorithmic
audit, not a new audit of the analytic tail, and not external human review.
Reviewed bytes are preserved by algorithm-audit-input-hashes.json.

## Precise question answered

The proposed positive extension uses exactly the frozen H0/H1 algorithms
at every even m <= (1/4) N^(2/3) ln N, with N>=2^2048 and error
exp[-(ln N)^2/(48 ln ln N)]. Does algorithm correctness or its expected
O(P^20) bit-time / O(P^10) bit-storage bound require the earlier
m^3<=N^2 range? **No.** The exact restricted law and complexity apply to
every even m>=0, N>=2. Only the old analytic omitted-mass theorem had the
smaller length restriction. Therefore the proposed analytic extension
can reuse these algorithmic conclusions unchanged.

This audit does not accept that displayed eta or length range by itself.
Their proof is owned by the analytic workers. They are recorded to bind
this dependency review to the exact theorem under discussion.

## Law and resource audit

1. The top-level cutoff is K=max{v<=N:v^(2v)<=P^4}, P=N+m+2. Source
   computes it once. Every allowed-component predicate and assembly cell
   closes over the same cutoff. No residual instance can shrink it.
   All even high-genus components on v<=K remain eligible.
2. The small-support completion memo uses (remaining,p,pi), including the
   actual permutation and exposed support partition. Its terminal test
   requires BOTH p=id and one support block. Its only pruning requires
   blocks(pi)-1<=remaining. Both statements hold at arbitrary length.
   Explicit-stack dependencies strictly decrease remaining, so ell>1000
   introduces no interpreter recursion assumption.
3. At degree v, at most v!Bell(v)<=v^(2v)<=P^4 states occur per remaining
   length. Across all v<=K and r<=m there are at most
   Q=(m+1)K P^4<=P^6 keys. The important length factor is present in the
   actual proof and source. Values count literal suffixes, hence use
   O((m+1)logP) bits. Keys use O(Klog(K+1)+log(m+1)+1) bits.
4. A pending DFS depth can have O(K^2) siblings, with depth at most m.
   Duplicate memo tasks are skipped. Each distinct key is expanded and
   finished at most once: a same-remaining pending sibling cannot be a
   descendant since remaining strictly decreases. The total transition
   work and stack space are polynomial with no genus bound.
5. Charging each dictionary access a linear scan over Q keys yields the
   displayed O(Q K^2[Q D+Klog(K+1)+B]) coarse bound. With Q<=P^6 and
   B,D=O(P^2), it is O(P^16); the proof's extra O(P^2) bookkeeping reserve
   and P^20 envelope are adequate. Memory Q(B+D) plus stack is below P^10.
   This uses standard exact bit arithmetic, not unit-cost huge integers.
6. H0's other branch calls the imported genus0/1 decoder only when
   ell=2v-2 or2v. Its per-component O(v^10log^3(v+1)) bound is therefore
   unaffected by the global m. Component degrees sum to at most N.
   Fixed-capacity caches (8192 count,256 branch cache), explicit work stack,
   allocation DP and saved child words fit the recorded polynomial storage.
   H1 never invokes nontrivial g0/1 formulas or decoding; shared random
   integer/subset utilities are elementary.
7. Positive connected-count and assembly tables have O(N^2(m+1)^2)
   arithmetic operations, including infeasible cells. Counts and positive
   numerators use O((m+1)logP) bits up to polynomial factors. Binomial and
   cutoff-power intermediates stay polynomial in P. This remains true
   without m<=N or m<=2N. No unbounded-genus table entry is omitted.
8. Assembly selects least-label component size/length by exact counts,
   its other labels and positions uniformly, and its connected word
   exactly. The cancellation law telescopes to1/Z_allowed for every
   literal output. No family of unproved conditional independence bounds
   is multiplied. Count recurrence alone is never called a decoder.
9. Both sets are nonempty at every even m because K>=2 and one repeated
   edge is permitted at every positive even length. The random integer
   rejection has fewer than two expected attempts. m0, m2, N2, empty
   N1 positive-length and odd-length cases are explicitly handled.
10. The v4 code repairs output predicate labels while preserving sampling
    logic, and uses a lossless hex fallback for huge CLI certificates.
    It does not change interpreter settings or invoke a decimal-only
    output assumption. Existing CLI-digit and policy-label regressions
    remain part of the inherited artifact acceptance.

## Dependency closure and limitations

Imported published dependency C: DYZ Proposition1 Eq13 and the word-count
normalization in Section1.2 Eqs19–20. Imported H0-only dependency G01:
September7 S1.v2 exact literal decoder using Vakil Section1.2, Corollary1.5
and the positive graph expansion. This review reads their frozen project
proofs and implementations and confirms the algorithmic interfaces; it
inherits the earlier explicitly recorded primary-source checks rather
than claiming a new line-by-line source verification.

No Hurwitz transitivity, mixing theorem, approximation oracle, independence
of random support edges, or work bound in logN wires is imported. Counting,
literal decoding, and global omitted mass remain three distinct obligations.

No unchanged sampler code was rewritten. The independent QC construction
is in this role directory and is not needed by the proposed log extension.

Relevant preserved regressions: same endpoint/different support history;
fixed top K at (42,12) versus residual(5,12); v2,length1400 explicit stack;
nonzero omitted mass within the old range; CLI huge integer serialization;
policy-specific target descriptions. Their historical exact evidence is
recorded in the reviewed R4 sampler_review-v3.md and project registry.

## Canonical integration check, ALG-INT.v1

Reviewed root proof.md SHA256
b55b299fd1331d2ce0d5dcb44930cdf8d9f483e4352c8bc7d6aaecae92ecdff1.
Section6 states the exact assembly, original-cutoff rule, support-history
suffix state, conditional-law cancellation, and all-even-length resource
scope consistently with ALG.v1 and the frozen source. Section3 imports
these algorithm conclusions without changing them to an accuracy-dependent
algorithm. The source and wrapper hashes match their prior frozen records.
H1's avoidance of the nontrivial g0/1 dependency is correctly distinguished.
ACCEPT this exact algorithmic integration; analytic sections retain their
separate reviewer obligations. No source or proof repair requested.
