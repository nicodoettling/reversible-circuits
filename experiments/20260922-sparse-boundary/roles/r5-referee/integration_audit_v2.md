# Final exact-version integration audit — RF-INT.v2

**Disposition: ACCEPT the canonical obstruction and smaller positive extension in the exact versions below, with the explicitly named published and imported decoder dependencies.** This is internal same-model review, not external human certification. The original full-range H0/H1 negligible-error claims remain refuted, and another polynomial-time sampler for the entire benchmark remains unresolved.

## Exact accepted inputs

| Artifact | SHA256 |
|---|---|
| root obstruction.md, SB-O1.v1 | bf7b3bed9f0616816e92bfc0c37527c8617abef8c525d15940d9c21b7aa40894 |
| root proof.md, SB-T1.v1, integration v2 | 3a54f12e4d172cfdfc5ef6f8e7b84c067e86eba8d10a2f387496ff7bd435d611 |
| root source_checks.md | 7940610828041f50b7ff94ae339114f1e874d31fac15ebf66c29c12c53fb9337 |
| R4 algorithm-audit.md as received | fcf6abeda1578f961248b2ea494b0723a1701d973ee35972c6cad96d64b3981c |
| unchanged sampler-v4.py | cdb91799b02539190bc31ce7d6fe31ee5af0477b1cc653f43452eb18de734002 |
| unchanged sparse-global sample.py wrapper | 2d74da262e4c53005a05d4f171b85c5469ade520e38b91b1b0df14f4cbe8386e |

Review copies, origin paths and copy timestamps are in integration_inputs_v1.json and integration_inputs_v2.json. The first canonical positive-proof snapshot b55b299fd1331d2ce0d5dcb44930cdf8d9f483e4352c8bc7d6aaecae92ecdff1 is preserved; this report accepts its revised successor rather than silently inheriting its version.

## Mathematical checks retained and closed

candidate_audit_v1.md gives the detailed nonauthor reconstruction. I rederived the DYZ convex recurrence and factorial genus majorant from the primary source, reconstructed the pair-insertion incidence bound under the exact bridge normalizer, and checked both the boundary obstruction and the new positive-range constants. These arguments are deterministic count comparisons, with no independent-edge transfer, unproved sequential product estimate, or vacuous-upper-bound-to-lower-bound inference.

The canonical obstruction preserves R2-O1's proof and yields

    Z_A/Z <= 2^(-1-jm/2)

at N=2^(8j), m=2^(6j), every integer j>=64. Since B subset A, both original errors tend to one.

The positive theorem preserves UPPER.v2's statistical proof, with S explicitly defined and integer J specified. It proves a common negligible error

    exp[-(ln N)^2/(48lnln N)]

for N>=2^2048 and even m<=N^(2/3)ln N/4, with eta=1 below that N threshold. The all-even-length exact restricted-law algorithms and their expected O((N+m+2)^20) bit-time and O((N+m+2)^10) storage envelope are separate inputs. I read the original R3 proof, direct dispatch/count/assembly code and R4's current dependency audit. The state includes actual permutation, exposed support partition, and remaining length; K remains fixed at the original input. The length factor in memory and bit lengths is retained. The independently fair-bit model is explicit; seeded PRNG execution is explicitly diagnostic only.

The H0-only genus-zero/one decoder remains the named September7 S1.v2 theorem with its fixed-endpoint counting/positive-allocation proof and source checks. R4 reviewed that frozen interface and code; I do not claim to have freshly reaudited every line of that historical implementation or its earlier source audit. H1 avoids this nontrivial decoder dependency. The present integration introduces no new hypothesis beyond these exposed inputs, and R4 confirms their algorithmic validity does not require the earlier sparse length range.

## Fresh repair check

The only diff between canonical positive-proof integration v1 and v2 is the Section 6 dispatch paragraph. I compared the exact revised bytes with sampler-v4.py's connected_sample:

- v=1 returns the empty connected component.
- Under H0, genus<=1 calls g01.sample for every eligible degree, including v<=K.
- Otherwise the policy requires v<=K and calls MarkedCounter.
- Under H1, every nontrivial component takes the MarkedCounter branch.

The revised paragraph states those choices exactly. It changes no sampler, target set, cutoff, error bound, runtime argument or source dependency. The earlier misleading reading is recorded in candidate_audit_v1.md and the preserved integration snapshot; it is not erased. No repair remains pending in this referee's integration scope.

## Evidence and limitations

Fresh exact tests are in finite_checks.py/json and candidate_checks.py/json. The latter checks 370 normalizer-ratio cells, 190 finite-genus sums, 10 genus-majorant cells and 31 normalized-series coefficients, using a separately written exact support/permutation DP and component assembly. All pass. They check normalization and finite regressions; the displayed all-parameter theorems rely on the proofs.

The immutable blind report has SHA256 76a35688d44c08b39c221778efa1b7a395d7b4bc9e9cc608a68c31b1e3fce22d. Its independently derived, stronger all-m_*(N) asymptotic obstruction is retained separately and is not silently substituted into the canonical theorem.

This acceptance does not prove local heat-bath mixing, a polynomial bound in log N wires, practical performance at enormous parameter values, or computational hardness. It accepts exactly the count obstruction and the separately smaller global-sampling theorem under the stated arithmetic/randomness model and identified literature/decoder inputs.
