# Cycle 05 M13 nonnormal-Schreier red-team plan

## Exact target

Work with maps composed by `(pq)(x)=p(q(x))`, the uniform law on

```text
Omega(N,m)={t in T_N^m:t_1...t_m=id},
```

and the exact lazy kernel

```text
K=(1/2)I
  +(1/(2|R_m|)) sum_{r in R_m}(1/(m-r+1))sum_i H_{i,r},
R_m={3,4,5} intersect [m].
```

First seek an explicit infinite family whose original-`K` conductance is
superpolynomially small.  Auxiliary aligned bridges and pure Hurwitz
restrictions do not suffice.

If no terminal family survives, audit the sharply named minimal-full-support
macro cut at `m=2(N-1)`:

```text
F_N={w in Omega(N,2N-2):the factorization graph is connected on all N labels}.
```

The intended rejection certificate is an exact count of adjacent removable
leaf squares, followed by one actual `r=3` heat-bath exit with every
normalization retained.  A secondary visible nonnormal coordinate is the
first-join star cut `{t_1 incident to a fixed label}`.

## Proof obligations

1. Give the exact stationary mass of `F_N`, including an exact formula for
   the global denominator.
2. Prove the insertion/deletion bijection for a marked adjacent leaf square
   and compute its uniform expectation in `F_N`.
3. Convert that expectation into a lower bound on the probability that a word
   has at least one certificate without assuming independence.
4. Specify a boundary-safe three-window and exact same-product outcome that
   removes the leaf label.
5. Track outer laziness, block-size scan, window scan, conditional-fiber size,
   duplicate outcomes, and the nonnegative `r=4,5` contributions.
6. Rerun `S_3,m=4`, `S_4,m=4`, and `S_4,m=6` with exact rational
   stationary mass and full `r=3,4,5` boundary flow.
7. State the surviving embedded nonnormal-Schreier isoperimetric proposition
   and explain why trivial normal quotients and polynomial diameter do not
   decide it.

## Falsification modes

- deleting a square does not leave connected support on the remaining labels;
- one state is overcounted by more than `N` marked certificates;
- the last adjacent pair has no legal length-three window;
- the replacement square still uses the removed label;
- a missing `1/2`, `|R_m|`, `m-2`, or conditional-fiber factor;
- conditional macro mass is substituted for the global stationary mass;
- a lower bound for a named cut is misreported as a global gap theorem.

## Output

Write a halfway checkpoint, exact verifier and machine-readable output, then a
nine-field report.  A finite run may falsify the analytic formulas but cannot
prove their universal quantifiers.
