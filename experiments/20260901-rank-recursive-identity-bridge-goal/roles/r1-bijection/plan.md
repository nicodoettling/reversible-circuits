# R1 plan: stable-sort disintegration and convention audit

Date: 2026-09-01 UTC

## Objective and target

Independently audit the positive rank disintegration for the fixed-length
uniform endpoint fiber

```text
Omega(N,L;g) = { (t_1,...,t_L) in T_N^L : t_1 ... t_L = g }.
```

The top-level project target is the uniform identity bridge, but this role
proves the word-level statement for every external endpoint `g in S_N` and
every length `L >= 0`.

## Convention lock

Permutations are maps on `[N]`.  I will use the product
`(alpha beta)(x)=alpha(beta(x))`; thus, in a displayed word
`t_1 ... t_L`, the rightmost factor acts first.  The implementation will use
the same convention and test it directly.

## Named claims to prove or falsify

1. For each fixed old/star binary pattern, stable sorting by
   `(i N) a -> a (a^{-1}(i) N)` terminates and is a product-preserving
   bijection from words with that pattern to an old word followed by a star
   word.
2. The inverse exists for every pattern and is obtained by the reverse local
   rule `a (j N) -> (a(j) N) a`; it preserves the stable relative order of
   both factor types.
3. Consequently, for all `N >= 2`, `L >= 0`, and `g in S_N`,

   ```text
   [g] C_N^L
    = sum_(k=0)^L binom(L,k) sum_(h in S_(N-1))
        [h] C_(N-1)^(L-k) [h^(-1)g] J_N^k.
   ```

4. The endpoint orientation is exactly `h^{-1}g` under the convention above.
5. The statement survives `N=2`, `L=0`, odd `L`, minimal endpoint length,
   and pair padding, with the empty-alphabet convention made explicit.

## Exact validation

Add a standard-library-only Python harness that:

- computes every endpoint coefficient by exact dynamic programming for every
  `2 <= N <= 5` and every `0 <= L <= 6`;
- computes the complete right-hand side independently from old-word and
  star-word dynamic programs;
- exhaustively checks the forward and inverse maps in a structured
  pattern/old-word/star-word enumeration, including product preservation and
  both inverse identities;
- writes per-endpoint machine-readable results and compact summaries.

The coefficient test uses dynamic programming rather than deriving counts by
enumerating the `10^6` length-six words in `S_5`.  Word enumeration is used
only for the requested exhaustive inverse-bijection audit.

## Reproducibility and expected failure modes

Repository commit at start: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
Python: `3.12.3`; no nonstandard dependency is planned.  The final report will
record the exact command and hashes of raw outputs.

Expected falsifiers are: a reversed `g h^{-1}` endpoint, an incorrect lower
endpoint update during an old/star swap, a nonconfluent stable sort, a failed
inverse for a nontrivial pattern, or mishandling `C_1^0` when `N=2`.  Any
counterexample will be retained rather than patched away silently.

Pre-existing changes shown by `git status --short` were present before this
role began and will not be modified.  This role writes only this directory.
