# r3 adversarial exact diagnostic plan

Objective: examine C1-v1's complete noisy-word law against M0's identical channel on global U(4,6), while preserving the already frozen blind attack reports. This tests implementation and finite effects; it is not an asymptotic security experiment.

Parameters: N=4,L=6, C1 signed Hurwitz steps s=0,1,2, all k=0,...,6. Each source is exactly enumerated with integer tape multiplicities. All 6^6=46656 literal output words are retained. The global bridge has 3936 words; the unscrumbled C1 has 24 distinct words. Source totals are 24*10^s. Products act rightmost first.

Noise: Q_k chooses a uniform k-subset and iid uniform gates, allowing equality to old values, with positions hidden. Compute all k via the coefficient of product_i(Id+z E_i), where E_i sums the source mass over old coordinate i and broadcasts to every replacement value. Normalize by source_total*binom(L,k)*6^k. This exactly marginalizes noise; it is not Bernoulli replacement. Cross-check k=1 against separate literal replacement enumeration. Validate k=0 and k=L and total mass for every k.

Predeclared diagnostics: all six edges distinct; distinct-edge count; gate-word support size and component count including isolates; adjacent repeats; first-three, first-four and middle-four product cycle types; endpoint cycle type; per-position edge marginals; complete-word TV. TV is an exact descriptive optimum in this finite space and must not be advertised as a held-out attack. These features were selected before results. The schedule in C1-v1 has many blocks and is not simulated by this tiny single-block case.

Boundary responsibility: coordinator runs inherited S3L4/S4L4/S4L6 global count and projection regressions, N2,L0,L2, odd rejection, endpoint/pair controls and CP1. C1 is not defined at S3L4 or S4L4; do not invent a fallback construction. This script additionally checks the applicable k endpoints.

Resource request: one coordinator-reserved process, 1GiB address-space limit, 120-second timeout, expected memory below 256MiB. Script `exact_c1.py`, unique output `exact-c1-results-v1.json`. No dependencies and no random seed, because all probabilities are exact. Record Python, actual commit, exact command, helper manifest and timing. On timeout or resource failure, retain the failure, do not execute unbounded, and narrow the check only by a separately reserved new version.

Interpretation rule: reject a finite candidate instance if a predeclared diagnostic differs, but quantify the effect exactly. Do not infer an asymptotic attack from these finite values; B1/BS1/BS2 provide separate symbolic arguments. A zero diagnostic gap is not evidence of computational security. Preserve all negative or minority findings.
