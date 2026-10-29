# C1-v1 runtime erratum v1

The general finite-family random-bit estimate in candidate-1-v1.md needs a log L term for selecting Hurwitz positions: expected O(L log N + s log L + s) unbiased bits, under exact rejection sampling. The written O((L+s)log N) is valid on the concrete polynomial schedule, where log L=O(log N), but not for arbitrary unrelated N and L. No sampler law, identity proof, entropy lower bound, attack, or schedule changes. Reviewers should read C1-v1 together with this erratum. Candidate status is not upgraded by this correction.
