# M98 plan: exact reset-defect sign

Date: 2026-08-12. Frozen predecessor base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and exact scope

This mission concerns only the full nonlazy stationary-flow parking-degree
projection `Pbar_r` in the minimal long-cycle factorization sector. It does
not concern the original lazy `{3,4,5}` same-product heat-bath kernel on
identity words. Permutations compose as `(pq)(x)=p(q(x))`; displayed factors
multiply left-to-right.

For a reachable context `x=(s,K,R,B)`, retain every attachment rank
`j=1,...,k` and M90's transformed quantities

```text
Q(x,y)=rho_s(k,t) nu_(K,R,k)(j),
U(x)=q_x(1-q_x)K/(R+1),
A(x)=sum_e [theta_e^2/Q_G(e)](1-q_(y_e)),
r_U(x)=U(x)-A(x)-Q U(x).
```

The primary exact targets are to prove or refute

```text
(A) r_U(x)>=0 for every reachable nonfresh K>R>=1;
(B) r_U(x)+Q r_U(x)>=0 for every fresh (K,R)=(1,0).
```

Together with strict phase descent these imply the accepted weighted reset
supersolution. A stronger unweighted statement will be pursued only if a
genuine global excursion construction is supplied; `q(1-q)` will not be
called a Bernoulli variance without an identified random variable.

## Method and falsification rules

1. Independently derive the all-`j` beta-binomial sum entering `QU`, and the
   Cayley-grouped canonical-basin formula entering `A`.
2. Test monotonicity in `(K,R)`, especially reduction to the minimal
   nonfresh context `(2,1)`, using exact rational arithmetic before making
   any asymptotic claim.
3. Seek a closed Borel/Cayley coefficient identity, TP2 comparison, or
   boundary-layer telescoping proof. If a sign fails, freeze the smallest
   exact witness and seek an infinite family.
4. Reproduce independently the accepted negative local-variance and scalar
   compensator witnesses; they remain refutations and are not reused as
   proof assumptions.
5. Treat every bounded scan as a falsifier only. Freeze a halfway checkpoint,
   machine-readable raw output, a nine-field report, hashes, and cache/status
   checks in this owned directory.

All computations are deterministic (`seed=null`) and use Python with `-B`.
