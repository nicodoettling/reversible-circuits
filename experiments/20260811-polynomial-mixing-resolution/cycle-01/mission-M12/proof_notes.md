# Proof Notes: Low-Surplus Cuts Have Polynomial Boundary

## 1. Setup and cut convention

Permutations are maps on \([N]\), \(pq=p\circ q\), and a word evaluates as
\(t_1\cdots t_m\).  Put \(M=\binom N2\).  The target \(\pi\) is uniform on
\(\Omega(N,m)\), and \(Q(A,B)=\sum_{x\in A}\pi(x)K(x,B)\).

For every nontrivial support component \(C\), write \(v_C=|C|\) and let
\(k_C\) be the number of factors supported on it.  Define its (integer)
surplus genus and the total surplus genus by

\[
 g_C=\frac{k_C-2(v_C-1)}2\ge0,
 \qquad G(w)=\sum_C g_C.
\]

The inequality and integrality follow from the proved feasible-component
criterion.  Let

\[
 A_g=\{w\in\Omega(N,m):G(w)=g\},\qquad A_{\le g}=\bigcup_{h=0}^gA_h.
\]

We measure a named partition by the orientation-free ratio

\[
 \Phi_{\pm}(A)=
 \frac{Q(A,A^c)}{\min\{\pi(A),\pi(A^c)\}}.
\]

Consequently no assumption such as \(\pi(A)\le1/2\) is hidden.  If
\(K_A^{\rm out}=Q(A,A^c)/\pi(A)\), then
\(\Phi_{\pm}(A)\ge K_A^{\rm out}\), regardless of which side is smaller.

## 2. Enumerative input, with normalization checked

For a fixed labeled \(v\)-set, let \(C_g(v)\) be the number of connected
identity transposition words of length \(2(v-1)+2g\).

Vakil defines \(c^g_\alpha\) as the number of transitive factorizations of a
*fixed* permutation of cycle type \(\alpha\) into
\(d+\ell(\alpha)+2g-2\) transpositions (Conventions 1.2), and Corollary 1.5
gives the genus-zero and genus-one formulas.  Specializing to
\(\alpha=1^v\) (whose fixed permutation is the identity and for which the
normalizing product \(\prod_i\alpha_i\) is one) gives

\[
 C_0(v)=(2v-2)!v^{v-3}                                      \tag{2.1}
\]

and

\[
 C_1(v)=\frac{(2v)!}{24}B_v,                                 \tag{2.2}
\]

where

\[
 B_v=v^v-v^{v-1}-\sum_{j=2}^v (j-2)!\binom vj v^{v-j}.
\]

In particular \(0<B_v\le v^v\).  The source is Ravi Vakil,
“Genus 0 and 1 Hurwitz numbers: Recursions, formulas, and graph-theoretic
interpretations,” Conventions 1.2 and Corollary 1.5:
<https://arxiv.org/abs/math/9812105> (the linked PDF contains the displayed
formulas).  Checks: \(C_0(2)=1\), \(C_0(3)=24\), \(C_0(4)=2880\), and
\(C_1(2)=1\), agreeing with the project smoke cases and the unique words on a
fixed two-point support.

## 3. Minimal components expose adjacent bridge squares

### Lemma 3.1 (fixed-position square probability)

For \(v\ge3\), under the uniform law on the \(C_0(v)\) minimal connected
words, the factors at any fixed adjacent position are equal with probability

\[
 p_v=
 \frac{
  \frac12\sum_{a=1}^{v-1}\binom va
        a^{a-2}(v-a)^{v-a-2}}
 {(2v-2)(2v-3)v^{v-3}}
 \ge \frac1{12v}.                                           \tag{3.1}
\]

For \(v=2\), the probability is one.

**Proof.**  Delete a specified adjacent pair \(t,t\).  The remaining word is
an identity word of length \(2v-4\).  Its support graph cannot remain
connected, by the feasible-component lower bound.  It cannot have three or
more components because adding the single support edge \(t\) could not make
the original graph connected.  Thus it has exactly two components, on an
unordered bipartition \(A\sqcup B\), and both component words are minimal.
Conversely, interleave minimal connected words on \(A,B\), choose one of the
\(|A||B|\) crossing transpositions, and insert it twice at the specified
position.  Deletion recovers every choice, so there is no multiplicity.

For \(|A|=a\), the count is

\[
 \binom{2v-4}{2a-2}C_0(a)C_0(v-a)a(v-a).
\]

Summing over labeled unordered bipartitions gives the numerator count

\[
 D_0(v)=\frac{(2v-4)!}{2}
 \sum_{a=1}^{v-1}\binom va a^{a-2}(v-a)^{v-a-2}.
\]

Here \(C_0(1)=1\) is the empty singleton word.  Dividing by (2.1) proves the
equality.  Keeping only the two ordered singleton terms after the factor
\(1/2\) yields

\[
 p_v\ge
 \frac{v(v-1)^{v-3}}
 {(2v-2)(2v-3)v^{v-3}}.
\]

The first rational factor is at least \(1/(4v)\), while
\(((v-1)/v)^{v-3}>1/3\) (use
\((1+1/(v-1))^{v-1}<e<3\)); hence (3.1).  For \(v=2\), the sole word is
\((t,t)\).  ∎

Every square counted above is a *bridge square*: after its deletion the
original component splits into exactly two minimal components.  This fact is
what keeps the later macro-layer claim honest.

### Lemma 3.2 (color interleavings do not hide all squares)

Fix any macrofiber in \(A_0\), with component lengths
\(k_j=2(v_j-1)\).  Under its conditional uniform law,

\[
 \Pr[\text{the global word has an adjacent equal pair}]
 \ge \frac1{12(m-1)}.                                      \tag{3.2}
\]

**Proof.**  The proved macrofiber factorization makes the internal component
words independent and uniform and makes their color interleaving uniform.
For two specified consecutive occurrences of a color of multiplicity \(k\),
the probability that no other color lies between them is exactly \(k/m\):
fusing the pair gives the ratio
\(\binom{m-1}{k-1}/\binom mk=k/m\), with the refinements by the other colors
cancelling.

Let \(X\) count globally adjacent equal pairs.  A component of size
\(v\ge3\) contributes in expectation

\[
 (2v-3)p_v\frac{2(v-1)}m
 \ge \frac1{12}\frac{k}{m}.
\]

For \(v=2\), its unique internal pair is equal and contributes \(k/m\), so
the same lower bound holds.  Summing \(k_j=m\) gives
\(\mathbb E X\ge1/12\).  Since \(X\le m-1\), (3.2) follows.  This explicitly
handles arbitrarily rare colors and disconnected multi-component words. ∎

## 4. Exact normalized square-refresh probability

Suppose \(m\ge4\) and a word contains \(t,t\) in adjacent positions.  Choose
deterministically one length-four window containing those positions.  Keeping
the other two entries fixed and replacing \(t,t\) by \(s,s\) preserves the
ordered block product under the declared convention because both pairs equal
the identity.

For any target product \(h\), a length-four fiber has size at most \(M^3\):
the first three transpositions determine the fourth.  Therefore the exact
kernel chooses any specified replacement with probability at least

\[
 \delta_{\rm block}
 =\frac1{2|R_m|}\frac1{m-3}\frac1{M^3}
 \ge\frac1{6(m-3)M^3}.                                    \tag{4.1}
\]

This includes the \(1/2\) laziness, uniform block-size selection, uniform
window selection, and uniform conditional-fiber probability.  At \(m=4\),
the sole \(r=4\) window is the whole word and \(|R_4|=2\); (4.1) is still a
valid (conservative) bound.

For a bridge square in a minimal component of size at least three, choose
\(s\) internal to one of the two deletion components having size at least
two.  The old component splits and that side gains two units of length, so the
new word lies in \(A_1\).  For a size-two minimal component, its deletion
leaves two isolated labels.  Since \(m\ge4\), an \(A_0\) word has another
nontrivial component; choose \(s\) internal to that component.  The size-two
component disappears and the other component gains genus one.  Again the
output is in \(A_1\), and \(s\ne t\).

Combining (3.2) and (4.1), every nonempty \(A_0\) satisfies

\[
 \frac{Q(A_0,A_1)}{\pi(A_0)}
 \ge \delta_0
 :=\frac1{72(m-1)(m-3)M^3}.                               \tag{4.2}
\]

This construction checks the macro layer after deletion and insertion; it is
not merely a statement that the support graph changed somehow.

### Theorem 4.2 (zero-surplus cut rejected)

Whenever \(A_0\) is nonempty and proper,

\[
 \Phi_\pm(A_0)\ge\delta_0.                                \tag{4.3}
\]

**Proof.**  Equation (4.2) gives
\(Q(A_0,A_0^c)\ge\pi(A_0)\delta_0\).  Divide by a quantity no larger than
\(\pi(A_0)\). ∎

At \(m=2(N-1)\), the equality
\(m=2\sum_C(v_C-1)\), including isolated labels, forces one component on all
\(N\) labels.  Hence \(A_0\) is exactly the full-support connected minimal
layer.  Its mass need not be at most \(1/2\); (4.3) is orientation-free and
therefore accounts for this explicitly.

## 5. One unit of surplus: bridge-square exposure

### Lemma 5.1 (genus-one bridge squares)

For \(v\ge3\), a uniform word counted by \(C_1(v)\) has, at any fixed
adjacent position, probability at least

\[
 p_v^{\rm br}\ge\frac1{64v^4}                              \tag{5.1}
\]

of an equal pair whose deletion leaves one isolated label and a connected
genus-one word on the other \(v-1\) labels.

**Proof.**  Choose the isolated label (\(v\) choices), a connected genus-one
word on the remaining labels (\(C_1(v-1)\) choices), and the crossing edge
from the isolated label (\(v-1\) choices), then insert that edge twice at the
specified position.  Deletion is an inverse, so this gives
\(v(v-1)C_1(v-1)\) distinct words.

At a specified position, inserting an arbitrary square into a minimal
connected word is injective, hence

\[
 C_1(v-1)\ge \binom{v-1}{2}C_0(v-1).
\]

Together with \(C_1(v)\le(2v)!v^v/24\), this gives

\[
 p_v^{\rm br}\ge
 \frac{6(v-1)^2(v-2)}{(2v-1)(2v-2)(2v-3)}
 \frac{(v-1)^{v-4}}{v^v}.
\]

The first factor is at least \(1/16\); the second is at least
\(1/(4v^4)\), using \((1-1/v)^v\ge1/4\) for integers \(v\ge2\) (and checking
\(v=3\) directly).  This proves (5.1). ∎

### Lemma 5.2 (uniform escape from every \(A_1\) macrofiber)

Assume even \(m\ge6\) and \(m\le2(N-1)\).  Under the conditional uniform law
of every macrofiber in \(A_1\),

\[
 \Pr[\text{a global adjacent square admits a refresh into }A_2]
 \ge\frac1{32N^2m(m-1)}.                                  \tag{5.2}
\]

**Proof.**  There is exactly one genus-one component.

If its size is \(v\ge3\), it has length \(2v\).  By (5.1), summing its
\(2v-1\) internal positions and applying the exact interleaving probability
\(2v/m\), the expected number of global adjacent bridge squares of the
specified kind is at least

\[
 (2v-1)\frac1{64v^4}\frac{2v}{m}
 \ge\frac1{32N^2m}.
\]

Divide by the maximum possible count \(m-1\).  On deleting such a square,
the \(v-1\) component has genus one; choosing \(s\) internal to it makes it
genus two while the isolated label stays isolated, so the new total surplus
is exactly two.

If the genus-one component has size two, then \(m\ge6\) forces at least one
minimal component.  A minimal component of size at least three supplies
bridge squares by Lemmas 3.1--3.2 (using only that one component gives a still
larger polynomial bound).  If all such components have size two, select one:
its two occurrences are adjacent in the global interleaving with probability
\(2/m\).  Move that square into the size-two genus-one component.  The former
component disappears and the latter becomes genus two.  Both bounds dominate
the right-hand side of (5.2). ∎

Combining (5.2) with (4.1) gives

\[
 \frac{Q(A_1,A_2)}{\pi(A_1)}
 \ge \delta_1
 :=\frac1{192N^2m(m-1)(m-3)M^3}.                          \tag{5.3}
\]

Here the notation means the aggregate conditional flow; each macrofiber in
\(A_1\) obeys the same lower bound, so mixtures do as well.

### Theorem 5.3 (cumulative genus-zero/one cut rejected)

For \(N\ge4\), even \(6\le m\le2(N-1)\),

\[
 \Phi_\pm(A_{\le1})
 \ge
 \frac1{27648N^2m(m-1)^2(m-3)^2M^6}.                      \tag{5.4}
\]

**Proof.**  In this regime \(A_0\) is nonempty (use a minimal connected word
on \(m/2+1\) labels), and \(A_2\) is nonempty (repeat one transposition
\(m\) times).  Reversibility and (4.2) imply

\[
 \pi(A_1)\ge Q(A_1,A_0)=Q(A_0,A_1)
 \ge\pi(A_0)\delta_0.
\]

Therefore
\(\pi(A_1)/(\pi(A_0)+\pi(A_1))\ge\delta_0/(1+\delta_0)
\ge\delta_0/2\).  Only retain the flow from \(A_1\) to \(A_2\) and use
(5.3):

\[
 \frac{Q(A_{\le1},A_{\le1}^c)}{\pi(A_{\le1})}
 \ge\frac{\delta_0\delta_1}{2}.
\]

Dividing instead by the smaller side can only increase the ratio.  Substituting
(4.2) and (5.3) yields (5.4). ∎

## 6. What this does and does not prove

Theorems 4.2 and 5.3 rigorously reject two named sparse bottleneck cuts,
including their stationary-mass orientation and exact kernel normalization.
They do not lower-bound the global spectral gap: a subset inside a macrofiber,
a higher-surplus threshold, or a full-support fiber could still have
superpolynomially small conductance.  No path routing or canonical hub is used;
all paths above have length one.  The first missing extension is a uniform
polynomial bridge-square (or more general slack-window) exposure estimate for
surplus genus \(g\ge2\), together with polynomial adjacent-layer mass ratios.
