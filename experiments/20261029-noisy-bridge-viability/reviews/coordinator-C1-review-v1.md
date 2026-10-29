# Coordinator exact-version review of C1-v1

Author-distinct, nonblind review; the coordinator has seen theory and construction messages. Same-model review is correlated. Inputs are frozen by hashes below. Verdict: **proof checks analytically; implementation gate remains pending**. No claim is promoted here.

## Exact inputs

- r2-construction/candidate-1-v1.md SHA256 e0462d7037134a0cc7c7a8b247fdb35ef3b8dbc5520ec696c2dbf7088549bd38
- r2-construction/candidate-1-runtime-erratum-v1.md SHA256 c86627c091dc2951810bd00e9250454dd82e0a37322ce181243ff748f45bd40f
- r2-construction/candidate-1-rejection-v1.md SHA256 62fe7255f50df888075d7159bf4b6c8d3e04f6d0768d796385d64b86856541ce

## Identity, quantifiers and source matching

Direct label tracing confirms (ac)(cd)(ab) maps a->b->c->d->a, and (ad)(bc)(bd) is its inverse. Each block has six distinct edges, so this is beyond the repeated-edge, adjacent-doubled, or mirrored-word controls. A fixed Hurwitz tape is invertible and preserves total identity, and conditional entropy is B log((N)_4); unconditional entropy is at least that conditional value. No endpoint randomness is used as word security. Setup contains only public parameters, so one-sample and reused-setup average/every-key distinctions collapse; one reply already suffices.

The general finite-family random-bit claim was false as originally written when L and N are unrelated: selecting one of L-1 positions costs log L bits. The immutable erratum correctly gives O(L log N+s log L+s) expected bits. The concrete schedule still has log L=O(log N), and sampler law and attack proof do not change. The original faulty complexity text is retained; downstream interpretation must include the erratum. The law is exact under expected-time rejection sampling, not claimed to use a bounded finite bit tape for arbitrary denominators.

## Attack proof rederivation

Let a=ceil(B/2). Deterministically, touching at most two aligned blocks per scrambling move and at most one per replacement leaves X>=B-2s-k. For lambda>=2, B=lambda^6, s=floor(B/10), k=lambda imply X>=.8B-lambda>=ceil(B/2); the worst endpoint lambda=2 has B=64,s=6,X>=50 and threshold32. A one-query threshold test thus accepts every candidate tape, not just an average subset choice.

For V iid mu and F={product V=id}, the joint (V,noise) conditioned on F is exactly (U,fresh independent noise). Consequently Pr[E(Q_k U)]<=Pr[E(Q_k V)]/Pr[F]. Independence of the noise from F is essential and explicitly present in M0. Conditional on every replacement subset, Q_k V remains a product of uniform gates; hence its unconditional full law remains iid. Fixed disjoint windows are independent ONLY in this unconditioned measure. Their null-product probability p6 is <=1/q; alternatively expose the first five gates, and there is at most one final transposition completing identity. Union bound over a-subsets gives binom(B,a)q^-a. For even L, symmetry plus Cauchy--Schwarz gives p_L(id)=sum_g p_(L/2)(g)^2>=1/N!. These identities prove the finite bound exactly. No product of conditional window-survival marginals occurs.

For lambda>=4, q>=lambda^4/4 and N!<=N^N give log R<=2lambda^2 log lambda-2lambda^6 log lambda+2lambda^6 log2<=-(lambda^6/2)log lambda. Thus the stated exp(-Omega(lambda^6 log lambda)) false-positive bound is justified by explicit elementary inequalities. This is a proof, not inference from finite runs.

## Falsification attempts and boundary scope

k=L makes both laws iid and violates the deterministic useful-threshold premise. Heavy scrambling likewise can destroy that premise. At N=2, L=0, L=2 the candidate is not defined; no generalized rejection is asserted. Using unrestricted iid words as the final reference would be invalid; the proof pays the bridge-conditioning probability explicitly. The universal inequalities may be vacuous at small parameters, but the C1 schedule satisfies their useful premise. Every source sample remains identity before noise, even when relator blocks share labels.

Remaining gates: exact implementation checks, r3 frozen blind/nonblind report, coordinator reconciliation with complete claim graph. This review does not certify any cryptographic hardness or reject arbitrary structured samplers.
