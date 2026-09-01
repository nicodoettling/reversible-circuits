# Fresh audit request for M266

Please audit M266 as an immutable assembly, without reusing its prose as a
proof source.

Required checks:

1. Verify every M266 checksum and the fourteen predecessor checksum-file
   digests in `dependency_manifest.md`.
2. Check that M251/M255 `Y-DV` and M258/M263 TAV use exactly the same
   normalized B profile, observables, odd-`k` range, cutoff range, and
   adjacent-rank range, and that `X-Y=Theta` is literal.
3. Check the direct full-DV constant `18400+500=18900`.
4. Check the substitutions
   `K_J=18900K_E+7185` and
   `C_W=18K_1+9K_2+340200K_E+129330`.
5. Verify channel masses, `J=0` cancellation, the singleton, cutoff
   endpoints, `k=3`, and odd-`n` handling.
6. Trace only the already accepted M256/M259 implications through
   PCS-bound.  Reject any inference of PCR, FCL1, a bridge gap, mixing, or a
   Terminal.
7. Confirm the corrected M166 freeze-manifest hash and treat M256's old value
   as a nonmaterial provenance typo.

The requested verdict is `ACCEPT`, `REVISE`, or `REJECT`, with numbered
material and nonmaterial objections.  If accepted, freeze the audit and
leave FD-bound/minority-sign as the exact next stop.

