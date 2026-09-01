# M13 Plan: Full-Support and Entropic Red Team

## Exact target

The target law is the uniform measure on

\[
\Omega(N,m)=\{(t_1,\ldots,t_m)\in T_N^m:t_1\cdots t_m=\mathrm{id}\},
\]

for `N >= 3` and even `m >= 4`. Permutations are maps on `[N]`, `pq` means
`p` after `q`, and a word is evaluated as `t_1 ... t_m`. The reviewed kernel is

\[
K_{N,m}=\frac12I+\frac1{2|R_m|}\sum_{r\in R_m}
 \frac1{m-r+1}\sum_{i=1}^{m-r+1}H_{i,r},
\qquad R_m=\{3,4,5\}\cap[1,m],
\]

where `H_{i,r}` is uniform on the exact length-`r` same-product fiber.

The assigned claim under attack is that no hidden full-support/fixed-macro
mode makes the gap superpolynomially small. A literal success for the red team
would be either nonirreducibility at an allowed `(N,m)` or an explicit infinite
family with a proved superpolynomial upper bound on the gap.

## Independent attack lanes

1. **Prefix bottleneck audit.** Prove exactly how a prefix permutation at a
   fixed cut can change: only windows crossing the cut matter. Quantify their
   total selection probability with laziness and all `r` normalizations. Test
   whether midpoint cycle type or a low-dimensional character has a
   nonnegligible two-phase stationary law separated by a small boundary.
2. **Full-support combinatorial modes.** Examine support-tree shape, edge
   multiplicity profile, and ordering statistics in the minimal connected
   regime `m=2(N-1)` and with small surplus. Determine which statistics can
   change under padded Hurwitz moves that remain in the full-support fiber.
3. **Restricted-fiber falsification.** Use Classification H to audit literal
   connectivity first, then seek an explicit Rayleigh-quotient witness or a
   cut whose conditional stationary mass and conditional boundary flow are
   both exactly controlled.
4. **Mean-lift stress test.** State the stationary-flow projection exactly and
   seek an explicit function whose fiber means have large projected energy but
   whose full energy is much smaller. Separate a failure of a particular
   one-step lift inequality from a failure of every polynomial decomposition.
5. **Named finite falsification only.** If symbolic analysis leaves a concrete
   universal local claim, enumerate `S_3,m=4`, `S_4,m=4`, and `S_4,m=6` to
   falsify it. Any script will record commit, Python version, fixed seed,
   exact command, and machine-readable output. Finite behavior will not be
   extrapolated into an asymptotic claim.

## Candidate universal statements to falsify

- `P-prefix`: every update can change a fixed prefix endpoint. (Expected to be
  false; the exact action rate should be `O(1/m)`.)
- `P-profile`: edge-multiplicity parity or degree parity determines identity
  or is invariant inside a full-support fiber. (Known calibration says false;
  record an explicit local witness if useful.)
- `P-tree`: minimal full-support words remain doubled trees under
  same-product/Hurwitz moves. (Expected false already in `S_3,m=4`.)
- `P-character-barrier`: the sign/cycle/standard-character midpoint statistic
  defines an asymptotic nonnegligible cut with superpolynomially small flow.
  This requires an exact stationary-mass formula and boundary estimate before
  promotion.
- `P-mean-lift`: an unqualified constant-factor mean-lift inequality holds for
  every partition/fiber. Seek a concrete counterexample while keeping clear
  that a polynomial-factor inequality may still survive.

## Calibration and stopping rule

Check odd `m`, `m=0`, `m=2`, `N=2`, the three exact smoke cases, the `m=4`
whole-word heat bath, doubled-tree near-minimal words, nontrivial color
interleavings, and the known failure of parity-only characterizations. Fixed
canonical hubs are forbidden as comparison evidence. A proposed asymptotic
cut is rejected unless its stationary mass and exact normalized flow are
proved.

This mission ends with the required nine-part return schema and one of the
allowed verdict strings. If no terminal obstruction survives, the report will
name the smallest standalone open proposition rather than convert finite or
polynomial slowness into a refutation.
