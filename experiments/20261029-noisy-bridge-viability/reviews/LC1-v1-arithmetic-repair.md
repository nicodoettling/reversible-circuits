# LC1-v1 computational wording repair

Reviewer r3 identified that the v1 proof claimed rational bit growth polynomial in L,s,log q and per-value rational description while summing q^s potentially unrelated denominators. That claim is overbroad for variable s. Probability identity, exact M0 eigenvalues, normalization, and fixed-s polynomial-time corollary are unaffected. Preserve v1 as reviewed history; do not silently replace it.

LC1-v2 uses an explicit operand bound O(q^s b+s^2 log(L+1)+s log(q+1)+s), where b bounds each evaluated value's bit description, with total arithmetic work polynomial in operand size and the number of operations. Distinct-denominator examples will be added to the finite registry. Status remains REPAIRED-PENDING-RECHECK until a fresh exact-version reviewer examines v2 and the targeted regression. This repair does not affect T0, C1 or C2, which do not depend on LC1.
