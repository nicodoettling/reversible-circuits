# Blind supplement BS1: C1-v1 and LC1

Frozen 2026-10-29 after B1, before any r1 proof/status, r2 analysis, or coordinator proposed proof/status was read. Exact additional inputs: `r2-construction/candidate-1-v1.md` and `coordinator/local-channel-statement-v1.md`, supplied as algorithm-only and statement-only documents. B1 and the earlier primary inputs remain the full input list. No new mathematical computation has been executed. Review is same-model correlated. New arguments below remain provisional pending finite regression and exact-version reconciliation.

## LC1: independently reconstructed proof

Write E_i for averaging coordinate i over the uniform alphabet while leaving the other s-1 coordinates fixed. These commuting projections obey E_i^2=E_i. For J subset [s], define

    f_J = (product_(i in J)(Id-E_i)) (product_(i not in J)E_i) f.

Then f=sum_J f_J, E_i f_J=0 for i in J, and E_i f_J=f_J otherwise. If T is the exact M0 channel on the s observed coordinates, then

    T f_J = alpha_|J| f_J,
    alpha_j = binom(L-j,k)/binom(L,k) = (L-k)_j/(L)_j.

Indeed, averaging any replaced coordinate in J kills the component; if no coordinate in J is replaced, replacement averages on all other coordinates leave it unchanged. The probability of avoiding J is exactly alpha_|J|. This argument uses the joint without-replacement law, not a product of marginal survival probabilities.

Because k<=L-s, all alpha_j are positive and alpha_j>=alpha_s. Set

    g = sum_J f_J/alpha_|J|,
    h = 1/2 + alpha_s*g/(2*3^s).

The expansion of product_(i in J)(Id-E_i) has 2^|J| terms, each bounded in absolute value by one, hence ||f_J||_infinity<=2^|J|. Therefore ||g||_infinity<=3^s/alpha_s and h lies in [0,1]. Moreover T g=f, so

    E_(Q_k P)[h]-E_(Q_k R)[h]
      = alpha_s/(2*3^s) * (E_P[f]-E_R[f]).

This is the exact claimed oriented difference. No independence within either source is used. The inverse is a linear function on observables, not a positive source-reconstruction kernel; adding and scaling is essential.

For computation, expand each f_J into coordinate averages. Direct enumeration uses at most

    sum_(J subset [s]) sum_(K subset J) q^(s-|K|)
      = (1+2q)^s <= (3q)^s <= 4^s q^s

evaluations of f at most, with considerable reuse available. Calculate alpha_j via falling factorials of length j, avoiding enormous binomials: their numerators/denominators have O(s log L) bits. Rational additions have costs polynomial in the complete rational input/output representation and number of evaluated terms. Any complexity formulation with only log q,log L and s as input size must retain the explicit exponential-in-s q^s cost; the statement does. Exact rational Bernoulli sampling has finite expected bit cost, with no finite worst-case tape bound.

For fixed s and k/L<=1-c, once L>=2s/c each factor (L-k-i)/(L-i) is >=c/2, so alpha_s>=(c/2)^s. Thus an inverse-polynomial original bias transfers to inverse-polynomial noisy bias for an explicit polynomial schedule. The local test f must be available from public A; choosing it after seeing hidden K is not licensed. Conditional application to public setup is valid pointwise when the stated source/noise independence holds.

### LC1 boundary/falsification checklist

- q=1: all source differences vanish, with only the constant component surviving.
- k=0: alpha_j=1 and T=Id; the displayed h works directly.
- s=L: admissible k is only zero.
- k=L-s: alpha_s=1/binom(L,s)>0, so inversion is valid; for fixed s it is inverse polynomial in L.
- k>L-s: alpha_s=0. A nonzero pure degree-s component is erased; extending the theorem with a positive coefficient would be false. For example q=2,s=L=1,k=1 erases a biased bit entirely.
- Ordered I may be any deterministic distinct-coordinate order. The channel calculation uses positions, not group structure.
- Marginal-survival multiplication is unnecessary. The cached-prefix regression's unsupported product inference is not used: alpha_j is counted directly under one fixed uniform subset.

Verdict on statement LC1: **provisionally proved by an independent blind derivation**, subject to the requested exact finite channel checks and later exact-version review; no computational hardness or universal attack follows.

## C1-v1: independent algorithm assessment

The block is `(ac),(cd),(ab),(ad),(bc),(bd)` on four distinct labels. Under rightmost-first multiplication, the first triple maps a->b->c->d->a and the last triple maps a->d->c->b->a. Thus the six-gate product is identity. The six edges are distinct. Each listed Hurwitz map preserves the pair product by direct cancellation. The labeling map is injective as stated: c is the intersection of gates 1 and 2, then a,b,d are recovered from gates 1,3,2 respectively. The entropy claim is a lower bound, not a security statement.

Apply B1.1 to the B designated six-gate windows. For every tape, after s adjacent Hurwitz moves and k replacements,

    X(observed) >= B-2s-k,

where X counts designated windows with identity product. Whenever t=B-2s-k>0, the test X>=t has structured probability one and reference probability at most min(1,B beta(N,6B,k,6)/t). This is a six-gate relation attack, independent of within-block gate-equality controls. It is polynomial time in the full explicit word length and N. The implementation may multiply six sparse transpositions without constructing full permutation tables, but no speed optimization is needed for polynomiality.

For the declared schedule N=lambda^2, B=lambda^6, s=floor(B/10), k=lambda, lambda>=2, t>=4B/5-lambda>0. If the long-completion relative mixing error epsilon_lambda on lengths L-6,...,L is negligible (a separately checked random-transposition estimate), then B1 yields

    advantage >= 1 - [B/t]*(1/binom(lambda^2,2)+epsilon_lambda/(1-epsilon_lambda)).

This tends to one. The first unproved imported step in this asymptotic route is the stated parity-relative mixing estimate at L-6=6lambda^6-6; exact finite beta gives the attack bound without that import. No claim about every sampler follows.

The B=1,k=0,s=0 boundary is deliberately instructive: the block-identity statistic is the full product, so the reference also always passes and the bound is vacuous. This does not invalidate the large-B attack. For N=4,L=6,s=0, the candidate's 24 distinct label-tuple words form a strict subset of the 3936 global bridges; their exact noiseless TV is 1-24/3936=163/164, and all-six-edges-distinct is a natural candidate-specific predeclared diagnostic. The exact count 24 depends on the injectivity just checked; the inherited bridge count is separately slated for coordinator regression. Noise and additional s need full matched enumeration rather than extrapolating this support ratio.

There is no hidden K in C1-v1. Reused-setup replies are independent under each exposed A, so ordinary amplification of this fixed one-sample attack does not face an unobserved-key mixture. The schedule's semantic error bound 4/lambda is not negligible, as the candidate correctly says.

## Proposed exact diagnostics (not yet run)

Use N=4,L=6 and s=0,1,2 as finite C1-v1 parameter cases, and enumerate the exact full noisy distributions for every k=0,...,6. The primary asymptotic schedule has far larger B; these small cases are falsification checks, not samples on that schedule. Predeclare all-six-edges-distinct, number of distinct edges, support size/components, adjacent repeats, prefix product cycle type, coordinate edge marginals, and full-word TV. The TV-maximizing event is a descriptive finite diagnostic, not a held-out attack. Validate global counts and noise endpoints separately; do not instantiate C1 outside N>=4,L divisible by six.
