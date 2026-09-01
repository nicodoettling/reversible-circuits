# R2 plan: positive branch-weight sampling

Date: 2026-09-01 UTC

## Target

For maps composed by `(alpha beta)(x)=alpha(beta(x))`, sample an actual
labeled pair `(k,h)`, `0<=k<=L`, `h in H=S_(N-1)`, with exact branch weight

```text
binom(L,k) A_(N-1,L-k)(h) B_(N,k)(h^(-1)g),
```

where `A_(r,s)(h)=[h]C_r^s` and `B_(N,k)(q)=[q]J_N^k`.  The external endpoint
`g` is arbitrary feasible; identity is only the public top-level endpoint.

## Named questions

1. Does the emerging positive prescribed-star endpoint formula make the
   *joint labeled* `h` law polynomial-time, rather than only making
   `B_(N,k)(q)` polynomial-time evaluable?
2. What is the smallest positive exact compression of the branch law by the
   cycle type of `h`, the pointed cycle type of `h^(-1)g`, and their labeled
   connection multiplicity?  State its exact state count and prove only a
   scoped obstruction if that table is superpolynomial.
3. Can dense pointwise flattening yield a genuinely samplable positive law?
   I will analyze two complementary regions: flatten the old walk when
   `L-k` is long, and flatten the star walk when `k` is long.  This avoids an
   uncontrolled middle or tail because one of the two lengths is at least
   `L/2`.
4. Give exact integer algorithms for the flattened branch normalizers and an
   actual labeled `h`, with arithmetic bit complexity and no enumeration of
   `S_(N-1)`.

## Proposed dense construction to prove or falsify

Let `d=binom(N-1,2)`, `b=N-1`, `a=g^(-1)(N)`, and `s=L-k`.

- If `s>=k`, replace the old endpoint walk by uniform on its parity class.
  Then the remaining exact star mass is the number `S_k(a)` of star words
  whose endpoint `q` satisfies `q(a)=N`.  This has a positive two-state token
  recurrence and a backward sampler; set `h=gq^(-1)`.
- If `k>s`, replace the star endpoint walk by uniform on its parity class.
  Then sample an unconditioned length-`s` old word and return its actual
  endpoint `h`.

After multiplying by a common denominator, the proposed integer `k` weights
are

```text
N binom(L,k) d^s S_k(a)     when s>=k,
  binom(L,k) d^s b^k        when k>s.
```

I will derive pointwise relative spectral bounds for both nonlazy periodic
walks, normalize them rigorously, and specialize them at `L=2N^3`.  Exact and
approximate laws will be kept separate; a fixed negligible bound is not the
same as supporting every requested `epsilon`.

## Exact compression audit

For partitions `lambda` of `N-1` and pointed types `mu`, define

```text
M_g(lambda,mu) = # {h in H : type(h)=lambda,
                              pointed_type(h^(-1)g)=mu}.
```

This gives a positive branch representation with weights
`A_s(lambda) B_k(mu) M_g(lambda,mu)`.  I will count its declared state
inventory and show any superpolynomial conclusion only for the implementation
that explicitly tables these cells.  A generating-function or direct
connection sampler remains a surviving alternative unless separately ruled
out.

## Validation and boundaries

Add a standard-library exact harness for small `N,L` that compares the exact
branch law with both positive constructions, checks the token recurrence and
labeled output, measures exact total variation, and checks `N=2`, `L=0`, odd
lengths, minimal endpoints, and pair padding.  Use exact integers/fractions;
record command, Python version, commit, and machine-readable results.

The run uses no package installation and writes only this role directory.
Pre-existing repository changes are preserved.
