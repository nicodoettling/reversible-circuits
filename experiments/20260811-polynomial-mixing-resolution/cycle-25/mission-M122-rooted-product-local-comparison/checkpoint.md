# M122 halfway checkpoint

Date: 2026-08-12.

## Exact progress

The full ROOTED PRODUCT LOCAL COMPARISON is not proved.  A clean infinite
family gives both a rigorous obstruction to bounded output locality and an
exact source-recoverable physical route through that worst cascade.

Use zero-based sheet labels.  For every `d>=3`, let `T_d` be the Cayley star
centered at `0`, rooted at `d-1`, and let `pi=id` in `S_(2d-2)`.  Under the
accepted `+`-mirror DPS closure, the rooted state and the ideal adjacent-value
swap of values `1,2` have words

```text
h,h,(0,1),(0,1),...,(0,d-2),(0,d-2),
h,h,(1,d-1),(1,d-1),...,(d-2,d-1),(d-2,d-1),
h=(0,d-1).
```

Thus one adjacent ideal permutation edit changes exactly `2d-4` of the
`2d-2` physical factors.  Since one signed adjacent-Hurwitz move changes at
most two coordinates, every physical path has length at least `d-2`.
Consequently the named premise

> every adjacent DPS face-label swap changes only `O(1)` output factors, or
> admits an `O(1)` signed-Hurwitz simulation

is **REFUTED** by an explicit infinite family.  A proof directly from the
DPS contour/stack algorithm is being frozen; exact evaluation through `d=15`
has zero failures but is not used as the universal proof.

The cascade is nevertheless polynomially routable.  More generally, for a
transposition `h` and a transposition word `U=(u_1,...,u_L)` with product
identity, assume the last factor `u_L` equals `h` or shares one endpoint with
`h`.  Then the fixed signed braid word

```text
R_2 R_3 ... R_L  R_(L+1)^(-1)  R_L ... R_3 R_2
```

(indices are one-based factor-pair positions in `(h,h,U)`) maps

```text
(h,h,u_1,...,u_L)
    -> (h,h,h u_1 h,...,h u_L h).
```

It has length `2L-1`; for the star family this is `4d-9`.  The endpoint
incidence hypothesis is necessary for this displayed derivation: a disjoint
last transposition gives a direct counterexample.  The action sequence depends
only on `L`, so a physical oriented edge, path time, and this route descriptor
recover the source uniquely by applying the inverse prefix.  This is an exact
ideal-edge path/source-recovery statement, not a congestion theorem for all
ideal edges.

### Subsequent strengthening before freeze

The endpoint-incidence condition is unnecessary if the shorter action word is
replaced by the full twist on the subtuple `(h,u_1,...,u_L)`:

```text
(R_2 R_3 ... R_(L+1))^(L+1).
```

Its subtuple product is `h`, so a direct cyclic-shift calculation shows that
it conjugates every subtuple factor by `h`.  This gives the same target for
every identity suffix `U`, has scheduled length `L(L+1)`, and retains unique
source recovery by prefix inversion.  The disjoint-last-factor example only
refutes dropping the hypothesis from the shorter `2L-1` word.  The final proof
note keeps both the universal full twist and the sharper star-family route.

## Immediate remaining work

- Write the algebraic induction and the DPS star-contour proof in full.
- Implement an independent deterministic audit recording the formulas,
  factor-change lower bound, path endpoint, and prefix-inversion recovery;
  add exact `d=3,4` coverage summaries and fixed-seed `d=5` samples only if
  they decide a broader claim.
- Test whether every adjacent-value edit decomposes into polynomially many
  square-prefix conjugations plus bounded local braid moves.  If not, isolate
  the first precise failing descriptor rather than claiming a global
  obstruction from finite data.

## Current verdict

`KEEP` candidate: a rigorous linear-cascade obstruction plus a matching
fixed-braid source-recoverable route for that family.  The global rooted
product comparison and arbitrary-product `Gamma_0` remain unresolved.
