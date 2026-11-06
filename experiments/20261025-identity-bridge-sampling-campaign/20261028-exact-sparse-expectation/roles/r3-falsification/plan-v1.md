# I2 R3 falsification plan v1

Frozen2026-10-28, base92af1b7b47583b60571a84c660d527422ce0e8ce. Target law: full uniform fixed-length transposition identity bridge on[N], canonical labels and ordered positions, rightmost-first maps, independent fair bits. No Markov kernel. Primary ES.v1 asks exact expected-polynomial sampling on m³<=N²; separately admitted ES-LOG.v1 asks m<=N^(2/3)ln(N)/4. Neither implies an all-length theorem.

## Frozen tests and obligations

1. For a9, define H_a(w)=sum over nontrivial support components B of a^|B|. Independently compute E_U H_a from exact bivariate labeled assembly and from literal product/support dynamic programming. Test the exact marked-component formula and rational finite genus bound under D=N-m+1>0. Never replace the bridge normalizer by an unconditioned support model.
2. Verify the finite moment implication: if E X_v<=N c rho^(v-1)/v³ and a*rho<=1/2, then E H_a<=Nc*a/8. This is a sum of unconditional expectations under the full exact macro law, not a product of adaptive marginals. Check the G=any high-genus components and additive versus maximum cost distinction.
3. Attack actual cost accounting: selected-only decoder initialization, transitions and lookups, per-component versus shared cache, fair-bit draws, output-position work, zero-mass branches. The proposed a9 envelope must dominate actual bit work apart from one fixed polynomial in originalN,m. A state inventory alone is insufficient.
4. Finite-degree exceptions must use the same uniform exact algorithm and an explicit finite constant; reject any unrecorded table, accuracy-dependent exponent or omitted input. Both primary/log ranges must remain distinct on smallN.
5. Classify limitations outside sparse regimes. A divergent sufficient moment envelope is not a lower bound on actual optimized decoder work and not a refutation of the mission. Any additional asymptotic claim will be frozen separately before proof.

## Intended bounded finite job (not authorized yet)

DYZ normalized counts for support v<=13 and even length<=24; bivariate exponential component-assembly table indexed by support s<=24 and half-length k<=12; exact weighted moments a3,a9. Literal independent product/support/length DP for N2..5,m0..12, state estimate below10000 and512MiB. Evaluate normalized moment/marking and finite rational upper bounds at selected N through1024 plus huge-degree symbolic evaluations N=2^36 and2^2400 at bounded m, avoiding enumeration of those groups. Deterministic seed0 unused, Python standard library, timeout180s/address1GiB proposed. Detailed output unique JSON; one short console summary. Send exact final command/resources and await coordinator reservation before running.

Historical regressions remain: odd/zero/two,N2,singleton positive genus,minimal lengths,81-versus80,(ab)^3,unweighted graph bias,cut multiplicities,fixed42/12->5/12 cutoff witness,H0/H1/H2 support failures and CP1. No new implementation is owned by this role; new production laws are R2/coordinator's obligation. This role provides independent exact moments/normalizers, not a surrogate sampler test.

Source obligations read: canonical20260922-sparse-global-sampler/proof.md Sections1–6 and8–10; canonical20260922-sparse-boundary/proof.md finite-genus/logarithmic tail; QC roles/r4-construction/proof-v1.md; actual audit path20260922-sparse-boundary/construction_audit.md. Their existing statuses are not upgraded here.
