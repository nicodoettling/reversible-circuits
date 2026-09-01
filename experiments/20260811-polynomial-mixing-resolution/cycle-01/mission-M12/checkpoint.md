# M12 Halfway Checkpoint

## Status

No TERMINAL B construction has survived.  The strongest halfway result goes
in the opposite direction: the most literal sparse/near-minimal cut has an
inverse-polynomial one-step boundary for the exact normalized kernel.

## Proved checkpoint: the zero-surplus layer is not a superpolynomial cut

For a word, call a nontrivial support component of size \(v\) and weight \(k\)
*minimal* when \(k=2(v-1)\).  Let \(A^{(0)}_{N,m}\) be the union of all
macrofibers in which every nontrivial component is minimal.  When this set is
nonempty and proper (the sparse regime \(m\le 2(N-1)\), with the trivial edge
cases separated), its two-sided cut ratio satisfies

\[
 \frac{Q(A^{(0)},(A^{(0)})^c)}
      {\min\{\pi(A^{(0)}),\pi((A^{(0)})^c)\}}
 \geq
 \frac{1}{72(m-1)(m-3)\binom N2^3}.
\]

Thus this cut is at worst polynomially thin.  At \(m=2(N-1)\),
\(A^{(0)}\) is exactly the full-support connected minimal layer, so the
standard near-minimal candidate is rejected as a source of TERMINAL B.

The key count is exact.  A uniform minimal connected identity factorization
on \(v\ge3\) labels has, at any fixed adjacent position, an equal pair with
probability

\[
p_v=
\frac{
 \frac12\sum_{a=1}^{v-1}\binom va
       a^{a-2}(v-a)^{v-a-2}}
 {(2v-2)(2v-3)v^{v-3}}
\ge \frac1{12v}.
\]

This follows by deleting the adjacent square.  The remainder has exactly two
minimal connected components; conversely, choose an unordered bipartition,
interleave a minimal word on each part, choose a crossing transposition, and
insert it twice.  The classical Hurwitz count used here is
\((2v-2)!v^{v-3}\); Goulden--Jackson's genus-zero formula (their equation
(7.3), specialized to cycle type \(1^v\), together with their normalization)
checks the exact convention.

Inside a fixed all-minimal macrofiber, the proved color-interleaving
factorization gives

\[
 \mathbb E[\#\text{ globally adjacent equal pairs}]\ge 1/12,
 \qquad
 \Pr[\text{at least one}]\ge \frac1{12(m-1)}.
\]

For any state with such a pair, select one length-four window containing it
and replace \(tt\) by a specifically chosen \(ss\) that changes the weighted
component data.  Since a length-four same-product fiber has size at most
\(M^3\), \(M=\binom N2\), the exact kernel assigns this replacement probability
at least \(1/[6(m-3)M^3]\), including laziness, block-size choice, window
choice, and conditional-fiber probability.  Multiplication conventions are
irrelevant to \(tt=ss=\mathrm{id}\), but remain \(pq=p\circ q\) throughout.

## Cuts rejected or narrowed

- A fixed full-support minimal Hurwitz orbit is not sticky: the same bound
  applies, independently of its stationary mass.
- A fixed labeled minimal component macrofiber is not sticky, even when its
  color is rare; uniform interleavings cost only the explicit \(k/m\) factor.
- The union over all all-minimal partitions is not sticky.  A square refresh
  creates two units of surplus in one component or changes the component
  partition, hence exits the union.
- Counting only the mass of a doubled-tree/canonical subset is invalid: such a
  subset can be exponentially rare, and the inherited canonical-hub result is
  a congestion warning rather than a conductance upper bound.
- Edge or degree parity was not used; it does not characterize identity.

## Remaining red-team frontier

The plausible sparse obstruction, if any, must live in a positive-surplus
fiber or in a square-poor/local-geodesic subset inside such a fiber.  The
standalone unresolved proposition is currently:

> **Low-surplus exposure proposition.**  There is a universal polynomial
> \(P\) such that for every feasible weighted support-component macrofiber
> whose total surplus
> \(\sum_C[k_C-2(|C|-1)]\) is at most \(O(1)\), the conditional uniform law
> gives probability at least \(1/P(N,m)\) to a length-\(3,4\), or \(5\)
> window whose same-product fiber contains a word in a different macrofiber.

Proving this would eliminate all bounded-surplus macrofibers as
superpolynomial traps.  Refuting it with a nonnegligible-mass family plus an
exact flow bound could seed TERMINAL B.  The second half will self-audit the
counting and transition construction and decide whether this proposition can
be advanced beyond surplus zero.
