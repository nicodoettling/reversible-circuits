# R0 coverage role plan

## Objective and target

Target the uniform fixed-length bridge law `U_N` on

```text
Omega(N,L_N;e),  L_N = 2N^3,
```

where every factor is one of the `M=binom(N,2)` transpositions.  Prove an
explicit exponentially small upper bound on the probability that at least one
transposition type is absent.  This role does not study local heat-bath
mixing.

Permutations are maps composed as `(sigma tau)(x)=sigma(tau(x))`; thus the
displayed product `t_1...t_L` acts on points right-to-left.  Random-walk
operators use right multiplication: starting from `e`, the successive states
are `t_1,t_1t_2,...,t_1...t_L`, exactly matching the displayed word order.

## Named claim under test

For `N>=3`, let `P` be right convolution by the uniform law on all
transpositions and, for a fixed transposition `a`, let `Q_a` be right
convolution by the uniform law on all transpositions except `a`.  Test and
prove the chain of inequalities

```text
Pr_U_N[a is absent]
 = ((M-1)/M)^L Q_a^L(e,e)/P^L(e,e),

||Q_a|| on {1,sign}^perp
 <= 1 - (N-2)/M,
```

and hence a union-bound estimate at `L=2N^3`.  The second line requires an
independent audit of invariant subspaces, parity, normalizations, and the exact
nontrivial absolute spectrum of `P`.

## Work plan

1. Derive the exact deleted-generator return-count ratio and handle parity.
2. Obtain the full-walk spectral gap from a self-contained argument or an
   exact primary-source theorem; translate its continuous/discrete
   normalization explicitly.
3. Compare `Q_a` to `P` in operator norm and convert the spectral estimate to
   an even-time pointwise return bound using the regular representation trace.
4. Union bound over the `M` transpositions and simplify constants at
   `L=2N^3`.
5. Check `N=2`, `L=0`, odd `L`, minimal endpoint length, and padding by pairs.
6. Write a tiny exact enumerator/spectral checker for small ranks.  Its purpose
   is only to falsify the claimed exact ratio or finite inequalities, not to
   prove the general theorem.

## Expected failure modes

- forgetting the `-1` sign eigenvector of the non-lazy transposition walk;
- applying a spectral-gap statement to absolute eigenvalues without the sign
  twist;
- comparing unnormalized counts as if both alphabets had size `M`;
- using a trace-average return bound without checking Cayley translation
  invariance;
- treating an unconditioned coupon-collector estimate as a bridge estimate;
- claiming anything for an empty odd-length identity fiber.

## Deliverables

`checkpoint.md`, `report.md`, a self-contained Python exact check, and
machine-readable output.  Material claims will be labeled and the report will
end with the required role schema.
