# M127 plan: fixed-braid intertwining for DPS adjacent values

Date: 2026-08-13 UTC.

## Objective

Decide the exact proposition that, for every `d` and adjacent value index
`i`, one signed Hurwitz action word `beta_(d,i)`, independent of the rooted
Cayley tree and permutation coordinate, maps every DPS output
`F(T,pi)` to `F(T,s_i pi)`.

## Target and convention

The auxiliary target is uniform on the connected minimal identity sector

```text
Z_d={w in T_d^(2d-2): eval(w)=id and support(w) is connected}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  Signed Hurwitz generators are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

The DPS `+`-mirror convention and root at `y_d` are those accepted in
M112/M119 and audited again in M122/M126.

## Claim tests

1. Exhaust every `(T,pi)` at `d=3,4` and every adjacent value index.
2. First test whether the rooted edit descends through the exact `d`-to-one
   forgetful map to a function on physical words.  A source-word collision
   with two distinct target words refutes every source-independent action.
3. Where descent survives, compute the simultaneous action-table constraint
   and search the finite image of the signed braid action, distinguishing a
   fixed braid word from an arbitrary permutation of `Z_d`.
4. Isolate the smallest metadata class on which the edit is well-defined,
   and state exactly what source recovery or root factor remains.

## Expected failure modes

- The adjacent-value edit may depend essentially on the forgotten white root.
- It may descend to words but not lie in the diagonal braid-group action on
  all sources.
- Small-rank survival would be finite evidence only unless an explicit
  universal braid identity is proved.
- No result here by itself bounds all-descriptor congestion, a physical gap,
  `Gamma_0`, the original heat-bath gap, or either terminal outcome.

## Reproduction standard

Use deterministic Python 3 with no nonstandard dependency and `seed=null`.
Record the repository commit, exact command, complete JSON results, proof or
counterexample note, nine-field report, freeze manifest, and SHA-256 sums.
