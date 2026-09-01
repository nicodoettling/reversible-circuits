# Halfway checkpoint: ordinary braid-abelian cuts are polynomial

## Frozen first-half claim

Let `F` be any identity-product Hurwitz orbit of length `m>=2` in any
group, and let

    P_H = (1/2) I
          + [1/(4(m-1))] sum_i (R_i+R_i^{-1})

be the lazy symmetric Hurwitz walk, with
`R_i(a,b)=(b,b^{-1}ab)`. Suppose a surjective coordinate
`phi:F -> Z/qZ` satisfies

    phi(R_i x) = phi(x)+1 mod q

for every `x` and every `i`. Then

    q divides m(m-1).

The pushforward of uniform measure on `F` is uniform on `Z/qZ`, and the
pushforward chain is exactly

    C_q(z,z)=1/2,  C_q(z,z+1)=C_q(z,z-1)=1/4,

with the two off-diagonal contributions combined when `q=2`. Its spectral
gap is

    gap(C_q)=sin^2(pi/q) >= 4/q^2

for `q>=2`. For every nonempty proper `B subset Z/qZ`, the preimage cut
`A=phi^{-1}(B)` has

    Phi_pm(A)
      = Q_F(A,A^c)/min(pi_F(A),pi_F(A^c))
      >= 1/q
      >= 1/[m(m-1)].

For an interval `B` of `k<=floor(q/2)` consecutive residues, the exact
quantities are

    pi_F(A)=k/q,
    Q_F(A,A^c)=1/(2q),
    Phi_pm(A)=1/(2k).

Thus no cut visible only to an ordinary braid-abelian cyclic coordinate can
be a superpolynomial bottleneck.

## Full argument and normalization

Write `delta=R_1 R_2 ... R_{m-1}`, with moves applied in the displayed
order, and let `P=g_1...g_m`. One sweep gives

    delta(g_1,...,g_m)
      =(g_2,...,g_m,P^{-1}g_1P).

Indeed, after moving `g_1` to the right, the last factor is
`(g_2...g_m)^{-1}g_1(g_2...g_m)=P^{-1}g_1P`. Product preservation lets the
same formula be iterated, so

    delta^m(g_1,...,g_m)
      =(P^{-1}g_1P,...,P^{-1}g_mP).

On an identity orbit `P=id`; hence the full twist `delta^m` fixes every
state. It is a positive braid word with `m(m-1)` generators. Equivariance of
`phi` therefore gives `m(m-1)=0 mod q`.

Every `R_i` is a bijection from the fiber `phi^{-1}(z)` to
`phi^{-1}(z+1)`, so all fibers have equal cardinality. In one `P_H` step,
laziness contributes `1/2`, the `m-1` positive generators contribute total
`1/4` to `z+1`, and the `m-1` inverse generators contribute total
`1/4` to `z-1`. This proves exact lumping.

For `q>=3`, each nontrivial subset of the cycle has at least two undirected
boundary edges. Each such edge contributes exactly
`(1/q)(1/4)=1/(4q)` to directed stationary flow from `B` to `B^c`.
The same formula, with the two generator orientations counted separately,
holds at `q=2`. Hence `Q(B,B^c)>=1/(2q)`; division by a smaller-side mass
at most `1/2` gives at least `1/q`. The interval formulas follow because
there are exactly two boundary contributions. Reversibility gives the equal
reverse flow `Q(A^c,A)`.

The same conclusion covers every finite abelian character of the braid group:
the braid relations make all standard generators equal in the abelianization,
so its image is cyclic. If their common image is not a chosen generator,
replace `q` by its order on the actual image.

### Post-freeze sharpening

The audited Classification H and paired-representative construction make the
conclusion stronger for the project orbits: **no nontrivial coordinate of this
kind exists**. Every feasible identity-transposition orbit contains a word

    (s_1,s_1,s_2,s_2,...,s_{m/2},s_{m/2}).

At that state, the Hurwitz generator on any displayed equal pair is the
identity. Equivariance would give `phi(x)=phi(x)+1`, hence `q=1`.
Equivalently, a point stabilizer contains a conjugate of a standard braid
generator. Any normal kernel containing that stabilizer contains the normal
closure of a standard generator, which is all of `B_m`. Thus **every
homomorphic normal quotient of the Hurwitz action is trivial**, not merely
every abelian one.

## Status and self-attack

**PROVED** for the named braid-abelian candidate family. This is not a lower
bound on the full Hurwitz Schreier graph. Nonnormal coset geometry and
state-dependent statistics are not homomorphic quotients. They may still form
a barbell even though all normal quotient modes are absent.

## Second-half work now underway

The remaining attack uses the minimal full-support orbit
`m=2(N-1)`. I will:

1. prove the universal local description of prefix join/cut paths and join
   trees under one Hurwitz move;
2. enumerate only `S_3,m=4` and `S_4,m=6` to falsify named uniform-tree,
   Markov-projection, or local-boundary conjectures;
3. attempt an exact infinite cut calculation for any statistic that survives;
4. otherwise isolate the nonabelian Schreier-gap proposition as the first
   unproved step.

No finite computation will be used to infer asymptotic mixing.
