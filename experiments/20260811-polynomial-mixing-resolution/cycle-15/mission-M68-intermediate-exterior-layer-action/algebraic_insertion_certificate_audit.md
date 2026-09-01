# M68 audit: algebraic insertion certificates and fractional marks

## 1. Exact direct-certificate law

Fix a connected identity-factorization fiber on a fixed labeled `d`-set,
with length

```text
k=2(d-1)+2g,        g>=1,
```

and uniform law `pi_g`.  A direct insertion certificate is a marked adjacent
square whose deletion leaves a connected word in the genus-`g-1` fiber.  If
`r(w)` is the number of such marked positions, the exact insertion/deletion
bijection gives

```text
S:=sum_w r(w)=(k-1) binom(d,2) C_(g-1)(d),           (1.1)
mu:=E_pi_g r=S/C_g(d).                               (1.2)
```

The accepted positive DYZ recurrence consequence is

```text
[C_g(d)/k!]/[C_(g-1)(d)/(k-2)!] <= d^3/12.          (1.3)
```

Therefore

```text
mu>=12 binom(d,2)/(d^3 k)=6(d-1)/(d^2 k).           (1.4)
```

Let `nu` be uniform on all `S` direct certificates and forget the mark.  Its
density relative to the uniform word law is exactly

```text
d nu_proj/d pi_g (w)=r(w)/mu.                        (1.5)
```

Since `r(w)<=k-1`, (1.4) gives the polynomial upper bound

```text
r(w)/mu <= (k-1)d^2 k/[6(d-1)] <= d k^2/3.          (1.6)
```

Thus the incidence identity does provide a clean polynomial *upper* RN
bound for direct marked words.  It provides no positive lower RN bound:
`r(w)` can be zero.  The exact N=5 two-deletion and four-null artifacts give
explicit zero-certificate words.  Weighting each existing certificate by
`1/r(w)` makes the projection uniform on `{r>0}` but still assigns zero mass
to its complement.

This is the exact limit of what (1.1) alone proves: a polynomial-mass marked
reservoir with controlled upper density, not a marked lift of every word.

## 2. Transporting the whole insertion certificate

A concrete direct certificate is `(z,p,e)`, where `z` is the connected
genus-`g-1` word, `p` an insertion gap, and `e` the inserted square edge.
To transport it from `I(z,p,e)` to a current word `w` under Hurwitz moves,
one must also retain a braid/coset carrying the inserted branch points.  The
tuple `(w,z,p,e)` alone is not enough to update locally: two braid histories
can have the same current factor tuple and the same deletion data but
different winding of the connecting arc.

The pure-braid example in `enhanced_marked_handle_audit.md` makes this exact.
For

```text
w=a_M^2 b^2 c^2 a^2,
a=(01), b=(23), c=(12),                              (2.1)
```

the pure braid `sigma_2^2` between the second marked `a` and the commuting
unmarked `b` fixes the factor tuple and returns the colored positions.  After
forgetting the marked strands, it induces the trivial braid on the remaining
word `z=b^2c^2a^2`, so the concrete algebraic deletion data are also the same.
But its powers give distinct twists of the connecting arc.  Hence:

- retaining enough history to make the local action invertible produces the
  infinite full-arc fiber;
- collapsing all these histories to `(w,z,p,e)` makes the local transported
  action non-injective/not well-defined.

This is a sharp monodromy obstruction to the literal “carry `(z,p,e)` and
re-reduce after every generator” prescription.

## 3. Why canonical re-reduction does not repair it

There are only two interpretations of canonical re-reduction.

1. **Re-reduce to a direct certificate of the current word.**  This is
   undefined whenever `r(w)=0`, including the exact N=5 counterexamples.
2. **Choose a separate insertion representative and a canonical braid path
   to the current word.**  This is always possible qualitatively, but a single
   generator of the word chain can reset the entire canonical path.  The two
   marked positions no longer follow the adjacent-card chain.  Bounding the
   loads of these resets is precisely a canonical-path/multicommodity-flow
   problem; the incidence ratio (1.4) supplies no such congestion estimate.

A randomized re-reduction is the fractional version of case 2.  To use it,
one must construct conditional distributions on insertion representatives
and braid histories such that every literal edge has polynomial aggregate
preimage load.  That is exactly the short bijective marked-cover proposition
in `recovery_obstruction.md`, not a consequence of the one-point density
(1.5).

For contrast, the product lift `Gamma x D` with a static insertion
certificate `D` has constant fibers and projects exactly uniformly, but the
static certificate has no algebraic relation to the current word and cannot
certify any literal square refresh.

## 4. Scoped verdict for the alternative

The exact incidence law proves polynomial marked-reservoir mass and an upper
RN density at most `d k^2/3`.  It does **not** turn the enhanced handle into a
polynomial finite cover.  Pure-braid monodromy forces either infinite history
fibers or a noninvertible canonical collapse, and zero-direct-certificate
words prevent pointwise re-reduction.

The smallest surviving proposition remains the **FINITE HANDLE-FRAMING
QUOTIENT / SHORT BIJECTIVE MARKED-COVER**: construct a finite equivariant
quotient that retains enough winding data for actual deletability while
having polynomial fibers and polynomial projected edge load.  No such
quotient or a superpolynomial lower bound against every quotient is proved
here.
