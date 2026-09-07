# Sampling Complexity Across Bridge Lengths

Status: final synthesis; classification `quantified-phase-diagram`. All bounds concern
uniform transposition bridges and exact output endpoints, not mixing of a
chain on words. All three role reports are final; both reciprocal fresh audits accepted.

Let `b=ceil(log2(1/epsilon))`, `M_d=binom(d,2)`, and for N≥5 define

```
q(N,m)=floor(m/[2N(N−1)]),
D_eps(N)=2N(N−1) ceil(144 ln(3N²/epsilon)),
R(N,m)=m⁴/[48(N−m+1)²]  (even 2≤m≤N).
```

For every fixed constant A, short exact sampling is polynomial on
`m≤A(log N)²`; its degree can depend on A. More precisely, its all-input
bound is `exp(O(sqrt(min{m,N}))) poly(N,m)`. The partition factor is not
polynomial for general variable m. All polynomial exact samplers below use
expected running time with fair random bits. R1 also gives a bounded-time
approximate implementation with exact endpoint and tunable epsilon.

## Global public target

| regime | sampler | exact/approximate | runtime | TV error | status | missing primitive |
|---|---|---|---|---|---|---|
| m=0 | Empty word | exact | O(1) output | 0 | proved | none |
| Odd m | Identity fiber empty | no sampler requested | parity check | n/a | proved | none |
| m=2,N≥2 | Uniform edge repeated twice | exact | poly(log N) expected bit time | 0 | proved | none |
| N=2, even m | Unique edge repeated m times | exact | O(m) output | 0 | proved | none |
| N=1 | Only m=0 feasible | exact/empty | constant | 0 on singleton | proved | none |
| All feasible lengths, parameterized by min{m,N} | Positive defect-type DP and labeled lift | exact | exp(O(sqrt(min{m,N}))) poly(N,m) | 0 | proved; fresh audit accepted | remove partition-state factor for general inputs |
| m≤A(log N)² for fixed A; also min{m,N}=O(log²(N+m)) | Same defect-type DP | exact | poly(N,m), degree depends on fixed regime constant | 0 | proved; fresh audit accepted | none in stated regime |
| Fixed N, every even m | Full type DP / finite-state bridge DP | exact | poly(m), constant depends on N | 0 | proved | no uniform poly(N,m) bound from fixed-N enumeration |
| even 2≤m≤N with R(N,m)≤epsilon | Minimal-component assembly and DPS | approximate global; exact within declared subset | O(N²m²) polynomial-bit integer arithmetic plus polynomial DPS reconstruction | ≤R(N,m) | proved; independently audited incidence bound | none in stated accuracy regime |
| Any (N,m) with Z0>0 and 1−Z0/Z≤epsilon | Same minimal-component sampler, exact mass certificate | approximate | poly(N,m); exact certificate arithmetic | exactly 1−Z0/Z | proved | none for inputs passing certificate |
| N≥5, feasible even m, q≥4ceil(log2 N) | Density-parameterized retained-rank recursion | approximate | O(N⁴m³) exact arithmetic on polynomial-bit operands | ≤min(1,3N² exp(−q/144)) | proved; fresh audit accepted | smaller requested error at fixed (N,m) |
| N≥5, feasible even m≥D_eps(N) | Same dense sampler | epsilon-close | poly(N,m,b) expected bit time | ≤epsilon | proved; fresh audit accepted | none in stated regime |
| Restricted hybrid assembly with certified omitted macro mass≤epsilon/2 | Exact macro counts, exact short/minimal connected words, dense connected rejection where certified | epsilon-close | poly(N,m,b) with fixed explicit exact-state cap | ≤omitted mass+epsilon/2 | proved reduction and certificate | connected generation for excluded components |
| Remaining feasible length/accuracy pairs | No audited general polynomial sampler supplied here | unresolved | no established bound | no established guarantee | uncovered | connected positive-surplus sampling; exact counting already solved |

Here Z counts all identity bridges, Z0 counts those whose every nontrivial
component is minimal, and both are exactly computable in polynomial time.
At fixed epsilon, the explicit sparse theorem reaches order sqrt(N); the
dense theorem starts at order N² log N. Exact short sampling can dominate
the sparse approximation when epsilon is very small. These are sufficient
regimes with different precision dependence, not a single threshold.

## Explicit uncovered band and precision

Outside fixed/slow degree exceptions, a conservative displayed band lies
between the end of the short/sparse guarantees and `D_eps(N)`. More
precisely, exclude from the band inputs satisfying any of:

1. `m≤A(log N)²` for a chosen fixed A (or the full polynomial type-state cap);
2. even `m≤N` and `R(N,m)≤epsilon`;
3. the exact minimal-component mass certificate or full hybrid certificate;
4. `m≥D_eps(N)`.

The remaining feasible inputs are the uncovered set for this run. For fixed
accuracy, general lengths between order sqrt(N) and order N² log N still
lack a theorem covering all inputs. The certificates can cover individual
instances inside this interval, so the interval is not asserted to be an
impossibility region. General m=Theta(N) remains an important unsolved
family. The upper endpoint changes with epsilon: at fixed m, increasing
computation alone is not proved to improve the stated dense error guarantee;
no matching lower bound on its actual TV error is claimed. The
precision-aware exact DP can also be polynomial in N,m,b when
`min{m,N}=O(log²(N+m+b))`.

## Conditional connected primitives and named-method obstructions

| regime | sampler | exact/approximate | runtime | TV error | status | missing primitive |
|---|---|---|---|---|---|---|
| Connected v-label identity words, length 2v−2 (g=0) | DPS rooted Cayley/permutation product, forget uniform root | exact | polynomial bit time; published RAM algorithm linear | 0 | proved; source and root quotient checked | none for this conditional target |
| Arbitrary endpoint g at minimal length N−cycles(g) | Positive cycle-splitting recurrence and interleaving | exact | polynomial in N | 0 | proved; R1 | none; public identity gives m=0 only |
| Prescribed endpoint star words | Féray coefficient and backward sampler | exact | polynomial in degree and length | 0 | proved imported primitive | does not itself sample general transposition bridges |
| Connected components with v^(2v)≤(Nm+2)^c for a fixed constant c | DP on (prefix permutation, exposed support partition) | exact | O(ell v³ v!Bell(v)) polynomial-bit work; polynomial under the cap | 0 | proved | no unrestricted R1-to-connected substitution |
| High-surplus connected words with C(v,ell)/Z(v,ell)≥1/2 and dense error δ | Reject disconnected dense outputs | approximate connected | expected polynomial for δ≤1/4 | ≤4δ | proved conditional transfer | sufficient dense length/accuracy condition |
| Connected words of length 2v (g=1), v unbounded | Counts solved by positive DYZ recurrence | sampling unresolved | count poly(v); no proved general sampling bound here | unresolved | uncovered primitive | exact or tunable uniform connected sampler |
| Positive-surplus intermediate components in general | Exact positive component/surplus reduction | unresolved generation | all weights poly(N,m) | no error claim without primitive | strict reduction | connected sampler with poly(v,ell,b) runtime |
| Full defect-type inventory, m≤N and m=omega(log²N) | Literal type enumeration | named-method obstruction | ≥exp(Omega(sqrt(m))) states | n/a | proved | compression or another method |
| Minimal-component-only output at m=Theta(N^alpha), fixed 2/3<alpha≤1 | Always condition total surplus to zero | named-method obstruction | sampler is polynomial but target approximation fails | TV→1 (or subset empty) | proved; independent R3 audit | allow positive surplus; no hardness consequence |

No computational hardness result is established. The fixed-positive-genus
long-cycle sampler in Féray–Louf–Thévenin has a different endpoint and an
asymptotic, rather than tunable, TV guarantee. Higher-genus coherent Hurwitz
mobiles remain a plausible route with an unproved sampling step.

Proofs and audits: [R1](roles/r1-short-exact/report.md),
[R2](roles/r2-dense-threshold/report.md),
[R3](roles/r3-intermediate-hybrid/report.md), and
[coordinator synthesis](coordinator_report.md). Primary dependency links and
composition translations are recorded in the coordinator report.

The dense hybrid predicate can be tested using integers. For v≥5, write
`q_v=floor(ell/[2v(v−1)])` and use the conservative requirement

```
q_v≥max(4ceil(log2 v),144[b+ceil(log2(24Nv²))]),
2C(v,ell)≥Z(v,ell).
```

It ensures component proposal TV≤epsilon/(8N) and connected acceptance
at least one half under the exact target. Ceiling binary logarithms are
integer bit-length comparisons. This suffices for the exact restricted
count Z_allowed and avoids a transcendental comparison in the selector.
