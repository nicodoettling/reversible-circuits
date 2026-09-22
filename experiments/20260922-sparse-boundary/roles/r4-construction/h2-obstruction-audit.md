# R4 nonauthor audit of R2-O2.v1

Verdict: ACCEPT the stated H2 support obstruction, with the imported uniform
factorial genus majorant as the same dependency explicitly used in R2-O1.
This review reads the full current corollary and its R2-O1 numerator and
denominator proofs. Exact reviewed hashes are in
h2-obstruction-audit-inputs.json. R4 authored the H2 policy/decoder but did
not author the obstruction proof; this is correlated same-model review.

The extension from K to an arbitrary fixed J uses only b_J*x<=1 in the
R2 numerator. All genus0/1 components remain present, while every genus
on v<=J is bounded by exp(b_J*x). Thus it does not recycle the invalid
old genus<=1-only obstruction or discard high genus on small support.
The support size condition D subset A_L is correct even though H2 need
not contain original H0.

On N=2^(8j),m=2^(6j), P<=2N and 2^L<=3^L<=P^4 give L<=32j+4.
Then b_L*x <=(32j+4)^3/(72*2^(10j)). Its j1 value is
46656/73728<1 and consecutive ratio is <8/1024, so the generalized
numerator holds for all j>=1. The other numerator conditions q<=1/2,
x<=1 do not depend on cutoff. The fixed-j64 denominator comparison in
R2-O1 is unchanged, including r=floor(m/(6j)), r!<=2^m and the safe
constant2^18. Its final inequality2^18*j^2<=2^(j/2) holds at64 and stays
true because the consecutive relative ratio increases.

The resulting |D|/Z<=2^(-1-jm/2), j>=64, is therefore valid. Testing the
omitted-set event gives TV>=1-|D|/Z for every law supported on D; it does
not assume the proposed QC decoder is correct. The same bound covers the
hybrid A_L including all genus0/1 components. T0 existence remains open.

This closes QC.v1's missing benchmark mass statement NEGATIVELY: a
logarithmic support cutoff does not rescue T0, even with all low-genus
components added. It does not invalidate the quotient-state sufficiency,
literal decoder, or polynomial exact restricted-law construction. Keep
that construction only as an exact primitive improvement and preserve this
negative conclusion beside it.
