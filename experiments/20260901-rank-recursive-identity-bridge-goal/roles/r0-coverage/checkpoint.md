# R0 coverage checkpoint

## Substantive claim reached

The deleted-generator spectral route gives a direct bridge-conditioned bound;
no coupon-collector independence assumption is needed.  The current theorem
candidate is: for `N>=3`, `M=binom(N,2)`, and every even `L`,

```text
Pr_{w uniform on Omega(N,L;e)}[not Full_N(w)]
 <= M (1-1/M)^L
      (1 + (N!/2) (1-(N-2)/M)^L).                 (C1)
```

At `L=2N^3`, elementary estimates reduce (C1) to

```text
Pr[not Full_N] <= exp(-2N).
```

The `N=2` dense case has probability zero and will be handled separately.
Status at this checkpoint: **conditional**, pending the final source and
normalization audit of the full transposition spectrum and the exact small
checks.

## Derivation audited so far

Use maps with `(sigma tau)(x)=sigma(tau(x))`; a word `t_1...t_L` acts
right-to-left.  On `ell^2(S_N,uniform)`, let

```text
P   = M^{-1} sum_{t in T_N} R_t,
Q_a = (M-1)^{-1} sum_{t in T_N, t!=a} R_t,
(R_t f)(x)=f(xt).
```

Then the exact bridge ratio for a fixed missing transposition `a` is

```text
Pr[a absent]
 = ((M-1)/M)^L Q_a^L(e,e)/P^L(e,e).               (C2)
```

Both operators have eigenvectors `1` and `sgn`, with eigenvalues `+1` and
`-1`, and their common orthogonal complement `W={1,sgn}^perp` is invariant.
For the full walk, the candidate exact fact is

```text
||P|_W|| = 1-N/M = 1-2/(N-1).                     (C3)
```

The positive-side gap in (C3) follows from Caputo--Liggett--Richthammer,
Theorem 1.1, applied to the interchange process on the unweighted complete
graph: the complete-graph one-particle Laplacian gap is `N`, while
`-L_IP=M(I-P)`.  Multiplication by `sgn` anti-commutes with `P`, so the
positive-side statement controls absolute eigenvalues after removing both
`1` and `sgn`.  This convention translation still needs to be recorded in
the final report with the primary citation.

The exact identity

```text
P = M^{-1} R_a + ((M-1)/M) Q_a
```

gives

```text
||Q_a-P|| <= 2/M,
||Q_a|_W|| <= 1-N/M+2/M = 1-(N-2)/M =: rho < 1.
```

For even `L`, Cayley translation invariance and the regular-representation
trace give

```text
P^L(e,e) >= 2/N!,
Q_a^L(e,e) <= 2/N! + rho^L.
```

Substitution in (C2) and a union bound over `M` choices of `a` yield (C1).
No step replaces the bridge law by an unconditioned word law.

For `L=2N^3`, use `1-x<=exp(-x)` twice.  The first contribution has logarithm
at most

```text
log M - L/M <= N-4N = -3N,
```

because `2 log N<=N` for `N>=3`.  The second has logarithm at most

```text
log(M/2)+log(N!)-(N-1)L/M
 <= N+N^2-4N^2 <= -3N.
```

Thus the sum is at most `2 exp(-3N)<=exp(-2N)`.

## Boundary audit

- `L` odd: `Omega(N,L;e)` is empty by sign, so no uniform target exists.
- `L=0`: the unique identity word is empty and is not full for `N>=2`; (C1)
  is only a loose valid bound there.
- `N=2`: there is one transposition.  Every positive even identity word uses
  it, so dense `L_2=16` has failure probability zero; `Q_a` is not defined
  and is not used.
- General endpoint feasibility: if `ell_T(g)=N-cycles(g)`, then a length-`L`
  transposition factorization exists exactly when `L>=ell_T(g)` and
  `sign(g)=(-1)^L`.  A minimal cycle decomposition gives length `ell_T(g)`;
  append adjacent pairs `tt` for padding.  For `N=2`, the parity condition
  selects the unique word at every feasible length.
- Minimal endpoint length and length two do not imply full support; the R0
  theorem is specifically the dense scheduled identity length.

## Remaining checks

1. Run a deterministic exact DP for the return ratios and the finite
   inequalities through `N=5,L=6`, plus dense small-rank fixed-edge checks.
2. Verify the character-ratio constant independently on partitions for small
   `N`.
3. Promote the status to proved only after the primary-source theorem and all
   continuous/discrete normalizations are explicit in `report.md`.

## Post-checkpoint refinement

The primary theorem applies directly to the deleted-edge interchange process,
not only to the complete graph.  The one-particle Laplacian of
`K_N minus {a}` has gap `N-2`: on the orthocomplement of constants it is
`N I-bb^T`, where `b` is the difference of the two endpoint basis vectors and
`||b||^2=2`.  Therefore the exact positive-side second eigenvalue of `Q_a` is

```text
rho_* = 1 - (N-2)/(M-1).
```

The sign anti-commutation again turns this into the exact absolute radius on
`W`.  This improves (C1) by replacing `1-(N-2)/M` by `rho_*`.  It also gives
the useful simplification

```text
((M-1)/M) rho_* = (N-2)/N = 1-2/N.
```

The earlier perturbation bound remains a valid independent cross-check.
