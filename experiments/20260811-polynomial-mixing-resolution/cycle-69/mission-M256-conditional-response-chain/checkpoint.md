# M256 Checkpoint

Status: halfway checkpoint; the exact chain has been reconstructed.

The source-of-truth documents and project skill have been read. Every entry
in each complete frozen inventory for M168/M171, M174/M178, M180/M182,
M186/M189, M192/M195, M217/M222, M235/M238, M239/M246, M248/M249, and
M252/M253 passes `sha256sum -c`. Directory listings contain no unlisted
regular payload except each inventory file itself; M189 also contains only a
generated `__pycache__` directory outside its payload.

The implication chain is licensed through `(PCS-bound)`, conditional on full
`(DV)`:

```text
DV + accepted DE
  => full WPCR                    (M252/M253)
  => SCBR                         (M186/M189, including M_1(1) and endpoint)
  => n eta(Q)=O(1) => BR          (M180/M182, including large-d tail/remainder)
  => PCS-bound                    (M174/M178, including affine kind transfer)
  => the PCS term in TV-close     (M168/M171).
```

The chain stops there. `(FD-bound)` is a separate hypothesis in M168's
deterministic closure and is still required (or must be replaced by M168's
minority-sign-mass alternative) to prove `FCL1` and the equivalent first-cell
quantity `A_k(1,1)=O(1)`. Full PCR and its unresolved J1-PCR refinement are
not needed for this weighted route.

Normalization checks retained for the final proof: `n=3k`, odd `k>=3`,
`m=(n-1)/2=floor(n/2)`; M168's temporary sequence length `N=n-3=3k-3`
is unrelated to the ambient symmetric-group parameter called `N` elsewhere
in the project. The singleton `M_1(1)=O(1/n)`, the Abel endpoint at `m`,
the M192 unequal-mass endpoint, M180's bounded response remainder, and
M174's explicit affine kind term all survive the chain.
