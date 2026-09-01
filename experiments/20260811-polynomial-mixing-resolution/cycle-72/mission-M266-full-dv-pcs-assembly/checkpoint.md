# Mission M266 Checkpoint

Status: substantive assembly complete; checker passed; payload frozen for a
fresh immutable audit.

All fourteen named M192/M195, M217/M222, M248/M249, M251/M255,
M252/M253, M256/M259, and M258/M263 inventories pass `sha256sum -c`.
Their checksum-file digests are recorded in `dependency_manifest.md`.

The observable and domain interfaces align exactly.  In the notation that
avoids reusing `D`, the exterior length is `L=2k-1`, the cutoff is
`2<=ell<=m=(3k-1)/2`, and the adjacent-rank sum is `1<=s<=k-2`, uniformly
for odd `k>=3`.  Both M251 and M258 use the same normalized literal
ordered-disjoint-double B profile and the exact identity

```text
Phi_s(X_ell)=Phi_s(Y_ell)+Theta_s(ell).
```

Therefore `18400+500=18900` proves full DV for both observables.  Substitution
into M252/M253 and M256/M259 gives

```text
K_J=18900 K_E+7185,
C_W=18K_1+9K_2+340200K_E+129330.
```

The deterministic checker passed 1,000 odd ranks through `k=2001`,
1,501,500 cutoff instances, exact channel-mass normalization, and the full
`k=3` boundary table.  These are arithmetic/domain falsification checks, not
the proof of the predecessor inequalities.

The accepted downstream chain ends unconditionally at PCS-bound in this
auxiliary fixed-cell model.  FD-bound, or the alternative minority-sign
estimate, remains independent; no PCR, FCL1, gap, mixing, or Terminal follows.

