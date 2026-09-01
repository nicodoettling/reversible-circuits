# M01 Plan: Classification and Irreducibility Closure

## Objective

Prove qualitative irreducibility of the exact lazy `{3,4,5}` same-product
heat-bath chain on `Omega(N,m)` for every `N>=3` and even `m>=4`, using the
audited Ben-Itzhak--Teicher classification and explicit realization of every
needed rewrite by a positive-probability kernel transition.

## Convention and target

Permutations are maps on `[N]`; `pq` means `p` after `q`, so
`(pq)(x)=p(q(x))`. Words evaluate to `t_1...t_m`. The target is global
uniform on `Omega(N,m)`, and the exact lazy kernel and random-scan
normalization are those in the run manifest.

## Proof obligations

1. Translate the cited Hurwitz generator to the project generator.
2. Show every adjacent Hurwitz or inverse-Hurwitz rewrite is contained in a
   length-three exact heat bath, including boundary pairs.
3. Put every identity word into an adjacent-square representative with the
   same labeled weighted support-component data.
4. Show every adjacent square refresh is contained in a length-four exact
   heat bath, including `m=4` and boundary pairs.
5. Connect every state to one universal square word and audit exceptional
   cases.

## Expected failure modes

- silently omitting isolated labeled vertices from the classification;
- assuming a square already exists without first using Classification H;
- overlooking the last adjacent pair in the padded-Hurwitz realization;
- treating reachability as a quantitative gap or congestion bound.
