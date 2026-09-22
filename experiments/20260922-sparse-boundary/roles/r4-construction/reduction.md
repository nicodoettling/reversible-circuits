# Remaining connected primitive after QC.v1

Status: proved reduction; availability of its primitive remains unresolved.
This is separate from any claim that H0, H1, or H2 succeeds at T0.

For N>=2, even m, keep the frozen top-level P,K and new L from QC.v1.
The exact global least-label macro law already has polynomial counting and
positive conditional choices. Genus0/1 components have the imported exact
connected sampler. QC.v1 adds exact decoding for every genus on v<=L.
Thus the only local inputs not covered by these constructions are

    L < v <= min(N,m/2+1),
    ell=2v-2+2g <= m,  g>=2.

A sufficient remaining primitive is one uniform algorithm which, on these
inputs and b>=1, returns a literal connected identity word on [v], of exact
length ell and product identity, within TV2^(-b) of its uniform connected
law, in expected bit time poly(N,m,b), with one fixed polynomial.
Its behavior on zero-count inputs must reject rather than normalize zero.
An exact version would eliminate b. No scalar connected count is being
substituted for this task.

Given that primitive, sample the unrestricted global macro exactly by the
positive count/assembly tables. Invoke the exact old or QC decoders where
available and the primitive otherwise. For each realized macro, couple
each approximate component output to its exact uniform connected target.
There are at most N components, so the union bound on these coupling
failures gives conditional TV<=N2^(-b). Averaging over the EXACT same
macro law leaves this bound unchanged. This is a valid finite sum of
conditional coupling errors; it does not multiply unconditional success
probabilities or discard a posterior normalizer.

For example, choose b=(ceil(log2(N+2)))^2. Then
N2^(-b) is negligible in N, with one fixed b-selection and a fixed
polynomial expected runtime. At most N calls occur, so sum of their
conditional expected costs remains polynomial provided the primitive
bound is uniform over all allowed inputs. The whole word always has
identity endpoint and the requested length, even on a coupling failure.

This reduction removes scalar counting, exact macro sampling, literal
interleavings, isolates, all low-genus components, and all support sizes
through Theta(logP) from the missing problem. It is stricter than the older
v>K,g>=2 reduction but still sufficient rather than necessary: a sampler
may ignore components whose total exact omitted mass is negligible, or use
a different global mechanism. It proves neither hardness nor absence of
another sampler.
