# Gap-composition parameterization of the cyclic quotient

Status: exact identities below are **proved**.  The final two-step inequality is
the named unresolved analytic step.

## 1. Conventions and Cayley weights

Permutations compose as \((pq)(x)=p(q(x))\), and a factor tuple is multiplied
from left to right.  Fix odd \(n=2\ell+1\), the long cycle
\(h=(0\,1\,\ldots\,n-1)\), and simultaneous conjugation
\(\theta(g)=h^{-1}gh\).  Put

\[
 \tau(d):=\frac{d^{d-1}}{d!},\qquad
 T(z):=\sum_{d\geq1}\tau(d)z^d,qquad T=ze^T.
\]

If a permutation \(q\) of transposition length \(r\) has nontrivial cycle
sizes \(d_1,\ldots,d_k\), then the number of ordered minimal transposition
factorizations is

\[
 F_r(q)=r!\prod_{j=1}^k\tau(d_j).
\]

The coefficient identity used below is

\[
 [z^n]T(z)^k=\frac{k\,n^{n-k-1}}{(n-k)!}.
\tag{1.1}
\]

## 2. Rank-two states as colored cyclic compositions

### 2.1 Oriented three-cycles

An admissible three-cycle has the noncrossing orientation

\[
 g=(a,\ a+x,\ a+x+y),\qquad x,y,z>0,\quad x+y+z=n.
\]

Its \(\theta\)-orbit is represented by the cyclic composition
\([x,y,z]\), and \(g^{-1}h\) has cycle sizes \((x,y,z)\).  If
\(r(x,y,z)\in\{1,3\}\) is the number of cyclic rotations fixing the ordered
triple, the orbit size is

\[
 o_3[x,y,z]=\frac{n}{r(x,y,z)}.
\]

Thus its exact quotient stationary mass is

\[
 \bar\pi_3([x,y,z])=
 \frac{o_3[x,y,z]\,3(n-3)!\,\tau(x)\tau(y)\tau(z)}{n^{n-2}}.
\tag{2.1}
\]

The only shortened orbit is the balanced triple \((n/3,n/3,n/3)\), when
\(3\mid n\); its size is \(n/3\).

### 2.2 Double transpositions

Let \((x,y,z,w)\) be a positive cyclic four-composition of \(n\), and set
\(p_0=a\), \(p_1=a+x\), \(p_2=a+x+y\), \(p_3=a+x+y+z\).  There are two
noncrossing matchings:

\[
 \begin{array}{c|c|c}
 \text{color}&g&\text{cycle sizes of }g^{-1}h\\ \hline
 S&(p_0p_1)(p_2p_3)&(x,z,y+w)\\
 N&(p_0p_3)(p_1p_2)&(x+z,y,w).
 \end{array}
\tag{2.2}
\]

Here \(S\) means separated and \(N\) nested relative to the chosen cut.
Changing the distinguished endpoint acts by

\[
 (x,y,z,w,S)\sim(y,z,w,x,N)
 \sim(z,w,x,y,S)\sim(w,x,y,z,N).
\tag{2.3}
\]

For odd \(n\), every double-transposition \(\theta\)-orbit has size \(n\):
a nontrivial stabilizing rotation would induce a nontrivial permutation of
its two edges, hence have order two, impossible in the odd cyclic group.
Writing \(\lambda_D(\alpha,c)\) for the three sizes in the last column of
(2.2),

\[
 \bar\pi_D([\alpha,c])=
 \frac{n\,2(n-3)!\prod_{d\in\lambda_D(\alpha,c)}\tau(d)}{n^{n-2}}.
\tag{2.4}
\]

### 2.3 Normalization check

Equation (1.1) gives

\[
 n(n-3)![z^n]T^3=3n^{n-3},
\]

so the total three-cycle mass is exactly \(3/n\).  For either double color,

\[
 \sum_{x+y+z+w=n}\tau(x)\tau(z)\tau(y+w)
 =[z^n]T^2(zT'-T)
 =[z^n]\frac{T^4}{1-T}
 =\frac{n^{n-4}}{(n-4)!}.
\tag{2.5}
\]

More explicitly, summing over the anchor \(a\) and both colors counts each
actual double transposition four times.  Therefore its total unnormalized
weight is

\[
 \frac n4\cdot2\cdot2(n-3)!\cdot
 \frac{n^{n-4}}{(n-4)!}=(n-3)n^{n-3}.
\]

After division by \(n^{n-2}\), the total double mass is \((n-3)/n\).
Hence (2.1) and (2.4) sum to one.

## 3. Four exact row schemas for \(\bar K\)

Fix a source \(g\), and let the three cycles of \(q=g^{-1}h\) have vertex
sets \(C_i\), sizes \(d_i\), and ranks \(r_i=d_i-1\), so
\(r:=r_1+r_2+r_3=n-3\).  A uniform minimal factorization of \(q\) is obtained
by independently choosing a uniform minimal factorization within each
\(C_i\), then uniformly interleaving the three color words having
multiplicities \(r_i\).

For a \(d\)-cycle \(c_d\), define the local first-edge law (when \(d\ge2\))

\[
 \nu_d(e)=\frac{(d-2)!\,\tau(u)\tau(d-u)}{d^{d-2}},
\tag{3.1}
\]

where deleting the chord \(e\) splits the cyclic order into sizes
\(u,d-u\).  Define the local first-pair-product law (when \(d\ge3\))

\[
 \mu_d(p)=
 \frac{a(p)(d-3)!\prod_{D\in\operatorname{cyc}(p^{-1}c_d)}
                    \tau(|D|)}{d^{d-2}},
\tag{3.2}
\]

where \(a(p)=3\) for an oriented three-cycle and \(a(p)=2\) for a double
transposition.  In local gap coordinates this is

\[
\begin{aligned}
 \mu_d^{I3}(x,y,z)&=\frac{3(d-3)!\tau(x)\tau(y)\tau(z)}{d^{d-2}},\\
 \mu_d^{IS}(x,y,z,w)&=
   \frac{2(d-3)!\tau(x)\tau(z)\tau(y+w)}{d^{d-2}},\\
 \mu_d^{IN}(x,y,z,w)&=
   \frac{2(d-3)!\tau(x+z)\tau(y)\tau(w)}{d^{d-2}}.
\end{aligned}
\tag{3.3}
\]

Let \(\operatorname{Emb}_i\) and \(\operatorname{Emb}_{ij}\) embed local
chords back into the global polygon.  The exact conditional law of the next
pair product is

\[
 K_g=
 \sum_i\frac{r_i(r_i-1)}{r(r-1)}\operatorname{Emb}_i\mu_{d_i}
 +\sum_{i<j}\frac{2r_ir_j}{r(r-1)}
       \operatorname{Emb}_{ij}(\nu_{d_i}\otimes\nu_{d_j}).
\tag{3.4}
\]

Proof: the first two colors in a uniform interleaving agree and equal \(i\)
with probability \(r_i(r_i-1)/(r(r-1))\), and are the two distinct colors
\(i,j\) in either order with probability \(2r_ir_j/(r(r-1))\).  Conditional
on the color event, deletion of the first one or two factors and the Cayley
factorization formula give (3.1)--(3.3).  The component factorizations are
independent.  This proves (3.4).  Pushing (3.4) through simultaneous cyclic
conjugation gives the quotient row \(\bar K([g],\cdot)\).

Accordingly every row is a sum of only four schema classes:

\[
 \mathcal S=\{I3,IS,IN,X\},
\]

where \(I3,IS,IN\) use two factors from one residual cycle and \(X\) uses
one factor from each of two residual cycles.  All dependence on the source is
through its three residual sizes, their cyclic embeddings, and the rational
interleaving weights in (3.4).

## 4. An exact collapsed check

Summing (3.4) over three-cycle targets gives

\[
 K_g(\text{three-cycle})=
 \frac{3}{(n-3)(n-4)}
 \sum_{i=1}^3\frac{(d_i-1)(d_i-2)}{d_i}
 =\frac{3\left(n-9+2\sum_i d_i^{-1}\right)}{(n-3)(n-4)}.
\tag{4.1}
\]

Since \(\bar\pi(\text{three-cycle})=3/n\),

\[
 K_g(3)-\frac3n=
 \frac{6\left[n\left(\sum_i d_i^{-1}-1\right)-6\right]}
      {n(n-3)(n-4)}.
\tag{4.2}
\]

Thus the coarse target-kind imbalance is already \(O(n^{-2})\), uniformly
over positive \(d_1+d_2+d_3=n\).  This does not prove the desired bound:
exact computations show mixed signs inside each target kind, so collapsing
to the two kinds destroys necessary within-kind cancellation.

There is a useful explicit uniform version.  Convexity and the extremal
positive composition give

\[
 \frac9n\leq\sum_i\frac1{d_i}\leq2+\frac1{n-2}.
\]

Substitution in (4.2) yields, for every source,

\[
 \left|K_g(3)-\frac3n\right|\leq\frac6{n(n-4)}.
\tag{4.3}
\]

Since a Markov kernel contracts the sup norm, the same bound holds with
\(K_g(3)\) replaced by \(K_g^r(3)\), for every \(r\geq1\).  Thus the kind
projection of the desired common-measure decomposition is already proved at
the required \(n^{-2}\) scale.

## 5. The first-edge law is a conditioned Borel split

Let

\[
 b_j=e^{-j}\tau(j)=e^{-j}\frac{j^{j-1}}{j!},\qquad j\geq1,
\]

the critical Borel(1) law.  Orient an edge drawn from \(\nu_d\) by an
independent fair coin, and let \((U,d-U)\) be its two oriented cyclic gaps.
The coefficient identity (1.1) gives

\[
 \Pr(U=u)=\frac{b_u b_{d-u}}
                 {\sum_{v=1}^{d-1}b_vb_{d-v}}
 =\Pr(B_1=u\mid B_1+B_2=d),
\tag{5.1}
\]

where \(B_1,B_2\) are independent Borel variables.  Hence every cross-cycle
schema \(X\) is exactly a product of two conditioned-Borel chord splits,
followed by deterministic embedding in the three source components.

This exposes both the natural coupling and its limitation.  If
\(S_d=\min(U,d-U)\), then

\[
 \left\|\mathcal L(S_d)-\mathcal L(B_1)\right\|_{\rm TV}
 =\Pr(B_1>\lfloor d/2\rfloor)
 \sim\frac2{\sqrt{\pi d}}.
\tag{5.2}
\]

Indeed the Borel probabilities decrease, and the Borel--Tanner convolution
satisfies
\(\tfrac12\Pr(B_1+B_2=d)=(1-1/d)b_d\).  Therefore the conditional smaller
fragment dominates \(b_j\) on \(j\le d/2\), making its total-variation
excess exactly the missing Borel tail; Stirling gives the asymptotic in
(5.2).  Thus a one-step coupling that retains only the small tree plus a
choice of the giant/root side loses \(\Theta(d^{-1/2})\), far too much for
the target \(O(n^{-2})\).  Any successful coupling has to use the signed
sum over the two steps (or a sharper cancellation retaining both boundary
choices); it cannot bound the four schemas separately by this naive Borel
coupling.

## 6. Common signed decomposition and the sixteen schemas

Compose (3.4) twice.  For \(A,B\in\mathcal S\), let
\(M^{g}_{A,B}\) be the quotient target measure obtained by first applying
schema \(A\) to \(g\), then schema \(B\) to the resulting state, including
the exact interleaving coefficients.  Then

\[
 \bar K^2([g],\cdot)=
 \sum_{A,B\in\mathcal S}M^{g}_{A,B}(\cdot).
\tag{6.1}
\]

Define the stationary schema averages

\[
 Q_{A,B}:=\sum_{[g]}\bar\pi([g])M^g_{A,B}.
\tag{6.2}
\]

Stationarity gives \(\sum_{A,B}Q_{A,B}=\bar\pi\).  Therefore the canonical
common signed decomposition is the exact identity

\[
 \bar K^2([g],\cdot)=\bar\pi+\frac1{n^2}E_g,
 \qquad
 E_g:=n^2\sum_{A,B\in\mathcal S}(M^g_{A,B}-Q_{A,B}).
\tag{6.3}
\]

The analytic task is precisely to prove
\(\sup_g\|E_g\|_{\rm TV}<\infty\).  Neither (6.2) nor (6.3) uses a
macro-lumpability assumption.  The coarse kind projection of \(E_g\) is
uniformly bounded by (4.3); the unresolved part is its signed conditional
distribution inside each kind.

Consequently the whole H0 coordinate-correlation step reduces to the following
finite family of weighted Cayley-convolution sums:

\[
 \sup_{g,g'}\frac12\sum_{[t]}
 \left|\sum_{A,B\in\mathcal S}
       \bigl(M^g_{A,B}([t])-M^{g'}_{A,B}([t])\bigr)\right|
 \le \frac{C}{n^2}.
\tag{6.4}
\]

The absolute value must remain outside the sum over all sixteen ordered schema
pairs; moving it inward loses the cancellation visible in the exact data.
If (6.4) holds, then \(\delta(\bar K^2)\le C/n^2\), so every nonconstant
eigenvalue \(\kappa\) of the self-adjoint H0 kernel obeys
\(|\kappa|^2\le C/n^2\), hence \(\kappa_{\max}=O(1/\ell)\).  Together with
the already proved covariance lower bound \(\kappa_{\min}\ge-1/(\ell-1)\),
this discharges the H0 coordinate-correlation input needed by the M16
accumulation argument.

At present (6.4) is **unresolved**.  It is, however, a finite-schema analytic
obligation rather than an unrestricted overlap enumeration.

## 7. Exact observed extremal family

For \(n=6k+3\), define the balanced-third orbit

\[
 A_k=[2k+1,2k+1,2k+1]_3
\]

and the near-balanced separated-double orbit

\[
 B_k=[2k,k+1,2k,k+2]_S.
\]

The residual sizes are respectively
\((2k+1,2k+1,2k+1)\) and \((2k,2k,2k+3)\).  Put
\(D=6k(6k-1)\).  Formula (3.4) specializes to

\[
\begin{aligned}
 K_{A_k}
 &=\sum_{i=1}^3\frac{2k(2k-1)}D\operatorname{Emb}_i\mu_{2k+1}
   +\sum_{i<j}\frac{8k^2}D
       \operatorname{Emb}_{ij}(\nu_{2k+1}\otimes\nu_{2k+1}),\\
 K_{B_k}
 &=\sum_{i=1}^2\frac{(2k-1)(2k-2)}D
       \operatorname{Emb}_i\mu_{2k}
   +\frac{(2k+2)(2k+1)}D\operatorname{Emb}_3\mu_{2k+3}\\
 &\quad+\frac{2(2k-1)^2}D
       \operatorname{Emb}_{12}(\nu_{2k}\otimes\nu_{2k})
   +\sum_{i=1}^2\frac{2(2k-1)(2k+2)}D
       \operatorname{Emb}_{i3}(\nu_{2k}\otimes\nu_{2k+3}).
\end{aligned}
\tag{7.1}
\]

After quotient pushforward, the exact signed two-step row difference is

\[
 \Delta_k:=\bar K^2(B_k,\cdot)-\bar K^2(A_k,\cdot)
          =(K_{B_k}-K_{A_k})\bar K,
\tag{7.2}
\]

with the two parenthesized measures given explicitly by (7.1) and each
second row by (3.4).  Thus (7.2) is an explicit sum of the sixteen schemas,
not a numerical definition.  At the first member \(k=1\), exhaustive exact
maximization over all \(n=9\) quotient-row pairs proves that this is a
Dobrushin maximizer and gives

\[
 \|\Delta_1\|_{\rm TV}
 =\frac{15514386669199}{114865340625000}.
\tag{7.3}
\]

Its exact signed mass on double targets is \(21076/590625\), and the
three-cycle mass is its negative.  The complete rational target-orbit vector
is stored in `h0_coordinate_correlation_n9.json`.  Floating enumeration
identifies the same family, up to the nearest integer four-composition, at
\(n=15\); related balanced-third/near-balanced-double pairs maximize through
\(n=21\).  These are finite calibrations only.

The simplest possible closure is false: \(\bar K^2(g,\text{kind})\) is not
determined solely by the three unordered residual sizes.  At \(n=7\), a
three-cycle and a nested double having the same residual sizes \((3,2,2)\)
have two-step three-cycle masses differing numerically by
\(0.1199074074\); the exact kernel artifact supplies a finite falsifier.
Thus source color/embedding is a genuine counterterm, although the measured
counterterm itself decreases at the target \(n^{-2}\) scale.

## 8. A diameter-two source metric

Let \(\Gamma_n\) have the \(\theta\)-orbits in \(X\) as vertices.  Join two
vertices when representatives admit ordered transposition-pair lifts which
agree in their first coordinate or agree in their second coordinate.

**Proposition 8.1 (proved).**  For every odd \(n\ge5\), \(\Gamma_n\) has
diameter at most two.

**Proof.**  Choose lifts \((a,b)\) of a representative of the first orbit
and \((c,d)\) of a representative of the second.  The endpoints of the
chord \(a\) cut the odd \(n\)-gon into arcs, the larger having length
\(L\ge(n+1)/2\).  Let \(k\le(n-1)/2\) be the shorter cyclic length of
\(d\).  If \(k\le L-2\), rotate \(d\) so both its endpoints lie strictly
inside the larger arc.  It is then disjoint and noncrossing with \(a\), so
their ordered product \(p=a\theta^r(d)\) is an admissible double
transposition.  In the only remaining case, \(L=(n+1)/2\) and
\(k=(n-1)/2\); place \(\theta^r(d)=(x,z)\) sharing an endpoint with
\(a=(x,y)\), with cyclic order \(x,z,y\).  Then
\(a\theta^r(d)=(x\,z\,y)\), the admissible orientation.  Thus \(p\in X\).
Its lift \((a,\theta^r(d))\) shares the first coordinate with \((a,b)\)
and the second with the rotated lift
\((\theta^r(c),\theta^r(d))\).  This is a path of length at most two. QED.

This reduces the full rowwise smoothing problem to one local influence.

> **SHARED-FACTOR TWO-STEP INFLUENCE (unresolved).**  There is an absolute
> constant \(C\) such that whenever adjacent vertices \(O,O'\) of
> \(\Gamma_n\) have lifts \((a,b)\) and \((a,b')\) (or the analogous
> shared-second-factor lifts),
> \[
>  \|\bar K^2(O,\cdot)-\bar K^2(O',\cdot)\|_{\rm TV}\le \frac C{n^2}.
> \tag{8.1}
> \]

Indeed Proposition 8.1 and the triangle inequality would give
\(\delta(\bar K^2)\le2C/n^2\), and hence
\(|\kappa|^2\le2C/n^2\) on every nonconstant invariant eigenmode.

There is also a useful data-augmentation formulation.  Let
\((G,S)\) have the exact symmetric quotient joint law
\(\bar J(O,P)=\bar\pi(O)\bar K(O,P)\).  Conditional on \(G=O\), sample
\(S\), then sample \(G'\) from the posterior conditional on \(S\).  The
law of \(G'\) is exactly \(\bar K^2(O,\cdot)\).  Thus (8.1) is a
strong-data-processing bound for two posterior predictives whose initial
rank-two products share one raw transposition.  In the residual-forest
description, the two sources agree through deletion of that common chord;
only the choice of the next chord differs.  This is the sharp coupling
interface suggested by (5.1), while retaining the full signed sum avoids
the \(d^{-1/2}\) loss in (5.2).

A stronger sufficient statement, also unresolved, is the uniform
chi-square estimate

\[
 \sup_O\chi^2\!\left(\bar K^2(O,\cdot)\,\middle\|\,\bar\pi\right)
 \le \frac C{n^4}.
\tag{8.2}
\]

By Cauchy--Schwarz it implies a uniform \(O(n^{-2})\) TV row bound.  More
directly, for mean-zero \(f\), (8.2) gives
\(|\bar K^2f(O)|\le\sqrt C\,n^{-2}\|f\|_2\), so
\(|\kappa|\le C^{1/4}/n\).

Exact exhaustive checks give

\[
\begin{array}{c|c|c|c}
n&\operatorname{diam}(\Gamma_n)&
n^2\max_{O\sim O'}\|\bar K^2_O-\bar K^2_{O'}\|_{TV}&
n^4\max_O\chi^2(\bar K^2_O\|\bar\pi)\\ \hline
7&2&11.5914513&510.4436871\\
9&2& 8.6538347&446.0189252
\end{array}
\]

At \(n=7\), the exact adjacent maximum is \(7185517/30375000\); at
\(n=9\), it is \(2094407996609/19603684800000\).  Floating checks through
\(n=21\) keep the diameter equal to two, the adjacent \(n^2\)-scaled TV
between \(6.72\) and \(7.36\) for \(n\ge11\), and the uniform
\(n^4\)-scaled chi-square below \(343\) there.  These finite facts do not
prove (8.1) or (8.2).

## 9. Why fixed Schatten moments are not the primary route

Although \(\ell^2\operatorname{Tr}(L_0^2)\) stays between \(4.99\) and
\(6.13\) through \(n=21\), its positive source-row decomposition has a
harmonic boundary profile.  At \(n=21\), the contributions grouped by
minimum residual size \(k=1,\ldots,7\) are

\[
 2.141,\ 1.261,\ .845,\ .580,\ .383,\ .194,\ .029.
\]

Their bulk is approximately proportional to \(1/k\).  The fourth moment
shows a weaker version of the same profile.  This is finite evidence, not a
proof of logarithmic divergence, but it invalidates treating the apparently
flat total trace as a safe route to a uniform constant.  The rowwise
influence (8.1) suppresses precisely these many boundary modes and is the
preferred remaining lemma.
