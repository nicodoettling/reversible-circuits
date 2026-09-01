# A polynomial signed marked cover for the voltage symmetry class

All statements are **proved** unless explicitly labeled otherwise.  The
composition convention is `(pq)(x)=p(q(x))`; tuple factors are evaluated
left-to-right; and

```text
R_i(a,b)=(b,bab),             R_i^(-1)(a,b)=(aba,a).
```

The result bypasses M84's zero row on a structured source class.  It is not a
cover of a whole Hurwitz macro, a full exterior-flow theorem, or a statement
about the spectral gap of the heat-bath chain.

## 1. The voltage word and a fixed marked target

Fix `L>=1` and put

```text
d=8L^2,                 k=16L^2=2d.
```

Let `W_L` be the accepted M78/M81 voltage word on vertices
`0,...,d-1`.  It is a connected identity transposition word of length `k`.
Define

```text
C_d=(01)^2 (12)^2 ... ((d-2)(d-1))^2 (01)^2.       (1.1)
```

It has length `2(d-1)+2=2d=k`, evaluates to identity, and has connected
support.  Deleting the final `(01)^2` leaves the doubled path

```text
(01)^2 (12)^2 ... ((d-2)(d-1))^2,                 (1.2)
```

which is still a connected identity word.  Thus the final square of `C_d`
is a literal connected two-deletion certificate.

## 2. A single fixed signed braid from `W_L` to `C_d`

The accepted quantitative Classification-H construction (M13, ledger
L-0037) is algorithmic.  Its componentwise procedure applies only literal
generators `R_i^{+/-1}` and brings a connected identity word on `d` vertices
with `k` factors to a componentwise canonical word.  The counter audit gives
at most `25 d k^3` moves from each source to that canonical word and hence at
most

```text
50 d k^3                                                   (2.1)
```

generators between any two words with the same labeled weighted component.

Make the construction deterministic as follows.  Order vertices and factor
occurrences lexicographically.  In every invocation of its Lemma 3.9, choose
the lexicographically first shortest support path and then the earliest
eligible occurrences in the orientation prescribed by the proof.  In every
Lemma 3.10 pair reordering, choose the leftmost required supporting pair.
All searches are graph breadth-first searches or linear scans, and all local
rewrites are the displayed signed Hurwitz generators.  Hence the audit's
loop bound is also a polynomial running-time bound for emitting the index/sign
sequence.

Run the deterministic algorithm from each of the two public templates
`W_L,C_d` to the same componentwise canonical word and reverse the second
path.  This avoids needing any unproved identification of the audit's
tie-broken canonical output with (1.1).  Call the resulting literal word

```text
beta_L,       beta_L(W_L)=C_d,       |beta_L|<=50 d k^3.     (2.2)
```

Although the precomputation inspects the fixed template, application of the
stored sequence `beta_L` has no adaptive branch.  It is one source-independent
bijection.

For every permutation `sigma` of the symbol labels, Hurwitz action is
equivariant generator by generator:

```text
sigma(bab)sigma^(-1)
 =(sigma b sigma^(-1))(sigma a sigma^(-1))(sigma b sigma^(-1)).  (2.3)
```

The same holds for `R_i^(-1)`.  Therefore

```text
beta_L(sigma W_L)=sigma C_d.                       (2.4)
```

No braid depending on `sigma` is needed.

## 3. Literal correction of cyclic phases

On `k` positions define

```text
rho_k=R_0 R_1 ... R_(k-2).                         (3.1)
```

If `u=(t_0,...,t_(k-1))` has identity product, bubbling `t_0` to the right
gives

```text
rho_k(u)=(t_1,...,t_(k-1), S^(-1)t_0S),
S=t_1...t_(k-1).
```

Since `t_0S=id` and `t_0` is an involution, `S=t_0`, so the final factor is
`t_0`.  Thus `rho_k` is literal cyclic left shift on every identity word.
Its inverse word is

```text
rho_k^(-1)=R_(k-2)^(-1)...R_0^(-1),                (3.2)
```

the cyclic right shift.  Correcting phase `q`, `0<=q<k`, costs exactly
`q(k-1)` generators.  Its worst cost is `(k-1)^2`; under uniform `q` its
expected cost is `(k-1)^2/2`.

## 4. Literal correction of the ambient pair interleaving

Adjoin two new vertices and the disjoint pair edge `e=(d,d+1)`.  An
interleaving is indexed by

```text
I={a,b} subset {0,...,k+1},        a<b.             (4.1)
```

Let `S_I` first apply `R_b,R_(b+1),...,R_k`, then
`R_a,R_(a+1),...,R_(k-1)`.  On a word whose two `I`-slots are `e,e` and all
other factors avoid `d,d+1`, every one of these moves is a disjoint
commutation.  It stably preserves the relative order of the genus-one factors
and moves `e,e` to the final two positions.  Its exact length is

```text
|S_I|=(k+1-b)+(k-a)=2k+1-a-b<=2k.                 (4.2)
```

Over uniform `I`, symmetry gives `E(a+b)=k+1`, hence

```text
E_I |S_I|=k.                                       (4.3)
```

The formula for `S_I` is a fixed positive braid word even when applied to a
source whose actual pair slots differ from `I`; it remains a bijection on the
whole macro.  Only its successful action at the matching index is used.

## 5. The indexed cover theorem

Let `sigma` range over arbitrary global relabelings of all `d+2` vertices,
let `0<=q<k`, and let `I` range over (4.1).  Define the natural voltage
symmetry class

```text
X_L={ Interleave_I(sigma rho_k^q(W_L), sigma(e),sigma(e)) }.    (5.1)
```

For each fixed labeled component partition, its corresponding slice
`X_(L,Gamma)=X_L intersect Gamma` lies in one two-component minimal exterior
macro `Gamma`; allowing all `sigma` compactly represents the analogous slices
for all relabelings of that construction.

For each indexed pair `(I,q)`, define the literal ambient braid

```text
gamma_(I,q)=S_I rho_k^(-q) beta_L,                 (5.2)
```

where the latter two words use only the first `k` positions after `S_I`.
For a source `x_(sigma,q,I)` with the matching metadata, Sections 2--4 give

```text
gamma_(I,q)(x_(sigma,q,I))
  =sigma(C_d),sigma(e),sigma(e).                   (5.3)
```

The final square inside `sigma(C_d)` is globally adjacent, belongs to
the genus-one component, and deletion leaves that component connected.
Thus (5.3) is in M75's literal marked set.

Choose `(I,q)` uniformly and independently of the source.  The indexed
family has

```text
P_L=k binom(k+2,2),        eta_L>=1/P_L.            (5.4)
```

Different indices may represent the same braid-group element or the same
endpoint on a symmetric source.  That causes no loss: the probability law is
on indexed words, and the one matching index still has mass `1/P_L`.

Using (2.2), (3.2), and (4.3), its expected length satisfies

```text
Dbar_L
 <=50 d k^3 + [(k-1)/2](k-1)+k
 =50 d k^3 +(k-1)^2/2+k.                           (5.5)
```

The separate worst-word bound is

```text
max_(I,q)|gamma_(I,q)|<=50 d k^3+(k-1)^2+2k.       (5.6)
```

It is sampled and emitted in polynomial time: sample `I,q`, emit the two
bubble lists, and append the once-precomputed deterministic `beta_L`.

Every prefix of every `gamma_(I,q)` is a bijection.  Consequently word index,
prefix time, and an actual directed edge determine at most one original
source by applying the inverse prefix.  This remains true with parallel
family entries and is exactly the source-recovery condition in M75's accepted
first-crossing theorem.

## 6. Exact heat-bath/coarea accounting on the covered class

Put

```text
n=d+2,       m=k+2=2n-2,       M=binom(n,2).
```

M75 proves that every specified signed Hurwitz generator used above is a
padded length-three same-product heat-bath outcome of probability at least

```text
p_H=1/[6(m-2)M^2].                                 (6.1)
```

The designated marked refresh has exact probability
`1/[6(m-2)D_n]`, where `D_n=(3n^2+n-12)/2<=M^2`, so it is also at least
`p_H`.

Fix one labeled macro `Gamma` and apply M75's edge charging only to starting
sources in `X_(L,Gamma)`.  For every `S subseteq X_(L,Gamma)`, first exit from
`S` or the terminal refresh gives

```text
sum_(x in S) K(x,(Gamma minus S) union (F_n minus A))
 >= p_H |S|/[P_L max(Dbar_L,1)].                   (6.2)
```

The endpoint version is used, because (5.3) is marked at the endpoint.  A
wrong family index may leave `X_L`; if it leaves `S`, that is already a valid
first boundary crossing.  Inverse-prefix recovery in Section 5 bounds the
weighted load exactly as in M75.

Equation (6.2) is polynomial in `n,m` and is a genuine arbitrary-subset
coarea statement **inside the covered class**.  It says nothing if a partial
macro contains negligible `X_L` mass, so it does not close the arbitrary
two-component macro lemma.

## 7. A signed-distance lower bound for the same source

The following complementary statement explains why the bypass cannot have
uniformly bounded length.

**Lemma 7.1 (crossing-voltage bound).**  Suppose a signed Hurwitz word of
length `q` sends `W_L` to a word with a safe adjacent equal pair.  If `V` is
the projected integral voltage of the corresponding pair-annulus core pulled
back to the original chronological torus, then

```text
|V_x|<=2q+2,             |V_y|<=2q+2.              (7.1)
```

**Proof.**  Mark the two factor occurrences forming the endpoint pair and
trace their two band strands backward through the signed braid diagram.  At
the endpoint, the annular core uses the two marked band cores.  Under one
inverse local Hurwitz rectangle:

- if neither marked strand meets the rectangle, the traced annulus is
  unchanged there;
- if one marked strand is the conjugated strand, each of its two endpoint
  tracks either stays fixed or follows the other band once; a transposition
  can move at most the two displayed endpoint tracks;
- if both marked strands meet the rectangle, the same local picture applies
  to the sole conjugated output strand; for equal factors the move is
  literally fixed.

Thus one signed generator inserts or removes at most two signed traversals of
the other factor-occurrence band in the pulled-back skeleton.  This count is
made in the braid diagram, with occurrence bands carried through all earlier
homeomorphisms; pulling all the way back sends each such carried band to its
single original occurrence band, so there is no recursive expansion into a
current transposition path.  The two marked closing bands contribute the
initial `2`.  Every original `W_L` band has each base voltage coordinate in
`{-1,0,1}`.  The triangle inequality proves (7.1).  This case split includes
a generator in which a marked pair strand itself participates.  QED.

Safety makes the endpoint pair curve nonseparating.  Hurwitz ribbon slides
are homeomorphisms, so its pullback is an embedded nonseparating curve on the
original torus.  M84's accepted integral cover calculation therefore gives

```text
V in L Z^2 minus {(0,0)}.                           (7.2)
```

At least one coordinate has magnitude at least `L`; combining (7.1)--(7.2)
gives

```text
q >=(L-2)/2.                                       (7.3)
```

This is a lower bound on the number of signed Hurwitz generators and hence
on the number of specified padded-`H3` path steps.  It is not a lower bound
on unrestricted heat-bath distance, because one `H4` or `H5` update need not
follow the tracked signed braid.  Since `n,m=Theta(L^2)`, (7.3) is only
polynomial and is compatible with the cover in Section 5.

## 8. What remains for the exterior route

The accepted M84 obstruction and the present bypass together leave the exact
standalone obligation:

> **ARBITRARY-MACRO NONCANONICAL MARKED-COVER LEMMA.**  For every
> two-component minimal exterior macro, construct one polynomial-time
> state-independent law on bijective local transport words, with polynomial
> expected length and inverse-polynomial worst-source marked hit probability;
> or prove a direct arbitrary-partial-macro first-boundary flow inequality
> with polynomial actual-edge occupation.

Classification H gives a polynomial state-dependent route from every source
to `C_d`, but turning the adaptive normalizer into one law for an arbitrary
macro could require exponentially many branch words.  The symmetry collapse
in Sections 2--5 works for `X_L` because every source differs from one public
template only by transformations corrected by polynomial metadata.  No such
polynomial metadata parametrization is proved for a whole macro.

The cases of odd `m`, `m=0`, `m=2`, and `N=2` do not instantiate the
positive-genus two-component geometry and are outside this theorem.
