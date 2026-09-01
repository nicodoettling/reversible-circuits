# Independent referee report: definitive M67 v4

Date: 2026-08-12. Audited manifest SHA-256:
`629439ef523c86537e9d5170312dd95235d575d0a34d62b76517a91ff95735c0`.
Every file listed in the manifest matched its recorded hash.

## Verdict

**ACCEPT**

Numbered objections: none.

## Numbered audit

1. The corrected cyclic-start argument counts each unoriented edge twice
   across `d` and `n-d`, giving exactly `8n` in (1.4).
2. Every ordered extendible disjoint pair has a unique positive-gap
   parameterization (1.7), including both orders of nested pairs. Cycle
   tracing gives residual sizes `a,b,u+v`, and the phase is
   `conj(a(e))a(f)=16s_a^2s_b^2 exp(2pi i(v-u)/n)`. The `n` starts give
   exactly the `16n` coefficient.
3. For three cyclically ordered vertices, exactly three of the six orders are
   extendible. Cyclic relabeling accounts for (1.11) without overcounting.
4. The max-gap estimates are correct: `c>=n/3` contributes `O(n^-5/2)`;
   the `a`-large and `b`-large parts contribute `O(n^-2)`. Combined with
   `ne^n(n-3)!/n^(n-2)=O(sqrt n)`, the shared term is `O(n^-3/2)`.
5. Correction 2 properly restricts (1.2) to `i<j`, preserving order `ef`.
   Reversed real covariance is the conjugate and causes no later ambiguity.
6. The minimal-factorization formula and convention translation agree with
   Féray--Kortchemski Lemma 2.1 and its stated convention.
7. Conditional on two pair products, raw lifts are independent uniforms
   because completion counts depend only on those products. Thus (2.2) is
   exact, and the `L^2` contraction direction in (2.3) is correct.
8. With Correction 1, the aligned Gram numerator is
   `V_f+(l-1)Re<f,Kf>` over direct-sum norm `lV_f`, yielding exactly
   `1/l+(l-1)kappa_f/l`.
9. The endpoint `h_(2l+1)` is even, raw length `2l` is feasible and minimal,
   and the family lies below `C_mix N log(N+1)` eventually for every fixed
   positive `C_mix`.
10. Scope is accurate: this rigorously refutes PRODUCT-INCREMENT BASE
    CORRELATION only. It is neither a complete-pair gap upper bound nor
    Terminal B.
