# Frozen statement T0 — six-window attack

Frozen 2026-10-29; statement only, for blind review. Status intentionally omitted from the referee input. No proposed proof is included.

Use M0 exactly: N>=2, even L, q=N(N-1)/2, T_N all transpositions, products rightmost first. U(N,L) is uniform on all labeled ordered length-L identity words. Q_k independently picks a uniform k-subset of positions and replaces the selected gates with iid uniform T_N draws; draws may equal old gates. The adversary sees the complete noisy word but neither positions nor draws. Define p_s=mu^{*s}, p_0=delta_id.

## Finite statement

Let L=6M with M>=2, B>=0 and 0<=k<=L integers. A structured word is produced by concatenating M arbitrary length-six identity words, applying an arbitrary simultaneous label conjugation and an arbitrary cyclic rotation, then performing at most B adjacent Hurwitz moves in either direction. Every choice may depend on hidden setup, the original word, and arbitrary internal randomness; only the stated bound B is required on every output. An adjacent move replaces (a,b) by (b,bab) or (aba,a). Let H=M-1-2B-k. If H>0, the test counts all L-5 nonwrapping consecutive six-gate windows whose ordered product is identity, and accepts iff their number is at least H.

For every structured source supported on this class, with any public/secret setup, the test accepts Q_k(D) with probability one. For Q_k(U(N,L)), its acceptance probability is at most

    min(1, (L-5) beta_N/H),
    beta_N = p_6(id)^2/p_12(id).

For every N>=1000, beta_N<1/40. In particular, if H>=M/2, the one-sample distinguishing advantage is at least 7/10. The bound is every-key, and exposes the same public setup in both worlds. No computational hardness assumption is used.

The literal-word test can be implemented in O(L) word-RAM operations on O(log N)-bit labels, since each window has six gates and at most twelve labels; a conservative bit bound is O(L log N). Setup and generation are treated separately from test cost.

## Explicit polynomial schedule

Let lambda be an integer >=32, N=lambda^2, L=6N, M=N, k=lambda, and B=floor(N/8). Then H>=M/2 and the attack advantage is >=7/10. Any exact polynomial-time generator in the structured class is covered, including the construction role's six-distinct-gate relator construction if its published algorithm satisfies the hypotheses. This is polynomial in lambda, N and L, not in log2 N alone. The common semantic error upper bound is 4/lambda, an inverse-polynomial upper bound, not negligible correctness.

Repeated fresh replies under the same setup remain broken already by one query. If the same fixed test is run on t independent fresh replies and accepts only when all t accept, structured acceptance is one and reference acceptance is at most (3/10)^t. The statement uses fresh independent word/noise tapes in the reference conditional on its exposed setup.

## More general local bound

For any even r>=2, even L>=2r, any fixed consecutive r-window of Q_k(U(N,L)), and any 0<=k<=L,

    Pr[window product=id] <= p_r(id)^2/p_(2r)(id).

This bound does not require that the chosen window avoid replacement. It is a finite bound for the matched noisy global reference.

## Required boundaries and exclusions

N=2, L=0, L=2, L=6, k=0, k=1, k=L, odd L, and H<=0 must be classified. The nontrivial numerical conclusion is restricted to N>=1000 and L=6M>=12. The theorem makes no claim about long enough scrambling to remove the window budget, arbitrary nonlocal compilers, general structured sources, or security of a candidate that survives this attack. Finite tests do not prove the asymptotic result.
