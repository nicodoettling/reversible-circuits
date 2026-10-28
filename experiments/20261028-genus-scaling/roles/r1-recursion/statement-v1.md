# R1 frozen conditional theorem — AUX-ENDPOINT-MARKER.v1

Frozen 2026-10-28. Status PROVISIONAL, exact-version review pending.

For each g>=2 let Theta_g be the finite set of nondecreasing tuples theta=(theta_1,...,theta_d), all theta_i>=2, with 2g−3<=sum_i(theta_i−1)<=3g−3. Suppose a deterministic uniform procedure, on input G, returns the exact rational coefficients c_(g,theta) for every 2<=g<=G in the fixed-permutation Hurwitz generating identity

    H_g(x,p)=sum_(theta in Theta_g) c_(g,theta)
        product_i psi_(theta_i)(s,p)/(1−psi_1(s,p))^(2g−2+d),
    psi_j(z,p)=sum_(a>=1) a^(a+j)/a! p_a z^a,
    s=x exp(psi_0(s,p)),
    H_g=sum_(N,alpha partition N) C_g(alpha)/(r! z_alpha) p_alpha x^N,
    r=N+len(alpha)−2+2g,
    z_alpha=product_a a^(m_a)m_a!.

The coefficient procedure must use at most A0 C0^(G+1) bit operations, return at most A0 C0^(G+1) coefficients, and each returned reduced numerator/denominator must have at most A0 C0^(G+1) bits, for absolute A0,C0>1. Genus zero and one use the source-scoped internally accepted formulas stated in the proof.

Then there is a single exact fair-bit algorithm which, given a nonempty exact label set [N], an explicitly listed permutation sigma on it with k individual cycles, and integer g>=0 with nonempty connected fiber, returns a uniform ordered transposition word of length N+k−2+2g, rightmost-first product sigma and connected support on all N labels. Its expected number of bit operations is at most A C^(g+1)(N+g+2)^15 for absolute A,C>1. Arbitrary exact labels can be canonically renamed and restored at their explicit bit cost; this theorem fixes labels [N].

Singleton g0 is the deterministic empty word; singleton positive genus is infeasible. Identity specialization N>=2 has m=2N−2+2g and is T0 under the coefficient-procedure hypothesis. Odd identity lengths are infeasible; m0 is connected only on a singleton; m2 connected identity requires N2; N2 has exactly one word for every feasible endpoint/parity. This is a literal word theorem, without any Markov-chain mixing, uniform graph, global-all-length, or wire-polynomial conclusion.

This freezes the reduction's exact dependency rather than asserting that the coefficient procedure is an external conditioning oracle. Coordinator COEFF-EXP.v1 is a separate proposed constructive discharge; no upgrade occurs until its proof and this theorem are reconciled and reviewed at exact versions.
