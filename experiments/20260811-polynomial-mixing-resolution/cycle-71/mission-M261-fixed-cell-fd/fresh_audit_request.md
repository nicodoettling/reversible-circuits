# Fresh audit request for M261

Please audit the frozen M261 package independently and do not modify it.

Priority checks:

1. verify all eight predecessor checksum ledgers and the recorded M166
   nonmaterial freeze-hash correction;
2. reconstruct the fixed-lag completion ratio in Proposition 1, including
   same-component and ordered cross-component coefficients;
3. verify the cyclic endpoint identity and the sign/index convention in
   `E_ell`;
4. verify the exact raw-to-two-channel normalization and that triangle/double
   kinds remain inside the final absolute value;
5. check `FD-bound <=> (PBV)`, especially
   `Lambda_n=(n-2)(1-2/n)^(-(n-3))` and the resulting `Theta(n)` factor;
6. audit the pointwise affine collision decomposition and its use of the
   accepted kind transfer;
7. rerun the smallest exact checker case before inspecting frozen output.

The intended verdict is only a strict exact reduction. FD-bound, the
minority-sign substitute, FCL1, every gap/mixing claim, and both Terminals
remain unresolved.

