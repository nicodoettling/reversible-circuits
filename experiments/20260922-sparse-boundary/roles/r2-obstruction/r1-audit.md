# Nonauthor audit of R1 UPPER.v2

Reviewer: /root/r2_obstruction. Exact reviewed proof:
roles/r1-upper/proof-v2.md, SHA256
`b76f706aad3dae20ed3550298b98bd260b295f7cc9752eb3f1ecef663c87ac3c`.
Complete input copied to r1-proof-v2.input.md. The old counting/marking
inputs were read separately. This is correlated same-model internal review.

Verdict: **ACCEPT the new mathematical upper bound and explicit accuracy
range**, conditional only on the listed imported count/marking and exact
algorithm dependencies being closed by the coordinator. No additional
unproved inequality or normalization assumption was found. I do not audit
the decoder implementation in this report; R4 owns that obligation.

The finite identity is valid term by term. With h=k-v+1 and
q=v-1+g, the falling factorial splits as
(k)_q=(k)_(v-1)(h)_g. Multiplying the factorial genus bound and summing
g=0..h gives exactly(1+4b_v/D^2)^h by the binomial theorem. The H0
subtraction removes precisely g0 and g1, and is zero at h0,1. The exact
bridge denominator remains present in the inherited incidence inequality;
no independent support-graph law or sequential product estimate is used.

The new real-variable comparison is valid for every s>=0:
1+s^3<=(1+s)^3 and log(1+s)<=s. With
s=v/(9D^2)^(1/3), it bounds the finite genus factor by exp(z_new v),
where z_new=3k/(9D^2)^(1/3). Combining falling-factorial and binomial
bounds yields exactly the stated N c_new rho_new^(v-1)/v^3 and the
geometric tail. No infinite all-genus/all-size series is evaluated.

For the explicit range m<=N^(2/3)ln(N)/4, N>=2^2048:

- L=ln N>1000 and L<=exp(L/3), so m<=N/4 and D>=3N/4.
- The cube of3/[2(81/16)^(1/3)] is2/3<1, proving
  z_new<=m/N^(2/3)<=L/4 with the displayed constants.
- Nx<=32m/(9N)<4m/N<=L exp(-L/3), and
  1+ln L<=L/24, hence ln rho_new<=-L/24.
- The existing fixed cutoff satisfies K>=L/ln L. Therefore the tail is
  at most2e exp(5L/4-L^2/(24ln L)).
- Since L/(48ln L)>3 for L>=1000, this is at most
  exp(-L^2/(48ln L)). Its negligible threshold for each fixed a is
  explicit and does not alter algorithm parameters or runtime exponents.

The improved rising-factorial denominator is also correct. A base has
I>=D+2q-1 isolated labels, so its ordered fresh-label count satisfies
(I)_(2q)>=D(D+1)...(D+2q-1). The same reverse incidence multiplicity
binom(k,q) applies. Zero residual bridge counts and q0 are harmless.

Independent exact falsification passed with the hash-checked old count
routine:3850 individual genus and rising-factorial comparisons,1045 exact
finite-binomial identities,409 near-minimal H0 zero cases. Domain:
2<=N<=32, even2<=m<=min(N,20), every feasible v,g. Script and raw output
are check_r1_upper.py and r1-upper-results.json. Runtime under0.1s;
standard-library rational arithmetic, no seed or stochastic conclusion.

The old-tail log^(1/3) range is correctly labeled an algebraic corollary.
The new log N range uses the finite binomial summation and is strictly
larger asymptotically. Neither establishes the full m^4<=N^3 benchmark.
This acceptance must not be inherited by edited proofs without recheck.
