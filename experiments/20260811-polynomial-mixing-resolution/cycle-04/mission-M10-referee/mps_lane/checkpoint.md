# Halfway checkpoint

The July 2026 Rozman--Molnar--Schuch source is public as arXiv:2607.19078v1.
The aligned bridge interaction is literally a block-normal MPS parent
interaction once the inherited arbitrary-product aligned-`H_4` connectivity
theorem is used; this is not merely an analogy.

For `G=A_N`, `E=T_N^2`, uniform `nu`, and `p(t,u)=tu`, take

```text
C^e = binom(N,2)^(-1) direct_sum_{rho in G-hat} rho(p(e)).
```

Its length-`r` MPS span is `sqrt(nu^r)` times all functions of the ordered
product.  The two-site conditional heat bath is its canonical ground-space
projector.  Each irreducible block is normal by Burnside, with injectivity
length at most `floor((N-1)/2)`.  Aligned arbitrary-product connectivity gives
`ker H_r=S_r` for every `r>=2`, so the full Hamiltonian is a parent
Hamiltonian and decomposes orthogonally by endpoint:

```text
Delta(H_r) = min_h Lambda_N(r;h).
```

Theorem 9 in Appendix B of arXiv:2607.19078 (its restatement of
Nachtergaele) is directly applicable.  The overlap `gamma_{r,0}` is the
maximum, over total endpoints, of the maximal correlation of the raw left and
right length-`r` tails in a length-`3r` bridge.  The middle segment has kernel
`Q_N^r`.  The inherited endpoint-tilt lemma therefore gives

```text
gamma_{r,0} <= (4 epsilon + 2 epsilon^2)/(1-epsilon)^2
```

whenever `max_g ||A_N|Q_N^r(g)-1|<=epsilon`.  Choosing
`epsilon<=1/(16 sqrt(r))` makes `gamma_{r,0}<=1/(2 sqrt(r))`.  The same
Diaconis--Shahshahani character estimates used in M10 reach this accuracy at
some `r_N<=C N log(N+1)`.  Thus Theorem 9 yields, for all `n>=r_N`,

```text
Delta(H_n) >= Delta(H_r_N)/(4(r_N-1)).
```

This is stronger in `n` than the frozen two-block recursion, but it still
contains the unresolved fixed-endpoint base gap at one (and, for shorter
chains, all) lengths `O(N log N)`.  Generic MPS estimates do not bound that
term.  The chosen bond dimension satisfies `D^2>=|A_N|`; the RMS generic
`Xi` computation costs `O(D^6)` to `O(D^12)`, while FNW transfer estimates
contain `Tr(rho_*^{-1})=d_rho^2`.  Naive pseudoinverse or minimum-bridge-mass
bounds pay at least factorial scale.

The deterministic `N=3,4`, `r=2,3` algebra/connectivity harness passes all
cases in `results.json`.  It is only a falsification check.

